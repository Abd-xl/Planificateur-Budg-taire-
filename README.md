# Planificateur Budgétaire

A simple, lightweight web-based budget planning application built with Python and Flask. This tool allows users to track their income and expenses, calculate their current balance, and view basic statistics.

## 🚀 Features

- **Track Income**: Add income with a source and amount.
- **Track Expenses**: Add expenses with a motif and amount.
- **Real-time Balance**: Automatically calculates and displays your current balance (in Fcfa).
- **Transaction History**: View lists of all income and expense transactions.
- **Statistics**: Get an overview of total income, total expenses, and transaction counts.
- **Data Persistence**: Data is stored locally in a JSON file.
- **Reset Functionality**: Easily clear all data to start fresh.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Framework**: Flask
- **Frontend**: HTML5, CSS3 (using Jinja2 templates)
- **Data Storage**: JSON

## 📋 Requirements

- Python 3.6 or higher
- Flask

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Planificateur-Budg-taire-
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv env
   # On Windows
   .\env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**:
   
   ```bash
   pip install Flask
   ```

## 🏃 Running the Application

To start the development server:

```bash
python main.py
```

The application will be available at `http://localhost:5000`.

## 📂 Project Structure

```text
.
├── budget_data.json     # Local database (JSON format)
├── gestion.py           # Core logic and BudgetManager class
├── main.py              # Flask application entry point
├── static/              # Static files
│   └── css/
│       └── main.css     # Main stylesheet
├── templates/           # HTML templates
│   ├── base.html        # Base layout
│   └── index.html       # Main application page
└── env/                 # Virtual environment (ignored by git)
```

## 🔐 Environment Variables

No specific environment variables are required for basic operation. The Flask app uses a hardcoded `secret_key` in `main.py` which should be moved to an environment variable in a production environment.

- `TODO`: Move `app.secret_key` to an environment variable for better security.

## 🧪 Tests

Currently, there are no automated tests for this project.
- `TODO`: Add unit tests for `BudgetManager` in `gestion.py`.

## 📝 Scripts

- `python main.py`: Starts the Flask development server.

## 📄 License

...

---
*Last updated: 2026-06-24*
