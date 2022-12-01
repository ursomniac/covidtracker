import pandas as pd
from ..utils.db import write_to_table

ENDPOINTS = {
    'world': 'https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/vaccinations.csv?raw=true',
    'state': 'https://github.com/owid/covid-19-data/blob/master/public/data/vaccinations/us_state_vaccinations.csv?raw=true'
}

def load_data(write_to_db=False, sample='state', keep_nulls=False):
    endpoint = ENDPOINTS[sample]
    raw = pd.read_csv(endpoint)
    raw['sample_date'] = pd.to_datetime(raw['date'])
    if keep_nulls:
        df = raw.copy()
    else:
        df = raw.dropna(subset=['total_boosters_per_hundred', 'people_fully_vaccinated_per_hundred', 'people_vaccinated_per_hundred'], how='all')
    if write_to_db:
        write_to_table('vaccine_usvaccination', df)
    return raw

