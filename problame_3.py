import pyttsx4

engine = pyttsx4.init()
engine.save_to_file('i am Hello World, i am a programmer. i think life is short.', 'test1.wav')
engine.runAndWait()
