Requirements

# Installation

Please make sure to not miss any step along the process.

1. Clone the project <br />
   ``` git clone https://github.com/ealili/django-project.git```


2. Change current directory to project's directory <br />
   ```cd django-project```


3. Copy *.example.env* to a *.env* file
    - For Windows <br />
      ``` copy .env.example .env```

    - For Linux or macOS <br />
      ``` cp .env.example .env```


4. Provide the OPENAI_KEY in the .env file
   ```OPENAI_KEY=youropenaikey```


5. Create a python virtual environment
    - For Windows <br />
      ```python3 -m venv venv``` <br />
      Activate the environment <br />
      ```venv\Scripts\activate.bat``` <br />
      Install the required packages <br />
      ```pip install -r requirements.txt``` <br/><br/>

    - For Linux or macOS <br />
      ```python3 -m venv venv``` <br />
      Activate the environment <br />
      ```source venv/bin/activate``` <br />
      Install the required packages <br />
      ```pip install -r requirements.txt``` 

#### Depending on your system, if you run into any issues while creating a virtual environment please refer to the official python docs on how you should create one [here](https://docs.python.org/3/library/venv.html).

6. Run migrations <br />
   ```python3 manage.py migrate```


7. Run the project <br />
   ```python3 -m manage.py runserver```

