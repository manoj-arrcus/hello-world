import sys 
import os 

#POC file to route actions based on git commit comments  
if sys.argv > 1:

	if sys.argv[1].find('TH-Build') >= 0:
		os.system("gcc helloworld.c")
		os.system("./a.out")
		os.system("rm a.out")
		print("\nTest Harness:Build c code and execute")

	if sys.argv[1].find('TH-Upgrade') >= 0:
		print("Test Harness:Upgrade Switches listed in second argument")

	if sys.argv[1].find('TH-Regression') >= 0:
		print("Test Harness:Trigger regression over the testbed")

