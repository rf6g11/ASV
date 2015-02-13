#!/usr/bin/python
##############################################################################
#heading_controller.py
#
#Initial code is a simplified subset of heading_controller.py from DelphinROSv2
#Code by Dr Alexander Brian Phillips, Leo Steenson and Catherine Harris
#
#Completed, checked, modified, corrected by Enrico Anderlini (ea3g09@soton.ac.uk)
#
#Modifications to code
# 21/11/2012	Modified code for ASV	ABP
# 03/02/2013    Finished completion and debugging of the  code, including change
#               of the publishers/subscribers names. Extensive comments added.
# 06/04/2013    Gains modified after model testing. Added a subscriber to the 
#               Boolean published by the circle and zigzag manoeuvres.
#
##############################################################################
#Notes
#
#This code is the heading controller for the ASV. When a heading demand is set
#in the states (e.g. state_goToXY), this node subscribes to that value and 
#obtains a rudder angle demand that publishes to the arduino node. The controller
#is a simple PID feedback controller (digital implementation) that employs the
#current heading value from the compass in order to estimate the current error. 
#The values of the PID constants is based on the actual model tests data (from the zigzag
#manoeuvres in fact - see report).
#In this code, only a P controller is implemented.
#
################################################################################
import roslib; roslib.load_manifest('asv')
import rospy
import time
import numpy

from asv.msg import position
#from ASV.msg import headingd          uncomment to read heading demand during debugging
from std_msgs.msg import Float32
from std_msgs.msg import Int8
from std_msgs.msg import Bool

######################### DEFINE GLOBAL VARIABLES ##############################
### General ###
    min_int_error  =-10  ##maximum and minimum integral errors in order to avoid an excessively slackish response.
    max_int_error  = 10  

########################## Rudder PID Controller ###############################
####Setting the Proportional, Integral and Derivative gains####
Pgain      =  0.723  ##These values have been obtained theoretically
Igain	   =  0.0
Dgain	   =  0.0

###IDEALLY NO NEED FOR SPEED MAX OR SPEED MIN but instead use power consumption.

speed_min =  0.5  ###m/s     
speed_max =  1.5  ###m/s

################################################################################
################################################################################

#This function constrains the value of the variable within defined limits-notice the variables order within brackets.
def limits(value, min, max):       
    if value < min:				   
       value = min
    elif value > max:
       value = max
    return value

################################################################################

################################################################################
########## MAIN CONTROL LOOP ###################################################
################################################################################

def main_control_loop():

        ###Defining global variables to be used within the main loop###

    	global speed_demand          ##see comment below in function heading_demand_cb
    	global current_speed
    	global controller_onOff
		
        # The following parameter 
	global manoeuvring
		
        #Initialise parmeters       
        controller_onOff = Bool()
        time_previous    = time.time()    
        speed_request  = 0           
        current_speed  = 0  
        error_previous	 = 0            ##used to simplify the derivative term
	int_error 	 = 0  				##initialization
	manoeuvring  = 0

        #Enter main loop
        while not rospy.is_shutdown():
			
            ## Calculate time since last calculation--Defining delta(t)##
            dt = time.time() - time_previous 
			
            #Calculate speed Error
            error  = speed_request - current_speed

            ### INTEGRAL ###   
            int_error += dt*error	##This has been take from the original code
            # Calculate the integral error 
            int_error =limits(int_error,min_int_error, max_int_error)  #uncomment for faster response.

            ### DERIVATIVE ###
            ##possible problems at the first time-step. A simple finite-difference,  first-order accurate,  backward scheme is used.##
            der_error = (error-error_previous)/ dt     

            time_previous = time.time()          ##This updates the value of time-zero as that of the previous time-step
            error_previous= error	       	     ##This updates the value of the error_zero to that of the previous time-step
                
                
            ############ALGORITHM TO CALCULATE SPEED RESPONSE##############
            Pterm = Pgain * error 
            Iterm = Igain * int_error
            Dterm = Dgain * der_error
                
            motor_rpm=Pterm+Iterm+Dterm   
          
 
                 
            #If Heading control is turned on publish rudder demand
            if controller_onOff:
                pub.publish(motor_rpm)
                
            #The following line is to avoid the node to publish values at too high a rate
            rospy.sleep(0.5)


################################################################################
######## END OF Main Control Loop    ###########################################
################################################################################


################################################################################
#The following functions are used for the correct set up of the subscribers-see
#later in the code. It is fundamental to note that the value within brackets and
#the global value must have different names in order to avoid errors.

def speed_demand_cb(speed_demand):          #During debugging, it may be changed with headingd (a message file)            
    global speed_request                      #So as to avoid error where global and local variables have the same name
    speed_request = speed_demand.data       #During debugging, it may be changed with headingd.heading_demand in conjuction with the line above             

def position_cb(position):
    global current_speed
    current_speed = position.speed

def onOff_cb(onOff):
    global controller_onOff
    controller_onOff=onOff.data  

   
    
################################################################################
def shutdown(args=None):
    # Define an instance of highlevelcontrollibrary to pass to all action servers
    
    #for debugging
    print 'entered shutdown'
    
    lib = library_highlevel()
    
    lib.stop()   

################################################################################
######## INITIALISATION ########################################################
################################################################################

if __name__ == '__main__':
    rospy.init_node('Speed_controller')

    ########################SET UP THE SUBSCRIBERS##############################
    rospy.Subscriber('speed_demand', Float32, speed_demand_cb) 
    rospy.Subscriber('position', position, position_cb)
    rospy.Subscriber('controller_onOFF', Bool, onOff_cb)

    ###########################SET UP THE PUBLISHERS############################
    pub=rospy.Publisher('motor_rpm', Float32)  
    
    ###############Call main_control_loop######################
    rospy.loginfo("Heading controller online")
    main_control_loop()
    
    rospy.on_shutdown(shutdown)
