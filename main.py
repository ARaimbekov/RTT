import methods as my_methods
import flask
import ping3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def give_js():
    ip = request.remote_addr
    print("Browser", ip)

    return render_template('index.html')


@app.route("/js")
def get_js():
    ip = request.remote_addr
    print("JS", ip)

    return render_template('index.html')


@app.route("/rtt")
def send_rtt():
    rtt = request.args.get("rtt")
    ip = request.remote_addr
    print("FINALLY", ip)
    print("Client RTT", rtt)

    r = ping3.ping(ip)
    print("Server RTT", r * 1000)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # my_methods.find_ip()
    # my_methods.rtt()
    # my_methods.rtt_over_proxy()
    # my_methods.test_packet()
