class QuizBrain:
	def __init__(self,q_list):
		self.question_number=0
		self.question_list=q_list
		self.score=0

	def still_has_questions(self):
		return self.question_number < len(self.question_list)

	def check_answer(self,user_answer,correct_answer):
		if user_answer.lower()== correct_answer.lower():
			print("\n")
			print("You got it !!!!!!!!!!!!!!!!\n")
			self.score+=1
			
		else:
			print("\n")
			print("Oops!!!.. That is wrong. :( :( \n")

		print(f"The correct answer was: {correct_answer}\n")
		print(f"Your Score is:({self.score}/{self.question_number})\n")



	def next_question(self):
		current_question=self.question_list[self.question_number]
		self.question_number+=1
		user_answer=input(f"Q.{self.question_number}.{current_question.text}(True/False)?:      \n")
		# correct_answer=current_question.answer
		self.check_answer(user_answer,current_question.answer)


	


