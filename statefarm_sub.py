# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:53:03 2016

@author: spookfish
"""

import numpy as np
import pandas as pd
import csv

data = pd.read_csv('statefarm_sub1.csv')

data = data.sort_values(['img'])

data.to_csv('statefarm_sub2.csv', index=False)