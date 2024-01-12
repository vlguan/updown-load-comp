import os
import sys
from moviepy.editor import *
from .tiktokvoicemain.main import tts
# add a feature to append audio file with session id to distingush sever users
def args(text):
    if (text[-1] =="."):
        text = text[:-1]
    sentences = text.split(".")
    return sentences
def main(sentences, voice='en_us_006'):
    # splitup passage into shorter sentences
    sentences = args(sentences)
    audio_files=[]
    # def tts(session_id, text_speaker, req_text, filename, play):
    for sentence in sentences:
        audio_files.append(tts('73782eef66d5ab64bf83342be9623375', voice, sentence)[1])
    audio_clip = concatenate_audioclips([audio for audio in audio_files])
    audio_clip.write_audiofile('tempAud/your_tts.mp3')
if __name__ == "__main__":
    main()