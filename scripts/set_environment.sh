#!/bin/bash
cd /home/ec2-user/poynt

rm .env -y

# add params
echo DISCORD_GUILD=$(aws ssm get-parameters --output text --region us-east-1 --names DISCORD_GUILD --with-decryption --query Parameters[0].Value) >> .env
