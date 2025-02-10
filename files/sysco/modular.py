import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


path = "/Users/abdussami/Desktop/chaya/chromedriver"
service = Service(path)

############

def CLAuto_ck(method,ddv,css_search,*args):
    if args[0]!= 0:
        ddv.implicitly_wait(args[0])
    i_element = ddv.find_element(method, css_search)
    i_element.click()

       


def CLAuto_sk(method,ddv,css_search,data,*args):
        if args[0]:
            ddv.implicitly_wait(args[0])
        i_element = ddv.find_element(method,css_search)
        i_element.send_keys(Keys.BACKSPACE)
        ddv.implicitly_wait(0.2)
        i_element.send_keys(data)
        i_element.send_keys(Keys.RETURN)

def general_css_click(method,ddv,store_fullist,store_dict,*args):
    _set_ = True
    while _set_ == True:
        try:
            CLAuto_ck(method,ddv,store_fullist[store_dict],args[0])
            _set_ = False
        except: 
            for errors in args[1]:
                try:
                    CLAuto_ck(method,ddv,errors)
                    time.sleep(2)
                finally: pass
            time.sleep(2)
    
def general_css_sk(method,ddv,store_fullist,store_dict,data,*args):
    _set_ = True
    while _set_ == True:
        try:
            CLAuto_sk(method,ddv,store_fullist[store_dict],data,args[0])
            _set_ = False
        except: 
            for errors in args[1]:
                try:
                    CLAuto_ck(method,ddv,errors)
                    time.sleep(2)
                finally: pass
            time.sleep(2)

