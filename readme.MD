# ✅ Prerequisites
* Python 3.8+

* PostgreSQL (or your preferred SQL DB)

# 🧪 Setting Up

## 1. Clone the repo
```
git clone https://github.com/lijoy26/fabric-health-workflows.git 

cd fabric-health-workflows/
```

## 2. Create a virtual environment
```
python -m venv venv
```

## 3. Activate the virtual environment

#### On Windows:
```
venv\Scripts\activate
```

#### On macOS/Linux:
```
source venv/bin/activate
```

## 4. Install dependencies
```
pip install -r requirements.txt
```

# 🔐 Environment Configuration
update .env file in the app folder

```
# .env
DB_HOST=database_host
DB_PORT=database_port
DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=database_password
```

# 🧬 Database Migrations

Run Migrations 
```
python db_migrate.py db upgrade
```

# Running the App
```
export FLASK_APP=run.py

flask run
```


# Creating Migrations

1. Modify Models / Add a New Table

    For example, add a new model class like User in app/import_job/model/.

    Make sure the model is imported somewhere before migrations, e.g., in app/__init__.py.


2. Create a New Migration

    After model changes:
    ```
    python db_migrate.py db migrate -m "Add users table"
    ```

3. Apply the New Migration to the Database

    ```
    python db_migrate.py db upgrade
    ```


### Deactivate (Optional):
```
deactivate
```