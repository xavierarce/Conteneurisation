🚀 Projet : Environnement de Développement ML/DL & SDN
Bienvenue dans l'environnement de travail de notre équipe. Ce projet fournit un environnement standardisé pour le développement Python orienté Machine Learning et la simulation réseau SDN.  

📋 Prérequis
Docker Desktop (lancé et fonctionnel).

Git (pour le partage du code).  

🛠️ Lancement rapide
Récupérer le projet :

Bash
git clone https://github.com/xavierarce/Conteneurisation.git
cd devepment_equipes
Lancer l'environnement :

Bash
bash setup.sh
Le conteneur python_ml_dev tourne maintenant en arrière-plan.

  

💻 Flux de Travail (Où coder ?)
Vous codez sur votre machine locale, pas "dans" le Docker.

Édition : Ouvrez le dossier devepment_equipes avec VS Code ou PyCharm.

Emplacements spécifiques :

Algorithmique : Placez vos fichiers de fonctions du TP "Algorithmique Avancée" dans le dossier /libs_algo.  

Machine Learning : Créez vos scripts à la racine du projet.

Exécution : Pour lancer un script (ex: main.py), utilisez la commande :

Bash
docker exec python_ml_dev python3 main.py
🧪 Vérification de la Conformité (Syllabus)
Pour prouver que l'environnement respecte les exigences de Thierry Thaureaux :  

1. Bibliothèques ML/DL
Vérifiez la présence de Scikit-learn, TensorFlow, PyTorch et Orange3 :

Bash
docker exec python_ml_dev pip list | grep -E "scikit-learn|tensorflow|torch|Orange3"
2. Outils de Qualité & Sécurité
Nous avons choisi une suite d'outils légers et complets (Analyse statique, sécurité, complexité) :

Qualité : docker exec python_ml_dev pylint --version

  

Sécurité : docker exec python_ml_dev bandit --version

  

Complexité : docker exec python_ml_dev radon --version

  

3. Simulation SDN
La topologie réseau est définie dans topology.yml pour être utilisée avec ContainerLab.