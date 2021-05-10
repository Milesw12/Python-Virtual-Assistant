def LogOutput():
    import logging
    logger = logging.getLogger('')
    logger.setLevel(logging.CRITICAL)
    fh = logging.FileHandler('my_log_info.log')
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
    fh.setFormatter(formatter)

    logger.addHandler(fh)

