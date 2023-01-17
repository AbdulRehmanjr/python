'''
@Author ==> 20021519-101
'''

''' Quesion 1'''
dictionary = {
  "pavement": "a hard surface, usually made of stone, brick, or concrete, that forms a path or roadway",
  "innovation": "the introduction of new ideas or methods",
  "diligent": "hardworking and careful",
  "accomplishment": "something successfully achieved, typically by effort or courage",
  "perseverance": "steadfastness in doing something despite difficulty or delay in achieving success",
  "aspiration": "a strong desire to achieve something",
  "tenacity": "the quality of being able to hold on tenaciously to something",
  "determination": "the quality of being determined to do or achieve something",
  "resilience": "the ability to recover from setbacks or hardships",
  "persistence": "the quality of continuing to exist or occur over a prolonged period of time"
}
print(dictionary) # print all 
print(dictionary["pavement"]) # print thorugh key 
del dictionary["pavement"] # delete
print(dictionary)
dictionary["pavement"] = "added" # add new 
print(dictionary)
dictionary["pavement"] = "no" # update
print(dictionary)

''' Question 2'''
dic = {
    'a':20,
    'b':50,
    'c':11
}
def draw_histogram(dictionary:dict):
    for key, value in dictionary.items():
        if value < 1:
            continue  
        print(key, ": ", end="")
        stars = value // 5 + (value % 5 > 0)
        print("*" * stars)
draw_histogram(dic)
'''Question 3'''
def get_word_len_dict(text):
  
  words = text.split()
  
  dictWord = {}
  
  for word in words:
    
    wordLength = len(word)
    
    if wordLength not in dictWord:
      dictWord[wordLength] = []
      
    dictWord[wordLength].append(word)
    
  for key, value in dictWord.items():
    dictWord[key] = value
    
  return sorted(dictWord.items())

text = "This is a python dictionary code"

s = get_word_len_dict(text)

print(s)
