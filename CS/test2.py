














# import pygame

# pygame.mixer.init()

# pygame.mixer.music.load("After_dark.mp3")
# pygame.mixer.music.play()


# print("Music is playing. Press Enter to stop...")
# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10) 

# # Start the music in a new thread
# # threading.Thread(target=play_music, daemon=True).start()













# import librosa as lbr

# #audio initialization
# audio_path = 'After_dark.mp3'
# y, sr=lbr.load(audio_path)

# #no of sample, sampling rate
# print(y.shape,sr)

# duration=len(y)/sr
# print(duration)

# estimated_tempo, beat_indices= lbr.beat.beat_track(y=y,sr=sr)
# beat_time= lbr.frames_to_time(beat_indices,sr=sr)

# print(estimated_tempo)
# print(beat_time)
