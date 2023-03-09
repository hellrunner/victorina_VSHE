from Q_A import questions_answers
from Q_A import score


def hi(): # функция приветствия к клиенту
    checkbox = True
    print("Приветствую, хотите ли сыграть в викторину?\nНапишите да или нет")
    while checkbox != False: # проверка на правильность ввода
        answ = str(input())
        if answ == "да":
            print("prog")
            checkbox = False
        elif answ == "нет":
            print("prog")
            checkbox = False
        else: print("да либо нет, других вариантов вам пока не доступно")
        # если ввод не правильный, повторяем попытку


def game():
    global score

    file = open("otchet.txt", "w") # создаём файл
    print("____________________________________")
    for i in range(len(questions_answers)): # цикл проходящий по всем вопросам
        Q = questions_answers[i]["Q"]

        answers = "Варианты ответа на вопрос:\n" # создаём список ответов
        for j in range((questions_answers[i]["Acounter"])):
            answers += str(j+1) +")" + str(questions_answers[i]["A" + str(j+1)]) + "  "
        print(Q)
        print(answers)
        file.write("Вопрос который был задан: " + Q + "\n" + answers + "\n")
        
        user_A = str(input()) # ответ пользователя
        R_Acounter_mass = []
        for j in range((questions_answers[i]["R_Acounter"])): # создаём список правильных ответов
            R_Acounter_mass.append(str(questions_answers[i]["R_A" + str(j+1)]))

        if user_A in R_Acounter_mass: # проверка на правильность ответа
            score += 10
            file.write("Ответ который дал пользователь: " + str(user_A) + " заработано 10 баллов\n")

        else:
            error(R_Acounter_mass, Q, answers)
    print(score)
            
        
    file.close()



def error(R_Acounter_mass, Q, answers): # функция проверки на правильность ответа при ошибке
    global score
    file = open("otchet.txt", "a")
    print("Ошибка, вы хотите попробовать ещё раз?\n Это будет стоить 5 баллов\n Ответье да или нет")
    user_answer = str(input())
    if user_answer == "да":
        file.write("Пользователь согласился на повторный ответ за 5 баллов\n")
        score -= 5

        print(Q)
        print(answers)
        print("Введите правильный ответ")
        user_A = str(input())
        if user_A in R_Acounter_mass: # проверка на правильность ответа
            score += 10
            file.write("Ответ который дал пользователь: " + str(user_A) + " заработано 10 баллов\n")
            return score
    elif user_answer == "нет":
        pass
    else:


if __name__ == '__main__':

    game()
    #hi()
