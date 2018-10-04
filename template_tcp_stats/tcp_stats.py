#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://linux.die.net/man/8/ss

import sys
import subprocess
from subprocess import PIPE, Popen

def print_data(data, arg):
    """ print data """
    
    if arg is not "":
        arg = "-[" + arg + "]"

    print "- tcp-listen" + arg, data.count("LISTEN")
    print "- tcp-estab" + arg, data.count("ESTAB")
    print "- tcp-time-wait" + arg, data.count("TIME-WAIT")
    print "- tcp-close-wait" + arg, data.count("CLOSE-WAIT")
    print "- tcp-closing" + arg, data.count("CLOSING")
    print "- tcp-syn-sent" + arg, data.count("SYN-SENT")
    print "- tcp-syn-recv" + arg, data.count("SYN-RECV")
    print "- tcp-fin-wait1" + arg, data.count("FIN-WAIT-1")
    print "- tcp-fin-wait2" + arg, data.count("FIN-WAIT-2")
    print "- tcp-last-ack" + arg, data.count("LAST-ACK")

def main(argv):
    """ main """

    try:
        if sys.argv[1:]:
            for arg in sys.argv[1:]:
                arg_str = "( dport = :" + arg + " or sport = :" + arg + " )"
                proc = Popen(["ss", "-ot", arg_str], stdout=PIPE)
                print_data(proc.communicate()[0], arg)
        else:
            # subprocess.check_output doesnt work on python 2.6
            # print_data(subprocess.check_output(["ss", "-at"]), "")
            proc = Popen(['ss', '-at'], stdout=PIPE)
            print_data(proc.communicate()[0], "")

    except subprocess.CalledProcessError as err:
        print err.output

if __name__ == "__main__":
    main(sys.argv[1:])
