#!/bin/bash
# python
sudo pip3 install virtualenv
cd /home/ec2-user/poynt
virtualenv environment
source environment/bin/activate
sudo pip3 install -r requirements.txt