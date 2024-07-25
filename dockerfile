# Utiliser une image de base Python
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'application dans le répertoire de travail
COPY . /app

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir dash plotly gunicorn

# Rendre le script exécutable
RUN chmod +x start.sh

# Exposer le port sur lequel l'application s'exécute
EXPOSE 8050

# Commande pour lancer l'application
CMD ["./start.sh"]