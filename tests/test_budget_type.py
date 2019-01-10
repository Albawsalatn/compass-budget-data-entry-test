"""Tests for the budget_type table"""
import logging

import numpy as np
import pandas as pd
import pytest

logger = logging.getLogger("compass-budget")


def test_budget_type_df_name_is_unique(budget_type_df):
    duplicated = budget_type_df.name.dropna().duplicated()
    logger.debug(duplicated.value_counts())
    assert any(duplicated) is False


def test_budget_type_df_name_has_id(budget_type_df):
    """tests if an id is null for a row that has a not null name
    
    Arguments:
        budget_type_df {pandas.DataFrame}
    """
    # Rows that have non null `name`
    not_null_name = budget_type_df.name.notnull()
    not_null_id = pd.to_numeric(
        budget_type_df.id[not_null_name], errors="coerce"
    ).notnull()
    logger.debug(not_null_id)
    assert all(not_null_id) is True


def test_budget_type_df_parent_id_is_in_id(budget_type_df):
    ids = list(budget_type_df.id.dropna())
    ids.append(0)
    logger.debug(budget_type_df[budget_type_df.parent_id.isin(ids)])
    # Used = instead of is because .all() returns numpy.bool
    assert budget_type_df.parent_id.dropna().isin(ids).all() == True


def test_budget_type_df_parent_name_is_empty_if_parent_id_is_zero(budget_type_df):
    """Tests if there is a parent name with a parent_id of 0
    
    Arguments:
        budget_type_df {pandas.DataFrame}
    """

    # TODO: test for the opposite

    parent_id_zero = budget_type_df.parent_id == 0
    name_notnull = budget_type_df.name.notnull()
    # TODO: find better name
    truth = budget_type_df[parent_id_zero & name_notnull].parent_name.isnull()
    # TODO: log rows causing prblem
    assert truth.all()
