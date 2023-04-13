import pandas as pd
import csv
import statistics
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns
import random
import numpy as np

data = pd.read_csv('savings_data.csv')
data_p = data['quant_saved'].to_list()
with open('savings_data.csv','r') as f:
    frame = csv.reader(f)
    data_c = list(frame)

sns.boxplot(data=data,x=data['quant_saved'])#print(f'median: ')
q1 = data['quant_saved'].quantile(0.25)
q3 = data['quant_saved'].quantile(0.75)
iqr = q3 - q1
lower_limit = q1 - 1.5*iqr
upper_limit = q3 + 1.5*iqr

n_df = data[data['quant_saved']<upper_limit]
list_df = n_df['quant_saved'].to_list()
print(f'mean: {statistics.mean(list_df)}')
print(f'median: {statistics.median(list_df)}')
print(f'median: {statistics.mode(list_df)}')
print(f'median: {statistics.stdev(list_df)}')

def randomcount(counter):
    dataset = []
    for i in range(counter):
        inte = random.randint(0,len(list_df)-1)
        dataset.append(inte)
    
    return dataset

temp_list = randomcount(100)
wealth = data['wealthy'].to_list()

print(f'median of sample: {statistics.mean(temp_list)}')
print(f'stdev of sample: {statistics.stdev(temp_list)}')
print(f'median of population: {statistics.mean(data_p)}')

cor = np.corrcoef(data_p,wealth)
def sig():
    if cor[0,1] > 0:
        i = 'significant'
        print('\n wealth and quantity saved are directly related')
    else:
        i = 'insignificant'
        
    return i
print(f'the correlation between wealth and quantity saved is {cor[0,1]} and is {sig()}')
if cor[0,1] // 1 == 0:
    print('wealth and quant saved are not at all related')
else:
    print('wealth and quant saved are inversly related')
