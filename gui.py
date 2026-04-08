import tkinter as tk

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
    root.configure(bg=BG_MAIN)
    state = "main"

    #frame
    top_frame = tk.Frame(root, bg=BG_MAIN)
    top_frame.pack()

    mid_frame = tk.Frame(root, bg=BG_MAIN)
    mid_frame.pack()

    bot_frame = tk.Frame(root, bg=BG_MAIN)
    bot_frame.pack()

    #helper
    def add_job():
        return
    
    def view_jobs():
        return

    #state functions
    def render_main():
        title_label = tk.Label(top_frame, bg=BG_MAIN, fg=FG_TEXT, text="Job Tracker", font=TITLE_FONT)
        title_label.pack(pady=20)

        button_frame = tk.Frame(mid_frame, bg=BG_MAIN)
        button_frame.pack(pady=40)

        tk.Button(button_frame, bg=BG_WIDGET, fg=FG_TEXT, text="Add Job", font=BUTTON_FONT, width=15, command=add_job).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(button_frame, bg=BG_WIDGET, fg=FG_TEXT,  text="View Jobs", font=BUTTON_FONT, width=15, command=view_jobs).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(bot_frame, bg=BG_WIDGET, fg=FG_TEXT, text="Exit", font=BUTTON_FONT, width=15, command=root.destroy).grid(row=1, column=0, columnspan=2, pady=10)

    def render_add_job():
        return

    def render_edit_job():
        return

    def render_view_jobs():
        return
        


    #state if chain
    if state == "main":
        render_main()
    elif state == "add_job":
        render_add_job()
    elif state == "edit_job":
        render_edit_job()
    elif state == "view_jobs":
        render_view_jobs()

    root.mainloop()
