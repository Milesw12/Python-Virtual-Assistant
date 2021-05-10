def LogOutput():
    import logging
    logging.basicConfig()
    logger = logging.getLogger('assistant')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='assistant.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
