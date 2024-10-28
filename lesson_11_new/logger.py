import pytest
import os
from test_system import log_event

LOG_FILE = 'login_system.log'

def test_log_event_success():




    log_event("test_user", "success")


    with open(LOG_FILE, "r") as f:
        logs = f.readlines()


    assert logs, "Log file is empty"
    assert "Login event - Username: test_user, Status: success" in logs[-1], \
        f"Expected 'Login event - Username: test_user, Status: success' in logs, got: {logs[-1].strip()}"

def test_log_event_expired():




    log_event("test_user", "expired")

    with open(LOG_FILE, "r") as f:
        logs = f.readlines()


    assert logs, "Log file is empty"
    assert "Login event - Username: test_user, Status: expired" in logs[-1], \
        f"Expected 'Login event - Username: test_user, Status: expired' in logs, got: {logs[-1].strip()}"

def test_log_event_failed():




    log_event("test_user", "failed")


    with open(LOG_FILE, "r") as f:
        logs = f.readlines()


    assert logs, "Log file is empty"
    assert "Login event - Username: test_user, Status: failed" in logs[-1], \
        f"Expected 'Login event - Username: test_user, Status: failed' in logs, got: {logs[-1].strip()}"