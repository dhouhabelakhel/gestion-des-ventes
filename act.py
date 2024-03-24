# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:31:18 2024

@author: user
"""
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox

clients=[]
articles = [
    {'code': 'A001', 'libelle': 'Ordinateur portable', 'quantite_stock': 10, 'prix_unitaire': 800},
    {'code': 'A002', 'libelle': 'Smartphone', 'quantite_stock': 20, 'prix_unitaire': 600},
    {'code': 'A003', 'libelle': 'Tablette', 'quantite_stock': 15, 'prix_unitaire': 400},
    {'code': 'A004', 'libelle': 'Écouteurs sans fil', 'quantite_stock': 30, 'prix_unitaire': 100},
    {'code': 'A005', 'libelle': 'Imprimante', 'quantite_stock': 5, 'prix_unitaire': 300},
]
def add_client(new_client):
    for client in clients:
        if client['code']==new_client['code']:
            messagebox.showerror("Erreur", "Ce client existe déjà!")
            return FALSE
    if new_client['code']=='' or new_client['nom']=='' or new_client['prenom']=='' or new_client['adresse']=='' :
            messagebox.showerror("Erreur", "fill all the inputs!")
    clients.append(new_client)
    add_command_form()
    print (clients)
    return TRUE
def verif_qte(commande):
    for article in commande['articles']:
        if article['qte_cmd']>articles[article['code_article']]:
            return False
    return True
        
def add_commande(code,commande):
    for client in clients:
        if client['code']==code:
            if verif_qte(commande):
                client['commande'].append(commande)
            
def articles_commande(num_cmd,articles):
    for client in clients:
        for commande in client['commande']:
            if commande['num_cmd']==num_cmd:
                commande['articles'].append(articles)
                return
def total_cmd(num_cmd):
    total=0
    for client in clients:
        for commande in client['commandes']:
            if commande['num_cmd']==num_cmd:
                for article in commande['articles']:
                    for prix_article in articles:
                        if prix_article['code']==article['code']:
                            total=total+(prix_article['PU']*article['qte_cmd'])
    return total
def affiche(code):
    for client in clients:
        if client['code']==code:
            print('nom :'+client['nom'])
            print('prenom :'+client['prenom'])
            print('adresse :'+client['adresse'])
            for commande in client['commandes']:
                print('num_commande :'+commande['num_cmd'])
                print('date'+commande['date'])
                print('total de la commande : '+total_cmd(commande['num_cmd']))
def nbr_cmd(code):
    nbre=0
    for client in clients:
        if client['code']==code:
            nbre=len(client['commnade'])
    return nbre
def nbr_cmd_client(code,nom):
    nbre=0
    for client in clients:
        if client['code']==code and client['nom']==nom:
            nbre=len(client['commnade'])
    return nbre

app=Tk()
app.geometry("800x500")
app.title('gestion des ventes en lignes')
Title=Label(app,text="'Gestion des ventes en lignes :",font="Script 35 bold", fg="#bd0b49",pady=10).grid(row=0,column=0,columnspan=2)
def add_client_form():
    code_client_label = Label(app,text="Code " ,font="Script 25 bold", fg="#bd0b49",pady=10).grid(row=1,column=1)
    nom_label= Label(app,text="nom ",font="Script 25 bold",fg="#bd0b49",pady=10).grid(row=2,column=1)
    prenom_label= Label(app,text="prenom ",font="Script 25 bold",fg="#bd0b49",pady=10).grid(row=3,column=1)
    adresse_label=Label(app,text="adresse ",font="Script 25 bold",fg="#bd0b49",pady=10).grid(row=4,column=1)
    code_value=StringVar()
    nom_value=StringVar()
    prenom_value=StringVar()
    adresse_value=StringVar()
    code=Entry(textvariable=code_value).grid(row=1,column=2)
    nom=Entry(textvariable=nom_value).grid(row=2,column=2)
    prenom=Entry(textvariable=prenom_value).grid(row=3,column=2)
    code=Entry(textvariable=adresse_value).grid(row=4,column=2)
    confirm_button=Button(text="add",padx=5,pady=5 ,command=lambda:add_client({'code': code_value.get(), 'nom': nom_value.get(), 'prenom': prenom_value.get(), 'adresse': adresse_value.get(), 'commande': []}))
    confirm_button.place(x=100, y=280)
def add_command_form():
    code_client_label = Label(app,text="Code " ,font="Script 25 bold", fg="#bd0b49",pady=10).grid(row=1,column=1)

menu = tk.Menu(app)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Add Client", command=add_client_form)
file_menu.add_command(label="Add Command", command=add_command_form)

app.config(menu=menu)
app.mainloop()