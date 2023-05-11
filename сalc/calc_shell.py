import tkinter
import calc_funcs as cf

CalcWindow = tkinter.Tk()
CalcWindow.title('Calculator')


# check widgets size
CalcWindow.rowconfigure(0, weight=1, minsize=100)
CalcWindow.rowconfigure(1, weight=1, minsize=50)
for i in range(2, 6):
    CalcWindow.rowconfigure(i, weight=1, minsize=100)

CalcWindow.columnconfigure(0, weight=1, minsize=400)


# OUTPUT FRAME
frm_output = tkinter.Frame(CalcWindow, borderwidth=3, relief=tkinter.GROOVE, padx=5, pady=5)
lbl_prev_input = tkinter.Label(frm_output, font=('Arial', 15))
lbl_output = tkinter.Label(frm_output, text='0', font=('Arial', 20))

frm_output.columnconfigure(0, weight=1)
frm_output.rowconfigure(0, weight=1)
frm_output.rowconfigure(1, weight=1)
# check resize
frm_output.grid(row=0, column=0, sticky='nswe')
lbl_prev_input.grid(row=0, column=0, padx=15, sticky='e')
lbl_output.grid(row=1, column=0, padx=15, sticky='e')

# MEMORY BUTTONS FRAME
frm_mem_btns = tkinter.Frame(CalcWindow, borderwidth=3, relief=tkinter.SUNKEN, pady=5, padx=5)
btn_mem_clear = tkinter.Button(frm_mem_btns, text="MC")  # mem clear
btn_mem_rem = tkinter.Button(frm_mem_btns, text='MR')  # mem remember
btn_mem_plus = tkinter.Button(frm_mem_btns, text='M+')  # mem plus
btn_mem_minus = tkinter.Button(frm_mem_btns, text='M-')  # mem minus
btn_mem_save = tkinter.Button(frm_mem_btns, text='MS')  # mem save

for i in range(5):
    frm_mem_btns.columnconfigure(i, weight=1)
frm_mem_btns.rowconfigure(0, weight=1)

frm_mem_btns.grid(row=1, column=0, pady=5, padx=5, sticky='nswe')

btn_mem_clear.grid(row=0, column=0, padx=3, sticky='nswe')
btn_mem_rem.grid(row=0, column=1, padx=3, sticky='nswe')
btn_mem_plus.grid(row=0, column=2, padx=3, sticky='nswe')
btn_mem_minus.grid(row=0, column=3, padx=3, sticky='nswe')
btn_mem_save.grid(row=0, column=4, padx=3, sticky='nswe')

# BUTTONS FIELD FRAME
frm_btns_field = tkinter.Frame(CalcWindow)
btn_percent = tkinter.Button(frm_btns_field, text='%')
btn_clear_evrthg = tkinter.Button(frm_btns_field, text='CE')
btn_clear = tkinter.Button(frm_btns_field, text='C')
btn_del = tkinter.Button(frm_btns_field, text='\N{LEFTWARDS BLACK ARROW}')

btn_denom = tkinter.Button(frm_btns_field, text='1/x')
btn_square = tkinter.Button(frm_btns_field, text='x^2')
btn_sqrt = tkinter.Button(frm_btns_field, text='√')
btn_div = tkinter.Button(frm_btns_field, text='/',
                         command=lambda: cf.oper_btn(lbl_prev_input, lbl_output, btn_div['text']))

btn_sev = tkinter.Button(frm_btns_field, text='7',
                         command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_sev['text']))
btn_eight = tkinter.Button(frm_btns_field, text='8',
                           command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_eight['text']))
btn_nine = tkinter.Button(frm_btns_field, text='9',
                          command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_nine['text']))

a = tkinter.StringVar

# mb change symbol
btn_multi = tkinter.Button(frm_btns_field, text='×',
                           command=lambda: cf.oper_btn(lbl_prev_input, lbl_output, btn_multi['text']))

btn_four = tkinter.Button(frm_btns_field, text='4',
                          command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_four['text']))
btn_five = tkinter.Button(frm_btns_field, text='5',
                          command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_five['text']))
btn_six = tkinter.Button(frm_btns_field, text='6',
                         command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_six['text']))
btn_minus = tkinter.Button(frm_btns_field, text='-',
                           command=lambda: cf.oper_btn(lbl_prev_input, lbl_output, btn_minus['text']))

btn_one = tkinter.Button(frm_btns_field, text='1',
                         command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_one['text']))
btn_two = tkinter.Button(frm_btns_field, text='2',
                         command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_two['text']))
btn_three = tkinter.Button(frm_btns_field, text='3',
                           command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_three['text']))
btn_plus = tkinter.Button(frm_btns_field, text='+',
                          command=lambda: cf.oper_btn(lbl_prev_input, lbl_output, btn_plus['text']))

btn_change_sign = tkinter.Button(frm_btns_field, text='+/-')
btn_zero = tkinter.Button(frm_btns_field, text='0',
                          command=lambda: cf.num_btn(lbl_prev_input, lbl_output, btn_zero['text']))
btn_comma = tkinter.Button(frm_btns_field, text='.',
                           command=lambda: cf.comma_btn(lbl_output))
btn_equals = tkinter.Button(frm_btns_field, text='=',
                            command=lambda: cf.total_btn(lbl_prev_input, lbl_output))

for i in range(6):
    frm_btns_field.rowconfigure(i, weight=1)
for j in range(4):
    frm_btns_field.columnconfigure(j, weight=1)

frm_btns_field.grid(row=2, column=0, rowspan=6, padx=5, pady=5, sticky='nswe')

btn_percent.grid(row=0, column=0, padx=3, pady=3, sticky='nswe')
btn_clear_evrthg.grid(row=0, column=1, padx=3, pady=3, sticky='nswe')
btn_clear.grid(row=0, column=2, padx=3, pady=3, sticky='nswe')
btn_del.grid(row=0, column=3, padx=3, pady=3, sticky='nswe')

btn_denom.grid(row=1, column=0, padx=3, pady=3, sticky='nswe')
btn_square.grid(row=1, column=1, padx=3, pady=3, sticky='nswe')
btn_sqrt.grid(row=1, column=2, padx=3, pady=3, sticky='nswe')
btn_div.grid(row=1, column=3, padx=3, pady=3, sticky='nswe')

btn_sev.grid(row=2, column=0, padx=3, pady=3, sticky='nswe')
btn_eight.grid(row=2, column=1, padx=3, pady=3, sticky='nswe')
btn_nine.grid(row=2, column=2, padx=3, pady=3, sticky='nswe')
btn_multi.grid(row=2, column=3, padx=3, pady=3, sticky='nswe')

btn_four.grid(row=3, column=0, padx=3, pady=3, sticky='nswe')
btn_five.grid(row=3, column=1, padx=3, pady=3, sticky='nswe')
btn_six.grid(row=3, column=2, padx=3, pady=3, sticky='nswe')
btn_minus.grid(row=3, column=3, padx=3, pady=3, sticky='nswe')

btn_one.grid(row=4, column=0, padx=3, pady=3, sticky='nswe')
btn_two.grid(row=4, column=1, padx=3, pady=3, sticky='nswe')
btn_three.grid(row=4, column=2, padx=3, pady=3, sticky='nswe')
btn_plus.grid(row=4, column=3, padx=3, pady=3, sticky='nswe')

btn_change_sign.grid(row=5, column=0, padx=3, pady=3, sticky='nswe')
btn_zero.grid(row=5, column=1, padx=3, pady=3, sticky='nswe')
btn_comma.grid(row=5, column=2, padx=3, pady=3, sticky='nswe')
btn_equals.grid(row=5, column=3, padx=3, pady=3, sticky='nswe')


CalcWindow.mainloop()
