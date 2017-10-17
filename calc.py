import sys

ADD= 'Добавление'
MIN= 'Отнимание'
MLP= 'Умножение'
DIV= 'Деление'
TXT= '\n+...1\n-...2\n*...3\n/...4\n'           #способ обработки
sposob_one = 1
sposob_two = 2
sposob_three = 3
sposob_four = 4
def method(output_param):
    methods= {
        ADD: 'Вы выбрали метод: Добавление',
        MIN: 'Вы выбрали метод: Отнимание',
        MLP: 'Вы выбрали метод: Умножение',
        DIV: 'Вы выбрали метод: Деление'
    }
    choose = methods.get(output_param)
    return choose

def minus(first_n, second_n):
    result = first_n - second_n
    return result

def mlp(first_n, second_n):
    result = first_n * second_n
    return result

def div(first_n, second_n):
    if first_n and second_n == 0:
        return False # Может тут лучше вывести ошибку? тоесть чтоб пользователь знал что произошло?
    else:
        result = first_n / second_n
        return result

if __name__ == '__main__':
    # При воде буквы скрипт падает, необходимо сделать проверку на присутсвие букв и иных знаков таких как !%::, и т.д.
    sposob = (input("Введите способ обработки: {}".format(TXT)))
    if not sposob.isdigit():
        print("Это не число")
    else: 
        first_n = float(input("Введите первое число: "))
        second_n = float(input("Введите второе число: "))

def calc():
    if sposob == 1:
        input_param = ADD
        choose = method(output_param = input_param)
        input_numbers = input("Введите числа для сумирования: ") 
        result = input_numbers.split(' ')
        result = list(map(float, result))  # что будет если один из  элементов списка будет буква? 
        print("{}\n{}".format(choose, sum(result, first_n+second_n)))
    elif sposob == 2:
        input_param = MIN
        choose = method(output_param = input_param)
        result = minus(first_n, second_n)
        print("{}\n{}".format(choose, result))
    elif sposob == 3:
        input_param = MLP
        choose = method(output_param = input_param)
        result = mlp(first_n, second_n)
        print("{}\n{}".format(choose, result))
    elif sposob == 4:
        input_param = DIV
        choose = method(output_param = input_param)
        result = div(first_n, second_n)
        print("{}\n{}".format(choose, result))
    else:
        print("Вы выбрали 0, или число которое меньше либо больше заявленого")
calc()  #может вывести функцию в основной поток выполнения??
sys.exit() # Аналогично