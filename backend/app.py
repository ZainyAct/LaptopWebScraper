import os
from flask import Flask, render_template, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
from ScraperFunc import scraper
app = Flask(__name__)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})



@app.route('/api/laptops')
def get_laptops():
    laptops = scraper.get_laptop_data()
    
    return jsonify(laptops)  # Return data as JSON

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("frontend/build/" + path):
        return send_from_directory("frontend/build", path)
    else:
        return send_from_directory("frontend/build", "index.html")

if __name__ == '__main__':
    app.run(debug=True)

