#!/bin/bash
cd /home/ec2-user/poynt

# run mongo container
mkdir db
chmod -R 755 db
docker-compose up -d

# run python
source venv/bin/activate
pkill -f bot.py
nohup python -u bot.py > output.log 2> error.log &
