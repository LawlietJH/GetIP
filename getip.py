
# Tested in Python 3.8.3
# By: LawlietJH

import requests
import socket
import json

class GetIP:
	
	def __init__(self, only_local=False):
		
		self.hostname = socket.gethostname()
		self.local_ipv4 = socket.gethostbyname(self.hostname)
		self.local_ipv6 = socket.getaddrinfo(self.hostname, None, socket.AF_INET6)[0][4][0]
		self.public_ipv4 = None
		self.public_ipv6 = None
		
		if not only_local:
			try:
				self.public_ipv4 = requests.get('https://api.ipify.org').text
				self.public_ipv6 = requests.get('https://api64.ipify.org').text
			except:
				pass



if __name__ == '__main__':	# Ejemplos de uso:
	
	# Conecta a la API de ipify para obtener las IP publicas.
	getip = GetIP()
	
	print('HOST:', getip.hostname)
	print('IPv4 Privada:', getip.local_ipv4)
	print('IPv6 Privada:', getip.local_ipv6)
	print('IPv4 Publica:', getip.public_ipv4)
	print('IPv6 Publica:', getip.public_ipv6)
	
	# Sirve en el caso de no necesitar las ips publicas.
	# Evita conectarse a la API de ipify.
	only_local = GetIP(only_local=True)
	
	print('HOST:', only_local.hostname)
	print('IPv4 Privada:', only_local.local_ipv4)
	print('IPv6 Privada:', only_local.local_ipv6)
	print('IPv4 Publica:', only_local.public_ipv4)
	print('IPv6 Publica:', only_local.public_ipv6)
	

