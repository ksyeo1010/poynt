#!/bin/bash
cd /home/ec2-user/app/

# run mongo container
docker-compose up -d

# run python
source environment/bin/activate
noup python bot.py &
