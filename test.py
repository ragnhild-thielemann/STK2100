

#%%

import pandas as pd

college = pd.read_csv('College.csv') #Henter ut datasettet
college2 = pd.read_csv('College.csv', index_col=0) #henter bare ut den første kolonnen av datasettet


college3 = college.rename({'Unnamed: 0': 'College'},
axis=1) #Lager en endimensjonal vektor for å lagre verdiene, som vi kaller College
college3 = college3.set_index('College') #lagrer verdiene om universitets navn til senere

college = college3

print(college)









# %%
