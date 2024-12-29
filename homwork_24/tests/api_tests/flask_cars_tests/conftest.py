from sys import modules

import pytest

@pytest.fixture(scope='module')
def base_url():
    print('Calling base_url fixture')
    return 'http://127.0.0.1:8080'