from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('patientPortal.html')

@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html')

@app.route('/recommended_exercises')
def recommended_exercises():
    return render_template('recommended.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

if __name__ == '__main__':
    app.run(debug=True)

