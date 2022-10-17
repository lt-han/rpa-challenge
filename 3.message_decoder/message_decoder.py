# pip install rpa --upgrade
# pip install pandas --upgrade

import rpa as r
import baidu_translate

r.init(chrome_browser = True, visual_automation = True, headless_mode = False, turbo_mode = True)
r.url('https://developer.automationanywhere.com/challenges/AutomationAnywhereLabs-Translate.html')


text_input = r.read('//div/div/section/h2/text()')
text_input = text_input.replace("Text to Decode:","").strip()

text_output = baidu_translate.translate(text_input,"保加利亚语","英语")
r.popup('automationanywhere')

r.type('//input[@id="message_input"]',text_output)
r.click('Submit')
r.wait(10)