#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:47:21 2018

@author: yasminelyagoubi
"""

import Bluebelt

def test_checkout():
    assert checkout([Guitar,Insurance,Insurance])==1005

def test_empty_list():
    assert checkout([])==0