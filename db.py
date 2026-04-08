import sqlite3
from job import job

#LEFT FOR CONTEXT OF DB
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

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

conn.execute("SELECT * FROM jobs")
conn.commit()

print(cursor.fetchall())
conn.close()