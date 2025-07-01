from flask import Flask, render_template, request
from tips_generator import generate_tip
from feedback_generator import analyze_confession
from voicetip import speak_tip

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    city = request.form['city']
    issue = request.form['climate_issue']
    transport = request.form['transport']
    electricity = request.form['electricity']

    tip = generate_tip(city, issue, transport, electricity)
    speak_tip(tip)
    return render_template('tip.html', tip=tip)

@app.route('/confessor')
def confessor():
    return render_template('carbon_confessor.html')

@app.route('/process_confession', methods=['POST'])
def process_confession():
    confession = request.form['confession']
    feedback = analyze_confession(confession)
    speak_tip(feedback)
    return render_template('carbon_confessor.html', feedback=feedback, confession=confession)

if _name_ == '_main_':
    app.run(debug=True)