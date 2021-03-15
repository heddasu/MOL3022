# MOL3022
In the command lines provided below, the `$` sign is included to show that these are command lines. Do not include the `$` sign when writing the lines in terminal.

In terminal, navigate into the folder your prefer to have this project. Then run the command:

```$ git clone https://github.com/heddasu/MOL3022.git```

Go into the folder with the command

```$ cd MOL3022```

## Run backend
To run the application, it is suggested that you make an virtual Python environment. 
Given that you already have Python 3 and pip installed, you can follow this guide.

#### Open terminal, and run the following command:

```$ pip install virtualenv```


### TODO LEGG INN git clone og naviger inn i repo
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

## Run frontend
In another terminal, ......
