#coding=utf-8
from selenium import webdriver
br=webdriver.Chrome()
br.get("https://www.baidu.com")
#1.标签选择器
# br.find_element_by_css_selector("input").send_keys("123")
#2.id选择器
# br.find_element_by_css_selector("#kw").send_keys("美国大选")
# 3.class选择器
# br.find_element_by_css_selector(".s_ipt").send_keys("拜登")
# 4.其他属性定位
# br.find_element_by_css_selector("[name='wd']").send_keys("川普")
#组合属性定位
# br.find_element_by_css_selector("input#kw").send_keys("钓鱼岛")
# br.find_element_by_css_selector("input.s_ipt").send_keys("270")
br.find_element_by_css_selector("input[name='wd']").send_keys("后裔")