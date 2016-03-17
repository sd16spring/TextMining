"""
Simple IRC Bot for Twitch.tv

Developed by Aidan Thomson <aidraj0@gmail.com>
"""
"""
Used by Kevin Zhang for Text Mining/Analysis course project in Software Design at Franklin W. Olin College, Spring 2016

Aidan's code was used as the base code, and I did some significant modifications for the purposes of text mining and text analysis.

Note that most of his function were not used, only the basic draws from Twitch API. Everything else is my own creation.
"""

import lib.irc as irc_
from lib.functions_general import *
import lib.functions_commands as commands
import sys
import textmining
import pickle

class Roboraj:

	def __init__(self, config):
		self.config = config
		self.irc = irc_.irc(config)
		self.socket = self.irc.get_irc_socket_object()
		


	def run(self):
		irc = self.irc
		sock = self.socket
		config = self.config
		filechicken = open('twitchchat', 'w')  # pickle was very difficult to implement because twitch chat uses very weird unicode values, which weren't able to be picked up pickle
		filechicken.seek(0,0)
		count = 0 #this allows for the program to automatically close itself after a certain period of time
		reload(sys)
		sys.setdefaultencoding('utf-8') #this assists in the ability of the script to take in weird words better.

		while True:
			data = sock.recv(config['socket_buffer_size']).rstrip()


			if len(data) == 0:
				pp('Connection was lost, reconnecting.')
				sock = self.irc.get_irc_socket_object()

			if config['debug']:
				print data

			# check for ping, reply with pong
			irc.check_for_ping(data)

			if irc.check_for_message(data):
				message_dict = irc.get_message(data)

				channel = message_dict['channel']
				message = message_dict['message']
				username = message_dict['username']

				ppi(channel, message, username)

				filtering = ('! @ # $ % ^ & * ( ) \ < > ? / \" \' , ; : _ - = + . ~').split(' ')

				for item in filtering:
					message = message.replace(item, '')        #these two lines get rid of weird characters that aren't important

				message = message.lower()

				filechicken.write(message + " ") #writes to the file
				#pickle.dump(filechicken, message) #pickle failed cuz of unicode values
				filechicken.close()
				print '' #clarity in the terminal when viewing

				textmining.analyze() #this goes to my analyzing code, and is updated in real time for every message that is sent to twitch chat

				print ''

				filechicken = open('twitchchat','r+')   #this puts the file back into writing and reading mode so that the next iteration can continue
				filechicken.seek(0,2) #goes the last thing written so it can continue

				if count == 100: #goes for a 100 messages, which is a good enough sample
					filechicken.close()
					filechicken = open("twitchchat", 'r')
					#textmining.sentiments(pickle.load(filechicken))
					textmining.sentiments(filechicken.read()) #this allows for the sentiment analysis of the entire message history of this script at the end.
					filechicken.close()
					sys.exit()    #closes the program
				count = count + 1	 #moves closer to closing the program

				