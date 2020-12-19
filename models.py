import json
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class Garden:
    def __init__(self):        
        try:
            with open("garden.json", "r") as f:
                self.garden = json.load(f)
        except FileNotFoundError:
            self.garden = []

    def all(self):
        return self.garden

    def get(self, id):
        return self.garden[id]

    def create(self, data):
        data.pop('csrf_token')
        self.garden.append(data)

    def save_all(self):
        with open("garden.json", "w") as f:
            json.dump(self.garden, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.garden[id] = data
        self.save_all()

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


garden = garden()