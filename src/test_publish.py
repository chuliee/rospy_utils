#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def main():
    publisher = rospy.Publisher("/testTopic", String, queue_size = 10)
    rospy.init_node("testNode", anonymous=True)
    rospy.loginfo("Initiated Test Node")
    if not(rospy.is_shutdown()):
        try:
            publisher.publish("Hello, world!")
        except KeyboardInterrupt:
            exit()
    else:
        exit()

if __name__ == "__main__":
    main()