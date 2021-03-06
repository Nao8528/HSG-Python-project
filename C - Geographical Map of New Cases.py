# This file visualizes all new cases cumulative over the past day on a map of Switzerland
# The user is allowed to zoom in and out. In addition the number of new cases will popup as soon as the user clicks on a canton
# This map will be saved in the project as "D - Geographical Map of New Cases.html" and can also be opened using the browser

# Import all necessary libraries
import numpy as np
import pandas as pd
import folium


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

# Data processing - combine whole data from different datasets
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

# Third - add new dataframe including all the canton coordinates, this is needed to visualize the data on the map
# The canton coordinates are made up of latitude and longitude of the capital of each canton
latitude_cantons=[46.84986, 46.94809, 47.39254, 47.33103, 47.38615, 47.48455, 47.55839, 46.80237, 46.20222, 47.04057,
                  47.36493, 47.05048, 46.99179, 46.95805, 46.89611, 47.42391, 47.69732, 47.20791, 47.02076, 47.55776,
                  46.19278, 46.88042, 46.516, 46.23343, 47.17242, 47.36667]
longitude_cantons=[9.53287, 7.44744, 8.04422, 9.40996, 9.27916, 7.73446, 7.57327, 7.15128, 6.14569, 9.06804, 7.34453,
                   8.30635, 6.931, 8.36609, 8.24531, 9.37477, 8.63493, 7.53714, 8.65414, 8.89893, 9.01703, 8.64441,
                   6.63282, 7.34939, 8.51745, 8.556]
coordinates_cantons=pd.DataFrame(index=cantons_namelist)
coordinates_cantons["latitude"]=latitude_cantons
coordinates_cantons["longitude"]=longitude_cantons

# Now the code to visualize the data on a map is added
# The visualization only includes the new corona cases over the last day for each canton (data filtering)
today=new_confirmed_cases.iloc[-1]

# A Map of Switzerland is created
map=folium.Map(location=[46.8131873, 8.22421],
               tiles="cartodbpositron",
               zoom_start=8)

# A titel is added to the map
titel_html="""<h3 align="center" style="font-size:20px"><b>New Corona Cases in Switzerland - Cumulative Over the Last Day</b></h3>"""
map.get_root().html.add_child(folium.Element(titel_html))

# New corona cases over the last day for each canton is added to the map (cantons which had no cases over the last day are excluded)
for i in range(0, len(cantons)):
    if today[i] != 0:
        folium.CircleMarker(location=[coordinates_cantons.iloc[i]["latitude"], coordinates_cantons.iloc[i]["longitude"]],
                            radius=(today.iloc[i]/20),
                            popup=today.index[i]+": " +str(today[i]),
                            color="#cc4131",
                            fill=True,
                            fill_color="#cc4131").add_to(map)

# The Map is saved in the project as a html file named "Geographical Map of New Cases.html" (it can be opened in the Browser when using PyCharm)
map.save("D - Geographical Map of New Cases.html")
map