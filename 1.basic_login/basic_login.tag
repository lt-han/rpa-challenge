// 请求url
https://s3-us-west-2.amazonaws.com/aai-devportal-media/wp-content/uploads/2021/06/29093713/AutomationAnywhereLabs-Login.html

// 输入账号
type //form/div/input[@id="inputEmail"] as user@automationanywhere.com

// 输入密码
type //form/div/input[@id="inputPassword"] as Automation123

// 点击登录
click //form/button[contains(@class,"btn-login")]

// 等待10秒
wait 10