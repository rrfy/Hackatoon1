import sqlite3

class BotDB:
    # open db
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    #is user in db
    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT 'id' FROM 'people' WHERE 'user_id = ?", (user_id))
        return bool(len(result.fetchall()))

    # get id of user
    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT 'id' FROM 'people' WHERE 'user_id' = ?", (user_id))
        return bool(len(result.fetchall()))

    def add_user(self, user_id, photo, name, description, username, course, institute, interests):
        with self.conn:
            return self.cursor.execute("INSERT INTO 'people' ('user_id', 'photo', name, 'description', 'username', 'coursee', 'institute', 'interests') VALUES (?, ?, ?, ?, ?, ?, ?) ", (user_id, photo, name, description, username, coursee, institute, interests))

    def edit_description(self, user_id, new_description):
        with self.conn:
            self.cursor.execute("UPDATE people SET 'description' = ? WHERE 'user_id' = ?", (new_description, user_id))

    def delete_profile(self, user_id):
        with self.conn:
            self.cursor.execute("DELETE FROM people WHERE 'user_id' = ?", (user_id))

    def get_photo(self, user_id):
        photo = self.cursor.execute("SELECT photo FROM people WHERE 'user_id' = ?", (user_id))
        return photo

    def get_all_profiles(self):
        profiles = self.cursor.execute("SELECT * FROM people").fetchall()
        return profiles

    def get_description(self, user_id):
        description = self.cursor.execute("SELECT description FROM people WHERE 'user_id' = ?", (user_id))
        return description

    def get_interests(self, user_id):
        interests = self.cursor.execute("SELECT interests FROM people WHERE 'user_id' = ?", (user_id))
        return interests

    def get_username(self, user_id):
        username = self.cursor.execute("SELECT username FROM people WHERE 'user_id' = ?", (user_id))
        return username

    def get_institute(self, user_id):
        institute = self.cursor.execute("SELECT institute FROM people WHERE 'user_id' = ?", (user_id))
        return institute

    def get_course(self, user_id):
        course = self.cursor.execute("SELECT course FROM people WHERE 'user_id' = ?", (user_id))
        return course

    def get_name(self, user_id):
        name = self.cursor.execute("SELECT name FROM people WHERE 'user_id' = ?", (user_id))
        return name

    # close db
    def close(self):
        self.conn.close()