import sqlite3

class Item:
    def __init__(self, type, name, description, cost):
        self.type = type
        self.name = name
        self.description = description
        self.cost = cost
        self.bought = 0
        self.db = sqlite3.connect("DiscordEcon.db")
        self.cursor = self.db.cursor()
        self.cursor.execute("INSERT INTO items (type, name, description, cost, bought) VALUES (?, ?, ?, ?, ?)", (self.type, self.name, self.description, self.cost, self.bought))
        self.db.commit()
    
    def update_data(self):
        self.cursor.execute("UPDATE items SET cost=?, bought=? WHERE name=?", (self.cost, self.bought, self.name))
        self.db.commit()

    def set_cost(self, cost):
        self.cost = cost
        self.update_data()
    
    def buy(self):
        self.bought += 1
        self.update_data()
