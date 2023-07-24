import random
import time
import wave
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
        self.noteCount = duration // 2
        self.name = name
        self.instrument = instrument
        self.notes = ["whole", "half", "quarter"]      
        
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
        
        """ Plays a c5 note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of c5 note 
            saxlowc.wav: sax mp3 file of c5 note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianolowc.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianolowchalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianolowcquarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxlowc.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxlowchalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxlowcquarter.wav", .25)
        
    def c5sharp(self):
        
        """ Plays a c5 sharp note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of c5 sharp note 
            saxlowc.wav: sax mp3 file of c5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianoc#.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianoc#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianoc#quarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxc#.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxc#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxc#quarter.wav", .25)
        
    def d5(self):
        
        """ Plays a d5 note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of d5 note 
            saxlowc.wav: sax mp3 file of d5 note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianod.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianodhalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianodquarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxd.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxdhalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxdquarter.wav", .25)
        
    def d5sharp(self):
        
        """ Plays a d5 sharp note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of d5 sharp note 
            saxlowc.wav: sax mp3 file of d5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianod#.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianod#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianod#quarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxd#.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxd#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxd#quarter.wav", .25)
        
    def e5(self):
        
        """ Plays a e5 note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of e5 note 
            saxlowc.wav: sax mp3 file of e5 note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianoe.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianoehalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianoequarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxe.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxehalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxequarter.wav", .25)
    def f5(self):
        
        """ Plays a f5 note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of f5 note 
            saxlowc.wav: sax mp3 file of f5 note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianof.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianofhalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianofquarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxf.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxfhalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxfquarter.wav", .25)
        
    def f5sharp(self):
        
        """ Plays a f5 sharp note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of f5 sharp note 
            saxlowc.wav: sax mp3 file of f5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianof#.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianof#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianof#quarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxf#.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxf#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxf#quarter.wav", .25)
        
    def g5(self):
        
        """ Plays a g5 note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of g5 note 
            saxlowc.wav: sax mp3 file of g5 note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianog.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianoghalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianogquarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxg.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxghalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxgquarter.wav", .25)
        
    def g5sharp(self):
        
        """ Plays a g5 sharp note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of g5 sharp note 
            saxlowc.wav: sax mp3 file of g5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianog#.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianog#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianog#quarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxg#.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxg#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxg#quarter.wav", .25)
        
    def a5(self):
        
        """ Plays a a5 note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of a5 note 
            saxlowc.wav: sax mp3 file of a5 note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianoa.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianoahalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianoaquarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxa.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxahalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxaquarter.wav", .25)
        
    def a5sharp(self):
        
        """ Plays a a5 sharp note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of a5 sharp note 
            saxlowc.wav: sax mp3 file of a5 sharp note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianoa#.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianoa#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianoa#quarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxa#.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxa#half.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxa#quarter.wav", .25)
        
    def b5(self):
        
        """ Plays a b5 note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of b5 note 
            saxlowc.wav: sax mp3 file of b5 note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianob.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianobhalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianobquarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxb.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxbhalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxbquarter.wav", .25)
        
    def c6(self):
        
        """ Plays a c6 note and return (s mp3 file of either a piano or saxophone playing it depending on which is chosen

            Returns:
            
            pianolowc.wav: piano mp3 file of c6 note 
            saxlowc.wav: sax mp3 file of c6 note 
        """
        
        if self.instrument.lower() == 'piano':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/pianohighc.wav", 1)
            if select == "half":
                return ("public/soundfiles/pianohighchalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/pianohighcquarter.wav", .25)
        
        elif self.instrument.lower() == 'sax':
            
            select = random.choice(self.notes)
            if select == "whole":
                return ("public/soundfiles/saxhighc.wav", 1)
            if select == "half":
                return ("public/soundfiles/saxhighchalf.wav", .5)
            if select == "quarter":
                return ("public/soundfiles/saxhighcquarter.wav", .25)  
    
        
        
    def play_song(self):
        
        """ Plays the song based on inputs given
        
            Side Effects:
            
            Increases elapsed by -500 for each key randomly chosen
        """
        
        elapsed = 0
        self.key = eval(self.key)
        while elapsed < self.noteCount:
            choice = random.choice(self.key)(mysong)
            self.wavfiles.append(choice[0])
            elapsed += choice[1]
            
    def compile_song_file(self):
        
        """ Turns file song into wav file and downloads it to directory
        
            Side Effects:
            
            Downloads song as wav file into directory.
            
        """
        
        infiles = self.wavfiles
        outfile = f"public/out_songs/{self.name}.wav"
        
        wav_out = wave.open(outfile, 'wb')
        for wav_path in infiles:
            wav_in = wave.open(wav_path, 'rb')
            if not wav_out.getnframes():
                wav_out.setparams(wav_in.getparams())
            wav_out.writeframes(wav_in.readframes(wav_in.getnframes()))   
            
            
def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args(list)
    """

    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('instrument', default = "sax", type = str, help = 'the instrument to be used')
    parser.add_argument('name', default = "andrew", type = str, help = 'The annual interest rate, should be a float between 0 and 1')
    parser.add_argument('key', default = "gmajor", type = str, help = 'The term of the mortgage, in years, should be a positive integer')
    parser.add_argument('duration', default= 12, type = int, help = 'The number of payments per year, should be a positive integer')
    
    args = parser.parse_args(args_list)
    
    
    
    return args


if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    mysong = Song(arguments.instrument, arguments.name, arguments.key, int(arguments.duration))
    mysong.play_song()
    print(mysong.wavfiles)
    mysong.compile_song_file()

    

        
        
