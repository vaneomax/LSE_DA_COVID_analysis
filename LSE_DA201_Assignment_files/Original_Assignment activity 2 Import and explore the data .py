#!/usr/bin/env python
# coding: utf-8

# # Import data sets & validate them

# In[2]:


#import Pandas package
import pandas as pd


# In[ ]:


#method to format numbers
def my_value(number):
    return ("{:,}".format(number))
print(my_value(100000000)


# In[11]:


#load date sets into dataframes
vac_original = pd.read_csv('covid_19_uk_vaccinated.csv')
cases_original = pd.read_csv('covid_19_uk_cases.csv')


# In[12]:


#create a copy of vaccinated and validate
vac = vac_original.copy()

#determine no of rows and columns
print('Vaccinated:',vac.shape)
print(vac.dtypes)


# In[13]:


#create a copy of cases and validate
cases = cases_original.copy()

print('Cases:', cases.shape)
print(cases.dtypes)


# In[14]:


#check missing data for vaccinated
print (vac.isnull().sum())


# In[15]:


#check missing data for cases
cases.isnull().sum()


# In[37]:


#view the first 5 rows
vac.head()


# In[38]:


#view the last 5 rows
vac.tail()


# In[39]:


#view the first 5 rows
cases.head()


# In[40]:


#view the last 5 rows
cases.tail()


# In[16]:


#Describe the data of the cases DataFrame
cases.describe()


# In[17]:


#Describe the data of the vaccinated DataFrame
vac.describe()


# In[24]:


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

# In[18]:


#view missing data
null_data = cases[cases.isnull().any(axis=1)]
null_data


# In[19]:


#copy the DataFrame
#replace missing data with first data that has a value before the missing data

cases_copy = pd.DataFrame(cases)
cases_copy.head()


#replace the missing data in each of the columns with the last valid observation

cases_copy['Deaths'].fillna(method = 'ffill', inplace = True)
cases_copy['Cases'].fillna(method = 'ffill', inplace = True)
cases_copy['Recovered'].fillna(method = 'ffill', inplace = True)
cases_copy['Hospitalised'].fillna(method = 'ffill', inplace = True)

#check that the missing data has been replaced
cases_copy.isnull().sum()


# # Potential Erroneous Data

# For the vaccinated column has the same values as the second dose column where it should contain the sum of the first and second dose column.

# In[23]:


#add first dose and second dose and insert the sum into the vaccinated column
sum_column = vac['First Dose'] + vac['Second Dose']
vac['Vaccinated'] = sum_column
 #Why Norah

vac.describe()


# # Filtering for Gibraltar

# vac file: use Province/State column to filter out Gibraltar
# cases file: use Province/State column to filter out Gibraltar
# 

# In[28]:


#filter for Gibraltar - cases
Gilb_cases = cases_copy[cases_copy['Province/State'] == 'Gibraltar']

Gilb_cases.shape


# In[29]:


#filter for Gibraltar - vac file
Gilb_vac = vac[vac['Province/State'] == 'Gibraltar']

print("Gilb_vac.shape")
Gilb_vac


# In[30]:


# print the whole DataFrame
# replace df with the name you have given your DataFrame
pd.set_option("display.max_rows", None)

Gilb_cases


# In[31]:


#generate descriptive statistics
Gilb_cases.describe()


# In[32]:


#generate descriptive statistics
Gilb_vac.describe()


# In[35]:


#Find earlist and latest data to ascertain the timeframe
earliest_date_Gilb = min(Gilb_cases['Date'])
latest_date_Gilb = max(Gilb_cases['Date'])

earliest_date_Gilb_v = min(Gilb_vac['Date'])
latest_date_Gilb_v = max(Gilb_vac['Date'])

print("Earliest Date for Gilbraltar Cases:",earliest_date_Gilb)
print("Latest Date for Gilbraltar Cases:",latest_date_Gilb)
print("Earliest Date for Gilbraltar Vaccinated:",earliest_date_Gilb_v)
print("Latest Date for Gilbraltar Vaccinated:",latest_date_Gilb_v)


# In[166]:


#create a subset of only numerical columns
result = Gilb_cases.select_dtypes(include='number')
result.head()


# In[168]:


#subset the data further to only include columns to be used in mathematical operations
new_result = result.loc[:,'Deaths':'Hospitalised']
new_result.head()


# In[ ]:


while Gilb_vac['Deaths']==0


# In[169]:


#calculate the sume of all the columns
sum_col= new_result.sum(axis=0)
print(sum_col)


# In[61]:


#check missing data in new table
Gilbraltar_cases.isnull().sum()


# # Calculations

# In[36]:


total_vac = Gilb_vac['Vaccinated'].sum()
print ("Total vaccinated in Gibraltar", total_vac)

first_dose = Gilb_vac['First Dose'].sum()
print ("Received first dose", first_dose)

second_dose = Gilb_vac['Second Dose'].sum()
print ("Received second dose", second_dose)

