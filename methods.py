import flask
import ping3

from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
@cross_origin()
def give_js():
    ip = request.remote_addr
    print("Browser", ip)

    return render_template('index.html')


@app.route("/js")
@cross_origin()
def get_js():
    ip = request.remote_addr
    print("JS", ip)

    return render_template('index.html')


@app.route("/rtt")
@cross_origin()
def send_rtt():
    rtt = request.args.get("rtt")
    ip = request.remote_addr
    print("FINALLY", ip)
    print("Client RTT", rtt)

    r = ping3.ping(ip)
    print("Server RTT", r * 1000)

    return render_template('index.html')


if __name__ == '__main__':
    app.run('95.182.120.116', port=8181, debug=True)
    # my_methods.find_ip()
    # my_methods.rtt()
    # my_methods.rtt_over_proxy()
    # my_methods.test_packet()

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
"main.py" 48L, 912C                                                                                                                                                                                             1,1           All
