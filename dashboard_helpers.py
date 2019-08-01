from helpers import get_session
import numpy as np # is any good data project complete without at least one call to np?
import pandas as pd
from datetime import datetime, timedelta


def get_locations():
    SQL_Query = \
        """
        SELECT DISTINCT device FROM ratings;
        """
    engine, Session = get_session()
    locations = pd.read_sql_query(SQL_Query, con=engine)['device'].tolist()
    return locations


class Data:
    def __init__(self, locations):
        self.SQL_Query = \
            """
            SELECT * FROM ratings;
            """

        self.df = self.get_df_from_sql()
        self.locations = locations
        self.df_week = self.make_all_weeklys()



    def get_df_from_sql(self):
        engine, Session = get_session()
        df = pd.read_sql_query(self.SQL_Query, con=engine)
        print('pulling data')
        return df

    def weekly_bar_chart(self, sub_df):
        df_week = sub_df[sub_df['date'].dt.date > datetime.date(datetime.now())
                                                    - timedelta(7)]
        week_1 = df_week[df_week['rating'] == 1].groupby(df_week.date.dt.date).count()['id']
        week_2 = df_week[df_week['rating'] == 2].groupby(df_week.date.dt.date).count()['id']
        week_3 = df_week[df_week['rating'] == 3].groupby(df_week.date.dt.date).count()['id']
        df_week = pd.concat([week_1, week_2, week_3], axis=1, sort=True).fillna(0)
        df_week.columns = ['1', '2', '3']

        return df_week

    def make_all_weeklys(self):
        weekly_dict = {'all': self.weekly_bar_chart(self.df)}
        for location in self.locations:
            weekly_dict[location] = self.weekly_bar_chart(self.df[self.df['device'] == location])

        return weekly_dict