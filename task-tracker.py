import sys, json, os

def load_tasks():
    if not os.path.exists("tasks.json"):
        with open("tasks.json", "w") as file:
            json.dump([], file)
    with open("tasks.json", "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({"id": task_id, "title": title, "status": "todo"})
    save_tasks(tasks)
    print(f"Task added: {title}")

def list_all():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            print(f"{task['id']}: {task['title']} - {task['status']}")

def list_status(status):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        found = False
        for task in tasks:
            if task['status'] == status:
                found = True
                print(f"{task['id']}: {task['title']} - {task['status']}")
        if not found:
            print(f"No tasks with status: {status}")

def mark_task(mark, task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = mark
            save_tasks(tasks)
            print(f"Task {task_id} marked as {mark}")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task['id'] != task_id]
    if len(updated_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
    else:
        save_tasks(updated_tasks)
        print(f"Task {task_id} deleted.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task-tracker.py <command> [arguments]")
    else:
        command = sys.argv[1]

        if command == "add":
            if len(sys.argv) < 3:
                print("Please provide a task title.")
            else:
                add_task(" ".join(sys.argv[2:]))

        elif command == "list":
            if len(sys.argv) < 3:
                list_all()
            else:
                list_status(sys.argv[2])

        elif command == "done" or command == "in-progress":
            if len(sys.argv) < 3:
                print("Please provide a task ID.")
            else:
                mark_task(command, int(sys.argv[2]))

        elif command == "delete":
            if len(sys.argv) < 3:
                print("Please provide a task ID.")
            else:
                delete_task(int(sys.argv[2]))

        else:
            print("Unknown command.")
