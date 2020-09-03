import cv2
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--videopath',type=str, default='../hook_helmet_dataset/HookHelmet_test8.mp4', help='mp4 path')
    parser.add_argument('--output', type=str, default='../hook_helmet_dataset/test8/', help='output file path')  # output folder
    opt = parser.parse_args()
vidcap = cv2.VideoCapture(opt.videopath)
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite(f"{opt.output}/frame{count}.jpg", image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1