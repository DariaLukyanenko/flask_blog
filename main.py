from flask import url_for
from flask import Flask, render_template,request
import requests
import datetime
import pandas as pd

def api():
    API_URL='https://api.npoint.io/c790b4d5cab58020d391'

    response = requests.get(API_URL)
    return response.json()

app = Flask(__name__)
current_time = datetime.datetime.now()

@app.route('/')
def home():
    data=api()
    month=current_time.strftime("%B")
    day=current_time.day
    year=current_time.year
    return render_template("index.html", data=data, month=month,day=day, year=year)

@app.route('/post/<int:num>')
def post_page(num=None):
    data=api()
    month=current_time.strftime("%B")
    day=current_time.day
    year=current_time.year
    return render_template("post.html", data=data, num=num, month=month,day=day, year=year)

@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/about')
def about():
    month=current_time.strftime("%B")
    day=current_time.day
    year=current_time.year
    return render_template("about.html", month=month,day=day, year=year)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    month = current_time.strftime("%B")
    day = current_time.day
    year = current_time.year
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        # Создание словаря с данными
        data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }
        
        # Создание DataFrame из словаря
        df = pd.DataFrame(data, index=[0])
        
        # Сохранение данных в CSV файл
        df.to_csv('data.csv', index=False)
        
        print(name)  
        success = True
        
    return render_template("contact.html", month=month, day=day, year=year, success=success)


if __name__ == "__main__":
    app.run(debug=True)
