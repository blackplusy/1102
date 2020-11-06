#coding=utf-8
from selenium import webdriver
import time
br=webdriver.Chrome()
br.maximize_window()
br.get("https://mail.qq.com/")
br.switch_to.frame("login_frame")
time.sleep(2)
br.find_element_by_link_text("帐号密码登录").click()
br.find_element_by_id("u").send_keys("914338492")
br.switch_to.default_content()
time.sleep(2)
br.find_element_by_link_text("手机版").click()

