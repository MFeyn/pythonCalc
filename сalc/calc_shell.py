import tkinter
import calc_funcs as cf

CalcWindow = tkinter.Tk()
CalcWindow.title('Calculator')

for i in range(8):
    CalcWindow.rowconfigure(i, weight=1)
CalcWindow.rowconfigure(8, weight=2)

for j in range(4):
    CalcWindow.columnconfigure(j, weight=1)

frm_form = tkinter.Frame(borderwidth=3, relief=tkinter.SUNKEN, bg='gray84')
frm_basement = tkinter.Frame(bg='gray84')


lbl_name = tkinter.Label(master=frm_form, text='Имя:', bg='gray84')
ent_name = tkinter.Entry(master=frm_form, width=50)

lbl_surn = tkinter.Label(master=frm_form, text='Фамилия:', bg='gray84')
ent_surn = tkinter.Entry(master=frm_form, width=50)

lbl_first_address = tkinter.Label(master=frm_form, text='Адрес 1:', bg='gray84')
ent_first_address = tkinter.Entry(master=frm_form, width=50)

lbl_second_address = tkinter.Label(master=frm_form, text='Адрес 2:', bg='gray84')
ent_sec_address = tkinter.Entry(master=frm_form, width=50)

lbl_city = tkinter.Label(master=frm_form, text='Город:', bg='gray84')
ent_city = tkinter.Entry(master=frm_form, width=50)

lbl_region = tkinter.Label(master=frm_form, text='Регион:', bg='gray84')
ent_region = tkinter.Entry(master=frm_form, width=50)

lbl_index = tkinter.Label(master=frm_form, text='Почтовый индкес:', bg='gray84')
ent_index = tkinter.Entry(master=frm_form, width=50)

lbl_country = tkinter.Label(master=frm_form, text='Страна:', bg='gray84')
ent_country = tkinter.Entry(master=frm_form, width=50)

lbl_fields = [
    lbl_name,
    lbl_surn,
    lbl_first_address,
    lbl_second_address,
    lbl_city,
    lbl_region,
    lbl_index,
    lbl_country
]

ent_fields = [
    ent_name,
    ent_surn,
    ent_first_address,
    ent_sec_address,
    ent_city,
    ent_region,
    ent_index,
    ent_country
]

btn_clear = tkinter.Button(master=frm_basement, text='Очистить',
                           command=lambda: cf.clear_all_entries(ent_fields), bg='gray84')

btn_send = tkinter.Button(master=frm_basement, text='Отправить',
                          command=lambda: cf.send_all_entries(lbl_fields, ent_fields), bg='gray84')


frm_form.grid(row=0, column=0, rowspan=8, columnspan=4)
frm_basement.grid(row=8, column=0, columnspan=4, sticky='we', ipadx=5, ipady=5)

lbl_name.grid(row=0, column=0, sticky='e')
ent_name.grid(row=0, column=1, columnspan=3)

lbl_surn.grid(row=1, column=0, sticky='e')
ent_surn.grid(row=1, column=1, columnspan=3)

lbl_first_address.grid(row=2, column=0, sticky='e')
ent_first_address.grid(row=2, column=1, columnspan=3)

lbl_second_address.grid(row=3, column=0, sticky='e')
ent_sec_address.grid(row=3, column=1, columnspan=3)

lbl_city.grid(row=4, column=0, sticky='e')
ent_city.grid(row=4, column=1, columnspan=3)

lbl_region.grid(row=5, column=0, sticky='e')
ent_region.grid(row=5, column=1, columnspan=3)

lbl_index.grid(row=6, column=0, sticky='e')
ent_index.grid(row=6, column=1, columnspan=3)

lbl_country.grid(row=7, column=0, sticky='e')
ent_country.grid(row=7, column=1, columnspan=3)

btn_clear.pack(side=tkinter.RIGHT, padx=3, pady=3)
btn_send.pack(side=tkinter.RIGHT, padx=3, pady=3)



CalcWindow.mainloop()
