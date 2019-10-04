from rating_app.helpers import get_session
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


def calc_color(num):
    if num <=1.5:
        return '#DC143C'
    elif num <= 2.5:
        return '#fde500'
    return '#3CB371'

