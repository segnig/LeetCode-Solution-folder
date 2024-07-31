import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df3 = employees.head(3)
    return df3