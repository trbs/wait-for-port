import sys
import argparse
from . import wait_for_port


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help="dns name or ip adress")
    parser.add_argument('port', type=int, help="Port number")
    parser.add_argument('-t', '--timeout', dest="timeout", type=int, help="Timeout waiting for port")
    parser.add_argument('-r', '--retries', dest="retries", type=int, help="How many times to retry")
    parser.add_argument('-f', '--fail-on-error', dest="fail_on_error", action="store_true", default=False, help="Exit on socket error")
    parser.add_argument('-s', '--sleep', dest="sleep", type=int, help="Amount of seconds to sleep between retries")
    parser.add_argument('-v', '--verbose', dest="verbose", action="store_true", default=False, help="Verbosity")
    args = parser.parse_args()

    host = args.host
    port = args.port
    timeout = args.timeout
    retries = args.retries
    fail_on_error = args.fail_on_error
    sleep = args.sleep
    verbose = args.verbose

    if wait_for_port(host=host, port=port, timeout=timeout, retries=retries, fail_on_error=fail_on_error, sleep=sleep, verbose=verbose):
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()
