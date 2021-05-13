import time
import turtle

t = turtle

firstquestion = input(str('What is your name? '))
secondquestion = input(str('Hi ' + firstquestion + ', How is your day going? '))
if(secondquestion == 'Good'):
    thirdquestion = input(str('Why was your day Good? '))
elif(secondquestion == 'good'):
  thirdquestion = input(str('Why was your day good? '))
elif(secondquestion == 'bad'):
    thirdquestion = input(str('Why was your day bad? '))
elif(secondquestion == 'Bad'):
    thirdquestion = input(str('Why was your day Bad? '))
else:
  thirdquestion = input(str('Why was your day ' + secondquestion + '? ' ))
fourthquestion = input(str('Is there anything that I can do to make it better for you? '))
print('Oh well I cant exactly help with that because im a robot')

time.sleep(2.5)

color = input(str('Anyways ' + firstquestion + ' whats your favorite color? '))

askdraw = input(str('Would you like me to draw something with the color you said? '))
if(askdraw == 'Yes'):
  t.color(color)
  t.circle(30)
  t.forward(40)
  t.backward(80)
  t.left(90)
  t.forward(80)
  t.right(90)
  t.forward(80)
  t.right(90)
  t.forward(80)
  time.sleep(2)
  askfriends = input(str('Wow! I love the color ' + color + '! so anyways do you have any friends?'))
elif(askdraw == 'yes'):
  t.color(color)
  t.circle(30)
  t.forward(40)
  t.backward(80)
  t.left(90)
  t.forward(80)
  t.right(90)
  t.forward(80)
  t.right(90)
  t.forward(80)
  time.sleep(2)
  askfriends = input(str('Wow! I love the color ' + color + '! so anyways do you have any friends?'))
elif(askdraw == 'y'):
  t.color(color)
  t.circle(30)
  t.forward(40)
  t.backward(80)
  t.left(90)
  t.forward(80)
  t.right(90)
  t.forward(80)
  t.right(90)
  t.forward(80)
  time.sleep(2)
  askfriends = input(str('Wow! I love the color ' + color + '! so anyways do you have any friends?'))
elif(askdraw == 'Y'):
  t.color(color)
  t.circle(30)
  t.forward(40)
  t.backward(80)
  t.left(90)
  t.forward(80)
  t.right(90)
  t.forward(80)
  t.right(90)
  t.forward(80)
  time.sleep(2)
  askfriends = input(str('Wow! I love the color ' + color + '! so anyways do you have any friends?'))
else:
  askaboutfriends = input(str('The color ' + color + '! is very nice, anyways do you have any friends yes or no? '))

if(askaboutfriends == 'Yes'):
  askfriendsnames = input(str('Oh thats good what are your friends names?'))
elif(askaboutfriends == 'yes'):
  askfriendsnames = input(str('Oh thats good what are your friends names?'))
elif(askaboutfriends == 'Y'):
  askfriendsnames = input(str('Oh thats good what are your friends names?'))
elif(askaboutfriends == 'y'):
  askfriendsnames = input(str('Oh thats good what are your friends names?'))
else:
  askfriendsnames = input(str('Oh well if you dont have any friends I would be your friend if i wasnt a robot'))