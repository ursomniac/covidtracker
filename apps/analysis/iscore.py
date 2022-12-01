import pandas as pd
import datetime as dt
from ..divoc.models import DIVOCCase7DayAvg
from .common import get_sample_peak, get_df_from_query, get_df_for_date

def calc_iscore(cases, peak):
    if cases < 0.001:
        return 1.0
    p = 150. if peak < 150. else peak
    imp = 1. - (cases/p)
    if cases > 100.:
        x = 0.6 * (300 - cases) / 200.
        if x < 0:
            x = 0
        return x
    # A
    if imp > 0.9:
        score = imp
    # B
    elif imp > 0.75:
        x = (imp - 0.75) / 0.15
        score = 0.8 + (x/10.)
    # C
    elif imp > 0.50:
        x = (imp - 0.5) / 0.25
        score = 0.7 + (x/10.)
    # D
    elif imp > 0.25:
        x = (imp - 0.25) / 0.25
        score = 0.6 + (x/10.)
    # F
    else:
        score = imp * 0.6 / 0.25

    # Bonuses
    if peak < 6.0:
        r = 1. - (peak/6.)
        b = 0.1 + 0.05 * r
        score += b
    elif peak < 10.0:
        r = 1. - (peak - 6.) / 4.
        b = 0.025 + 0.075 * r
        score += b

    score = 1. if score > 1. else score
    return score

def get_iscore(as_of_date, location):
    df = get_df_from_query(as_of_date, location)
    cases = df.iloc[-1]['cases']
    peak = df['cases'].max()
    raw_iscore = 1. - cases / peak
    iscore = calc_iscore(cases, peak)
    return raw_iscore, iscore

def get_row_iscore(row):
    return calc_iscore(row['cases'], row['peak'])

def get_iscore_timeseries(location):
    df = get_df_from_query(location)
    print(df)
    # TODO: get peak values when ingesting!
    df['peak'] = df.apply(lambda row: get_sample_peak(row, df), axis=1)
    df['raw_iscore'] = 1. - df['cases'] / df['peak']
    df['iscore'] = df.apply(lambda row: get_row_iscore(row), axis=1)
    return df

def get_iscores_for_date(as_of_date):
    df = get_df_for_date(as_of_date)
    df['case_date'] = pd.to_datetime(as_of_date)
    # ERROR: This won't work = you already need to calculate peak!
    df['peak'] = df.apply(lambda row: get_sample_peak(row, df), axis=1)
    df['raw_iscore'] = 1. - df['cases'] / df['peak']
    df['iscore'] = df.apply(lambda row: get_row_iscore(row), axis=1)
    return df
