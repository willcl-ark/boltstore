import argparse
import selectors
import socket
import traceback

import libclient

sel = selectors.DefaultSelector()


def create_request(action, value):
    if action == "invoice":
        return dict(
                type="text/json",
                encoding="utf-8",
                content=dict(action=action, value=value),
        )
    else:
        return dict(
                type="binary/custom-client-binary-type",
                encoding="binary",
                content=bytes(action + value, encoding="utf-8"),
        )


def start_connection(host, port, request):
    addr = (host, port)
    print("starting connection to", addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    message = libclient.Message(sel, sock, addr, request)
    sel.register(sock, events, data=message)


def connect(host, port, action, value):
    request = create_request(action, value)
    start_connection(host, port, request)

    try:
        while True:
            events = sel.select(timeout=1)
            for key, mask in events:
                message = key.data
                try:
                    message.process_events(mask)
                except Exception:
                    print(
                            "main: error: exception for",
                            f"{message.addr}:\n{traceback.format_exc()}",
                    )
                    message.close()
            # Check for a socket being monitored to continue.
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("caught keyboard interrupt, exiting")
    finally:
        sel.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Connect to boltstore server.')
    parser.add_argument('host',
                        type=str,
                        help='host to connect to')
    parser.add_argument('port',
                        type=int,
                        help='port to connect to')
    parser.add_argument('action',
                        type=str,
                        help='action for server')
    parser.add_argument('value',
                        type=str,
                        help='value of action to process')
    args = parser.parse_args()
    if args.host and args.port and args.action and args.value:
        connect(args.host, args.port, args.action, args.value)
    else:
        print('Please provide host, port action and value')
