from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    env_name = os.getenv("APP_ENV", "local")
    return jsonify({
        "message": "Bulutli texnologiyalar - 1-topshiriq",
        "environment": env_name,
        "status": "OK"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)