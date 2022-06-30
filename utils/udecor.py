from functools import wraps,lru_cache,partial
import time
from random import random

def retry(count:int=3,retry_except:tuple=(Exception,),retry_interval:float=3,random_interval:bool=True,log=None):
    """retry decorator support retry on condition of specific exceptions

    Args:
        func (function): function that will retry
        count (int, optional): should retry count. Defaults to 3.
        retry_except (tuple, optional): retry on condition of specific exceptions. Defaults to (Exception,).
        retry_interval:retry time between next func execute
        random_interval:if True,use random time between 0.1~retry_interval
        log (log, optional): logging object. Defaults to None.

    Returns:
        func()
    """
    if not log:
        log=lambda _:_
        log.info=print
        log.error=print
    def _wrap(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            for i in range(count):
                try:
                    result = func(*args, **kwargs)
                    return result
                except retry_except as e:
                    log.error(
                        "retrying...func_name:{0},count:{1},msg:{2}".format(func.__name__, i + 1,str(e)))
                    if random_interval:
                        time.sleep(random()*retry_interval)
                        continue
                    time.sleep(retry_interval)
            log.info("try {0} times still failed, func:{1},default return None".format(count, func.__name__))
            return 
        return _wrapper
    return _wrap

