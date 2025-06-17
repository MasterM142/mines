from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mines.html')

@app.route('/mines')
def mines():
    return render_template('mines.html')

if __name__ == '__main__':
    app.run(debug=True)