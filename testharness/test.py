import sys 
import os 

bin_url = "http://10.9.195.14:7777/2020_06_25/ArcOS_v4.1.1.EFT6/ONL/ARCOS-ArcOS_v4.1.1.EFT6_ONL-OS_2020-06-26.0221-7f9bfa0_AMD64_INSTALLED_INSTALLER"
host_ip = "10.9.9.26"

#POC file to route actions based on git commit comments  
if sys.argv > 1:

	if sys.argv[1].find('TH-Build') >= 0:
		os.system("gcc helloworld.c")
		os.system("./a.out")
		os.system("rm a.out")
		print("\nTest Harness:Build c code and execute")

	if sys.argv[1].find('TH-Upgrade') >= 0:
		fp = open("upgrade_onl_template.xml","r")
		fw = open("upgrade_onl.xml","w+")
		while True:
			line = fp.readline()
			if not line:
				break
			if line.find("package-name") >= 0:
				fw.write("<package-name>{}</package-name>\n".format(bin_url))
			else:
				fw.write(line)
		fp.close()
		fw.close()
		print("new file created")
		os.system("./netconf-console --host {} --port 830 -u root -p arrcus --rpc upgrade_onl.xml".format(host_ip))
		os.system("pwd")
		print("Test Harness:Upgrade Switches listed in second argument")

	if sys.argv[1].find('TH-Regression') >= 0:
		print("Test Harness:Trigger regression over the testbed")

