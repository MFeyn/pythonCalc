import tkinter

# operand_fst = 0
# operand_sec = 0
# operator = ''

after_oper_flag = False
after_total_flag = False

# def is_number(s: str) -> bool:
#     try:
#         float(s)
#         return True
#     except ValueError:
#         return False


def is_oper(symbol: str) -> bool:
    if symbol in ['+', '-', '/', '×']:
        return True
    else:
        return False


def check_int(num: float) -> float | int:
    if num.is_integer():
        return int(num)
    else:
        return num


def get_expression_lst(prev_input_lbl: tkinter.Label) -> list:
    expression = prev_input_lbl['text'].split()
    return expression


# def output_res(output_lbl: tkinter.Label) -> None:
#     global result
#     global operand_fst
#     global operand_sec
#
#
#     output_lbl['text'] = str(result)
#     operand_fst = 0
#     operand_sec = 0

# 5=5 fix total func/oper
def oper_handler(first_operand: float, sec_operand: float, oper: str) -> float | int:
    match oper:
        case '+':
            result = sum_nums(first_operand, sec_operand)
        case '-':
            result = subtraction(first_operand, sec_operand)
        case '×':
            result = multiplication(first_operand, sec_operand)
        case '/':
            result = division(first_operand, sec_operand)
        case _:
            result = 'Error'

    # if oper == '+':
    #     result = sum_nums(operand_fst, operand_sec)
    # elif oper == '-':
    #     result = subtraction(operand_fst, operand_sec)
    # elif oper == '×':
    #     result = multiplication(operand_fst, operand_sec)
    # elif oper == '/':
    #     result = division(operand_fst, operand_sec)

    return result


def is_first_press(output_lbl: tkinter.Label) -> bool:
    if float(output_lbl['text']) == 0:
        return True
    else:
        return False
#
#
# def is_total_pressed(prev_input_lbl: tkinter.Label) -> bool:
#     if prev_input_lbl['text'] != '' and prev_input_lbl['text'][-1] == '=':
#         return True
#     else:
#         return False


# add spaces?
# comma doesn't count (len check)
# OPERATOR CAN'T PASS FIRST IF       SOLVED
def num_btn(prev_input_lbl: tkinter.Label, output_lbl: tkinter.Label, num: str) -> None:
    # if prev_input_lbl['text'] != '':
    #     expression = get_expression_lst(prev_input_lbl)
    #     if is_oper(expression[-1]):
    #         output_lbl['text'] = num
    global after_oper_flag
    global after_total_flag

    len_output_lbl = len(output_lbl['text'])
    if after_oper_flag:
        output_lbl['text'] = num
        after_oper_flag = False
    elif after_total_flag:
        prev_input_lbl['text'] = ''
        output_lbl['text'] = num
        after_total_flag = False
    elif is_first_press(output_lbl):
        output_lbl['text'] = num
    elif len_output_lbl < 16:
        output_lbl['text'] += num
    else:
        return

    # if prev_input_lbl['text'] != '' and is_oper(prev_input_lbl['text'][-1]):
    #     output_lbl['text'] = num
    # elif int(output_lbl['text']) == 0:
    #     output_lbl['text'] = num

    # if len_output_lbl < 16:
    #     output_lbl['text'] += num
    # else:
    #     return


def oper_btn(prev_input_lbl: tkinter.Label, output_lbl: tkinter.Label, oper: str) -> None:
    # global operand_fst
    # global operand_sec
    # global operator

    global after_oper_flag
    global after_total_flag

    # if is_number(output_lbl['text']) and prev_input_lbl['text'] == '':

    # if prev_input_lbl['text'] == '':
    # operand_fst = float(output_lbl['text'])

    expression = get_expression_lst(prev_input_lbl)

    if expression and after_oper_flag is False:
        if is_oper(expression[-1]):
            after_oper_flag = True
            res = calculations(prev_input_lbl, output_lbl)
            output_lbl['text'] = str(res)

    prev_input_lbl['text'] = f'{output_lbl["text"]} {oper}'

    # operator = oper
    # output_lbl['text'] = '0'

    # expression = get_expression_lst(prev_input_lbl)

    # if len(expression) != 0:
    #     if not is_oper(expression[-1]):
    #         prev_input_lbl['text'] += f' {oper}'
    # elif is_total_pressed(prev_input_lbl):
    #     pass

    # if is_oper(expression[-1]) and after_oper_flag is False:
    #     return total_btn(output_lbl, prev_input_lbl)

    if expression:
        if is_oper(expression[-1]):
            expression[-1] = oper
            prev_input_lbl['text'] = f'{expression[0]} {expression[1]}'

    after_oper_flag = True
    after_total_flag = False


def sum_nums(num_fst: float, num_sec: float) -> float | int:
    res = num_fst + num_sec
    res = check_int(res)
    return res


def subtraction(num_fst: float, num_sec: float) -> float | int:
    res = num_fst - num_sec
    res = check_int(res)
    return res


def division(num_fst: float, num_sec: float) -> float | int | str:
    try:
        res = num_fst / num_sec
        res = check_int(res)
        return res
    except ZeroDivisionError:
        return 'Zero division error'


def multiplication(num_fst: float, num_sec: float) -> float | int:
    res = num_fst * num_sec
    res = check_int(res)
    return res


def calculations(prev_input_lbl: tkinter.Label, output_lbl: tkinter.Label) -> float | int:
    global after_total_flag
    global after_oper_flag
    expression = get_expression_lst(prev_input_lbl)

    if len(expression) == 0 or expression[1] == '=':
        expression = get_expression_lst(output_lbl)
        prev_input_lbl['text'] = f'{expression[0]} ='
        return check_int(float(expression[0]))

    if after_oper_flag:
        expression.append(output_lbl['text'])
        prev_input_lbl['text'] = f'{expression[2]} {expression[1]}'

    if after_total_flag:
        expression[0] = output_lbl['text']
        prev_input_lbl['text'] = f'{expression[0]} {expression[1]} {expression[2]} ='

    first_operand = float(expression[0])
    oper = expression[1]
    sec_operand = float(expression[2])

    res = oper_handler(first_operand, sec_operand, oper)
    return res


def total_btn(prev_input_lbl: tkinter.Label, output_lbl: tkinter.Label) -> None:
    # global operand_fst
    # global operand_sec
    # global operator

    global after_total_flag
    global after_oper_flag

    prev_input_lbl['text'] += f' {output_lbl["text"]} ='

    # expression = get_expression_lst(prev_input_lbl)

    # if after_total_flag:
    #     expression[0] = output_lbl['text']
    #     prev_input_lbl['text'] = f'{expression[0]} {expression[1]} {expression[2]} ='

    # try:
    #     first_operand = float(expression[0])
    #     oper = expression[1]
    #     sec_operand = float(expression[2])
    # except IndexError:
    #     prev_input_lbl['text'] = ''
    #     output_lbl['text'] = 'Error'
    #     return

    result = calculations(prev_input_lbl, output_lbl)
    output_lbl['text'] = str(result)

    # operand_sec = float(output_lbl['text'])
    # sec_op_out = check_int(operand_sec)
    # res = oper_handler(operator)
    #
    # prev_input_lbl['text'] += f' {sec_op_out} ='
    # output_lbl['text'] = str(res)
    # operand_fst = 0
    # operand_sec = 0

    after_total_flag = True
    after_oper_flag = False

