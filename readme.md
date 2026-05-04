🚀 Projet : Environnement de Développement ML/DL & SDN
Bienvenue dans l'environnement de travail de notre équipe. Ce projet a pour but de fournir un environnement standardisé pour le développement Python orienté Machine Learning, incluant nos outils de qualité de code et de simulation réseau.

📋 Prérequis
Avant de commencer, assurez-vous d'avoir installé sur votre poste :

Docker & Docker Compose

Git

Une distribution Linux (ou Docker Desktop sur Windows/Mac)

🛠️ Comment lancer l'environnement ?
Pour vous simplifier la vie, un script de déploiement automatique a été créé.

Récupérer le projet :

Bash
git clone https://github.com/xavierarce/Conteneurisation.git
cd devepment_equipes
Lancer le déploiement :

Bash
bash setup.sh
Ce script va construire l'image Docker et démarrer le conteneur en arrière-plan.


Entrer dans l'environnement de travail :

Bash
docker exec -it python_ml_dev bash
💻 Où écrire votre code ?
Le dossier actuel sur votre machine est synchronisé avec le dossier /app à l'intérieur du conteneur.

Vos scripts Python : Écrivez-les directement à la racine du projet sur votre PC (VS Code, PyCharm, etc.). Ils apparaîtront instantanément dans le conteneur.

Bibliothèques d'Algorithmique : Veuillez placer les fonctions créées lors du TP "Algorithmique Avancée" dans le dossier /libs_algo.

🧪 Comment tester si tout fonctionne ?
Une fois à l'intérieur du conteneur (via docker exec), lancez ces commandes pour vérifier la conformité au syllabus :

1. Vérifier les bibliothèques ML/DL
Bash
python3 -c "import sklearn, tensorflow, torch; print('✅ Bibliothèques ML/DL prêtes !')"
2. Vérifier les outils de qualité de code
Le syllabus impose des outils d'analyse statique et de sécurité. Testez-les ainsi :

Pylint (Qualité) : pylint --version

Bandit (Sécurité) : bandit --version

Flake8 (Style) : flake8 --version

3. Tester le réseau SDN (ContainerLab)
Pour la partie réseau, assurez-vous que les commandes clab sont accessibles pour déployer la topologie définie dans topology.yml.

📂 Structure du Projet
Dockerfile : Configuration de l'image (Python, outils).

docker-compose.yml : Orchestration du conteneur et des volumes.

requirements.txt : Liste des bibliothèques à installer.

setup.sh : Script de déploiement sur les postes.

topology.yml : Configuration du réseau SDN ContainerLab.

Note pour l'équipe : N'oubliez pas de faire un git pull régulièrement pour avoir les dernières configurations de l'environnement !