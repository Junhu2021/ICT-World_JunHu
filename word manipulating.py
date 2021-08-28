## story song “henryTheSquareEaredCat.txt” as follows
##Henry The Square Eared Cat
##
##Once upon a time there was a square eared cat named Henry.
##he did not look like the other cats, for the other cats had pointy ears.
##He was very shy and did not like raising attention to himself.
##He preferred blending in with the other animals.
##
##One day Henry came across a fox.
##And the fox said, "Wow!"
##Henry did not like this, and at that moment he ran away,
##he jumped to the top of the highest tree to hide.
##
##Henry:
##I don't like having square ears.
##I don't like them, not at all.
##All my friends have pointy ears.
##Squares are not for ears at all!
##
##The next morning Henry came across a frog.
##The frog said, "I have never seen square ears before!"
##At this, Henry bolted in the opposite direction,
##he hid behind a giant haystack so that nobody could see him.
##
##Henry:
##I don't like having square ears.
##I don't like them, not at all.
##All my friends have pointy ears.
##Squares are not for ears at all!
##
##later that day Henry came across a sparrow.
##The sparrow pointed and said, "What a sight!"
##Henry then dived into a nearby hole,
##He patiently stayed there hiding until the sparrow flew away.
##
##Henry:
##I don't like having square ears.
##I don't like them, not at all.
##All my friends have pointy ears.
##Squares are not for ears at all!
##
##As the moon came up that evening, Henry was out for a walk.
##To his surprise, he came across all three animals.
##Henry was ready to run!
##Before he could run away,
##the fox said, "Why did you run away?  Wow I love those ears!"
##The frog said "I never seen square ears before, but I like them!"
##The sparrow said "You are the greatest sight I have seen all day!"
##
##Henry did not know how to react, but then it came to him.
##"Perhaps I should not have ran away" he thought!
##Perhaps we can all be friends!
##
##The three friends then sang together:
##We love square ears!
##They appear to hear quite clear!
##Squares can be for anything!
##We love them after all!
##
##From that day forward, the three friends embraced each other.
##And the fox, the frog, the sparrow, and Henry lived happily ever after.

## The description of the program is listed as below
##a)	Reads the story: “henryTheSquareEaredCat.txt”
##
##b)	Have your program create a new story called “henryThePentagonEaredCat.txt”
##
##c)	In this new txt file replace every word “Square” with the word “Pentagon.”
##•	Be careful to replace “Squares” with a capital “S” with “Pentagons” with a capital “P”
##•	Same goes for lower case!
##
##d)	Have your program close the file “henryTheSquareEaredCat.txt” when done replacing all squares with pentagons.
##
##e)	Ask the user if they want to keep the newly generated file “henryThePentagonEaredCat.txt”
##
##f)	If the user inputs “n” for no, delete the new file. If the user inputs “y” for yes, keep the new file.


## Reads the story: “henryTheSquareEaredCat.txt”
file = open ('henryTheSquareEaredCat.txt', mode = 'r')
## create an empty list to add new lines with new changes
newLines = []
## replace lines with square or Square with pentagon or Pentagon
for line in file:
    if 'square' in line:
        newLine = line. replace('square','pentagon')
        newLines.append(newLine)
    elif 'Square' in line:
        newLine = line. replace('Square','Pentagon')  
        newLines.append(newLine)
    else:
        newLines.append(line)
## close the file
print(newLines)
print('')
file.close()

## create a new story file called “henryThePentagonEaredCat.txt”
with open ('henryThePentagonEaredCat.txt', mode = 'w') as newFile:
    for newLine in newLines:
        newFile.write(newLine)
## close the file 
## newFile.close()

## create yes/no option for the user
import os
def to_lower(myString):
    return str(myString.lower())
def to_yes_no(yesNo):
    return to_lower(yesNo)
## If the user inputs “n” for no, delete the new file. If the user inputs “y” for yes, keep the new file
decision = input (' would you like o keep the newly generated file “henryThePentagonEaredCat.txt (y/n)(Yes/No)? : \n')
if ('y' == to_lower(decision) or 'yes' == to_yes_no(decision)):
    print (' you file is saved')
    newFile.close()
else:
    print (' your file is deleted')
    os.remove('henryThePentagonEaredCat.txt')
