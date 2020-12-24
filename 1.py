'''
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://39.106.254.225/#/login")
driver.maximize_window()
#time.sleep(1)
driver.implicitly_wait(5)#智能等待5秒
#driver.set_window_size(1280,960)设置窗口大小
driver.find_element_by_class_name("el-input__inner").send_keys("gudehai")
#time.sleep(2)#强制等待
driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("a123456")
driver.find_element_by_xpath("//span[text()=' 登录 ']").click()
driver.find_element_by_xpath("(//span[text()='主工作台'])[1]").click()
driver.find_element_by_xpath("(//li[@role='menuitem'])[2]").click()
#time.sleep(2)#强制等待
driver.find_element_by_id("tab-1").click()
#time.sleep(4)
#driver.find_element_by_id("tab-first").click()#点击我已审批下面的全部
target = driver.find_element_by_xpath("(//li[@class='number'])[2]").click()#定位页面数第3页进行点击(0,1,2)
driver.find_element_by_xpath("(//span[contains(@class,'oper_shenhejilu icon-operate-btn')])[1]").click()
#time.sleep(3)这个强制等待可以不要
driver.find_element_by_css_selector("div#approvalRecords>div>header>div>p:nth-of-type(7)>button:nth-of-type(2)>span").click()
#time.sleep(3)
num=driver.window_handles
driver.switch_to.window(num[1])
#driver.switch_to.frame("frame_test")无用
driver.find_element_by_xpath("(//input[@class='el-input__inner'])[1]").send_keys("333")
driver.find_element_by_xpath("(//button[@class='el-button el-button--primary'])[1]").click()
driver.find_element_by_xpath("//i[contains(@class,'icon-operate-btn iconfont')]").click()
driver.find_element_by_xpath("(//button[contains(@class,'el-button fr')]//span)[1]").click()
driver.find_element_by_xpath("(//textarea[@class='el-textarea__inner'])[1]").send_keys("走，大保健去")
driver.find_element_by_xpath("//button[@slot='append']//span[1]").click()
driver.find_element_by_css_selector("div#approval-comments>div:nth-of-type(6)>div>div>div:nth-of-type(3)>div:nth-of-type(2)>button").click()
driver.quit()#退出浏览器
#实现新建项目时对项目名称不重复........................................................................................................................................................
.........................................................................................................................
.........................................................................................................................
from time import sleep #导入时间模块
from selenium import webdriver#从模块selenium中导入webdriver定义。
import random
import os
def shengcheng():
    return random.randint(0,1000)
driver=webdriver.Chrome()#赋值谷歌驱动
driver.get("http://39.106.254.225/#/login")#驱动加载网址
driver.maximize_window()#窗口做大化
driver.implicitly_wait(5)#智能等待5秒
#driver.set_window_size(1280,960)设置窗口大小
driver.find_element_by_class_name("el-input__inner").send_keys("gudehai")#登录页面，输入账号
driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("a123456")#登录页面，输入密码
driver.find_element_by_xpath("//span[text()=' 登录 ']").click()#然后点击登录
driver.find_element_by_css_selector("aside#aside>div>div>div>div>ul>li:nth-of-type(2)>div").click()#点击主工作台客户管理
driver.find_element_by_xpath("//li[text()='融资客户管理']").click()#点击客户管理下的融资客户管理
driver.find_element_by_css_selector("div#main_view>div>div:nth-of-type(2)>div:nth-of-type(2)>button:nth-of-type(3)>span").click()#点击新增融资客户
driver.find_element_by_xpath("(//input[@placeholder='请输入客户名称'])[2]").send_keys(('测试编号：'+str(shengcheng())))#输入客户名称
driver.find_element_by_xpath("//input[@placeholder='请输入客户简称']").send_keys("922gu")#输入客户简称
driver.find_element_by_css_selector("input#province").click()#选择客户状态
driver.find_element_by_xpath("(//input[@placeholder='请选择客户状态'])[2]").click()#选择客户状态
driver.find_element_by_xpath("(//span[text()='初步洽谈'])[2]").click()#选择客户状态
driver.find_element_by_xpath("(//input[@name='province'])[2]").click()#选择行业1
driver.find_element_by_xpath("(//li[text()=' 农、林、牧、渔业 '])[2]").click()#选择行业1
driver.find_element_by_xpath("(//input[@name='city'])[2]").click()#选择行业2
driver.find_element_by_xpath("(//li[text()=' 农业 '])[2]").click()#选择行业2
driver.find_element_by_css_selector("div#main_view>div>div:nth-of-type(7)>div>div:nth-of-type(2)>div>div>div>div>form>div:nth-of-type(19)>div>div>textarea").send_keys("你猜")
driver.find_element_by_xpath("(//button[contains(@class,'el-button el-button--default')]/following-sibling::button)[5]").click()
driver.find_element_by_xpath("//button[@title='9.22gu']//span[1]").click()
'''
import time
from time import sleep #导入时间模块
from selenium import webdriver#从模块selenium中导入webdriver定义。
import random
import os
def shengcheng():
    return random.randint(0,1000)
driver=webdriver.Chrome()#赋值谷歌驱动
driver.get("http://39.106.254.225/#/login")#驱动加载网址
driver.maximize_window()#窗口做大化
driver.implicitly_wait(5)#智能等待5秒
#driver.set_window_size(1280,960)设置窗口大小
driver.find_element_by_class_name("el-input__inner").send_keys("gudehai")#登录页面，输入账号
driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("a123456")#登录页面，输入密码
driver.find_element_by_xpath("//span[text()=' 登录 ']").click()#然后点击登录
driver.find_element_by_css_selector("aside#aside>div>div>div>div>ul>li:nth-of-type(2)>div").click()#点击主工作台客户管理
driver.find_element_by_xpath("//li[text()='融资客户管理']").click()#点击客户管理下的融资客户管理
time.sleep(2)
driver.find_element_by_xpath("//button[@title='测试编号：643']//span[1]").click()
driver.find_element_by_id("tab-1").click()
driver.find_element_by_xpath("(//div[@class='el-form-item__content']//button)[5]").click()
driver.find_element_by_xpath("(//input[@placeholder='请输入联系人姓名'])[2]").send_keys(('倪大红'+str(shengcheng())))
driver.find_element_by_xpath("(//input[@placeholder='请输入部门'])[2]").send_keys("测试部")
driver.find_element_by_xpath("//input[@placeholder='请输入固话']").send_keys("01025688745")
driver.find_element_by_xpath("//input[@placeholder='请输入职务']").send_keys("我是老板")
driver.find_element_by_xpath("(//span[@class='el-radio__input']//span)[1]").click()
driver.find_element_by_xpath("//input[@placeholder='请输入证件号码']").send_keys("342201199602189598")
driver.find_element_by_xpath("//input[@placeholder='请输入手机号码']").send_keys("15600589845")
driver.find_element_by_xpath("(//input[@placeholder='请输入邮箱'])[2]").send_keys("1550485652@qq.com")
driver.find_element_by_css_selector("div#pane-1>div>div:nth-of-type(4)>div>div:nth-of-type(3)>span>button:nth-of-type(2)").click()
driver.find_element_by_id("tab-2").click()
driver.find_element_by_css_selector("div#pane-2>div>div>div>form>div:nth-of-type(4)>div>button").click()
driver.find_element_by_css_selector("div#pane-2>div>div>div:nth-of-type(5)>div>div:nth-of-type(2)>div>form>div>div>div>div>span>span>i").click()
driver.find_element_by_xpath("html[1]/body[1]/div[3]/div[1]/div[1]/ul[1]/li[1]").click()
driver.find_element_by_xpath("//input[@placeholder='请输入股东姓名']").send_keys(('顾得哈'+str(shengcheng())))
driver.find_element_by_xpath("//input[@placeholder='请输入持股数']").send_keys("100000")
driver.find_element_by_xpath("//input[@placeholder='请输入身份证号']").send_keys("342201199602178956")
driver.find_element_by_xpath("//input[@placeholder='请输入持股比例']").send_keys("100000")
driver.find_element_by_css_selector("div#pane-2>div>div>div:nth-of-type(5)>div>div:nth-of-type(3)>span>button:nth-of-type(2)").click()
driver.find_element_by_id("tab-3").click()
#driver.find_element_by_css_selector("div#cus_file>div>div:nth-of-type(2)>ul>li:nth-of-type(2)").click()
#os.system(r'C:\Users\15501\shangchuan.exe %s%D:\测试文件夹\1.docx')
driver.find_element_by_xpath("//ul[@class='clearfix']//li[1]").click()
driver.find_element_by_id("tab-4").click()
driver.find_element_by_css_selector("div#pane-4>div>div>div>form>div:nth-of-type(4)>div>button").click()
driver.find_element_by_css_selector("div#pane-4>div>div>div:nth-of-type(5)>div>div:nth-of-type(2)>div>form>div:nth-of-type(2)>div>button").click()
driver.find_element_by_xpath("(//input[@placeholder='输入关键字进行搜索'])[1]").send_keys("谷德海")
time.sleep(3)
driver.find_element_by_xpath("(//div[@class='el-input-group__append']//button)[1]").click()
driver.find_element_by_xpath("(//label[@class='el-checkbox chooseA'])[1]").click()
#time.sleep(2)
#js="var q=document.documentElement.scrollTop=1000"
#driver.execute_script(js)
time.sleep(2)
driver.find_element_by_css_selector("html>body>div:nth-of-type(3)>div>div:nth-of-type(3)>span>button:nth-of-type(2)").click()
driver.find_element_by_xpath("(//button[contains(@class,'el-button fl')])[5]").click()
driver.find_element_by_xpath("((//span[text()='选择人员'])[3]/following::input)[1]").send_keys("谷德海")#定位输入框编辑，谷德海
time.sleep(2)
driver.find_element_by_xpath("//span[@class='el-input__suffix']/following-sibling::div[1]").click()#点击搜索按钮
time.sleep(3)
driver.find_element_by_xpath("html[1]/body[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/p[1]/span[1]/label[1]").click()
print('1111')
driver.find_element_by_css_selector("html>body>div:nth-of-type(3)>div>div:nth-of-type(3)>span>button:nth-of-type(2)").click()
