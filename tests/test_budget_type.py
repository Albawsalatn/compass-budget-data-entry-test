"""Tests for the budget_type table"""
import pandas as pd
import pytest
import vcr
from tests.fixtures.loader import loader
import logging
import numpy as np

logger = logging.getLogger("compass-budget")


@pytest.fixture()
def budget_type_df(loader):
    with vcr.use_cassette(
        "fixtures/vcr_cassettes/budget_type_df.yaml", record_mode="new_episodes"
    ):
        return loader.worksheet_to_df("budget_type")


def test_budget_type_df_name_is_unique(budget_type_df):
    # TODO: may want to include string stripping
    duplicated = (
        budget_type_df.name.replace(r"^\s*$", np.nan, regex=True).dropna().duplicated()
    )
    logger.debug(duplicated.value_counts())
    assert any(duplicated) is False
