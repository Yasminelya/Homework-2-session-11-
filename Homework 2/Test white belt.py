#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:18:42 2018

@author: yasminelyagoubi
"""

from whitebelt import checkout

def test_checkout():
    assert checkout([Guitar,Guitar,Pick_box])==2005
    
def test_empty_list():
    assert checkout([])==0
