import os 
import sys 
import crontab
import time
import pandas as pd 
 
#import through API 
df = pd.read_json('https://healthdata.gov/resource/gskt-tzcc.json')
df.to_csv('data/covid.csv', index = None)

#get and print cwd
cwd = os.getcwd()
print(cwd)

current_time = time.time()
print(current_time)

start_time = time.strftime("%Y-%m-%D_%H:%M:%S", time.localtime(current_time))
print('Program started at: ', start_time)

#create a new file in the current working directory
with open(cwd + '/home/Sarah/crontab/testFile_' + start_time + '.txt', 'w') as f:
    f.write(str(df)) 