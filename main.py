
import cv2 as cv
import numpy as np
# from cv_bridge import CvBridge

from image_io import ImageIO


def depth_clbck(depth_msg):

    # bridge = CvBridge()
    # image = bridge.imgmsg_to_cv2(depth_msg,"32FC1")
    image = depth_msg
    depth_array = np.array(image, dtype=np.float32)
    
    # print(depth_array.shape)
    
    depth_colormap = cv.applyColorMap(cv.convertScaleAbs(image, alpha=0.05), cv.COLORMAP_HSV)

    cv.imshow('image', np.array(depth_colormap))
    cv.waitKey()


# print(1)

reader = ImageIO("reference_images")

# samp = cv.imread("reference_images/so_sample_image.jpg")
# cv.imshow("image", samp)
# cv.waitKey()
depth_clbck(reader.read_image("so_sample_image.jpg"))
