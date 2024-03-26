# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:31:18 2024

@author: user
"""
import gestion_vente_module
from tkinter import *
import tkinter as tk
app = Tk()
menu = tk.Menu(app)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Menu", menu=file_menu)
file_menu.add_command(label="Home", command=gestion_vente_module.home_interface)
file_menu.add_command(label="Add Client", command=gestion_vente_module.add_client_form)
file_menu.add_command(label="Add Command", command=gestion_vente_module.add_command_form)
file_menu.add_command(label="command total ", command=gestion_vente_module.command_total_form)
file_menu.add_command(label="afficher client ", command=gestion_vente_module.client_command_form)


app.geometry("1000x500")
app.config(menu=menu)
app.mainloop()
