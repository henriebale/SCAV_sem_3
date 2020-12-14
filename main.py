import os, sys, subprocess, shlex, re
from subprocess import call

def conversion ():
    #convert to vp8
    os.system("ffmpeg -i BBB_video_120.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_video_120_vp8.webm")
    os.system("ffmpeg -i BBB_video_240.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_video_240_vp8.webm")
    os.system("ffmpeg -i BBB_video_480.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_video_480_vp8.webm")
    os.system("ffmpeg -i BBB_video_720.mp4 -c:v libvpx -b:v 1M -c:a libvorbis BBB_video_720_vp8.webm")

    #convert to vp9
    os.system("ffmpeg -i BBB_video_120.mp4 -c:v libvpx-vp9 -b:v 2M BBB_video_120_vp9.webm")
    os.system("ffmpeg -i BBB_video_240.mp4 -c:v libvpx-vp9 -b:v 2M BBB_video_240_vp9.webm")
    os.system("ffmpeg -i BBB_video_480.mp4 -c:v libvpx-vp9 -b:v 2M BBB_video_480_vp9.webm")
    os.system("ffmpeg -i BBB_video_720.mp4 -c:v libvpx-vp9 -b:v 2M BBB_video_720_vp9.webm")

    #convert to h265
    os.system("ffmpeg -i BBB_video_120.mp4 -c:v libx265 -c:a aac -b:a 128k BBB_video_120_h265.mp4")
    os.system("ffmpeg -i BBB_video_240.mp4 -c:v libx265 -c:a aac -b:a 128k BBB_video_240_h265.mp4")
    os.system("ffmpeg -i BBB_video_480.mp4 -c:v libx265 -c:a aac -b:a 128k BBB_video_480_h265.mp4")
    os.system("ffmpeg -i BBB_video_720.mp4 -c:v libx265 -c:a aac -b:a 128k BBB_video_720_h265.mp4")

    #convert to av1
    os.system("ffmpeg -i BBB_video_120.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental BBB_video_120_av1.mkv")
    os.system("ffmpeg -i BBB_video_240.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental BBB_video_240_av1.mkv")
    os.system("ffmpeg -i BBB_video_480.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental BBB_video_480_av1.mkv")
    os.system("ffmpeg -i BBB_video_720.mp4 -c:v libaom-av1 -crf 30 -b:v 0 -strict experimental BBB_video_720_av1.mkv")


ex="1"
while ex != "0":
    print("Exercice Nº (insert 0 to end)")
    ex=input()
    print(f"Exercise {ex} selected")
    if ex=="1":
        conversion()

    elif ex=="2":
        #h265 mosaic
        os.system('ffmpeg -i BBB_video_120_h265.mp4 -i BBB_video_240_h265.mp4 -i BBB_video_480_h265.mp4 -i BBB_video_720_h265.mp4 -filter_complex "nullsrc=size=640x480 [base]; [0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; [base][upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 [tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" mosaic_h265.mp4')
        #vp8 mosaic
        os.system('ffmpeg -i BBB_video_120_vp8.webm -i BBB_video_240_vp8.webm -i BBB_video_480_vp8.webm -i BBB_video_720_vp8.webm -filter_complex "nullsrc=size=640x480 [base]; [0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; [base][upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 [tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" mosaic_vp8.webm')
        #vp9 mosaic
        os.system('ffmpeg -i BBB_video_120_vp9.webm -i BBB_video_240_vp9.webm -i BBB_video_480_vp9.webm -i BBB_video_720_vp9.webm -filter_complex "nullsrc=size=640x480 [base]; [0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; [base][upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 [tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" mosaic_vp9.webm')
        #av1 mosaic
        os.system('ffmpeg -i BBB_video_120_av1.mkv -i BBB_video_240_av1.mkv -i BBB_video_480_av1.mkv -i BBB_video_720_av1.mkv -filter_complex "nullsrc=size=640x480 [base]; [0:v] setpts=PTS-STARTPTS, scale=320x240 [upperleft]; [1:v] setpts=PTS-STARTPTS, scale=320x240 [upperright]; [2:v] setpts=PTS-STARTPTS, scale=320x240 [lowerleft]; [3:v] setpts=PTS-STARTPTS, scale=320x240 [lowerright]; [base][upperleft] overlay=shortest=1 [tmp1]; [tmp1][upperright] overlay=shortest=1:x=320 [tmp2]; [tmp2][lowerleft] overlay=shortest=1:y=240 [tmp3]; [tmp3][lowerright] overlay=shortest=1:x=320:y=240" mosaic_av1.mkv')
    elif ex=="3":+
        #Command used to stream the BBB video to the IP 192.168.0.35 using the port 23000.
        os.system('ffmpeg -re -i BBB_video.mp4 - qscale 0 -f mpegts "udp://192.168.0.35:23000"')
        # To see the streaing video input this command in a new terminal window: ffplay udp://192.168.0.35:23000

    else:
        print(f"Exercise {ex} doesn't exiat")



