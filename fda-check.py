#!/usr/bin/env python3
import sys
import os
import subprocess
from subprocess import Popen, PIPE
import shutil

def main():
    fda_restricted_path = os.path.expanduser('~/Library/Mail') # Use Library\Mail as a test FDA-restricted location

    # First, copy the test malware file to restricted path
    print('Copying test malware file to {}'.format(fda_restricted_path))
    shutil.copyfile('malware_test_file/eicar.com', fda_restricted_path + '/eicar.com')
    print('File copied.')

    # Scan this location via fsav command-line tool
    print('Scanning using F-Secure Anti-virus command-line tool {}'.format(fda_restricted_path))
    p = subprocess.Popen(['sudo', '/Library/F-Secure/fssp/bin/fsav', fda_restricted_path, '--virus-action1=delete'], stdin=PIPE, stdout=PIPE) # Remove malware if found
    p.stdin.write(b"yes\n")
    outputlog, errorlog = p.communicate()
    p.stdin.close()

    if(os.path.exists(fda_restricted_path + '/eicar.com')): # FDA is not enabled due to F-Secure cannot scan or remove from restricted path, therefore this file still exists
        print('FDA IS NOT ENABLED.') 

        # Clean up the malware file
        print('Cleaning up test malware file at {}'.format(fda_restricted_path))
        os.remove(fda_restricted_path + '/eicar.com')
        print('Malware file is removed.')

    else:
        print('FDA IS ENABLED.') # FDA is enabled due to F-Secure can scan and remove from restricted path

    
if __name__ == '__main__':
    main()