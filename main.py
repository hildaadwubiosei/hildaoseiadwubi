from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import SubmitMessage
from flask_mail import Message, Mail
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv()

app = Flask(__name__)

email = os.getenv('EMAIL_')
password = os.getenv('MY_PASSWORD')


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = password



app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
mail = Mail(app)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = SubmitMessage()
    if form.validate_on_submit():
        msg = Message(
            subject=f"I'm {form.name.data}, sent from your website",
            sender=email,
            recipients=["hildaosei109@gmail.com"],
            reply_to=form.email.data,
            body=f"From: {form.name.data} ({form.email.data})\n\n{form.message.data}"           
        )
        mail.send(msg)
        flash("Message successfully sent!", "success")
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

@app.route('/blog')
def blogs():
    return render_template('blog.html')

@app.route('/archives')
def archives():
    return render_template('archives.html')



if __name__ == "__main__":
    app.run(debug=True)

