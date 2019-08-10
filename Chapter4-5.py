from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt 
from lxml import objectify

import matplotlib.cm as cm
import string
import pandas as pd
##Using Python 3.7

def SayHello():
    print("hello")

def DoSum(Value1, Value2):
    return Value1 + Value2

def DisplaySum(Value1, Value2):
    print(str(Value1) + ' + ' + str(Value2) + ' = ' +
    str((Value1 + Value2)))

def DisplayMulti(ArgCount = 0, *VarArgs):
    print('You passed ' + str(ArgCount) + ' arguments.', VarArgs)

def TestValue(Value):
    if Value == 5:
        print('Value equals 5!')
    elif Value == 6:
        print('Value equals 6!')
    else:
        print('Value is something else.')
        print('It equals ' + str(Value))

def SecretNumber():
    One = int(input("Type a number between 1 and 10: "))
    Two = int(input("Type a number between 1 and 10: "))
    if (One >= 1) and (One <= 10):
        if (Two >= 1) and (Two <= 10):
            print('Your secret number is: ' + str(One * Two))
        else:
            print("Incorrect second value!")
    else:
        print("Incorrect first value!")

def DisplayMultiString(*VarArgs):
    for Arg in VarArgs:
        if Arg.upper() == 'CONT':
            continue
            print('Continue Argument: ' + Arg)
        elif Arg.upper() == 'BREAK':
            break
            print('Break Argument: ' + Arg)
        print('Good Argument: ' + Arg)

def SecretNumberWhile():
    GotIt = False
    while GotIt == False:
        One = int(input("Type a number between 1 and 10: "))
        Two = int(input("Type a number between 1 and 10: "))
        if (One >= 1) and (One <= 10):
            if (Two >= 1) and (Two <= 10):
                print('Secret number is: ' + str(One * Two))
                GotIt = True
                continue
            else:
                print("Incorrect second value!")
        else:
            print("Incorrect first value!")
        print("Try again!")

#SayHello()
#print(DoSum(10,20))
#DisplaySum(10,30)
#DisplayMulti(3,'Hello',1,True)
#TestValue(1)
#TestValue(5)
#TestValue(6)
#SecretNumber()
#DisplayMultiString('Hello', 'Goodbye', 'First', 'Last')
#DisplayMultiString('Hello', 'Cont', 'Goodbye', 'Break', 'Last')
#SecretNumberWhile()

SetA = set(['Red', 'Blue', 'Green', 'Black'])
print(SetA)
SetB = set(['Black', 'Green', 'Yellow', 'Orange'])
print(SetB)
SetX = SetA.union(SetB) 
SetY = SetA.intersection(SetB) 
SetZ = SetA.difference(SetB) 
print('{0}\n{1}\n{2}'.format(SetX, SetY, SetZ))

MyTuple = (1, 2, 3, (4, 5, 6, (7, 8, 9)))
for Value1 in MyTuple:
    if type(Value1) == int:
        print(Value1)
    else:
        for Value2 in Value1:
            if type(Value2) == int:
                print("\t", Value2)
            else:
                for Value3 in Value2:
                    print("\t\t", Value3)

ListA = ['Orange', 'Yellow', 'Green', 'Brown']
ListB = [1, 2, 3, 4]
for Value in ListB[1:3]:
    print(Value)
for Value1, Value2 in zip(ListA, ListB):
    print(Value1, '\t', Value2)

MyDict = {'Orange':1, 'Blue':2, 'Pink':3}
MyDict.keys()

print('\n')
with open("C:\\Users\\Siva\\Documents\\Certificate in Data Science UT Texas\\Data Science with Python\\Colors.txt", 'rb') as open_file:
    print('Colors.txt content:\n' + open_file.read().decode('UTF-8'))

print('\n')
with open("C:\\Users\\Siva\\Documents\\Certificate in Data Science UT Texas\\Data Science with Python\\Colors.txt", 'rb') as open_file:
    for observation in open_file:
        print('Reading Data: ' + observation.decode('UTF-8'))

print("\n")
print("Sampling")
n = 2
with open("C:\\Users\\Siva\\Documents\\Certificate in Data Science UT Texas\\Data Science with Python\\Colors.txt", 'rb') as open_file:
    for j, observation in enumerate(open_file):
        if j % n==0:
            print('Reading Line: ' + str(j) + ' Content: ' + observation.decode('UTF-8'))

print("\n")
print("Random Sampling")
from random import random
sample_size = 0.25
with open("C:\\Users\\Siva\\Documents\\Certificate in Data Science UT Texas\\Data Science with Python\\Colors.txt", 'rb') as open_file:
    for j, observation in enumerate(open_file):
        if random()<=sample_size:
            print('Reading Line: ' + str(j) + ' Content: ' + observation.decode('UTF-8'))

print("\n")
print("Reading from Text File using Pandas")
color_table = pd.io.parsers.read_csv("C:\\Users\\Siva\\Documents\\Certificate in Data Science UT Texas\\Data Science with Python\\Colors.txt",sep="\t")
print(color_table)

print("\n")
print("Reading from CSV delimited File using Pandas")
titanic = pd.io.parsers.read_csv("C:\\Users\\Siva\\Documents\\Certificate in Data Science UT Texas\\Data Science with Python\\Titanic.csv")
X = titanic[['age']]
print(X)

print("\n")
print("Reading Excel file using Pandas")
xls = pd.ExcelFile("C:\\Users\\Siva\\Documents\\Certificate in Data Science UT Texas\\Data Science with Python\\Values.xls")
trig_values = xls.parse('Sheet1', index_col=None, na_values=['NA'])
print(trig_values)

print("\n")
print('Sending Data in Unstructured File Form')
example_file = ("http://upload.wikimedia.org/" + "wikipedia/commons/7/7d/Dog_face.png")
image = imread(example_file, as_grey=True)
plt.imshow(image, cmap=cm.gray)
plt.show()
print("data type: %s, shape: %s" %(type(image), image.shape))


print("\n")
print("Accessing Data from the Web") 
xml = objectify.parse(open('C:\\Users\\Siva\\Documents\\Certificate in Data Science UT Texas\\Data Science with Python\\XMLData.xml'))
root = xml.getroot()
df = pd.DataFrame(columns=('Number', 'String', 'Boolean'))
for i in range(0,4):
    obj = root.getchildren()[i].getchildren()
    row = dict(zip(['Number', 'String', 'Boolean'], [obj[0].text, obj[1].text, obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)
print(df)

print("\n")
