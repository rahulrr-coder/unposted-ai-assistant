"""
Supabase database client and helpers
"""
from supabase import create_client, Client
from app.config import settings
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class Database:
    """Supabase database client wrapper."""
    
    def __init__(self):
        self.client: Optional[Client] = None
        
    def connect(self) -> Client:
        """Initialize Supabase client."""
        if not self.client:
            try:
                self.client = create_client(
                    supabase_url=settings.SUPABASE_URL,
                    supabase_key=settings.SUPABASE_KEY
                )
                logger.info("Supabase client initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Supabase client: {e}")
                raise
        return self.client
    
    def get_client(self) -> Client:
        """Get the Supabase client instance."""
        if not self.client:
            return self.connect()
        return self.client


# Global database instance
db = Database()


def get_db() -> Client:
    """Dependency for getting database client."""
    return db.get_client()
