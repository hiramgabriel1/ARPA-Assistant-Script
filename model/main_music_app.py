# packages
from pygame import mixer

# modules
from model import songs, controls

def app():
    mixer.init()

    for x in songs.songs:
        print("")
        print("songs available:" + " " + str(x))

    cancion = str(input(""))
    if cancion == str(1):
        mixer.music.load(songs.songs[0])
        mixer.music.set_volume(0.7)
        mixer.music.play()

    elif cancion == str(2):
        mixer.music.load(songs.songs[1])
        mixer.music.set_volume(0.7)
        mixer.music.play()

    elif cancion == str(3):
        mixer.music.load(songs.songs[2])
        mixer.music.set_volume(0.7)
        mixer.music.play()

    elif cancion == str(4):
        mixer.music.load(songs.songs[3])
        mixer.music.set_volume(0.7)
        mixer.music.play()

    while True:
        print(controls)
        opc = input(":")

        if(opc == "p"):
           mixer.music.pause()
        elif(opc == "r"):
            mixer.music.unpause()
        elif(opc == "e"):
            mixer.music.stop()

            for x in songs.songs:
                print("")
                print("songs available:" + " " + str(x))
        
            cancion = str(input(""))
            mixer.music.load(cancion)
            mixer.music.play()

            # cancion = str() 
        elif(opc == "s"):
            exit()        
app()