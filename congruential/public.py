from flask import Flask
app = Flask(__name__)


flag = None

m = 1073741827
c = 195523042
n = 0x7fffffff


def next():
    global seed, m, c, n
    seed = (seed * m + c) & n
    return seed


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


if __name__ == "__main__":
    app.run(port=31337)
