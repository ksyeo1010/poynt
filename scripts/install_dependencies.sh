#!/bin/bash
cd /home/ec2-user/poynt

# cp env
#rm .env
sudo cp ~/.env .

# python
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# mongodb
docker-compose build