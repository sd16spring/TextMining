#!/usr/bin/env python

from sys import argv
from src.bot import *
from src.config.config import *
import pickle
import sys
import src.config.config


name = raw_input('\n\nPlease input the name of the streamer whose chat you would like to analyze!\n\n')

name = name.lower()

streamer_name = name

	
bot = Roboraj(config).run()

	




