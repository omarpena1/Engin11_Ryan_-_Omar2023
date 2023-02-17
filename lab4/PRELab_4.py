#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import time
import random
import sys

# sys.argv

start_time = int(time.time())
itime = start_time\

run_time = int(sys.argv[1])

# file_name = "data_tbl"

# if( len(sys.argv)>2):
#     file_name = sys.argv[1]
    
# file = open(file_name, 'w')

# print(file_name)


while itime < (start_time + run_time):
    value = (random.random())
    itime = time.time()
    print(itime, value)
    time.sleep(1)
    
    
    
#on your terminal cd C:...users/... python PRELab_4.py