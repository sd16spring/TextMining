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
import matplotlib.pyplot as plt
import time
import numpy as np



class Roboraj:

	def __init__(self, config):
		self.config = config
		self.irc = irc_.irc(config)
		self.socket = self.irc.get_irc_socket_object()
		


	def run(self):
		"""
		This function was based on Aidan's code, which is used mainly for the purpose of connecting to Twitch's Chat's servers and getting access to the chat.
		The only parts borrowed from Aidan are the connection to the server, and the access to the messages in the chat. 
		Everything else is my own creation.
		"""

		irc = self.irc
		sock = self.socket
		config = self.config
		filechicken = open('twitchchat', 'w') 				 # pickle was very difficult to implement because twitch chat uses very weird unicode values, which pickle couldn't understand
		filechicken.seek(0,0)      							#this makes sure the file always writes from the beginning
		count = 0 											#this allows for the program to automatically close itself after a certain period of time
		reload(sys)
		sys.setdefaultencoding('utf-8') 					#this assists in the ability of the script to take in weird words better.

		fig=plt.figure() 									#makes a matplotlib
		plt.axis([0,1,0,50])
		plt.ion()
		plt.xlabel('Sentiment value: Troll/Negative <-----> Happy/Positive', fontsize = 16)
		plt.ylabel('Message Frequency (Sum of words\' freq)', fontsize = 16)
		plt.suptitle('Text Mining Visualization', fontsize = 20)
		plt.show()											#this is a graph that will visualize the data, plotting sentiment vs. word frequency

		while True:
			data = sock.recv(config['socket_buffer_size']).rstrip()


			if len(data) == 0:
				pp('Connection was lost, reconnecting.')
				sock = self.irc.get_irc_socket_object()

			if config['debug']:
				print data

																# check for ping, reply with pong
			irc.check_for_ping(data)

			if irc.check_for_message(data): 					#retrieves each message sent to the chat
				message_dict = irc.get_message(data)

				channel = message_dict['channel']
				message = message_dict['message']
				username = message_dict['username']

				ppi(channel, message, username)

				filtering = ('! @ # $ % ^ & * ( ) \ < > ? / \" \' , ; : _ - = + . ~').split(' ')

				for item in filtering:
					message = message.replace(item, '')        #these two lines get rid of weird characters that aren't important

				message = message.lower()

				filechicken.write(message + " ") 				#writes to the file
				#pickle.dump(filechicken, message)			    #pickle failed cuz of unicode values
				filechicken.close()
				print ''										 #clarity in the terminal when viewing

				textmining.analyze() 							#this goes to my analyzing code, and is updated in real time for every message that is sent to twitch chat
				
				freq = 0											#keeps track of frequencies of messages as a summation of their words

				for words in message:							#finds the frequency of message as a summation the words in the message
					freq += textmining.findfreq(words)


				 												#plots the message's sentiment
				plt.scatter(float(textmining.wordsentiment(message)),freq)
				plt.draw()
				time.sleep(.05)


				print ''

				filechicken = open('twitchchat','r+')  			 #this puts the file back into writing and reading mode so that the next iteration can continue
				filechicken.seek(0,2)							 #goes the last thing written so it can continue

				if count == 100: 								#goes for a 100 messages, which is a good enough sample
					filechicken.close()
					filechicken = open("twitchchat", 'r')
					#textmining.sentiments(pickle.load(filechicken))  #pickle failure
					textmining.sentiments(filechicken.read()) 	#this allows for the sentiment analysis of the entire message history of this script at the end.
					filechicken.close()
					plt.show(block=True)						#makes sure the graph stays on after it's done plotting
					sys.exit()   								 #closes the program
				count = count + 1								 #moves closer to closing the program

				