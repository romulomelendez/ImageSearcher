from flask import Flask, request, render_template
from webscrapping import getImage

app = Flask(__name__)

#routes
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home():
    value = request.form['stuff']
    getImage(value)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)