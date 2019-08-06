from helpers import get_session
import numpy as np # is any good data project complete without at least one call to np?
import pandas as pd
from datetime import datetime, timedelta

class Data:
    def __init__(self, locations):
        self.SQL_Query = \
            """
            SELECT * FROM ratings;
            """

        self.df = None
        self.locations = locations
        self.week_dict = {}
        self.days_dict = None

        self.get_df_from_sql()
        self.make_all_weeklys()
        self.make_pie_chart()

    def get_df_from_sql(self):
        engine, Session = get_session()
        df = pd.read_sql_query(self.SQL_Query, con=engine)
        self.df = df

    def weekly_bar_chart(self, sub_df):
        df_week = sub_df[sub_df['date'].dt.date > (datetime.date(datetime.now())
                                                   - timedelta(7))]
        week_1 = df_week[df_week['rating'] == 1].groupby(df_week.date.dt.date).count()['id']
        week_2 = df_week[df_week['rating'] == 2].groupby(df_week.date.dt.date).count()['id']
        week_3 = df_week[df_week['rating'] == 3].groupby(df_week.date.dt.date).count()['id']
        df_week = pd.concat([week_1, week_2, week_3], axis=1, sort=True).fillna(0)
        df_week.columns = ['1', '2', '3']
        df_week['mean'] = ((df_week['1'] * 1 + df_week['2'] * 2 + df_week['3'] * 3)
                          /(df_week['1'] + df_week['2'] + df_week['3']))
        return df_week

    def make_all_weeklys(self):
        self.week_dict = None
        weekly_dict = {'all': self.weekly_bar_chart(self.df)}
        for location in self.locations:
            weekly_dict[location] = self.weekly_bar_chart(self.df[self.df['device'] == location])

        self.week_dict = weekly_dict

    def make_days_pie(self, sub_df):
        data = sub_df[sub_df['date'].dt.date == datetime.date(datetime.now())]
        data = data.groupby('rating').count()
        data = data['id']
        return data

    def make_pie_chart(self):
        days_dict = {'all': self.make_days_pie(self.df)}
        for location in self.locations:
            days_data = self.make_days_pie(self.df[self.df['device'] == location])
            days_dict[location] = days_data
        self.days_dict = days_dict

