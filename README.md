# Clean Energy
## What it does:
Clean Energy is a responsive web application built with Flask. It's supposed to represent an energy company's website, which has a fully functional form for submitting emails.
## Technologies used:
The app was built with Flask. MIMEText, smtplib, dotenv, and waitress were used as well. MIMEText is used for the message part of the email, which is then sent using the smtplib module. Waitress is used to host the app. Last but not least, Mailtrap is used as the platform for receiving emails.
## Why said technologies:
I wanted to try and build a website/application with Python as the backend. Flask is known as the go-to microframework for building quick but decent apps, and smtplib and waitress were used for their simplicity. Mailtrap is the best choice for the email-receiving platform because it provides the necessary syntax depending on the technologies you're using, it's free, and it actually works as intended.
## How to install it:
First, you need to download/clone the project. After that, you need to create an environment for it and activate it. If you don't know how to do that, you can follow this tutorial by *teclado*: https://youtu.be/KxvKCSwlUv8. Next, you have to install all of the requirements for the project in the *requirements.txt* file by executing the following command in the terminal: *pip install -r requirements.txt*. The last step is to run the *app.py* file.
## How to use it:
First and foremost, you need to create a *.env* file in the main directory of the project. You also need to make a Mailtrap account, navigate to *Email Testing -> Inboxes* and then open the available inbox. For the purpose of the app, it's recommended to rename it to *support@clean.energy* as that is the receiving inbox in the code. If you want the email to be sent to a different inbox, you have to change the *receiver* variable in the *app.py* file. Otherwise, you need to navigate to the *SMTP Settings* section of your inbox and switch the *cURL* integration to *smtplib*. After that, you expand the drop down *Show Credentials* and in the *.env* file, you put in the following environment variables:<br>
<br>
MAIL_HOST="*place the Mailtrap host as a string*"<br>
MAIL_PORT=*place the Mailtrap port as an int*<br>
UNAME="*place your Mailtrap username as a string*"<br>
PASS="*place your Mailtrap password as a string*"<br>
<br>
After you've done this, you can restart the *app.py* file if it's running and then navigate to *localhost:8080* in your browser. The app works as a regular website, so navigation should be as you expect. To try out the main feature of the project, all you have to do is scroll down to the bottom of the main page and type your *name*, *email* and *message*. After that, you click *Send Message* and it'll appear in your inbox after a few seconds. The form on the *Contacts* page works exactly the same.
## Credits:
Python Simplified: https://youtu.be/6plVs_ytIH8<br>
Xiaohua Cai: https://youtu.be/OKJ_Se5NL_Q<br>
NeuralNine: https://youtu.be/8dlQ_nDE7dQ
