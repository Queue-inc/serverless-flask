# coding: utf8

from functools import wraps
import logging

class Interceptor:
    """
        Interceptor
    """

    def logger(f):
        """
            logger
        """
        @wraps(f)
        def inner(*args, **kwargs):
            # TODO should be fixed to dynamically
            logger = logging.getLogger(f.__name__)
            logger.setLevel(logging.DEBUG)
            from flask import request
            logger.info("[header] --  " + str(request.headers))
            logger.info("[body] -- " + str(request.path))
            result = f(*args, **kwargs)
            return result
        return inner
    
    
    def middleware(func):
        """
            custom middleware
        """
        def _decorator(f):
            @wraps(f)
            def inner(*args, **kwargs):
                from flask import request
                data = func(request)
                if isinstance(data, dict):
                    kwargs.update(data)
                elif isinstance(data, list) or isinstance(data, tuple):
                    args.extend(data) 
                else:
                    raise ValueError("Middleware should return dict, list, tuple.")
                result = f(*args, **kwargs)
                return result
            return inner
        return _decorator