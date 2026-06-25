from datetime import datetime
import json
import os

class BudgetManager:
    def __init__(self, data_file='budget_data.json'):
        self.data_file = data_file

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return self._get_default_data()
        return self._get_default_data()

    def save_data(self, data):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _get_default_data(self):
        return {'income': [], 'depense': [], 'emprunts': [], 'solde': 0}

    def valider_texte(self, texte):
        if not texte or not texte.strip():
            return False
        return texte.replace(' ', '').isalnum()

    def valider_montant(self, montant):
        try:
            montant_float = float(montant)
            return montant_float > 0
        except (ValueError, TypeError):
            return False

    def ajouter_income(self, montant, source):

        if not self.valider_montant(montant):
            return False, "Montant invalide. Doit être un nombre positif."

        if not self.valider_texte(source):
            return False, "Source invalide. Pas de caractères spéciaux."

        data = self.load_data()

        entree = {
            "montant": float(montant),
            "source": source.strip(),
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        data['income'].append(entree)
        data['solde'] += entree['montant']


        self.save_data(data)

        return True, f"Revenu de {entree['montant']:.0f} Fcfa ajouté avec succès!"

    def ajouter_depense(self, montant, motif):


        if not self.valider_montant(montant):
            return False, "Montant invalide. Doit être un nombre positif."

        if not self.valider_texte(motif):
            return False, "Motif invalide. Pas de caractères spéciaux."

        data = self.load_data()

        sortie = {
            "montant": float(montant),
            "motif": motif.strip(),
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        data['depense'].append(sortie)
        data['solde'] -= sortie['montant']


        self.save_data(data)

        return True, f"Dépense de {sortie['montant']:.0f} Fcfa ajoutée avec succès!"

    def get_solde(self):

        data = self.load_data()
        return data['solde']

    def get_income_list(self):

        data = self.load_data()
        return data['income']

    def get_depense_list(self):

        data = self.load_data()
        return data['depense']
    
    def get_emprunt_list(self):

        data = self.load_data()
        return data['emprunts']

    def get_statistiques(self):

        data = self.load_data()

        total_income = sum(item['montant'] for item in data['income'])
        total_depense = sum(item['montant'] for item in data['depense'])
        total_emprunts = sum(item['montant'] for item in data['emprunts'])

        return {
            'total_income': total_income,
            'total_depense': total_depense,
            'total_emprunts': total_emprunts,
            'nombre_revenus': len(data['income']),
            'nombre_depenses': len(data['depense']),
            'nombre_emprunts': len(data['emprunts']),
            'solde': data['solde']
        }

    def reset_data(self):

        self.save_data(self._get_default_data())
        return True, "Données réinitialisées avec succès!"

    def supprimer_transaction(self, type_transaction, index):

        data = self.load_data()

        if type_transaction not in ['income', 'depense', 'emprunts']:
            return False, "Type de transaction invalide"

        if index < 0 or index >= len(data[type_transaction]):
            return False, "Transaction introuvable"

        transaction = data[type_transaction][index]
        montant = transaction['montant']

        if type_transaction == 'income':
            data['solde'] -= montant
        elif type_transaction == 'emprunts':
            data['solde'] -= montant
        else:
            data['solde'] += montant

        data[type_transaction].pop(index)

        self.save_data(data)

        return True, f"Transaction de {montant:.0f} Fcfa supprimée!"
    
    def ajouter_emprunt(self, montant, source):
        if not self.valider_montant(montant):
            return False, "Montant invalide. Doit être un nombre positif."

        if not self.valider_texte(source):
            return False, "Source invalide. Pas de caractères spéciaux."

        data = self.load_data()

        emprunt = {
            "montant": float(montant),
            "source": source.strip(),
            "date": datetime.now().strftime("%d/%m/%Y %H:%M")
        }

        if 'emprunts' not in data:
            data['emprunts'] = []

        data['emprunts'].append(emprunt)
        data['solde'] += emprunt['montant']

        self.save_data(data)

        return True, f"Emprunt de {emprunt['montant']:.0f} Fcfa ajouté avec succès!"