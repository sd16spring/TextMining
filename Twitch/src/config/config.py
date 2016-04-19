"""
The configuration page, which holds all the information passed to the server to make the correct connection to the right streamer.
It is driven by user input on the streamer name.

Base code by Aidan, the modification of user input was done my me
Kevin Zhang, Software Design Spring 2016
"""
global config



config = {
	
	# details required to login to twitch IRC server
	'server': 'irc.twitch.tv',
	'port': 6667,
	'username': 'azulflower8850',
	'oauth_password': 'oauth:08dybr0t5r2zpn6nr2grrinaob88z2', # get this from http://twitchapps.com/tmi/
	
	# channel to join
	'channels': ['chicken'],   #currently with a proxy which will be replaced by user input

	# if set to true will display any data received
	'debug': False,


	'cron': {
		'chicken': {
			'run_cron': False, 	# set this to false if you want don't want to run the cronjob but you want to preserve the messages etc
			'run_time': 5, 		# time in seconds
			'cron_messages': [
				'This is cron message one.',
				'This is cron message two.'
			]
		},

	},

	# if set to true will display any data received
	'debug': False,

	# if set to true will log all messages from all channels
	# todo
	'log_messages': True,

	# maximum amount of bytes to receive from socket - 1024-4096 recommended
	'socket_buffer_size': 2048
}

