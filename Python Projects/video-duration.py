import os
import sys
from os.path import isfile, join
from tqdm import tqdm
import time

a = 2


def convert(seconds):
    hours = seconds // 3600
    seconds %= 3600

    mins = seconds // 60
    seconds %= 60

    return hours, mins, seconds


try:
    directory_name = sys.argv[1]

    files = [f for f in os.listdir(directory_name) if isfile(join(directory_name, f))]
    duration = 0

    import moviepy.editor as editor

    for i in tqdm(range(len(files)), desc="Loading..."):
        if files[i].endswith(".mp4"):
            file = join(directory_name, files[i])
            video = editor.VideoFileClip(file)

            video_duration = int(video.duration)
            duration += video_duration
    # duration = convert(duration)
    # print(f"This Directory contains {duration[0]} hours {duration[1]} mins {duration[2]} seconds videos")
    duration = time.strftime("%H:%M:%S", time.gmtime(duration))
    print("*******************")
    print(f"{len(files)} videos of durations {duration} ")
    print()
    print("*******************")

except Exception as e:
    print("Please pass directory name", e)
