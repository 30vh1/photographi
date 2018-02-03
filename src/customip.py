class customIP:
	ports = []
	protocols = []
	services = []
	ipRange = []
	hostname = str()
	title = []

	def __init__(self,address):
		self.address=address

	def add_port(self,port):
		self.ports.append(port)

	def add_protocol(self,protocol):
		self.protocols.append(protocol)

	def add_service(self,service):
		self.services.append(service)

	def add_port_protocol_service(self,port,protocol,service):
		self.add_port(port)
		self.add_protocol(protocol)
		self.add_service(service)

	def add_range(self,range):
		self.ipRange=range

	def add_hostname(self,hostname):
		self.hostname=hostname

	def add_title(self,title):
		self.title.append(title)

	def get_address(self):
		return self.address

	def get_ports(self):
		return self.ports

	def get_protocols(self):
		return self.protocols

	def get_range(self):
		return self.ipRange

	def get_hostname(self):
		return self.hostname

	def get_title(self):
		return self.title

	def get_services(self):
		return self.services

	def get_all(self):
		combination = []
		index = int()
		index=0
		for element in self.ports:
			combination.append([element,self.protocols[index],self.services[index]])
			index+=1
		return combination

	def print_info(self):
		print("Address:\t\t"+self.get_address())
		print("Title:  \t\t"+self.get_title())
		print("Hostname:\t\t"+str(self.get_hostname()))
		print("Range:   \t\t"+str(self.get_range()))
		print("Ports:	")
		index = int(0)
		for port in self.get_ports():
				print("\t"+port+"\t"+self.get_protocols()[index]+"\t"+self.get_services()[index])
				index+=1

	def print_info_to_file(self,PATH):
		file = open(PATH+self.get_address+".info",'w')
		file.write("Address:\t\t"+self.get_address())
		file.write("Title:  \t\t"+str(self.get_title()))
		file.write("Hostname:\t\t"+str(self.get_hostname()))
		file.write("Range:   \t\t"+str(self.get_range()))
		file.write("Ports:	")
		index = int(0)
		for port in self.get_ports():
				file.write("\t"+port+"\t"+self.get_protocols()[index]+"\t"+self.get_services()[index])
				index+=1
		file.close()