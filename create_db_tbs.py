import sqlite3
import random
import string

# Connect to the database (creates it if it doesn't exist)
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Create the tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS table1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    value INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS table2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    value INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS table3 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    value INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS table4 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    value INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS table5 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    value INTEGER
)
""")

# Function to generate random data
def random_string(string_length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

# Insert 100 records into each table
for i in range(1000):
    cursor.execute("INSERT INTO table1 (name, value) VALUES (?, ?)", (random_string(), random.randint(0, 100)))
    #cursor.execute("INSERT INTO table2 (name, value) VALUES (?, ?)", (random_string(), random.randint(0, 100)))
    #cursor.execute("INSERT INTO table3 (name, value) VALUES (?, ?)", (random_string(), random.randint(0, 100)))
    #cursor.execute("INSERT INTO table4 (name, value) VALUES (?, ?)", (random_string(), random.randint(0, 100)))
    #cursor.execute("INSERT INTO table5 (name, value) VALUES (?, ?)", (random_string(), random.randint(0, 100)))

# Commit the changes and close the connection
conn.commit()
conn.close()
