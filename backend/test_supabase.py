#!/usr/bin/env python3
"""
Test Supabase connection
"""
import sys
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent))

from app.database import db

def test_connection():
    """Test Supabase database connection."""
    try:
        print("🔌 Testing Supabase connection...")
        print(f"📍 URL: https://lvfmdzwbooucjtnxvffq.supabase.co")
        
        # Initialize client
        client = db.connect()
        print("✅ Supabase client initialized successfully!")
        
        # Try to list tables (this will work even without tables)
        print("\n📊 Testing database query...")
        
        # Test a simple query - list users table (create it if needed)
        try:
            result = client.table("users").select("*").limit(1).execute()
            print(f"✅ Database query successful!")
            print(f"📝 Users table exists with {len(result.data)} records (showing max 1)")
        except Exception as e:
            if "relation" in str(e).lower() and "does not exist" in str(e).lower():
                print("⚠️  Users table doesn't exist yet - needs to be created in Supabase")
                print("   You can create it via Supabase dashboard or migration")
            else:
                print(f"⚠️  Query error: {e}")
        
        print("\n✅ Supabase connection test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
