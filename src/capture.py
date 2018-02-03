import capture_IP
import argparse
import sys
import os
import threading
from time import strftime

# Config File

config_file = "./config.json"


# Logo art

LOGO = """
                                                                         ██╗
██████╗ ██╗  ██╗ ██████╗ ████████╗ ██████╗  ██████╗ ██████╗  █████╗   ████████╗
██╔══██╗██║  ██║██╔═══██╗╚══██╔══╝██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗ ██╔═██╔═██╗
██████╔╝███████║██║   ██║   ██║   ██║   ██║██║  ███╗██████╔╝███████║ ██║ ██║ ██║
██╔═══╝ ██╔══██║██║   ██║   ██║   ██║   ██║██║   ██║██╔══██╗██╔══██║ ██║ ██║ ██║
██║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║ ╚████████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═██╔══╝
                                                                          ╚╝
                                                                    By B0vh1
"""
# Thread that handles simultaneous image capturing


if __name__ == '__main__':
    print(LOGO)
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-config','-c', metavar='file', type=str, nargs=1, help= 'file to read configuration from')
    parser.add_argument('-file','-f', metavar='file', type=str, nargs='?', help='file to read IP/domains from')
    parser.add_argument('-path','-p', metavar='path', type=str, nargs='?', help='path to store all data (Optional)')
    parser.add_argument('-target','-t', metavar='target', type=str, nargs='?', help='target to scan (In case there\'s only one')
    parser.add_argument('-threads','-th', metavar='threads', type=int, nargs='?', help='number of threads to use (only when reading from file)')
    parser.add_argument('-verbose','-v',metavar='verbose',type=str,nargs='?', help='shows verbose information, if a file is specified, outputs to it')
    args = parser.parse_args()

    if args.path:
        PATH = os.getcwd()+os.sep+args.path+os.sep
        if os.path.isdir(PATH):
            print("Working in "+args.path+" directory",file=sys.stderr)
        else:
            print("Creating "+args.path+" directory",file=sys.stderr)
            os.makedirs(PATH)
    else:
        print("Working in current directory",file=sys.stderr)
        PATH = os.getcwd()+os.sep

    if args.file:
        try:
            print("Capturing from file "+args.file+"...",file=sys.stderr)
            file  = open(args.file,"r")
        except:
            print("Error trying to open a file!!! Make sure the name is correct!!!",file=sys.stderr)
            exit(1)
        splitted_content=file.readlines()
        file.close()
        num_elements = len(splitted_content)
        index = int(0)
        if args.threads:
            thread_num = args.threads
        else:
            thread_num = 5

        base_index = 0

        threads=[]
        while (base_index) <= num_elements:
            for i in range(thread_num):
                try:
                    current_url = splitted_content[base_index+i].replace('\n','')
                    # print("["+strftime("%H:%M:%S")+"]\tCapturing",current_url,"from thread",threading.current_thread(),sep=" ", file=sys.stderr)
                    thread = threading.Thread(target=capture_IP.takeScreenshotFullURL, args=(current_url,PATH,))
                    threads.append(thread)
                    thread.start()
                except IndexError:
                    pass
            # Wait for threads to finish
            for x in threads:
                    x.join()    
            threads[:] = []
            base_index+=(thread_num)

    elif args.target:
        print("Capturing "+args.target+"...",file=sys.stderr)
        capture_IP.takeScreenshotFullURL(args.target,PATH)
    else:
        print("You should indicate at least one file or address!!",file=sys.stderr)
        exit(1)