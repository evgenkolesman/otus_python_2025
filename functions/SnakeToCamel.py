def snake_to_camel(word_in_camel_case: str):
    if "_" not in word_in_camel_case:
        return "Cannot be converted to camel case"
    else:
      words_need_to_rework =  word_in_camel_case.split("_")
      result =""
      for a in range(len(words_need_to_rework)):
          if a == 0:
              result = words_need_to_rework[a]
          else:
              result += words_need_to_rework[a].title()
      return result


value = input("Enter a word in snake case: ")
print(snake_to_camel(value))
