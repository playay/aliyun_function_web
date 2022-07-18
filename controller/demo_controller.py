from flask import current_app as app
from flask import request
from db.mongo import mongo_client
from db.redis import redis_client
from bson import json_util
import json

@app.route('/demo', methods=['GET', 'POST'])
def demo():
    return {
        "query_string": request.args,
        "json_body": request.get_json(),
        "redis_counter": redis_client.incr('fc'),
        "mongo": json.loads(json_util.dumps(mongo_client.access_key.find_one()))
    }

@app.route('/demo/error', methods=['GET', 'POST'])
def demo_error():
    1 / 0

@app.route('/demo/echo/<echo_url_param>', methods=['GET', 'POST'])
def demo_echo_url_param(echo_url_param):
    return echo_url_param