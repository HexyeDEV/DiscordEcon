import sqlite3

def create_db():
    db = sqlite3.connect("DiscordEcon.db")
    c = db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (discord_id INTEGER, balance REAL, job STRING, moltiplicator REAL, boosters TEXT, level INTEGER, inventory TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS jobs (name TEXT, reward INTEGER, timeout INTEGER, users_count INTEGER, total_gained INTEGER, opened BOOLEAN)")
    c.execute("CREATE TABLE IF NOT EXISTS items (type TEXT, name TEXT, description TEXT, cost INTEGER, bought INTEGER)")
    db.commit()