import pandas as pd
import requests
import matplotlib.pyplot as plt
import datetime


url = "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_ZH_total.csv"
r = requests.get(url)
text = r.text
df = pd.read_csv("https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_ZH_total.csv")
pd.set_option("display.max_columns", None)
print(df.tail(3))
print(df["date"])
df.plot(x="date",y="ncumul_conf")
plt.show()