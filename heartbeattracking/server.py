import time
from flask import Blueprint, request
import flask


class HeartbeatTrackingServer():

    def __init__(self):
        self.blueprint = Blueprint("heartbeattracking")
        self.current_heartbeat = None
        self.last_update = None
        self._register_routes()
        self.heartbeat_timeout = 16

    def _register_routes(self):
        self.blueprint.add_url_rule("/update",
                                    view_func=self._update_web_controller,
                                    methods=['POST', "GET"],
                                    endpoint="heartbeat_update")
        self.blueprint.add_url_rule(
            "/get",
            view_func=self._get_heartbeat_web_controller,
            methods=["GET"],
            endpoint="heartbeat_get")
        self.blueprint.add_url_rule(
            "/show",
            view_func=self.show_heartbeat_web_controller,
            methods=["GET"],
            endpoint="heartbeat_show")

    def _update_web_controller(self):
        # post a heartbeat data
        self.update_time = time.time()
        self.current_heartbeat = float(
            request.form.get("value",
                             default=request.args.get("value", default=None)))
        assert self.current_heartbeat is not None
        return "OK"

    def _get_heartbeat_web_controller(self):
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

    def register_to_app(self, app: flask.Flask, **kwargs):
        url_prefix = kwargs.pop("url_prefix", "/heartbeat")
        app.register_blueprint(self.blueprint, url_prefix=url_prefix, **kwargs)