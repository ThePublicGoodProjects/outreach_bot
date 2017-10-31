# PGP_Bot, a Public Health Chat-bot #

The PGP_bot reads file of tweets from excel, then tweet them if they are past their scheduled time but have not yet been tweeted.

**Currently in Beta. This is a work in progress!**

## Features ##

- Read file of tweets from Excel
- Log all activity
- Filter the dataframe to retain only rows with no completed timestamps
- Tweet the content of rows that meet the criteria
- Save resulting Excel

## Getting Started ##

### Pre-requisites ###

- A Linux System
- Python 2 / 3
- Pandas / Numpy

### Setup a Virtual Machine (VM) ###
We will use Amazon Web Services (AWS), but other options are available (Microsot Azure, Google Cloud Platform, etc). 
Here's a link to detailed [Amazon Linux AMI IDs][https://aws.amazon.com/amazon-linux-ami/] and here's a simple link to a tutorial on how to [setup an EC2 instance][https://www.infoworld.com/article/3220410/cloud-computing/linux-amazon-ec2-tutorial-how-to-set-up-an-ec2-instance.html]

E.g. for our chatbot, we will use the [**Deep Learning AMI Ubuntu Linux - 2.4_Oct2017 (ami-37bb714d)**][https://aws.amazon.com/marketplace/pp/B06VSPXKDX]. There's no extra charge and it comes with many things preinstalled.

Go through the following [instructions][https://aws.amazon.com/blogs/ai/the-aws-deep-learning-ami-now-with-ubuntu/] and download {your key}.pem to your computer to later access the VM through SSH. 

### Login to the VM ###

Navigate to the directory where **{your key.pem}** is located and change the permissions 

```
chmod 400 {your key}.pem
```

Now ssh into the VM

```
SSH –L localhost:8888:localhost:8888 –i <your key.pem> ubuntu@<Your instance DNS>
```

And follow [these instructions][https://blog.keras.io/running-jupyter-notebooks-on-gpu-on-aws-a-starter-guide.html] to configure **Jupyter Notebook.** Once that's done, start the server:

```
jupyter notebook.
```

And log into ```https://{your Amazon EC2 IP:8888}```. Don't mind the security warning, it's because our SSL certificate is not trusted (we created our own).

### Clone the PGP_BOT repository ###
Open a terminal. Go to the directory where you saved your PEM key and log through SSH to your VM. Copy & paste the following into the terminal window and **hit `Return`**. You may be prompted to enter your password.

```
ssh -i {name}.pem ec2-user@your-ip-address
```

Once you are logged, check if **`git`** is installed in your system, otherwise run for Debian-based Linux Systems:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
```

And for Red Hat-based Linux Systems:

```
sudo yum upgrade
sudo yum install git
```

Now with Git installed, clone the PGP_BOT Repository.

```
git clone https://github.com/ThePublicGoodProjects/pgp_bot.git
```

### Getting started ###

Move into the folder and explore the files
```
cd pgp_bot
ls
```

We have the following:

Key       | Type    | Description
:-------- | :------ | :---------------------------------------------------------------------------------------------------------
bot.py  | python  | Main file
bot_utils.py   | python  | Utility functions for configuration, logging
settings.py   | python | Global settings for script

Let's explore what options we can change within settings.py

```
pause_duration = 0.01 # seconds to pause between tweets

# location to save log files
logs_folder = './logs'

# write log to file and/or to console
log_file = True
log_console = True
log_level = lg.INFO
log_name = 'pgp_bot'
log_filename = 'pgp_bot'
```

### Running bot.py ###

Our algorithm feeds from an outputted excel file (.xlsx) and then uses a function to post a tweet with the screenname and content values. 

```
def post_tweet(row):
    """
    Create a tweet's content from a dataframe row, then post it.
    """
    try:
        # create a status from screenname and content values, then post it
        status = '@{screenname} {content}'.format(screenname=row['screenname'], content=row['content'])
        #api.PostUpdate(status=status)
        log('tweeted: "{}"'.format(status))
        time.sleep(pause_duration)

        # return the current datetime to save completion time to excel file
        return dt.datetime.now()
    except Exception as e:
        log('Error: {}'.format(e), level=lg.ERROR)
        return None
```

### Setup Cron ###

Here's a [link][https://www.centos.org/docs/5/html/5.2/Deployment_Guide/s2-autotasks-cron-configuring.html] to better understand how Cron works, or you can just follow these [steps][https://www.cumulations.com/blogs/37/How-to-write-Cron-jobs-on-Amazon-Web-ServicesAWS-EC2-server] to configure Cron Jobs Amazon Web Services(AWS) EC2 server.

Go to the PGP_BOT repository and get the absolute path for **`bot.py`**. We will use that later.

```
ls
cd pgp_bot
readlink -f bot.py
```

Now open **`crontab`**

```
sudo su
cd /etc
crontab -e
```

**Extract from: CentOS documentation:**
The main configuration file for cron, /etc/crontab, contains the following lines:

```
SHELL=/bin/bash 
PATH=/sbin:/bin:/usr/sbin:/usr/bin 
MAILTO=root HOME=/  
# run-parts 
01 * * * * root run-parts /etc/cron.hourly 
02 4 * * * root run-parts /etc/cron.daily 
22 4 * * 0 root run-parts /etc/cron.weekly 
42 4 1 * * root run-parts /etc/cron.monthly

```

The first four lines are variables used to configure the environment in which the cron tasks are run. The SHELL variable tells the system which shell environment to use (in this example the bash shell), while the PATH variable defines the path used to execute commands. The output of the cron tasks are emailed to the username defined with the MAILTO variable. If the MAILTO variable is defined as an empty string (MAILTO=""), email is not sent. The HOME variable can be used to set the home directory to use when executing commands or scripts.

Each line in the /etc/crontab file represents a task and has the following format:

```
minute   hour   day   month   dayofweek   command
```

- minute — any integer from 0 to 59
- hour — any integer from 0 to 23
- day — any integer from 1 to 31 (must be a valid day if a month is specified)
- month — any integer from 1 to 12 (or the short name of the month such as jan or feb)
- dayofweek — any integer from 0 to 7, where 0 or 7 represents Sunday (or the short name of the week such as sun or mon)
- command — the command to execute (the command can either be a command such as ls /proc >> /tmp/proc or the command to execute a custom script)

To automate the execution of **`bot.py`** to occur every day at 8:00 AM, we write:

```
0 8 * * * python {absolute path to bot.py, e.g. /home/ubuntu/notebooks/pgp_bot/bot.py} 
```

## Additional useful information ##

{to be completed..}

## Credits ##

Developed by the Public Good Project, inspired by the work of [Geoff Boeing](<https://github.com/gboeing>).