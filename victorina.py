from Q_A import questions_answers



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


    file = open("otchet.txt", "w") # создаём файл
    score = 0
    print("____________________________________")
    for i in range(len(questions_answers)): # цикл проходящий по всем вопросам
        Q = questions_answers[i]["Q"]

        answers = "Варианты ответа на вопрос:\n" # создаём список ответов
        for j in range((questions_answers[i]["Acounter"])):
            answers += str(j+1) +")" + str(questions_answers[i]["A" + str(j+1)]) + "  "
        print(Q)
        print(answers)
        file.write("Вопрос который был задан: " + Q + "\n" + answers + "\n")
        
        user_A = int(input()) # ответ пользователя
        R_Acounter_mass = []
        for j in range((questions_answers[i]["R_Acounter"])): # создаём список правильных ответов
            R_Acounter_mass.append(questions_answers[i]["R_A" + str(j+1)])

        if user_A in R_Acounter_mass: # проверка на правильность ответа
            score += 1
        else:
            error(R_Acounter_mass, Q, answers, score)
    print(score)
            
        
    file.close()



def error(R_Acounter_mass, Q, answers, score): # функция проверки на правильность ответа при ошибке

    print("Ошибка, вы хотите попробовать ещё раз?\n Это будет стоить 0.5 баллa\n Ответье да или нет")
    user_answer = str(input())
    if user_answer == "да":
        print(Q)
        print(answers)
        print("Введите правильный ответ")
        user_A = int(input())
        if user_A in R_Acounter_mass: # проверка на правильность ответа
            score += 1


if __name__ == '__main__':

    game()
    #hi()
