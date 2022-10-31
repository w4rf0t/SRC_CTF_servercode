# ![image](https://user-images.githubusercontent.com/61643034/198817144-e2ae6933-470b-4f56-ad03-0613431b4676.png)


## Install

1. Install dependencies: `pip3 install -r requirements.txt`
   
   - You can also use the `sudo ./prepare.sh` script to install system dependencies using apt.
   
2. Use `python3 serve.py` or `flask run` in a terminal to drop into debug mode.

## Configure verify email: 
- To enable verify email, choose ***Enable*** in ***Admin Config*** Page

- And then in `/CTFd/utils/email/smtp.py`, change the ***gmail_user*** ,***sent_from*** and ***gmail_password***   (gmail app password)
![image](https://user-images.githubusercontent.com/61643034/198817396-ed3c0b4e-db40-49e2-a010-0a3d821ba382.png)


## Default Account
- username:  `admin`
- password: `admin`

## Other informations:

- I have added some challenges in this project.
- This platform was copyright by [CTFd.io](https://ctfd.io), modifed by [@w4rf0t](https://github.com/w4rf0t) and used neon theme.
