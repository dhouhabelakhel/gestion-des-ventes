# 📊 Système de Gestion des Ventes

## 🎯 Description

Application de gestion des ventes développée en Python avec Tkinter, permettant de gérer efficacement les clients, les commandes et le stock d'articles. Cette solution complète offre une interface graphique intuitive pour les opérations commerciales quotidiennes.

## ✨ Fonctionnalités

### 👥 Gestion des Clients
- **Ajout** de nouveaux clients avec validation des données
- **Modification** des informations client existantes
- **Suppression** de clients avec confirmation
- **Visualisation** détaillée des informations client et historique des commandes
- **Tableau** interactif avec tri et recherche

### 📦 Gestion des Commandes
- **Création** de commandes avec sélection d'articles
- **Calcul automatique** des totaux
- **Vérification** de stock en temps réel
- **Calendrier intégré** pour la sélection des dates
- **Historique** complet des commandes par client

### 🏪 Gestion du Stock
- **Suivi** des quantités en stock
- **Mise à jour automatique** lors des commandes
- **Catalogue** d'articles prédéfini
- **Contrôle** des stocks insuffisants

## 🛠️ Technologies Utilisées

- **Python 3.9+**
- **Tkinter** - Interface graphique
- **tkcalendar** - Sélecteur de dates
- **PyInstaller** - Compilation en exécutable
- **Inno Setup** - Créateur d'installateur Windows

## 📋 Prérequis

- Python 3.9 ou supérieur
- Modules Python requis :
  ```
  tkinter (inclus dans Python)
  tkcalendar
  ```

## 🚀 Installation

### Option 1 : Utilisation du code source

1. **Clonez le dépôt**
   ```bash
   git clone https://github.com/votre-username/gestion-des-ventes-en-lignes.git
   cd gestion-des-ventes-en-lignes
   ```

2. **Installez les dépendances**
   ```bash
   pip install tkcalendar
   ```

3. **Lancez l'application**
   ```bash
   python gestion_vente_module.py
   ```

### Option 2 : Exécutable Windows

1. **Téléchargez l'installateur**
   - Rendez-vous dans le dossier `dist/Output/`
   - Exécutez `mysetup.exe`

2. **Installation automatique**
   - Suivez les instructions de l'installateur
   - L'application sera disponible dans le menu Démarrer

### Option 3 : Exécutable portable

1. **Téléchargez l'exécutable**
   - Récupérez `gestion_vente.exe` dans le dossier `dist/`
   - Aucune installation requise, double-cliquez pour lancer

## 📁 Structure du Projet

```
gestion-des-ventes-en-lignes/
├── gestion_vente_module.py      # Code source principal
├── build/                       # Fichiers de compilation PyInstaller
│   └── gestion_vente/
│       ├── Analysis-00.toc
│       ├── base_library.zip
│       ├── gestion_vente.pkg
│       └── localpycs/
├── dist/                        # Exécutables générés
│   ├── gestion_vente.exe       # Exécutable portable
│   ├── steup.iss               # Script Inno Setup
│   └── Output/
│       └── mysetup.exe         # Installateur Windows
├── __pycache__/                # Cache Python
└── README.md                   # Documentation
```

## 🖥️ Interface Utilisateur

### Écran Principal
- **Tableau** des clients avec informations complètes
- **Boutons d'action** : Ajouter, Modifier, Supprimer, Voir détails
- **Menu** de navigation intuitif

### Formulaires
- **Formulaire client** : Saisie et modification des informations
- **Formulaire commande** : Sélection d'articles avec calendrier
- **Validation** en temps réel des données

### Fonctionnalités Avancées
- **Calcul automatique** des totaux de commandes
- **Vérification** des stocks avant validation
- **Historique** détaillé par client
- **Messages** de confirmation et d'erreur

## 💡 Utilisation

1. **Démarrer l'application**
   - Lancez l'exécutable ou le script Python
   - L'interface principale s'affiche avec la liste des clients

2. **Gestion des clients**
   - Cliquez sur "Ajouter" pour créer un nouveau client
   - Sélectionnez un client et cliquez sur "Modifier" pour éditer
   - Utilisez "Voir détails" pour consulter l'historique

3. **Créer une commande**
   - Ajoutez d'abord un client
   - Sélectionnez des articles dans la liste déroulante
   - Spécifiez les quantités
   - Validez la commande

4. **Suivi des stocks**
   - Les quantités sont automatiquement mises à jour
   - Le système vous alerte si le stock est insuffisant

## 🐛 Dépannage

### Problèmes courants

**L'application ne se lance pas**
- Vérifiez que Python 3.9+ est installé
- Installez les dépendances : `pip install tkcalendar`

**Erreur de stock insuffisant**
- Vérifiez les quantités disponibles
- Réduisez la quantité commandée

**Interface qui se fige**
- Redémarrez l'application
- Vérifiez les données saisies

## 🔧 Développement

### Compilation en exécutable

```bash
# Installer PyInstaller
pip install pyinstaller

# Générer l'exécutable
pyinstaller --onefile --windowed gestion_vente_module.py
```

### Créer l'installateur

1. Installez Inno Setup
2. Ouvrez `steup.iss`
3. Compilez le script pour générer l'installateur

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos modifications
4. Poussez vers la branche
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📞 Support

Pour toute question ou problème :
- Ouvrez une issue sur GitHub
- Contactez l'équipe de développement
- Consultez la documentation

## 🔄 Versions

- **v1.0.0** - Version initiale complète
  - Gestion des clients (ajout, modification, suppression)
  - Gestion des commandes avec calendrier intégré
  - Gestion du stock en temps réel
  - Interface graphique intuitive
  - Compilation en exécutable Windows
  - Installateur Windows inclus



---

*Développé avec ❤️ en Python & Tkinter*
