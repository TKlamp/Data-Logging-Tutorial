# Data-Logging-Tutorial

## Installation & Setup

Download tklamp.py. 

Install the following packages. 
```
$ pip install serial, sys, pandas, matplotlib.pyplot, tqdm
```

TK2303 does not support live logging. Data is saved to tester first and transferred in the end to PC.
Before transferring data to PC, it is important to pause logging by clicking "stop recording" button on tester. 

## Quickstart 

1. Connect USB to PC, turn on tester.
   
    Find current USB serial port name.
    
    ```
    $ ls /dev/tty.*  
    ```
    
    ```
    >>>
    /dev/tty.BLTH
    /dev/tty.Bluetooth-Incoming-Port
    /dev/tty.usbserial-14440  #your serial_port_name
    ```

2. Get script ready in terminal, but DO NOT RUN it yet.

    ```
    $ python3 tklamp.py serial_port_name 
    ```

3. Start measurement. You can view live plot by navigating to the plotting page on tester. Once done, pause measurement using "Stop Recording" button.

5. Start transfer. Click on "Transfer Data" button on tester, now you have 10 seconds to run the script in step 2.

    Once finished, you should see confirmation message in terminal.  
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
    > What happens if I missed the 10s window or run them in the wrong order?
    Stop python script if it is running with `ctrl + c`. On tester, exit data transfer popup window. Then repeat step 4. 

