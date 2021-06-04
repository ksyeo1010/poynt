#!/bin/bash
# codedeploy
yum -y update
yum install -y ruby
yum install -y aws-cli
cd /home/ec2-user
wget https://aws-codedeploy-us-east-2.s3.us-east-2.amazonaws.com/latest/install
chmod +x ./install
./install auto

# python dependencies
yum install python3 pip3
pip3 install virtualenv

# docker
amazon-linux-extras install docker
service docker start
usermod -a -G docker ec2-user

# docker compose
curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose