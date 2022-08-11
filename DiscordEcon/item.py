import sqlite3

class Item:
    def __init__(self, type, name, description, cost):
        self.type = type
        self.name = name
        self.description = description
        self.cost = cost
        self.bought = 0
        self.buyable = True
        self.db = sqlite3.connect("DiscordEcon.db")
        self.cursor = self.db.cursor()
        self.load_data()
    
    def load_data(self):
        r = self.cursor.execute("SELECT * FROM items WHERE name = ?", (self.name,)).fetchone()
        if r != None:
            self.type = r[0]
            self.description = r[2]
            self.cost = r[3]
            self.bought = r[4]
            self.buyable = r[5]
            
        else:
            self.cursor.execute("INSERT INTO items (type, name, description, cost, bought, buyable) VALUES (?, ?, ?, ?, ?, ?)", (self.type, self.name, self.description, self.cost, self.bought, self.buyable))
            self.db.commit()


    def update_data(self):
        self.cursor.execute("UPDATE items SET cost=?, bought=?, buyable=? WHERE name = ?", (self.cost, self.bought, self.buyable, self.name))
        self.db.commit()
    
    def buyable_status(self, status):
        self.buyable = status
        self.update_data()

    def set_cost(self, cost):
        self.cost = cost
        self.update_data()
    
    def buy(self):
        self.bought += 1
        self.update_data()
