#!/usr/bin/env python
"""
This is the main file that is to be run for the program to work. It asks for a user input for streamer name and then runs the program based on the inputted streamer.
Enjoy the waterfall of trololololol

Used the base code of Aidan, modified with user input by myself.
Kevin Zhang, Software Design Spring 2016
"""

from sys import argv
from src.bot import *
from src.config.config import *
import pickle
import sys
import src.config.config




global streamer_name 																						#makes a global variable that can be accessed by config

streamer_name = ''

name = raw_input('\n\nPlease input the name of the streamer whose chat you would like to analyze!\n\n')     #allows for user input of streamer's name from Twtich Chat

name = name.lower()																							#standardizes input and adds a hashtag
streamer_name = '#' + name


config['channels'] = [streamer_name]																		#assigns the input to the config module
	
bot = Roboraj(config).run()																					#runs the main code

	




