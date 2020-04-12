import sys
from livereload import Server
import htmlmin
from flask import Flask
from components import render
app = Flask(__name__)


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
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve()
