from flask import Flask, render_template, url_for, redirect, send_file, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from authlib.integrations.flask_client import OAuth
from datetime import timedelta
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
oauth = OAuth(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretkeyformyproject'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=25)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

google = oauth.register(
    name='google',
    client_id='767871294638-60larcsr76maomn6hp6va2pr4lfpbrvo.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo', 
    client_kwargs={'scope': 'openid email profile'},
)

@app.route('/twitter')
def twitter():
    oauth.register(
        name='twitter',
        client_id='xFBzFDpMKyifB9CjucMZR0m1E',
        client_secret='D57LRANv96ntzTpUux5dWrkvWLGO2teagcAYWBiVA13XKEUelO',
        request_token_url='https://api.twitter.com/oauth/request_token',
        request_token_params=None,
        access_token_url='https://api.twitter.com/oauth/access_token',
        access_token_params=None,
        authorize_url='https://api.twitter.com/oauth/authenticate',
        authorize_params=None,
        api_base_url='https://api.twitter.com/1.1/',
        client_kwargs=None,
    )
    redirect_uri = url_for('twitter_auth', _external=True)
    return oauth.twitter.authorize_redirect(redirect_uri)
 
@app.route('/twitter/auth/')
def twitter_auth():
    token = oauth.twitter.authorize_access_token()
    resp = oauth.twitter.get('account/verify_credentials.json')
    profile = resp.json()
    return redirect(url_for('oauth_dashboard'))


@app.route('/facebook')
def facebook():
    oauth.register(
        name='facebook',
        client_id='496722728465686',
        client_secret='7c04cfd23c0956ffd515b45e5f8e0019',
        access_token_url='https://graph.facebook.com/oauth/access_token',
        access_token_params=None,
        authorize_url='http://darkerr.co/users/auth/facebook',
        authorize_params=None,
        api_base_url='https://graph.facebook.com/',
        client_kwargs={'scope': 'email'},
    )
    redirect_uri = url_for('facebook_auth', _external=True)
    return oauth.facebook.authorize_redirect(redirect_uri)
 
@app.route('/facebook/auth/')
def facebook_auth():
    token = oauth.facebook.authorize_access_token()
    resp = oauth.facebook.get(
         'https://graph.facebook.com/me?fields=id,name,email,picture{url}')
    profile = resp.json()
    print("Facebook User ", profile)
    return redirect(url_for('oauth_dashboard'))


github_blueprint = make_github_blueprint(client_id='98aa2422c3eadaa1db65',
                                         client_secret='e798df9dc78411f7eb4ba1ec0fe3b93b8af7dfaf')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/github_login')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
       return redirect(url_for('oauth_dashboard'))

@app.route('/login_with_google')
def login_with_google():
    google  = oauth.create_client('google')
    redirect_uri = url_for('authorize_google', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize_google')
def authorize_google():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    response = google.get('userinfo')
    user_info = response.json()
    session['email'] = user_info['email']
    return redirect(url_for('oauth_dashboard'))

@login_manager.user_loader
def load_user(user_id):
    return User_Table.query.get(int(user_id))

class User_Table(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"Password"})

    submit = SubmitField("Register")

    def validate_username(self, username):
        exisitng_user_username = User_Table.query.filter_by(username=username.data).first()
        if exisitng_user_username:
            raise ValidationError("Username already exists!! Please choose different name.")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"Password"})

    submit = SubmitField("Login")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/oauth_dashboard', methods=['GET', 'POST'])
def oauth_dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')
@app.route('/download', methods=['GET', 'POST'])
def download():
    path = "book.pdf"
    return send_file(path, as_attachment=True)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User_Table.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User_Table(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    for key in list(session.keys()):
        session.pop(key)
    logout_user
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)