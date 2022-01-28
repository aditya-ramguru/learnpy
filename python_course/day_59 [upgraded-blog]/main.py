from flask import Flask, render_template, request
import requests
import smtplib

MY_EMAIL = 'pythonsmtp58@gmail.com'
password = '8884230038'
app = Flask(__name__)
API_END ="https://api.npoint.io/157951f2d42b7034ec9f"
response = requests.get(url=API_END)
response.raise_for_status()
data = response.json()
print(data)


@app.route('/')
def home():
    return render_template('index.html', data=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET"])
def contact():
    return render_template('contact.html', is_filled=False)


@app.route('/post/<int:id_num>')
def get_post(id_num):
    return render_template('post.html', id_num=id_num, data=data, img_url=data[id_num-1]['img_add'])


@app.route("/contact", methods=["POST"])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone_no']
    message = request.form['message']
    email_message= f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=password)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=email_message)
    return render_template('contact.html', is_filled=True)


# can put the contents of receive data in contact and change the url_for receive data to url_for contact that way the code
# becomes more concise and clean can use if requests.method == post

if __name__== '__main__':
    app.run(debug=True)