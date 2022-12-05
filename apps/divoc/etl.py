import pandas as pd
from ..utils.db import write_to_table
from .utils import add_calculations_to_time_series

"""
Still haven't found a way to get DIVOC-91 data from a specific URL.
"""
DEFAULT_AVG_FILE_PATH = 'DATA/DIVOC/91-DIVOC-states-normalized.csv'
DEFAULT_TOTAL_FILE_PATH = 'DATA/DIVOC/91-DIVOC-states.csv'  # Do I want this?
DEFAULT_DAILY_FILE_PATH = "DATA/DIVOC/91-DIVOC-daily-states.csv"

def load_avg_data(fn=None, keep_nulls=False, return_raw=False, write_to_db=False, debug=False):
    fn = DEFAULT_AVG_FILE_PATH if fn is None else fn
    table_name = 'divoc_divoccase7dayavg' if write_to_db else None
    df = load_divoc_file(fn, keep_nulls=keep_nulls, return_raw=return_raw)
    df_with_calc = add_calculations_to_time_series(df, scores=True, debug=debug)
    if write_to_db:
        write_to_table(table_name, df_with_calc)
    return df_with_calc


def load_daily_data(fn=None, keep_nulls=True, return_raw=False, write_to_db=False, debug=False):
    fn = DEFAULT_DAILY_FILE_PATH if fn is None else fn
    table_name = 'divoc_divoccasedaily' if write_to_db else None
    df = load_divoc_file(fn, keep_nulls=keep_nulls, return_raw=return_raw)
    df_with_calc = add_calculations_to_time_series(df)
    if write_to_db:
        write_to_table(table_name, df_with_calc)
    return df


def load_total_data(fn=None, keep_nulls=False, return_raw=False, write_to_db=False):
    fn = DEFAULT_TOTAL_FILE_PATH if fn is None else fn
    table_name = 'divoc_divoccasetotal' if write_to_db else None
    df = load_divoc_file(fn, keep_nulls=keep_nulls, return_raw=return_raw)
    if write_to_db:
        write_to_table(table_name, df)
    return df


def load_divoc_file(fn, keep_nulls=False, return_raw=False):
    raw = pd.read_csv(fn)
    if return_raw:
        return raw

    # Change to timeseries:  location, date, value
    pass1 = pd.melt(raw, id_vars=['location'], value_vars=raw.columns.to_list()[1:])
    pass1['case_date'] = pd.to_datetime(pass1['variable'])
    pass1.rename(columns={'value': 'cases'}, inplace=True)
    pass1.drop(columns=['variable'], inplace=True)
    # Return filtered by NaN - or not
    if keep_nulls:
        df = pass1
    else:
        nulls = pass1['cases'].isnull()
        df = pass1[~nulls]
    return df

