from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/dvnc', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('prompt', '')
    
    responses = {
        'physics': f"Analyzing physics aspects of: {user_message}. Consider force distribution and structural integrity.",
        'biomechanics': f"From a biomechanics view: {user_message}. Think about natural movement patterns.",
        'anatomy': f"Anatomical perspective on: {user_message}. Apply human proportions and ergonomics.",
        'synthesis': f"Comprehensive analysis of: {user_message}. Combining all domains for optimal solution."
    }
    
    model = data.get('model', 'synthesis')
    
    return jsonify({
        'analysis': responses.get(model, responses['synthesis']),
        'confidence': 0.85 + random.random() * 0.15
    })

if __name__ == '__main__':
    app.run()
