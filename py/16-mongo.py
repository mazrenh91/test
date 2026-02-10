# initialize
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()   # Load environment variables from .env file

mongo_uri = os.getenv('MONGODB_ATLAS_CLUSTER_URI')

class DatabaseManager:
    def __init__(self, db_name='example.db', connection_string=mongo_uri):
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.users_collection = self.db.users
        self.posts_collection = self.db.posts
        self,init.database()

    def init_database(self):
        """Initialize database with collections and indexes."""
        # create unique index on email for users
        self.users_collection.create_index('email', unique=True)
        # create index on user_id for posts for better query performance
        self.posts_collection.create_index('user_id')

# create function - 1
    def create_user(self, name, email, age):
        """Create a new user."""
        try:
            user_doc = {
                'name': name,
                'email': email,
                'age': age,
                'created_at': datetime.utcnow()
            }
            result = self.users_collection.insert_one(user_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error: {e}")
            return None

# create function - 2
    def create_post(self, user_id, title, content):
        """Create a new post"""
        try:
            # convert string user_id to ObjectID if it's a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_id = ObjectId(user_id)
            else:
                user_object_id = user_id
            
            post_doc = {
                'user_id': user_object_id,
                'title': title,
                'content': content,
                'created_at': datetime.utcnow()
            }
            result = self.posts_collection.insert_one(post_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error creating post: {e}")
            return None

# read function - 1
    def get_all_users(self):
        """Get all users"""
        try:
            users = list(self.users_collection.find())
            # convert ObjectId to string for display
            for user in users:
                user['_id'] = str(user['_id'])  # Convert ObjectId to string for easier handling
            return users
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []

# read function - 2
    def get_posts_by_user(self, user_id):
        """Get posts by user"""
        try:
            # convert string user_id to ObjectID if it's a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            posts = list(self.posts_collection.find(
                {"user_id": user_object_id}
            ).sort("created_at", -1))

            # convert ObjectId to string for display
            for post in posts:
                post['_id'] = str(post['_id'])  # Convert ObjectId to string for easier handling
                post['user_id'] = str(post['user_id'])  # Convert user_id ObjectId to string
            
            return posts
        except Exception as e:
            print(f"Error fetching posts: {e}")
            return []