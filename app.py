import os
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# API Key aur Model Name
genai.configure(api_key="AIzaSyAy5JUBzOVGMlqT2Bvm8sKqJoBrTTPgpU4")

@app.route('/')
def home():
    return "Fard AI Backend is Live!"

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        file_base64 = data.get('file')
        mime_type = data.get('mimeType')

        # Sabse stable model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = "Extract Punjab Fard data and translate to English HTML table. Include Khewat, Khatoni, Khasra, Area, Owner."
        
        file_data = base64.b64decode(file_base64)
        response = model.generate_content([prompt, {'mime_type': mime_type, 'data': file_data}])
        
        return jsonify({"translated": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)