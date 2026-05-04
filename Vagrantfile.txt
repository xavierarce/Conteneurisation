# Vagrantfile
Vagrant.configure("2") do |config|
  # On choisit Ubuntu 22.04 LTS pour sa stabilité avec Docker/ML
  config.vm.box = "ubuntu/jammy64"

  # Configuration des ressources (ajustable selon les besoins ML)
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096" # 4 Go recommandés pour ML/Docker
    vb.cpus = 2
    vb.name = "Projet_ML_SDN_VM"
  end

  # Adresse IP fixe pour accéder à la VM
  config.vm.network "private_network", ip: "192.168.56.10"

  # On synchronise le dossier du projet avec la VM
  config.vm.synced_folder ".", "/home/vagrant/projet"

  # Script de provisionnement (installation automatique)
  config.vm.provision "shell", path: "provision.sh"
end