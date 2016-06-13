#!/usr/bin/python
# LED main
# 2016-05-01 K.OHWADA @ FabLab Kannai

import sys
import argparse
from server import server_run

# constant
SERVER_HOST_DEFAULT = "0.0.0.0"
SERVER_PORT_DEFAULT = 5010
PIN_LED_DEFAULT = 11

# main
def main():
    parser = argparse.ArgumentParser(prog="run")
    parser.add_argument("--host", action="store", type=str, dest="host",
        help="Specify the server host")
    parser.add_argument("--port", action="store", type=int, dest="port",
        help="Specify the server port")
    parser.add_argument("--pin", action="store", type=int, dest="pin",
        help="Specify the LED pin")
    args = parser.parse_args()
    host = initParam(args.host, SERVER_HOST_DEFAULT)
    port = initParam(args.port, SERVER_PORT_DEFAULT)
    pin = initParam(args.pin, PIN_LED_DEFAULT)
    server_run(host, port, pin)

def initParam(param, default):
    if param is not None:
        val = param
    else:
        val = default
    return val

if __name__ == "__main__":
    main()
