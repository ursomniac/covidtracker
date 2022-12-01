import pandas as pd
from ..analysis.common import get_sample_peak
from ..utils.db import write_to_table
"""
Still haven't found a way to get DIVOC-91 data from a specific URL.
"""
DEFAULT_AVG_FILE_PATH = 'DATA/DIVOC/91-DIVOC-states-normalized.csv'
DEFAULT_TOTAL_FILE_PATH = 'DATA/DIVOC/91-DIVOC-states.csv'

def load_avg_data(fn=None, keep_nulls=False, return_raw=False, write_to_db=False):
    fn = DEFAULT_AVG_FILE_PATH if fn is None else fn
    table_name = 'divoc_divoccase7dayavg' if write_to_db else None
    df = load_divoc_file(fn, table_name=table_name, keep_nulls=keep_nulls, return_raw=return_raw)
    return df

def load_total_data(fn=None, keep_nulls=False, return_raw=False, write_to_db=False):
    fn = DEFAULT_TOTAL_FILE_PATH if fn is None else fn
    table_name = 'divoc_divoccasetotal' if write_to_db else None
    df = load_divoc_file(fn, table_name=table_name, keep_nulls=keep_nulls, return_raw=return_raw)
    return df

def load_divoc_file(fn, table_name=None, keep_nulls=False, return_raw=False, ):
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

    if table_name is not None:
        write_to_table(table_name, df)
    return df

