import sqlite3
from job import Job
import os


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

def create_db():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT,
            title TEXT,
            status TEXT,
            date_applied TEXT,
            location TEXT,
            notes TEXT,
            link TEXT
        )
    """)
    conn.commit()
    conn.close()

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

def delete_db(delete_job_id):
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jobs WHERE id = ?", (delete_job_id,))
    conn.commit()
    conn.close()

def clear_db():
    if os.path.exists("jobs.db"):
        os.remove("jobs.db")
        create_db()