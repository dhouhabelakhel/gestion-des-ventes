# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:31:18 2024

@author: user
"""
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from tkcalendar import Calendar, DateEntry
clients=[]
articles = (
    {'code_article': 'A001', 'libelle': 'Ordinateur portable', 'quantite_stock': 10, 'prix_unitaire': 800},
    {'code_article': 'A002', 'libelle': 'Smartphone', 'quantite_stock': 20, 'prix_unitaire': 600},
    {'code_article': 'A003', 'libelle': 'Tablette', 'quantite_stock': 15, 'prix_unitaire': 400},
    {'code_article': 'A004', 'libelle': 'Écouteurs sans fil', 'quantite_stock': 30, 'prix_unitaire': 100},
    {'code_article': 'A005', 'libelle': 'Imprimante', 'quantite_stock': 5, 'prix_unitaire': 300},
)
commandes=[]
def add_client(new_client):
    for client in clients:
        if client['code']==new_client['code']:
            messagebox.showerror("Erreur", "Ce client existe déjà!")
            return FALSE
    if new_client['code']=='' or new_client['nom']=='' or new_client['prenom']=='' or new_client['adresse']=='' :
            messagebox.showerror("Erreur", "fill all the inputs!")
    clients.append(new_client)
    messagebox.showerror("Erreur", "insert client command")
    add_command_form(new_client['code'])
    print (clients)
    return TRUE
def verif_qte(commande):
    for article in commande['articles']:
        code_article = article['code_article']
        qte_cmd = article['qte_cmd']
        for item in articles:
            if item['code_article'] == code_article:
                quantite_stock = item['quantite_stock']
                if qte_cmd > quantite_stock:
                    return False
    return True

        
def add_commande(code,commande):
    print(code)
    for client in clients:
        if client['code']==code:
            print('done')
            if verif_qte(commande):
                client['commandes'].append({'num_cmd':len(commandes)+1,'commande':commande})
                commandes.append({'num_cmd':len(commandes)+1,'commande':commande})
                print(client)
 

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
                for article in commande['commande']['articles']:
                    for prix_article in articles:
                        if prix_article['code_article']==article['code_article']:
                            total=total+(prix_article['prix_unitaire']*article['qte_cmd'])
    total_label=Label(app,text=total).grid(row=2,column=1)
def affiche(code):
    clear_interface() 
    for client in clients:
        if client['code']==code:
            nom=Label(app,text=client['nom']).grid(row=2,column=1)
            prenom=Label(app,text=client['prenom']).grid(row=3,column=1)
            adresse=Label(app,text=client['adresse']).grid(row=4,column=1)
            for commande in client['commandes']:
                num_cmd=Label(app,text=commande['num_cmd']).grid(row=5,column=1)
                date=Label(app,text=commande['commande']['date']).grid(row=6,column=1)
                total=Label(app,text=total_cmd(commande['num_cmd'])).grid(row=7,column=1)
def nbr_cmd(code):
    nbre=0
    for client in clients:
        if client['code']==code:
            nbre=len(client['commandes'])
    return nbre
def nbr_cmd_client(code,nom):
    nbre=0
    for client in clients:
        if client['code']==code and client['nom']==nom:
            nbre=len(client['commnades'])
    return nbre

app=Tk()
app.geometry("800x500")
app.title('gestion des ventes en lignes')
def clear_interface():
    for widget in app.winfo_children():
        if widget != menu:
            widget.destroy()
def add_client_form():
    clear_interface()
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
    confirm_button=Button(text="add",padx=5,pady=5 ,command=lambda:add_client({'code': code_value.get(), 'nom': nom_value.get(), 'prenom': prenom_value.get(), 'adresse': adresse_value.get(), 'commandes': []}))
    confirm_button.place(x=100, y=280)
#https://www.plus2net.com/python/tkinter-DateEntry.php
def get_selected_date():
    selected_date = cal.get_date()
    return selected_date
   

     
row=4
selected_articles=[]
def show_article(event,articles_select):
    global row
    article = articles_select.get()
    article_label=Label(app,text=article).grid(row=row,column=5)
    article_qte=tk.Spinbox(app, from_=0, to=100)
    article_qte.grid(row=row,column=6)
    row=row+1
    selected_articles.append({'code_article':article,'qte_cmd':article_qte.get()})
    print(selected_articles)

def add_command_form(code=None):
    clear_interface()
    num_cmd_label=Label(app,text=f"Commande n° : {len(commandes)+1}",font="Script 20 bold", fg="#bd0b49",pady=10).grid(row=1,column=1)
    code_client_label = Label(app,text="Code " ,font="Script 25 bold", fg="#bd0b49",pady=10).grid(row=2,column=1)
    code_value=StringVar()
    
    code_entry=Entry(textvariable=code_value)
    code_entry.grid(row=2,column=2)
    date_label = Label(app,text="Date " ,font="Script 25 bold", fg="#bd0b49",pady=10).grid(row=3,column=1)
    global cal 
    cal = Calendar(app, selectmode='day', year=2024, month=3, day=24)
    cal.grid(row=3, column=2)
    articles_label= Label(app,text="articles  " ,font="Script 25 bold", fg="#bd0b49",pady=10).grid(row=4,column=1)
    articles_select=ttk.Combobox( values=[article['libelle'] for article in articles],state="readonly")
    articles_select.grid(row=4,column=2)
    #https://stackoverflow.com/questions/40641130/how-to-use-a-comboboxselected-virtual-event-with-tkinter
    articles_select.bind("<<ComboboxSelected>>",lambda event: show_article(event, articles_select))
    confirm_button=Button(text="add",command=lambda:add_commande(code_value.get(),
                                                                 {'date':get_selected_date(),
                                                                  'articles': selected_articles })).grid(row=5,column=1)
    if code is not None:
       code_value.set(code)
       code_entry.configure(state='readonly')
   
        

def home_interface():
    clear_interface()
    columns=('code','nom','prenom','adresse','nombre commande')
    tree = ttk.Treeview(app, columns=columns, show="headings")
    for col in columns:
        tree.heading(col,text=col)
    tree.pack(expand=True, fill=tk.BOTH)
    for client in clients:
        code = client['code']
        nom = client['nom']
        prenom = client['prenom']
        adresse = client['adresse']
        nb_commandes =nbr_cmd(client['code'])
        tree.insert("", "end", values=(code, nom, prenom, adresse, nb_commandes))
def command_total_form():
    clear_interface()
    num_cmd_label=Label(app,text="Numero commande").grid(row=1,column=1)
    num_cmd_value=StringVar()
    num_cmd_entry=Entry(textvariable=num_cmd_value).grid(row=1,column=2)
    confirm_button=Button(text="montant ",padx=5,pady=5 ,command=lambda:total_cmd(num_cmd_value.get())).grid(row=1,column=3)
    
menu = tk.Menu(app)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Home", command=home_interface)
file_menu.add_command(label="Add Client", command=add_client_form)
file_menu.add_command(label="Add Command", command=add_command_form)
file_menu.add_command(label="command total ", command=command_total_form)

app.geometry("1000x500")
app.config(menu=menu)
app.mainloop()