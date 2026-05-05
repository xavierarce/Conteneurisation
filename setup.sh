#!/bin/bash

echo "--- Démarrage du déploiement de l'environnement ---"

# 1. Vérification de Docker
if ! command -v docker &> /dev/null
then
    echo "Docker n'est pas installé. Veuillez l'installer avant de continuer."
    exit
fi

# 2. Construction de l'image Docker[cite: 1]
echo "Construction de l'image Docker en cours..."
docker compose build

# 3. Lancement de l'environnement
echo "Lancement du conteneur..."
docker compose up -d

echo "L'environnement est prêt ! Utilisez 'docker exec -it python_ml_dev bash' pour entrer."