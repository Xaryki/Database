import sqlite3


class Manager:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)

    def check_table(self, name):
        print(self.conn.execute(f"SELECT * from {name}").fetchall())
        self.conn.commit()

    def add_new_user(self, username):
        self.conn.execute(f"INSERT INTO users (username) VALUES (?)", (username,))
        self.conn.commit()

    def add_new_channel(self, title, link):
        self.conn.execute("INSERT INTO channels (title, link) VALUES (?, ?)", (title, link))
        self.conn.commit()

    def add_new_news(self, channel_id, message_id, create_date, embed):
        self.conn.execute("INSERT INTO news (channel_id, message_id, create_date, embed) VALUES (?, ?, ?, ?)",
                          (channel_id, message_id, create_date, embed))
        self.conn.commit()

    def add_new_many_news(self, news_list):
        query = "INSERT INTO news (channel_id, message_id, create_date, embed) VALUES (?, ?, ?, ?)"
        self.conn.executemany(query, news_list)
        self.conn.commit()

    def subscribe_user_to_channel(self, user_id, channel_id):
        self.conn.execute("INSERT INTO subscriptions (user_id, channel_id) VALUES (?, ?)", (user_id, channel_id))
        self.conn.commit()

    def unsubscribe_user_from_channel(self, user_id, channel_id):
        self.conn.execute("DELETE FROM subscriptions WHERE user_id = ? AND channel_id = ?", (user_id, channel_id))
        self.conn.commit()

    def close(self):
        self.conn.close()
