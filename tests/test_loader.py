import os
import logging

import pandas as pd
import pygsheets

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger("compass-budget")


def test_loader_returns_sheet(loader):
    assert isinstance(loader.loaded_data, pygsheets.Spreadsheet)


def test_loader_returns_worksheet_as_dataframe(loader):
    actual = loader.worksheet_to_df("budget_by_type")
    logger.debug(actual)
    expected = pd.DataFrame
    assert (actual, expected)
