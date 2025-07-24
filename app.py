from flask import Flask, request, jsonify

app = Flask(__name__)
EIP_KEY = "d3aefb2f5c4f4b3f8c90a7b8dcd9d1ef"  # key ngẫu nhiên bạn vừa tạo
data_storage = []

# Middleware kiểm tra API key
@app.before_request
def check_key():
    if request.path == '/':
        return
    api_key = request.headers.get('EIP-KEY')
    if api_key != EIP_KEY:
        return jsonify({"error": "Unauthorized"}), 401

@app.route('/')
def home():
    return jsonify({"message": "API server is running", "status": "ok"})

@app.route('/api/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"status": "error", "message": "No JSON data"}), 400
        data_storage.append(data)
        return jsonify({"status": "received", "data": data})
    return jsonify({"status": "ok", "stored_data": data_storage})

@app.route('/api/view-data', methods=['GET'])
def view_data():
    return jsonify(data_storage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
