import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
from apps.analysis.iscore import calc_iscore, calc_raw_iscore
from apps.analysis.nscore import calc_nscore
from apps.analysis.rscore import calc_rscore
from apps.analysis.vscore import calc_vscore
from apps.meta.models import StateRegion
from apps.vaccine.models import USVaccination

def get_last_non_null_entry(df):
    """
    Last entry of a timeseries where cases is not NaN.
    """
    return df.loc[df['cases'].isnull()==False].iloc[-1]

def plot_time_series(df):
    df.plot(x='case_date', y='cases')
    pl.show()

def plot_scores(df):
    df.plot(x='case_date', y=['iscore', 'iscore_raw', 'rscore'])
    pl.show()

def find_peak_at_each_date(row, df):
    subset = df[df['case_date'] <= row['case_date']]
    return subset['cases'].max()

def cases_to_date(case_date, df_total=None):
    if df_total is None:
        return 0.
    try:
        cases = df_total.loc[df_total['case_date'] <= case_date].iloc[-1]['cases']
    except:
        return 1.
    else:
        return cases

def vax_at_date(case_date, df_vax=None, stage=2):
    if df_vax is None:
       return 0.00001
    try: 
        row = df_vax.loc[df_vax['case_date'] <= case_date].iloc[-1]
    except:
        return 0.00002
    else:
        if stage == 1:
            return row['vax_1']
        elif stage == 2:
            return row['vax_2']
        elif stage == 3:
            return row['vax_booster']
        else:
            return 0.00003
        

def add_calculations_to_time_series(df_all, scores=False, debug=False):
    pd.options.mode.chained_assignment = None  # default='warn'
    locations = sorted(df_all['location'].unique())
    for idx, loc_name in enumerate(locations):
        if debug:
            print(f"\t{loc_name}")
        # Get location metadata
        location = StateRegion.objects.filter(name=loc_name).first()
        if location is None:
            print (f"Cannot find Location {loc_name}")
            continue
        population = location.population
        # Get data for this location
        subset = df_all.loc[df_all['location'] == loc_name]
        # Add peak
        subset['peak'] = subset.apply(lambda row: find_peak_at_each_date(row, subset), axis=1)
        # For the 7-d average add NScore, IScore, Row IScore, RScore, and VScore
        if scores:
            subset['iscore_raw'] = subset.apply(lambda row: calc_raw_iscore(row['cases'], row['peak']), axis=1)
            subset['iscore'] = subset.apply(lambda row: calc_iscore(row['cases'], row['peak']), axis=1)
            subset['rscore'] = subset.apply(lambda row: calc_rscore(row['cases'], row['peak']), axis=1)
            subset['nscore'] = subset.apply(lambda row: calc_nscore(row['iscore'], row['rscore'], row['peak']), axis=1)
            subset['vscore'] = subset.apply(
                lambda row: calc_vscore(
                    cases_to_date(row['case_date'], location.total_cases_dataframe), 
                    population, 
                    vax_at_date(row['case_date'], location.vaccination_dataframe), 
                    row['rscore']
                ), 
                axis=1
            )
        # Create or append to the processed dataframe
        out_df = subset if idx == 0 else pd.concat([out_df, subset])
    return out_df

