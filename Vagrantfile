$script = <<-SCRIPT
  echo "Lancement de l'installation des paquets apt"
  sudo apt-get update
  sudo apt-get install git
  sudo apt-get install python3-pip
  sudo apt-get install postgresql-9.5

  echo "Lancement de l'installation des paquets python3"
  pip3 install django
  pip3 install djangorestframework
  pip3 install psycopg2
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.define "DJANGO" do |web|
    web.vm.box = "ubuntu/xenial64"

    web.vm.network "private_network", ip: "192.168.100.12"
    web.vm.network "forwarded_port", guest: 8000, host: 8000

    web.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.name = "DJANGO"
      vb.memory = 1024
      vb.cpus = 1
    end

    web.vm.provision "shell", inline: $script
  end
end
