#coding=utf-8
from selenium import webdriver
br=webdriver.Chrome()
br.get("http://127.0.0.1/test.html")
#1.通过send_keys()
# br.find_element_by_id("select1").send_keys("ccc")
#2.通过二次操作
br.find_element_by_id("select1").find_element_by_xpath("//option[@value='20']").click()
