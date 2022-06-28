import tkinter.ttk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from financial_statements import *


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


class RatioDisplay:
    def __init__(self, year, ratio, table_frame, graph_frame):
        self.year_list = year
        self.ratio_list = ratio
        self.ratio_table_frame = table_frame
        self.ratio_graph_frame = graph_frame
        self.count = len(self.ratio_list)

    def create_table(self):
        ratio_treeview = tkinter.ttk.Treeview(self.ratio_table_frame, columns=('1', '2'))
        ratio_treeview.configure(height=45)
        ratio_treeview.column('#0', width=0)
        ratio_treeview.column('1', anchor=W, width=588)
        ratio_treeview.column('2', anchor=W, width=588)
        ratio_treeview.heading('1', text='Year')
        ratio_treeview.heading('2', text='Ratio')
        for i in range(self.count):
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


class RatioAnalysis:
    def __init__(self, data1, data2, data3, data4, data5, data6, table_frame, graph_frame, liquidity_ratio,
                 solvency_ratio, profitability_ratio, turnover_ratio):
        self.company_data1 = data1
        self.company_data2 = data2
        self.company_data3 = data3
        self.company_data4 = data4
        self.company_data5 = data5
        self.company_data6 = data6
        self.ratios1 = None
        self.ratios2 = None
        self.ratios3 = None
        self.ratios4 = None
        self.ratios5 = None
        self.ratios6 = None
        self.ratios_list = []
        self.ratio_list = []
        self.year1 = None
        self.year2 = None
        self.year3 = None
        self.year4 = None
        self.year5 = None
        self.year6 = None
        self.year_list = []
        self.liquidity_ratio = liquidity_ratio
        self.solvency_ratio = solvency_ratio
        self.profitability_ratio = profitability_ratio
        self.turnover_ratio = turnover_ratio
        self.ratio_table_frame = table_frame
        self.ratio_graph_frame = graph_frame

    def create_ratio(self):
        if self.company_data1 is not None:
            self.ratios1 = Ratios(self.company_data1[0], self.company_data1[1])
        if self.company_data2 is not None:
            self.ratios2 = Ratios(self.company_data2[0], self.company_data2[1])
        if self.company_data3 is not None:
            self.ratios3 = Ratios(self.company_data3[0], self.company_data3[1])
        if self.company_data4 is not None:
            self.ratios4 = Ratios(self.company_data4[0], self.company_data4[1])
        if self.company_data5 is not None:
            self.ratios5 = Ratios(self.company_data5[0], self.company_data5[1])
        if self.company_data6 is not None:
            self.ratios6 = Ratios(self.company_data6[0], self.company_data6[1])

        self.ratios_list = [self.ratios1, self.ratios2, self.ratios3, self.ratios4, self.ratios5, self.ratios6]

        if self.liquidity_ratio.get() == 'Current Ratio':
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
            years_list = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6]
            for year in years_list:
                if year is not None:
                    self.year_list.append(year)
            for ratio in self.ratios_list:
                if ratio is not None:
                    self.ratio_list.append(ratio.current_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()
        if self.liquidity_ratio.get() == 'Quick Ratio':
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
            years_list = [self.year1, self.year2, self.year3, self.year4, self.year5, self.year6]
            for year in years_list:
                if year is not None:
                    self.year_list.append(year)
            for ratio in self.ratios_list:
                if ratio is not None:
                    self.ratio_list.append(ratio.absolute_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.liquidity_ratio.get() == 'Cash Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.absolute_ratio(), self.ratios2.absolute_ratio(), self.ratios3.absolute_ratio(),
                          self.ratios4.absolute_ratio(), self.ratios5.absolute_ratio(), self.ratios6.absolute_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.solvency_ratio.get() == 'Debt to Equity Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.debt_equity_ratio(), self.ratios2.debt_equity_ratio(),
                          self.ratios3.debt_equity_ratio(), self.ratios4.debt_equity_ratio(),
                          self.ratios5.debt_equity_ratio(), self.ratios6.debt_equity_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.solvency_ratio.get() == 'Debt to Capital Employed Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.debt_capital_ratio(), self.ratios2.debt_capital_ratio(),
                          self.ratios3.debt_capital_ratio(), self.ratios4.debt_capital_ratio(),
                          self.ratios5.debt_capital_ratio(), self.ratios6.debt_capital_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.solvency_ratio.get() == 'Proprietary Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.proprietary_ratio(), self.ratios2.proprietary_ratio(),
                          self.ratios3.proprietary_ratio(), self.ratios4.proprietary_ratio(),
                          self.ratios5.proprietary_ratio(), self.ratios6.proprietary_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.solvency_ratio.get() == 'Interest Coverage Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.icr(), self.ratios2.icr(), self.ratios3.icr(), self.ratios4.icr(),
                          self.ratios5.icr(), self.ratios6.icr()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Gross Profit Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.gp_ratio(), self.ratios2.gp_ratio(), self.ratios3.gp_ratio(),
                          self.ratios4.gp_ratio(), self.ratios5.gp_ratio(), self.ratios6.gp_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Proprietary Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.proprietary_ratio(), self.ratios2.proprietary_ratio(),
                          self.ratios3.proprietary_ratio(), self.ratios4.proprietary_ratio(),
                          self.ratios5.proprietary_ratio(), self.ratios6.proprietary_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Operating Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.operating_ratio(), self.ratios2.operating_ratio(),
                          self.ratios3.operating_ratio(), self.ratios4.operating_ratio(),
                          self.ratios5.operating_ratio(), self.ratios6.operating_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Operating Profit Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.operating_profit_ratio(), self.ratios2.operating_profit_ratio(),
                          self.ratios3.operating_profit_ratio(), self.ratios4.operating_profit_ratio(),
                          self.ratios5.operating_profit_ratio(), self.ratios6.operating_profit_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Net Profit Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.net_profit_ratio(), self.ratios2.net_profit_ratio(),
                          self.ratios3.net_profit_ratio(), self.ratios4.net_profit_ratio(),
                          self.ratios5.net_profit_ratio(), self.ratios6.net_profit_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Return on Investment Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.roi_ratio(), self.ratios2.roi_ratio(), self.ratios3.roi_ratio(),
                          self.ratios4.roi_ratio(), self.ratios5.roi_ratio(), self.ratios6.roi_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Return on Networth Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.ronw_ratio(), self.ratios2.ronw_ratio(), self.ratios3.ronw_ratio(),
                          self.ratios4.ronw_ratio(), self.ratios5.ronw_ratio(), self.ratios6.ronw_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()
        if self.profitability_ratio.get() == 'Earnings Per Share':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.eps_ratio(), self.ratios2.eps_ratio(), self.ratios3.eps_ratio(),
                          self.ratios4.eps_ratio(), self.ratios5.eps_ratio(), self.ratios6.eps_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Book Value Per Share':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.bps_ratio(), self.ratios2.bps_ratio(), self.ratios3.bps_ratio(),
                          self.ratios4.bps_ratio(), self.ratios5.bps_ratio(), self.ratios6.bps_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Dividend Payout Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.dp_ratio(), self.ratios2.dp_ratio(), self.ratios3.dp_ratio(),
                          self.ratios4.dp_ratio(), self.ratios5.ronw_ratio(), self.ratios6.ronw_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Price Earning Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.pe_ratio(), self.ratios2.pe_ratio(), self.ratios3.pe_ratio(),
                          self.ratios4.pe_ratio(), self.ratios5.pe_ratio(), self.ratios6.pe_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Inventory Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.inventory_turnover_ratio(), self.ratios2.inventory_turnover_ratio(),
                          self.ratios3.inventory_turnover_ratio(), self.ratios4.inventory_turnover_ratio(),
                          self.ratios5.inventory_turnover_ratio(), self.ratios6.inventory_turnover_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Debtors Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.tr_turnover_ratio(), self.ratios2.tr_turnover_ratio(),
                          self.ratios3.tr_turnover_ratio(), self.ratios4.tr_turnover_ratio(),
                          self.ratios5.tr_turnover_ratio(), self.ratios6.tr_turnover_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Creditors Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.tp_turnover_ratio(), self.ratios2.tp_turnover_ratio(),
                          self.ratios3.tp_turnover_ratio(), self.ratios4.tp_turnover_ratio(),
                          self.ratios5.tp_turnover_ratio(), self.ratios6.tp_turnover_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Capital Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.capital_turnover_ratio(), self.ratios2.capital_turnover_ratio(),
                          self.ratios3.capital_turnover_ratio(), self.ratios4.capital_turnover_ratio(),
                          self.ratios5.capital_turnover_ratio(), self.ratios6.capital_turnover_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Fixed Asset Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.fixed_asset_turnover_ratio(), self.ratios2.fixed_asset_turnover_ratio(),
                          self.ratios3.fixed_asset_turnover_ratio(), self.ratios4.fixed_asset_turnover_ratio(),
                          self.ratios5.fixed_asset_turnover_ratio(), self.ratios6.fixed_asset_turnover_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Working Capital Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [self.ratios1.working_capital_turnover_ratio(), self.ratios2.working_capital_turnover_ratio(),
                          self.ratios3.working_capital_turnover_ratio(), self.ratios4.working_capital_turnover_ratio(),
                          self.ratios5.working_capital_turnover_ratio(), self.ratios6.working_capital_turnover_ratio()]
            statement = RatioDisplay(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()
