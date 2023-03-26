from multiprocessing import cpu_count



# Socket Path

bind = '0.0.0.0:8090'



# Worker Options

workers = cpu_count() * 2 + 1

worker_class = 'uvicorn.workers.UvicornWorker'



# Logging Options

loglevel = 'debug'

accesslog = '/root/api/access_log'

errorlog =  '/root/api/error_log'
