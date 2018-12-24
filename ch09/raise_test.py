#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 11:01:29 2018

@author: pinyu
"""

import sys

def displaySalary(salary):
    if salary < 0:
        raise ValueError('薪水為正')
    print("薪水" + str(salary))

try:
    Salary = eval(input("請輸入薪水："))
    displaySalary(Salary)
except OSError as err:
    print("OSError:(0)", format(err))
except ValueError:
    print("請輸入薪水值為正")
except:
    print("Unexpected error:",sys.exc_info()[0])