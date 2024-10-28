import pytest
from unittest.mock import patch
from test_system import log_event

LOG_FILE = "login_system.log"


@pytest.mark.parametrize("username, status, expected_log_method, expected_message", [
    ("test_user", "success", "info", "Login event - Username: test_user, Status: success"),
    ("test_user", "expired", "warning", "Login event - Username: test_user, Status: expired"),
    ("test_user", "failed", "error", "Login event - Username: test_user, Status: failed")

])
@patch("test_system.logging.getLogger")

def test_log_event(mock_get_logger, username, status, expected_log_method, expected_message):

    mock_logger = mock_get_logger.return_value

    log_event(username, status)
    log_method = getattr(mock_logger, expected_log_method)
    log_method.assert_called_once_with(expected_message)

    with open(LOG_FILE, "r") as f:
        logs = f.readlines()


    assert len(logs) > 0, "Log file is empty"

    last_log = logs[-1].strip()
    assert expected_message in last_log, f"Expected '{expected_message}' in last log, got '{last_log}'"
