import cv2 as cv
import numpy as np
import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge
from std_msgs.msg import Int32
import numpy as np

class operations(Node):
    def __init__(self):
        super().__init__("operations_node")
        self.op_subscriber=self.create_subscription(Image,"ImageRaw",self.op_callback,10)
        self.width_pub=self.create_publisher(Int32,"int_width",10)
        self.bridge=CvBridge()
    def op_callback(self,Image_msg):
        frame=self.bridge.imgmsg_to_cv2(Image_msg,desired_encoding='bgr8')
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        lower_blue = np.array([100, 150, 0])
        upper_blue = np.array([140, 255, 255])
        mask=cv.inRange(hsv,lower_blue,upper_blue)
        contours,hierarchy=cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        if contours:
            maxcontour=max(contours,key=cv.contourArea)
            x,y,w,h=cv.boundingRect(maxcontour)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            self.get_logger().info(f"Found pixel width{w}")
            width=Int32()
            width.data=w
            self.width_pub.publish(width)
        cv.imshow("video",frame)
        cv.waitKey(1)
def main():
    rclpy.init()
    node=operations()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    cv.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()

