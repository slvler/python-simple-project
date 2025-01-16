import pandas as pd

smps = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_2_(1990%E2%80%9391)")

print(len(smps))
print(smps[1])