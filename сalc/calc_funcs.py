import tkinter

after_oper_flag = False
after_total_flag = False
is_comma_flag = False


def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_oper(symbol: chr) -> bool:
    if symbol in ['+', '-', '/', '×']:
        return True
    else:
        return False


def check_int(num: float) -> float | int:
    if num.is_integer():
        return int(num)
    else:
        return num


def check_comma_num(output_lbl: tkinter.Label) -> None:
    global is_comma_flag
    if is_comma_flag:
        if not is_number(output_lbl['text']):
            output_lbl['text'] = output_lbl['text'].replace('.', '')
        else:
            output_lbl['text'] = str(float(output_lbl['text']))


def get_expression_lst(prev_input_lbl: tkinter.Label) -> list:
    expression = prev_input_lbl['text'].split()
    return expression


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

    return result


def is_first_press(output_lbl: tkinter.Label) -> bool:
    if float(output_lbl['text']) == 0 and is_comma_flag is False:
        return True
    else:
        return False


def comma_btn(output_lbl: tkinter.Label) -> None:
    global is_comma_flag
    global after_oper_flag
    global after_total_flag

    if output_lbl['text'].find('.') != -1:
        return

    if is_comma_flag is False:
        output_lbl['text'] += '.'
        is_comma_flag = True
        after_oper_flag = False
        after_total_flag = False
    else:
        return


def num_btn(prev_input_lbl: tkinter.Label, output_lbl: tkinter.Label, num: str) -> None:
    global after_oper_flag
    global after_total_flag
    global is_comma_flag

    len_output_lbl = len(output_lbl['text'])
    if after_oper_flag:
        output_lbl['text'] = num
        after_oper_flag = False

        is_comma_flag = False
    elif after_total_flag:
        prev_input_lbl['text'] = ''
        output_lbl['text'] = num
        after_total_flag = False
        is_comma_flag = False
    elif is_first_press(output_lbl):
        output_lbl['text'] = num
    elif len_output_lbl < 16:
        output_lbl['text'] += num
    else:
        return


def oper_btn(prev_input_lbl: tkinter.Label, output_lbl: tkinter.Label, oper: str) -> None:
    global after_oper_flag
    global after_total_flag
    global is_comma_flag

    expression = get_expression_lst(prev_input_lbl)

    if expression and after_oper_flag is False:
        if is_oper(expression[-1]):
            after_oper_flag = True
            return total_btn(prev_input_lbl, output_lbl)

    check_comma_num(output_lbl)

    prev_input_lbl['text'] = f'{output_lbl["text"]} {oper}'

    if expression:
        if is_oper(expression[-1]):
            expression[-1] = oper
            prev_input_lbl['text'] = f'{expression[0]} {expression[1]}'

    after_oper_flag = True
    after_total_flag = False
    if output_lbl['text'].find('.') == -1:
        is_comma_flag = False


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

    if after_total_flag:
        expression[0] = output_lbl['text']
        prev_input_lbl['text'] = f'{expression[0]} {expression[1]} {expression[2]} ='

    first_operand = float(expression[0])
    oper = expression[1]
    sec_operand = float(expression[2])

    res = oper_handler(first_operand, sec_operand, oper)

    return res


def total_btn(prev_input_lbl: tkinter.Label, output_lbl: tkinter.Label) -> None:
    global after_total_flag
    global after_oper_flag
    global is_comma_flag

    check_comma_num(output_lbl)

    prev_input_lbl['text'] += f' {output_lbl["text"]} ='

    result = calculations(prev_input_lbl, output_lbl)
    output_lbl['text'] = str(result)

    after_total_flag = True
    after_oper_flag = False
    if output_lbl['text'].find('.') == -1:
        is_comma_flag = False