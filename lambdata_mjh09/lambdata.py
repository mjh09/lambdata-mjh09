# Checks DataFrame for null values
def null(dataFrame):
    from pandas import isna
    return dataFrame.isna().sum()


# Splits date for a column 
def split_date(dataFrame, column):
    import pandas
    from pandas import to_datetime
    df = dataFrame
    df[f'{column}'] = pandas.to_datetime(
                                         dataFrame[f'{column}'],
                                         infer_datetime_format=True
                                         )
    df[f'{column}_year'] = df[f'{column}'].dt.year
    df[f'{column}_month'] = df[f'{column}'].dt.month
    df[f'{column}_day'] = df[f'{column}'].dt.day
    df = df.drop(columns=f'{column}')
    return df
