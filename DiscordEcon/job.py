import sqlite3

class Job:
    def __init__(self, name, reward, timeout):
        self.name = name
        self.reward = reward
        self.timeout = timeout
        self.users_count= 0
        self.total_gained = 0
        self.opened = True
        self.db = sqlite3.connect("DiscordEcon.db")
        self.cursor = self.db.cursor()
        self.load_data()

    def load_data(self):
        r = self.cursor.execute("SELECT * FROM jobs WHERE name = ?", (self.name,)).fetchone()
        if r != None:
            self.reward = r[1]
            self.timeout = r[2]
            self.users_count = r[3]
            self.total_gained = r[4]
            self.opened = r[5]
        else:
            self.cursor.execute("INSERT INTO jobs (name, reward, timeout, users_count, total_gained, opened) VALUES (?, ?, ?, ?, ?, ?)", (self.name, self.reward, self.timeout, self.users_count, self.total_gained, self.opened))
            self.db.commit()

    def update_data(self):
        self.cursor.execute("UPDATE jobs SET users_count=?, total_gained=?, opened=? WHERE name=?", (self.users_count, self.total_gained, self.opened, self.name))
        self.db.commit()

    def add_user(self):
        self.users_count += 1
    
    def rewarded(self):
        self.total_gained += self.reward
    
    def opened_status(self, status: bool):
        self.opened = status
