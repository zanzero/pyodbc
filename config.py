reload = True
daemon = True
bind = '0.0.0.0:6666'
worker_class = 'sanic.worker.GunicornWorker'
loglevel = 'debug'
accesslog = 'access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = 'error.log'