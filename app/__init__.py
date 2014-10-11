# coding: utf8

# everything for Flask
from flask import Flask, Response
from flask.ext.cache import Cache
from flask.ext.compress import Compress

from bvg import get_issues
import json

# the Flask app
app = Flask(__name__)
app.debug = True

# set cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# enable gzip compression
Compress(app)

@app.route("/")
@cache.cached(timeout=1800)
def index():
    return Response(json.dumps(get_issues(), indent=2), mimetype="application/json; charset=utf-8")

if __name__ == "__main__":
    app.run()
