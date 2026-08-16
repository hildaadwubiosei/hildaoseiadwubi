from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import SubmitMessage
import os
from dotenv import load_dotenv
import resend

load_dotenv()

app = Flask(__name__)

email = os.getenv('EMAIL_')
resend.api_key = os.getenv("RESEND_API_KEY")


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
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
        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": [email],
            "reply_to": form.email.data,
            "subject": f"New message from {form.name.data}",
            "text": f"From: {form.name.data} ({form.email.data})\n\n{form.message.data}"
        })
        print("Sending to:", email)
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

