import random
import time
from pydub import AudioSegment, silence
from pydub.playback import play
import ffmpeg
import argparse
import sys


class Song:
    
    """ Creates a song based on certain inputs.
    
        Attributes:
        
        self.songinmilli(int): The amount of time in milliseconds the song will be.
        (str): String to be combined with other notes.
    """
    
    def __init__(self, instrument, name, key, duration):
        self.key = "self." + key
        self.songinmilli = duration * 1000
        self.name = name
        self.instrument = instrument        
        
        assert self.instrument in ['piano', 'sax'], "Nothing should print here"         #Tests that the users choice is 'piano' or 'sax'
        
        #MAJOR KEYS
        self.chromatic = [Song.c5, Song.c5sharp, Song.d5, Song.d5sharp, Song.e5, Song.f5, Song.f5sharp, Song.g5, Song.g5sharp, Song.a5, Song.a5sharp, Song.b5, Song.c6]
        self.cmajor = [Song.c5, Song.d5, Song.e5, Song.f5, Song.g5, Song.a5, Song.b5, Song.c6]
        self.dmajor = [Song.d5, Song.e5, Song.f5sharp, Song.g5, Song.a5, Song.b5, Song.c5sharp]
        self.emajor = [Song.e5, Song.f5sharp, Song.g5sharp, Song.a5, Song.b5, Song.c5sharp, Song.d5sharp]
        self.fmajor = [Song.f5, Song.g5, Song.a5, Song.a5sharp, Song.c5, Song.d5, Song.e5, Song.f5]
        self.gmajor = [Song.g5, Song.a5, Song.b5, Song.c5, Song.d5, Song.e5, Song.f5sharp]
        self.amajor = [Song.a5, Song.b5, Song.c5sharp, Song.d5, Song.e5, Song.f5sharp, Song.g5sharp]
        self.bmajor = [Song.b5, Song.c5sharp, Song.d5sharp, Song.e5, Song.f5sharp, Song.g5sharp, Song.a5sharp]
        self.csharpmajor = [Song.c5sharp, Song.d5sharp, Song.f5, Song.f5sharp, Song.g5sharp, Song.a5sharp, Song.c5]
        self.dsharpmajor = [Song.d5sharp, Song.f5, Song.g5, Song.g5sharp, Song.a5sharp, Song.c5, Song.d5]
        self.fsharpmajor = [Song.f5sharp, Song.g5sharp, Song.a5sharp, Song.b5, Song.c5sharp, Song.d5sharp, Song.f5]
        self.gsharpmajor = [Song.g5sharp, Song.a5sharp, Song.c5, Song.c5sharp, Song.d5sharp, Song.f5, Song.g5]
        self.asharpmajor = [Song.a5sharp, Song.c5, Song.d5, Song.d5sharp, Song.f5, Song.g5, Song.a5]    
        
        #MINOR KEYS
        self.cminor = [Song.c5, Song.d5, Song.d5sharp, Song.f5, Song.g5, Song.g5sharp, Song.a5sharp, Song.c6]
        self.dminor = [Song.d5, Song.e5, Song.f5, Song.g5, Song.a5, Song.a5sharp, Song.c5]
        self.eminor = [Song.e5, Song.f5sharp, Song.g5, Song.a5, Song.b5, Song.c5, Song.d5]
        self.fminor = [Song.f5, Song.g5, Song.g5sharp, Song.a5sharp, Song.c5, Song.c5sharp, Song.d5sharp]
        self.gminor = [Song.g5, Song.a5, Song.a5sharp, Song.c5, Song.d5, Song.d5sharp, Song.f5]
        self.aminor = [Song.a5, Song.b5, Song.c5, Song.d5, Song.e5, Song.f5, Song.g5]
        self.bminor = [Song.b5, Song.c5sharp, Song.d5, Song.e5, Song.f5sharp, Song.g5, Song.a5]
        self.csharpminor = [Song.c5sharp, Song.d5sharp, Song.e5, Song.f5sharp, Song.g5sharp, Song.a5, Song.b5]
        self.dsharpminor = [Song.d5sharp, Song.f5, Song.f5sharp, Song.g5sharp, Song.a5sharp, Song.b5, Song.c5sharp]
        self.fsharpminor = [Song.f5sharp, Song.g5sharp, Song.a5, Song.b5, Song.c5sharp, Song.d5, Song.e5]
        self.gsharpminor = [Song.g5sharp, Song.a5sharp, Song.b5, Song.c5sharp, Song.d5sharp, Song.e5, Song.f5sharp]
        self.asharpminor = [Song.a5sharp, Song.c5, Song.c5sharp, Song.d5sharp, Song.f5, Song.f5sharp, Song.g5sharp]
        
        
        #LIST TO BE TURNED INTO FILE
        self.wavfiles = []

        
    def c5(self):
        
        """ Plays a c5 note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of c5 note 
            saxlowc.wav: sax mp3 file of c5 note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianolowc.wav"))
            return "soundfiles/pianolowc.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxlowc.wav"))
            return "soundfiles/saxlowc.wav"
        
    def c5sharp(self):
        
        """ Plays a c5 sharp note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of c5 sharp note 
            saxlowc.wav: sax mp3 file of c5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianoc#.wav"))
            return "soundfiles/pianoc#.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxc#.wav"))
            return "soundfiles/saxc#.wav"
        
    def d5(self):
        
        """ Plays a d5 note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of d5 note 
            saxlowc.wav: sax mp3 file of d5 note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianod.wav"))
            return "soundfiles/pianod.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxd.wav"))
            return "soundfiles/saxd.wav"
        
    def d5sharp(self):
        
        """ Plays a d5 sharp note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of d5 sharp note 
            saxlowc.wav: sax mp3 file of d5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianod#.wav"))
            return "soundfiles/pianod#.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxd#.wav"))
            return "soundfiles/saxd#.wav"
        
    def e5(self):
        
        """ Plays a e5 note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of e5 note 
            saxlowc.wav: sax mp3 file of e5 note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianoe.wav"))
            return "soundfiles/pianoe.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxe.wav"))
            return "soundfiles/saxe.wav"
    def f5(self):
        
        """ Plays a f5 note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of f5 note 
            saxlowc.wav: sax mp3 file of f5 note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianof.wav"))
            return "soundfiles/pianof.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxf.wav"))
            return "soundfiles/saxf.wav"
        
    def f5sharp(self):
        
        """ Plays a f5 sharp note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of f5 sharp note 
            saxlowc.wav: sax mp3 file of f5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianof#.wav"))
            return "soundfiles/pianof#.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxf#.wav"))
            return "soundfiles/saxf#.wav"
        
    def g5(self):
        
        """ Plays a g5 note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of g5 note 
            saxlowc.wav: sax mp3 file of g5 note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianog.wav"))
            return "soundfiles/pianog.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxg.wav"))
            return "soundfiles/saxg.wav"
        
    def g5sharp(self):
        
        """ Plays a g5 sharp note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of g5 sharp note 
            saxlowc.wav: sax mp3 file of g5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianog#.wav"))
            return "soundfiles/pianog#.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxg#.wav"))
            return "soundfiles/saxg#.wav"
        
    def a5(self):
        
        """ Plays a a5 note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of a5 note 
            saxlowc.wav: sax mp3 file of a5 note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianoa.wav"))
            return "soundfiles/pianoa.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxa.wav"))
            return "soundfiles/saxa.wav"
        
    def a5sharp(self):
        
        """ Plays a a5 sharp note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of a5 sharp note 
            saxlowc.wav: sax mp3 file of a5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianoa#.wav"))
            return "soundfiles/pianoa#.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxa#.wav"))
            return "soundfiles/saxa#.wav"
        
    def b5(self):
        
        """ Plays a b5 note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of b5 note 
            saxlowc.wav: sax mp3 file of b5 note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianob.wav"))
            return "soundfiles/pianob.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxb.wav"))
            return "soundfiles/saxb.wav"
        
    def c6(self):
        
        """ Plays a c6 note and returns mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of c6 note 
            saxlowc.wav: sax mp3 file of c6 note 
        """
        
        if self.instrument.lower() == 'piano':
            play(AudioSegment.from_wav("soundfiles/pianohighc.wav"))
            return "soundfiles/pianohighc.wav"
        elif self.instrument.lower() == 'sax':
            play(AudioSegment.from_wav("soundfiles/saxhighc.wav"))
            return "soundfiles/saxhighc.wav"
        
    
        


    
        
        
    def play_song(self):
        
        """ Plays the song based on inputs given
        
            Side Effects:
            
            Increases elapsed by -500 for each key randomly chosen
        """
        
        elapsed = 0
        self.key = eval(self.key)
        while elapsed < self.songinmilli:
            choice = random.choice(self.key)(mysong)
            self.wavfiles.append(choice)
            time.sleep(2)
            elapsed += 2000
            
            
def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args(list)
    """

    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('instrument', type = str, help = 'the instrument to be used')
    parser.add_argument('name', type = str, help = 'The annual interest rate, should be a float between 0 and 1')
    parser.add_argument('key', type = str, help = 'The term of the mortgage, in years, should be a positive integer')
    parser.add_argument('duration', type = int, help = 'The number of payments per year, should be a positive integer')
    
    args = parser.parse_args(args_list)
    
    
    
    return args




if __name__ == "__main__":
    #play(AudioSegment.from_wav("soundfiles/saxa.wav"))
    #silence.min_silence_len(-500)
    arguments = parse_args(sys.argv[1:])
    mysong = Song(arguments.instrument, arguments.name, arguments.key, arguments.duration)
    mysong.play_song()
    #mysong.compile_song()
    

        
        
