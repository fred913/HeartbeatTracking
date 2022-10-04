from flask import Flask, request


class HeartbeatTrackingServer():

    def __init__(self):
        self.web_app = Flask("heartbeattracking")
        self.current_heartbeat = None
        self.last_update = None
