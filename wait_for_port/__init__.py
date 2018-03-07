import time
import socket


__version__ = "1.0.2"


def wait_for_port(host='localhost', port=80, timeout=None, retries=None, fail_on_error=False, sleep=None, verbose=False):
    port = int(port)
    timeout = float(timeout) if timeout else None
    retries = int(retries) if retries else 1
    sleep = float(sleep) if sleep else None
    exc = ""
    for retry in range(1, retries + 1):
        if retry > 1 and sleep:
            if verbose:
                print("Sleeping for %s seconds" % sleep)
            time.sleep(sleep)
        if verbose:
            timeout_msg = ""
            if timeout:
                timeout_msg = "timeout %ds " % timeout
            print("Waiting for port '%s:%s' %s(attempt %d/%d)" % (host, port, timeout_msg, retry, retries))
        try:
            s = socket.create_connection((host, port), timeout=timeout)
            s.close()
            if verbose:
                print("Port '%s:%s' is open" % (host, port))
            return True
        except socket.timeout as e:
            exc = e
        except socket.error as e:
            if fail_on_error:
                raise
            exc = e
    if verbose:
        if exc:
            exc = "(%s)" % exc
        print("Port '%s:%s' unavailable %s" % (host, port, exc))
    return False
