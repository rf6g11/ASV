#!/usr/bin/python
##############################################################################
#compass.py
#
#Initial code is a simplified subset of compass_oceanserver.py from DelphinROSv2
#Code by Dr Alexander Brian Phillips, Leo Steenson and Catherine Harris
#Code modified and adapted for use in ASV package by Enrico Anderlini 
#(ea3g09@soton.ac.uk).
#
#
#Modifications to code
#11/12/2012  in order to account for correct installation in ASV BP. All 
#modifications are marked with ##
#04/02/2013  extensive comments added
#06/02/2013  calibration function removed and simplification of the code
#            after calibration of the compass (by Dr Alexander Brian Phillips).
#05/03/2013  io settings removed and changed with serial.Serial and readline().
#            Now code works fine. 
#
#05/02/2015 Code changed to be used by a BBB for the ASV transatlantic
#
##############################################################################
#Notes
#
#This code publishes the compass readings to node ID 5. This code is designed 
#to operate with an Ocean Server compass.
#
#NOTES: For Python v2.6+, the eol parameter for readline() is no longer 
#supported! This required some changes to the code by Dr Alexander Brian 
#Phillips. For more information on this issue see: 
#http://pyserial.sourceforge.net/shortintro.html . However, for clarity these
#changes have also been commented with double ## as above. This has been changed
#by Enrico Anderlini, as the program read the data only once. Now problem has
#been fixed.
#
#The calibration of the compass has been performed according to the guide, since
#it is going to be installed in the correct orientantion. More information
#on this process is to be found at page 17 of the OS5000 family guide that
#can be downloaded from http://www.oceanserver-store.com/compass.html.
#This process is to be performed in  Cutecom, which is in hexadecimal language.
#Therefore, for calibration on a level plate, the required commands are:
#ascii           hexadecimal
#Esc + C  -->    1B + 43
#Tab      -->     20                  to move to the other commmand
#For caliration of the rolled sensor:
#Esc + Z  -->    1B + 5A
#Tab      -->     20                  to move to the other commmand
#
##############################################################################
import roslib; roslib.load_manifest('asv')    ##
import rospy
import numpy
import time
import math
from re import findall
from asv.msg import compass                   
from asv.msg import status
from bbio import *                    
global serialPort


################################################################
#The following function sets up and opens the serial port of the compass.
#This port has been set in the udev local rules of the computer in the file
#/etc/udev/rules.d/10-local.rules as /dev/usbcompass.
def setUpSerial():
    global serialPort
	try:
	   serialPort = Wire2.begin()
           Wire2.write(0x1e,2,1)
    
           print "Initialised OceanServer serial."
	   return True
        except:
           return False
           
#    print serialPort.portstr
#    print serialPort.isOpen()
#    serialPort.flushInput()
#    serialPort.flushOutput()
#    return serialPort.isOpen()
    
    
################################################################
#The following function reads the data being published by the serial port.
def listenForData(status):
    global serialPort
    
    time_zero = time.time()
    time_out= 5 
    
    
    while not rospy.is_shutdown():    
        try:
            time.sleep(0.01)  # Prevents node from using 100% CPU!!

            while time.time()-time_zero<time_out:  

                data = Wire2.read(0x1e, 0, 10)

                pubStatus.publish(nodeID = 2, status = status)
               
              
                try:

                    dt = time.time() - time_zero
                    #print data
                    time_zero = time.time()
                    
                    heading     = data[4]
                    pitch       = data[6]
                    roll        = data[8]    
 
                    
                    #The following print statements should be left uncommented only during debugging                    
#                    print '*******'
                    print 'heading %f' %(heading)
                    print 'pitch  %f' %(pitch)
                    print 'roll %f' %(roll)

     
                    #Publish data to compass_out
                    pub.publish(heading=heading,pitch=pitch,roll=roll)
                    
                except ValueError: 
                    print 'not a float'
                
        except:
            print 'read error'
        

################################################################
#Shut down function, which closes the serial port
def shutdown():
    Wire2.end()
    pubStatus.publish(nodeID = 2, status = False)
    

################################################################        
#     INITIALISE     ###########################################
################################################################

if __name__ == '__main__':
    time.sleep(1) #Allow System to come Online    
    rospy.init_node('OceanServer_compass')
    
    global pub
    global serialPort
    
    ####Setting up the publisher####
    pub = rospy.Publisher('compass_out', compass)   
    pubStatus = rospy.Publisher('status', status)
    
    rospy.on_shutdown(shutdown)  
    
    port_status = setUpSerial()
    str = "Compass port status = %s. Port = Wire2" %(port_status)
    rospy.loginfo(str)
    time.sleep(0.3)
    
    if  port_status == True:    
        status = True
        #Publishing the status of the node
        pubStatus.publish(nodeID = 2, status = status)
        rospy.loginfo("Compass is online")
    else:
        #Publishing the status of the node
        status = False
        pubStatus.publish(nodeID = 2, status = status)
      
    
    listenForData(status)   #Main loop for receiving data
    
    
