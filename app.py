import flask
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import json

with open("userinfo.json") as f:
    userdata = json.load(f)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


class RegisterForm(FlaskForm):
    login = StringField('Имя пользователя')
    email = StringField('Адрес электронной почты')
    password = StringField('Пароль')
    submit = SubmitField('Зарегистрироваться')


@app.route('/register/', methods=['GET', 'POST'])
def render():
    form = RegisterForm()
    if flask.request.method == 'GET':
        return render_template("index.html", form=form)
    userdata.append({'login': form.login.data, 'email': form.email.data, 'pass': form.password.data})
    with open("userinfo.json", "w") as f:
        json.dump(userdata, f, indent=4)
    return 'Добро пожаловать в систему. Ваш логин: {}, Адрес электронной почты: {}, Пароль: {}'.format(form.login.data,
                                                                                                       form.email.data,
                                                                                                       form.password.data)


if __name__ == '__main__':
    app.run()
