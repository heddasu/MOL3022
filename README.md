# MOL3022
In the command lines provided below, the `$` sign is included to show that these are command lines. Do not include the `$` sign when writing the lines in terminal.

## Prerequisites
To run the project ```git```, ```Python3```, ```pip``` and ```npm``` need to be installed. 
If using Windows a terminal needs to be downloaded, e.g., PowerShell.

## Clone project 
Given that you already have  ```git``` installed, you can follow this guide. 

In terminal, navigate into the folder your prefer to have this project. Then run the command:

```$ git clone https://github.com/heddasu/MOL3022.git```

## Run backend
Go into the folder with the command

```$ cd MOL3022```

To run the application, it is suggested that you make an virtual Python environment. 
Given that you already have  ```Python3``` and  ```pip``` installed, you can follow this guide.

#### Open terminal, and run the following command:

```$ pip install virtualenv```

#### Inside the project folder (MOL3022)
Run the following commands:

  ```$ virtualenv venv```

  ```$ source venv/bin/activate```

If this is done correctly, `(venv)` should appear in paranthesis in front of the `$` sign. You are now in the virtual environment.

#### Install dependencies

  ```(venv)$ pip install -r requirements.txt```

#### Run application
The application is built upon Django RF.

  ```(venv)$ python manage.py makemigrations```

  ```(venv)$ python manage.py migrate```

  ```(venv)$ python manage.py runserver```

### Quit backend 

ctrl + c 

## Run frontend
Given that you already have ```npm``` installed, you can follow this guide.

### Access the frontend folder 
In another terminal go into the folder with the command

```$ cd MOL3022```
 
and go into the frontend folder

```$ cd frontend```

### Project setup

```$ npm install```

### Install charts.js

```$ npm install --save axios chart.js```

### Compiles and run project

```$ npm run serve```

### Quit backend 

ctrl + c 

## Access web page
When backend and frontend is running, go to browser and visit:

http://localhost:8080/
