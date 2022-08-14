# UI元素定位

## 基本选择器
### 通过 id
s(id='URL')
### 通过 className
s(className="XCUIElementTypeCell")
### 通过 name
s(name='屏幕使用时间')
s(nameContains='屏幕')
s(nameMatches="屏幕.*")
### 通过 value
s(value="屏幕使用时间")
### 通过 label
s(label="屏幕使用时间")
s(labelContains="屏幕")
注:也可以组合多个属性，可以组合的属性包括：className、name、label、visible、enabled
s(className="XCUIElementTypeCell",name="屏幕使用时间").click()

## 子元素定位
s(className='XCUIElementTypeTable').child(name='通知').exists

## 多个实例
### 返回所有匹配到的元素
s(nameContains='模式').find_elements()
[<wda.Element(id="15000000-0000-0000-0901-000000000000")>, <wda.Element(id="1B000000-0000-0000-0901-000000000000")>, <wda.Element(id="5E000000-0000-0000-0901-000000000000")>]
### 使用index来选择匹配到的多个元素
s(nameContains='模式', index=2).click() # 点击匹配到的第3个元素
#### 或者
s(nameContains='模式')[2].click()

## XPath定位
s(xpath='//*[@name="屏幕使用时间"]')
#### 或者
s.xpath('//*[@name="屏幕使用时间"]')

## Predicate定位
### Predicate定位是iOS原生支持的定位方式，定位速度比较快，它可以通过使用多个匹配条件来准确定位某一个或某一组元素。
s(predicate='name BEGINSWITH "屏幕"').click() # 点击屏幕使用时间

## classChain定位
### classChain是Predicate和Xpath定位的结合，搜索效率比XPath更高
s(classChain='**/XCUIElementTypeTable/*[`name == "通知"`]').click() # 点击【通知】

## 获取元素信息
### 检查元素是否存在
s(name="屏幕使用时间").exists # Return True or False
### 读取UI元素的属性信息
ele = s(name="屏幕使用时间").get(timeout=3.0) # 如果10s内没有找到，会抛出WDAElementNotFoundError错误
ele = s(name="屏幕使用时间").wait(timeout=3.0)

#### 获取元素属性
ele.className # XCUIElementTypeCell
ele.name # XCUIElementTypeCell
ele.visible # True 
ele.value 
ele.label # 屏幕使用时间
ele.text # 屏幕使用时间
ele.enabled # True 
ele.displayed # True 
ele.accessible

x, y, w, h = ele.bounds # Rect(x=0, y=744, width=375, height=46)


## 元素操作方法
### 点击UI元素
s(name="屏幕使用时间").get(timeout=3.0).tap()
s(name="屏幕使用时间").tap()
s(name="设置").tap_hold(2.0) # 长按
s(name="屏幕使用时间").click()
s(text='屏幕使用时间').click_exists() # return True or False
s(text='屏幕使用时间').click_exists(timeout=5.0)
### 点击像素坐标
s = c.session('com.apple.Preferences')
s.tap(490, 1885) # 通过像素坐标点击
s.click(490, 1885) 
s.click(0.426, 0.716)
s.double_tap(490, 1885)  # 双击

## 文本输入
### 文本值输入与清除
ele = s(text='搜索').get()
ele.set_text("NFC") # 输入文本
ele.clear_text() # 清除文本
ele.set_text("\b\b\b\n") # 删除3个字符
ele.set_text("NFC\n") # 输入文本并确认

## 等待wait
### 设置隐式等待
s.implicitly_wait(5) # 5s
### 设置超时时间
s.set_timeout(10.0)
### 等待元素
s(name="屏幕使用时间").wait(timeout=3.0) # 等待元素出现
s(name="屏幕使用时间").wait_gone(timeout=3.0) # 等待元素消失

## Alert操作
### 对Alert弹框进行处理
>>> print(s.alert.exists) # 判断是否存在
True
>>> print(s.alert.text) # 获取弹框信息
移除“设置”？
“从主屏幕移除”会将App保留在App资源库中。

s.alert.accept() # 确认
s.alert.dismiss() # 取消
s.alert.wait(5) # 等待出现
s.alert.buttons() # 返回选项，例如：['取消', '从主屏幕移除']
s.alert.click("取消") # 点击取消
s.alert.click(["取消", "cancel"]) # 点击出现的列表中的某个选项

### 监控到Alert出现后进行操作
with c.alert.watch_and_click(['好', '确定']):
	s(label="Settings").click() # 

## 滑动swipe
### 根据像素坐标滑动
c.swipe(fx, fy, tx, ty, duration=0.5) # 从(fx, fy)滑到(tx, ty)，坐标值可以是迅速值或者百分比，duration单位秒
c.swipe_left() # 向左滑动
c.swipe_right()
c.swipe_up()
c.swipe_down()

## 截图
s.screenshot().save("test.png")
from PIL import Image
s.screenshot().transpose(Image.ROTATE_90).save("correct.png") # 横屏截图
## 设备截屏
c.screenshot().save("screen.png")
c.press_duration("snapshot", 0.1) 

