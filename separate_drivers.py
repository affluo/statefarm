# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:51:46 2016

@author: robsalz
"""
import os
import pandas as pd
import shutil 


drivers_df = pd.read_csv('/Users/robsalz/Projects/data/statefarm/driver_imgs_list.csv')
drivers = []
classes = []

for driver in drivers_df['subject']:
    if driver not in drivers:
        drivers.append(driver)
        
for classname in drivers_df['classname']:
    if classname not in classes:
        classes.append(classname)
        
for classname in classes:
    os.makedirs('/Users/robsalz/Projects/data/statefarm/split2/val/' + classname)
    os.makedirs('/Users/robsalz/Projects/data/statefarm/split2/train/' + classname)

        

        
        
tr_drivers = drivers[0:5]
va_drivers = drivers[5:-1]



for i in drivers_df.index:
    src = '/Users/robsalz/Projects/data/statefarm/imgs/train/' + drivers_df['classname'][i] + '/' + drivers_df['img'][i]
    if drivers_df['subject'][i] in va_drivers:
        dst = '/Users/robsalz/Projects/data/statefarm/split2/val/' + drivers_df['classname'][i] + '/' + drivers_df['img'][i]
        shutil.copy2(src, dst)
    else:
        dst = '/Users/robsalz/Projects/data/statefarm/split2/train/'+ drivers_df['classname'][i] + '/' + drivers_df['img'][i]
        shutil.copy2(src, dst)
           