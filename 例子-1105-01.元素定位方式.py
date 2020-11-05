#coding=utf-8
#导入webdriver库
from selenium import  webdriver
#定义浏览器的驱动
br=webdriver.Chrome()
#打开网页
br.get("https://www.baidu.com")
#1.通过id值来定位百度的输入框
# br.find_element_by_id("kw").send_keys("黑哥真帅！")
#2.通过name的值来定位百度的输入框
# br.find_element_by_name("wd").send_keys("美国大选")
#3.通过class的值来定位百度的输入框
# br.find_element_by_class_name("s_ipt").send_keys("拜登")
#4.通过tag进行定位百度的输入框
# br.find_element_by_tag_name("input").send_keys("川普")
#5.通过link定位百度新闻超链接
# br.find_element_by_link_text("新闻").click()
#6.通过partial_link定位带有闻的超链接
# br.find_element_by_partial_link_text("闻").click()
#7.通过xpath定位id是kw的元素
# br.find_element_by_xpath("//*[@id='kw']").send_keys("哈勒少什么意思")
#8.通过css来定位id是kw的元素
br.find_element_by_css_selector("#kw").send_keys("塞朗黑！")

