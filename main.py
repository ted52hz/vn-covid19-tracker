from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

@app.route("/")
def home():
    data = requests.get("https://disease.sh/v2/countries/Vietnam",verify=False)
    data_dict = data.json()
    return render_template('home.html',data=data_dict)

@app.route('/send', methods=['POST'])
def send():
    if requests.method == 'POST':
        return render_template('home.html')
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)