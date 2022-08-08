import sqlite3
import pickle
class User:
    def __init__(self, discord_id):
        self.discord_id = discord_id
        self.balance = 100
        self.job = "0"
        self.moltiplicator = 1
        self.boosters = pickle.dumps([])
        self.level = 1
        self.inventory = pickle.dumps([])
        self.db = sqlite3.connect("DiscordEcon.db")
        self.cursor = self.db.cursor()
        self.load_data()
    
    def load_data(self):
        r = self.cursor.execute("SELECT * FROM users WHERE discord_id = ?", (self.discord_id,)).fetchone()
        if r != None:
            self.balance = r[1]
            self.job = r[2]
            self.moltiplicator = r[3]
            self.boosters = pickle.load(r[4])
            self.level = r[5]
            self.inventory = pickle.load(r[6])
        else:
            self.cursor.execute("INSERT INTO users (discord_id, balance, job, moltiplicator, boosters, level, inventory) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.discord_id, self.balance, self.job, self.moltiplicator, self.boosters, self.inventory))
            self.db.commit()

    def update_data(self):
        self.cursor.execute("UPDATE users SET job=?, balance=?, moltiplicator=?, inventory=?, boosters=?, level=? WHERE discord_id=?", (self.job, self.balance, self.moltiplicator, self.inventory, self.boosters, self.level, self.discord_id))
        self.db.commit()
        
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