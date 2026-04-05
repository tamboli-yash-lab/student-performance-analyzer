import pandas as pd

def load_data():
    return pd.read_csv("data.csv")

def calculate_average(df):
    df["Average"] = df[["Maths", "Physics", "Chemistry"]].mean(axis=1)
    return df

def top_students(df):
    return df.sort_values(by="Average", ascending=False).head(3)

def weak_students(df):
    return df[df["Average"] < 60]