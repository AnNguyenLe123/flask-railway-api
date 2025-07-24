from flask import Flask, request, jsonify

app = Flask(__name__)
data_storage = []  # Nơi lưu dữ liệu POST

# Route hỗ trợ GET và POST
@app.route('/api/echo', methods=['GET', 'POST'])
def echo():
    if request.method == 'POST':
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"status": "error", "message": "No JSON data received"}), 400
        data_storage.append(data)
        return jsonify({"status": "received", "you_sent": data}), 200

    # Nếu là GET thì trả về dữ liệu đã lưu
    return jsonify({
        "status": "ok",
        "message": "GET request thành công",
        "stored_data": data_storage
    })

# Route chỉ GET để xem toàn bộ dữ liệu
@app.route('/api/view-data', methods=['GET'])
def view_data():
    return jsonify(data_storage)

if __name__ == '__main__':
    # Server chạy trên tất cả interface với port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
