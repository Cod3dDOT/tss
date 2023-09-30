from bs4 import BeautifulSoup
from tss_cmd.api.exceptions import ParseException

from tss_cmd.api.reqs import get, post


def parse_request_token(html):
    """Parses request token from page"""
    soup = BeautifulSoup(html, "html.parser")

    request_token_hidden_input = soup.find(
        "input", {"name": "__RequestVerificationToken"}
    )

    if not request_token_hidden_input:
        raise ParseException("Failed to parse hidden request token")

    return request_token_hidden_input.get("value") # type: ignore


def login(user: str, passwd: str) -> bool:
    """Log in user into tss account"""

    login_page = get("/Identity/Account/Login")
    request_token = parse_request_token(login_page.text)

    login_request = post(
        "/Identity/Account/Login?ReturnUrl=%2F",
        {
            "Input.Name": user,
            "Input.Password": passwd,
            "Input.RememberMe": True,
            "__RequestVerificationToken": request_token,
        },
    )

    soup = BeautifulSoup(login_request.text, "html.parser")
    loggedIn = soup.find("a", {"href": "/Identity/Account/Manage/ChangePasswords"}) is not None

    return loggedIn


def answer(ticket: int, answer: str, log: str = "") -> tuple[bool, str, int]:
    """Submits answer to a given task and returns (correct, response)"""

    request = post(
        "/task/check?ReturnUrl=%2F",
        {"ticketId": ticket, "userAnswer": answer, "log": log if log else answer},
    )

    return (
        request.status_code < 299,
        request.text.encode().decode("unicode_escape").replace("\r", ""),
        request.status_code
    )
