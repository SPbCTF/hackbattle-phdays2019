from flask import Flask, render_template, send_file
app = Flask(__name__)


flag = "battles{y0u_r34lly_l0v3_r4nd0m}"

# seed = 667878891
m = 1073741827
c = 195523042
n = 0x7fffffff


def next():
    global seed, m, c, n
    seed = (seed * m + c) & n
    return seed


@app.route('/')
def index():
    return send_file('index.html')


@app.route('/check/<int:_seed>')
def check(_seed):
    global seed
    seed = _seed
    generated = [hex(next()) for i in range(5)]
    if int(generated[-1], 16) == 0xba771e3:
        generated.append(flag)
    else:
        generated.append("NOPE:(")
    return "\n".join(generated)


@app.route('/lcg.py')
def source():
    return send_file('public.py')


if __name__ == "__main__":
    app.run(port=31337, host="0.0.0.0")
