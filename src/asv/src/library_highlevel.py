#!/usr/bin/python
##############################################################################
#library_highlevel.py
#
#Initial code is a simplified subset of library_highlevel.py from DelphinROSv2
#Code by Dr Alexander Brian Phillips, Leo Steenson and Catherine Harris
#
#Revisited and corrected by Enrico Anderlini (ea3g09@soton.ac.uk).
#
#Modifications to code
# 21/11/2012	Modified code for ASV	ABP
# 03/02/2013    Corrected subscribers/publishers names in accordance with their 
#               variables in the other nodes
# 13/02/2013    Changing subscribers and publishers names and adding some
#               subscribers in order to work with the arduinos
# 14/02/2013    Modifying setter and getter functions
# 16/02/2013    Finalisation and test of the node
# 21/03/2013    Had to modify some variable names     
#
##############################################################################
#Notes
#
#This code contains the background coding required to provide get and set functions for
#the other high level code to use
#
#The arduino status may create problems 
#
##############################################################################
import roslib; roslib.load_manifest('asv')
import rospy
import numpy
import math
import time
import re

#import message types for publishing:
from std_msgs.msg import Float32
from std_msgs.msg import Bool
from std_msgs.msg import Int8
from std_msgs.msg import String

#import message types for subscribing:
from asv.msg import compass
from asv.msg import position
from asv.msg import status



class library_highlevel:
# library class for high-level controller.  Defines the inputs, output and basic functionality that
# all high-level controllers should inherit.
	

    def __init__(self):
        #constructor method - creates objects of type 'HighLevelController'
        
        #set up publishers (stored as object variables)

        self.pub_speed_demand              = rospy.Publisher('speed_demand', FLoat32) 
        self.pub_heading_demand            = rospy.Publisher('heading_demand', Float32) 
        self.Mission_pub                   = rospy.Publisher('MissionStrings', String)
        self.pub_heading_control_onOff     = rospy.Publisher('Heading_onOFF', Bool)             #turns heading controller on and off
        self.pub_rudder_demand   	   = rospy.Publisher('rudder_demand', Float32)



        
        #set up subscribers
        rospy.Subscriber('compass_out', compass, self.callback_compass)                         
        rospy.Subscriber('position', position, self.callback_position)                     		
        rospy.Subscriber('back_seat_flag', Int8, self.callback_back_seat_flag)
	#rospy.Subscriber('obj_avoid_correction', XY....			     ###NEEDS TO REF TO THE AIS PROCESSING NODE
        #rospy.Subscriber('motor_voltage', Float32, self.callback_motor_voltage)  
        #rospy.Subscriber('motor_current', Float32, self.callback_motor_current)  
        #rospy.Subscriber('motor_power', Float32, self.callback_motor_power)  
        #rospy.Subscriber('battery_voltage', Float32, self.callback_battery_voltage)

	    
        #initilise empty object variables to hold latest data from subscribers
        ######### might need to set default values in message files-not done
        self.__compass = compass()
        self.__position = position()

        self.__back_seat_flag  = 0 #back_seat_flag is 0 when no errors are present
        #self.__BatteryVoltage   = 0      
        self.__gps_status      = 0
        self.__compass_status  = 0
        #self.__arduino_status  = 0
        #self.__arduino_warning = 0
        #self.__water_detected  = 0
        #self.__bilge_pump      = 0
        self.__rudder_angle    = 0.0
        self.__motor_rpm        = 0.0   
        #self.__motor_voltage   = 0
        #self.__motor_current   = 0
        #self.__motor_power     = 0
        #self.__motor_method    = 0
        #self.__motor_target    = 0
        #self.__motor_dutycycle = 0
        #self.__CaseTemperature= 0           ###need to buy a sensor
        

	#Below are the various functions that can be called by the mission control node
	###############################################################################



    # stops vehicle and shuts down ROS
    def stop(self):
        str="Stop method invoked - ROS will shut down in 1 second"
        rospy.logfatal(str)
        self.setMotorRPM(0)
        self.setRudderAngle(0)
        time.sleep(1)
        rospy.logfatal("Shutting down")
        self.Mission_pub.publish('Shutting Down')
        rospy.signal_shutdown('mission finished')
	###need to change this function so that it set the system to restart in case something goes bad
        
    ##The following are the "setter" functions->publishers##
    
    # sets the motor operating mode: 1 for duty cycle, 2 for motor voltage,
    #3 for propeller rpm, 4 for motor power 
    #def setMotorSetting(self, demand):
        #str = "Setting motor operating mode %s" %demand			
        #rospy.loginfo(str)
        #self.pub_motor_setting.publish(demand)
        #NOT NEEDED ATM

    # sets a 'demand' for the motor power (percentage)
    #def setMotorPower(self, demand):
     #   str = "Setting motor power %s" %demand			
       # rospy.loginfo(str)
      #  self.setMotorSetting(4)             #see arduino
        #self.pub_motor_target.publish(demand)
    
    def setMotorRPM(self, demand):
        str = "Motor RPM demand %.3f deg" %demand
        rospy.loginfo(str)
        #publish rear rudder_demand
        self.switchHeadingOnOff(0)
        self.pub_rudder_demand.publish(demand)

    # set a 'demand' (in degrees) for the rudder angle
    def setRudderAngle(self, demand):
        str = "Ruddder demand %.3f deg" %demand
        rospy.loginfo(str)
        #publish rear rudder_demand
        self.switchHeadingOnOff(0)
        self.pub_rudder_demand.publish(demand)


    # move to heading 'demand' (degrees)
    def setHeading(self, demand):
        #publish headingDemand
        cur_heading=self.getHeading()
        str = "Setting heading demand %.3f deg, current heading %.3f deg" %(demand, cur_heading)
        rospy.loginfo(str)
        self.switchHeadingOnOff(1)					#Turn on Heading control
        self.pub_heading_demand.publish(demand)

    # change heading by 'headingChange' (degrees)
    def changeHeadingBy(self, headingChange):
        self.setHeading(self.__compass.heading + headingChange)


    # switch heading controller on or off {1,0}
    def switchHeadingOnOff(self,onOff):
        if onOff ==1:
            self.pub_heading_control_onOff.publish(1)
            str = "Switch Heading Control ON"
            rospy.logdebug(str)	 
        else:
            self.pub_heading_control_onOff.publish(0)
            str = "Switch Heading Control OFF"
            rospy.logdebug(str)	 

    #################################################
    ## "Getter" methods->subscribers##    
    
    def getHeading(self):
        return self.__compass.heading
    
    def getRoll(self):
        return self.__compass.roll
    
    def getPitch(self):
        return self.__compass.pitch
    
    def getTemperature(self):
        return self.__compass.temperature
    
   
    # magnetometer
    def getM(self):
        return self.__compass.m
    
    def getMx(self):
        return self.__compass.mx
    
    def getMy(self):
        return self.__compass.my
    
    def getMz(self):
        return self.__compass.mz
    
    # accelerometer
    def getA(self):
        return self.__compass.a
    
    def getAx(self):
        return self.__compass.ax
    
    def getAy(self):
        return self.__compass.ay
    
    def getAz(self):
        return self.__compass.az

    # get position values                         
    def getX(self):
        return self.__position.X

    def getY(self):
        return self.__position.Y
    
    def getGPSValidFix(self):
        return self.__position.ValidGPSfix    

    
    def getBackSeatErrorFlag(self):
        return self.__back_seat_flag

	# get status
    def getGPSStatus(self):
        return self.__gps_status
    
    def getCompassStatus(self):
        return self.__compass_status


     # get battery voltage

   # def getBatteryVoltage(self):
    #    return self.__BatteryVoltage
    
 
    #################################################
    # Callbacks
    #################################################

    def callback_compass(self, compass_data):
           self.__compass = compass_data
    
    def callback_position(self, position):
           self.__position = position   
                   
    def callback_back_seat_flag(self, back_seat_flag):
           self.__back_seat_flag = back_seat_flag.data      
    
    # The following function can have problems with the arduino status
    
    def callback_status(self, status):
            if status.nodeID == 3:
                self.__obj_avoid_status = status.status
                return
            elif status.nodeID == 1:
                self.__gps_status = status.status
                return
            elif status.nodeID == 2:
                self.__compass_status = status.status
                return
	    elif status.nodeID == 4:
		self.__motor_interface_status == status.status
		return
	    elif status.nodeID == 5:
		self.__rudder_interface_status == status.status
		return

            
  
