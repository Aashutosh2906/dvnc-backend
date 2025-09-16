from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'OPTIONS', 'PUT', 'DELETE'])
def catch_all(path):
    # Log what we're receiving
    print(f"Path: {path}, Method: {request.method}")
    
    # Handle OPTIONS for CORS
    if request.method == 'OPTIONS':
        response = Response()
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response
    
    # Handle root
    if path == '':
        data = {"status": "Backend running", "path": path, "method": request.method}
        response = Response(json.dumps(data), mimetype='application/json')
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    
    # Handle api/dvnc
    if path == 'api/dvnc':
        if request.method == 'GET':
            data = {"message": "Use POST", "path": path}
        else:  # POST
            body = {}
            try:
                body = request.get_json() or {}
            except:
                pass
            data = {
                "analysis": f"Leonardo analyzes: {body.get('prompt', 'test')}",
                "confidence": 0.9
            }
        
        response = Response(json.dumps(data), mimetype='application/json')
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    
    # Fallback
    data = {"error": "Not found", "path": path, "method": request.method}
    response = Response(json.dumps(data), mimetype='application/json', status=404)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
