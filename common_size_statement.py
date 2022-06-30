import tkinter.ttk
from tkinter import *


class CommonSizeStatement:
    def __init__(self, pl, bs, pl_frame, bs_frame):
        self.com_pl = pl
        self.com_bs = bs
        self.common_p_l_frame = pl_frame
        self.common_bs_frame = bs_frame

    def create_statement(self):
        com_pl_treeview = tkinter.ttk.Treeview(self.common_p_l_frame, columns=('1', '2', '3'))
        com_pl_treeview.configure(height=95)
        com_pl_treeview.column('#0', width=0)
        com_pl_treeview.column('1', anchor=W, width=400)
        com_pl_treeview.column('2', anchor=W, width=175)
        com_pl_treeview.column('3', anchor=W, width=175)
        com_pl_treeview.heading('1', text='Particulars')
        com_pl_treeview.heading('2', text='Amount')
        com_pl_treeview.heading('3', text='Percentage')
        for j in range(15):
            com_pl_treeview.insert(parent='', index=END, values=self.com_pl[j])
        com_pl_treeview.place(x=0, y=20)

        com_bs_treeview = tkinter.ttk.Treeview(self.common_bs_frame, columns=('1', '2', '3'))
        com_bs_treeview.configure(height=95)
        com_bs_treeview.column('#0', width=0)
        com_bs_treeview.column('1', anchor=W, width=400)
        com_bs_treeview.column('2', anchor=W, width=175)
        com_bs_treeview.column('3', anchor=W, width=175)
        com_bs_treeview.heading('1', text='Particulars')
        com_bs_treeview.heading('2', text='Amount')
        com_bs_treeview.heading('3', text='Percentage')
        for j in range(13):
            com_bs_treeview.insert(parent='', index=END, values=self.com_bs[j])
        com_bs_treeview.place(x=0, y=20)
