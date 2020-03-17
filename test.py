import sqlite3
conn = sqlite3.connect('./private/db/database.db')
c = conn.cursor()

test = input()
print(test)
