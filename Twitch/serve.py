#!/usr/bin/env python

from sys import argv
from src.bot import *
from src.config.config import *
import pickle
import sys
import src.config.config

global streamer_name 

streamer_name = ''

name = raw_input('\n\nPlease input the name of the streamer whose chat you would like to analyze!\n\n')

name = name.lower()
streamer_name = '#' + name


config['channels'] = [streamer_name]
	
bot = Roboraj(config).run()

	




