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
global motorRPM
global stop_motor1
#global setmotortarget

motor1_pin= "P9_16"

################################################################
#Set up the pins to send signal to esc

def setUpPWM():
    global PWMport        
    try:
########PWM.start(channel, duty, freqency, polarity)
    	stop_motor1 = PWM.start(motor1_pin, 34, 489) ###Set the frequency and duty cycle so that the engine holds stationary
	global stop_motor1
	print 'Motor number 1 is stopped'
    	return True
    except:
	return False



################################################################
#The following function reads the data being published by the serial port.
def DriveMotor(status):
    global PWMport
    global motorRPM

    time_zero = time.time()		#for watchdog if no new rpm published in last 5s we want to shut motors down
    time_out=5
    
    #####################   
    
    
    while not rospy.is_shutdown():    
        try:
            time.sleep(0.1)  # Prevents node from ustiing 100% CPU

            if time.time()-time_zero<time_out:
####Data found experimentally	
		frequency = 489

		PWM.set_frequency( motor1_pin , frequency)

		rev_duty_cycle_min = 13
		rev_duty_cycle_max = 1

		fwd_duty_cycle_min = 40
		fwd_duty_cycle_max = 60
		
######This translates the data found experimentally in the towing tank into dut cycles

		if motorRPM < -600:
			duty_cycle = rev_duty_cycle_max
		elif -600 < motorRPM < -60 :
			duty_cycle = -0.0211978022 * (motorRPM -606) -1
		elif motorRPM > -60 :
			duty_cycle = rev_duty_cycle_min
		elif 0 < motorRPM < 330:
			duty_cycle = fwd_duty_cycle_min
		elif 330 < motorRPM< 620:
			duty_cycle = (motorRPM - 330) * 0.05952381 + 40
		else :
			duty_cycle = fwd_duty_cycle_max 
		

		PWM.set_duty_cycle(motor1_pin , duty_cycle)
		

	    else:
		motorRPM=0				#initise motorRPM to zero
		stop_motor1 ###Set RPM to zero
            
            #write motor setting to pwm pin

	except:
	    return False
	    pass

	    





#Shut down function, which closes the serial port
def shutdown():
    global PWMport
    global stop_motor1
    stop_motor1
    PWM.stop(motor1_pin)
####PWM.cleanup()
         



################# Setting up callback functions for subscribers ###############

def motorRPM_cb (MotorRPM):
    global motorRPM
    motorRPM = MotorRPM.data

    
####################### Main Loop ########################  
if __name__ == '__main__':

    
    global pub
    global PWMport
    
    rospy.init_node('motor_interface')
        
    ######################## Define Publishers ############################# 
    pubStatus = rospy.Publisher('status', status)
    error           = rospy.Publisher('motor_status', Int8)  #0 running OK, 1 error
        
    ####################### Define Subscribers #############################       
    rospy.Subscriber('motor_rpm', Float32, motorRPM_cb)

    
    rospy.on_shutdown(shutdown)  
    
    port_status = setUpPWM()
    str = "Motor PWM status = %s" %(port_status)
    rospy.loginfo(str)

    time.sleep(0.3)


    #Publishing the status of the node
    pubStatus.publish(nodeID = 4, status = port_status) 
    rospy.loginfo("motor PWM online")
     

    DriveMotor(status)   #Main loop for driving motor
    
    
