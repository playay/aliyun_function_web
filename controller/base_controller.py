from flask import current_app as app
from flask import request
import traceback

@app.before_request
def before_request():
    app.logger.info(
        '[request] method: %s, url: %s, headers: %s, body: %s,',
        request.method, 
        request.url, 
        request.headers.to_wsgi_list(), 
        request.get_data().decode('utf8')
    )

@app.after_request
def after_request(response):
    app.logger.info(
        '[response] status: %s, headers: %s, body: %s',
        response.status_code, 
        response.headers.to_wsgi_list(), 
        response.get_data().decode('utf8')
    )
    return response

@app.errorhandler(Exception)
def handle_exceptiont(e):
    return {
        'success': False,
        'msg': str(e),
        'detail': traceback.format_exc()
    }

@app.route('/ping', methods=['GET', 'POST'])
def ping():
     return 'pong'