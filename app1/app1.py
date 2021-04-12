import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
   # print(word)
    result = get_close_matches(word,data.keys(),cutoff=0.8)
    #print(result)
    if word.lower() in data:
        return data[word]
    elif word.title() in data:
        print("title block")
        return data[word.title()]
    
    elif word.upper() in data:
        print("upper block")
        return data[word.upper()]
    
    elif len(result)>0:
        reply = input("Did you mean %s instead " % result[0])
       # print("Input Taken ")
        if reply == 'Y':
            print("Check done {}".format(reply))
            return data[result[0]]
        else:
            return 'Sorry ...Double check it We cant find a suitable word '
    else:
        print(" {} doesn't exist ".format(word))
        
word = input("Enter the word : ")
output = translate(word)
if type(output)== list:
    for i in output:
        print(i)
else:
    print(output)


