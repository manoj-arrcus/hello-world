import sys 
  
if sys.argv == 1:
	return

if sys.argv[1].find('TH-Build') >= 0:
	printf("Build c code and execute")

if sys.argv[1].find('TH-Upgrade') >= 0:
	printf("Upgrade Switches listed in second argument")

if sys.argv[1].find('TH-Regression') >= 0:
	printf("Trigger regression over the testbed")

