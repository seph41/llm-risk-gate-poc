# app.py

from flask import Flask, request
app = Flask(__name__)

@app.route("/vulnerable")
def vulnerable():
    # Injection simple volontaire
    param = request.args.get("param")
    return f"Hello {param}"  # vulnérable à XSS
