import pytest
from test_suite.loader import Loader
import vcr
import pandas as pd
import numpy as np


@pytest.fixture()
def loader():
    with vcr.use_cassette(
        "fixtures/vcr_cassettes/loader.yaml", record_mode="new_episodes"
    ):
        return Loader()


@pytest.fixture()
def budget_type_df(loader):
    with vcr.use_cassette(
        "fixtures/vcr_cassettes/budget_type_df.yaml", record_mode="new_episodes"
    ):
        return (
            loader.worksheet_to_df("budget_type")
            .pipe(lambda df: df.assign(id=pd.to_numeric(df.id, errors="coerce")))
            .pipe(
                lambda df: df.assign(
                    parent_id=pd.to_numeric(df.parent_id, errors="coerce")
                )
            )
            .pipe(
                lambda df: df.assign(name=df.name.replace(r"^\s*$", np.nan, regex=True))
            )
            .pipe(
                lambda df: df.assign(
                    parent_name=df.parent_name.replace(r"^\s*$", np.nan, regex=True)
                )
            )
        )
