from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load your video file
video = VideoFileClip("input_video.mp4")

# Define the start and end times for the slices (in seconds)
# For example, slice 1 from 10s to 20s, slice 2 from 40s to 50s
clip1 = video.subclip("00:00:00", "00:00:20")  # Slice from 0:00:00 to 0:00:20
clip2 = video.subclip("00:00:40", "00:00:50")  # Slice from 0:00:40 to 0:00:50
clip3 = video.subclip("00:01:00", "00:01:10")  # Slice from 0:01:00 to 0:01:10
clip4 = video.subclip("00:01:20", "00:01:30")  # Slice from 0:01:20 to 0:01:30

# Combine the slices into a single video
final_clip = concatenate_videoclips([clip1, clip2, clip3, clip4])

# Write the result to a file
final_clip.write_videofile("output_video.mp4", codec="libx264")
