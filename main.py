from flask import Flask, render_template, request
from tips_generator import generate_tip
from feedback_generator import analyze_confession
from voicetip import speak_tip

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    city = request.form['city']
    issue = request.form['climate_issue']
    transport = request.form['transport']
    electricity = request.form['electricity']
    language = request.form['language']

    tip = generate_tip(city, issue, transport, electricity, language)
    speak_tip(tip)
    return render_template('tip.html', tip=tip)

@app.route('/confessor')
def confessor():
    return render_template('carbon_confessor.html')

@app.route('/confess', methods=['POST'])
def confess():
    confession = request.form['confession']
    feedback = analyze_confession(confession)
    speak_tip(feedback)
    return render_template('carbon_confessor.html', confession=confession, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
