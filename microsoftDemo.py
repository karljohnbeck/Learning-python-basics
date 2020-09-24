# # name = input("whats your name?")
# # print('hello')
# # print(name)

print("another line")

print('math time', 2 / 2)

print("chicken math:")
print("hens", 25+ 30 / 6)
print("roosters", 100-25*3%4)

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end.  try removing it to see what happens
# print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 'what?'))



# basic for loop! that prints an array of strings

people = ['me', 'you']

for name in people: 
    print(name)
    
# index = 0 


# while index < len(people):
#     print (people[index])
#     index = index + 1

for i in range(100):
    if i % 3 == 0: 
	    if i % 5 == 0:
			print('fizzbuzz')
		else:			print('fizz')
	elif i % 5 == 0:
		print ('buzz')
	else :
		print('i')

