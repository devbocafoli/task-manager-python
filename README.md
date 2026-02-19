# Task Manager Python 🚀

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
    
    Manage your tasks simply and efficiently using Python.

## 🔹Description

    This project is a simple task manager written in Python. It allows you to add, list, and remove tasks, saving the data to a JSON file. It's ideal for those who want to organize their tasks practically without relying on complex software.

## 🔹Features

- ✅ Add new tasks
- ✅ List all tasks
- ✅ Mark tasks as completed/pending
- ✅ Edit or remove existing tasks
- ✅ Data storage in JSON

## 🔹Technologies

- Python 3.11+
- JSON (for data storage)

## 🔹How to Use

1. Clone this Repository:
```bash
git clone https://github.com/devbocafoli/task-manager-python.git 
```

2. Go to the Project Folder:
```bash
cd task-manager-python
```

3. Run the Program:
```bash
python main.py
```

4. Follow the instructions in the menu to manage your tasks.

## 🔹Estrutura do Projeto
```
task-manager-python/
├─ src/
│ ├─ task_manager/
│ │ ├─ models/
│ │ │ ├─ tasks.py
│ │ ├─ services.py
│ │ ├─ storage.py
│ ├─ main.py
├─ .gitignore
├─ README.md
```

## 🔹What I Learned
- How to organize a Python project in a modular way (separating models, services, and storage)
- Manipulating JSON files to save and load data
- Creating interactive menus in the terminal
- Concepts of functions, classes, and static methods
- How to plan and refactor code to make it cleaner and more readable
- Error handling

## 🔹Challenges Faced:

- Ensuring data was saved correctly in the JSON file.
- Structuring the project in a way that was scalable and easy to understand.
- Handling user input and preventing errors during execution.

## 🔹 Next steps / improvements

- Implement automated tests with pytest
- Add a prioritization system for tasks
- Create a version with a graphical user interface (GUI)
- Add advanced task filters and searches

## 🔹 Contributions

Contributions are welcome! If you want to improve this project:

1. Fork this repository.

2. Create a branch with your feature:
```bash
git checkout -b my-feature
```

3. Commit your changes:
```bash
git commit -m "My contribution"
```

4. Push to the original branch:
```bash
git push origin my-feature
```

5. Open a Pull Request.

## 🔹License

MIT License © 2026 Giovani Bocafoli