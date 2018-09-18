import subprocess
import os

def make_vid(path):
    #for command line
    #ffmpeg -r 1 -i img_%03d.jpg -vcodec mpeg4 -y movie.mp4
    os.chdir(path)
    try:
        code=subprocess.call(['ffmpeg', '-r', '1', '-i', 'img_%03d.jpg', '-vcodec', 'mpeg4', '-y', 'vid.mp4'])
        print ('Video Process: ',code,'\n')
    except Exception as e:
        print "Error occurred in Video formation. "+str(e)
