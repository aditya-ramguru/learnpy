from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField(label='Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField(label='Closing Time e.g. 5:30PM', validators=[DataRequired()])
    Coffee_rating = SelectField(label='Coffee Rating', choices=[0, 1, 2, 3, 4, 5], validate_choice=True, coerce=int)
    Wifi_strength = SelectField(label='Wifi Strength Rating', choices=[0, 1, 2, 3, 4, 5], validate_choice=True,
                                coerce=int)
    power = SelectField(label='Power Socket Availability', choices=[0, 1, 2, 3, 4, 5], validate_choice=True, coerce=int)
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        info_row = [form.cafe.data, form.location.data, form.open.data, form.close.data, form.Coffee_rating.data,
                    form.Wifi_strength.data, form.power.data]
        with open('cafe-data.csv', mode='a', newline='') as csvfile:  # newline='' it doesnt put an additional \n
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(info_row)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:  # newline is set to '' so that \r\n  doesnt convert to \n
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
