#!/usr/bin/env python
# coding: utf-8

# # Import data sets & validate them

# In[38]:


#import Pandas package
import pandas as pd


# In[39]:


#load date sets into dataframes
vac_original = pd.read_csv('covid_19_uk_vaccinated.csv')
cases_original = pd.read_csv('covid_19_uk_cases.csv')


# In[40]:


#create a copy of vaccinated and validate
vac = vac_original.copy()

#determine no of rows and columns
print('Vaccinated:',vac.shape)
print(vac.dtypes)


# In[41]:


#create a copy of cases and validate
cases = cases_original.copy()

print('Cases:', cases.shape)
print(cases.dtypes)


# In[42]:


#check missing data for vaccinated
print (vac.isnull().sum())


# In[43]:


#check missing data for cases
cases.isnull().sum()


# In[44]:


#view the first 5 rows
vac.head()


# In[45]:


#view the last 5 rows
vac.tail()


# In[46]:


#view the first 5 rows
cases.head()


# In[47]:


#view the last 5 rows
cases.tail()


# In[48]:


#Describe the data of the cases DataFrame
cases.describe()


# In[49]:


#Describe the data of the vaccinated DataFrame
vac.describe()


# In[50]:


#Find earlist and latest data to ascertain the timeframe
earliest_date = min(vac['Date'])
latest_date = max(vac['Date'])
print(earliest_date)
print(latest_date)


# # Missing Data

# The two files were checked for missing data.
# The vaccinated file had no data recorded for Vaccinated, First Dose and Second Dose for the first two quartiles
# 
# Cases did have data missing for two rows and would be categoriest as (MAR) missing at random data because all the data that is missing is over a two day period.
# Given that we expect some patterns in the data the ffil method was used to fill the missing data. It is unlikely that a there will be a high number of deaths one day and zero the next (should find a simpler way of writing that)
# 

# In[51]:


#view missing data
null_data = cases[cases.isnull().any(axis=1)]
null_data


# In[52]:



#replace the missing data in each of the columns with the last valid observation
cases['Deaths'].fillna(method = 'ffill', inplace = True)
cases['Cases'].fillna(method = 'ffill', inplace = True)
cases['Recovered'].fillna(method = 'ffill', inplace = True)
cases['Hospitalised'].fillna(method = 'ffill', inplace = True)

#check that the missing data has been replaced
cases.isnull().sum()


# # Potential Erroneous Data

# For the vaccinated column has the same values as the second dose column where it should contain the sum of the first and second dose column.

# In[53]:


#add first dose and second dose and insert the sum into the vaccinated column
sum_column = vac['First Dose'] + vac['Second Dose']
vac['Vaccinated'] = sum_column
 #Why Norah

vac.describe()


# # Filtering for Gibraltar

# vac file: use Province/State column to filter out Gibraltar
# cases file: use Province/State column to filter out Gibraltar
# 

# In[54]:


#filter for Gibraltar - cases
Gilb_cases = cases[cases['Province/State'] == 'Gibraltar']

Gilb_cases.shape


# In[55]:


#filter for Gibraltar - vac file
Gilb_vac = vac[vac['Province/State'] == 'Gibraltar']

print("Gilb_vac.shape")
Gilb_vac


# In[56]:


# print the whole DataFrame
# replace df with the name you have given your DataFrame
pd.set_option("display.max_rows", None)

Gilb_cases


# In[57]:


#generate descriptive statistics
Gilb_cases.describe()


# In[58]:


#generate descriptive statistics
Gilb_vac.describe()


# In[59]:


#Find earlist and latest data to ascertain the timeframe
earliest_date_Gilb = min(Gilb_cases['Date'])
latest_date_Gilb = max(Gilb_cases['Date'])

earliest_date_Gilb_v = min(Gilb_vac['Date'])
latest_date_Gilb_v = max(Gilb_vac['Date'])

print("Earliest Date for Gilbraltar Cases:",earliest_date_Gilb)
print("Latest Date for Gilbraltar Cases:",latest_date_Gilb)
print("Earliest Date for Gilbraltar Vaccinated:",earliest_date_Gilb_v)
print("Latest Date for Gilbraltar Vaccinated:",latest_date_Gilb_v)


# In[60]:


#create a subset of only numerical columns
result = Gilb_cases.select_dtypes(include='number')
result.head()


# In[61]:


#subset the data further to only include columns to be used in mathematical operations
new_result = result.loc[:,'Deaths':'Hospitalised']
new_result.head()


# In[62]:


#calculate the sume of all the columns
sum_col= new_result.sum(axis=0)
print(sum_col)


# In[63]:


#check missing data in new table
Gilb_cases.isnull().sum()


# # Calculations

# In[64]:


total_vac = Gilb_vac['Vaccinated'].sum()
print ("Total vaccinated in Gibraltar", total_vac)

first_dose = Gilb_vac['First Dose'].sum()
print ("Received first dose", first_dose)

second_dose = Gilb_vac['Second Dose'].sum()
print ("Received second dose", second_dose)


# # Merge & Analyse Data

# Summary
# Recall the work you are doing for the UK government for your final assignment. Review the requirements introduced in: Assignment: Data Analytics using Python. To help increase the number of second dose vaccinations, the government wants to test a new marketing campaign. They want guidance on which area they should target to test the new campaign to help increase the number of second dose vaccinations. Since the campaign is aimed at increasing the number of second dose vaccinations, they want to test the campaign in the area that has the highest number of people who have received a first dose but no second dose. Where should they target?

# # Observations

# Decribing the merge files and the two individual files:
# - the common columns are the same and values don't change after the merge
# 
# Steps taken to ensure that merge by index works well.
# 1. verified that data in both dataframes is sorted by date
# 2. Compare heads to ensure that dates correspond
# 3. Compare tails to ensure that dates correspond
# 4. Checked dataframe descriptions before and after merge to make sure they remain accurate
# 

# # Data Observations
# 
# 1. In some cases there are more people that have a second dose which indicates that the data is not accurate

# # 3.2 Merge the dataframes

# In[65]:


#import numpy package
import numpy as np


# In[66]:


#merge the two dataframes
#use the difference function to remove duplicated columns


#find columns that are not present in the vac
unique_cols = vac.columns.difference(cases.columns)

print(unique_cols)
new_vac = vac[unique_cols]

#merge the dataframes
cases_vac_merge = pd.merge(cases, new_vac, left_index=True,
                     right_index=True, how='left')

cases_vac_merge.head()


# In[67]:


#view description of the new dataframe
cases_vac_merge.describe()


# In[68]:


#check the shape of the dataframe (rows and columns)
cases_vac_merge.shape


# In[69]:


#view original dataframes to double check against the merged dataframe
cases.describe()


# In[70]:


#view original dataframes to double check against the merged dataframe
vac.describe()


# In[71]:


# Check datatypes
cases_vac_merge.dtypes


# ##### 2c Convert the data type of the Date column from object to DateTime

# In[77]:


#convert date from object to Datetime
cases_vac_merge['Date'] = pd.to_datetime(cases_vac_merge['Date'])

#check datatypes
cases_vac_merge.dtypes


# #### 2d drop unnecessary columns
# All duplicate columns were dropped in previous steps

# #### 3 Determine cases in the UK

# In[95]:


#extract month and year from the data
cases_vac_merge['Year'] = pd.DatetimeIndex(cases_vac_merge['Date']).year
cases_vac_merge['Month'] = pd.DatetimeIndex(cases_vac_merge['Date']).month
cases_vac_merge['Diff between Doses'] = cases_vac_merge['First Dose'] - cases_vac_merge['Second Dose']
cases_vac_merge.head()


# In[ ]:





# In[133]:


#Group by Month and Yar
by_year = cases_vac_merge.groupby(['Year','Month'])['Vaccinated','First Dose','Second Dose','Diff between Doses','Cases'].sum()
by_year.head(20)


# In[135]:


#divide by 100 to make the table easier to read and make deductions
value=100
by_year=(by_year/value).round(2)
by_year.tail(10)


# #### Min and Max by Province

# In[155]:


#by_province = cases_vac_merge.groupby('Province/State')
by_province = cases_vac_merge.groupby(['Province/State'])['First Dose','Second Dose','Cases'].agg([max,min]).reset_index()


by_province.sort_values(by=[('First Dose', 'max'),('Second Dose', 'max'),('Cases', 'max')], ascending=False).reset_index().head(10)


# In[162]:


#calculate % between two columns
print(by_province_perc)
by_province_perc['Perc Second Dose'] = ((by_province['Second Dose','max']/by_province['First Dose','max'])/100).round(2)


# ### Some Tips

# apply() can be used to sum up columns and I think rows
# 
# #Let's call this "custom_sum" as "sum" is a built-in function
# def custom_sum(row):
#     return row.sum()
# df['D'] = df.apply(custom_sum, axis=1)
# 
# A new column D is added and the sums are added in the new columns
# 
# 
# ------
# CHANGE the DATA TYPE in one line
# # Employ the applymap function to specified columns.
# drinks_new = drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float)
