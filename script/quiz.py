quiz = {
    "question1": {
        "question": "Stopping smoking is about will power and being steadfast. you can stop safely by having bupropion or nicotine patch cover initially in consult with a doctor. contact an addiction clinic near you. wishing you best of health thanks",
        "answer": "how do i stop smoking now"
    },
    "question2": {
        "question": "This sounds quite unfamiliar that due to no reason at this age you have no cycle for last three months. pregnancy is surely a remote possibility as there was a tubal ligation. the endometriosis is also unlikely could cause stoppage of cycle. you definitely need some hormonal tests like thyroid or prolactin to know the balance inside as well as an withdrawal bleeding. meet your doctor for an evaluation.",
        "answer": "I had a tubaligation 4 years",
    },
    "question3": {
        "question": "Thanks for submitting your question here. as per the description you have undergone repeated surgery for ovarian torsion where the ovary is preserved. this sounds a bit different as in torsion it is a dictum to remove the whole ovary. now as you are having recurrent pain from the ovaries you need an obg consultation right now. there may be possibility of endometriosis which might present with similar feature. you need to have the biopsy of previous operation and only after few blood tests and clinical examination; a definite opinion can be formed. sincerely dr bhattacharyya",
        "answer": "hello",
    }
}

score = 0

for key,value in quiz.items():
  print(value['question'])
  answer  = input("Answer ? ")

  if answer.lower() == value["answer"].lower():
      print("Correct")
      score = score + 1


print("You won !" + str(score))