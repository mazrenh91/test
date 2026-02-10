# initialise database (CREATE)
import sqlite3

class DatabaseManager:
    def __init__(self, db_name='example.db'):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Initialize database with tables"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')   

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(id)
                )
            ''')

# create data (INSERT) -1
    def create_user(self, name, email, age):
        """Create a new user"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (name, email, age)
                    VALUES (?, ?, ?)
                ''', (name, email, age))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return None

# create data (INSERT) -2
    def create_post(self, user_id, title, content):
        """Create a new post"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO orders (user_id, title, content)
                VALUES (?, ?, ?)
            ''', (user_id, title, content))
            return cursor.lastrowid

# read data (SELECT) -1
    def get_all_user(self):
        """Get all users"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()

# read data (SELECT) -2
    def get_user_posts(self, user_id):
        """Get posts by user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT p.id, p.title, p.content, p.created_at
                FROM orders p
                WHERE p.user_id = ?
                ORDER BY p.created_at DESC
            ''', (user_id,))
            return cursor.fetchall()

# delete data (DELETE)
    def delete_user(self, user_id):
        """Delete a user and their posts"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM posts WHERE user_id = ?', (user_id,))
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount > 0

# update data (UPDATE)
    def update_user_email(self, user_id, new_email):
        """Update user's email"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE users
                    SET email = ?
                    WHERE id = ?
                ''', (new_email, user_id))
                return cursor.rowcount > 0
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")
            return False
        
# run on terminal function
def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("Database Manager")
    print("="*40)
    print("1. Create User")
    print("2. View All Users")
    print("3. Create Post")
    print("4. View User Posts")
    print("5. Delete User")
    print("6. Exit")
    print("7. Update User Email")
    print("="*40)

def main():
    """Main interactive CLI function"""
    db = DatabaseManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            print("\n--- Create New User ---")
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            try:
                age = int(input("Enter age: ").strip())
                user_id = db.create_user(name, email, age)
                if user_id:
                    print(f"✓ User created successfully! ID: {user_id}")
                else:
                    print("✗ Failed to create user.")
            except ValueError:
                print("✗ Invalid age. Please enter a number.")

        elif choice == '2':
            print("\n--- All Users ---")
            users = db.get_all_user()
            if users:
                for user in users:
                    print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]} | Age: {user[3]}")
            else:
                print("No users found.")

        elif choice == '3':
            print("\n--- Create New Post ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                title = input("Enter post title: ").strip()
                content = input("Enter post content: ").strip()
                post_id = db.create_post(user_id, title, content)
                if post_id:
                    print(f"✓ Post created successfully! ID: {post_id}")
                else:
                    print("✗ Failed to create post.")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")

        elif choice == '4':
            print("\n--- View User Posts ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                posts = db.get_user_posts(user_id)
                if posts:
                    for post in posts:
                        print(f"\nPost IDL {post[0]}")
                        print(f"Title: {post[1]}")
                        print(f"Content: {post[2]}")
                        print(f"Created At: {post[3]}")
                        print("-"*30)
                else:
                    print("No posts found for this user.")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")

        elif choice == '5':
            print("\n--- Delete User ---")
            try:
                user_id = int(input("Enter user ID to delete: ").strip())
                confirm = input(f"Are you sure you want to delete user ID {user_id}? (y/n): ").strip().lower()
                if confirm == 'y':
                    if db.delete_user(user_id):
                        print("✓ User deleted successfully.")
                    else:
                        print("✗ User not found or deletion failed.")
                else:
                    print("✗ Deletion cancelled.")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")
        
        elif choice == '6':
            print("\nGoodbye! :)")
            break

        elif choice == '7':
            print("\n--- Update User Email ---")
            try:
                user_id = int(input("Enter user ID: ").strip())
                new_email = input("Enter new email: ").strip()
                if db.update_user_email(user_id, new_email):
                    print("✓ Email updated successfully.")
                else:
                    print("✗ User not found or email update failed.")
            except ValueError:
                print("✗ Invalid user ID. Please enter a number.")

        else:
            print("✗ Invalid choice. Please enter 1 - 7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()