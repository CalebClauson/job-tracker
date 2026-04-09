# Job Tracker

WIP currently non-functional.

A simple Python job tracker that lets users store, organize, update, and review job applications. This project uses SQLite for data storage and is being built with a Tkinter GUI.

This project also serves as practice with Tkinter, GUI design, and event-driven programming in Python.

## Project Goal

The goal of this project is to create a useful application for tracking job applications in one place. It is designed to help manage important details such as company name, job title, application status, date applied, notes, and job links.

A second goal of this project is to improve my understanding of Tkinter and how event-driven programs work, including handling user input, button actions, window state changes, and connecting a GUI to a database backend.

## Tools Used

- Python
- Tkinter
- SQLite
- VS Code
- Git and GitHub

## Features

### Current or Planned Features
- Create a database automatically if it does not exist
- Add a new job application
- View all saved applications
- Update an application
- Delete an application by ID
- Search applications by company or title
- Filter applications by status
- Sort applications by date or company name
- Input validation for cleaner and safer user input

## Project Structure

```text
job-tracker/
├── main.py
├── db.py
├── job.py
├── gui.py
├── README.md
└── .gitignore