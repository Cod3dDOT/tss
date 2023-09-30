import requests

from tss_cmd.api.api_globals import SESSION, TSS_ENDPOINT, CONN_TIMEOUT


def post(url: str, data: dict) -> requests.Response:
    """Makes an authorized POST request"""
    return SESSION.post(
        TSS_ENDPOINT + url,
        data=data,
        timeout=CONN_TIMEOUT,
    )


def get(url: str) -> requests.Response:
    return SESSION.get(
        TSS_ENDPOINT + url,
        timeout=CONN_TIMEOUT,
    )
