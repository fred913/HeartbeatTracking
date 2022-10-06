[中文](README_cn.md)|English

# HeartbeatTracking

A simple heartbeat tracking system, which could be used in Beat Saber live. 

## Requirements
 - A computer
 - A supported heartbeat tracking device (see the list below)

## Supported tracking devices
 - ALL Android **Wear** devices, like Mi Watch (2018), TicWatch

## Installation
### PC side (Make sure you have Python 3.7+ installed)
1. Go to [Releases](https://git.ft2.club/fred913/HeartbeatTracking/releases) and find the latest one, the top of the list.
2. Download the file marked as `Sources (ZIP)`.
3. Extract the ZIP file **to an empty directory**, the second one in step 2. 
4. Open the terminal (for Windows users, `cmd.exe`, `powershell.exe` or the `Windows Terminal`; for MacOS users, the `Terminal`; for Linux users, you must know about it or you should not use Linux), and open the extracted directory. 
5. Type `pip install pipenv && pipenv lock && pipenv sync && pipenv lock`. The steps should be automatically done. Then the installation process has finished. 
6. To run the server (PC side), open a terminal at where the files are located (the extracted zip) and type `pipenv run start-server`. To stop the server, press `Ctrl-C`.

### Wear side
1. Connect your watch to your PC. Make sure your PC has `adb` (aka Android Debug Bridge) installed. 
2. Go to [Releases](https://git.ft2.club/fred913/HeartbeatTracking/releases) and find the latest one (the top of the list), and download the APK file from the `Files` section.
3. Open a terminal at where the APK is located.  
4. Type `adb devices` and check if your Wear has connected. It should be like this:
```
List of devices attached
XXXXXXXXXXXXXXXX  device
```
Notice it's **device**. It shouldn't be `unauthorized`. If so, check for a permission prompt on your watch and accept it. 

5. Type `adb install ` (with one space at last), and input the full name of the APK file. On Windows, you can drag the file to the terminal window to prevent any mistake. 
6. Type ENTER, then wait until `Success` appears on the screen. 
7. Open the app on your watch. 
8. Find your PC's IP address and start the server on your PC, and type it on your watch, in the area. (For v0.1, there's a default value `10.0.0.29` and it shouldn't be used)
9. After typing the IP address, click `TRIGGER`. The heartbeat tracking will get started.

### Final steps
Open [this link](http://127.0.0.1:5999/heartbeat/show) in your browser and enjoy it! 
(NOTE: You can open the page in OBS browser and do something like a Greenscreen. Or adding it to OVR toolkit is also OK. You can do everything you want - like capturing the API, editing the code and beautify the page, because it's open-source.)

## Contribution
Currently the project needs tons of ideas. If you're ready to help, please write an email to me at `fredtools999@gmail.com`. If you're good at Python, just register an account in my Git service. Pull Requests are absolubely welcomed. 

## Last words
If you like the project, please share it to your friends who need it. Thanks. 