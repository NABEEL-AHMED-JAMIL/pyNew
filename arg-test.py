# -*- coding: cp1252 -*-
# Python source files are treated as encoded in UTF-8
import sys;

print ("Show All Args: ", sys.argv);

if len(sys.argv) < 2:
    print("Processing Without Args");
    quit();
else:    
    print("Script Name: ", sys.argv[0]);
    print("Arguments: ", sys.argv[1]);
    print("CMD ARGS: ", sys.argv[1:]);
