#!/usr/bin/python3
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from robot_navigator import BasicNavigator
class Robotgoal(Node):
    point1 = [9.0,5.0,0.0,0.0,0.0,0.0,1.0]
    def __init__(self):
        super().__init__('robotgoal')
        self.publisher_ = self.create_publisher(PoseStamped, 'geometry_msgs', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        navigator = BasicNavigator()
        initial_pose = PoseStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = navigator.get_clock().now().to_msg()
        initial_pose.pose.position.x = 8.0
        initial_pose.pose.position.y = 5.0
        initial_pose.pose.orientation.w = 1.0
        self.publisher_.publish(initial_pose)
        navigator.waitUntilNav2Active()

        goal_pose = PoseStamped()
        goal_pose.header.frame_id = 'map'
        goal_pose.header.stamp = navigator.get_clock().now().to_msg()
        goal_pose.pose.position.x = point1[0]
        goal_pose.pose.position.y = point1[1]
        goal_pose.pose.orientation.w = point1[6]
        navigator.goToPose(goal_pose)

def main(args=None):
    rclpy.init(args=args)

    robotgoal = Robotgoal()

    rclpy.spin(robotgoal)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    robotgoal.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()