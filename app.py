from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

# Simple CORS handling without flask-cors
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/')
def home():
    return jsonify({
        "status": "DVNC Backend Running",
        "message": "API endpoint available at /api/dvnc"
    })

@app.route('/api/dvnc', methods=['GET', 'POST', 'OPTIONS'])
def chat():
    # Handle OPTIONS
    if request.method == 'OPTIONS':
        return '', 204
    
    # Handle GET
    if request.method == 'GET':
        return jsonify({"message": "Use POST to send messages"})
    
    # Handle POST
    if request.method == 'POST':
        data = request.get_json() if request.is_json else {}
        user_message = data.get('prompt', 'Hello')
        model = data.get('model', 'synthesis')
        
        return jsonify({
            'analysis': f"Leonardo's {model} analysis: {user_message}",
            'confidence': 0.92
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
