import random, os

#Function to generate list of Multiplication problems.
def init_problems(max):
    problem_list = []
    for a in range(0, max + 1):
        for b in range(0, max + 1):
            # Add PROBLEM & ANSWER to dictionary to list.
            problem_list.append({'problem': str(a) + ' x ' + str(b), 'answer': a * b})
    return problem_list

max_factor = 12
problems = init_problems(max_factor)
total_problems = len(problems)

random.shuffle(problems)
correct = []
incorrect = []

while len(problems) > 1:
    question = problems.pop()
    answer = raw_input(question['problem'] + '? ')

    try:
        if question['answer'] == int(answer):
            correct.append(question)
            print 'Good!'
            continue
    except ValueError:
        print 'That wasn\'t even a number'

    incorrect.append(question)

    print 'Incorrect!'

grade = len(correct) / float(total_problems)  * 100

report = 'Incorrect: ' + str(len(incorrect)) +\
         '\nCorrect: ' + str(len(correct)) +\
         '\nGrade: ' + '{:03.2F}'.format(grade) + '%'

print report

log = open('/Users/kelbycannick/Desktop/kelbylog1.txt', 'w+')

log.write(report)
log.write('\nMissed Problems\n---------------------\n')

for line in incorrect:
    log.write(line['problem'] + ' = ' + str(line['answer']) + '\n')

log.close()
