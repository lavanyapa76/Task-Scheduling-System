# Distributed Task Scheduling System

## Project overview
A mini project that demonstrates task submission, task scheduling, and task execution using three simulated workers. The scheduler assigns tasks in Round Robin order and the dashboard displays task and worker status.

## Technology used
- Python
- Flask
- SQLite
- HTML and CSS
- Python threading

## Folder structure
```text
Task_Scheduling/
|-- app.py
|-- database.py
|-- scheduler.py
|-- requirements.txt
|-- README.md
|-- templates/
|   `-- index.html
`-- static/
    `-- style.css
```

## Run in Windows VS Code terminal
```bash
python -m venv venv
venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 in your browser.

The `tasks.db` database is created automatically when the application starts.

## Note
This is an educational simulation. Three worker threads run on the same computer; they are not separate networked machines. The scheduler demonstrates Round Robin worker assignment.
