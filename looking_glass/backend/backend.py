from flask import Flask, render_template, request, render_template_string
import requests as rq

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/look")
def look():
    url = request.args.get('url')
    banned = ['127.00.00.1', '127.0.0.1', 'localhost']
    if any([x in url for x in banned]):
        return "Sorry"
    resp = rq.get(url)
    return render_template_string(resp.text)


if __name__ == "__main__":
    app.run()
