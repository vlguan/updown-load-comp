# INCOMPLETE MUST REMOVE OR ADD MORE COMPONENTS TO ALLOW USER TO CHOOSE CAPTION SPEED, CAPTION TYPE
import whisper_timestamped as whisper
import random
from moviepy.editor import *
def create_subtitles(results, videosize):
    subs = []
    textPos = ('center',(videosize)/2)
    # seperates the words from whisper
    for seg in results["segments"]:
        for i,word in enumerate(seg["words"]):
            text = word["text"].upper()
            start = word["start"]
            # print(start)
            end = word["end"]
            dur = end - start
           #text_clip = TextClip(subtitle.text, fontsize=fontsize, font=font, color=color, bg_color = 'black',size=(video_width*3/4, None), method='caption').set_start(start_time).set_duration(duration)
            txt_clip = TextClip(txt=text, fontsize=90, color='white',font='Take-Looks', method='caption', stroke_width=1,stroke_color='black').set_start(start).set_duration(dur)
            # txt_clip.write_videofile('Videos/sub%d.mp4'%i)
            subs.append(txt_clip.set_position(textPos))
    return subs
def main(speedup, adhdBool):
    model = whisper.load_model("medium", device='cpu')
    # ttsAudio = AudioFileClip('audioOutput/fulltts.mp3').fx(vfx.speedx,speedup)
    # if ttsAudio.duration > 60:
    #     print(ttsAudio.duration)
    #     raise ValueError('tts too long skippped')
    ttsAudio=''
    video = VideoFileClip('Videos/FGclip2.mp4')
    audio = whisper.load_audio('Videos/FGclip2.mp4')
    result = whisper.transcribe(model, audio, language='en')
    randInt = random.randint(1,20)
    if adhdBool:
        vid1 = VideoFileClip('Videos/rand15.mp4').set_audio(None)
        # vid2 = VideoFileClip('Videos/rand%d.mp4'%randInt)
        clip = adhdCrop_clip(video, vid1,  (video.duration)*speedup)
    else:
        print("rand%d.mp4 is being clipped"%randInt)
        video = VideoFileClip('Videos/rand%d.mp4'%randInt)
        
        clip = crop_clip(video, (ttsAudio.duration)*speedup)
    w,h = clip.size
    subs = create_subtitles(result,h)
    final = CompositeVideoClip([clip] + subs).fx(vfx.speedx,speedup)
    # final = final.set_audio(ttsAudio)
    return final
    # final.write_videofile('Videos/productTest.mp4')
if __name__ == "__main__":
    main()