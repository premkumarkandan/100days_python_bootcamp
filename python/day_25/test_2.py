# create squirrel count csv
# fur, color, count
# 0, grey, 2473
# 1, red, 392
# 2, black, 103

import pandas as pd
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
key = 'Fur Color'


grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

ndict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
n_df = pd.DataFrame(ndict)
n_df.to_csv('squirrel_count.csv', index = False )
print(n_df)
