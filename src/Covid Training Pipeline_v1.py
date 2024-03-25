#!/usr/bin/env python
# coding: utf-8

# ## Covid Training Pipeline_v1
# 
# New notebook

# # **COVID Training Pipeline**
# This Python Pandas ETL pipeline uses the [COVID-19 Dataset](https://www.kaggle.com/datasets/imdevskp/corona-virus-report) by Devakumar K.P. on Kaggle. The raw data source used contains the cumulative count of confirmed, death and recovered cases of COVID-19 from different countries since January 2020.
# 
# ## **Initial Columns**
# The following columns are the original columns of the raw data set.
# + **Province/State** - Province/State of the recorded case(s)
# + **Country/Region** - Country/Region of the recorded case(s)
# + **Lat** - Latitude of the location
# + **Long** - Longitude of the location
# + **Date** - Date of the cumulative report
# + **Confirmed** - Cumulative number of confirmed cases until the given date
# + **Deaths** - Cumulative number of deaths until the given date
# + **Recovered** - Cumulative number of recovered cases until the given date
# + **Active** - Cumulative number of active cases until the given date
# + **WHO Region** - The WHO Region of the recorded case(s)

# ## **Step 1: Load raw data**

# In[2]:


import pandas as pd
# Load data into pandas DataFrame from "../data/" + "covid_19_clean_complete.csv"
dfRaw = pd.read_csv("../data/" + "covid_19_clean_complete.csv")
df = dfRaw.copy()

display(dfRaw[:250])


# ## **Step 2: Drop unused columns and create grain columns**

# In[3]:


# Get columns
columns = df.columns

# Drop unused columns
# if "Lat" in columns:
#     del df["Lat"]

# if "Long" in columns:
#     del df["Long"]

if "Province/State" in columns:
    del df["Province/State"]

# Create WHO Region Code column
def region(data):
    match data:
        case "Eastern Mediterranean":
            return "EMR"
        case "Europe":
            return "EUR"
        case "Africa":
            return "AFR"
        case "Americas":
            return "AMR"
        case "Western Pacific":
            return "WPR"
        case "South-East Asia":
            return "SEAR"

df["WHO Region Code"] = df["WHO Region"].apply(lambda x: region(x))    
df = df.rename(columns={"WHO Region": "WHO Region Name"})

# Create grain columns
if "Year" not in columns:
    df["Year"] = pd.DatetimeIndex(df["Date"]).year
    df["Month"] = pd.DatetimeIndex(df["Date"]).month
    df["Month Name"] = pd.to_datetime(df['Date'], format='ISO8601')
    df["Day of Week"] = pd.DatetimeIndex(df["Date"]).weekday
    df["Day Name"] = pd.DatetimeIndex(df["Date"]).day_name()
    del df["Date"]

df = df.rename(columns={"Country/Region": "Country"})

columns = df.columns
print(list(columns))
display(df)


# ## **Step 3: Transform the rest of the columns**

# In[4]:


# Transform Country column
df["Country"] = df["Country"].str.split(r"\s+(and)", expand=True)[0]
df["Country"] = df["Country"].str.split(r"\s*\(", expand=True)[0]
df["Country"] = df["Country"].apply(lambda x: "United States" if x == "US" else x)
df["Country"] = df["Country"].apply(lambda x: "Cape Verde" if x == "Cabo Verde" else x)
df["Country"] = df["Country"].apply(lambda x: "Ivory Coast" if x == "Cote d'Ivoire" else x)
df["Country"] = df["Country"].str.split(r"\*", expand=True)[0]

# Transform MonthName column
df["Month Name"] = df["Month Name"].dt.month_name()

# Create MonthShortName column from MonthName column
df["Month Short Name"] = df["Month Name"].str.slice(0,3)


# ## **Step 4: Write the cleaned and transformed data into CSV file**
# 
# ### **Final Columns**
# The following columns are the final columns comprising the output data set.
# + **Country** - Country of the recorded case(s)
# + **Lat** - Latitude of the location
#     - *This column is retained only for Power BI Map visualizations.*
# + **Long** - Longitude of the location
#     - *This column is retained only for Power BI Map visualizations.*
# + **Confirmed** - Cumulative number of confirmed cases until the given date
# + **Deaths** - Cumulative number of deaths until the given date
# + **Recovered** - Cumulative number of recovered cases until the given date
# + **Active** - Cumulative number of active cases until the given date
# + **WHO Region** - The WHO Region Code of the recorded case(s)
# + **WHO Region** - The WHO Region Name of the recorded case(s)
# 
# ### **Grain Columns**
# The following columns are implemented to introduce more granularity into the final data set.
# + **Year** - Year of the cumulative report
# + **Month** - Month of the cumulative report
# + **Month Name** - Month name of the cumulative report
# + **Day of Week** - Day of week of the cumulative report
# + **Day Name** - Day name of the cumulative report
# + **Month Short Name** - Short name of the month the cumulative report

# In[5]:


# Write to CSV
df.to_csv("../data/" + "Covid-19 By Country Complete.csv", encoding='utf-8', index=False)

# display(df.loc[:100])
display(df)

