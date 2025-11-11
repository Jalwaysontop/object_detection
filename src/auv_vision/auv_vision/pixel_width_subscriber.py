import rclpy
from std_msgs.msg import Int32,Float32
import yaml
import os
from rclpy.node import Node


class Pixel_avg(Node):
    def __init__(self):
        super().__init__("pixel_width_subscriber")
        self.subscriber=self.create_subscription(Int32,'int_width',self.callback,10)
        self.pixel_list=[]
        self.pixel_sum=0    
    def callback(self,width_msg):
        width=width_msg.data
        if(len(self.pixel_list)>=50):
            pixel_avg=self.pixel_sum/len(self.pixel_list)
            self.get_logger().info(f"P_avg={pixel_avg:.2f}")
            confi_data={
                'calibration':{
                    'P_avg':pixel_avg,
                    'box_object_width_cm':17.9,
                    'known_distance_cm':50
                }
            }
            os.makedirs('config',exist_ok=True)
            with open('config/pixel_focal_length.yaml','w') as f:
                yaml.dump(confi_data,f)
            self.get_logger().info("Saved the data in config/focal_length.yaml")
            self.destroy_node()
            rclpy.shutdown()
        self.pixel_list.append(width)
        self.pixel_sum+=width

def main():
    rclpy.init()
    node=Pixel_avg()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    
if __name__=='__main__':
    main()       
