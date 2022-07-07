#get the lists of maori and english words

english_line = "red,white,black,blue,green,yellow"
maori_line = "whero,ma,panga,kahurangi,kakariki,kowhai"

english = english_line.split(",")
maori = maori_line.split(",")

#write a function to perform the quiz
def do_quiz():
  """
  main quiz code
  """
  score = 0
  print('starting quiz')
  #start a loop
  for i in range(6):
    print('Question ',i)
    question = "What is the maori name for " + english[i]
    #print(question)
    #ask the next/first question
    user_response = input(question + "\n")
    print(user_response)
  #compare response with the correct answer
    if user_response == maori[i]:
      print("Correct")
      score += 1
    else:
      print('incorrect')
      pass
  #amend  tte  score
  #report back
  #display total score.
  print(f"You scored {score}.")

if __name__ == '__main__':
  do_quiz()