# 🗂 Task Manager - Python

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pytest](https://img.shields.io/badge/Tests-pytest-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-Study%20Project-lightgrey)

A task manager built in Python with a focus on clean architecture, code organization, and automated testing.

---

## 🚀 About the Project

This project started as a simple CLI application to practice logic and JSON file handling, but it evolved into a more professional structure applying real-world software development concepts.

The project now includes:

* Layered architecture (models, services, storage)
* Clear separation of responsibilities
* JSON-based data persistence
* Automated testing with pytest
* Dependency isolation in tests
* Structure prepared for future scalability

---

## 🧠 What Was Learned During Development

Throughout the development process, the following concepts were practiced and strengthened:

### 📦 Project Structure

* Separation between business logic and persistence
* Modular organization

### 🗃 Data Persistence

* Working with JSON files
* Exception handling
* Object serialization (to_dict)
* Object reconstruction (from_dict)

### 🧪 Automated Testing

* Using pytest
* Writing unit tests
* Using tmp_path for temporary files
* Using monkeypatch to isolate dependencies
* Testing the models layer
* Testing the services layer
* Testing the storage layer

### 🔎 Debugging & Code Quality

* Reading and understanding tracebacks
* Fixing import errors
* Resolving inconsistencies between tests and implementation
* Proper usage of assert

---

## 🏗 Project Structure

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
├─ README.mdsrc/
├─ tests/
│ ├─ test_tasks.py
│ ├─ test_services.py
│ ├─ test_storage.py
```

---

## ▶️ How to Run

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

---

## ⚔️ Challenges Faced

During development, several important challenges appeared:

* Persistence not saving correctly at first
* AttributeError when testing storage
* Initial difficulties with virtual environments
* Understanding monkeypatch and test isolation

Each challenge was solved through debugging, reading error messages, and refactoring.

---

## 📈 Future Improvements

* Implement SQLite database
* Build an API using FastAPI
* Add a task history system
* Improve error handling
* Add test coverage reporting

---

## 💡 Project Goal

More than just a task manager, this project represents practical growth in Python, testing, and software organization.

It demonstrates the transition from simple scripts to a more market-ready project structure.

---

Built for study, practice, and continuous improvement 🚀

## 🔹License

MIT License © 2026 Giovani Bocafoli