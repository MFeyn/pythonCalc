import tkinter
import calc_funcs as cf

CalcWindow = tkinter.Tk()
CalcWindow.title('Calculator')

frm_form = tkinter.Frame()

lbl_num = tkinter.Label(frm_form, text='0')
btn_throw = tkinter.Button(frm_form, text='Бросить', command=lambda: cf.throw_dice(lbl_num))

frm_form.pack(fill=tkinter.BOTH, expand=True)
btn_throw.pack(fill=tkinter.BOTH, pady=3, expand=True)
lbl_num.pack(fill=tkinter.BOTH, expand=True)

CalcWindow.mainloop()
