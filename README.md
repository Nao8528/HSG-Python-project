# HSG-Python Project on SARS-CoV-2 Data - by YuLun Chen and Stephanie Frey

The following project visualizes the past corona data for Switzerland and allows for an up-to-date monitoring of the pandemic. 
Data is updated regularly and the code is written to capture new data points.
This project was written by YuLun Chen (National ChengChi University in Taipei, exchange student at the University of St. Gallen) 
and Stephanie Frey (University of St. Gallen). This project worked fine in PyCharm by 17. December 2020.
There is no specific sequence for running this project, files can be run separately and will work independently.

The Project includes the following elements:
A. A file including the data processing of the corona data for each canton. At the end a summary of the data is printed
B. Bar chart of cumulative new Covid-19 cases over time. User can choose which canton to display and also view the whole of Switzerland
C. Map of Switzerland visualizing the number of new Covid-19 infections over the past day for each Swiss canton. This graph is saved in the project and can also be visualize using the Browser (helpful when using PyCharm)
D. HTML File of the code in C. - can be opened using the browser and can serve as comparison to last day (in that case, must be saved before running the program)
E. Interactive animation of the infection frequency per 100'000 (cumulative over one calendar week) of the three main language clusters in Switzerland: french-, german-, and italian-speaking regions
F. Line graph displaying the timeseries of the reproduction number (R) for Switzerland, with reference to R = 1
G. Using random forest, new Covid-19 infections are predicted and compared with actual values in a line graph

Information about the data used in this project:
The SARS-CoV-2 data is collected from an open government datasets for SARS-CoV-2 related data reported by the Swiss Cantons and the Principality of Liechtenstein.
This data is generated and validated daily using manual and automated procedures. The data was collected from 26.02.2020 onwards.
Note that the data includes only reported information by the Swiss Cantons and the Principality of Liechtenstein. Thus, gaps result if Swiss Cantons or the 
Principality of Liechtenstein do not report data for the specific date or report the data later on.
Link to the datasets: https://github.com/openZH/covid_19

Regarding the reproduction number a second data source was used. This data source is updated daily and provides the reproductive number for Switzerland 
from 07.02.2020 until about 10 days prior to the present date.
The calculation method for the R number was done by:
Jana S. Huisman (Department of Environmental Systems Science, ETH Zurich and Swiss Institute of Bioinformatics)
Jeremie Scire (Swiss Institute of Bioinformatics and Department of Biosystems Science and Engineering, ETH Zurich)
Daniel Angst (Department of Environmental Systems Science, ETH Zurich)
Richard Nehe (Biozentrum, University of Basel)
Sebastian Bonhoeffer (Department of Environmental Systems Science, ETH Zurich)
Tanja Stadler (Swiss Institute of Bioinformatics and Department of Biosystems Science and Engineering, ETH Zurich)
Link to the dataset: https://github.com/covid-19-Re/dailyRe-Data