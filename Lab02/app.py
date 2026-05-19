from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher
# nếu có thêm RSA thì import ở đây

app = Flask(__name__)

# Home
@app.route("/")
def home():
    return render_template("index.html")

# Caesar
@app.route("/caesar")
def caesar():
    return render_template("caesar.html")

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    cipher = CaesarCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    cipher = CaesarCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# Vigenere
@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = VigenereCipher()
    encrypted = cipher.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted}"

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = VigenereCipher()
    decrypted = cipher.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted}"

# RailFence
@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    cipher = RailFenceCipher()
    encrypted = cipher.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted}"

@app.route("/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    cipher = RailFenceCipher()
    decrypted = cipher.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted}"

# Playfair
@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["inputPlainText"]
    key = request.form["inputKeyPlain"]
    cipher = PlayfairCipher()
    matrix = cipher.create_playfair_matrix(key)
    encrypted = cipher.playfair_encrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted}"

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["inputCipherText"]
    key = request.form["inputKeyCipher"]
    cipher = PlayfairCipher()
    matrix = cipher.create_playfair_matrix(key)
    decrypted = cipher.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted}"

# Transposition
@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKeyPlain"])
    cipher = TranspositionCipher()
    encrypted = cipher.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted}"

@app.route("/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKeyCipher"])
    cipher = TranspositionCipher()
    decrypted = cipher.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted}"

# RSA (nếu bạn có)
@app.route("/rsa")
def rsa():
    return render_template("rsa.html")

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
