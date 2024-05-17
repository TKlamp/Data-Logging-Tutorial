#!/usr/bin/env python

import serial, sys, pandas, matplotlib.pyplot, tqdm, datetime, json

def byte_concant(lst):
   """ 
   Return decimal value of 2 bytes after concatenation  
   Param: a list of bytes

   Input example: [00,11,aa,aa, ..] 
   Return example: [17,43690, ..]
   """
   return [int(x+y,16) for x,y in zip(lst[0::2], lst[1::2])]

def generator():
   while True:
      yield

def main(): 
   # Verify if user input includes serial port 
   if (len(sys.argv) != 2):
      print("command line: tklamp.py serial_port")
      sys.exit()
   port = sys.argv[1]

   # Reading serial data
   ser = serial.Serial(port,9600)
   ser.setDTR()
   ser.flushInput()

   count = 0
   log = []
   log_dict = {  'lumen': [],
               'candela': [],
                   'lux': [],}

   # Read serial data and save to log list
   for _ in tqdm.tqdm(generator()):  # progress bar 
         count += 1
         x = ser.read()
         log.append(format(ord(x),"x"))
         if count == 3620:  
            break 

   # Decoding byte data from log list
   # Header: 1-16 byte
   header = byte_concant(log[:16])
   sampling_time = header[2]
   distance_to_surface = header[3]
   candela_multi = header[5]
   lux_multi = header[6] 

   # Body: 17-3616 byte
   log_dict['lumen'].extend(byte_concant(log[16:1216]))
   log_dict['candela'].extend(byte_concant(log[1216:2416]))
   log_dict['lux'].extend(byte_concant(log[2416:3616]))
   log_dict_pd = pandas.DataFrame(log_dict)

   # Apply candela and lux multipe. Multiples can be set in tester setting.
   log_dict_pd["candela"] =  log_dict_pd["candela"].apply(lambda x: x * candela_multi)
   log_dict_pd["lux"] =  log_dict_pd["lux"].apply(lambda x: x * lux_multi)

   # Save result to csv
   current_datetime = datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
   filename = "Output" + str(current_datetime) + ".csv"
   log_dict_pd.to_csv(filename, index=True)

   # Save metadata to json 
   meta_dict={
    'Export csv file name': filename,
    'Sampling time (ms)': sampling_time,
    'Distance to surface (cm)': distance_to_surface,
    'Candela multiples': candela_multi,
    'Lux multiples': lux_multi
   }

   jsonname = "Metadata" + str(current_datetime) + ".json"
   with open(jsonname, 'w') as f:
      json.dump(meta_dict, f)
      
   # Print confirmation message
   cfm_msg = f'''
   {'-'*60}
   # Successfully saved data in {filename}
   # Sampling time (ms): {sampling_time}
   # Distance to surface (cm): {distance_to_surface}
   # Candela multiples: {candela_multi}
   # Lux multiples: {lux_multi}
   {'-'*60}
   '''
   print(cfm_msg)
   
   # Uncomment below to plot results
   # log_dict_pd.plot()
   # matplotlib.pyplot.show()

if __name__ == '__main__':
    main() 
