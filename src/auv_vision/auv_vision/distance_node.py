import rclpy
from std_msgs.msg import Int32,Float32
from rclpy.node import Node
import yaml
import os

class Distance_calculate(Node):
	def __init__(self):
		super().__init__("distance_calculator")
		self.sub=self.create_subscription(Int32,'int_width',self.callback,10)
		self.pub=self.create_publisher(Float32,'distance',10)
		self.distance=0
	def callback(self,width_msg):
		width=width_msg.data
		config_path='config/pixel_focal_length.yaml'
		if not os.path.exists(config_path):
			self.get_logger().error("config file not found!!")
		with open(config_path,'r') as f:
			data=yaml.load(f,Loader=yaml.SafeLoader)
			p_avg=data['calibration']["P_avg"]
			width_real=data['calibration']['box_object_width_cm']
			f_pixel=data['focal_length_pixel']
			if width==0:
				self.get_logger().warn("Width is 0")
				return
			self.distance=width_real*f_pixel/width
		msg=Float32()
		msg.data=self.distance
		self.pub.publish(msg)
		self.get_logger().info(f'The Distance is:{self.distance:.2f} cm')
def main():
	rclpy.init()
	node=Distance_calculate()
	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		pass
	node.destroy_node()
	rclpy.shutdown()

if __name__=='__main__':
	main()
		
