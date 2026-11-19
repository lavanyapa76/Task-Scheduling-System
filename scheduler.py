import threading
import time
from database import get_pending_task, update_task, update_worker

_worker_number = 0
_lock = threading.Lock()
_started = False

def process_task(task_id, task_name, worker_id):
    worker_name = f"Worker {worker_id}"
    update_worker(worker_id, "Busy")
    update_task(task_id, "Running", worker_name, "Processing...")
    time.sleep(3)  # Simulates task execution
    update_task(task_id, "Completed", worker_name, f"{task_name} completed successfully")
    update_worker(worker_id, "Idle")

def scheduler_loop():
    global _worker_number
    while True:
        task = get_pending_task()
        if task:
            with _lock:
                _worker_number = (_worker_number % 3) + 1
                worker_id = _worker_number
            thread = threading.Thread(
                target=process_task,
                args=(task[0], task[1], worker_id),
                daemon=True
            )
            # Mark it as running before starting another scheduler cycle.
            update_task(task[0], "Queued", f"Worker {worker_id}", "Waiting for worker")
            thread.start()
        time.sleep(1)

def start_scheduler():
    global _started
    if not _started:
        threading.Thread(target=scheduler_loop, daemon=True).start()
        _started = True
