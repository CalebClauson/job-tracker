import tkinter as tk


BG_MAIN = "#F5F1EB"
BG_PANEL = "#E7DED1"
BG_WIDGET = "#D8C3A5"
BG_ACTIVE = "#C7A98B"
TEXT_MAIN = "#3E342B"
TEXT_BUTTON = "#2F241C"

def start_gui():
    root = tk.Tk()
    root.title("Job-Tracker")
    root.geometry("800x600")    
    state = "main"

    #frame
    top_frame = tk.Frame(root)
    top_frame.pack()

    mid_frame = tk.Frame(root)
    mid_frame.pack()

    bot_frame = tk.Frame(root)
    bot_frame.pack()

    
    #state functions
    def render_main():
        title_label = tk.Label(top_frame, text="Job Tracker")
        title_label.pack(pady=20)

        button_frame = tk.Frame(mid_frame)
        button_frame.pack(pady=40)

        tk.Button(button_frame, text="Add Job", width=15).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(button_frame, text="View Jobs", width=15).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(bot_frame, text="Exit", width=15).grid(row=1, column=0, columnspan=2, pady=10)

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
