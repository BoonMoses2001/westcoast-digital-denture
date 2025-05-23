import os
from flask import Flask, render_template
# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/all-on-x')
def all_on_x():
    return render_template('all_on_x.html')
@app.route('/partial-dentures')
def partial_dentures():
    return render_template('partial_dentures.html')
@app.route('/full-dentures')
def full_dentures():
    return render_template('full_dentures.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
