# LSE_DA_COVID_analysis
Course 2 Assignment 1 LSE_DA_COVID_analysis
Two files were loaded into two Dataframes.

Both files cover the period from 2020-01-22 to 2021-10-14 and are sorted in ascending order by date.
Importing the data and describing it identifies several insights.  

5 columns in each table are the same name and datatype.

Missing Data Check
Vaccinated file, has missing data of the “Missing at random type”  has the value zero in the first two quartiles for ‘Vaccinated’,’First Dose’ and ‘Second Dose’ columns.  This suggests that they did not start recording the data for that period or that data was lost.  There is evidence of this when the data is described and 25% (first quartile) and 50%(second quartile) are set to 0.  Dates that vaccinated started needs to be verified to confirm this.

The cases file also has missing data of the MAR type and has missing values for a two day period 2020-09-21 and 2020-09-22.

Erroneous data:
Vaccinated file the vaccinated column should be the sum of the first and second dose but it is the same as the second dose

More info

What was the first date that data was recorded in the vaccinated file compared to the entire data set, for vaccinated, first dose and second dose
what is the proportion of death to cases in each region? Were some regions affected more badly than others
correlation between cases and non vaccinated?
are deaths higher at the start before people were vaccinated
Are there dates when vaccinations became available in each region?
Find out more about standard deviation and what it tells us.
Format numbers.
