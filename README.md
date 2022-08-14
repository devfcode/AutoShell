# WebDriverAgent 自动化脚本

## 1. 调试工具安装
brew install libimobiledevice  
#libimobiledevice中并不包含ipa的安装命令，所以还需要安装  
brew install ideviceinstaller  

## 2. 配置 tidevice
## 安装 ssl 依赖
pip3 install -U "tidevice[openssl]" 
## 安装 tidevice
pip3 install -U tidevice

## 3. 配置python 驱动WebDriverAgent 的依赖包
pip3 install -U facebook-wda

## 4. 将 WebDriverAgent 安装在手机上
仓库地址: https://github.com/MyReverse/WebDriverAgent.git  
可以将 Xcode 运行工程后 在缓存中将 WebDriverAgentRunner-Runner 取出来, 放在 Payload 里压缩在一个新的 WebDriverAgent.ipa  
以后这个 WebDriverAgent.ipa 直接装在手机上,就不用每次运行 Xcode了   

## 5. tidevice 启动 WebDriverAgent.ipa 并设置 端口转发
tidevice xctest -B com.facebook.WebDriverAgentRunner.xctrunner -e USE_PORT:8100 --debug   
tidevice relay 8100 8100. 

## 6. 运行自己的 python 自动化脚本
./your_shell.py


## 辅助找界面元素的工具
### weditor 安装和使用
pip3 install -U weditor # 安装   
### 启动 weditor,命令行输入  
weditor  
网页上会自动打开一个调试界面, 在url里输入: http://localhost:8100   
即可连接   
