from datetime import datetime

def valider_saisie_texte(message):
    while True:

        source = input(message).strip()
        if not source:
            return None

        if not source.isalnum():
            print("Pas de caractère speciaux pls")
        else:
            return source

def saisir_montant(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Tchai")

def ajouter_entres(income_, solde_):

    print("Ajout Income")
    montant = saisir_montant("Montant ?: ")
    source = valider_saisie_texte("Une Source ?: ")

    entres = {
        "montant" : montant,
        "source" : source,
        "date" : datetime.now().strftime("%d/%m/%Y"),
    }

    income_.append(entres)
    solde_ += entres["montant"]
    return income_, solde_

def ajouter_depense(depense_,solde_ ):

    print("Ajout de dépense")
    montant = saisir_montant("Montant ?: ")
    motif = valider_saisie_texte("Un motif ?: ")

    sorties = {
        "montant" : montant,
        "motif" : motif,
        "date" : datetime.now().strftime("%d/%m/%Y"),
    }
    depense_.append(sorties)
    solde_ -= sorties["montant"]
    return depense_, solde_

def voir_solde(solde_):
    print(f"Votre solde est : {solde_:.0f} Fcfa ")

def voir_income(income_):
    if not income_:
        print("Aucun revenu enregistré.")
        return
    print("\n--- Historique des revenus ---")
    for x in income_:
        print(f"{x['date']} | +{x['montant']:.0f} Fcfa | {x['source']} ")

def voir_depense(depense_):
    if not depense_:
        print("Aucune depense enregistré.")
        return
    print("\n--- Historique des depenses ---")
    for x in depense_:
        print(f"{x['date']} | -{x['montant']:.0f} Fcfa | {x['motif']} ")

income = []
depense = []
solde = 0

while True:
    print("\nMenu\n")
    print("1. Ajouter Income")
    print("2. Ajouter Depense")
    print("3. Voir solde")
    print("4. voir income")
    print("5. Voir depense")
    print("6. Quitter")


    choice = input("\nChoix ?: ")
    if choice == '1':
        income, solde = ajouter_entres(income, solde)
    elif choice == '2':
        depense, solde = ajouter_depense(depense, solde)
    elif choice == '3':
        voir_solde(solde)
    elif choice == '4':
        voir_income(income)
    elif choice == '5':
        voir_depense(depense)
    elif choice == '6':
        break
    else:
        print("Tchai")
