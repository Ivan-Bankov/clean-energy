# Clean Energy
## What it does:
Clean Energy is a responsive web application built with Flask. It's supposed to represent an energy company's website which has a fully functional form for submitting emails.
## Technologies used:
The app was built with Flask. MIMEText, smtplib, dotenv, and waitress were used as well. MIMEText is used for the message part of the email which is then sent using the smtplib module. Waitress is used to host the app. Last but not least, Mailtrap is used as the platform for receiving emails.
## Why said technologies:
I wanted to try and build a website/application with Python as the backend. Flask is know as the go-to (micro)framework for building quick apps and smtplib and waitress were used for their simplicity. Mailtrap is the best choice for the email-receiving platform because it provides the necessary syntax depending on the technologies you're using, it's free, and it actually works as intended.
## How to install it:
First you need to download/clone the project. After that you need to create an environment for it and activate it. If you don't know how to do that, you can follow this tutorial by teclado: https://youtu.be/KxvKCSwlUv8. Next, you have to install all of the requirements for the project in the *requirements.txt* file by executing the following command in the terminal: *pip install -r requirements.txt*. The last step is to run the *app.py* file.
## How to use it:
First and foremost you need to create a *.env* file in the main directory of the project. You'll need to get 
