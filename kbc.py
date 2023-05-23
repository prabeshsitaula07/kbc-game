import pyttsx3
engine = pyttsx3.init()

questions = [

  [" What is the capital city of Nepal?" , "Dhading", "Nuwakot", "Gorkha", "Kathmandu", "d"] ,

  [" Who is the present prime minister of Nepal?", "KP Oli", "Puspa Kamal Dahal", "Sher Bahadur Deuba", "Rabi Lamichhane", "b"],
  
  [" Which country won the FIFA World Cup 2022 which was held in Qatar?" , "Portugal", "Argentina", "France", "Brazil",  "b"] ,

  [" How many times India won the T20 World Cup under Virat Kholi's captency?", "0", "1", "2", "3",  "a"],
  
  [" Where was Prabesh Sitaula born?" , "Dhading", "Nuwakot", "Bhaktapur", "Kathmandu",  "a"] ,

  [" Which of the following is not a frontend language?", "HTML", "CSS", "Python", "JS",  "c"],
  
  [" Who started using the quoet 'JAY NEPAL'?" , "BhanuBhakta Aachrya", "Sukhraraj Shastri", "Amar Singh Thapa", "Balabhadra Kunwar",  "b"] ,

  [" What percentage of land of Nepal is used for Agriculture?", "13%", "15%", "17%", "19%", "c"],
  
  [" Who invented zero?" , "Aarya Bhatt", "Thomas Edison", "Aristotle", "Jonathan James", "a"] ,

  [" How many heritage properties are listed in the World Heritage List?", "9" , "10", "13", "17", "b" ],
  
  [" In which district is the 'Fungfung waterfall'?" , "Dhading", "Nuwakot", "Bhaktapur", "Kathmandu", "b"] ,

  [" How many trade points have been opened between Nepal and India?", "21", "23", "25", "27", "c"],
  
  [" What is considered the world's first cashier?" , "Coffee", "Water", "Milk", "Tea",  "d"] ,

  [" Who has used the custom of cutting a child,s placenta after birth?", "Prabesh", "Ram Shah", "Chandra Sumsher", "Amshuverma", "d"],
  
  [" Which country is ruled by two presidents?" , "Sudan", "Samoa", "Sanmarino", "Senegal",  "c"] 
]

name = input("Enter your name to continue this game: ")

level = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 500000, 10000000, 70000000]
money = 0
# print(len(level))
engine.say(f"Hi {name}, Welcome to K B C game.")
engine.runAndWait()
print("RULES OF THE GAME ! ")
engine.say("RULES OF THE GAME \n ")
engine.runAndWait()

print("-- YOUR ANSWER as (a, b, c or d).")
engine.say("ENTER YOUR ANSWER as (a\n b\n c\n or d).")
engine.runAndWait()

print("-- YOUR ANSWER WILL BE WRONG \n  i. IF YOU ENTER THE WRONG OPTION \n ii. IF YOUR ANSWER IS EMPTY \niii. IF YOU ENTER THE OPTIONS EXCEPT a,b,c or d")
engine.say("YOUR ANSWER WILL BE WRONG \n  IF YOU ENTER THE WRONG OPTION \n  IF YOUR ANSWER IS EMPTY \n IF YOU ENTER THE OPTIONS EXCEPT a,b,c or d")
engine.runAndWait()

print("TO QUIT, ENTER 0.\n\n")
engine.say("TO QUIT, ENTER 0.")
engine.runAndWait()


i = 0
for i in range(0, len(questions)):
  question = questions[i]

  print(f"Question for RS. {level[i]}\n")
  engine.say(f"Question for rupees {level[i]}")
  engine.runAndWait()

  print(f"{question[0]}\n")
  engine.say(f"{question[0]}")
  engine.runAndWait()

  print(f"a.{question[1]}   b.{question[2]}\nc.{question[3]}   d.{question[4]}\n\n")
  engine.say(f"option a\n {question[1]}\n  option b\n {question[2]}\noption c\n {question[3]}\n or option d\n {question[4]}")
  engine.runAndWait()

  reply = (input("enter your answer: ")).lower()
  
  if reply == question[-1] :
    print(f"Congratulations, you have won RS.{level[i]}")
    engine.say(f"Your answer is correct. \nCongratulations, you have won Rupees {level[i]}")
    engine.runAndWait()
    if i == 13:
      money = 10000000
    elif i >=9 and i <13:
      money = 320000
    elif i >=4:
      money = 10000
    else:
      money = 0

  elif reply == "0":
    if i == 0:
      print(f"You quit the game. You won nothing, better luck next time {name}.")
      engine.say(f"You quit the game.\n You won nothing, better luck next time {name}.")
      engine.runAndWait()
    else:  
      print(f"You quit the game. You will take home RS.{level[i-1]}")
      engine.say(f"You quit the game. \n You will take home rupees {level[i-1]}")
      engine.runAndWait()
    break
  
  else:
    print(f"Your answer is incorrect. You will take RS.{money}")
    engine.say(f"Your answer is incorrect.\n You will take rupees {money}")
    engine.runAndWait()
    break

