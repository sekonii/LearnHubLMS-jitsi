from flask import Flask
import os

app = Flask(__name__)

# Your routes go here
@app.route('/')
def home():
    return 'Hello, Railway! Your Flask app is live.'

# This is the important part
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Railway will provide the PORT env variable
    app.run(host='0.0.0.0', port=port)
