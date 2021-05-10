def LogOutput():
    import logging
    logger = logging.getLogger('Assistant')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(filename='assistant.log', encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
    logger.addHandler(Handler)

