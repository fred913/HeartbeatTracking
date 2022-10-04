import random
import time
from . import HeartbeatTrackingClient
from . import HeartbeatTrackingServer
import sys

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == "start-server":
            server = HeartbeatTrackingServer()
            server.run()
        elif sys.argv[1] == "start-test-client":
            server = HeartbeatTrackingClient("127.0.0.1")
            while True:
                try:
                    value=random.randint(70, 90)
                    print("value:", value)
                    server.update(value)
                    time.sleep(random.randint(3, 5))
                except KeyboardInterrupt:
                    print("Stopped.")
                    break

        else:
            print("Action not found")
    else:
        print("Usage:", sys.argv[0], "<action>")