pip install requests
pip install lxml
pip install bs4

# Import required modules
import requests
import bs4
import pandas as pd
 
 
 
# Make requests from webpage
url = 'https://www.worldometers.info/coronavirus/country/india/'
result = requests.get(url)
 
 
 
# Creating soup object
soup = bs4.BeautifulSoup(result.text,'lxml')
 
 
 
# Searching div tags having maincounter-number class
cases = soup.find_all('div' ,class_= 'maincounter-number')
 
 
 
# List to store number of cases
data = []
 
# Find the span and get data from it
for i in cases:
    span = i.find('span')
    data.append(span.string)
 
# Display number of cases 
print(data)
 
 
   
# Creating dataframe
df = pd.DataFrame({"CoronaData": data})
 
# Naming the columns
df.index = ['TotalCases', ' Deaths', 'Recovered']
 
 
 
# Exporting data into Excel
df.to_csv('Corona_Data.csv')
