import tkinter


# add spaces?
def num_btn(output: tkinter.Label, num: str) -> None:
    output_len = len(output['text'])
    if int(output['text']) == 0:
        output['text'] = num
    elif output_len < 16:
        output['text'] += num
    else:
        return

