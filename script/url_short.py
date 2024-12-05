import pyshorteners


long_url = input("Long Url please: ")

s = pyshorteners.Shortener()
short_url = s.tinyurl.short(long_url)


print(short_url)