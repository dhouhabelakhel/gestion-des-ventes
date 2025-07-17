from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from datetime import datetime

# Données globales
clients = []
articles = [
    {'code_article': 'A001', 'libelle': 'Ordinateur portable', 'quantite_stock': 10, 'prix_unitaire': 800},
    {'code_article': 'A002', 'libelle': 'Smartphone', 'quantite_stock': 20, 'prix_unitaire': 600},
    {'code_article': 'A003', 'libelle': 'Tablette', 'quantite_stock': 15, 'prix_unitaire': 400},
    {'code_article': 'A004', 'libelle': 'Écouteurs sans fil', 'quantite_stock': 30, 'prix_unitaire': 100},
    {'code_article': 'A005', 'libelle': 'Imprimante', 'quantite_stock': 5, 'prix_unitaire': 300},
]
commandes = []
command_row = 5
selected_articles = []
cal = None

def clear_interface(app):
    """Nettoie l'interface en gardant le menu"""
    for widget in app.winfo_children():
        if hasattr(app, 'menu') and widget != app.menu:
            widget.destroy()

def find_client_by_code(code):
    """Trouve un client par son code"""
    for client in clients:
        if str(client['code']) == str(code):
            return client
    return None

def find_article_by_libelle(libelle):
    """Trouve un article par son libellé"""
    for article in articles:
        if article['libelle'] == libelle:
            return article
    return None

def add_client(app, new_client):
    """Ajoute un nouveau client"""
    # Vérification des champs vides
    if not all([new_client['code'], new_client['nom'], new_client['prenom'], new_client['adresse']]):
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs!")
        return False
    
    # Vérification de l'existence du client
    if find_client_by_code(new_client['code']):
        messagebox.showerror("Erreur", "Ce client existe déjà!")
        return False
    
    clients.append(new_client)
    messagebox.showinfo("Succès", "Client ajouté avec succès!")
    
    # Demander si on veut ajouter une commande
    if messagebox.askyesno("Commande", "Voulez-vous ajouter une commande pour ce client?"):
        add_command_form(app, new_client['code'])
    else:
        home_interface(app)
    
    return True

def modify_client(app, code, updated_client):
    """Modifie un client existant"""
    print(f"Tentative de modification du client avec code: {code}")  # Debug
    client = find_client_by_code(code)
    if not client:
        print(f"Client non trouvé. Codes disponibles: {[c['code'] for c in clients]}")  # Debug
        messagebox.showerror("Erreur", "Client non trouvé!")
        return False
    
    # Vérification des champs vides
    if not all([updated_client['nom'], updated_client['prenom'], updated_client['adresse']]):
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs!")
        return False
    
    # Mise à jour des informations
    client['nom'] = updated_client['nom']
    client['prenom'] = updated_client['prenom']
    client['adresse'] = updated_client['adresse']
    
    messagebox.showinfo("Succès", "Client modifié avec succès!")
    home_interface(app)
    return True

def delete_client(app, code):
    """Supprime un client"""
    print(f"Tentative de suppression du client avec code: {code}")  # Debug
    client = find_client_by_code(code)
    if not client:
        print(f"Client non trouvé. Codes disponibles: {[c['code'] for c in clients]}")  # Debug
        messagebox.showerror("Erreur", "Client non trouvé!")
        return False
    
    if messagebox.askyesno("Confirmation", f"Êtes-vous sûr de vouloir supprimer le client {client['nom']} {client['prenom']}?"):
        clients.remove(client)
        messagebox.showinfo("Succès", "Client supprimé avec succès!")
        home_interface(app)
        return True
    return False

def verif_qte(commande):
    """Vérifie la disponibilité des quantités en stock"""
    for article in commande['articles']:
        code_article = article['code_article']
        qte_cmd = article['qte_cmd']
        for item in articles:
            if item['code_article'] == code_article:
                if qte_cmd > item['quantite_stock']:
                    return False
    return True

def add_commande(app, code, commande):
    """Ajoute une commande à un client"""
    client = find_client_by_code(code)
    if not client:
        messagebox.showerror("Erreur", "Client non trouvé!")
        return False
    
    if not commande['articles']:
        messagebox.showerror("Erreur", "Veuillez ajouter au moins un article!")
        return False
    
    if not verif_qte(commande):
        messagebox.showerror("Erreur", "Quantité insuffisante en stock!")
        return False
    
    # Mettre à jour le stock
    for article in commande['articles']:
        for item in articles:
            if item['code_article'] == article['code_article']:
                item['quantite_stock'] -= article['qte_cmd']
    
    # Ajouter la commande
    num_cmd = len(commandes) + 1
    nouvelle_commande = {'num_cmd': num_cmd, 'commande': commande, 'client_code': code}
    client['commandes'].append(nouvelle_commande)
    commandes.append(nouvelle_commande)
    
    messagebox.showinfo("Succès", "Commande ajoutée avec succès!")
    selected_articles.clear()
    home_interface(app)
    return True

def total_cmd(num_cmd):
    """Calcule le total d'une commande"""
    total = 0
    for commande in commandes:
        if commande['num_cmd'] == num_cmd:
            for article in commande['commande']['articles']:
                for prix_article in articles:
                    if prix_article['code_article'] == article['code_article']:
                        total += prix_article['prix_unitaire'] * article['qte_cmd']
    return total

def nbr_cmd(code):
    """Compte le nombre de commandes d'un client"""
    client = find_client_by_code(code)
    return len(client['commandes']) if client else 0

def add_articles(article_libelle, qte_cmd):
    """Ajoute un article à la sélection"""
    if not qte_cmd or int(qte_cmd) <= 0:
        messagebox.showerror("Erreur", "Quantité invalide!")
        return
    
    article = find_article_by_libelle(article_libelle)
    if article:
        selected_articles.append({
            'code_article': article['code_article'],
            'libelle': article_libelle,
            'qte_cmd': int(qte_cmd)
        })
        messagebox.showinfo("Succès", f"Article {article_libelle} ajouté!")

def show_article(app, event, articles_select):
    """Affiche le formulaire pour ajouter un article à la commande"""
    global row
    article = articles_select.get()
    if not article:
        return
    
    article_label = Label(app, text=article, font=("Arial", 10))
    article_label.grid(row=row, column=5, padx=5, pady=2)
    
    article_qte = tk.Spinbox(app, from_=1, to=200, width=10)
    article_qte.grid(row=row, column=6, padx=5, pady=2)
    
    add_button = Button(app, text="Ajouter", bg="#4CAF50", fg="white",
                       command=lambda: add_articles(article, article_qte.get()))
    add_button.grid(row=row, column=7, padx=5, pady=2)
    
    row += 1

def add_client_form(app):
    """Formulaire d'ajout de client"""
    clear_interface(app)
    
    # Titre
    title_label = Label(app, text="Ajouter un Client", font=("Arial", 20, "bold"), fg="#2196F3")
    title_label.grid(row=0, column=0, columnspan=3, pady=20)
    
    # Champs du formulaire
    fields = [
        ("Code Client:", "code_value"),
        ("Nom:", "nom_value"),
        ("Prénom:", "prenom_value"),
        ("Adresse:", "adresse_value")
    ]
    
    variables = {}
    for i, (label_text, var_name) in enumerate(fields, 1):
        Label(app, text=label_text, font=("Arial", 12, "bold"), fg="#333").grid(row=i, column=0, sticky="e", padx=10, pady=5)
        variables[var_name] = StringVar()
        Entry(app, textvariable=variables[var_name], font=("Arial", 11), width=25).grid(row=i, column=1, padx=10, pady=5)
    
    # Boutons
    button_frame = Frame(app)
    button_frame.grid(row=len(fields)+1, column=0, columnspan=3, pady=20)
    
    Button(button_frame, text="Ajouter", bg="#4CAF50", fg="white", padx=20, pady=10,
           command=lambda: add_client(app, {
               'code': variables['code_value'].get(),
               'nom': variables['nom_value'].get(),
               'prenom': variables['prenom_value'].get(),
               'adresse': variables['adresse_value'].get(),
               'commandes': []
           })).pack(side=LEFT, padx=5)
    
    Button(button_frame, text="Annuler", bg="#f44336", fg="white", padx=20, pady=10,
           command=lambda: home_interface(app)).pack(side=LEFT, padx=5)

def modify_client_form(app, code):
    """Formulaire de modification de client"""
    client = find_client_by_code(code)
    if not client:
        messagebox.showerror("Erreur", "Client non trouvé!")
        return
    
    clear_interface(app)
    
    # Titre
    title_label = Label(app, text="Modifier le Client", font=("Arial", 20, "bold"), fg="#FF9800")
    title_label.grid(row=0, column=0, columnspan=3, pady=20)
    
    # Champs du formulaire
    fields = [
        ("Code Client:", "code_value", client['code'], True),
        ("Nom:", "nom_value", client['nom'], False),
        ("Prénom:", "prenom_value", client['prenom'], False),
        ("Adresse:", "adresse_value", client['adresse'], False)
    ]
    
    variables = {}
    for i, (label_text, var_name, default_value, readonly) in enumerate(fields, 1):
        Label(app, text=label_text, font=("Arial", 12, "bold"), fg="#333").grid(row=i, column=0, sticky="e", padx=10, pady=5)
        variables[var_name] = StringVar(value=default_value)
        entry = Entry(app, textvariable=variables[var_name], font=("Arial", 11), width=25)
        if readonly:
            entry.configure(state='readonly')
        entry.grid(row=i, column=1, padx=10, pady=5)
    
    # Boutons
    button_frame = Frame(app)
    button_frame.grid(row=len(fields)+1, column=0, columnspan=3, pady=20)
    
    Button(button_frame, text="Modifier", bg="#FF9800", fg="white", padx=20, pady=10,
           command=lambda: modify_client(app, code, {
               'nom': variables['nom_value'].get(),
               'prenom': variables['prenom_value'].get(),
               'adresse': variables['adresse_value'].get()
           })).pack(side=LEFT, padx=5)
    
    Button(button_frame, text="Annuler", bg="#f44336", fg="white", padx=20, pady=10,
           command=lambda: home_interface(app)).pack(side=LEFT, padx=5)

def get_selected_date():
    """Récupère la date sélectionnée"""
    return cal.get_date() if cal else datetime.now().strftime("%Y-%m-%d")

def add_command_form(app, code=None):
    """Formulaire d'ajout de commande"""
    global cal, row, selected_articles
    selected_articles = []
    row = 6
    
    clear_interface(app)
    
    # Titre
    title_label = Label(app, text=f"Commande n° : {len(commandes)+1}", font=("Arial", 18, "bold"), fg="#2196F3")
    title_label.grid(row=0, column=0, columnspan=8, pady=10)
    
    # Code client
    Label(app, text="Code Client:", font=("Arial", 12, "bold"), fg="#333").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    code_value = StringVar()
    code_entry = Entry(app, textvariable=code_value, font=("Arial", 11))
    code_entry.grid(row=1, column=1, padx=10, pady=5)
    
    # Date
    Label(app, text="Date:", font=("Arial", 12, "bold"), fg="#333").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    cal = Calendar(app, selectmode='day', date_pattern='y-mm-dd')
    cal.grid(row=2, column=1, padx=10, pady=5)
    
    # Articles
    Label(app, text="Articles:", font=("Arial", 12, "bold"), fg="#333").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    articles_select = ttk.Combobox(app, values=[article['libelle'] for article in articles], state="readonly", width=20)
    articles_select.grid(row=3, column=1, padx=10, pady=5)
    articles_select.bind("<<ComboboxSelected>>", lambda event: show_article(app, event, articles_select))
    
    # En-têtes pour les articles sélectionnés
    Label(app, text="Article", font=("Arial", 10, "bold")).grid(row=4, column=5, padx=5, pady=2)
    Label(app, text="Quantité", font=("Arial", 10, "bold")).grid(row=4, column=6, padx=5, pady=2)
    Label(app, text="Action", font=("Arial", 10, "bold")).grid(row=4, column=7, padx=5, pady=2)
    
    # Boutons
    button_frame = Frame(app)
    button_frame.grid(row=5, column=0, columnspan=8, pady=20)
    
    Button(button_frame, text="Valider Commande", bg="#4CAF50", fg="white", padx=20, pady=10,
           command=lambda: add_commande(app, code_value.get(), {
               'date': get_selected_date(),
               'articles': selected_articles.copy()
           })).pack(side=LEFT, padx=5)
    
    Button(button_frame, text="Annuler", bg="#f44336", fg="white", padx=20, pady=10,
           command=lambda: home_interface(app)).pack(side=LEFT, padx=5)
    
    if code:
        code_value.set(code)
        code_entry.configure(state='readonly')

def home_interface(app):
    """Interface principale avec tableau des clients"""
    clear_interface(app)
    
    # Titre
    title_label = Label(app, text="Gestion des Clients", font=("Arial", 20, "bold"), fg="#2196F3")
    title_label.pack(pady=10)
    
    # Frame pour le tableau
    table_frame = Frame(app)
    table_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
    # Colonnes du tableau
    columns = ('Code', 'Nom', 'Prénom', 'Adresse', 'Nb Commandes')
    tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
    
    # Configuration des colonnes
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor='center')
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    # Placement
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Remplissage du tableau
    for client in clients:
        tree.insert("", "end", values=(
            client['code'],
            client['nom'],
            client['prenom'],
            client['adresse'],
            len(client['commandes'])
        ))
    
    # Boutons d'action
    button_frame = Frame(app)
    button_frame.pack(pady=10)
    
    def on_modify():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner un client!")
            return
        code = str(tree.item(selected[0])['values'][0])
        print(f"Code sélectionné pour modification: {code}")  
        modify_client_form(app, code)
    
    def on_delete():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner un client!")
            return
        code = str(tree.item(selected[0])['values'][0])
        print(f"Code sélectionné pour suppression: {code}")  
        delete_client(app, code)
    
    def on_view():
        selected = tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner un client!")
            return
        code = str(tree.item(selected[0])['values'][0])
        print(f"Code sélectionné pour affichage: {code}")  
        affiche_client(app, code)
    
    Button(button_frame, text="Modifier", bg="#FF9800", fg="white", padx=15, pady=5,
           command=on_modify).pack(side=LEFT, padx=5)
    
    Button(button_frame, text="Supprimer", bg="#f44336", fg="white", padx=15, pady=5,
           command=on_delete).pack(side=LEFT, padx=5)
    
    Button(button_frame, text="Voir Détails", bg="#2196F3", fg="white", padx=15, pady=5,
           command=on_view).pack(side=LEFT, padx=5)

def affiche_client(app, code):
    """Affiche les détails d'un client et ses commandes"""
    client = find_client_by_code(code)
    if not client:
        messagebox.showerror("Erreur", "Client non trouvé!")
        return
    
    clear_interface(app)
    
    # Informations du client
    info_frame = LabelFrame(app, text="Informations Client", font=("Arial", 12, "bold"), fg="#2196F3")
    info_frame.pack(fill=X, padx=20, pady=10)
    
    Label(info_frame, text=f"Code: {client['code']}", font=("Arial", 11)).grid(row=0, column=0, sticky="w", padx=10, pady=5)
    Label(info_frame, text=f"Nom: {client['nom']}", font=("Arial", 11)).grid(row=0, column=1, sticky="w", padx=10, pady=5)
    Label(info_frame, text=f"Prénom: {client['prenom']}", font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=10, pady=5)
    Label(info_frame, text=f"Adresse: {client['adresse']}", font=("Arial", 11)).grid(row=1, column=1, sticky="w", padx=10, pady=5)
    
    # Commandes
    if client['commandes']:
        cmd_frame = LabelFrame(app, text="Commandes", font=("Arial", 12, "bold"), fg="#4CAF50")
        cmd_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        for i, commande in enumerate(client['commandes']):
            cmd_info = Frame(cmd_frame)
            cmd_info.pack(fill=X, padx=10, pady=5)
            
            Label(cmd_info, text=f"Commande n° {commande['num_cmd']}", font=("Arial", 11, "bold")).pack(anchor="w")
            Label(cmd_info, text=f"Date: {commande['commande']['date']}", font=("Arial", 10)).pack(anchor="w")
            Label(cmd_info, text=f"Total: {total_cmd(commande['num_cmd'])} €", font=("Arial", 10), fg="#FF5722").pack(anchor="w")
            
            # Articles de la commande
            articles_text = "Articles: "
            for article in commande['commande']['articles']:
                articles_text += f"{article['libelle']} (x{article['qte_cmd']}), "
            Label(cmd_info, text=articles_text[:-2], font=("Arial", 9), fg="#666").pack(anchor="w")
            
            ttk.Separator(cmd_frame, orient='horizontal').pack(fill=X, pady=5)
    else:
        Label(app, text="Aucune commande pour ce client", font=("Arial", 12), fg="#999").pack(pady=20)
    
    # Bouton retour
    Button(app, text="Retour", bg="#607D8B", fg="white", padx=20, pady=10,
           command=lambda: home_interface(app)).pack(pady=10)

def command_total_form(app):
    """Formulaire pour calculer le total d'une commande"""
    clear_interface(app)
    
    title_label = Label(app, text="Calculer le Total d'une Commande", font=("Arial", 18, "bold"), fg="#2196F3")
    title_label.pack(pady=20)
    
    frame = Frame(app)
    frame.pack(pady=20)
    
    Label(frame, text="Numéro de commande:", font=("Arial", 12, "bold")).pack(side=LEFT, padx=10)
    
    num_cmd_value = StringVar()
    Entry(frame, textvariable=num_cmd_value, font=("Arial", 11), width=15).pack(side=LEFT, padx=10)
    
    def show_total():
        try:
            num_cmd = int(num_cmd_value.get())
            total = total_cmd(num_cmd)
            if total > 0:
                result_label.config(text=f"Total: {total} €", fg="#4CAF50")
            else:
                result_label.config(text="Commande non trouvée", fg="#f44336")
        except ValueError:
            result_label.config(text="Numéro invalide", fg="#f44336")
    
    Button(frame, text="Calculer", bg="#4CAF50", fg="white", padx=15, pady=5,
           command=show_total).pack(side=LEFT, padx=10)
    
    result_label = Label(app, text="", font=("Arial", 14, "bold"))
    result_label.pack(pady=20)
    
    Button(app, text="Retour", bg="#607D8B", fg="white", padx=20, pady=10,
           command=lambda: home_interface(app)).pack(pady=10)

def client_command_form(app):
    """Formulaire pour afficher les commandes d'un client"""
    clear_interface(app)
    
    title_label = Label(app, text="Afficher les Commandes d'un Client", font=("Arial", 18, "bold"), fg="#2196F3")
    title_label.pack(pady=20)
    
    frame = Frame(app)
    frame.pack(pady=20)
    
    Label(frame, text="Code Client:", font=("Arial", 12, "bold")).pack(side=LEFT, padx=10)
    
    code_value = StringVar()
    Entry(frame, textvariable=code_value, font=("Arial", 11), width=15).pack(side=LEFT, padx=10)
    
    Button(frame, text="Afficher", bg="#4CAF50", fg="white", padx=15, pady=5,
           command=lambda: affiche_client(app, code_value.get())).pack(side=LEFT, padx=10)
    
    Button(app, text="Retour", bg="#607D8B", fg="white", padx=20, pady=10,
           command=lambda: home_interface(app)).pack(pady=10)