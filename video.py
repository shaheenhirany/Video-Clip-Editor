from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys

# Load your video file
video = VideoFileClip("input_video.mp4")

# Get the duration of the video
video_duration = video.duration

# List to store the slices
clips = []

# Ask the user for the number of slices they want to create
num_slices = int(input("Enter the number of slices you want to create: "))

for i in range(num_slices):
    while True:
        start_time = input(f"Enter the start time for slice {i+1} (in format HH:MM:SS): ")
        end_time = input(f"Enter the end time for slice {i+1} (in format HH:MM:SS): ")
        
        # Convert the start and end times to seconds
        start_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start_time.split(":"))))
        end_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(end_time.split(":"))))
        
        # Check if the start and end times are within the video's duration
        if start_seconds < 0 or end_seconds > video_duration or start_seconds >= end_seconds:
            print(f"Invalid times. Please enter times within the video duration (0 to {video_duration:.2f} seconds).")
        else:
            clip = video.subclip(start_time, end_time)
            clips.append(clip)
            break

# Combine the slices into a single video
if clips:
    final_clip = concatenate_videoclips(clips)

    # Write the result to a file
    final_clip.write_videofile("output_video.mp4", codec="libx264")
    print("Video processing completed successfully.")
else:
    print("No valid slices were provided.")

# Exit the script
print("Exiting the program...(*Powered by Shaheen Hirani & Ali Karim*)")
sys.exit()00:00