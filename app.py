from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS with specific configuration
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"]}})

@app.route('/')
def home():
    return jsonify({
        "status": "DVNC Backend Running",
        "message": "API endpoint available at /api/dvnc",
        "version": "1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# Fix: Add both GET and POST methods, handle OPTIONS
@app.route('/api/dvnc', methods=['GET', 'POST', 'OPTIONS'])
def chat():
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        response = jsonify({'status': 'ok'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        return response
    
    # Handle GET request (for testing)
    if request.method == 'GET':
        return jsonify({
            "message": "DVNC API is running. Use POST to send prompts.",
            "endpoint": "/api/dvnc",
            "method": "POST",
            "expected_payload": {"prompt": "your message", "model": "synthesis"}
        })
    
    # Handle POST request (actual chat)
    if request.method == 'POST':
        try:
            data = request.get_json() or {}
            user_message = data.get('prompt', 'Hello')
            model = data.get('model', 'synthesis')
            
            responses = {
                'synthesis': f"Analyzing through Leonardo's multidisciplinary lens: {user_message}. Combining physics, biomechanics, and anatomy principles for innovative solutions.",
                'physics': f"Physics analysis of {user_message}: Consider fluid dynamics, structural forces, and Leonardo's observations on water flow and mechanical principles.",
                'biomechanics': f"Biomechanical perspective on {user_message}: Applying joint articulation patterns and natural movement optimization from Leonardo's anatomical studies.",
                'anatomy': f"Anatomical approach to {user_message}: Implementing Vitruvian proportions and human-centered design principles."
            }
            
            response = jsonify({
                'analysis': responses.get(model, responses['synthesis']),
                'confidence': 0.85 + (len(user_message) % 15) / 100
            })
            
            # Add CORS headers to response
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
            
            return response
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method not allowed", "allowed": ["GET", "POST", "OPTIONS"]}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
