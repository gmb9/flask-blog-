from flask import Flask

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'123c_5#y2L"F4Q8z\n\xec]/'
from app import routes

app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['ADMIN_PASSWORD'] = '1234'
app.run(debug = True, host = '0.0.0.0')