import cv2
import glob
import subprocess

files = sorted(glob.glob("*.ppm"))

for idx, filename in enumerate(files):
    img = cv2.imread(filename)
    cv2.imwrite("frames/{0:06d}.png".format(idx), img)

subprocess.call("ffmpeg -i frames/%06d.png -pix_fmt yuv420p video.mp4", shell=True)
