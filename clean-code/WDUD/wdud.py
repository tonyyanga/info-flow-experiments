import sys, os
import experiment.alexa as alexa
import experiment.trials as trials

# from analyst import *

class Treatment:

	def __init__(self, name):
		self.name = name
		self.count=0
		self.str = "" #'sites':[], 'gender':'', }
	
	def add_site_file(self, file):
		if(self.count==0):
			self.str += "site|:|"+file
		else:
			self.str += "|+|site|:|"+file
		self.count += 1
	
	def add_gender(self, gender='m'):
		if (gender.lower()=='m' or gender.lower()=='male'):
			gender = 'm'
		elif (gender.lower()=='f' or gender.lower()=='female'):
			gender = 'f'
		if(self.count==0):
			self.str += "gender|:|"+gender
		else:
			self.str += "|+|gender|:|"+gender
		self.count += 1
	
	def add_interest(self, interest='Auto'):
		if(self.count==0):
			self.str += "interest|:|"+interest
		else:
			self.str += "|+|interest|:|"+interest
		self.count += 1
		

def collect_sites_from_alexa(alexa_link="http://www.alexa.com/topsites", output_file="out.txt", pages=4):	# n-number of pages on Alexa
	
	PATH="./"+output_file
	if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
		response = raw_input("This will overwrite file %s. Continue? (Y/n)" % output_file)
		if response == 'n':
			sys.exit(0)
	fo = open(output_file, "w")
	fo.close()
	print "Beginning Collection"
# 	os.system("python experimenter/alexa.py %s %s %s" % (output_file, alexa_link, n))
	alexa.run_script(alexa_link, output_file, pages)
	print "Collection Complete. Results stored in ", output_file

def begin_experiment(log_file="log.txt", samples=2, 
		treatments=[], blocks=1, runs=1, reloads=10, delay=5, browser='firefox'):	
	PATH="./"+log_file
	if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
		response = raw_input("This will overwrite file %s. Continue? (Y/n)" % log_file)
		if response == 'n':
			sys.exit(0)
	fo = open(log_file, "w")
	fo.close()
	print "Starting Experiment"
	trials.begin(log_file, samples, treatments, blocks, runs, reloads, delay, browser)
	print "Experiment Complete"