from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask inside Docker!"

if __name__ == "__main__":
    # écoute sur toutes les interfaces, port 8080
    app.run(host="0.0.0.0", port=8080)
