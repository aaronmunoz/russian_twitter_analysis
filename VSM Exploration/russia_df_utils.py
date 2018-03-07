import pandas as pd

cleaned_csv_location = '../cleaned_tweets.csv'

def read_cleaned_df():
    df = pd.read_csv(cleaned_csv_location, index_col='id')
    df = df[~df['processed_text'].isnull()]
    df['created_datetime'] = pd.to_datetime(df['created_datetime'])
    return df

def save_cleaned_df(df):
    df.to_csv(cleaned_csv_location)

def get_data():
    df = read_cleaned_df()
    df = df[~df['processed_text'].isnull()]
    df['created_datetime'] = pd.to_datetime(df['created_datetime'])
    return df
    
def get_uncategorized_df_rows(drop_retweets=False):
    df = read_cleaned_df()
    df = df[(df['@midnight'] == False) & (df['merkel'] == False)]
    if drop_retweets:
        df = df[df['is_rt'] == False]

    return df

def get_uncategorized_RT_df_rows():
    df = read_cleaned_df()
    df = df[(df['@midnight'] == False) & (df['merkel'] == False) & (df['is_rt'] == True)]

    return df