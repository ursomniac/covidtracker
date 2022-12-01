import pandas as pd
import datetime as dt
from .common import get_peak, get_df_from_query, get_df_for_date
from ..divoc.models import DIVOCCase7DayAvg

def calc_rscore(rate, peak, calib=300.):
    if rate < 0.01:
        return 0.
    
    if rate <= 2.0: # A
        x = rate / 2. 
        score = 1.0 - x
    elif rate <= 6.0: # B
        x = (rate - 2.) / 4.
        score = 0.9 - x
    elif rate <= 10.0: # C
        x = (rate - 6.) / 4.
        score = 0.8 - x
    elif rate <= 15.0:
        x = (rate - 10.) / 5.
        score = 0.7 - x
    else:
        x = (calib - rate) / (calib - 15.)
        score = x * 0.6
    score = 0. if score < 0. else score
    return score

def get_rscore(as_of_date, location):
    as_of_date = dt.date(2030, 1, 1) if as_of_date is None else as_of_date
    qs = DIVOCCase7DayAvg.objects.filter(location=location, case_date__lte=as_of_date)
    values = qs.values('case_date', 'cases')
    df = pd.DataFrame.from_records(values).set_index('case_date')
    cases = df.iloc[-1]['cases']
    peak = df['cases'].max()
    raw_iscore = 1 - cases / peak
    rscore = calc_rscore(cases, peak)
    return rscore

def get_row_rscore(row):
    return calc_rscore(row['cases'], row['peak'])

def get_rscore_timeseries(location):
    df = get_df_from_query(location)
    df['peak'] = df.apply(lambda row: get_peak(row, df), axis=1)
    df['rscore'] = df.apply(lambda row: get_row_rscore(row), axis=1)
    return df

def get_rscores_for_date(as_of_date):
    df = get_df_for_date(as_of_date)
    df['case_date'] = pd.to_datetime(as_of_date)
    df['peak'] = df.apply(lambda row: get_peak(row, df), axis=1)
    df['rscore'] = df.apply(lambda row: get_row_rscore(row), axis=1)
    return df
    
