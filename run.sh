#!/bin/bash
source /home/ec2-user/miniconda/bin/activate TWITTER
cd /home/ec2-user/outreach_bot
python bot.py
source /home/ec2-user/miniconda/bin/deactivate
