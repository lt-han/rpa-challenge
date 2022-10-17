# pip install rpa --upgrade
# pip install pandas --upgrade

import pandas as pd
import rpa as r
import os

r.init(chrome_browser = True, visual_automation = True, headless_mode = False, turbo_mode = True)
r.url('https://developer.automationanywhere.com/challenges/AutomationAnywhereLabs-ShoppingList.html')

r.click('//a[contains(@class,"btn btn-success")]')
while not os.path.exists("ShoppingList.csv"):
    r.wait(1)
df = pd.read_csv("ShoppingList.csv")

for i in range(len(df.axes[0])):
    # 输入食物名称
    r.type('//div[@class="form-group"]/input[@id="myInput"]',"[clear]" + df["Favorite Food"][i])
    
    # 点击添加按钮
    r.click('//div[@class="form-group"]/button[contains(@class,"btn btn-success btn-lg")]')

# 点击接受条款
r.click('//div[@class="form-check form-check-inline"]/input[@id="agreeToTermsYes"]')

# 点击提交订单
r.click('//div[@class="form-group"]/button[contains(@class,"btn-primary")]')