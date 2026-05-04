#!/bin/bash

# Arrêter le script si une erreur survient
set -e

echo "=========================================="
echo "  Déploiement du Réseau SDN (ContainerLab)"
echo "=========================================="

# 1. Vérification que l'image ML existe bien sur la machine
if [[ "$(docker images -q projet-ml-env:latest 2> /dev/null)" == "" ]]; then
  echo "Attention : L'image Docker 'projet-ml-env:latest' n'existe pas encore."
  echo "Veuillez d'abord lancer votre script 'setup.sh' pour la construire !"
  exit 1
fi

# 2. Déploiement de la topologie avec sudo (ContainerLab nécessite les droits root pour le réseau)
echo "Lancement de ContainerLab..."
sudo clab deploy -t sdn_topology.yml

echo "=========================================="
echo "  Réseau déployé avec succès !            "
echo "=========================================="
echo ""
echo "Commandes utiles :"
echo "- Pour entrer dans le nœud A : docker exec -it clab-sdn_ml_cluster-data-node-a bash"
echo "- Pour détruire le réseau : sudo clab destroy -t sdn_topology.yml"