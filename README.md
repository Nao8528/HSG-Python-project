# HSG-Python Project on SARS-CoV-2 data

The following project visualizes the past corona data for Switzerland and allows for an up-to-date monitoring of the pandemic 
in this country. This project was written by Yu-Lun ... and Stephanie Frey from the University .... and 
University of St. Gallen and worked fine on PyCharm and ... by December 2020.

The Project includes following elements:
Firstly, the new corona cases are visualized over time in a bar chart. 
The output includes a bar chart of the data for the whole of Switzerland and of data for selected cantons.
Secondly, the new corona cases are visualized on a map of Switzerland.
This map shows the new corona cases over the last day.
Thirdly, the timeseries of the reproduction number of Switzerland is plotted on a line graph with reference to R = 1.
Finally, random forest is used to predict the new corona cases and the quality of the model is visualized on a 
line graph displaying the predicted and actual values.

Information about the data used in this project:
The SARS-CoV-2 data is collected from an open government datasets for SARS-CoV-2 related data reported by the 
Swiss Cantons and the Principality of Liechtenstein. This data is generated and validated daily using manual and 
automated procedures. The data was collected from 26.02.2020 onwards. Note that the data includes only reported 
information by the Swiss Cantons and the Principality of Liechtenstein. Thus, gaps result if Swiss Cantons or the 
Principality of Liechtenstein do not report data for the specific date or report the data later on.
Link to the datasets: https://github.com/openZH/covid_19

Regarding the reproductive number a second data source was used. This data source is updated daily and
provides the reproductive number for Switzerland from 07.02.2020 until about 10 days prior to the present date.
The calculation method for the R number was done by:
Jana S. Huisman (Department of Environmental Systems Science, ETH Zurich and Swiss Institute of Bioinformatics)
Jeremie Scire (Swiss Institute of Bioinformatics and Department of Biosystems Science and Engineering, ETH Zurich)
Daniel Angst (Department of Environmental Systems Science, ETH Zurich)
Richard Nehe (Biozentrum, University of Basel)
Sebastian Bonhoeffer (Department of Environmental Systems Science, ETH Zurich)
Tanja Stadler (Swiss Institute of Bioinformatics and Department of Biosystems Science and Engineering, ETH Zurich)
Link to the dataset: https://github.com/covid-19-Re/dailyRe-Data