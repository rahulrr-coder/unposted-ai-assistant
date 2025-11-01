"""
Todo API endpoints - CRUD operations for todos table
"""
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from app.models.schemas import TodoCreate, TodoUpdate, TodoResponse
from app.database import db
from app.api.auth import get_current_user
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/todos", tags=["todos"])


@router.get("/", response_model=List[TodoResponse])
async def get_todos(
    status: Optional[str] = None,
    priority: Optional[str] = None,
    current_user: dict = Depends(get_current_user)
):
    """
    Get all todos for the current user.
    
    Optional filters:
    - status: pending, in_progress, completed, archived
    - priority: low, medium, high, urgent
    """
    try:
        user_id = current_user["id"]
        client = db.get_client()
        
        # Build query
        query = client.table("todos").select("*").eq("user_id", user_id)
        
        # Apply filters
        if status:
            query = query.eq("status", status)
        if priority:
            query = query.eq("priority", priority)
        
        # Execute query
        response = query.order("created_at", desc=True).execute()
        
        return response.data
        
    except Exception as e:
        logger.error(f"Error fetching todos: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(
    todo_id: int,
    current_user: dict = Depends(get_current_user)
):
    """Get a specific todo by ID."""
    try:
        user_id = current_user["id"]
        client = db.get_client()
        
        response = client.table("todos").select("*").eq("id", todo_id).eq("user_id", user_id).execute()
        
        if not response.data:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching todo {todo_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=TodoResponse, status_code=201)
async def create_todo(
    todo: TodoCreate,
    current_user: dict = Depends(get_current_user)
):
    """Create a new todo."""
    try:
        user_id = current_user["id"]
        client = db.get_client()
        
        # Prepare data
        todo_data = todo.model_dump()
        todo_data["user_id"] = user_id
        
        # Insert into database
        response = client.table("todos").insert(todo_data).execute()
        
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create todo")
        
        logger.info(f"Created todo {response.data[0]['id']} for user {user_id}")
        return response.data[0]
        
    except Exception as e:
        logger.error(f"Error creating todo: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int,
    todo: TodoUpdate,
    current_user: dict = Depends(get_current_user)
):
    """Update an existing todo."""
    try:
        user_id = current_user["id"]
        client = db.get_client()
        
        # Check if todo exists and belongs to user
        existing = client.table("todos").select("*").eq("id", todo_id).eq("user_id", user_id).execute()
        
        if not existing.data:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        # Prepare update data (only non-None fields)
        update_data = {k: v for k, v in todo.model_dump().items() if v is not None}
        
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")
        
        # Update in database
        response = client.table("todos").update(update_data).eq("id", todo_id).eq("user_id", user_id).execute()
        
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to update todo")
        
        logger.info(f"Updated todo {todo_id} for user {user_id}")
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating todo {todo_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{todo_id}", status_code=204)
async def delete_todo(
    todo_id: int,
    current_user: dict = Depends(get_current_user)
):
    """Delete a todo."""
    try:
        user_id = current_user["id"]
        client = db.get_client()
        
        # Check if todo exists and belongs to user
        existing = client.table("todos").select("*").eq("id", todo_id).eq("user_id", user_id).execute()
        
        if not existing.data:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        # Delete from database
        client.table("todos").delete().eq("id", todo_id).eq("user_id", user_id).execute()
        
        logger.info(f"Deleted todo {todo_id} for user {user_id}")
        return None
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting todo {todo_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
