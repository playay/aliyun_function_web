# 通用配置
__common_config = {
    "redis.port": 6379,
    "redis.db": 0,
    "redis.password": None,
    "redis.max_connections": 3000,
}

# 各环境配置, 启动时会选取当前环境的配置, 当前环境配置优先级高于通用配置
__all_region = {
    "cn-beijing" : {
        "env": "test",
        "mongodb.uri": "mongodb://access_manage:bHGb3X9zn8VjCG6uPB3LyGd%@inner.feling.net:27017/access_manage",
        "redis.host": "inner.feling.net",
    }
}

cfg = __common_config.copy()

def __pick_current_region_config(current_region_name):
    cfg.update(__all_region[current_region_name])