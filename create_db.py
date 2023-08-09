import sqlite3


class Manager:
    def __init__(self, db_name='database.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        create_users_table = '''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT NOT NULL
            )
        '''
        create_channels_table = '''
            CREATE TABLE IF NOT EXISTS channels (
                channel_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                link TEXT NOT NULL,
                subscribers_count INTEGER DEFAULT 0
            )
        '''
        create_subscriptions_table = '''
            CREATE TABLE IF NOT EXISTS subscriptions (
                user_id INTEGER,
                channel_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                FOREIGN KEY (channel_id) REFERENCES channels (channel_id),
                PRIMARY KEY (user_id, channel_id)
            )
        '''
        create_news_table = '''
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                channel_id INTEGER,
                message_id INTEGER,
                create_date DATE,
                embed TEXT,
                FOREIGN KEY (channel_id) REFERENCES channels (channel_id)
            )
        '''
        create_increase_subscribers_trigger = '''
            CREATE TRIGGER IF NOT EXISTS increase_subscribers_count
            AFTER INSERT ON subscriptions
            BEGIN
                UPDATE channels
                SET subscribers_count = subscribers_count + 1
                WHERE channel_id = NEW.channel_id;
            END;
        '''
        create_decrease_subscribers_trigger = '''
            CREATE TRIGGER IF NOT EXISTS decrease_subscribers_count
            AFTER DELETE ON subscriptions
            BEGIN
                UPDATE channels
                SET subscribers_count = subscribers_count - 1
                WHERE channel_id = OLD.channel_id;
            END;
        '''
        self.conn.execute(create_users_table)
        self.conn.execute(create_channels_table)
        self.conn.execute(create_subscriptions_table)
        self.conn.execute(create_news_table)
        self.conn.execute(create_increase_subscribers_trigger)
        self.conn.execute(create_decrease_subscribers_trigger)
        self.conn.commit()

    def close(self):
        self.conn.close()
