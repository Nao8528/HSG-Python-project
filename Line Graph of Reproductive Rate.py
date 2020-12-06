# This file visualizes the reproductive rate of Switzerland
# import all necessary libraries
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt


#Import dataset
R_numbers=pd.read_csv("https://raw.githubusercontent.com/covid-19-Re/dailyRe-Data/master/CHE-estimates.csv")

#data processing of R numbers
R_numbers_ch=R_numbers[R_numbers["region"]=="CHE"]
R_numbers_ch=R_numbers_ch[R_numbers_ch["data_type"]=="Confirmed cases"]
R_numbers_ch=R_numbers_ch[R_numbers_ch["estimate_type"]=="Cori_step"]
R_numbers_ch["date"]=pd.to_datetime(R_numbers_ch["date"])
R_numbers_ch.index=R_numbers_ch["date"]

#plot the the reproductive rate and add a horizontal line at 1
plt.subplots(1,1,figsize=(18,6))
plt.plot(R_numbers_ch.index,R_numbers_ch["median_R_mean"],color="blue")
plt.xticks(rotation=45)
plt.title("Reproductive Rate of Switzerland",fontsize=15)
plt.axhline(y=1, color="r", linestyle="-")
plt.grid()
plt.show()