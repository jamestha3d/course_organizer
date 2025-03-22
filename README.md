## How to run

Clone repo and cd into project folder.

Make sure you are on the right Git branch. 

```git checkout branch_name```


## Let's run the project

```ls```

You should see:

```README.md       backend       frontend```

First we need to create a virtual environment and install the dependencies. 

```cd backend``` 

```python3 -m venv env``` ```

<!-- Create the virtual environment. -->```

Activating the virtual enviroment depends on your OS:

On Windows:

```env\Scripts\activate```

On macOS and Linux:

```source env/bin/activate``` 

```<!-- ^^^ We created a virtual environment called env and we are activating it. -->```

Next we have to install the dependencies.

```pip install -r requirements.txt```


This next step won't be needed when we connect to postgres.

Let's migrate create our local sqlite db and migrate our tables

```python manage.py makemigrations```

```python manage.py migrate```

Now we can run the server.

```python manage.py runserver```


## API DOCUMENTATION:

http://localhost:8000/api/documentation