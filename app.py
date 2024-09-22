from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# POST method: Handles data processing
@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Extracting the data from the request
        data = request.json['data']
        file_b64 = request.json.get('file_b64', None)

        # Separate numbers and letters
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [char for char in data if char.islower()]

        # Find the highest lowercase alphabet (last alphabet in 'a' to 'z')
        highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else None

        # File handling (if file is included)
        file_valid = False
        file_mime_type = None
        file_size_kb = None
        if file_b64:
            try:
                file_data = base64.b64decode(file_b64)
                file_size_kb = len(file_data) / 1024
                file_valid = True  # Assuming it's valid for now
                file_mime_type = "image/png"  # For example
            except:
                file_valid = False

        # Preparing the response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else [],
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }

        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

# GET method: Always returns operation_code = 1
@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)

