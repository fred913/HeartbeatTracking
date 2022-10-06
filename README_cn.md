中文|[English](README.md)

# 心率检测

一个简单的心率检测，可适用于《节奏光剑》直播

## 需求
 - 一台电脑
 - 一个支持心率检测的设备（具体见下表）

## 知识的设备
 - 所有的 Android / WearOS **穿戴** 设备，例如 Mi Watch (2018)、TicWatch

## 安装
### PC 端（请确保安装了 Python3.7+）
1. 前往 [发行版](https://git.ft2.club/fred913/HeartbeatTracking/releases) 并且找到页面最顶部的最新版本
2. 下载源代码（被标注为 `源代码 (ZIP)`）
3. 将从第 2 步下载到的压缩包文件解压到 **一个空的文件夹**
4. 打开你的终端 (Windows 用户请尝试 `cmd.exe`, `powershell.exe` 或 `Windows Terminal`; MacOS 用户请打开 `终端`; Linux 用户应该会知道这一点，你可是在用 Linux)，并打开到该文件夹
5. 输入并运行 `pip install pipenv && pipenv lock && pipenv sync && pipenv lock`。以上安装步骤会自动完成。
6. 在这些文件所在的文件夹打开终端，输入 `pipenv run start-server` 以运行 PC 的服务端。可以输入 `Ctrl-C` 停止进程。

### 移动端
1. 将你的穿戴设备连接到电脑。请确保你的电脑安装了 `adb`，即 `Android 测试桥`
2. 前往 [发行版](https://git.ft2.club/fred913/HeartbeatTracking/releases) 并且找到页面最顶部的最新版本。下载 `附件` 里的 APK 文件。
3. 在 APK 文件所在的文件夹打开终端
4. 输入 `adb devices` 并检查穿戴设备是否连接。以下为示例：
```
List of devices attached
XXXXXXXXXXXXXXXX  device
```
注意：这里应为 **device**，而不是 `unauthorized`。如果是的话，请检查你的穿戴设备并同意 ADB 测试。

5. 输入 `adb install `（最后有个空格）并将你下载的 APK 的完整文件名输入进去。在 Windows 里，你可以直接拖拽 APK 文件以避免任何失误。
6. 回车
7. 打开穿戴设备上的应用。
8. 打开 PC 的服务端，找到电脑的 IP 地址并输入至移动端的输入框内（在v0.1版本内，有一个默认值 `10.0.0.29` 且不会被使用）
9. 输入完 IP 地址后，点击 `TRIGGER`。然后心率检测就会启动。

### 最终
在电脑的浏览器打开 `http://127.0.0.1:5999/heartbeat/show` 并享受这一切吧~  
(提示: 你可以在 OBS 的网页浏览器内打开该网页，并进行绿幕抠像。或者将其添加到 OVR 工具包中也可以。你可以做任何你想要的 - 比如捕获 API、编辑代码和美化页面，因为这是个开源项目)

## 贡献
目前该项目需要大量的想法。如果你准备好了，欢迎发电邮至 `fredtools999@gmail.com`。如果你擅长于Python，我们绝对欢迎你提交PR！

## 结语
如果你喜欢该项目，请把它分享给更多人。谢谢。