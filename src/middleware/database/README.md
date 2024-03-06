# Database
This directory contains the package that handles webscraper database functions

Also contains some information on how to set a xamp server with password and make it available everywhere via TCP tuneling

## XAMPP

* Download XAMPP and START Apache & MySQL
* Open phpMyAdmin vy pressing Admin in MySQL row
* Create a new database giving a specific name
* In order to set password for database open cmd in Xampp UI and run: mysqladmin.exe -u root password <pass>
* After setting password press Config in Apache row and open "phpMyAdmin(config.inc.php)"
* Complete the password in section <$cfg['Servers'][$i]['password'] = '*NMp[R!Pha4Eiv8A';>

## NGROK
In order to port forward the local server make a user account in NGROK site and download the app. 
* execute ngrok app and run the following commands:
* ngrok config add-authtoken 2KgDC6QguXH5FvSow5olkAYNvAO_34mgBSwgSR1mVi1yWruf6 (token is given in ngrok site)
* ngrok tcp 3306

## SERVICE
* https://www.youtube.com/watch?v=ON2uRHlt_GI&ab_channel=Britec09




