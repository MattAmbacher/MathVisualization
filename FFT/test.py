import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure()

l, = plt.plot( [], [], 'b-')
data = np.random.rand(2, 25)
plt.xlim(0,1)
plt.ylim(0,1)
def update_img(num, data, line):
	line.set_data(data[...,:num])
	return line,
	
ani = animation.FuncAnimation(fig, update_img, 25, fargs=(data, l),interval=50, blit=True)

ani.save('test.mp4')

plt.show()
