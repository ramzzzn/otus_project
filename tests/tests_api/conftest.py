import pytest
from api_tools.joke_api import JokeAPI


@pytest.fixture(scope='function')
def joke_api():
    return JokeAPI()
