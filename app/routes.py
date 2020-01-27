from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, ChoiceForm
from app.models import Choice
from app import models


@app.route('/login', methods= ['get','post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



@app.route('/', methods=['GET', 'POST'])
def index():
    form = ChoiceForm()

    form.opts.query = Choice.query.filter(Choice.id > 1)

    if form.validate_on_submit():
        return '<html><h1>{}</h1></html>'.format(form.opts.data)

    return render_template('nowy.html', form=form)