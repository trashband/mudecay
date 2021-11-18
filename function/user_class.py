import sqlite3
conn = sqlite3.connect('database.db', check_same_thread=False)

class user_class():
    
    def user_data(id):
        user_data = []
        cursor = conn.execute("SELECT * FROM user")
        for i in cursor:
            if i[1] == id:
                user_data.append(i)
                return user_data