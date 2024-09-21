team1_num = 5
team2_num = 6
score_2 = 42
team1_time = 18015.2
score_1 = 40
challenge_result = "победа команды Мастера кода!"
tasks_total = 82
time_avg = 350.4

line1 = "В команде Мастера кода участников: %d !" % team1_num
print(line1)

line2 = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(line2)

line3 = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(line3)

line4 = "Волшебники данных решили задачи за {} с !".format(team1_time)
print(line4)

line5 = f"Команды решили {score_1} и {score_2} задач."
print(line5)

line6 = f"Результат битвы: {challenge_result}"
print(line6)

line7 = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."
print(line7)