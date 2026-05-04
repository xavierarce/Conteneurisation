#!/bin/bash
export DEBIAN_FRONTEND=noninteractive

echo "--- Mise à jour du système ---"
sudo apt-get update && sudo apt-get upgrade -y

echo "--- Installation de Docker ---"
sudo apt-get install -y ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Permettre à l'utilisateur vagrant d'utiliser docker sans sudo
sudo usermod -aG docker vagrant

echo "--- Installation de ContainerLab ---"
bash -c "$(curl -sL https://get.containerlab.dev)"

echo "--- Installation de Python et outils de base ---"
sudo apt-get install -y python3-pip git

echo "--- VM Prête ! ---"