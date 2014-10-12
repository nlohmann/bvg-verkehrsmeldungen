# coding: utf8

# everything for Flask
from flask import Flask, Response, request
from flask.ext.cache import Cache
from flask.ext.compress import Compress

from datetime import datetime
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
    issues = get_issues()
    issues['request_url'] = request.url
    issues["date_updated"] = datetime.today().isoformat()
    
    return Response(json.dumps(issues, indent=2), mimetype="application/json; charset=utf-8")

if __name__ == "__main__":
    app.run()
