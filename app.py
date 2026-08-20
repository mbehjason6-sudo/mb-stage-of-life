
from flask import Flask, render_template, request
 
app = Flask(__name__)
def  get_stage(age):
    try:
        age = int(age)
    except:
        return "unknown stage"
    if age<0:
        return "not yet born"
    elif age<=2:
        return "Baby - The Beginning"
    elif age<=12:
        return "childhood - Time to learn & play"
    elif age<=19:
        return "teenager - The discovery stage"
    elif age<=35:
        return "youth -The building stage"
    elif age<=55:
        return "Aduldhood - The responsilbility stage"
    else:
        return "Elder - The wisdom stage"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home", methods=['POST'])
def home():
    name = request.form.get("name", "Guest")
    age = request.form.get("age", "0")
    stage = get_stage(age)
    return render_template("home.html", name=name, age=age, stage=stage)


if __name__ == '__main__':
    app.run(debug=True)