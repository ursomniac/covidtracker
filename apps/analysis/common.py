import datetime as dt
import pandas as pd
from ..divoc.models import DIVOCCase7DayAvg as model

def get_df_from_query(location, as_of_date=None):
    qs = model.objects.filter(location=location)
    if as_of_date is not None:
        qs = qs.filter(case_date__lte=as_of_date)
    values = qs.values('location', 'case_date', 'cases')
    df = pd.DataFrame.from_records(values)
    return df

def get_df_for_date(as_of_date):
    t = dt.datetime.strptime(as_of_date, '%Y-%m-%d')
    qs = model.objects.filter(
        case_date__year=t.year,
        case_date__month=t.month,
        case_date__day=t.day
    )
    values = qs.values('location', 'cases')
    df = pd.DataFrame.from_records(values)
    return df

def get_peak(row, df):
    # ERROR: This takes a LOOOOOONG TIME.
    # Why?
    subset = df.copy()[df['location'] == df['location']]
    sample = subset[subset['case_date'] <= row['case_date']]
    return sample['cases'].max()

def get_sample_peak(row, df):
    sample = df[df['case_date'] <= row['case_date']]
    return sample['cases'].max()