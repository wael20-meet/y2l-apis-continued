from flask import Flask, render_template, request
app = Flask(__name__)
import requests, json

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    
    image_url = request.form['url-input']
    headers = {'Authorization': 'Key <7e1da2acfe784db0856fbef1822707cb>'}
    api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"


    data ={"inputs": [
      {
        "data": {
          "image": {
            "url": "image_url"
          }
        }
      }
    ]}

# putting everything together; sending the request!
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response.status_code

    
    return render_template('home.html', results="No results yet :(")

if __name__ == '__main__':
    app.run(debug=True)