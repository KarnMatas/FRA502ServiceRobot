from math import sin, cos, pi
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from geometry_msgs.msg import Quaternion
from sensor_msgs.msg import JointState
from tf2_ros import TransformBroadcaster, TransformStamped

class StatePublisher(Node):
	def __init__(self):
		super().__init__('statePublisher')
		self.joint_pub = self.create_publisher(JointState, 'joint_states', 10)
		timer_period = 0.5
		self.timer = self.create_timer(timer_period, self.timer_callback)
		loop_rate = self.create_rate(30)
       
	def timer_callback(self):
		joint_state = JointState()
		try:
			while rclpy.ok():
				rclpy.spin_once(self)
				
				# update joint_state
				now = self.get_clock().now()
				joint_state.header.stamp = now.to_msg()
				joint_state.name = ['lrod_joint', 'lsphere_joint','rrod_joint','rsphere_joint','left_wheel_joint'
				,'right_wheel_joint','sphere_wheel_joint','imu_joint','camera_joint','laser_joint']
				joint_state.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
				self.joint_pub.publish(joint_state)
				loop_rate.sleep()
		except KeyboardInterrupt:
            		 pass
def main():
    rclpy.init()
    statePublisher = StatePublisher()
    self.sleep(2)
    rclpy.spin(statePublisher)
    
    
if __name__ == '__main__':
    main()
