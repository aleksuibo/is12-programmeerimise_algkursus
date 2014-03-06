class switch():
	
	def __init__(self,state):
		self.state=state
	
	def on(self):
		self.state=True
		
	def off(self):
		self.state=False
		
	def state_get(self):
		return self.state
				
obj1=switch(False)
print obj1.state_get()
obj1.on()
print obj1.state_get()


				
