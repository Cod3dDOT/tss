from os import path


PAYLOAD = ""

with open(path.join(path.dirname(__file__), "payloads/template.js"), "r") as file:
    PAYLOAD = file.read()

PAYLOAD_FUNCTIONS = {
    "cmd": "run",
    "pwsh": "run_pwsh"
}
