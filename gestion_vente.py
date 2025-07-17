# -*- coding: utf-8 -*-
"""
Système de Gestion des Ventes
Application principale avec interface graphique Tkinter
"""

import tkinter as tk
from tkinter import ttk
import gestion_vente_module as gvm

def main():
    """Fonction principale de l'application"""
    # Création de la fenêtre principale
    app = tk.Tk()
    app.title('Gestion des Ventes en Ligne')
    app.geometry("1200x700")
    app.configure(bg='#f5f5f5')
    
    # Configuration de l'icône et des propriétés de fenêtre
    app.resizable(True, True)
    app.minsize(800, 600)
    
    # Création du menu principal
    menubar = tk.Menu(app)
    app.config(menu=menubar)
    
    # Menu Clients
    client_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Clients", menu=client_menu)
    client_menu.add_command(label="Accueil", command=lambda: gvm.home_interface(app))
    client_menu.add_command(label="Ajouter Client", command=lambda: gvm.add_client_form(app))
    client_menu.add_command(label="Afficher Client", command=lambda: gvm.client_command_form(app))
    client_menu.add_separator()
    client_menu.add_command(label="Quitter", command=app.quit)
    
    # Menu Commandes
    command_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Commandes", menu=command_menu)
    command_menu.add_command(label="Nouvelle Commande", command=lambda: gvm.add_command_form(app))
    command_menu.add_command(label="Total Commande", command=lambda: gvm.command_total_form(app))
    
    # Menu Aide
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Aide", menu=help_menu)
    help_menu.add_command(label="À propos", command=lambda: show_about(app))
    
    # Stocker la référence du menu pour le module
    app.menu = menubar
    
    # Initialisation de l'interface d'accueil
    gvm.home_interface(app)
    
    # Barre d'état
    status_bar = tk.Label(app, text="Prêt", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Lancement de l'application
    app.mainloop()

def show_about(app):
    """Affiche la fenêtre À propos"""
    about_window = tk.Toplevel(app)
    about_window.title("À propos")
    about_window.geometry("400x300")
    about_window.resizable(False, False)
    
    # Centrer la fenêtre
    about_window.transient(app)
    about_window.grab_set()
    
    # Contenu de la fenêtre
    tk.Label(about_window, text="Gestion des Ventes", font=("Arial", 16, "bold"), fg="#2196F3").pack(pady=20)
    tk.Label(about_window, text="Version 2.0", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_window, text="Application de gestion des clients et commandes", font=("Arial", 10)).pack(pady=10)
    
    features_text = """
    Fonctionnalités:
    • Gestion des clients (ajout, modification, suppression)
    • Gestion des commandes
    • Calcul automatique des totaux
    • Vérification des stocks
    • Interface utilisateur améliorée
    """
    
    tk.Label(about_window, text=features_text, font=("Arial", 9), justify=tk.LEFT).pack(pady=10)
    
    tk.Button(about_window, text="Fermer", command=about_window.destroy, 
              bg="#607D8B", fg="white", padx=20, pady=5).pack(pady=20)

if __name__ == "__main__":
    main()