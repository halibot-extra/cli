import time
import readline
from halibot import HalAgent, Message
from threading import Thread

class Cli(HalAgent):

	def init(self):
		self.running = True
		self.thread = Thread(target=self.input_loop)	
		self.thread.start()

	def shutdown(self):
		self.running = False
		self.thread.join()

	def input_loop(self):
		while self.running:
			inp = input('>> ')
			msg = Message(body=inp, origin=self.name)
			self.dispatch(msg)
			time.sleep(.1) # Kludge so responses appear before the prompt

	def receive(self, msg):
		print(msg.body)

