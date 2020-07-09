'''
Simple Flask application deployed to Amazon Web Services
Uses Elastic Beanstalk

Author: Daniella Patton - mileadtraining@gmail.com

'''

from flask import Flask, redirect, url_for, render_template, request, session

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.secret_key = "super secret key"


# Route for handling the login page
@application.route('/', methods=['GET', 'POST'])
def login():
    error = None
    session['my_var'] = 'No'
    if request.method == 'POST':
        if request.form['username'] != 'miLead2020' or request.form['password'] != 'miLead2020':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['my_var'] = 'Yes'
            return redirect('/home')
    return render_template('index.html', error=error)

@application.route("/home")
def home():
    my_var = session.get('my_var', None)
    if my_var == 'Yes':
        return render_template('home.html')
    else:
        return redirect('/')

@application.route("/slide_design")
def sd():
    my_var = session.get('my_var', None)
    if my_var == 'Yes':
        return render_template("slide_design.html")
    else:
        return redirect('/')

@application.route("/primary_research")
def pr():
    my_var = session.get('my_var', None)
    if my_var == 'Yes':
        return render_template("primary_research.html")
    else:
        return redirect('/')

@application.route("/secondary_research")
def sec():
    my_var = session.get('my_var', None)
    if my_var == 'Yes':
        return render_template("secondary_research.html")
    else:
        return redirect('/')

@application.route("/competitive_landscape")
def cl():
    my_var = session.get('my_var', None)
    if my_var == 'Yes':
        return render_template("competitive_landscape.html")
    else:
        return redirect('/')

@application.route("/market_analysis")
def market_r():
    my_var = session.get('my_var', None)
    if my_var == 'Yes':
        return render_template("market_analysis.html")
    else:
        return redirect('/')


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()




