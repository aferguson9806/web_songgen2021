import os
import sys
import argparse

def remove_file(path):
    try:
        os.remove(path)
    except:
        raise "Invalid Path"
    

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args(list)
    """

    
    
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type = str, help = 'the path of the file to be deleted')
    
    args = parser.parse_args(args_list)
    
    
    
    return args
    
    
if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:])
    remove_file(arguments.path)