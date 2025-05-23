from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)  # __name__ với 2 dấu gạch dưới ở 2 bên

# Khởi tạo đối tượng CaesarCipher
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Chạy Flask app khi chạy file này trực tiếp
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
