# Database Setup

## Supabase Configuration

### ✅ Already Configured

Your `.env` file is configured with:
- **URL**: `https://lvfmdzwbooucjtnxvffq.supabase.co`
- **Anon Key**: ✅ Configured

### 📊 Existing Tables

You already have these tables:
- `todos` - Main todos
- `tasks` - Subtasks
- `tags` - Categorization tags
- `todo_tags` - Many-to-many junction

### ➕ Add New Tables

Run the migration to add tables for the journaling assistant:

1. Open: https://lvfmdzwbooucjtnxvffq.supabase.co
2. Go to **SQL Editor** in the left sidebar
3. Click **New Query**
4. Copy and paste the contents of `001_initial_schema.sql`
5. Click **Run** or press `Ctrl+Enter`

This will add:
- ✅ `user_preferences` - News preferences, voice settings
- ✅ `journal_entries` - Voice journal data
- ✅ `user_interactions` - News reading history
- ✅ `saved_articles` - Bookmarked articles

**Safe to run**: Uses `IF NOT EXISTS` - won't break existing tables!

### 🔌 Test Connection

```bash
cd backend
python test_supabase.py
```

Expected output:
```
✅ Supabase client initialized successfully!
✅ Database query successful!
```

## New Tables Overview

### user_preferences
- Links to `auth.users(id)` (Supabase built-in auth)
- `news_categories` - Array of preferred categories
- `news_sources` - Array of preferred sources
- `voice_preference` - TTS voice selection
- `notification_enabled`, `theme`, `language`

### journal_entries
- `transcript` - Voice journal text
- `entities` - Extracted entities array
- `emotion_valence`, `emotion_arousal` - Emotion coordinates
- `emotion_label` - Human readable emotion
- `bullets` - Three reflection bullets (array)
- `next_prompt` - Follow-up question

### user_interactions
- Tracks news article interactions
- `article_id`, `article_title`, `article_url`
- `interaction_type` - view, like, share, save

### saved_articles
- Bookmarked news articles
- Full article metadata
- `published_at`, `saved_at` timestamps

## Authentication

Using **Supabase Auth** (built-in):
- No custom users table needed
- References `auth.users(id)`
- JWT tokens handled by Supabase
- Row Level Security (RLS) enabled

## Next Steps

1. ✅ Run migration: `001_initial_schema.sql` in Supabase SQL Editor
2. ✅ Test connection: `python test_supabase.py`
3. ✅ Start backend: `./start_backend.sh`
4. ✅ Test endpoints: Visit http://localhost:8000/docs
