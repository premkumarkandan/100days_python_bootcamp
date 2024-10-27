import pandas as pd

poke_df = pd.read_csv('pokemon_data.csv')

poke_df_xlsx = pd.read_excel('pokemon_data.xlsx')
poke_df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

print(poke_df.tail(3))

print(poke_df_xlsx.head(10))

print(poke_df_txt)

# Read Headers
print(poke_df.columns)

# Read each column
print(poke_df[['Type 1', 'HP', 'Name']][0:10])

# Read each row
print(poke_df.head(3))
print(poke_df.iloc[0:5, 1:4])
for index, row in poke_df.iterrows():
    print(index, row[['Name', 'Legendary']])
print(poke_df.loc[poke_df['Legendary'] == False])
# Sort by values
print(poke_df.sort_values(['Type 1', 'Speed'], ascending=[0,1]))
poke_df['Total'] = poke_df.iloc[:, 4:10].sum(axis=1)
cols = list(poke_df.columns)
poke_df = poke_df[cols[0:4] + [cols [-1]] + cols[4:12]]
print(poke_df.head(3))
print(poke_df['Total'])

poke_df.loc[(poke_df['Type 1'] == 'Grass') & (poke_df['Type 2'] == 'Poison') & (poke_df['HP'] > 70)]

# Remove a certain row entry based on a condition using ~
Modified_new = Modified.loc[~poke_df['Name'].str.contains('Mega')]

poke_df.loc[poke_df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]


# To modify contents of a df based on user defined conditions
Modified = poke_df.loc[poke_df['Type 1'] == 'Fire', 'Legendary'] = True
poke_df.loc[poke_df['Total'] > 500, ['Generation', 'Legendary']] = 'Test_Value'

Modified_new.to_csv('Modified.csv', index=False)
Modified.reset_index(drop=True, inplace=True)
print(Modified)

poke_df.to_csv('Modified.csv', index=False, sep='\t')

poke_df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)
poke_df.groupby(['Type 1']).mean().sort_values('HP', ascending=False)

for poke_df in pd.read_csv('modified.csv', chunksize=5)
    print('CHUNK DF')
    print(poke_df)

