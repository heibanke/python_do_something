# -*- coding: utf-8 -*-
# comment by heibanke
import cv2

"""
################# 静态图像的输入，输出 ##################
image = cv2.imread('ship.png')
#这里image的维度image.shape = (w,h,3)，
#w*h是图片的长宽，3是BGR等三种颜色的channel值，每个值为0～255
cv2.imwrite('ship.jpg', image)
#灰度图片的颜色channel只有一个，0～255表示灰度值
grayImage = cv2.imread('ship.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
#显示图像
cv2.imshow('test',grayImage)
#捕获键盘输入
k=cv2.waitKey(0)
if k==27:
    cv2.destroyWindow('test')

"""

"""
################# 视频文件的输入，输出 ##################

#读取视频文件
videoCapture = cv2.VideoCapture('test_in.avi')
#设置帧速率30
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
#设置大小为原有图像大小
size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
    int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

#写入到另一个视频文件 
# cv2.VideoWriter(filename, fourcc, fps, frame_size, is_color=true)
# filename – Name of the output video file.
# fourcc – 4-character code of codec used to compress the frames. 
#    For example, CV_FOURCC('P','I','M','1') is a MPEG-1 codec, 
#                 CV_FOURCC('M','J','P','G') is a motion-jpeg codec etc. 
#                 List of codes can be obtained at Video Codecs by http://www.fourcc.org/codecs.php.
# fps – Framerate of the created video stream.
# frameSize – Size of the video frames.
# isColor – If it is not zero, the encoder will expect and encode color frames, 
#    otherwise it will work with grayscale frames (the flag is currently supported on Windows only).
# I420-uncompress avi, XVID-avi
videoWriter = cv2.VideoWriter(
    'test_out.avi', cv2.cv.CV_FOURCC('X','V','I','D'), fps, size)

#一帧一帧读取视频流
success, frame = videoCapture.read()

while success:
    # Loop until there are no more frames.
    videoWriter.write(frame)
    success, frame = videoCapture.read()




"""
################# 摄像头的输入，输出 ##################
def onMouse(event, x, y, flags, param):
    # Event:
    # CV_EVENT_MOUSEMOVE 0                   滑动
    # CV_EVENT_LBUTTONDOWN 1           左键点击
    # CV_EVENT_RBUTTONDOWN 2           右键点击
    # CV_EVENT_MBUTTONDOWN 3           中键点击
    # CV_EVENT_LBUTTONUP 4                 左键放开
    # CV_EVENT_RBUTTONUP 5                 右键放开
    # CV_EVENT_MBUTTONUP 6                 中键放开
    # CV_EVENT_LBUTTONDBLCLK 7         左键双击
    # CV_EVENT_RBUTTONDBLCLK 8         右键双击
    # CV_EVENT_MBUTTONDBLCLK 9         中键双击

    # x,y为鼠标点击位置

    # flags:
    # CV_EVENT_FLAG_LBUTTON 1           左键拖曳
    # CV_EVENT_FLAG_RBUTTON 2           右键拖曳
    # CV_EVENT_FLAG_MBUTTON 4           中键拖曳
    # CV_EVENT_FLAG_CTRLKEY 8     (8~15)按Ctrl不放事件
    # CV_EVENT_FLAG_SHIFTKEY 16   (16~31)按Shift不放事件
    # CV_EVENT_FLAG_ALTKEY 32       (32~39)按Alt不放事件
    
    # param: 自定义编号

    global clicked
    if event == cv2.cv.CV_EVENT_LBUTTONUP:
        clicked = True

clicked = False

#读取摄像头输入
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyCamera')

#绑定鼠标callback
cv2.setMouseCallback('MyCamera', onMouse)
print u'点击窗口或者按任意键退出.'
success, frame = cameraCapture.read()

while cv2.waitKey(1) == -1 and not clicked:
    if frame is not None:
        cv2.imshow('MyCamera', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyCamera')

