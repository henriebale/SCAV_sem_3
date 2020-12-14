# SCAV_sem_3

Input the exercise nº you want to execute. When 0 is input it ends the script.

Ex2:

h265 has the most consistent output regardless of the bitrate, but this means that the higher quality videos do not differ a lot in detail compared to the low quality ones.
In contrast, vp8 and vp9 perform better at high bitrate having more detail in the image but as we lower the bitrate the loss in detail is harder than in h265.
I couldn't make av1 conversion work so I can't analyze how it works at each bitrate. The code should work regardless it was a problem of libraries and ffmpeg.


Ex3:
In order to see the streamed video you need to input ffplay udp://192.168.0.35:23000 in another terminal window. 
