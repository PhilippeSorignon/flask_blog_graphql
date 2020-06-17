import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.debug = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
db = SQLAlchemy(app)
migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

class SecureView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

admin = Admin(app, index_view=SecureAdminIndexView())


from blog.post.views import post

app.register_blueprint(post)

from blog.auth.views import auth

app.register_blueprint(auth)

db.create_all()
