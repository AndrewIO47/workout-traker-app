from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main-page')
def main_page():
    return render_template('main-page.html')

@app.route('/start-workout')
def start_workout():
    return render_template('start-workout.html')

@app.route('/workout-log')
def workout_log():
    return render_template('workout-log.html')

if __name__ == "__main__":
    app.run(debug=True)