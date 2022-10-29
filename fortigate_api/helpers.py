"""Helper functions"""

import time


def time_spent(func):
    """Wrapper measure function execution time"""

    def wrap(*args, **kwargs):
        """Wrapper"""
        started = time.time()
        try:
            _return = func(*args, **kwargs)
        except Exception:
            elapsed = time.time() - started
            print("====== {:s}, spent {:.3f}s ======".format(func.__name__, elapsed))
            raise
        elapsed = time.time() - started
        print("====== {:s}, spent {:.3f}s ======".format(func.__name__, elapsed))
        return _return

    return wrap
