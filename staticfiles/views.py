
from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.core.files.images import ImageFile
from django.conf import settings
import os 
import glob
import seaborn as sns
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyspark.ml.regression import LinearRegression
import requests
from sklearn import metrics
from bs4 import BeautifulSoup


# Create your views here.


def data(request):
    COVID_DATA = pd.read_csv(
        'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/DMV10043.csv'
        )
    PM25_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_pm25.csv',
    )
    PM25_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_pm25.csv',
    )
    PM25_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_pm25.csv',
    )
    PM25_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_pm25.csv',
    )
    PM25_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_pm25.csv',
    )
    PM25_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_pm25.csv',
    )
    DC_PM25_Concentrations = PM25_2015.append(PM25_2016).append(PM25_2017).append(PM25_2018).append(PM25_2019).append(PM25_2020)
    DC_PM25_Concentrations = DC_PM25_Concentrations.dropna()
    DC_PM25_Concentrations = DC_PM25_Concentrations.rename(columns={"Daily Mean PM2.5 Concentration":"Daily_Mean_PM25_Concentration"})
    PM10_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_pm10.csv',
    )
    PM10_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_pm10.csv',
    )
    PM10_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_pm10.csv',
    )
    PM10_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_pm10.csv',
    )
    PM10_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_pm10.csv',
    )
    PM10_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_pm10.csv',
    )
    DC_PM10_Concentrations = PM10_2015.append(PM10_2016).append(PM10_2017).append(PM10_2018).append(PM10_2019).append(PM10_2020)
    SO2_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_so2.csv',
    )
    SO2_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_so2.csv',
    )
    SO2_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_so2.csv',
    )
    SO2_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_so2.csv',
    )
    SO2_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_so2.csv',
    )
    SO2_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_so2.csv',
    )
    DC_SO2_Concentrations = SO2_2015.append(SO2_2016).append(SO2_2017).append(SO2_2018).append(SO2_2019).append(SO2_2020)
    NO2_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_no2.csv',
    )
    NO2_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_no2.csv',
    )
    NO2_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_no2.csv',
    )
    NO2_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_no2.csv',
    )
    NO2_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_no2.csv',
    )
    NO2_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_no2.csv',
    )
    DC_NO2_Concentrations = NO2_2015.append(NO2_2016).append(NO2_2017).append(NO2_2018).append(NO2_2019).append(NO2_2020)
    CO_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_co.csv',
    )
    CO_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_co.csv',
    )
    CO_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_co.csv',
    )
    CO_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_co.csv',
    )
    CO_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_co.csv',
    )
    CO_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_co.csv',
    )
    DC_CO_Concentrations = CO_2015.append(CO_2016).append(CO_2017).append(CO_2018).append(CO_2019).append(CO_2020)
    

    context = {"DC_PM25_Concentrations": DC_PM25_Concentrations.to_html, "DC_PM10_Concentrations": DC_PM10_Concentrations.to_html, 
    "DC_SO2_Concentrations": DC_SO2_Concentrations.to_html, "DC_NO2_Concentrations": DC_NO2_Concentrations.to_html, 
    "DC_CO_Concentrations":DC_CO_Concentrations.to_html, "COVID_DATA": COVID_DATA.to_html}
    return render(request, 'analyzer/data.html', context)

def home(request):
    

    return render(request, 'analyzer/home.html')

def eda(request):
    COVID_DATA = pd.read_csv(
        'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/DMV10043.csv'
        )
    PM25_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_pm25.csv',
    )
    PM25_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_pm25.csv',
    )
    PM25_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_pm25.csv',
    )
    PM25_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_pm25.csv',
    )
    PM25_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_pm25.csv',
    )
    PM25_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_pm25.csv',
    )
    DC_PM25_Concentrations = PM25_2015.append(PM25_2016).append(PM25_2017).append(PM25_2018).append(PM25_2019).append(PM25_2020)
    DC_PM25_Concentrations = DC_PM25_Concentrations.dropna()
    DC_PM25_Concentrations = DC_PM25_Concentrations.rename(columns={"Daily Mean PM2.5 Concentration":"Daily_Mean_PM25_Concentration"})
    PM10_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_pm10.csv',
    )
    PM10_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_pm10.csv',
    )
    PM10_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_pm10.csv',
    )
    PM10_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_pm10.csv',
    )
    PM10_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_pm10.csv',
    )
    PM10_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_pm10.csv',
    )
    DC_PM10_Concentrations = PM10_2015.append(PM10_2016).append(PM10_2017).append(PM10_2018).append(PM10_2019).append(PM10_2020)
    SO2_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_so2.csv',
    )
    SO2_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_so2.csv',
    )
    SO2_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_so2.csv',
    )
    SO2_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_so2.csv',
    )
    SO2_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_so2.csv',
    )
    SO2_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_so2.csv',
    )
    DC_SO2_Concentrations = SO2_2015.append(SO2_2016).append(SO2_2017).append(SO2_2018).append(SO2_2019).append(SO2_2020)
    NO2_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_no2.csv',
    )
    NO2_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_no2.csv',
    )
    NO2_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_no2.csv',
    )
    NO2_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_no2.csv',
    )
    NO2_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_no2.csv',
    )
    NO2_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_no2.csv',
    )
    DC_NO2_Concentrations = NO2_2015.append(NO2_2016).append(NO2_2017).append(NO2_2018).append(NO2_2019).append(NO2_2020)
    CO_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_co.csv',
    )
    CO_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_co.csv',
    )
    CO_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_co.csv',
    )
    CO_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_co.csv',
    )
    CO_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_co.csv',
    )
    CO_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_co.csv',
    )
    DC_CO_Concentrations = CO_2015.append(CO_2016).append(CO_2017).append(CO_2018).append(CO_2019).append(CO_2020)
    
    x_data = COVID_DATA[[' Ozone_ Contn', ' NO2_Contn', ' CO_ Concn', 'Temp_ Avg ', 'SO2 _Contn',
        ' PM2.5_Contn', 'deathIncrease']].astype(int)
    #Source for saving figures in Django: https://stackoverflow.com/questions/46203051/django-save-image-in-folder

    x_data.plot.area()                               # Partial View of all the  Concentrationd/month 
    plt.xlabel("Monthly Period ")
    plt.ylabel("Ozone,NO2,CO,SO2,Temp_ Avg,and PM2.5,CvdDz")
    plt.title ("Concentrations of Gaseous Elements and Covid_Death")
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/COVID1.png'))
    plt.close()


    alldata = x_data.describe()
    corr=alldata.corr()
    sns.heatmap(corr,annot=True,cmap="RdYlGn") 
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/COVIDHEAT.png'))
    plt.close()


    #EDA of PM25 v PM10
    plt.scatter(DC_PM25_Concentrations['Daily_Mean_PM25_Concentration'][:2000], DC_PM10_Concentrations['Daily Mean PM10 Concentration'][:2000], c="green");
    plt.title("Compared Concentrations of PM2.5 and PM10 | 2015-2020");
    plt.ylabel("Daily Mean PM10 Concentration ");
    plt.xlabel("Daily Mean PM2.5 Concentration");
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/pm25vpm10.png'))
    plt.close()


    #EDA of PM25 v SO2
    plt.scatter(DC_PM25_Concentrations['Daily_Mean_PM25_Concentration'][:3000], DC_SO2_Concentrations['Daily Max 1-hour SO2 Concentration'][:3000], c="navy");
    plt.title("Compared Concentrations of PM2.5 and SO2 | 2015-2020");
    plt.ylabel("Daily Max 1-Hour Mean SO2 Concentration ");
    plt.xlabel("Daily Mean PM2.5 Concentration");
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/pm25vSO2.png'))
    plt.close()



    #EDA of PM25 v NO2
    plt.scatter(DC_PM25_Concentrations['Daily_Mean_PM25_Concentration'][:8000], DC_NO2_Concentrations['Daily Max 1-hour NO2 Concentration'][:8000], c="purple");
    plt.title("Compared Concentrations of PM2.5 and NO2 | 2015-2020");
    plt.ylabel("Daily Max 1-Hour Mean NO2 Concentration ");
    plt.xlabel("Daily Mean PM2.5 Concentration");
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/pm25vNO2.png'))
    plt.close()


    #EDA of PM25 v CO
    plt.scatter(DC_PM25_Concentrations['Daily_Mean_PM25_Concentration'][:3000], DC_CO_Concentrations['Daily Max 8-hour CO Concentration'][:3000], c="orange");
    plt.title("Compared Concentrations of PM2.5 and CO | 2015-2020");
    plt.ylabel("Daily Max-8-Hour Mean CO Concentration ");
    plt.xlabel("Daily Mean PM2.5 Concentration");
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/pm25vCO.png'))
    plt.close()

    #Pearson's R Test:
    sns.heatmap(np.corrcoef(DC_PM25_Concentrations['Daily_Mean_PM25_Concentration'][:3000], DC_CO_Concentrations['Daily Max 8-hour CO Concentration'][:3000]))
    np.corrcoef(DC_PM25_Concentrations['Daily_Mean_PM25_Concentration'][:3000], DC_CO_Concentrations['Daily Max 8-hour CO Concentration'][:3000])
    plt.title("Correlation Matrix of PM2.5 and Confounding Pollutants")
    plt.xticks([1.5,0.5],["PM2.5", "Confounding Pollutants"])
    plt.yticks([1.5,0.5],["PM2.5", "Confounding Pollutants"])
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/pm25heat.png'))
    plt.close()


    
    #Assistance was procured from the following source: https://deallen7.medium.com/managing-date-datetime-and-timestamp-in-python-pandas-cc9d285302ab

    # Compile the PM2.5 Concentrations Date-Wise:
    DC_PM25_Concentrations['Year'] = pd.DatetimeIndex(DC_PM25_Concentrations['Date']).year
    DC_PM25_Concentrations['Month'] = pd.DatetimeIndex(DC_PM25_Concentrations['Date']).month
    DC_PM25_Concentrations['DATE'] = pd.to_datetime(DC_PM25_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_PM25_2015to2020 = pd.pivot_table(DC_PM25_Concentrations, values = 'Daily_Mean_PM25_Concentration', index = 'DATE', aggfunc = np.mean) 
    plt.plot(DC_PM25_2015to2020)


    # Compile the SO2 Concentrations Date-Wise:
    DC_SO2_Concentrations['Year'] = pd.DatetimeIndex(DC_SO2_Concentrations['Date']).year
    DC_SO2_Concentrations['Month'] = pd.DatetimeIndex(DC_SO2_Concentrations['Date']).month
    DC_SO2_Concentrations['DATE'] = pd.to_datetime(DC_SO2_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_SO2_2015to2020 = pd.pivot_table(DC_SO2_Concentrations, values = 'Daily Max 1-hour SO2 Concentration', index = 'DATE', aggfunc = np.mean) 
    plt.plot(DC_SO2_2015to2020)

    # Compile the NO2 Concentrations Date-Wise:
    DC_NO2_Concentrations['Year'] = pd.DatetimeIndex(DC_NO2_Concentrations['Date']).year
    DC_NO2_Concentrations['Month'] = pd.DatetimeIndex(DC_NO2_Concentrations['Date']).month
    DC_NO2_Concentrations['DATE'] = pd.to_datetime(DC_NO2_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_NO2_2015to2020 = pd.pivot_table(DC_NO2_Concentrations, values = 'Daily Max 1-hour NO2 Concentration', index = 'DATE', aggfunc = np.mean) 
    plt.plot(DC_NO2_2015to2020)


    # Compile the PM10 Concentrations Date-Wise:
    DC_PM10_Concentrations['Year'] = pd.DatetimeIndex(DC_PM10_Concentrations['Date']).year
    DC_PM10_Concentrations['Month'] = pd.DatetimeIndex(DC_PM10_Concentrations['Date']).month
    DC_PM10_Concentrations['DATE'] = pd.to_datetime(DC_PM10_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_PM10_2015to2020 = pd.pivot_table(DC_PM10_Concentrations, values = 'Daily Mean PM10 Concentration', index = 'DATE', aggfunc = np.mean) 
    plt.plot(DC_PM10_2015to2020)


    # Compile the CO Concentrations Date-Wise:
    DC_CO_Concentrations['Year'] = pd.DatetimeIndex(DC_CO_Concentrations['Date']).year
    DC_CO_Concentrations['Month'] = pd.DatetimeIndex(DC_CO_Concentrations['Date']).month
    DC_CO_Concentrations['DATE'] = pd.to_datetime(DC_CO_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_CO_2015to2020 = pd.pivot_table(DC_CO_Concentrations, values = 'Daily Max 8-hour CO Concentration', index = 'DATE', aggfunc = np.mean) 
    plt.plot(DC_CO_2015to2020);

    # #Compile PM2.5 AQI Concentrations Date-Wise: 
    DC_PM25_AQI_2015to2020 = pd.pivot_table(DC_PM25_Concentrations, values = 'DAILY_AQI_VALUE', index = 'DATE', aggfunc = np.mean) 
    plt.plot(DC_PM25_AQI_2015to2020)

    # Modify the plots with essentials:
    plt.legend(["PM2.5", "SO2", "NO2", "PM10", "CO", "AQI"], bbox_to_anchor=(0.9, 0.6))
    plt.title("Concentrations of Pollutants within the Washington, DC, Area")
    plt.xlabel("Years")
    plt.ylabel("Relative Pollutant Concentration");
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/pm25overallcomp.png'))
    plt.close()






    context = {"DC_PM25_Concentrations": DC_PM25_Concentrations.to_html, "DC_PM10_Concentrations": DC_PM10_Concentrations.to_html, 
    "DC_SO2_Concentrations": DC_SO2_Concentrations.to_html, "DC_NO2_Concentrations": DC_NO2_Concentrations.to_html, 
    "DC_CO_Concentrations":DC_CO_Concentrations.to_html}
    return render(request, 'analyzer/eda.html', context)  


def regression(request):
    COVID_DATA = pd.read_csv(
        'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/DMV10043.csv'
        )
    PM25_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_pm25.csv',
    )
    PM25_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_pm25.csv',
    )
    PM25_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_pm25.csv',
    )
    PM25_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_pm25.csv',
    )
    PM25_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_pm25.csv',
    )
    PM25_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_pm25.csv',
    )
    DC_PM25_Concentrations = PM25_2015.append(PM25_2016).append(PM25_2017).append(PM25_2018).append(PM25_2019).append(PM25_2020)
    DC_PM25_Concentrations = DC_PM25_Concentrations.dropna()
    DC_PM25_Concentrations = DC_PM25_Concentrations.rename(columns={"Daily Mean PM2.5 Concentration":"Daily_Mean_PM25_Concentration"})
    PM10_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_pm10.csv',
    )
    PM10_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_pm10.csv',
    )
    PM10_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_pm10.csv',
    )
    PM10_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_pm10.csv',
    )
    PM10_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_pm10.csv',
    )
    PM10_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_pm10.csv',
    )
    DC_PM10_Concentrations = PM10_2015.append(PM10_2016).append(PM10_2017).append(PM10_2018).append(PM10_2019).append(PM10_2020)
    SO2_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_so2.csv',
    )
    SO2_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_so2.csv',
    )
    SO2_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_so2.csv',
    )
    SO2_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_so2.csv',
    )
    SO2_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_so2.csv',
    )
    SO2_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_so2.csv',
    )
    DC_SO2_Concentrations = SO2_2015.append(SO2_2016).append(SO2_2017).append(SO2_2018).append(SO2_2019).append(SO2_2020)
    NO2_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_no2.csv',
    )
    NO2_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_no2.csv',
    )
    NO2_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_no2.csv',
    )
    NO2_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_no2.csv',
    )
    NO2_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_no2.csv',
    )
    NO2_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_no2.csv',
    )
    DC_NO2_Concentrations = NO2_2015.append(NO2_2016).append(NO2_2017).append(NO2_2018).append(NO2_2019).append(NO2_2020)
    CO_2015 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2015_data_DC_co.csv',
    )
    CO_2016 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2016_data_DC_co.csv',
    )
    CO_2017 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2017_data_DC_co.csv',
    )
    CO_2018 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2018_data_DC_co.csv',
    )
    CO_2019 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2019_data_DC_co.csv',
    )
    CO_2020 = pd.read_csv(
    'https://raw.githubusercontent.com/darbyna/DATA606_Capstone/main/606_2020_data_DC_co.csv',
    )
    DC_CO_Concentrations = CO_2015.append(CO_2016).append(CO_2017).append(CO_2018).append(CO_2019).append(CO_2020)


    
    #Assistance was procured from the following source: https://deallen7.medium.com/managing-date-datetime-and-timestamp-in-python-pandas-cc9d285302ab
    COVID_DATA = COVID_DATA.reindex(columns=[' NO2_Contn','CO_ Concn','Temp_ Avg ', 'SO2 _Contn', ' PM2.5_Contn',
        'deathIncrease'])

    sns.pairplot(COVID_DATA,x_vars=[' NO2_Contn','Temp_ Avg ', 'SO2 _Contn', ' PM2.5_Contn'],y_vars ='deathIncrease',size=7,aspect=0.4,kind='reg')
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/COVIDR1.png'))
    plt.close()

    # Compile the PM2.5 Concentrations Date-Wise:
    DC_PM25_Concentrations['Year'] = pd.DatetimeIndex(DC_PM25_Concentrations['Date']).year
    DC_PM25_Concentrations['Month'] = pd.DatetimeIndex(DC_PM25_Concentrations['Date']).month
    DC_PM25_Concentrations['DATE'] = pd.to_datetime(DC_PM25_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_PM25_2015to2020 = pd.pivot_table(DC_PM25_Concentrations, values = 'Daily_Mean_PM25_Concentration', index = 'DATE', aggfunc = np.mean) 


    # Compile the SO2 Concentrations Date-Wise:
    DC_SO2_Concentrations['Year'] = pd.DatetimeIndex(DC_SO2_Concentrations['Date']).year
    DC_SO2_Concentrations['Month'] = pd.DatetimeIndex(DC_SO2_Concentrations['Date']).month
    DC_SO2_Concentrations['DATE'] = pd.to_datetime(DC_SO2_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_SO2_2015to2020 = pd.pivot_table(DC_SO2_Concentrations, values = 'Daily Max 1-hour SO2 Concentration', index = 'DATE', aggfunc = np.mean) 

    # Compile the NO2 Concentrations Date-Wise:
    DC_NO2_Concentrations['Year'] = pd.DatetimeIndex(DC_NO2_Concentrations['Date']).year
    DC_NO2_Concentrations['Month'] = pd.DatetimeIndex(DC_NO2_Concentrations['Date']).month
    DC_NO2_Concentrations['DATE'] = pd.to_datetime(DC_NO2_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_NO2_2015to2020 = pd.pivot_table(DC_NO2_Concentrations, values = 'Daily Max 1-hour NO2 Concentration', index = 'DATE', aggfunc = np.mean) 


    # Compile the PM10 Concentrations Date-Wise:
    DC_PM10_Concentrations['Year'] = pd.DatetimeIndex(DC_PM10_Concentrations['Date']).year
    DC_PM10_Concentrations['Month'] = pd.DatetimeIndex(DC_PM10_Concentrations['Date']).month
    DC_PM10_Concentrations['DATE'] = pd.to_datetime(DC_PM10_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_PM10_2015to2020 = pd.pivot_table(DC_PM10_Concentrations, values = 'Daily Mean PM10 Concentration', index = 'DATE', aggfunc = np.mean) 


    # Compile the CO Concentrations Date-Wise:
    DC_CO_Concentrations['Year'] = pd.DatetimeIndex(DC_CO_Concentrations['Date']).year
    DC_CO_Concentrations['Month'] = pd.DatetimeIndex(DC_CO_Concentrations['Date']).month
    DC_CO_Concentrations['DATE'] = pd.to_datetime(DC_CO_Concentrations[['Year', 'Month']].assign(DAY=1))
    DC_CO_2015to2020 = pd.pivot_table(DC_CO_Concentrations, values = 'Daily Max 8-hour CO Concentration', index = 'DATE', aggfunc = np.mean) 
    

    # #Compile PM2.5 AQI Concentrations Date-Wise: 
    DC_PM25_AQI_2015to2020 = pd.pivot_table(DC_PM25_Concentrations, values = 'DAILY_AQI_VALUE', index = 'DATE', aggfunc = np.mean) 
   
    DC_PM25_2015to2020 = DC_PM25_2015to2020.reset_index()
    PM25_Analyzer = pd.DataFrame(DC_PM10_2015to2020['Daily Mean PM10 Concentration'][:72]).reset_index()
    PM25_Analyzer2 = pd.DataFrame(DC_PM25_2015to2020['Daily_Mean_PM25_Concentration'][:72]).reset_index()
    PM25_Analyzer3 = pd.DataFrame(DC_SO2_2015to2020['Daily Max 1-hour SO2 Concentration'][:72]).reset_index()
    PM25_Analyzer4 =  pd.DataFrame(DC_NO2_2015to2020['Daily Max 1-hour NO2 Concentration'][:72]).reset_index()
    PM25_Analyzer5 = pd.DataFrame(DC_CO_2015to2020['Daily Max 8-hour CO Concentration'][:72]).reset_index()
    PM25_Analyzer6 = pd.DataFrame(DC_PM25_AQI_2015to2020['DAILY_AQI_VALUE'][:72]).reset_index()
    PM25_Analyzer7 = pd.DataFrame(DC_PM25_2015to2020['DATE'][:72]).reset_index()
    PM25_Analyzer['Daily Max 1-hour SO2 Concentration']=  PM25_Analyzer3['Daily Max 1-hour SO2 Concentration']
    PM25_Analyzer['Daily Max 1-hour NO2 Concentration'] =   PM25_Analyzer4['Daily Max 1-hour NO2 Concentration']
    PM25_Analyzer['Daily Max 8-hour CO Concentration'] = PM25_Analyzer5['Daily Max 8-hour CO Concentration']
    PM25_Analyzer['Daily_Mean_PM25_Concentration'] = PM25_Analyzer2['Daily_Mean_PM25_Concentration']
    PM25_Analyzer['DAILY_AQI_VALUE'] = PM25_Analyzer6['DAILY_AQI_VALUE']
    PM25_Analyzer['DATE'] = PM25_Analyzer7['DATE']
    PM25_Analyzer = PM25_Analyzer
    # Construct a model for Ordinary Least Squares:
    # Source: https://datatofish.com/statsmodels-linear-regression/
    def OLSConstructor(data,target, feature):
        import statsmodels.api as sa
        
        # Construct the X and Y variables
        target_y = data[target]
        feature_x = data[feature]
        
        # Develop the constant
        feature_x = sa.add_constant(feature_x)
        
        # Ordinary Least Squares Model
        the_model = sa.OLS(target_y,feature_x).fit()
        
        return the_model,feature_x,target_y
    
    # Create binary month variables for OLS analysis:
    PM25_Analyzer= PM25_Analyzer.set_index('DATE')
    binarized_months = pd.get_dummies(PM25_Analyzer.index.month).rename(columns={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'})

    #Clean the newly modified PM2.5 Analyzer: 
    PM25_Analyzer = PM25_Analyzer.reset_index()
    PM25_Analyzer = pd.concat([PM25_Analyzer, binarized_months], axis=1)

    # Construct training and testing datasets and split them based on time-period: 
    PM25_Training_Set = PM25_Analyzer.loc[PM25_Analyzer['DATE'] < '01/01/2021']
    PM25_Testing_Set = PM25_Analyzer.loc[PM25_Analyzer['DATE'] >= '01/01/2021']

    # Add primary features: 
    values = ['Daily Max 1-hour NO2 Concentration', 'Daily Max 1-hour SO2 Concentration','Daily Max 8-hour CO Concentration','Jan','Feb','Mar','Apr', 'May', 'Jul', 'Aug', 'Nov', 'Dec']

    # Construct the machine learning model based on OLS: 
    THE_MODEL, X_PM25, Y_PM25 = OLSConstructor(PM25_Training_Set, 'Daily_Mean_PM25_Concentration', values)
    print(THE_MODEL.summary())

    # Make Predictions:
    PM25_Predictions = THE_MODEL.predict(X_PM25)
    PM25_Training_Set['Predictions_PM25'] = PM25_Predictions

    #Plot the figure of the Actual vs. Predicted: 
    PM25_predict_fig, PM25_predict_ax = plt.subplots()
    PM25_Training_Set.plot(x='DATE', y='Daily_Mean_PM25_Concentration', ax=PM25_predict_ax, c="blue")
    PM25_Training_Set.plot(x='DATE', y='Predictions_PM25', linestyle='--', ax=PM25_predict_ax, c="gold")
    PM25_predict_ax.legend(['PM2.5 Concentration, ug/m3 LC', 'Model Predictions, PM2.5 Concentration']);
    plt.title("Actual vs Predicted PM2.5 Concentrations in Washington, DC (2015-2021)")
    #Source: https://stackoverflow.com/questions/46203051/django-save-image-in-folder
    plt.savefig(os.path.join(settings.BASE_DIR, 'static/images/pm25regression.png'))
    plt.close()


    # Measure the accuracy of the model: 
    print('Mean Absolute Error:', metrics.mean_absolute_error(PM25_Training_Set['Daily_Mean_PM25_Concentration'], PM25_Predictions))
    print('Mean Squared Error:', metrics.mean_squared_error(PM25_Training_Set['Daily_Mean_PM25_Concentration'], PM25_Predictions))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(PM25_Training_Set['Daily_Mean_PM25_Concentration'], PM25_Predictions)))

    context = {"DC_PM25_Concentrations": DC_PM25_Concentrations.to_html, "DC_PM10_Concentrations": DC_PM10_Concentrations.to_html, 
    "DC_SO2_Concentrations": DC_SO2_Concentrations.to_html, "DC_NO2_Concentrations": DC_NO2_Concentrations.to_html, 
    "DC_CO_Concentrations":DC_CO_Concentrations.to_html, "PM25_Analyzer": PM25_Analyzer.to_html, "COVID_DATA": COVID_DATA.to_html}

    return render(request, 'analyzer/regression.html', context)

def load(request):
    

    return render(request, 'analyzer/load.html')

def index(request):


    return render(request, 'analyzer/index.html')

