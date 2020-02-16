print("Mary had a little lamb.")
#Quando coloquei várias curly braces vazias na linha abaixo (achando que todos iam ser substituídos por 'snow',
#o terminal me deu um erro 'tuple index out of range' - ainda não sei o que são tuples)
print("Its fleece was white as {}".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  #what'd that do?

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

#watch end = ' ' at the end. try removing to see what happens
#end=' ' significa que não se irá separar a próxima linha por um "enter", mas sim por um espaço
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)