import tkinter.ttk
from tkinter import *


class ComparativeStatement:
    def __init__(self, base, current, pl_frame, bs_frame, data1, data2, data3, data4, data5, data6):
        self.base_year = base
        self.current_year = current
        self.comp_p_l_frame = pl_frame
        self.comp_bs_frame = bs_frame
        self.company_data1 = data1
        self.company_data2 = data2
        self.company_data3 = data3
        self.company_data4 = data4
        self.company_data5 = data5
        self.company_data6 = data6
        self.comp_pl_statement = None
        self.comp_bs_statement = None
        self.select_base_pl = None
        self.select_current_pl = None
        self.select_base_bs = None
        self.select_current_bs = None
        self.base_pl1 = None
        self.base_bs1 = None
        self.base_pl2 = None
        self.base_bs2 = None
        self.base_pl3 = None
        self.base_bs3 = None
        self.base_pl4 = None
        self.base_bs4 = None
        self.base_pl5 = None
        self.base_bs5 = None
        self.base_pl6 = None
        self.base_bs6 = None
        self.current_pl1 = None
        self.current_bs1 = None
        self.current_pl2 = None
        self.current_bs2 = None
        self.current_pl3 = None
        self.current_bs3 = None
        self.current_pl4 = None
        self.current_bs4 = None
        self.current_pl5 = None
        self.current_bs5 = None
        self.current_pl6 = None
        self.current_bs6 = None

    def create_statement(self):
        if self.base_year == self.company_data1[0].year:
            self.base_pl1 = self.company_data1[0]
            self.base_bs1 = self.company_data1[1]
        if self.base_year == self.company_data2[0].year:
            self.base_pl2 = self.company_data2[0]
            self.base_bs2 = self.company_data2[1]
        if self.base_year == self.company_data3[0].year:
            self.base_pl3 = self.company_data3[0]
            self.base_bs3 = self.company_data3[1]
        if self.base_year == self.company_data4[0].year:
            self.base_pl4 = self.company_data4[0]
            self.base_bs4 = self.company_data4[1]
        if self.base_year == self.company_data5[0].year:
            self.base_pl5 = self.company_data5[0]
            self.base_bs5 = self.company_data5[1]
        if self.base_year == self.company_data6[0].year:
            self.base_pl6 = self.company_data6[0]
            self.base_bs6 = self.company_data6[1]

        if self.current_year == self.company_data1[0].year:
            self.current_pl1 = self.company_data1[0]
            self.current_bs1 = self.company_data1[1]
        if self.current_year == self.company_data2[0].year:
            self.current_pl2 = self.company_data2[0]
            self.current_bs2 = self.company_data2[1]
        if self.current_year == self.company_data3[0].year:
            self.current_pl3 = self.company_data3[0]
            self.current_bs3 = self.company_data3[1]
        if self.current_year == self.company_data4[0].year:
            self.current_pl4 = self.company_data4[0]
            self.current_bs4 = self.company_data4[1]
        if self.current_year == self.company_data5[0].year:
            self.current_pl5 = self.company_data5[0]
            self.current_bs5 = self.company_data5[1]
        if self.current_year == self.company_data6[0].year:
            self.current_pl6 = self.company_data6[0]
            self.current_bs6 = self.company_data6[1]
        base_pl_list = [self.base_pl1, self.base_pl2, self.base_pl3, self.base_pl4, self.base_pl5, self.base_pl6]
        for item in base_pl_list:
            if item is not None:
                self.select_base_pl = item
        current_pl_list = [self.current_pl1, self.current_pl2, self.current_pl3, self.current_pl4, self.current_pl5,
                           self.current_pl6]
        for item in current_pl_list:
            if item is not None:
                self.select_current_pl = item
        base_bs_list = [self.base_bs1, self.base_bs2, self.base_bs3, self.base_pl4, self.base_bs5, self.base_bs6]
        for item in base_bs_list:
            if item is not None:
                self.select_base_bs = item
        current_bs_list = [self.current_bs1, self.current_bs2, self.current_bs3, self.current_pl4, self.current_bs5,
                           self.current_bs6]
        for item in current_bs_list:
            if item is not None:
                self.select_current_bs = item
        self.comp_pl_statement = self.select_current_pl - self.select_base_pl
        self.comp_bs_statement = self.select_current_bs - self.select_base_bs

        comp_pl_tree = tkinter.ttk.Treeview(self.comp_p_l_frame, columns=('1', '2', '3', '4', '5'))
        comp_pl_tree.configure(height=98)
        comp_pl_tree.column('#0', width=0)
        comp_pl_tree.column('1', anchor=W, width=200)
        comp_pl_tree.column('2', anchor=W, width=137)
        comp_pl_tree.column('3', anchor=W, width=137)
        comp_pl_tree.column('4', anchor=W, width=137)
        comp_pl_tree.column('5', anchor=W, width=137)
        comp_pl_tree.heading('#0', text='')
        comp_pl_tree.heading('1', text='Particulars')
        comp_pl_tree.heading('2', text='Base Year')
        comp_pl_tree.heading('3', text='Current Year')
        comp_pl_tree.heading('4', text='Absolute Change')
        comp_pl_tree.heading('5', text='Percentage Change')
        for j in range(15):
            comp_pl_tree.insert(parent='', index=END, values=self.comp_pl_statement[j])
        comp_pl_tree.place(x=0, y=20)
        comp_bs_tree = tkinter.ttk.Treeview(self.comp_bs_frame, columns=('1', '2', '3', '4', '5'))
        comp_bs_tree.configure(height=98)
        comp_bs_tree.column('#0', width=0)
        comp_bs_tree.column('1', anchor=W, width=200)
        comp_bs_tree.column('2', anchor=W, width=137)
        comp_bs_tree.column('3', anchor=W, width=137)
        comp_bs_tree.column('4', anchor=W, width=137)
        comp_bs_tree.column('5', anchor=W, width=137)
        comp_bs_tree.heading('#0', text='')
        comp_bs_tree.heading('1', text='Particulars')
        comp_bs_tree.heading('2', text='Base Year')
        comp_bs_tree.heading('3', text='Current Year')
        comp_bs_tree.heading('4', text='Absolute Change')
        comp_bs_tree.heading('5', text='Percentage Change')
        for j in range(13):
            comp_bs_tree.insert(parent='', index=END, values=self.comp_bs_statement[j])
        comp_bs_tree.place(x=0, y=20)
