# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:47:52 2021

@author: CWilson
"""
#Import Values
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#Define zips to scrape
boston_zips = ["02108", "02109", "02110", "02111", "02112", "02113", "02114", 
               "02115", "02116", "02117", "02118", "02119", "02120", "02121",
               "02122", "02123", "02124", "02125", "02126"]