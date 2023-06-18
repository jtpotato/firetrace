import pandas as pd

bushfires_df = pd.read_csv('./data/data.csv')

bushfires_df['acq_date'] = pd.to_datetime(bushfires_df['acq_date'])

new_df = pd.DataFrame()

grouped_df = bushfires_df.groupby(pd.Grouper(freq='M', key='acq_date'))

new_df['fires'] = grouped_df['fires'].mean()
new_df['scan'] = grouped_df['scan'].sum()
new_df['max_t'] = grouped_df['max_t'].mean()
new_df['month_sin'] = grouped_df['month_sin'].first()
new_df['month_cos'] = grouped_df['month_cos'].first()
new_df['acq_date'] = grouped_df['acq_date'].first()
new_df['year'] = grouped_df['acq_date'].first().dt.year

new_df.to_csv('./data/monthly.csv')