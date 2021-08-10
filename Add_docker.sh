sudo apt-get update
sudo apt-get install curl
curl -fsSL https://get.docker.com/ | sh
sudo usermod -aG docker user
sudo service docker restart
