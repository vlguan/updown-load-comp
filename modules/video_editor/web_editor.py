from moviepy.editor import *
'''
purpose return a sped up clip giving speed_up value
video: the videoclip obj from moviepy
speedup: value at which to speedup by, ie 1.25 = 1.25 the speed of video
'''
def speed_up(video,speedup):
   return video.fx(vfx.speedx, speedup)
'''
purpose is to return a subclip given the duration(tuple)
params:
video: the videoclip obj from moviepy
duration: tuple of timestamps (start, finish)
'''
def create_subclip(video, duration):
   start, finish = duration
   return video.subclip(start,finish)
'''
purpose is to stitch videos together
params:
videoArray: an array of videos you want to attach together, must be an even number of videos
rows: how many rows do you want per video
'''
def adhdCrop_clip(videoArray, rows):
   num_of_video = len(videoArray)
   i=0
   clip_matrix = [[] for _ in range(rows)]
   if num_of_video%2 != 0:
       raise ValueError("The number of inputed Videos must be even for this operation")
   for video in videoArray:
      if len(clip_matrix[i]) == num_of_video/rows:
         i += 1
      clip_matrix[i].append(video)
   print(clip_matrix)
   final_clip = clips_array(clip_matrix)
   return final_clip
# crops one clip to a target
# params:
# video: a clip you desire to crop 
# duration: duration of the subtitle if applies to your needs
# target_aspect_ration: size and ration you desire, default is a story sized video
def crop_clip(video, target_aspect_ratio=(9, 16)):
    # Get video dimensions
   original_width, original_height = video.size

    # Calculate target width based on the aspect ratio
   target_width = int(original_height * target_aspect_ratio[0] / target_aspect_ratio[1])

    # Calculate horizontal and vertical black bars to add
   horizontal_padding = (original_width - target_width) // 2
   vertical_padding = 0  # No vertical padding for centering in this example
   # Apply cropping
   cropped_clip = video.crop(x1=horizontal_padding, x2=original_width - horizontal_padding,
                            y1=vertical_padding, y2=original_height - vertical_padding)
   # Write the result to a new file
   return cropped_clip
if __name__ == "__main__":
   adhdCrop_clip([1,2,3,4,5,6,7,8,9,10], 2)