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
fourthquestion = input(str('(send a few word response) Is there anything that I can do to make it better for you? '))
print('Sorry I cant help with ' + fourthquestion + ' I am just a robot')

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
  askfriends = input(str('Wow! I love the color ' + color + '! so anyways do you have friends? '))
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
  askfriends = input(str('The color ' + color + '! is very nice, anyways do you have any friends yes or no? '))

if(askfriends == 'Yes'):
  askfriendsnames = input(str('Oh thats good what are your friends names?'))
elif(askfriends == 'yes'):
  askfriendsnames = input(str('Oh thats good what are your friends names?'))
elif(askfriends == 'Y'):
  askfriendsnames = input(str('Oh thats good what are your friends names?'))
elif(askfriends == 'y'):
  askfriendsnames = input(str('Oh thats good what are your friends names?'))
else:
  askfriendsnames = input(str('Oh well what is a few of your family members names? '))
listfriendsnamesaskcrime = input(str('The people you listed names are ' + askfriendsnames + ' and they are very nice names! Anyways just curious have you ever commited a crime? '))

if(listfriendsnamesaskcrime == 'Yes'):
  askwhatcrime = input(str(firstquestion + ' WOAH YOUR GOING TO JAIL, wait, wait wait, what crime? '))
elif(listfriendsnamesaskcrime == 'yes'):
  askwhatcrime = input(str(firstquestion + ' WOAH YOUR GOING TO JAIL, wait, wait wait, what crime? '))
elif(listfriendsnamesaskcrime == 'Y'):
  askwhatcrime = input(str(firstquestion + ' WOAH YOUR GOING TO JAIL, wait, wait wait, what crime? '))
elif(listfriendsnamesaskcrime == 'y'):
  askwhatcrime = input(str(firstquestion + ' WOAH YOUR GOING TO JAIL, wait, wait wait, what crime? '))
else:
  askwhatcrime = input(str('Im a lie detector bot aswell as a question bot I can tell you are lying tell me what crime!?'))

thatsaseriouscrime = input(str('WOAH!! ' + askwhatcrime + ' IS A VERY SERIOUS CRIME... would you do it again? '))
if(thatsaseriouscrime == 'Yes'):
  wouldyoudoitagain = input(str('WHY? ' + askwhatcrime + ' IS A VERY SERIOUS FEDERAL CRIME!!!, but I wont judge '))