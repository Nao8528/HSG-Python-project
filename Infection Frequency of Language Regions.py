# This file visualizes the infection frequency of the three language regions of Switzerland
# These language regions include the german- / italian- and french-speaking part of Switzerland, the Rhaeto-Romanic part of Switzerland
# is not looked at, since the population is small and displaying this fragmented region makes little sense in this context
# This clustering can provide useful information, since these three language regions are three social groups with high
# mobility within the social group and less mobility across the three social groups
# Please note that this visualization displays only the year 2020 in an animated and interactive bar chart over time, year 2021 will not be displayed

# Import all necessary libraries
import numpy as np
import pandas as pd
import plotly.express as px

# Import all corona datasets
AG = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_AG_total.csv")
AI = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_AI_total.csv")
AR = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_AR_total.csv")
BE = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_BE_total.csv")
BL = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_BL_total.csv")
BS = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_BS_total.csv")
FR = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_FR_total.csv")
GE = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_GE_total.csv")
GL = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_GL_total.csv")
GR = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_GR_total.csv")
JU = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_JU_total.csv")
LU = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_LU_total.csv")
NE = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_NE_total.csv")
NW = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_NW_total.csv")
OW = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_OW_total.csv")
SG = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_SG_total.csv")
SH = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_SH_total.csv")
SO = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_SO_total.csv")
SZ = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_SZ_total.csv")
TG = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_TG_total.csv")
TI = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_TI_total.csv")
UR = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_UR_total.csv")
VD = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_VD_total.csv")
VS = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_VS_total.csv")
ZG = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_ZG_total.csv")
ZH = pd.read_csv(
    "https://raw.githubusercontent.com/openZH/covid_19/master/fallzahlen_kanton_total_csv_v2/COVID19_Fallzahlen_Kanton_ZH_total.csv")

# Data processing:
cantons = [GR, BE, AG, AI, AR, BL, BS, FR, GE, GL, JU, LU, NE, NW, OW, SG, SH, SO, SZ, TG, TI, UR, VD, VS, ZG, ZH]
cantons_namelist = ["GR", "BE", "AG", "AI", "AR", "BL", "BS", "FR", "GE", "GL", "JU", "LU", "NE", "NW", "OW", "SG",
                    "SH", "SO", "SZ", "TG", "TI", "UR", "VD", "VS", "ZG", "ZH"]

# Merge all cumulated cases by each canton and calculate new confirmed cases day by day
# First-merge data by "ncumul_conf" and create a dataframe including all the confirmed cases for each canton
for i in range(0, len(cantons)):
    cantons[i].index = cantons[i]["date"]
    Confirmed_cases = pd.DataFrame(np.random.randn(len(GR.index), 1), index=GR.index)

for i in range(0, len(cantons)):
    Confirmed_cases = pd.merge(Confirmed_cases, cantons[i]["ncumul_conf"].to_frame(), on="date", how="left")
    Confirmed_cases.rename(columns={"ncumul_conf": cantons_namelist[i]}, inplace=True)

Confirmed_cases = Confirmed_cases.drop(columns=[0])

# Set the date as index of the dataframe
Confirmed_cases.index = pd.to_datetime(Confirmed_cases.index)

# Use last day's data to fill in NA
Confirmed_cases = Confirmed_cases.fillna(method='ffill')

# Add data of whole Switzerland to the dataframe
Confirmed_cases['Whole Switzerland'] = Confirmed_cases.apply(lambda x: x.sum(), axis=1)

# Second-caculate new confirmed cases day by day
new_confirmed_cases = Confirmed_cases.diff()
new_confirmed_cases=new_confirmed_cases.fillna(0)

# Third get the infection frequency for each language region
# Cluster the data according to the three language regions: German, Italian and French (the roman part is not considered, as it makes up only 0.5% of the Swiss population)
German_cantons = new_confirmed_cases.filter(items=["GR", "BE", "AG", "AI", "AR", "BL", "BS","GL", "JU", "LU","NW",
                                                    "OW", "SG","SH", "SO", "SZ", "TG","UR","ZG", "ZH"])
Italian_cantons = new_confirmed_cases.filter(items=["TI"])
French_cantons = new_confirmed_cases.filter(items=["FR", "GE","NE","VD", "VS"])

# Collect the population size of the different language regions
# The population size accoridng to the Swiss government is 8.6 million and the german-, italian- and french-speaking
# make up 63%, 8% and 23% respectively
Pop_German=8.6*1000000*0.63
Pop_Italian=8.6*1000000*0.08
Pop_French=8.6*1000000*0.23

# Calculate the relative infection frequency of the different language regions per 100'000
German_frequency = German_cantons.sum(axis=1)/Pop_German*100000
Italian_frequency = Italian_cantons.sum(axis=1)/Pop_Italian*100000
French_frequency = French_cantons.sum(axis=1)/Pop_French*100000

# Create a dataframe of all infection frequencies of the different language regions
Infection_frequency_F = pd.DataFrame(French_frequency, columns=["Infection Frequency"])
Infection_frequency_F["Swiss Language Region"] = "french-speaking"
Infection_frequency_F.reset_index(inplace=True)
Infection_frequency_G = pd.DataFrame(German_frequency, columns=["Infection Frequency"])
Infection_frequency_G["Swiss Language Region"]="german-speaking"
Infection_frequency_G.reset_index(inplace=True)
Infection_frequency_I = pd.DataFrame(Italian_frequency, columns=["Infection Frequency"])
Infection_frequency_I["Swiss Language Region"]="italian-speaking"
Infection_frequency_I.reset_index(inplace=True)
Infection_frequency=Infection_frequency_F.append([Infection_frequency_G, Infection_frequency_I])

# Add another column to the dataframe containing the calendar week for animation in bar chart
Infection_frequency["Calendar Week 2020"]=Infection_frequency["date"].dt.isocalendar().week

# Plot an animated and interactive bar chart for the infection rates of the three language regions in 2020
fig=px.bar(Infection_frequency, x="Swiss Language Region", y="Infection Frequency",
           color="Swiss Language Region", color_discrete_sequence=px.colors.qualitative.T10,
           title="Infection Frequency of the Language Regions in Switzerland 2020",
           animation_frame="Calendar Week 2020",
           animation_group="Swiss Language Region",
           range_y=[0,250])
fig.update_layout(showlegend=False)
fig.show()