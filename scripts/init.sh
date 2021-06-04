#!/bin/bash
# codedeploy
yum -y update
yum install -y ruby
yum install -y aws-cli
cd /home/ec2-user
wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
chmod +x ./install
./install auto

# python 3.9 dependencies
yum install -y gcc
yum install -y openssl-devel
yum install -y bzip2-devel
yum install -y libffi-devel
cd /opt
wget https://www.python.org/ftp/python/3.9.4/Python-3.9.4.tgz
tar xzf Python-3.9.4.tgz
cd Python-3.9.4
./configure --enable-optimizations
make altinstall
rm -f /opt/Python-3.9.4.tgz
python3.9 -m pip3 install virtualenv

# docker
amazon-linux-extras install docker -y
service docker start
usermod -a -G docker ec2-user

# docker compose
curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose