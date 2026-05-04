Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.synced_folder ".", "/home/vagrant/projet"
  config.vm.provision "shell", path: "provision.sh"

  # Configuration si l'étudiant utilise VirtualBox
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 2
    vb.name = "Projet_ML_VirtualBox"
  end

  # Configuration si l'étudiant utilise VMware
  config.vm.provider "vmware_desktop" do |v|
    v.vmx["memsize"] = "4096"
    v.vmx["numvcpus"] = "2"
    v.vmx["displayName"] = "Projet_ML_VMware"
  end
end