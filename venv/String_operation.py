import re

a = "   "+"tHis iz your homeWork, copy these Text to variable. ".capitalize()+"\n"

b = "   "+"You NEED TO normalize it fROM letter CASEs point oF View.".capitalize()

c = "also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph. ".capitalize()+"\n"

d = "   "+"it iZ misspeLLing here. ".capitalize()
e = "fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. ".capitalize()+"\n"

f = "   "+"last iz TO calculate nuMber OF Whitespace characteRS in this Text. ".capitalize()

g = "caREFULL, not only Spaces, but ALL whitespaces. I got 87.".capitalize()

append_text = ["Variable is to save value of program. Sentence is used to express something.",
               "Paragraph represent an article.",
               "Mistake is maybe a wrong thing.",
               "Whitespaces are characters that used to divide strings.",
               "87 is a number."]
# concate the sentences
long_text = ''.join(a + b + c + d+e+f+g)
print(long_text, '\n')
# calculate all whitespaces: space plus \t
countSpace = len(re.findall(' ', long_text)) + len(re.findall('	', long_text) * 4)
print("Number of whitespaces is: ", countSpace, '\n')

# prepare the append string
long_text_append = ''.join(append_text)
# print(long_text_append, '\n')

# append at the end of the paragraph
long_text_joined = long_text + long_text_append
# print(long_text_joined, '\n')

# replace the mistake 'iz' to 'is'
long_text_joined = long_text_joined.replace('iz', 'is').replace('fix“is”', 'fix“iz”')
print(long_text_joined, '\n')
