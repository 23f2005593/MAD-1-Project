# Watchman Entry Book App

A simple Flask-based CRUD (Create, Read, Update, Delete) application to manage entries in a database. This app allows users to add, update, delete, and search for entries.

---

## Features
- Add new entries with a name.
- View all entries with their IDs and timestamps.
- Update existing entries.
- Delete entries.
- Search for entries by ID.

---

## Prerequisites
- Python 3.7 or higher
- Flask and its dependencies (see `requirements.txt`)

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/devloperhs14/MAD-1-Project-Practice.git
   cd MAD-1-Project-Practice
   ```

2. **Create a Virtual Environment (Optional but Recommended):**
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up the Database:**
   ```bash
   >> flask db init
   >> flask db migrate -m "Initial migration."
   >> flask db upgrade
   ```

---

## Running the Application
1. **Run the Flask App:**
   ```bash
   python app.py
   ```

2. **Access the App:**
   Open your browser and go to: `http://127.0.0.1:5000/`

---

## Usage

### Add a New Entry
Use the form on the homepage to add a new entry by entering a name and clicking "Submit."

### View All Entries
All entries are displayed on the homepage with their IDs, names, and timestamps.

### Update an Entry
Click the "Update" button next to an entry, enter a new name, and submit.

### Delete an Entry
Click the "Delete" button next to an entry to remove it.

### Search for an Entry
Use the search bar to find an entry by its ID. The result will be displayed below the search bar.

---

## Project Structure
```
MAD-1-PROJECT-PRACTICE/
├── app.py
├── config.py
├── database.py
├── forms.py
├── models.py
├── templates/
│   └── index.html
├── .gitignore
├── README.md
└── requirements.txt
```

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

---

## Contact
**Name:** Harsh
**GitHub:** [devloperhs14](https://github.com/devloperhs14)

