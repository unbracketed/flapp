"""Main application code"""
#from flask import redirect, url_for, request, render_template, session
from flask import Flask, render_template, session, request
import secrets


app = Flask(__name__)
app.secret_key = secrets.SECRET_KEY


@app.route('/')
def index():
    """Display home page"""    
    return render_template('index.html', domain=session.get('domain', ''))


@app.route('/oauth/')
def oauth_request():
    """Redirects user to Google's Oauth page"""
    authorize_url = get_authorize_url(FEED_URL, request, session)
    return redirect(authorize_url)


@app.route('/login/')
def oauth_access():
    """Authorize our app to access user's Gmail data"""
    authorize_app(request, session)
    return redirect('/check/')
    

if __name__ == '__main__':
    app.run()
