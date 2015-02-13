#!/usr/bin/python
##############################################################################
#arduino.py
#
#Code created by alex phillips to talk to the arduino boards on the asv
#
#Modifications to code
# 11/03/2013 Code created
#
##############################################################################
#Notes
#
#
#
##############################################################################

import roslib; roslib.load_manifest('asv')
import rospy
import serial
import time
import numpy
from re import findall
from re import search
from std_msgs.msg import Float32
from std_msgs.msg import Int8
from std_msgs.msg import Bool
from asv.msg import status


global serialPort
global rudderdemand
global setmotorsetting
global setmotortarget



################################################################
#The following function sets up and opens the serial port of the compass.
#This port has been set in the udev local rules of the computer in the file
#/etc/udev/rules.d/10-local.rules as /dev/usbcompass.
def setUpSerial():
    global serialPort
    
    #Specifying the serial port to be opened
    serialPort = serial.Serial(port='/dev/usbarduino', baudrate='19200', timeout=0.01) # may need to change timeout if having issues!
    serialPort.bytesize = serial.EIGHTBITS
    serialPort.stopbits = serial.STOPBITS_ONE
    serialPort.parity = serial.PARITY_NONE
    
    print "Initialised arduino"
    print serialPort.portstr
    print serialPort.isOpen()
    serialPort.flushInput()
    serialPort.flushOutput()
    return serialPort.isOpen()



################################################################
#The following function reads the data being published by the serial port.
def listenForData(status):
    global serialPort
    global rudderdemand
    global setmotorsetting
    global setmotortarget
    time_zero = time.time()
    print "entered listen for data"
    
    rudderdemand=0
    setmotorsetting=0
    setmotortarget=0
    
    #####################   
    
    
    while not rospy.is_shutdown():    
        try:
            time.sleep(0.02)  # Prevents node from using 100% CPU!!
            #serialPort.flushInput()
            #serialPort.flushOutput()
            
          
            
            str="R%4.2f M%3.2f T%i"%(rudderdemand, setmotortarget, setmotorsetting)
            #print str
            serialPort.write(str) 
            
            if serialPort.inWaiting() > 0 :     #while there is data to be read - read the line...
                dataRaw = serialPort.readline()
                #print dataRaw
                if dataRaw[0]=="$":
                    #print "data recieved"
                    try:   
                        data = numpy.array(findall('p1=(\d+) p2=(\d+) p3=([-]*\d+.\d+) p4=([-]*\d+.\d+) p5=([-]*\d+.\d+) p6=([-]*\d+.\d+) p7=(\d+) p8=([-]*\d+.\d+) p9=([-]*\d+.\d+) p10=([-]*\d+.\d+) p11=([-]*\d+.\d+) p12=([-]*\d+.\d+) p13=([-]*\d+.\d+) p14=([-]*\d+.\d+)',dataRaw), numpy.float32)

                        #print data
                        
                        
                	error.publish(int(data[0,0]))
    			warning.publish(int(data[0,1]))
    			batteryvoltage.publish(float(data[0,2]))
    			casetemperature.publish(float(data[0,3]))
    			ruddertarget.publish(float(data[0,4]))
    			rudderangle.publish(float(data[0,5]))
    			motorsetting.publish(int(data[0,6]))
    			motortarget.publish(float(data[0,7]))
    			dutycycle.publish(float(data[0,8]))
    			proprpm.publish(float(data[0,9]))
    			motorvoltage.publish(float(data[0,10]))
    			motorcurrent.publish(float(data[0,11]))
    			motorpower.publish(float(data[0,12]))
                        thrust.publish(float(data[0,13]))                        
                    except:
                        print "format wrong"
        except:
            pass
    
        

def validDataCheck():
    attempts = 1
    
    while attempts < 5:
        
        while not serialPort.read(1) == '$':
            pass
        #The following line has been left for clarity of the change required with new Python versions
        #dataRaw = serialPort.readline(size = None, eol = '\n')   #This line MUST be left commented!
        #The following line contains the actual change required with Python v2.6+; the command reads in line of the data
        dataRaw = serialPort.readline()  #serialIO.readline()
        data=findall('p1=(\d+) p2=(\d+) p3=([-]*\d+.\d+) p4=([-]*\d+.\d+) p5=([-]*\d+.\d+) p6=([-]*\d+.\d+) p7=(\d+) p8=([-]*\d+.\d+) p9=([-]*\d+.\d+) p10=([-]*\d+.\d+) p11=([-]*\d+.\d+) p12=([-]*\d+.\d+) p13=([-]*\d+.\d+) p14=([-]*\d+.\d+)',dataRaw)
        print data
        if len(data) == 1:
            return True
    
    return False

#Shut down function, which closes the serial port
def shutdown():
    global serialPort
    serialPort.flushInput()
    serialPort.flushOutput()
    RudderAngle=0
    RPM=0
    MotorMethod=0
         
            
    str="R%4.2f M%3.2f T%i"%(RudderAngle, RPM, MotorMethod)
    serialPort.write(str)
    time.sleep(1)
    serialPort.write(str) 
    pubStatus.publish(nodeID = 20, status = False) #will need to change node ids
    serialPort.close()


################# Setting up callback functions for subscribers ###############

def rudderd_cb (rudderD):
    global rudderdemand
    rudderdemand = rudderD.data

def setting_cb (MotorS):
    global setmotorsetting
    setmotorsetting = MotorS.data

def target_cb (MotorT):
    global setmotortarget
    setmotortarget = MotorT.data
    
####################### Main Loop ########################  
if __name__ == '__main__':

    
    global pub
    global serialPort
    
    rospy.init_node('arduino')
        
    #Publish compass status as true!
    pubStatus = rospy.Publisher('status', status)
        
    ######################## Define Publishers #############################       
    error           = rospy.Publisher('arduino_status', Int8)  #0 running OK, 1 error
    warning         = rospy.Publisher('arduino_warning', Int8)
    batteryvoltage  = rospy.Publisher('battery_voltage', Float32)
    casetemperature = rospy.Publisher('CaseTemperature', Float32)
    ruddertarget    = rospy.Publisher('rudder_target_angle', Float32)
    rudderangle     = rospy.Publisher('rudder_angle', Float32)
    motorsetting    = rospy.Publisher('motor_target_method', Int8)
    motortarget     = rospy.Publisher('motor_target', Float32)
    dutycycle       = rospy.Publisher('MotorDutyCycle', Float32)
    proprpm         = rospy.Publisher('prop_rpm', Float32)
    motorvoltage    = rospy.Publisher('motor_voltage', Float32)
    motorcurrent    = rospy.Publisher('motor_current', Float32)
    motorpower      = rospy.Publisher('motor_power', Float32)
    thrust          = rospy.Publisher('thrust', Float32)

        
    ####################### Define Subscribers #############################       
    rospy.Subscriber('rudder_demand', Float32, rudderd_cb)
    rospy.Subscriber('setMotorTargetMethod', Int8, setting_cb)
    rospy.Subscriber('setMotorTarget', Float32, target_cb)
    
    rospy.on_shutdown(shutdown)  
    
    port_status = setUpSerial()
    str = "Arduino port status = %s. Port = %s" %(port_status, serialPort.portstr)
    rospy.loginfo(str)
    time.sleep(0.3)
    status = True
    #Publishing the status of the node
    pubStatus.publish(nodeID = 20, status = status) #will need to change node id!!!!!!
    rospy.loginfo("arduino online")
     
    print "test"
    listenForData(status)   #Main loop for receiving data
    
    
