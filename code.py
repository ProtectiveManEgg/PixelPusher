from pixelPusher import pusher
import board

channels = [			# max channels 4
	[board.GP6, 18],	#gpio_pin, num_leds
	[board.GP8, 44]
]

#pusher(ssid: str, passw: str, brightness: int = 50, channels: list = None)
pusher("ssid", "passw", channels = channels, singleChannel = True)