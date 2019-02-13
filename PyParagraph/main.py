import re

#path= r'C:\Users\ahsanmuh\Desktop\Data Analytics and Visualization\UTAUS201901DATA3\homework-instructions\03-Python\ExtraContent\Instructions\PyParagraph\raw_data\paragraph_1
#.txt'
path = os.path.join('..','Resources', 'paragraph_1.txt')
file = open(path,'r')
paragraph = ""
for line in file:
    paragraph +=line


sentence_count = re.split("(?<=[.!?]) +", paragraph)
letter_count = re.split("[a-zA-Z]{1}", paragraph)
word_count = re.split("[a-zA-Z]+", paragraph)

print ('Paragraph Analysis')
print ('-----------------')
print (f'Approximate Word Count: {len(word_count)}')
print (f'Approximate Sentence Count: {len(sentence_count)}')
print (f'Average Letter Count: {len(letter_count)/len(word_count)}')
print (f'Average Sentence Length: {len(word_count)/len(sentence_count)}')
