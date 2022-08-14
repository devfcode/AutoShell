# wda 使用细节

## 创建客户端
import wda
c = wda.Client('http://localhost:8100')
c = wda.Client() # 读取环境变量DEVICE_URL,如果没有使用默认地址:http://localhost:8100

## 或者使用USBClient连接设备
c = wda.USBClient() # 仅连接一个设备可以不传参数
c = wda.USBClient("00008101-000255021E08001E", port=8100) # 指定设备 udid 和WDA 端口号
c = wda.Client("http+usbmux://{udid}:8100".format(udid="00008101-000255021E08001E")) # 通过DEVICE_URL访问
c = wda.USBClient("00008101-000255021E08001E", port=8100, wda_bundle_id="com.facebook.WebDriverAgentRunner.xctrunner") # 1.2.0 引入 wda_bundle_id 参数
注:初始化连接设备时不需要事先使用tidevice命令启动WDA,wda.Client()会自动启动WDA应用


## 设备操作
### 默认120s，安静的等待，无进度输出
c.wait_ready(timeout=120, noprint=True)

## 锁屏
### 判断是否已经锁屏
isClock =c.locked()
### 锁屏操作
c.lock()
### 解屏操作
c.unlock()

## 回到手机主页面
c.home()
### 或者
c.press("home")

## 增大降低音量
c.press("volumeUp")
c.press_duration("volumeUp", 1) # 长按1s
c.press("volumeDown")
c.press_duration("volumeDown", 1) 

## 打开App
s = c.session('com.apple.Health') # 打开app
s = c.session('com.apple.Health', alert_action="accept") 
s.close() # 关闭
c.session().app_activate("com.apple.Health") # 打开app

## 停止App
c.session().app_terminate("com.apple.Health") # 关闭app

## 获取app状态
appStatus = c.session().app_state("com.apple.Health") # 返回app状态
### 返回结果
{'value': 1, 'sessionId': 'BEB6A59E-254A-428A-AB53-F52A957ABE1F', 'status': 0}
1：表示已关闭
2：表示后台运行
4：表示正在运行

## 获取设备应用信息
### 查看设备状态信息
c.status()
{'message': 'WebDriverAgent is ready to accept commands', 'state': 'success', 'os': {'testmanagerdVersion': 28, 'name': 'iOS', 'sdkVersion': '14.5', 'version': '14.6'}, 'ios': {'ip': '192.168.5.159'}, 'ready': True, 'build': {'time': 'Jul 27 2021 20:50:24', 'productBundleIdentifier': 'com.facebook.WebDriverAgentRunner'}, 'sessionId': '4D60BDFB-5D18-4EFB-8C40-97E4826B9AAB'}
### 当前应用信息
c.app_current()
{'processArguments': {'env': {}, 'args': []}, 'name': '', 'pid': 228, 'bundleId': 'com.apple.Preferences'}
### 获取设备信息
c.device_info()
{'timeZone': 'GMT+0800', 'currentLocale': 'zh_CN', 'model': 'iPhone', 'uuid': '1DF5DFF9-93B2-4B87-8249-DB33ADB6A330', 'userInterfaceIdiom': 0, 'userInterfaceStyle': 'light', 'name': 'iPhone12', 'isSimulator': False}
### 电量信息
c.battery_info()
{'level': 0.9800000190734863, 'state': 2}
### 分辨率
c.window_size()
Size(width=375, height=812)

