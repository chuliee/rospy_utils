#!/usr/bin/env python

import rospy
import datetime
import requests
from std_msgs.msg import String

def callback_air(data):
    param = data.data.split("|")
    url = 'https://Server:1337/sensor-data-input?robot_id=512345&light={0}&humidity={1}&temperature={2}&co={3}&noise={4}'.format(param[0], param[1], param[2], param[3], param[4])
   
    try:
        request_text = "Requested: " + url
        rospy.loginfo(request_text)
        res = requests.get(url, verify=False)
        if str(res.status_code) == "200":
            rospy.loginfo("Transmission Succeeded: " + str(res.status_code))
        else:
            rospy.loginfo('Verify Result Code: ' + str(res.status_code))
        rospy.loginfo('Result Code: ' + str(res.status_code) + " | " + res.text)
        rospy.loginfo('Waiting for New Dataset ...')
    except (Exception) as error:
        rospy.loginfo('Failed')
        rospy.loginfo(error)

if __name__ == '__main__':		
    # Parameters
    sub_topic = "/data_sensing"
 
    # Initiate ROS node
    rospy.init_node("environment_ros")
    rospy.loginfo('Waiting for New Dataset ...')
    rospy.Subscriber(sub_topic, String, callback_air)
    rospy.spin()