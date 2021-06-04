#!/bin/bash
cd /home/ec2-user/poynt

# run mongo container
docker-compose up -d

# run python
source environment/bin/activate
pkill -f bot.py
nohup python -u ./bot.py > output.log 2> error.log &
