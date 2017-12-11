from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
	"""A class to generate random walks"""
	
	def __init__(self, num_points = 5000):
		"""Intialize attributes of a walk."""
		self.num_points = num_points
		
		# All walks start at (0,0).
		self.x_values = [0]
		self.y_values = [0]
		
		
		
	def fill_walk(self):
		"""Calculate all the points of the walk"""
		
		#Keep taking steps until the walk reaches the desired length.
		while len(self.x_values) < self.num_points:
			#decide which direction to go and how far.
			x_step = self.get_step()
			y_step = self.get_step()
			
			#moves that go nowhere are rejected
			if x_step == 0 and y_step == 0:
				continue
				
			#calculate the next x and y values.
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
			
			
			
	def get_step(self):
		"""finds the direction and the distance travelled in that direction."""
		direction = choice([1,-1])
		distance = choice([0, 1, 2, 3, 4])
		step = direction * distance
		return step
			

			
			
			
#keep making random walks while true
while True:	
	#make a randomwalk and plot the points
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	#set the size of the plotting window, my laptop dpi is 127
	plt.figure(dpi=127, figsize=(10,6))
	
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
	#plt.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)
	
	#emphasize first and last points
	plt.scatter(0, 0, c='green', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100) 
	
	#clean up the axes by removing them
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()
	
	keep_running = input("Make another walk? (y/n) ")
	if keep_running == 'n':
		break
		