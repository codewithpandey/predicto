import re
from flask import Flask, request, jsonify
import brain.model as model

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
    return "Welcome to Predicto!"


@app.route('/getRating')
def getRating():
    review = str(request.args.get('review'));
    brain = model.Model()
    
    # brain.train()
    # Absolutely love this watch! Get compliments almost every time I wear it. Dainty.
    
    rating = brain.predict([review])

    response = {
        "review": review,
        "rating": str(rating[0])
    }

    return jsonify(response)

@app.route('/train')
def train():
    brain = model.Model()
    brain.train()
    return "Training has been initiated."
    # I'll add templates and html pages in the next commit :P

@app.route('/predicto')
def about():
    return "Predicto is an AI based star rating predictor"
    # I'll add templates and html pages in the next commit :P

@app.route('/download')
def download():
    return "This route shall be used for providing downloads and installation instructions."
    # I'll add templates and html pages in the next commit :P

if __name__ == "__main__":
    app.run(debug=True)