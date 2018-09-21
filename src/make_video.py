import subprocess
import os

def make_vid(path):
    #for command line
    #ffmpeg -r 1 -i img_%03d.jpg -vcodec mpeg4 -y movie.mp4
    os.chdir(path)
    try:
        code=subprocess.call(['ffmpeg', '-r', '1', '-i', 'img_%05d.jpg', '-vcodec', 'mpeg4', '-y', 'vid.mp4'])
        print ('Video Process: ',code,'\n')
        if(code==0):
            print "Video built successfully"
            return 1
        else:
            return 0
    except Exception as e:
        print "Error occurred in Video formation. "+str(e)
        return 0
