
import pytest
from homework_16_1 import TeamLead

@pytest.fixture
def team_lead():

    return TeamLead("Stiv Jobs", 9500000, "Apple", "C/C++", 20000)

def test_teamlead_manager_attributes(team_lead):

    assert team_lead.name == "Stiv Jobs"
    assert team_lead.salary == 9500000
    assert team_lead.department == "Apple"

def test_teamlead_developer_attributes(team_lead):

    assert team_lead.programming_language == "C/C++"

def test_teamlead_own_attributes(team_lead):

    assert team_lead.team_size == 20000