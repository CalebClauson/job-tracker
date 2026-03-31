# Job Tracker
WIP currently non-functional.
A simple Python job tracker that lets users store, organize, update, and review job applications. This project uses SQLite for data storage and is built as a command line application.

## Project Goal

The goal of this project is to create a useful application for tracking job applications in one place. It is designed to help manage important details such as company name, job title, application status, date applied, notes, and job links.

## Tools Used

- Python
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
├── tracker.py
├── README.md
└── .gitignore