'''import re
str = "ababbababa"
matches = re.findall(r"ab*", str)
print(matches)'''
'''import re
str = "ababbababa"
matches = re.findall(r"ab{2,3}", str)
print(matches)'''
'''import re
str = "AbabABAb. ababaABB"
matches = re.findall(r"[a-z]+_[a-z]+", str)
print(matches)'''
'''import re
str = "AbabABAb. ababaABB"
matches = re.findall(r"[A-Z][a-z]+", str)
print(matches)'''
'''import re
str = "AbabABAb. ababaABB"
matches = re.findall(r"a.*b", str)
print(matches)'''
'''import re
str = "AbabABAb. ababaABB"
matches = re.sub(r"[ ,.]", ":", str)
print(matches)'''
'''text = "hello_world_this_is_a_test"
words = text.split("_")
camel_words = [words[0]] + [word.capitalize() for word in words[1:]]
camel_text = "".join(camel_words)
print(camel_text)  '''
'''import re
str = "AbabABAb. ababaABB"
matches = re.findall(r"[A-Z][^A-Z]*", str)
print(matches)'''
'''
text = "ThisIsACamelCaseString"
words = []
current_word = ""
for char in text:
  if char.isupper():
    if current_word:
      words.append(current_word)
    current_word = char
  else:
    current_word += char
if current_word:
  words.append(current_word)
new_text = " ".join(words)
print(new_text)
'''
def camel_to_snake(text):
  snake_text = ""
  for char in text:
    if char.isupper():
      snake_text += "_" + char.lower()
    else:
      snake_text += char
  return snake_text
text = "ThisIsACamelCaseString"
snake_text = camel_to_snake(text)
print(snake_text)  