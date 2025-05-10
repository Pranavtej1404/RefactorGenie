from flask import Flask, request, jsonify,render_template
from main import analyze
import os
app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_api():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    uploaded_file = request.files['file']
    code = uploaded_file.read().decode('utf-8')

    suggestions = analyze(code)
    return jsonify({'suggestions': suggestions})

@app.route('/analyze_pasted', methods=['POST'])
def analyze_paste():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({'error': 'No code provided'}), 400

    code = data['code']
    suggestions = analyze(code)
    return jsonify({'suggestions': suggestions})

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)
    
