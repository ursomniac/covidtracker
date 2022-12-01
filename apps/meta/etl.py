import pandas as pd
import sqlite3
from ..utils.db import write_to_table

def seed_state_file(write_to_db=False):
    path = 'DATA/STATE/state_region_seed.csv'
    raw = pd.read_csv(path, thousands=',').dropna(how='all')
    # fix the population issue
    raw['population'] = raw['population'].replace(',', '').astype(int)
    # Get the MA county rows out
    ma_mask = raw['name'].str.startswith('MA - ')
    df = raw.copy().loc[~ma_mask]

    ma_counties = raw.copy().loc[ma_mask]
    ma_counties['state'] = 'MA'
    if write_to_db:
        write_to_table('meta_stateregion', df)
        write_to_table('meta_uscounty', ma_counties)
    return df, ma_counties 

