#!/usr/bin/env python
##############################################################################
#state_bollard.py
#
# 1o/3/2014 bollard pull code was created to check battery discharge and calibrate the thrust block.
#
#
#Modifications to code
# 21/11/2012	Modified code for ASV	ABP
#
#
#
##############################################################################
#Notes
#
#This code contains the code for the Bollard Pull state.
#
##############################################################################
import roslib; roslib.load_manifest('asv')
import rospy
import smach
import smach_ros
import time
from std_msgs.msg import String

#################smach state Bollard (defined in mission_script.py)################
class Bollard(smach.State):
	def __init__(self, lib, rpm, timeout):
		smach.State.__init__(self, outcomes=['succeeded','aborted','preempted'])
                self.__controller = lib
                self.__rpm = rpm
                self.__timeout = timeout
                   		
	def execute(self,userdata):
                global pub
                #Set Up Publisher for Mission Control Log
                pub = rospy.Publisher('MissionStrings', String)               
                str= 'ASV Bollard state started at time = %s' %(time.time())
                pub.publish(str)

                #Set the rpm to the required value               
                self.__controller.setProp(self.__rpm)

                time_zero = time.time()

                while not rospy.is_shutdown() and (time.time()-time_zero) < self.__timeout and self.__controller.getBackSeatErrorFlag() == 0:
                        pass

                if self.__controller.getBackSeatErrorFlag() == 1:
                        rospy.logerr("BackSeatDriver Identified Fault") 
                        str = 'Backseat Driver Identified Fault Bollard State preempted'
                        pub.publish(str)
                        return 'preempted'
                elif (time.time()-time_zero) > self.__timeout:
                        rospy.logerr("Bollard state completed required time")  
                        str='Bollard state completed required time'
                        pub.publish(str)              
                        return 'succeeded'
                else:
                        return 'aborted'

