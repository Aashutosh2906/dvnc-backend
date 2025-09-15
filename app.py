from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Add this root route so you can test if backend is running
@app.route('/')
def home():
    return jsonify({
        "status": "DVNC Backend Running",
        "message": "API endpoint available at /api/dvnc",
        "version": "1.0"
    })

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

# Main API endpoint
@app.route('/api/dvnc', methods=['POST', 'OPTIONS'])
def chat():
    # Handle OPTIONS request for CORS
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    
    data = request.json
    user_message = data.get('prompt', '')
    model = data.get('model', 'synthesis')
    
    responses = {
        'synthesis': f"Analyzing through Leonardo's multidisciplinary lens: {user_message}. Combining physics, biomechanics, and anatomy principles for innovative solutions.",
        'physics': f"Physics analysis of {user_message}: Consider fluid dynamics, structural forces, and Leonardo's observations on water flow and mechanical principles.",
        'biomechanics': f"Biomechanical perspective on {user_message}: Applying joint articulation patterns and natural movement optimization from Leonardo's anatomical studies.",
        'anatomy': f"Anatomical approach to {user_message}: Implementing Vitruvian proportions and human-centered design principles."
    }
    
    return jsonify({
        'analysis': responses.get(model, responses['synthesis']),
        'confidence': 0.85 + (len(user_message) % 15) / 100  # Varying confidence
    })

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Endpoint not found", "available": ["/", "/health", "/api/dvnc"]}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
