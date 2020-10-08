from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask import Flask,render_template, session, redirect,url_for, flash
app = Flask(__name__)

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'hard to guess string'

#bt khi xu ly form => request.form
class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# @app.route('/form', methods = ['GET','POST'])
# def form():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#     return render_template('form.html',form = form,name=name)

@app.route('/form', methods = ['GET',"POST"])
def form1():
    name = session.get('name')
    # name = session['name']
    form = NameForm()
    if form.validate_on_submit():
        if session.get('name')!=form.name.data:
            flash('Bạn vừa đổi tên thành công !!')
            session['name'] = form.name.data
        return redirect(url_for('form1'))
    return render_template('form.html',form = form,name=name)

@app.route('/')
def index():
    x = app.config['SECRET_KEY']
    return "hello form.py %s"%x

app.run(debug=True, port=3001)