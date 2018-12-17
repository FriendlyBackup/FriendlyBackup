from flask_login import LoginManager

app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'
