#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:47:19 2018

@author: yasminelyagoubi
"""

shopping_cart=[]
Guitar=1000
Pick_box=5
Guitar_Strings=10
Insurance=5
Priority_mail=10
def checkout(shopping_cart):
    
    if shopping_cart.count(Insurance)>1:
        return (sum(shopping_cart)-((shopping_cart.count(Insurance)*Insurance))+Insurance)
    elif shopping_cart.count(Priority_mail)>1: 
        return (sum(shopping_cart)-((shopping_cart.count(Priority_mail)*Priority_mail))+Priority_mail)    
    elif len(shopping_cart)==0:
        return("The list is empty")
    else:
        return sum(shopping_cart)