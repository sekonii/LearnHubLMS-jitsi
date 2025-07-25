from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'App is running on Railway!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Fallback to 5000 locally
    app.run(debug=False, host='0.0.0.0', port=port)
