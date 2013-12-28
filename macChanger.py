#!/usr/bin/python
# -*- coding: utf-8 -*-

# FUNCTIONALITY 
# -e, --endding    Don't change the vendor bytes.
# -a                Set random vendor MAC of any kind.
# -r, --random   Set fully random MAC.  
# -m, --mac XX:XX:XX:XX:XX:XX     Set the MAC XX:XX:XX:XX:XX:XX
# -apple,         Set random mac with vender MAC from Apple

# TODO
#Add in functionality to spoof an already authenticated user
#check scope of newMac maybe make it global
#TO-TEST	-apple	-m	

#get old mac before changing
class MacChanger:
	import random
	import string
	
	def changeMac(self, option, oldMac): # Test
		if option.lower() == '-r': #completely randomize mac
			return self.randomMac()       
		elif option.lower() == '-a':     #change only vender get vender codes
			return self.changeVender(oldMac)      
		elif option.lower() == '-apple':    #change vender to apple
			return self.appleMac()
		elif option.lower() == '-e':	#change only the ending 
			return self.changeEnding(oldMac)
		elif option.lower() == '-m':	#user custom Mac address
			return self.customMac()	#this is going to need to take the custon mac...
	  
	def appleMac(self): # TODO use old mac endpeice or randomize new..?
		newMac = ''
		fr = open('appleMacs.txt')
		for line in fr:        #read mac vender codes from file
			appleMacs.append(line)    
		appleVender = appleMacs[self.random.randint(0,appleMacs.length)]    #random choice of mac venders
		newMac = '{0}:{1}:{2}:{3}'.format(appleVender[:2], appleVender[2:4], appleVender[4:6], oldMac[9:]) # newMac invalid syntax
		# seperate the apple vender and add on the original NIC
		return newMac
	  
	def randomMac(self): 
		newMac = ''
		for i in range(6):
			newMac = newMac.join(self.random.sample(self.string.hexdigits, 2)) # one random octet
		      
		newMac = '{0}:{1}:{2}:{3}:{4}:{5}'.format(newMac[:2], newMac[2:4],newMac[4:6],newMac[6:8],newMac[8:10],newMac[10:12])     #combine each octet
		return newMac
	  
	def changeVender(self, oldMac):
		newMac = ''
		for i in range(3):
			newMac = newMac.join(self.random.sample(self.string.hexdigits, 2)) #one random octet
	      
		newMac = '{0}:{1}:{2}:{3}'.format(newMac[:2], newMac[2:4],newMac[4:6],oldMac[9:])
		return newMac
		#take the three new octets and the old nic

	def changeEnding(self, oldMac):
		newMac = '' 
		for i in range(3):
			newMac = newMac.join(self.random.sample(self.string.hexdigits, 2)) #one random octet
		newMac = '{0}:{1}:{2}:{3}'.format(oldMac[:8], newMac[:2], newMac[2:4],newMac[4:6])
		return newMac
		  
	def customMac(self, newMac):	
		#check that the mac address given is in the correct format
		print 'No MAC validation has been done'
		return newMac
print 'test'
if __name__ == "__main__":
	print 'WELCOME TO MACCHANGER'    
	#how to find HWaddr with out macchanger
	#ifconfig eth0 hw ether 01:02:03:04:05:06
	# TODO Get old mac address..
	oldMac = '00:00:00:00:00:00'

	mc = MacChanger()
	newMac = mc.changeMac('-r', oldMac)

	sub.call('ifconfig %s down'%(interface), shell=True)
	sub.call('ifconfig %s hw ether %s'%(interface, newMac), shell=True)
	sub.call('ifconfig %s up'%(interface), shell=True)

	print 'new' +newMac
	print 'old' +oldMac

