from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# python3 run.py db init
# python3 run.py db migrate
# python3 run.py db update --> ambos tem que ser rodados pra atulizar db

from app.controllers import default 
