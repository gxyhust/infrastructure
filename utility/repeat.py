def retry(max_retries: int = 3, interval: (int, float) = 0,
          exceptions: list = None, front_waiting: bool = False):
    """
    重试装饰器。
    被修饰的函数被要求只有两类结果，要么是异常，要么是正确的结果。
    :param max_retries:  重试次数。
    :param interval:  可重试异常发生时、重试的延迟，单位秒。
    :param exceptions:  可重试异常的list,单个异常也需包装成list传入。
    :param front_waiting:  默认为false即不前置等待
    """
    def wrapper(f):
        def _wrapper(*args, **kwargs):
            if front_waiting:
                time.sleep(interval)
            start = time.time()
            for i in range(1, max_retries + 1):
                try:
                    res = f(*args, **kwargs)
                    if res:
                        consume_time = time.time() - start
                        logger.info('执行__{}__耗时__{}'.format(f.__name__, str(consume_time)))
                        return res
                except Exception as e:
                    if i == max_retries:
                        raise e
                    if e.__class__ in exceptions:
                        if interval > 0:
                            logger.error("第{}次重试".format(str(i + 1)))
                            time.sleep(interval)
                    else:
                        # 非重试异常需要直接抛出
                        raise e
        return _wrapper
    return wrapper
