from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.debug = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kbwowatv:3E0F0eZPfoyD4WaQ3DQfKK_sW543ess4@dumbo.db.elephantsql.com:5432/kbwowatv'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

class SecureView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class SecureAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

admin = Admin(app, index_view=SecureAdminIndexView())


from blog.post.views import post

app.register_blueprint(post)

from blog.auth.views import auth

app.register_blueprint(auth)
