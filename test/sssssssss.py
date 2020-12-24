import time
from selenium import webdriver #赋值给驱动
driver=webdriver.Chrome() #用谷歌浏览器驱动
driver.get("http://101.200.204.190/#/login")#驱动谷歌打开该网址
driver.maximize_window()#窗口最大化
driver.find_element_by_xpath("//input[@placeholder='请输入账号']").send_keys("gudehai")#输入账号
driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("a123456")#输入密码
driver.find_element_by_xpath("//span[@class='el-checkbox__input']//span[1]").click()#点击登录
driver.find_element_by_xpath("(//button[@type='button'])[1]").click()#勾选记住密码
driver.implicitly_wait(5)#智能等待5秒钟
driver.find_element_by_css_selector("aside#aside>div>div>div>div>ul>li:nth-of-type(2)>div>i:nth-of-type(2)").click()#点击主工作台客户管理
driver.find_element_by_xpath("//li[text()='融资客户管理']").click()#点击融资客户管理
driver.find_element_by_xpath("(//button[@title='详情']//i)[1]").click()#点击客户详情
driver.find_element_by_xpath("(//div[@class='el-tabs__item is-top'])[4]").click()#点击拜访记录
driver.find_element_by_css_selector("div#pane-4>div>div>div>form>div:nth-of-type(4)>div>button").click()#点击新增拜访记录
driver.find_element_by_xpath("(//button[contains(@class,'el-button fl')])[4]").click()#点击选择人员
driver.find_element_by_xpath("(//input[@placeholder='输入关键字进行搜索'])[1]").send_keys("谷德海")#输入谷德海
driver.find_element_by_xpath("(//div[@class='el-input-group__append']//button)[1]").click()#点击搜索谷德海
driver.find_element_by_xpath("(//label[@class='el-checkbox chooseA']//span)[1]").click()#选择勾选框
driver.find_element_by_css_selector("html>body>div:nth-of-type(2)>div>div:nth-of-type(3)>span>button:nth-of-type(2)>span").click()#点击确认
driver.find_element_by_xpath("(//div[contains(@class,'fl el-input')]/following-sibling::button)[5]").click()#点击选择人员
driver.find_element_by_xpath("(//input[@placeholder='输入关键字进行搜索'])[1]").send_keys("谷德海")#输入谷德海
driver.find_element_by_xpath("(//div[@class='el-input-group__append']//button)[1]").click()#点击搜索谷德海
driver.find_element_by_xpath("(//span[@class='el-checkbox__input']//span)[5]").click()#选择勾选框
driver.find_element_by_xpath("//div[@id='pane-4']/div[1]/div[1]/div[9]/div[1]/div[1]/div[3]/span[1]/button[2]").click()#点击确认
driver.find_element_by_xpath("(//input[@placeholder='开始日期'])[2]").click()#定位拜访日期
driver.find_element_by_xpath("(//input[@placeholder='选择日期'])[3]").send_keys("2020-10-16")#输入开始日期
time.sleep(2)
driver.find_element_by_xpath("//input[@placeholder='选择时间']").click()#选择时间
driver.find_element_by_xpath("//button[@class='el-time-panel__btn confirm']").click()#点击时间确认
driver.find_element_by_xpath("(//button[contains(@class,'el-button el-picker-panel__link-btn')])[2]").click()#点击开始拜访日期确认
time.sleep(2)
driver.find_element_by_xpath("//input[@placeholder='结束日期']").click()#定位拜访日期
driver.find_element_by_xpath("(//input[@placeholder='选择日期'])[4]").send_keys("2020-10-17")#输入开始日期
time.sleep(2)
driver.find_element_by_xpath("(//input[@placeholder='选择时间'])[2]").click()#选择时间
driver.find_element_by_xpath("(//button[@class='el-time-panel__btn confirm'])[2]").click()#点击时间确认
driver.find_element_by_xpath("(//button[contains(@class,'el-button el-picker-panel__link-btn')])[4]").click()#点击结束拜访日期确认
driver.find_element_by_xpath("(//textarea[@class='el-textarea__inner'])[4]").send_keys("nicai")#定位拜访地点并输入内容
driver.find_element_by_xpath("(//textarea[@class='el-textarea__inner'])[5]").send_keys("skrjgwlojo够够够够")#定位主要成果并输入内容
driver.find_element_by_css_selector("div#pane-4>div>div>div:nth-of-type(5)>div>div:nth-of-type(3)>span>button:nth-of-type(2)").click()#点击保存

