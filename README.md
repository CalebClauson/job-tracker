# Job Tracker (Python + Tkinter)

A job application tracker built with Python, Tkinter, and SQLite as I continue learning how to create more structured, interactive, and data-driven applications.

## Overview

This project started as a smaller idea for tracking job applications and gradually grew into a multi-file application with a graphical interface, SQLite database support, and a more organized state-driven GUI flow.

The project is designed to store and manage job applications in one place while also serving as practice for building desktop applications in Python. It focuses on separating interface code from backend logic, organizing a project across multiple files, and improving how I work with event-driven programming.

## Purpose

This project was created to move beyond basic scripts and continue practicing how to build a more complete application with multiple files, connected systems, reusable logic, and a GUI.

It focuses on practicing:

- Tkinter GUI design
- event-driven programming
- state management
- SQLite database integration
- working with classes and objects
- CRUD-style application structure
- separating GUI code from backend logic
- debugging across multiple files
- refactoring as a project grows

A major goal of this project is improving my comfort with Tkinter while learning how a GUI application connects user input, program state, and persistent database storage.

## Current Features

### GUI-Based Application Flow

The project uses a Tkinter interface instead of the console, allowing the user to move through the application using buttons, forms, and different window states.

Current GUI flow includes:

- main menu
- add job screen
- view jobs screen
- edit job screen

The GUI is being built around a state-based structure so different screens can be rendered more cleanly as the project expands.

### Job Entry System

The application includes a form for entering job application data.

Current job fields include:

- company
- job title
- status
- date applied
- location
- notes
- link

This allows the project to track the main pieces of information I would actually want to keep with each application.

### SQLite Database Support

The project uses SQLite for persistent storage so job applications can be saved and loaded outside of a single session.

Current database work includes:

- connecting to a SQLite database
- inserting job applications
- viewing saved job data
- clearing saved records for testing
- laying the groundwork for updating existing records

This helps the project move beyond temporary runtime data and into something more practical and reusable.

### Object-Based Data Handling

The project uses a `Job` class to represent a job application as a structured object rather than passing loose values around everywhere.

This helps with:

- grouping application data together
- making inserts cleaner
- improving readability
- preparing for update and edit functionality

### View and Edit Workflow

The project now includes a jobs list screen that displays saved applications and begins setting up the flow for editing an existing entry.

Current edit-related progress includes:

- loading saved jobs into a Listbox
- selecting a job from the list
- moving into an edit state
- preloading selected row data into the edit form
- laying the groundwork for database updates by row id

This part of the project is helping me practice how GUI selection connects to backend data.

## Project Structure

The project is split across multiple files so responsibilities are separated more clearly.

Current structure includes files such as:

- `main.py` for starting the application
- `gui.py` for window states, forms, buttons, and interface flow
- `db.py` for SQLite database functions
- `job.py` for the `Job` class
- `README.md` for project documentation

This separation is helping keep the project more organized as more features are added.

## Current or Planned Features

- create the database automatically if it does not exist
- add a new job application
- view all saved applications
- edit an existing application
- delete an application
- search applications by company or title
- filter applications by status
- sort applications by date or company
- input validation for cleaner and safer user input

## Recent Progress

Some of the more recent improvements to the project include:

- building a Tkinter GUI skeleton
- adding reusable window states
- organizing the app with multiple files
- connecting the add form to SQLite inserts
- setting up a jobs view screen with a Listbox
- creating an edit state for selected applications
- practicing how selected GUI rows map back to database rows
- improving understanding of Tkinter widget scope, callbacks, and shared state

These updates have helped the project feel more like a real application while also giving me more practice with Tkinter and event-driven design.

## Running

The project can be run normally in Python from the project folder.

Basic run command for Linux:

```bash
python3 main.py