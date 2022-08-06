import uuid
import sqlite3

class User:
    def __init__(self):
        self.uuid = uuid.uuid4()
        self.discord_id = uuid.uuid4()
        self.balance = 100
        self.job = "0"
        self.moltiplicator = 1
        self.boosters = []
        self.level = 1
        self.inventory = []
        self.db = sqlite3.connect("DiscordEcon.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("INSERT INTO users (uuid, discord_id, balance, job, moltiplicator, boosters, level, inventory) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.uuid, self.discord_id, self.balance, self.job, self.moltiplicator, ' '.join(self.boosters), ' '.join(self.inventory)))
        self.db.commit()
    
    def update_data(self):
        self.cursor.execute("UPDATE users SET job=?, balance=?, moltiplicator=?, boosters=?, level=? WHERE uuid=?", (self.job, self.balance, self.moltiplicator, ' '.join(self.boosters), self.level, self.uuid))
        
    def set_job(self, job):
        self.job = job
    
    def change_balance(self, balance):
        self.balance += balance
    
    def set_balance(self, balance):
        self.balance = balance
    
    def change_moltiplicator(self, moltiplicator):
        self.moltiplicator += moltiplicator
    
    def change_boosters(self, booster):
        if self.boosters == None:
            self.boosters = [booster]
        else:
            self.boosters.append(booster)
    
    def change_level(self, levels):
        self.level += levels
    
    def set_level(self, level):
        self.level = level