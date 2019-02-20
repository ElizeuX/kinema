#
# Name: ValidateDirectoryWritable Function
#
# Desc: Function that will validate a directory path as 
#           existing and writable.  Used for argument validation only
#
# Input: a directory path string
#  
# Actions: 
#              if valid will return the Directory String
#
#              if invalid it will raise an ArgumentTypeError within argparse
#              which will inturn be reported by argparse to the user
#

def ValidateDirectoryWritable(theDir):

    # Validate the path is a directory
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')

    # Validate the path is writable
    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise argparse.ArgumentTypeError('Directory is not writable')
        raise RuntimeError('specific message') from error

#End ValidateDirectoryWritable ===================================
