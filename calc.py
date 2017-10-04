# А где if name = main? #
ADD= 'Добавление'
MIN= 'Отнимание'
MLP= 'Умножение'
DIV= 'Деление'
TXT= '\n+...1\n-...2\n*...3\n/...4\n' 
def method(output_param):
    methods= {
        ADD: 'Вы выбрали метод: Добавление',
        MIN: 'Вы выбрали метод: Отнимание',
        MLP: 'Вы выбрали метод: Умножение',
        DIV: 'Вы выбрали метод: Деление'
        
    }
    choose = methods.get(output_param)
    return choose

def add(x, y):
    result = x + y
    return result

def minus(x, y):
    result = x - y
    return result

def mlp(x, y):
    result = x * y
    return result

def div(x, y):
    result = x / y
    return result

x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
sposob = int(input("Введите способ обработки: {}".format(TXT)))

def calc():
    if sposob == 0 or sposob<0 or sposob>4:
        print("Вы выбрали 0, или число которое меньше либо больше заявленого")
    elif sposob == 1:
        input_param = ADD
        choose = method(output_param = input_param)
        result = add(x, y)
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
        # если у - будет 0? код упадет?
        result = div(x, y)
        print("{}\n{}".format(choose, result))
calc()

## 4) У пользователя должна быть возможность передать более двух значений для суммирования - только для суммирования -- Где это?