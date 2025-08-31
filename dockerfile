# Étape 1 : Choisir une image de base (Python 3.12 slim = légère et sécurisée)
FROM python:3.12-slim

# Étape 2 : Créer un dossier de travail dans le container
WORKDIR /app

# Étape 3 : Installer Flask
# (on crée un fichier temporaire requirements.txt avec juste Flask)
RUN pip install flask

# Étape 4 : Copier le fichier app.py dans le container
COPY app.py /app

# Étape 5 : Exposer le port 8080 (celui sur lequel Flask va écouter)
EXPOSE 8080

# Étape 6 : Commande de démarrage → lance Flask
CMD ["python", "app.py"]
