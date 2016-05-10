#!/usr/bin/env python
# LED main
# 2016-05-01 K.OHWADA @ FabLab Kannai

import sys
import argparse
from server import server_run

# constant
SERVER_HOST_DEFAULT = "0.0.0.0"
SERVER_PORT_DEFAULT = 5010

# main
def main():
    parser = argparse.ArgumentParser(prog="run")
    parser.add_argument("--host", action="store", type=int, dest="host",
        help="Specify the host on which to bind the server")
    parser.add_argument("--port", action="store", type=int, dest="port",
        help="Specify the port on which to bind the server")
    args = parser.parse_args()
    host = initServerHost(args.host)
    port = initServerPort(args.port)
    server_run(host, port)

def initServerHost(param_host):
    if param_host is not None:
        host = param_host
    else:
        host = SERVER_HOST_DEFAULT
    return host

def initServerPort(param_port):
    if param_port is not None:
        port = param_port
    else:
        port = SERVER_PORT_DEFAULT
    return port

if __name__ == "__main__":
    main()
