import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load data of UFO sightings
data_set = pd.read_csv('ufo_sightings.csv')

# location of UFO sightings in the US
location = data_set['Location.State'].value_counts()

# days of the week with the most UFO sightings
days = data_set['Dates.Documented.Day'].value_counts()

# month of the year with the most UFO sightings
month = data_set['Dates.Sighted.Month'].value_counts()

# linear regression of UFO sightings by year
year = data_set['Dates.Sighted.Year'].value_counts()
slope, intercept, r_value, p_value, std_err = stats.linregress(year.index, year.values)

# plot the data of UFO sightings by state with bigger width
plt.figure(figsize=(10, 5))
plt.bar(location.index, location.values, width=0.8)
plt.title('UFO sightings by state')
plt.xlabel('State')
plt.ylabel('Number of sightings')
plt.xticks(rotation=90)

# plot the data of UFO sightings by day
plt.figure(figsize=(10, 5))
plt.bar(days.index, days.values, width=0.8)
plt.title('UFO sightings by day')
plt.xlabel('Day')
plt.ylabel('Number of sightings')
plt.xticks(rotation=90)

filtered_year = year[(year.index >= 1960) & (year.index <= 2023)]

# plot the data of UFO sightings by year with linear regression from 1960 to 2023
plt.figure(figsize=(10, 5))
plt.scatter(filtered_year.index, filtered_year.values, c='b', label='UFO sightings')
plt.plot(filtered_year.index, intercept + slope * filtered_year.index, 'r', label='Fitted line')
plt.title('UFO sightings by year')
plt.xlabel('Year')
plt.ylabel('Number of sightings')
plt.xticks(rotation=90)
plt.legend()

# plot the data of UFO sightings by month
plt.figure(figsize=(10, 5))
plt.bar(month.index, month.values, width=0.8)
plt.title('UFO sightings by month')
plt.xlabel('Month')
plt.ylabel('Number of sightings')
plt.xticks(rotation=90)

#plit the data of UFO sightings by month

plt.tight_layout()
plt.show()

# print the linear regression results
print('slope =', slope)
print('intercept =', intercept)
print('r_value =', r_value)
print('p_value =', p_value)
print('std_err =', std_err)
