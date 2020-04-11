import htmlmin
from flask import Flask
from components import render
app = Flask(__name__)
import sys


@app.route('/')
def homepage():
    return render()


def export():
    html = render()
    minified = htmlmin.minify(html, remove_empty_space=True)
    filename = "../index.html"
    f = open(filename, 'w')
    f.write(minified)
    f.close()


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        if sys.argv[1] == "build":
            export()
            exit(0)
    app.run(use_reloader=True, debug=True)
