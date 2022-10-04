import time
from flask import Flask, request
import flask


class HeartbeatTrackingServer():

    def __init__(self):
        self.web_app = Flask("heartbeattracking")
        self.current_heartbeat = None
        self.last_update = None
        self.register_routes()
        self.heartbeat_timeout = 16

    def register_routes(self):
        self.web_app.add_url_rule("/heartbeat/update",
                                  view_func=self.update_web_controller,
                                  methods=['POST', "GET"],
                                  endpoint="heartbeat_update")
        self.web_app.add_url_rule("/heartbeat/get",
                                  view_func=self.get_heartbeat_web_controller,
                                  methods=["GET"],
                                  endpoint="heartbeat_get")
        self.web_app.add_url_rule("/heartbeat/show",
                                  view_func=self.show_heartbeat_web_controller,
                                  methods=["GET"],
                                  endpoint="heartbeat_show")

    def update_web_controller(self):
        # post a heartbeat data
        self.update_time = time.time()
        self.current_heartbeat = float(
            request.form.get("value",
                             default=request.args.get("value", default=None)))
        assert self.current_heartbeat is not None
        return "OK"

    def get_heartbeat_web_controller(self):
        # get heartbeat data
        assert self.current_heartbeat
        format_ = request.args.get("format", default="plain")
        if format_ == 'plain':
            assert (time.time() - self.update_time) < self.heartbeat_timeout
            return str(self.current_heartbeat)
        elif format_ == "json":
            return flask.jsonify({
                "value":
                self.current_heartbeat,
                "last_update":
                self.update_time,
                "outdated":
                not ((time.time() - self.update_time) < self.heartbeat_timeout)
            })
        return "Format method '%s' not found" % (format_, ), 404

    def show_heartbeat_web_controller(self):
        return flask.render_template("hb_show.html")

    def run(self):
        self.web_app.run("0.0.0.0", 5999)