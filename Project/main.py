#goal of this project is to a turtle that draws people faces
#first step is to figure out what exactly to use supposedly I have to use pillow so let's see what it requires
#setup
from PIL import Image
image = "Images/"+str(input("Enter filename(MAKE SURE YOU TYPE THE FILENAME CORRECTLY WITH):"))
import turtle
screen = turtle.Screen()
screen.tracer(0) #control how fast the thing is animated just learned this
bob = turtle.Turtle()  
bob.penup()
img = Image.open(image)
img = img.resize((200, 200))
img = img.convert("RGB")
WIDTH = 200
HEIGHT = 200
pixels = img.load()
turtle.colormode(255)
for x in range(WIDTH):
    for y in range (HEIGHT):
        r, g, b = pixels[x, y]
        bob.goto(x, -y)
        bob.dot(3, (r, g, b))
screen.update()
turtle.done()
