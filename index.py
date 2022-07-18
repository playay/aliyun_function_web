def initializer(context):
    import logging
    logger = logging.getLogger() 
    logger.info('初始化函数计算实例, 开始')

    global base_path
    base_path = '/{}'.format(context.service.name)

    import region_config
    region_config.__pick_current_region_config(context.region)

    logger.info('初始化 flask 实例')
    global app
    from flask import Flask
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    
    with app.app_context():
        logger.info('注册 flask web controller')
        import controller
        

    logger.info('初始化函数计算实例, 完成')


def handler(environ, start_response):
    environ['PATH_INFO'] = environ['PATH_INFO'][len(base_path):]
    environ['SCRIPT_NAME'] = base_path
    return app(environ, start_response)