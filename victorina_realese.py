#Реализация викторины, которая берет количество вопросов, вопрос, ответы, правильные ответы и пояснения
#Три функции, hi() - для приветствия пользователя, game()-основная функция игры, error() - действия при ошибке пользователя
def hi():  # функция приветствия к клиенту
    checkbox = True
    file = open("otchet.txt", "a")  # открываем файл отчета для записи
    print("Приветствую, хотите ли вы поучавствовать в викторине?\nНапишите да или нет.\n")
    while checkbox != False:  # проверка на правильность ввода
        answ = str(input())  # ввод пользователя
        if answ == "да":
            file.write("Викторина началась!\n\n")
            file.close()
            game()  #  запуск самой викторины
            checkbox = False
        elif answ == "нет":
            print("Жаль, хотелось, чтобы вы поучавствовали.")
            checkbox = False
        else:
            print("да либо нет, других вариантов вам пока не доступно.") # если ввод не правильный, повторяем попытку


def game(): # функция викторины
    global score  # испульзуем глобальную переменную для изменения счета во всех функциях программы
    file = open("otchet.txt", "a")  # открываем файл отчета для записи
    print("_____________________\nВикторина начинается!\n")
    num_qa = int(QA.readline()) # берем из файла количество вопросов для выполнения правильного цикла
    for i in range(num_qa):  # цикл проходящий по всем вопросам
        line = QA.readline()[:-1] # читаем каждую строку из файла
        stripped = line.split("/") # разделяем вопрос и ответы по ячейкам массива
        Q = stripped[0][4:] # перменная вопроса
        P = stripped[5][5:] # переменная пояснения
        answers = "Варианты ответа на вопрос:\n"  # создаём список ответов
        O_A = [] # список только ответов
        for j in range(3): # формируем ответы в одну переменную
            answers += str(j+1) + ")" + str(stripped[j+1][6:]) + "  "
            O_A.append(str(stripped[j+1][6:]))
        print("Ответьте на вопрос:\n" + Q)  # вывод вопроса для пользователя
        print(answers, "\n")  # вывод всех предложенных ответов
        file.write("Вопрос который был задан: " + Q + "\n" + answers + "\n\n") # запись в файл отчета о заданом вопросе
        print("Ваш ответ:")
        user_A = str(input())  # ответ пользователя
        
        R_A = stripped[4][7:] # создаем переменную правильного ответа

        if (user_A == "1" or user_A == "2" or user_A == "3") and (O_A[int(user_A) - 1] in R_A):  # проверка на правильность ответа
            score += 10
            file.write("Ответ который дал пользователь: " +
                    str(user_A) + ", заработано 10 баллов\n\n") # запись в файл отчета о зароботке баллов
            print("Поздравляю, вы заработали 10 баллов!\n" + P + "\n")
        else:
            file.write("Ответ который дал пользователь: " +
                    str(user_A) + ",  потеряно 5 баллов\n\n") # запись в файл отчета о потери баллов
            print("Неудача, вы потеряли 5 баллов!\n")
            score -= 5
            file.close()
            error(O_A, Q, answers, R_A, P) # переход в функцию действий при ошибке
            file = open("otchet.txt", "a")
    if score >= 80:
        print("\nОтличная работа!\nВаш счет за викторину: " + str(score) + "\nСпасибо что учавстовали в викторине!!")
        file.write("\nОтличная работа\nБаллы пользователя: " + str(score)) # запись в файл отчета о счете в викторине
    elif score >= 50:
        print("\nХорошая работа!\nВаш счет за викторину: " + str(score) + "\nСпасибо что учавстовали в викторине!!")
        file.write("\nХорошая работа!\nБаллы пользователя: " + str(score)) # запись в файл отчета о счете в викторине
    else: 
        print("\nНе самая выдающаяся работа!\nВаш счет за викторину: " + str(score) + "\nСпасибо что учавстовали в викторине!!")
        file.write("\nНе самая выдающаяся работа!\nБаллы пользователя: " + str(score)) # запись в файл отчета о счете в викторине


def error(O_A, Q, answers, R_A, P):  # функция проверки на правильность повторного ответа при ошибке
    global score
    file = open("otchet.txt", "a")  # открываем файл отчета для записи
    print("Ошибка, вы хотите попробовать ответить ещё раз на этот вопрос?\nПлата: 2 балла\nОтветье да или нет.\n")
    user_answer = str(input()) # ответ пользователя
    if user_answer == "да": # повторный ввод ответа на вопрос
        file.write("Пользователь согласился на повторный ответ за 2 балла\n\n") # запись в файл отчета о повторном ответе
        score -= 2
        print("\nОтветьте на вопрос:\n" + Q)
        print(answers)
        print("\nВведите правильный ответ.\n")
        user_A = str(input())
        if user_A == "1" or "2" or "3" and O_A[int(user_A) - 1] in R_A:  # проверка на правильность ответа
            score += 10
            file.write("Ответ который дал пользователь: " +
                    str(user_A) + ", заработано 10 баллов\n\n") # запись в файл отчета о зароботке баллов
            print("Поздравляю, вы заработали 10 баллов!\n" + P + "\n")
            return score
    elif user_answer == "нет": # пропуск повторного ввода ответа
        print("\nХорошо, переходим к следующему вопросу, если еще остались.")
        file.write("Пользователь отказался от повторного ответа\n\n") # запись в файл отчета об отказе повторного ответа
    else:
        print("Вы снова ответили не правильно, будте внимательны.\nОтвет нужно выбирать из предложенных вариантов.\n")
        file.write("Пользователь отказался на повторный ответ\n\n") # запись в файл отчета об отказе повторного ответа


if __name__ == '__main__': # запуск программы
    score = 0
    QA =  open("Q_A.txt", "r")
    file = open("otchet.txt", "w+")  # создаём файл
    hi()  # запускаем викторину через функцию приветствия
    file.close()  # закрываем файл и созраняем все записи