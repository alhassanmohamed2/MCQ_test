'''This Program Simply Proves a point of view that says that it's possible that a number of students that 
simply didn't know anything about a MCQ exam passed in it by randomly choich an answer in each question 
eventhough the precentage of them is very very low.
'''

import random
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

students_num = 10000
number_of_questions = 10
test_answer_list =  ['d', 'a', 'c', 'c', 'd', 'd', 'b', 'd', 'b', 'b']
choise_list = ['a', 'b', 'c', 'd']
student_answered_list = []
mark = 0
precentge = 0
students_precentge_list = []



# for i in range(number_of_questions):
# 	test_answer_list.append(random.choice(choise_list))

for j in range(students_num):
	for x in range(number_of_questions):
		student_answered_list.append(random.choice(choise_list))
	for y in range(number_of_questions):
		if student_answered_list[y] == test_answer_list[y]:
			mark += 1

	precentge = (mark/number_of_questions) * 100
	students_precentge_list.append(precentge)
	mark = 0
	precentge = 0
	student_answered_list = []

students_precentge_list = np.array(students_precentge_list)
succuess_students = np.count_nonzero(students_precentge_list>=60)

temp = np.partition(-students_precentge_list, succuess_students)
high_marks_list = -temp[:succuess_students]

if succuess_students == 0:
	print(f'All marks \n{students_precentge_list}\n')
else:
	print(f'Passed marks \n{high_marks_list}\n')	
print(f'The number of all Students {students_num}\n')
print(f'The number of Passed Students {succuess_students}\n')
print(f'The precentge of Passed Students {succuess_students/students_num}%\n')
print(f'The highest Student mark { 0 if len(high_marks_list) == 0 else np.max(high_marks_list)}%\n')
print(f'The number of Students take full mark {np.count_nonzero(students_precentge_list == 100)}\n')
print(f'The mean value of students marks {np.mean(students_precentge_list)}%')
