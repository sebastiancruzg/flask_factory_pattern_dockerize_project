import os
import logging
import sys

def log_error(error: Exception) -> None:
    """Debug error

    Args:
        error (Exception): handle error
    """
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    logging.error(exc_obj)
    logging.error(exc_type)
    logging.error('%s: %s',fname ,str(exc_tb.tb_lineno))
    logging.error(error)
