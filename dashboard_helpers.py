from helpers import get_session
import numpy as np # is any good data project complete without at least one call to np?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
sns.set()

SQL_Query = \
"""
SELECT * FROM ratings
"""


def get_df_from_sql():
    engine, Session = get_session()
    df = pd.read_sql_query(SQL_Query, con=engine)
    return df

def weekly_bar_chart(df):
    df_week = df[df['date'].dt.date > datetime.date(datetime.now()) - timedelta(7)]
    week_1 = df_week[df_week['rating'] == 1].groupby(df_week.date.dt.date).count()['id']
    week_2 = df_week[df_week['rating'] == 2].groupby(df_week.date.dt.date).count()['id']
    week_3 = df_week[df_week['rating'] == 3].groupby(df_week.date.dt.date).count()['id']
    df_week = pd.concat([week_1, week_2, week_3], axis=1, sort=True).fillna(0)
    df_week.columns = ['1', '2', '3']

    return df_week