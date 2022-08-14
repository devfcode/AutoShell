#!/usr/bin/python3
# -*- coding:utf8 -*-

import wda
import time

# for debug
# Enable debug will see http Request and Response
# wda.DEBUG = True

wda.DEBUG = False # default False
wda.HTTP_TIMEOUT = 180.0 # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

#uuid="58dad54ccf463a7cf3752365408d766808f40ffd"
#port=8100
#c = wda.Client("http://localhost:8100")
#c = wda.USBClient(uuid, port=8100) # 指定设备 udid 和WDA 端口号
#c = wda.USBClient(uuid, port=8100) # 指定设备 udid 和WDA 端口号
#wda_bundle_id="com.facebook.WebDriverAgentRunner.xctrunner"
#c = wda.USBClient(uuid, port=port, wda_bundle_id=wda_bundle_id)
uuid = "58dad54ccf463a7cf3752365408d766808f40ffd"
port = 8100
wda_bundle_id = "com.facebook.WebDriverAgentRunner.xctrunner"
c = wda.USBClient(uuid, port=port, wda_bundle_id=wda_bundle_id)

curStatus = c.status()
print("curStatus=%s" % curStatus)

bundleID="com.tencet.xin001"
s = c.session(bundleID) # 打开app

# alert = s(xpath = '//Alert/Other[1]/Other[1]/Other[2]/ScrollView[2]/Other[1]/Other[1]/Other[3]')
# alert.click_exists()        # 有弹框就点击
if(s.alert.exists):
    s.alert.click("允许")
    # s.alert.accept() # 确认

s(name="注册").click()
# s(xpath = '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[2]').click()
# s(xpath = '//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[1]').click()

s(name="用手机号注册").click()

# 昵称
tf = s(xpath = '//ScrollView/Other[1]/Other[2]/TextField[1]')
tf.click()
tf.clear_text()
tf.set_text("Mingzhi312313")

# 选国家
# s(xpath='//ScrollView/Other[2]/Other[1]').click()
# s(xpath='//Window[1]/Other[3]/Other[1]/Other[1]/Other[1]/Other[1]/Table[1]/Cell[194]').click()
# s(className="XCUIElementTypeCell",name="泰国").click()
# 子元素定位
# s(className='XCUIElementTypeTable').child(name='泰国').click()

# 输入手机号
tf = s(xpath='//ScrollView/Other[3]/Other[1]/TextField[1]')
tf.click()
tf.set_text("958914757")

s(xpath='//ScrollView/Other[2]/Other[1]').click()
s(label="返回").click()
# s(label="下一项").click()
# sc = s(xpath='//ScrollView')
# sc.swipe_up()
# tf(label="删除").click()

stf = s(xpath='//SecureTextField')
stf.click()
stf.set_text("aass4757")

s(label="go").click()


# 同意微信协议
s(xpath='//ScrollView/Other[5]/Other[1]').tap()

s(className='XCUIElementTypeButton',label='同意并继续').click()


s(label="我已阅读并同意上述条款").click()

s(xpath='//ScrollView/Button[2]').click()


time.sleep(15)

s(label="开始").click()

time.sleep(60)

# s(label="返回注册流程").click()
#
# while()
s(label="返回注册流程").click()

# 接口获取验证码 (如果没收到验证码要重发)
# phone_code = httpg("www.xxxx.com")



