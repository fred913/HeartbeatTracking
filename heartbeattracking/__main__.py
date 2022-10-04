import random
import time
from . import HeartbeatTrackingClient
from . import HeartbeatTrackingServer
import sys
from flask import Flask

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == "start-server":
            app = Flask("heartbeattracking")
            tracking_server_bp = HeartbeatTrackingServer()
            tracking_server_bp.register_to_app(app)
            app.run("0.0.0.0", 5999)

        elif sys.argv[1] == "start-test-client":
            client = HeartbeatTrackingClient("127.0.0.1")
            while True:
                try:
                    value = random.randint(70, 90)
                    print("value:", value)
                    client.update(value)
                    time.sleep(random.randint(3, 5))
                except KeyboardInterrupt:
                    print("Stopped.")
                    break
        elif sys.argv[1] == "start-poll-client":
            client = HeartbeatTrackingClient("127.0.0.1")
            while True:
                try:
                    print("value:", client.get(), end="     \r")
                    time.sleep(1)
                except KeyboardInterrupt:
                    print("Stopped.")
                    break

        else:
            print("Action not found")
    else:
        print("Usage:", sys.argv[0], "<action>")