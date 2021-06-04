#!/bin/bash
cd /home/ec2-user/poynt

# cp env
rm .env
sudo cp ~/.env .

# python
virtualenv environment
source environment/bin/activate
sudo pip3 install -r requirements.txt

# mongodb
docker-compose build