#!/bin/bash
# python
cd /home/ec2-user/poynt
virtualenv environment
source environment/bin/activate
sudo pip3 install -r requirements.txt

# mongodb
docker-compose build