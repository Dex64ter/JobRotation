def invertaString(s):
  word_reverse=""
  for i in range(len(s)-1,-1,-1):
    word_reverse += s[i]
  print(word_reverse)
  return word_reverse

invertaString("chat")
invertaString("familia")
invertaString("849aaaaaaaaaaabbbbbbbbbbcccccccccc495354984872416598715915")