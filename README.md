# Planificateur Budgétaire

A simple, lightweight web-based budget planning application built with Python and Flask. This tool allows users to track their income and expenses, calculate their current balance, and view basic statistics.

## 🚀 Features

- **Track Income**: Add income with a source and amount.
- **Track Expenses**: Add expenses with a motif and amount.
- **Real-time Balance**: Automatically calculates and displays your current balance (in Fcfa).
- **Transaction History**: View lists of income and expense transactions.
- **Statistics**: Get an overview of total income, total expenses, and transaction counts.
- **Data Persistence**: Data is stored locally in a JSON file.
- **Reset Functionality**: Clear all data and start fresh.

## 🔧 En cours / À améliorer

- Le support des **emprunts** est partiellement implémenté dans `gestion.py`, mais il n’est pas encore exposé dans l’interface utilisateur.
- L’interface actuelle affiche seulement les revenus et les dépenses.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Framework**: Flask
- **Frontend**: HTML5, CSS3 (Jinja2 templates)
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

4. **Set `FLASK_SECRET_KEY` in the environment**
   - On Linux/macOS:
     ```bash
     export FLASK_SECRET_KEY="ta_cle_secrete"
     ```
   - On Windows PowerShell:
     ```powershell
     $env:FLASK_SECRET_KEY = "ta_cle_secrete"
     ```

5. **Do not share a secret key publicly**
   - If you want to keep it local, add `KEY.env` to `.gitignore` but do not require it.

## 🏃 Running the Application

To start the development server:

```bash
python main.py
```

Then open `http://localhost:5000`.

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
├── KEY.env              # Local environment variables (do not commit)
└── env/                 # Virtual environment (ignored by git)
```

## 🔐 Environment Variables

The application reads `FLASK_SECRET_KEY` from the environment.

- `FLASK_SECRET_KEY` is used by Flask to sign sessions and secure cookies.
- If `FLASK_SECRET_KEY` is missing, the app falls back to a default development key.
- In production, do not rely on the fallback key.


## 🚀 Next steps

- Ajouter l’interface et la route pour gérer les emprunts.
- Afficher les emprunts dans le tableau de bord et dans les statistiques.
- Envisager SQLite pour un stockage plus fiable.

## 📄 License

...

---
*Last updated: 2026-06-25*
