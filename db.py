import sqlite3
from job import Job

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

def insert_job(job):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO jobs (company, title, status, date_applied, location, notes, link) VALUES (?, ?, ?, ?, ?, ?, ?)", job.to_tuple())
    conn.commit()
    conn.close()

def view_db():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    db = cursor.fetchall()
    conn.close()
    return db

def update_db(edit_job_id, job):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE jobs SET company = ?, title = ?, status = ?, date_applied = ?, location = ?, notes = ?, link = ? WHERE id = ?",
        job.to_tuple() + (edit_job_id,)
    )
    conn.commit()
    conn.close()


def clear_db():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs")
    conn.commit()
    conn.close()