from helpers import get_session

import pandas as pd

def get_df_from_sql():
    engine, Session = get_session()
    df = pd.read_sql_query('select * from ratings', con=engine)
    return df

