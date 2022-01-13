from flask import Flask, render_template
import requests, json

app = Flask(__name__)

# Function to access the api url
def getAdvice():

    try:
        request = requests.get('https://api.adviceslip.com/advice')
        advice = json.loads(request.content)['slip']['advice']
        return advice
    except Exception as error:
        return f'{ error }'

# routes
@app.route('/', methods=['GET','POST'])
def advice():
    ad = getAdvice()
    return render_template('index.html', advice = ad)

if __name__ == '__main__':
    app.run(debug=True)