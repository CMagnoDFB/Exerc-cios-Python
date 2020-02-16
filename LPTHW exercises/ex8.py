#Definindo a variável string com 4 espaços para formatação
formatter = "{} {} {} {}"
#Print the str formatter, using the format function, and passsing 4 arguments
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    " All you need is love \n",
    "All you need is love \n",
    "All you need is love, love \n",
    "Love is all you need \n"
))