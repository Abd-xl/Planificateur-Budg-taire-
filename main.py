from datetime import datetime

income = []
depense = []
solde = 0

def ajouter_entres():
    global income, solde
    print("Ajout Income")
    while True:
        try:
            montant = float(input("Montant : "))
            break
        except ValueError:
            print("Tchai")
    entres = {
        "montant" : montant,
        "source" : input("Une Source ?: "),
        "date" : datetime.now().strftime("%d/%m/%Y"),
    }
    income.append(entres)
    solde += entres["montant"]

def ajouter_depense():
    global depense, solde
    print("Ajout de dépense")
    while True:
        try:
            montant = float(input("Montant : "))
            break
        except ValueError:
            print("Tchai")
    sorties = {
        "montant" : montant,
        "motif" : input("Un motif?: "),
        "date" : datetime.now().strftime("%d/%m/%Y"),
    }
    depense.append(sorties)
    solde -= sorties["montant"]

def voir_solde():
    global solde
    print(f"Votre solde est : {solde}")

while True:
    print("\nMenu\n")
    print("1. Ajouter Income")
    print("2. Ajouter Depense")
    print("3. Voir solde")
    print("4. Quitter")

    choice = input("Choix ?: ")
    if choice == '1':
        ajouter_entres()
    elif choice == '2':
        ajouter_depense()
    elif choice == '3':
        voir_solde()
    elif choice == '4':
        break
    else:
        print("Tchai")
