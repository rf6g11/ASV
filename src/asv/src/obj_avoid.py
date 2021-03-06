
import roslib; roslib.load_manifest('asv') 
import serial
import time
import ais
from math import sqrt
from time import sleep


from std_msgs.msg import String

#from asv.msg import compass
from asv.msg import position

from asv.msg import ais_data               
from asv.msg import status


##############################################################
###Set up the port####
##############################################################

def setUpSerial():
    global serialPort
 
    serialPort = serial.Serial( port= '/dev/ttyUSB0' ,  baudrate = '38400' , timeout = 0.5) ##import the data from USB0 port on the BBB
    
    serialPort.bytesize = serial.EIGHTBITS
    serialPort.stopbits = serial.STOPBITS_ONE
    serialPort.parity = serial.PARITY_NONE
    
    print "Initialised AIS Serial."
    print serialPort.portstr
    print serialPort.isOpen()
    return serialPort.isOpen()

#############################################################
###Loop to listen for the data###
#############################################################


def listenForData(status):
	global serialPort

	counter = 1 ###later used to define the sleep function

	time_zero = time.time()
	time_out = 5
	maximum_sleep_ais = 60  ###defines the maximum sleep time before cheking for a vessel nearby

	while not rospy.is_shutdown():

		time.sleep(0.01)
		while time.time()-time_zero<time_out :
			
			pubStatus.publish(nodeID = 3, status = status)
				
        		dataraw = data.readline() ##read the data entering the port and assmebles per line
        		line=dataraw.split() 
        		newline=[] ##creating an empty string to be poulated by the 
       			for elem in line:
                		newline.extend(elem.strip().split(',')) ##split the data by comma (,) into different elements and appending them to the empty string

#       print newline (to confirm the data output while developing)

			try : ###try and except was made to reject the errors given by the ais decode, if some of the data is coming out in the wrong format from the usb.
				body= newline[5]
        			pad= int(newline[6][0]) ###body and pad are required by the ais decoding function.

              			msg= ais.decode(body,pad)  #decodes and output the data relevant to the vessels around, outputs a dictionary type with relevant information
                		print msg

		        except:
				print 'AIS decoding error'		
		                pass

			

#Getting initial location from position message using the library_highlevel.py functions
		        current_x = self.__controller.getX()
			current_y = self.__controller.getY()
        		vessel_x = msg['x']
			vessel_y = msg['y']
			delta_x = current_x - vessel_x
			delta_y = current_y - vessel_y
			distance = sqrt ((delta_x ** 2)+(delta_y **2))
			current_speed = self.__controller.getspeed()

			reaction_distance= 3/ current_speed  ###this is the reaction distance, defined in miles, available for the ASV to manouver away to avoid collision, it is based on the maximum speed of the vessel. it is a function of the current speed of the vessel, as the vessel goes slower is required to be greater as less manouvering capabilities are available. 

#####The next part of the function tryes to minimise the CPU time by sleeping the function depending on the number of messages recieved from vessels within the reaction distance. Then publishes the data

			if distance < reaction_distance:
				pub.publish(AIS_message = msg)
				counter += 1
			else:
				print 'read error'
				pass


			if time.time()-time_zero > maximum_sleep_ais :
				counter = 1
				sleep (1)
			elif counter < 3
				sleep(1)
			else:
				sleep(0.1)

################################################################################
####Shut down function###
###############################################################################				

def shutdown():
    serialPort.flushInput()
    serialPort.flushOutput()
    pubStatus.publish(nodeID = 3, status = False)
    serialPort.close()


################################################################################
#### Initialise ####
###############################################################################

if __name__ == '__main__':

    time.sleep(1) #Allow System to come Online    
    rospy.init_node('ASV_ais')
    
    global pub
    global serialPort
    
    ####Setting up the publisher####
    pub = rospy.Publisher('AIS_message', ais_data)   
    pubStatus = rospy.Publisher('status', status)
    
    rospy.on_shutdown(shutdown)  
    
    port_status = setUpSerial()
    str = "AIS port status = %s. Port = %s" %(port_status, serialPort.portstr)
    rospy.loginfo(str)
    time.sleep(0.3)
    
    if  port_status == True:    
        status = True
        #Publishing the status of the node
        pubStatus.publish(nodeID = 3, status = status)
        rospy.loginfo("AIS is online")
    else:
        #Publishing the status of the node
        status = False
        pubStatus.publish(nodeID = 3, status = status)
      
    
    listenForData(status)   #Main loop for receiving data
    


	

