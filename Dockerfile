# Utilisation d'une base Python légère sous Debian (conforme au choix de distro)
FROM python:3.10-slim

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Création du dossier de travail
WORKDIR /app

# Copie et installation des bibliothèques Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Espace pour vos bibliothèques d'Algorithmique Avancée
# On crée un dossier dédié que vous remplirez plus tard
RUN mkdir -p /app/libs_algo

# Commande par défaut : on lance un bash pour rester interactif
CMD ["bash"]