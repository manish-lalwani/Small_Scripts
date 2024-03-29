'''
Had small requirement from Team to connect linux host remotely so found this library called paramiko.

Using paramiko to connect to Linux host and executing commands remotely and getting the output and providing input 
using stdout, stdin and stderr
'''

import paramiko 
import os
import time
import datetime

now = datetime.datetime.now()
day = now.day 
month = now.month
year = now.year
hour = now.hour
minute = now.minute
#====

todays_date = datetime.date.today()
#todays_date_str=todays_date.srftime('%d_%m_%y')

#date in string format
todays_date_str=todays_date.strftime('%d%m%y')


output_file_name = 'script_output_' + todays_date_str
command_date = 'date >> ' + output_file_name
command_df='df -hT | grep /dev/sdb >>  ' + output_file_name
command_ping = 'ping -c 4 google.com >> ' + output_file_name
command_touch='touch ' + output_file_name
command_echo= 'echo "=============================================" >> ' + output_file_name

try:
	client=paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	#or
	#client.load_system_host_keys()
	# will load the host keys from the systems host keys as i was getting not known host error and was little suspicious about adding auto policy so used this line
	
	client.connect('direct.labs.play-with-docker.com','22','ipxxx-xx-x-xx-xxxxxxxxxxxxxxx','None') #docker instance
	#client.connect(hostname, port=port, username=username, password=password) #normal host

	stdin,stdout,stderr=client.exec_command('cd /root')
	stdin,stdout,stderr=client.exec_command('pwd')
	stdin,stdout,stderr=client.exec_command(command_touch)
	#command  touch $( date '+%Y-%m-%d_%H-%M-%S' )
	#time.sleep(2)
	print("stdout\n\n",stdout.readlines(),"stderr : ",stderr.readlines())
	#time.sleep(2)
	stdin,stdout,stderr=client.exec_command(command_echo)
	stdin,stdout,stderr=client.exec_command(command_date)
	stdin,stdout,stderr=client.exec_command(command_df)
	stdin,stdout,stderr=client.exec_command(command_echo)
	stdin,stdout,stderr=client.exec_command(command_ping,get_pty=True)
	time.sleep(2)
	print("stdout\n\n",stdout.readlines(),"stderr : ",stderr.readlines())



except Exception as e:
	print("An exception occoured : ",e)


finally:
	client.close()
