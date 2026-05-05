# 🚀 Projet : Environnement de Développement ML/DL & SDN

Bienvenue dans l'environnement de travail de notre équipe. Ce projet fournit un environnement Infrastructure as Code (IaC) standardisé pour le développement Python orienté Machine Learning et la simulation réseau SDN via ContainerLab.

## 📋 Prérequis (Machine Hôte)
Avant de commencer, assurez-vous d'avoir installé les outils suivants sur votre ordinateur :

- **Vagrant** : [Télécharger ici](#)

### Un Hyperviseur :
- **VirtualBox (Gratuit)** : [Télécharger ici](#)
- **OU VMware (Workstation ou Fusion)** : Si vous utilisez VMware, installez le plugin utilitaire :

```bash
vagrant plugin install vagrant-vmware-desktop
```

- **Git** : Pour cloner le dépôt.

## 🛠️ Lancement Rapide (Déploiement Automatisé)
Grâce à Vagrant, la création de la VM Linux, l'installation de Docker et de ContainerLab sont automatisées.

Récupérer le projet :

```bash
git clone https://github.com/xavierarce/Conteneurisation.git
```

Lancer la Machine Virtuelle :

- Avec VirtualBox (par défaut) :

```bash
vagrant up
```

- Avec VMware :

```bash
vagrant up --provider=vmware_desktop
```

Accéder à l'environnement :
Une fois la VM démarrée, connectez-vous en SSH :

```bash
vagrant ssh
```

Note : Le dossier du projet sur votre PC est synchronisé avec le dossier /home/vagrant/projet dans la VM.

Initialiser les conteneurs (dans la VM) :

```bash
cd projet
sed -i 's/\r$//' setup.sh
sed -i 's/\r$//' deploy_sdn.sh
bash setup.sh
```

## 📦 Rôle des fichiers du projet
Voici un aperçu rapide de ce que fait chaque fichier principal du dépôt :

| Fichier | Rôle |
| --- | --- |
| `Dockerfile` | Construit l'image Docker de l'environnement ML et installe les dépendances Python. |
| `docker-compose.yml` | Définit le service Docker de développement et monte le projet dans le conteneur. |
| `setup.sh` | Lance l'environnement en construisant l'image puis en démarrant les conteneurs. |
| `deploy_sdn.sh` | Déploie la topologie SDN avec ContainerLab. |
| `provision.sh` | Installe Docker, ContainerLab et les outils de base dans la VM Vagrant. |
| `Vagrantfile` | Configure la VM Ubuntu, le partage de dossier et la provision. |
| `requirements.txt` | Liste les bibliothèques Python pour le ML, la qualité et la sécurité. |
| `sdn_topology.yml` | Décrit la topologie réseau utilisée pour la simulation SDN. |
| `main.py` | Point d’entrée principal du projet Python. |
| `linear_api.py` | Gère la logique liée au modèle ou à l’API linéaire. |
| `matrix_api.py` | Gère la logique liée au traitement matriciel ou à l’API matricielle. |
| `tree_api.py` | Gère la logique liée au traitement par arbre ou à l’API arborescente. |
| `test_ml.py` | Vérifie rapidement l’installation des bibliothèques ML et de NumPy. |
| `files_descriptions.txt` | Centralise des descriptions courtes pour chaque fichier du projet. |

## 💻 Flux de Travail (Où coder ?)
L'avantage de cette configuration est que vous profitez de la puissance de la VM tout en gardant votre confort de développement :

- **Édition** : Ouvrez le dossier devepment_equipes sur votre machine physique avec votre IDE préféré (VS Code, PyCharm). Les modifications sont instantanément répercutées dans la VM.

- **Exécution** : Les scripts doivent être lancés via Docker à l'intérieur de la VM Vagrant.

# Exemple pour lancer un script
```bash
docker exec python_ml_dev python3 main.py
```

Emplacements spécifiques :
- **Algorithmique** : Placez vos bibliothèques du TP "Algorithmique Avancée" dans /libs_algo.

- **Machine Learning** : Créez vos scripts à la racine du projet.

## 🧪 Vérification de la Conformité (Syllabus)
Pour prouver que l'environnement respecte les exigences pédagogiques :

1. **Bibliothèques ML/DL & Calcul**
Vérifiez la présence des frameworks (Scikit-learn, TensorFlow, PyTorch) :

```bash
docker exec python_ml_dev pip list | grep -E "scikit-learn|tensorflow|torch|numpy|pandas"
```

2. **Outils de Qualité & Sécurité**
Nous avons intégré une suite complète d'analyse statique :

- **Qualité (Linting)** : docker exec python_ml_dev pylint --version

- **Sécurité** : docker exec python_ml_dev bandit --version

- **Complexité** : docker exec python_ml_dev radon --version

3. **Simulation Réseau SDN**
La topologie réseau est gérée par ContainerLab. Pour déployer le réseau simulé (depuis la VM) :

```bash
sudo clab deploy -t sdn_topology.yml
```

## 🛑 Arrêt de l'environnement
Pour économiser les ressources de votre PC quand vous avez fini de travailler :

- **Mettre la VM en pause** : vagrant suspend

- **Éteindre la VM** : vagrant halt

- **Supprimer la VM (supprime l'instance mais garde votre code)** : vagrant destroy

## Pourquoi ce choix technique ? (Justification)
Vagrant : Assure que chaque membre de l'équipe et le correcteur disposent de la même version d'OS (Ubuntu 22.04) et des mêmes versions d'outils, éliminant les problèmes de compatibilité Windows/Mac/Linux.

Multi-Provider : Le projet est flexible et supporte aussi bien VMware (souvent utilisé en entreprise) que VirtualBox (standard académique).