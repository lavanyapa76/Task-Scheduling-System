Task Scheduling System

## Project Overview

The Distributed Task Scheduling System is a Python-based web application developed to manage and distribute multiple tasks efficiently among available workers. It uses the **Round Robin Scheduling Algorithm** to allocate tasks in a balanced manner.

The system provides a simple web dashboard where users can submit tasks, monitor task execution, and view the status of different workers. Multiple worker threads simulate distributed task processing and help demonstrate the basic concepts of distributed computing.

## Objectives

- To understand the concepts of distributed task scheduling.
- To distribute tasks among multiple workers efficiently.
- To implement the Round Robin scheduling algorithm.
- To monitor task execution and worker status.
- To demonstrate workload distribution and parallel processing.

## Features

- **Task Submission:** Users can create and submit tasks through the web interface.
- **Automatic Scheduling:** Tasks are automatically assigned to workers using the Round Robin algorithm.
- **Multiple Workers:** Multiple worker threads handle task execution.
- **Task Monitoring:** Users can view pending, processing, and completed tasks.
- **Worker Status:** Displays the current activity of available workers.
- **Database Management:** SQLite stores task details and execution information.
- **User-Friendly Dashboard:** A simple interface for managing and monitoring tasks.

## Technologies Used

- Python – Core programming language
- Flask – Web application framework
- SQLite – Database management
- HTML – Web page structure
- CSS – Interface styling
- Threading – Simulating multiple workers

## System Workflow

1. The user opens the web application.
2. A new task is submitted through the dashboard.
3. The scheduler receives the submitted task.
4. The Round Robin algorithm assigns the task to a worker.
5. The worker processes the assigned task.
6. The task status is updated in the database.
7. The dashboard displays the latest task and worker status.

## Scheduling Algorithm

The project uses the **Round Robin Scheduling Algorithm**. It assigns tasks to workers one after another in a circular order.

For example, if three workers are available, tasks are assigned in the following order:

- Task 1 → Worker 1
- Task 2 → Worker 2
- Task 3 → Worker 3
- Task 4 → Worker 1

This approach helps distribute tasks evenly among the available workers.

## Project Structure

```text
Task_Scheduling/
│
├── app.py
├── database.py
├── scheduler.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation and Execution

**Step 1: Clone the Repository**

```bash
git clone https://github.com/lavanyapa76/Task-Scheduling-System.git
```

**Step 2: Open the Project Folder**

```bash
cd Task-Scheduling-System
```

**Step 3: Install Required Packages**

```bash
pip install -r requirements.txt
```

**Step 4: Run the Application**

```bash
python app.py
```

**Step 5: Open in Browser**

```text
http://127.0.0.1:5000
```

## Expected Outcome

The application allows users to submit and manage tasks through a web dashboard. Tasks are automatically distributed among multiple worker threads using the Round Robin algorithm. Users can monitor task progress and worker activities, making it easier to understand task scheduling and workload distribution.

## Future Enhancements

- Support for workers running on separate machines.
- Priority-based task scheduling.
- Improved task execution monitoring.
- User authentication and access management.
- Advanced performance analysis and reporting.

## Conclusion

The Distributed Task Scheduling System demonstrates the fundamental concepts of distributed computing through task allocation, worker management, and workload distribution. By implementing the Round Robin algorithm with Python, Flask, SQLite, and multiple worker threads, the project provides a practical understanding of how tasks can be scheduled and processed efficiently.

## Author

**Lavanya PA**

GitHub: https://github.com/lavanyapa76
