import tkinter.ttk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class TrendDisplay:
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


class TrendAnalysis:
    def __init__(self, data1, data2, data3, data4, data5, data6, table_frame, graph_frame):
        self.company_data1 = data1
        self.company_data2 = data2
        self.company_data3 = data3
        self.company_data4 = data4
        self.company_data5 = data5
        self.company_data6 = data6
        self.trend_table_frame = table_frame
        self.trend_graph_frame = graph_frame
        self.x = []
        self.y = []
        self.trend_value1 = None
        self.trend_value2 = None
        self.trend_value3 = None
        self.trend_value4 = None
        self.trend_value5 = None
        self.trend_value6 = None
        self.year1 = None
        self.year2 = None
        self.year3 = None
        self.year4 = None
        self.year5 = None
        self.year6 = None

    def trend_rfo(self):
        if self.company_data1 is not None:
            self.trend_value1 = self.company_data1[0].rfo
        if self.company_data2 is not None:
            self.trend_value2 = self.company_data2[0].rfo
        if self.company_data3 is not None:
            self.trend_value3 = self.company_data3[0].rfo
        if self.company_data4 is not None:
            self.trend_value4 = self.company_data4[0].rfo
        if self.company_data5 is not None:
            self.trend_value5 = self.company_data5[0].rfo
        if self.company_data6 is not None:
            self.trend_value6 = self.company_data6[0].rfo
        trend_list = [self.trend_value1, self.trend_value2, self.trend_value3, self.trend_value4, self.trend_value5,
                      self.trend_value6]
        for trend in trend_list:
            if trend is not None:
                self.y.append(trend)
        if self.company_data1 is not None:
            self.year1 = self.company_data1[0].year
        if self.company_data2 is not None:
            self.year2 = self.company_data2[0].year
        if self.company_data3 is not None:
            self.year3 = self.company_data3[0].year
        if self.company_data4 is not None:
            self.year4 = self.company_data4[0].year
        if self.company_data5 is not None:
            self.year5 = self.company_data5[0].year
        if self.company_data6 is not None:
            self.year6 = self.company_data6[0].year
        year_list = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6]
        for year in year_list:
            if year is not None:
                self.x.append(year)
        trend_statement = TrendDisplay(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                       graph_frame=self.trend_graph_frame, title='Revenue From Operations')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_gp(self):
        if self.company_data1 is not None:
            self.trend_value1 = self.company_data1[0].gp
        if self.company_data2 is not None:
            self.trend_value2 = self.company_data2[0].gp
        if self.company_data3 is not None:
            self.trend_value3 = self.company_data3[0].gp
        if self.company_data4 is not None:
            self.trend_value4 = self.company_data4[0].gp
        if self.company_data5 is not None:
            self.trend_value5 = self.company_data5[0].gp
        if self.company_data6 is not None:
            self.trend_value6 = self.company_data6[0].gp
        trend_list = [self.trend_value1, self.trend_value2, self.trend_value3, self.trend_value4, self.trend_value5,
                      self.trend_value6]
        for trend in trend_list:
            if trend is not None:
                self.y.append(trend)
        if self.company_data1 is not None:
            self.year1 = self.company_data1[0].year
        if self.company_data2 is not None:
            self.year2 = self.company_data2[0].year
        if self.company_data3 is not None:
            self.year3 = self.company_data3[0].year
        if self.company_data4 is not None:
            self.year4 = self.company_data4[0].year
        if self.company_data5 is not None:
            self.year5 = self.company_data5[0].year
        if self.company_data6 is not None:
            self.year6 = self.company_data6[0].year
        year_list = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6]
        for year in year_list:
            if year is not None:
                self.x.append(year)
        trend_statement = TrendDisplay(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                       graph_frame=self.trend_graph_frame, title='Gross Profit')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_op(self):
        if self.company_data1 is not None:
            self.trend_value1 = self.company_data1[0].op
        if self.company_data2 is not None:
            self.trend_value2 = self.company_data2[0].op
        if self.company_data3 is not None:
            self.trend_value3 = self.company_data3[0].op
        if self.company_data4 is not None:
            self.trend_value4 = self.company_data4[0].op
        if self.company_data5 is not None:
            self.trend_value5 = self.company_data5[0].op
        if self.company_data6 is not None:
            self.trend_value6 = self.company_data6[0].op
        trend_list = [self.trend_value1, self.trend_value2, self.trend_value3, self.trend_value4, self.trend_value5,
                      self.trend_value6]
        for trend in trend_list:
            if trend is not None:
                self.y.append(trend)
        if self.company_data1 is not None:
            self.year1 = self.company_data1[0].year
        if self.company_data2 is not None:
            self.year2 = self.company_data2[0].year
        if self.company_data3 is not None:
            self.year3 = self.company_data3[0].year
        if self.company_data4 is not None:
            self.year4 = self.company_data4[0].year
        if self.company_data5 is not None:
            self.year5 = self.company_data5[0].year
        if self.company_data6 is not None:
            self.year6 = self.company_data6[0].year
        year_list = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6]
        for year in year_list:
            if year is not None:
                self.x.append(year)
        trend_statement = TrendDisplay(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                       graph_frame=self.trend_graph_frame, title='Operating Profit')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_np(self):
        if self.company_data1 is not None:
            self.trend_value1 = self.company_data1[0].pat
        if self.company_data2 is not None:
            self.trend_value2 = self.company_data2[0].pat
        if self.company_data3 is not None:
            self.trend_value3 = self.company_data3[0].pat
        if self.company_data4 is not None:
            self.trend_value4 = self.company_data4[0].pat
        if self.company_data5 is not None:
            self.trend_value5 = self.company_data5[0].pat
        if self.company_data6 is not None:
            self.trend_value6 = self.company_data6[0].pat
        trend_list = [self.trend_value1, self.trend_value2, self.trend_value3, self.trend_value4, self.trend_value5,
                      self.trend_value6]
        for trend in trend_list:
            if trend is not None:
                self.y.append(trend)
        if self.company_data1 is not None:
            self.year1 = self.company_data1[0].year
        if self.company_data2 is not None:
            self.year2 = self.company_data2[0].year
        if self.company_data3 is not None:
            self.year3 = self.company_data3[0].year
        if self.company_data4 is not None:
            self.year4 = self.company_data4[0].year
        if self.company_data5 is not None:
            self.year5 = self.company_data5[0].year
        if self.company_data6 is not None:
            self.year6 = self.company_data6[0].year
        year_list = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6]
        for year in year_list:
            if year is not None:
                self.x.append(year)
        trend_statement = TrendDisplay(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                       graph_frame=self.trend_graph_frame, title='Net Profit')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_debt(self):
        if self.company_data1 is not None:
            self.trend_value1 = self.company_data1[1].ltb
        if self.company_data2 is not None:
            self.trend_value2 = self.company_data2[1].ltb
        if self.company_data3 is not None:
            self.trend_value3 = self.company_data3[1].ltb
        if self.company_data4 is not None:
            self.trend_value4 = self.company_data4[1].ltb
        if self.company_data5 is not None:
            self.trend_value5 = self.company_data5[1].ltb
        if self.company_data6 is not None:
            self.trend_value6 = self.company_data6[1].ltb
        trend_list = [self.trend_value1, self.trend_value2, self.trend_value3, self.trend_value4, self.trend_value5,
                      self.trend_value6]
        for trend in trend_list:
            if trend is not None:
                self.y.append(trend)
        if self.company_data1 is not None:
            self.year1 = self.company_data1[0].year
        if self.company_data2 is not None:
            self.year2 = self.company_data2[0].year
        if self.company_data3 is not None:
            self.year3 = self.company_data3[0].year
        if self.company_data4 is not None:
            self.year4 = self.company_data4[0].year
        if self.company_data5 is not None:
            self.year5 = self.company_data5[0].year
        if self.company_data6 is not None:
            self.year6 = self.company_data6[0].year
        year_list = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6]
        for year in year_list:
            if year is not None:
                self.x.append(year)
        trend_statement = TrendDisplay(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                       graph_frame=self.trend_graph_frame, title='Debt')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_ox(self):
        if self.company_data1 is not None:
            self.trend_value1 = self.company_data1[0].oe
        if self.company_data2 is not None:
            self.trend_value2 = self.company_data2[0].oe
        if self.company_data3 is not None:
            self.trend_value3 = self.company_data3[0].oe
        if self.company_data4 is not None:
            self.trend_value4 = self.company_data4[0].oe
        if self.company_data5 is not None:
            self.trend_value5 = self.company_data5[0].oe
        if self.company_data6 is not None:
            self.trend_value6 = self.company_data6[0].oe
        trend_list = [self.trend_value1, self.trend_value2, self.trend_value3, self.trend_value4, self.trend_value5,
                      self.trend_value6]
        for trend in trend_list:
            if trend is not None:
                self.y.append(trend)
        if self.company_data1 is not None:
            self.year1 = self.company_data1[0].year
        if self.company_data2 is not None:
            self.year2 = self.company_data2[0].year
        if self.company_data3 is not None:
            self.year3 = self.company_data3[0].year
        if self.company_data4 is not None:
            self.year4 = self.company_data4[0].year
        if self.company_data5 is not None:
            self.year5 = self.company_data5[0].year
        if self.company_data6 is not None:
            self.year6 = self.company_data6[0].year
        year_list = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6]
        for year in year_list:
            if year is not None:
                self.x.append(year)
        trend_statement = TrendDisplay(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                       graph_frame=self.trend_graph_frame, title='Operating Expenses')
        trend_statement.create_table()
        trend_statement.create_graph()
