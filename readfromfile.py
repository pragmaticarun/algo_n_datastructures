# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 20:45:40 2019

@author: atara
"""

import random

with open("quotes.txt","r") as f:
    s = f.readlines()
    print(s[random.randint(0,1)])
    
from collections import defaultdict

x = defaultdict(lambda: 20*20)

print(x[21])