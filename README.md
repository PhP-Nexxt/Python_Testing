# Repository - Projet 11 - Dev Application Python

Ce projet est réalisé dans le cadre de la formation OpenClassrooms Développeur d'Applications Python. Il s'agit d'ameliorer une application en effectuant du debogage, puis des tests. Ceci pour le compte de la societe fictive 'Guglft" en utilisant le framework `Flask`


Installation & lancement :
Installer Python en version 3.8.8 Lancez un terminal et placez vous dans le dossier de votre choix puis clonez le repository: git clone https://github.com/PhP-Nexxt/Python_Testing

Placez vous dans le dossier Python_Testing, puis créez un environnement virtuel:

python -m venv venv_gudlft

Ensuite, activez-le sur MacOs/Linux source venv_gudlft/bin/activate - ou sur Windows venv_gudlft\scripts\activate.b
Installez ensuite les packages requis: pip install -r requierement.txt

Definissez l'environnement  flask: export FLASK_APP=server.py 
Lancer le serveur flask: python3 -m flask run

Utiliser l'application avec l'url suivante : http://127.0.0.1:5000/