import sys
ADD= 'Добавление'
MIN= 'Отнимание'
MLP= 'Умножение'
DIV= 'Деление'
TXT= '\n+...1\n-...2\n*...3\n/...4\n'           #способ обработки
def method(output_param):
    methods= {
        ADD: 'Вы выбрали метод: Добавление',
        MIN: 'Вы выбрали метод: Отнимание',
        MLP: 'Вы выбрали метод: Умножение',
        DIV: 'Вы выбрали метод: Деление'
        
    }
    choose = methods.get(output_param)
    return choose

def minus(x, y):
    result = x - y
    return result

def mlp(x, y):
    result = x * y
    return result

def div(x, y):
    result = x / y
    return result
if __name__ == '__main__':
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    sposob = int(input("Введите способ обработки: {}".format(TXT)))
def calc():
    if sposob == 0 or sposob<0 or sposob>4:
        print("Вы выбрали 0, или число которое меньше либо больше заявленого")
    elif x == 0 or y == 0:
        print("Вы ввели 0")                         #если будет 0 - прога не запуститься
    elif sposob == 1:
        z = float(input("Введите третье число: "))
        a = float(input("Введите четвертое число: "))
        input_param = ADD
        choose = method(output_param = input_param)
        result = sum( [x, y, z, a] )                #сделал через сум, как ты говорил
        print("{}\n{}".format(choose, result))
    elif sposob == 2:
        input_param = MIN
        choose = method(output_param = input_param)
        result = minus(x, y)
        print("{}\n{}".format(choose, result))
    elif sposob == 3:
        input_param = MLP
        choose = method(output_param = input_param)
        result = mlp(x, y)
        print("{}\n{}".format(choose, result))
    elif sposob == 4:
        input_param = DIV
        choose = method(output_param = input_param)
        result = div(x, y)
        print("{}\n{}".format(choose, result))
calc()
sys.exit()