import pandas as pd

def find_peak_at_each_date(row, df):
    subset = df[df['date'] <= row['date']]
    return subset['value'].max()

def construct_peak_data():
    x = [
        ['2020-01-01',  5],
        ['2020-01-02',  7],
        ['2020-01-03',  9],
        ['2020-01-04', 11],
        ['2020-01-05', 10],
        ['2020-01-06',  8],
        ['2020-01-07',  6],
        ['2020-01-08',  4],
        ['2020-01-09',  2]
    ]
    df = pd.DataFrame(x, columns=['date', 'value'])
    df['date'] = pd.to_datetime(df['date'])
    df['peak'] = df.apply(lambda row: find_peak_at_each_date(row, df), axis=1)
    return df

def test_get_peak():
    df = construct_peak_data()
    max_value = df['value'].max()
    last_peak = df.iloc[-1]['peak']
    assert last_peak == max_value