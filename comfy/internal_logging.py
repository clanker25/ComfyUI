import logging


DETAIL = 16
logging.addLevelName(DETAIL, "DETAIL")


def detail(message, *args, **kwargs):
    kwargs.setdefault("stacklevel", 2)
    logging.log(DETAIL, message, *args, **kwargs)
