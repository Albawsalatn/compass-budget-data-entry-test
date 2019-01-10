# compass-budget-dataentry-test
Test suite for data entry of the Tunisian finance law

## General constraints

* Each row must have an ID.
* For Hierarchichal tables, parent_name having a non null value and parent_id having a value other than 0 are mutually exclusive.
* For Hierarchichal tables, parent_id must exist in the ID columns.
* For Numerical columns, all values must be greater than 0.
* For tables that are used in other tables, identifying columns must be unique.