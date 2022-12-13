count = 0
print("Welcome to the KBC game")
press = int(input(print("Press 1 if you want to play otherwise 2 ")))
if press == 1:
  print(
    "\nOk lets start! Here, I will ask you 7 questions and for each correct answer you will get 1 lacs rupees. Please note that there is no negative marking for wrong answer.\n"
  )
  print("Question 1: What is the capital of India?")
  a = input()
  if a.lower() == "new delhi":
    count = count + 1
    print("correct answer\n")
  else:
    print("Wrong answer\n")
  print("Question 2: What is the capital of France?")
  a = input()
  if a.lower() == "paris":
    count = count + 1
    print("correct answer\n")
  else:
    print("Wrong answer")
  print("Question 3: What is the capital of Spain?")
  a = input()
  if a.lower() == "madrid":
    count = count + 1
    print("correct answer\n")
  else:
    print("Wrong answer\n")
  print("Question 4: What is the capital of Maldives?")
  a = input()
  if a.lower() == "male":
    count = count + 1
    print("correct answer\n")
  else:
    print("Wrong answer\n")
  print("Question 5: What is the capital of Bangladesh?")
  a = input()
  if a.lower() == "dhaka":
    count = count + 1
    print("correct answer\n")
  else:
    print("Wrong answer\n")
  print("Question 6: What is the capital of Canada?")
  a = input()
  if a.lower() == "ottawa":
    count = count + 1
    print("correct answer\n")
  else:
    print("Wrong answer\n")
  print("Question 7: What is the capital of Russia?")
  a = input()
  if a.lower() == "moscow":
    count = count + 1
    print("correct answer\n")
  else:
    print("Wrong answer\n")

  count1 = count * 100000
  print(
    f"Congratulatoins you have won {count1} rupees by answering {count} correct questions."
  )

else:
  print("Thankyou")
