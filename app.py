from flask import Flask, abort, request

app = Flask(__name__)


@app.route("/")
def index():
    print(f"index: {request.remote_addr}")
    return {"success": True, "msg": "message"}


@app.route("/get_ip")
def get_ip():
    return {"ip": request.remote_addr}


@app.route("/abort")
def abort_test():
    abort(403)
