import os
from flask import Flask, render_template, request, redirect, url_for, flash
from gestion import BudgetManager

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'cle_secrete_de_dev')

budget_manager = BudgetManager('budget_data.json')


@app.route('/')
def index():
    data = budget_manager.load_data()
    stats = budget_manager.get_statistiques()

    return render_template('index.html',
                         solde=data['solde'],
                         income_list=data['income'],
                         depense_list=data['depense'],
                         stats=stats)


@app.route('/ajouter_income', methods=['POST'])
def ajouter_income():

    montant = request.form.get('montant')
    source = request.form.get('source')

    success, message = budget_manager.ajouter_income(montant, source)

    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')

    return redirect(url_for('index'))


@app.route('/ajouter_depense', methods=['POST'])
def ajouter_depense():

    montant = request.form.get('montant')
    motif = request.form.get('motif')

    success, message = budget_manager.ajouter_depense(montant, motif)

    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')

    return redirect(url_for('index'))


@app.route('/supprimer/<type_transaction>/<int:index>', methods=['POST'])
def supprimer_transaction(type_transaction, index):

    success, message = budget_manager.supprimer_transaction(type_transaction, index)

    if success:
        flash(message, 'success')
    else:
        flash(message, 'error')

    return redirect(url_for('index'))


@app.route('/reset', methods=['POST'])
def reset():

    success, message = budget_manager.reset_data()
    flash(message, 'info')
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
