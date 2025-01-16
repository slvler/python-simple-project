import pandas as pd

text = pd.read_csv('username.csv')

text.rename(columns={'Username; Identifier;First name;Last name': 'head'}, inplace=True)
print(text)

df = pd.read_csv("username.csv", sep=";")
print(df)