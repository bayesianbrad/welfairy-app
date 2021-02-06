from flask import Flask, url_for, session
from flask import render_template, redirect
from authlib.integrations.flask_client import OAuth
import os
import json

# create the application object

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.secret_key = app.config['SECRET_KEY']
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth = OAuth(app)
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)

#use decorators to link the function to a url 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route('/auth')
def auth():

    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    response = oauth.google.get('userinfo')
    user_info = response.json()
    session['user'] = user
    session['email'] = user_info['email']
    return redirect('/logout')

@app.route('/logout')
def logout():
    email = dict(session).get('email', None)
    # print(f'Thank you, {email}')
    session.pop('user', None)
    return f'Thank you, {email}'

# handle user login
# @app.route('/login',methods=['GET','POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin'  or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             # url_for() will take the successful login users to the home page
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)


# start the server with run() method. 

if __name__=='__main__':
    app.run(debug=True)

