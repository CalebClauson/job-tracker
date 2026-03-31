import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

#Initial Database created
# cursor.execute("""
#            CREATE TABLE jobs(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             company TEXT,
#             title TEXT,
#             status TEXT,
#             date_applied TEXT,
#             location TEXT,
#             notes TEXT,
#             link TEXT
#            )""")

conn.commit()
conn.close()