import os
import subprocess
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
subprocess.call('C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE')
#os.startfile('C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE')
#chrome_options = webdriver.FirefoxOptions() # 实例化Option对象
#chrome_options.add_argument('--headless') # 靜默浏览器
#driver = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://exchange.hktvmall.com/merchant/shared/loginform.php')
userName = driver.find_element_by_name('username')
userName.send_keys('H0909000_SM')
password = driver.find_element_by_name('pwd')
password.send_keys('90936388')
login = driver.find_element_by_xpath("//input[@value='Login']")
login.click()
driver.get('https://exchange.hktvmall.com/merchant/home/oms_order.php?shippingMethod=omsStandardDelivery')

order_string = []

orderIds = driver.find_elements_by_id('orderId')
pick_ups = driver.find_elements_by_id('pickUpDate')

for i in range(len(orderIds)):
    string = []
    string.append(orderIds[i].text)
    orderIds[i].click()
    string.append(pick_ups[i].text)
    order_string.append(string)

print(order_string)
driver.execute_script("window.open('https://web.whatsapp.com/');")
driver.execute_script("window.open('https://www.wix.com/dashboard/045a4ad6-dc06-4bba-abf3-67875492ac54/store/categories/list/category/58b9d2cc-eeef-b192-f2c1-bc29bf694d64');")
#driver.switch_to.window(driver.window_handles[-1])



#driver.get('https://y.qq.com/n/yqq/album/003DFRzD192KKD.html') # 访问页面
#time.sleep(2)
#button = driver.find_element_by_class_name('js_get_more_hot')
#button.click()
#time.sleep(1)
#button.click()
#time.sleep(1)
#comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') # 使用class_name找到评论
#print(len(comments)) # 打印获取到的评论个数
#for comment in comments: # 循环
    #sweet = comment.find_element_by_tag_name('p') # 找到评论
    #print('评论：%s\n ---\n'%sweet.text) # 打印评论
#driver.close() # 关闭浏览器
