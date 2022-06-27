import tkinter.ttk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


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
        if self.company_data1 is not None:
            if self.base_year == self.company_data1[0].year:
                self.base_pl1 = self.company_data1[0]
                self.base_bs1 = self.company_data1[1]
        if self.company_data2 is not None:
            if self.base_year == self.company_data2[0].year:
                self.base_pl2 = self.company_data2[0]
                self.base_bs2 = self.company_data2[1]
        if self.company_data3 is not None:
            if self.base_year == self.company_data3[0].year:
                self.base_pl3 = self.company_data3[0]
                self.base_bs3 = self.company_data3[1]
        if self.company_data4 is not None:
            if self.base_year == self.company_data4[0].year:
                self.base_pl4 = self.company_data4[0]
                self.base_bs4 = self.company_data4[1]
        if self.company_data5 is not None:
            if self.base_year == self.company_data5[0].year:
                self.base_pl5 = self.company_data5[0]
                self.base_bs5 = self.company_data5[1]
        if self.company_data6 is not None:
            if self.base_year == self.company_data6[0].year:
                self.base_pl6 = self.company_data6[0]
                self.base_bs6 = self.company_data6[1]

        if self.company_data1 is not None:
            if self.current_year == self.company_data1[0].year:
                self.current_pl1 = self.company_data1[0]
                self.current_bs1 = self.company_data1[1]
        if self.company_data2 is not None:
            if self.current_year == self.company_data2[0].year:
                self.current_pl2 = self.company_data2[0]
                self.current_bs2 = self.company_data2[1]
        if self.company_data3 is not None:
            if self.current_year == self.company_data3[0].year:
                self.current_pl3 = self.company_data3[0]
                self.current_bs3 = self.company_data3[1]
        if self.company_data4 is not None:
            if self.current_year == self.company_data4[0].year:
                self.current_pl4 = self.company_data4[0]
                self.current_bs4 = self.company_data4[1]
        if self.company_data5 is not None:
            if self.current_year == self.company_data5[0].year:
                self.current_pl5 = self.company_data5[0]
                self.current_bs5 = self.company_data5[1]
        if self.company_data6 is not None:
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


class TrendAnalysis:
    def __init__(self, trend, year, table_frame, graph_frame, title):
        self.y = trend
        self.x = year
        self.trend_table_frame = table_frame
        self.trend_graph_frame = graph_frame
        self.title = title
        self.count = len(self.x)

    def create_table(self):
        trend_treeview = tkinter.ttk.Treeview(self.trend_table_frame, columns=('1', '2'))
        trend_treeview.configure(height=45)
        trend_treeview.column('#0', width=0)
        trend_treeview.column('1', anchor=W, width=588)
        trend_treeview.column('2', anchor=W, width=588)
        trend_treeview.heading('1', text='Year')
        trend_treeview.heading('2', text='Amount')
        for j in range(self.count):
            trend_treeview.insert(parent='', index=END, values=(self.x[j], self.y[j]))
        trend_treeview.place(x=0, y=0)

    def create_graph(self):
        fig = plt.Figure(figsize=(24, 7), dpi=50)
        ax = fig.add_subplot(111)
        ax.set_title(self.title)
        ax.bar(self.x, self.y, 0.25)
        chart = FigureCanvasTkAgg(fig, self.trend_graph_frame)
        chart.get_tk_widget().place(x=0, y=0)
        tool_bar = NavigationToolbar2Tk(chart, self.trend_graph_frame)
        tool_bar.place(x=0, y=0)


class RatioAnalysis:
    def __init__(self, year, ratio, table_frame, graph_frame):
        self.year_list = year
        self.ratio_list = ratio
        self.ratio_table_frame = table_frame
        self.ratio_graph_frame = graph_frame

    def create_table(self):
        ratio_treeview = tkinter.ttk.Treeview(self.ratio_table_frame, columns=('1', '2'))
        ratio_treeview.configure(height=45)
        ratio_treeview.column('#0', width=0)
        ratio_treeview.column('1', anchor=W, width=588)
        ratio_treeview.column('2', anchor=W, width=588)
        ratio_treeview.heading('1', text='Year')
        ratio_treeview.heading('2', text='Ratio')
        for i in range(6):
            ratio_treeview.insert(parent='', index=END, values=(self.year_list[i], self.ratio_list[i]))
        ratio_treeview.place(x=0, y=0)

    def create_graph(self):
        fig = plt.Figure(figsize=(24, 7), dpi=50)
        ax = fig.add_subplot(111)
        ax.set_title('Ratio')
        ax.bar(self.year_list, self.ratio_list, 0.25)
        chart = FigureCanvasTkAgg(fig, self.ratio_graph_frame)
        chart.get_tk_widget().place(x=0, y=0)
        toolbar = NavigationToolbar2Tk(chart, self.ratio_graph_frame)
        toolbar.place(x=0, y=0)
