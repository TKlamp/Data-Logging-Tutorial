# Data-Logging-Tutorial

Quickstart guide to exporting TK2303D measurement data to PC in csv. 

## Installation & Setup

> This guide is created for MacOS. For Linux, refer to [notes](https://gist.github.com/flashlightstuff/fc9b65e3d4a158d985975968c78b4522) shared by @nescobar

Download [tklamp.py](/tklamp.py). 

Install the following packages. 
```
$ pip install pyserial, sys, pandas, matplotlib, tqdm, datetime
```

TK2303D does not support live logging, as data is saved first to the tester before being transferred to a PC. It is essential to pause logging by clicking the "stop recording" button on the tester before initiating the transfer process.

## Quickstart

1. Connect USB to PC, turn on tester.
   
    Find the name of the current USB serial port using command below. 
    
    ```
    $ ls /dev/tty.*  
    ```
    
    ```
    >>>
    /dev/tty.BLTH
    /dev/tty.Bluetooth-Incoming-Port
    /dev/tty.usbserial-14440  #your serial_port_name
    ```

2. Get script ready to run in terminal, but DO NOT RUN it yet. 

    ```
    $ python3 tklamp.py serial_port_name 
    ```

3. Start measurement.

   You can view live plot by navigating to the plotting page. Once done, pause measurement using "Stop Recording" button.

4. Transfer data to PC. 

   Click on the "Transfer Data" button on the tester. Within the next 10 seconds, execute the tklamp.py script with the command specified in step 2. Script must be executed before the countdown for data transfer reaches 0.
   
   After the data transfer is complete, the terminal will return a confirmation message.  
    ```
    >>>
       ------------------------------------------------------------
       # Successfully saved data in Output_2024-04-23 at 00:19:27.csv
       # Sampling time (ms): 500
       # Distance to surface (cm): 100
       # Candela multiples: 1
       # Lux multiples: 1
       ------------------------------------------------------------
    ```
    > What happens if I missed the 10s window or run steps in the wrong order?
    > Stop python script using `ctrl + c` if it is still running. Exit data transfer popup window on the tester. Repeat step 4.


## Troubleshooting 

- Reboot your tester and run the script again.
- When transferring data, ensure that "recording" is paused to avoid any issues.
- It is crucial to run the script within 10 seconds of triggering the data transfer button. Running it too soon or too late may result in errors. 
- Changing the order of steps could potentially lead to errors or result in receiving irrelevant data.


## Video
[![Youtube](https://img.youtube.com/vi/NJ26TU5rA78/0.jpg)](https://www.youtube.com/watch?v=NJ26TU5rA78)


