import random
# How do I do this with this tech?
# Any question on stackoverflow can be divided into for pieces.
# Each of these arrays contains a piece of a question.
one = ["How do I use ", "How to ", "Maybe I'm a bit thick, but how do I do ",
       "Maybe I'm a bit thick, but how do I use ", "How to install ",
       "How can I do ", "How to get ", "How to ignore ", "What is ", "How to get ",
       "How to use ", "Can anyone help me to use ", "Can anyone help me to create a "]

two = ["an array ", "an object ", "console.log ",
       "a dictionary ", "a function ", "get a job ",
       "C++ ", "load ", "JSON ", "data ", "[object Object] ",
       "variables ", "computed values ", "print() ", "array.sort() ",
       "API ", "Chat bot ", "Twitter bot ", "github clone "]

three = ["with ", "in ", "on ", "using ", "using only ", "against ", "to ",
         "within ", "without ", "despite "]

four = ["Androind", "MacOS", "Arch Linux", "Windows XP", "VueJS",
        "React", "React native", "VueJS Native", "ElectronJS",
        "Express", "NestJS", "Python", "Ruby", "Ruby On Rails", "Swift",
        "GoLang", "C++", "C", "Visual Basic", "Microsoft Excel", "GIMP", "Python",
        "Web Assembly", "Android Studio", "Kotlin", "Google Chrome", "Javascript",
        "Typescript", "NodeJS", "Java", "COBOL", "Fortran", "C#", "The new Mac Mini"]


def chooseFromArray(array):
    x = random.randint(0, len(array) - 1)
    return array[x]


def generateQuestion():
    firstPart = chooseFromArray(one)
    secondPart = chooseFromArray(two)
    thirdPart = chooseFromArray(three)
    fourthPart = chooseFromArray(four)

    question = firstPart + secondPart + thirdPart + fourthPart + "?"
    # print(question)
    return question
