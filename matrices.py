import matplotlib.pyplot as plt

data=[
      [10,10,10,10,10,10,10,10,10,10,10],
      [10,10,10,0,0,0,0,0,10,10,10],
      [10,10,0,4,4,4,4,4,0,10,10],
      [10,0,4,10,4,4,4,10,4,0,10],
      [10,0,4,10,4,0,4,10,4,0,10],
      [10,0,0,0,0,10,0,0,0,0,10],
      [10,0,10,10,10,0,10,10,10,0,10],
      [10,10,0,10,10,10,10,10,0,10,10],
      [10,10,10,0,0,0,0,0,10,10,10],
      [10,10,10,10,10,10,10,10,10,10,10]
      ]

plt.imshow(data,cmap="flag")
plt.show()