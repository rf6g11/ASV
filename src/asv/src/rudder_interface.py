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
import Adafruit_BBIO as PWM
from asv.msg import status
from std_msgs.msg import Float32
#from std_msgs.msg import Int8
#from std_msgs.msg import Bool


global PWMport
global rudderdemand
global center_rudder1
#global setmotortarget

rudder1_pin= "P9_16"

################################################################
#Set up the pins to send signal to esc

def setUpPWM():
    global PWMport        
    try:
    	center_rudder1 = PWM.start(rudder1_pin, 14, 90) ###Set the frequency and duty cycle so that the engine holds stationary
	global center_rudder1
	print 'The rudder number 1 is centered'
    	return True
    except:
	return False



################################################################
#The following function reads the data being published by the serial port.
def RudderAngle(status):
    global PWMport
    global motorRPM

    time_zero = time.time()		#for watchdog if no new rpm published in last 5s we want to shut motors down
    time_out=5
    
    
    
    #####################   
    
    
    while not rospy.is_shutdown(): 
	global rudderdemand
	global center_rudder
   
        try:
            time.sleep(0.1)  # Prevents node from ustiing 100% CPU

            if time.time()-time_zero<time_out:
		frequency = 90
		PWM.set_frequency(rudder1_pin , frequency)

		duty_cycle_min = 7.0
		duty_cycle_max = 21.0
		if rudderdemand < -70 :
			duty_cycle = duty_cycle_min
		elif -70 < rudderdemand < 70 :
			duty_cycle = (rudderdemand - 70)*0.1 + 21
		else:
			duty_cycle = duty_cycle_max

		PWM.set_duty_cycle(rudder1_pin , duty_cycle)
		time_zero = time.time()

		
	    else:
		rudderdemand=0				#initise motorRPM to zero
		center_rudder1 ###Set RPM to zero
            
            #write motor setting to pwm pin

	except:
	    return False
	    pass

	    





#Shut down function, which closes the serial port
def shutdown():
    global PWMport
    global center_rudder1
    center_rudder1
    PWM.stop(rudder1_pin)
####PWM.cleanup()
         



################# Setting up callback functions for subscribers ###############

def ruddderd_cb (MotorRPM):
    global rudderdemand
    rudderdemand = rudderD.data

    
####################### Main Loop ########################  
if __name__ == '__main__':

    
    global pub
    global PWMport
    
    rospy.init_node('rudder_interface')
        
    ######################## Define Publishers ############################# 
    pubStatus = rospy.Publisher('status', status)
    error           = rospy.Publisher('rudder_status', Int8)  #0 running OK, 1 error
        
    ####################### Define Subscribers #############################       
    rospy.Subscriber('rudder_demand', Float32, rudderd_cb)

    
    rospy.on_shutdown(shutdown)  
    
    port_status = setUpPWM()
    str = "Rudder PWM status = %s" %(port_status)
    rospy.loginfo(str)

    time.sleep(0.3)


    #Publishing the status of the node
    pubStatus.publish(nodeID = 5, status = port_status) 
    rospy.loginfo("Rudder PWM online")
     

    RuderAngle(status)   #Main loop for driving motor
    
    
