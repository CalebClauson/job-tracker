import tkinter as tk
from job import Job
from db import insert_job, view_db, clear_db, update_db

TITLE_FONT = ("Helvetica", 18, "bold")
BUTTON_FONT = ("Helvetica", 12)

BG_MAIN = "#F5F1EB"
BG_PANEL = "#E7DED1"
BG_WIDGET = "#D8C3A5"
BG_ACTIVE = "#C7A98B"
FG_TEXT = "#2F241C"

def start_gui():
    root = tk.Tk()
    root.title("Job-Tracker")
    root.geometry("800x600")
    root.resizable(False, False)
    root.maxsize(800, 600)
    root.minsize(800, 600)
    root.configure(bg=BG_MAIN)
    state = "main"

    #initializing variables for job class
    company_entry = None
    title_entry = None
    status_entry = None
    status_var = None
    date_applied_entry = None
    location_entry = None
    notes_entry = None
    link_entry = None

    #editing variables
    edit_job_id = None
    jobs = None
    job_listbox = None
    selected_job = None

    #frame definition
    top_frame = tk.Frame(root, bg=BG_MAIN)
    top_frame.pack(fill="x")

    mid_frame = tk.Frame(root, bg=BG_MAIN)
    mid_frame.pack(fill="both", expand=True)

    bot_frame = tk.Frame(root, bg=BG_MAIN, height=120)
    bot_frame.pack(fill="x", side="bottom")
    bot_frame.pack_propagate(False)

    #helper for frames / state changer
    def clear_all_frames():
        for frame in (top_frame, mid_frame, bot_frame):
            for widget in frame.winfo_children():
                widget.destroy()

    def clear_entry():
        company_entry.delete(0, tk.END)
        title_entry.delete(0, tk.END)
        date_applied_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)
        notes_entry.delete(0, tk.END)
        link_entry.delete(0, tk.END)

    def main_menu():
        nonlocal state
        clear_all_frames()
        state = "main"
        render_main()

    def add_job():
        nonlocal state
        clear_all_frames()
        state = "add_job"
        render_add_job()

    def view_jobs():
        nonlocal state
        clear_all_frames()
        state = "view_jobs"
        render_view_job()

    def edit_job():
        nonlocal state, jobs, job_listbox, selected_job, edit_job_id

        if not job_listbox.curselection():
            return

        selected_index = job_listbox.curselection()[0]
        selected_job = jobs[selected_index]
        edit_job_id = selected_job[0]
        clear_all_frames()
        state = "edit_job"
        render_edit_job()

    #helper for backend
    def on_save_job():
        nonlocal company_entry, title_entry, status_var, date_applied_entry, location_entry, notes_entry, link_entry
        job = Job(
            company_entry.get(),
            title_entry.get(),
            status_var.get(),
            date_applied_entry.get(),
            location_entry.get(),
            notes_entry.get(),
            link_entry.get()
        )
        #backend for inserting into db
        insert_job(job)
        clear_entry()

    def on_save_edit_job():
        nonlocal company_entry, title_entry, status_var, date_applied_entry, location_entry, notes_entry, link_entry, edit_job_id
        job = Job(
            company_entry.get(),
            title_entry.get(),
            status_var.get(),
            date_applied_entry.get(),
            location_entry.get(),
            notes_entry.get(),
            link_entry.get()
        )

        update_db(edit_job_id, job)
        clear_entry()

    #state functions
    def render_main():
        title_label = tk.Label(top_frame, bg=BG_MAIN, fg=FG_TEXT, text="Job Tracker", font=TITLE_FONT)
        title_label.pack(pady=20)

        button_frame = tk.Frame(mid_frame, bg=BG_MAIN)
        button_frame.pack(pady=20)

        tk.Button(button_frame, bg=BG_WIDGET, fg=FG_TEXT, text="Add Job", font=BUTTON_FONT, width=15, command=add_job).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(button_frame, bg=BG_WIDGET, fg=FG_TEXT, text="View Jobs", font=BUTTON_FONT, width=15, command=view_jobs).grid(row=1, column=0, padx=10, pady=10)

        tk.Button(bot_frame, bg=BG_ACTIVE, fg=FG_TEXT, text="Clear DB", font=BUTTON_FONT, width=10, command=clear_db).place(relx=1.0, rely=1.0, x=-15, y=-15, anchor="se")

    def render_add_job():
        nonlocal company_entry, title_entry, status_var, status_entry, date_applied_entry, location_entry, notes_entry, link_entry

        title_label = tk.Label(top_frame, bg=BG_MAIN, fg=FG_TEXT, text="Add Job Application", font=TITLE_FONT)
        title_label.pack(pady=20)

        form_frame = tk.Frame(mid_frame, bg=BG_MAIN)
        form_frame.pack(pady=20)

        button_frame = tk.Frame(mid_frame, bg=BG_MAIN)
        button_frame.pack(pady=20)

        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Company:", font=BUTTON_FONT, width=15).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Job Title:", font=BUTTON_FONT, width=15).grid(row=1, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Status:", font=BUTTON_FONT, width=15).grid(row=2, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Date Applied:", font=BUTTON_FONT, width=15).grid(row=3, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Location:", font=BUTTON_FONT, width=15).grid(row=4, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Notes:", font=BUTTON_FONT, width=15).grid(row=5, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Link:", font=BUTTON_FONT, width=15).grid(row=6, column=0, padx=10, pady=10)

        company_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        title_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        status_var = tk.StringVar(value="Applied")
        status_entry = tk.OptionMenu(form_frame, status_var, "Applied", "Interview", "Rejected", "Offer")
        status_entry.config(bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=12)
        date_applied_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        location_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        notes_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        link_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)

        company_entry.grid(row=0, column=2, padx=10, pady=10)
        title_entry.grid(row=1, column=2, padx=10, pady=10)
        status_entry.grid(row=2, column=2, padx=10, pady=10)
        date_applied_entry.grid(row=3, column=2, padx=10, pady=10)
        location_entry.grid(row=4, column=2, padx=10, pady=10)
        notes_entry.grid(row=5, column=2, padx=10, pady=10)
        link_entry.grid(row=6, column=2, padx=10, pady=10)

        tk.Button(button_frame, bg=BG_WIDGET, fg=FG_TEXT, text="Save", font=BUTTON_FONT, width=15, command=on_save_job).grid(row=0, column=0, pady=10)
        tk.Button(button_frame, bg=BG_WIDGET, fg=FG_TEXT, text="Back", font=BUTTON_FONT, width=15, command=main_menu).grid(row=1, column=0, pady=10)

    def render_view_job():
        nonlocal jobs, job_listbox
        jobs = view_db()

        title_label = tk.Label(top_frame, bg=BG_MAIN, fg=FG_TEXT, text="Job Applications", font=TITLE_FONT)
        title_label.pack(pady=20)

        job_listbox = tk.Listbox(mid_frame, width=50, height=20, font=BUTTON_FONT)
        for job in jobs:
            job_listbox.insert(tk.END, job)
        job_listbox.pack()

        button_frame = tk.Frame(mid_frame, bg=BG_MAIN)
        button_frame.pack(pady=20)

        tk.Button(button_frame, bg=BG_WIDGET, fg=FG_TEXT, text="Edit", font=BUTTON_FONT, width=15, command=edit_job).pack()
        tk.Button(bot_frame, bg=BG_WIDGET, fg=FG_TEXT, text="Back", font=BUTTON_FONT, width=15, command=main_menu).place(relx=0.0, rely=1.0, x=15, y=-15, anchor="sw")

    def render_edit_job():
        nonlocal company_entry, title_entry, status_var, status_entry, date_applied_entry, location_entry, notes_entry, link_entry, selected_job

        title_label = tk.Label(top_frame, bg=BG_MAIN, fg=FG_TEXT, text="Edit Job Application", font=TITLE_FONT)
        title_label.pack(pady=20)

        form_frame = tk.Frame(mid_frame, bg=BG_MAIN)
        form_frame.pack(pady=20)

        button_frame = tk.Frame(mid_frame, bg=BG_MAIN)
        button_frame.pack(pady=20)

        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Company:", font=BUTTON_FONT, width=15).grid(row=0, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Job Title:", font=BUTTON_FONT, width=15).grid(row=1, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Status:", font=BUTTON_FONT, width=15).grid(row=2, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Date Applied:", font=BUTTON_FONT, width=15).grid(row=3, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Location:", font=BUTTON_FONT, width=15).grid(row=4, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Notes:", font=BUTTON_FONT, width=15).grid(row=5, column=0, padx=10, pady=10)
        tk.Label(form_frame, bg=BG_MAIN, fg=FG_TEXT, text="Link:", font=BUTTON_FONT, width=15).grid(row=6, column=0, padx=10, pady=10)

        company_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        title_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        status_var = tk.StringVar(value="Applied")
        status_entry = tk.OptionMenu(form_frame, status_var, "Applied", "Interview", "Rejected", "Offer")
        status_entry.config(bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=12)
        date_applied_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        location_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        notes_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)
        link_entry = tk.Entry(form_frame, bg=BG_WIDGET, fg=FG_TEXT, font=BUTTON_FONT, width=15)

        company_entry.grid(row=0, column=2, padx=10, pady=10)
        title_entry.grid(row=1, column=2, padx=10, pady=10)
        status_entry.grid(row=2, column=2, padx=10, pady=10)
        date_applied_entry.grid(row=3, column=2, padx=10, pady=10)
        location_entry.grid(row=4, column=2, padx=10, pady=10)
        notes_entry.grid(row=5, column=2, padx=10, pady=10)
        link_entry.grid(row=6, column=2, padx=10, pady=10)

        company_entry.insert(0, selected_job[1])
        title_entry.insert(0, selected_job[2])
        status_var.set(selected_job[3])
        date_applied_entry.insert(0, selected_job[4])
        location_entry.insert(0, selected_job[5])
        notes_entry.insert(0, selected_job[6])
        link_entry.insert(0, selected_job[7])

        tk.Button(button_frame, bg=BG_WIDGET, fg=FG_TEXT, text="Save", font=BUTTON_FONT, width=15, command=on_save_edit_job).grid(row=0, column=0, pady=10)
        tk.Button(button_frame, bg=BG_WIDGET, fg=FG_TEXT, text="Back", font=BUTTON_FONT, width=15, command=main_menu).grid(row=1, column=0, pady=10)

    #state if chain
    if state == "main":
        render_main()
    elif state == "add_job":
        render_add_job()
    elif state == "edit_job":
        render_edit_job()

    root.mainloop()