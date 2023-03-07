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


    file = open("otchet.txt", "w")
    score = 0
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(len(questions_answers)):
        Q = questions_answers[i]["Q"]
        answers = "Варианты ответа на вопрос:\n"
        for j in range((questions_answers[i]["Acounter"])):
            answers += str(j+1) +")" + str(questions_answers[i]["A" + str(j+1)]) + "  "
        print(Q)
        print(answers)
        file.write("Вопрос который был задан: " + Q + "\n" + answers + "\n")
    file.close()


if __name__ == '__main__':

    game()
    #hi()
