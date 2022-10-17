
# pip install rpa --upgrade
# pip install pandas --upgrade

import rpa as r
def translate(text_input,input_lang=None,output_lang="中文(简体)"):
    # 请求百度翻译url
    r.dom('window.open("https://fanyi.baidu.com")')

    # 新窗口中打开
    r.popup('fanyi')
    # 输入文本
    r.type('//textarea[@id="baidu_translate_input"]',"[clear]" + text_input + "[enter]")

    # 点击选择文本语言
    if input_lang:
        r.click('//a[contains(@class,"select-from-language")]/span[@class="select-inner"]/span[@class="language-selected"]')
        r.click(f'//div[@class="lang-table"]//span[text()="{input_lang}"]')
        r.wait()


    # 点击选择目标语言
    if output_lang:
        r.click('//a[contains(@class,"select-to-language")]/span[@class="select-inner"]/span[@class="language-selected"]')
        r.click(f'//div[@class="lang-table"]//span[text()="{output_lang}"]')
        r.wait()
 

    text_out = r.read('//div[@class="trans-right"]//p[contains(@class,"target-output")]')
    r.dom('window.close()')
    return text_out
