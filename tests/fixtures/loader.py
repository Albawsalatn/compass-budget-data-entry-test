import pytest
from test_suite.loader import Loader
import vcr


@pytest.fixture()
def loader():
    with vcr.use_cassette(
        "fixtures/vcr_cassettes/loader.yaml", record_mode="new_episodes"
    ):
        return Loader()
