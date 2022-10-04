import requests


class HeartbeatTrackingClient:

    def __init__(self,
                 host: str,
                 port: int = 5999,
                 is_ssl: bool = False) -> None:
        self.session = requests.Session()
        self.host = (str(host), int(port), bool(is_ssl))

    def update(self, value):
        response = self.session.post(
            f"{'https' if self.host[2] else 'http'}://{self.host[0]}:{self.host[1]}/heartbeat/update",
            data={"value": value})
        assert response.status_code == 200

    def get(self):
        response = self.session.get(
            f"{'https' if self.host[2] else 'http'}://{self.host[0]}:{self.host[1]}/heartbeat/get?format=json"
        )
        assert response.status_code == 200
        assert not response.json()['outdated']
        return response.json()['value']