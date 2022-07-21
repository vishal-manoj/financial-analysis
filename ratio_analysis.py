import tkinter.ttk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from financial_statements import *


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
    def __init__(self, data1, data2, data3, data4, data5, data6, table_frame, graph_frame, selected_ratio):
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
        self.selected_ratio = selected_ratio
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

        if self.selected_ratio[0] == 0:
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
        if self.selected_ratio[0] == 1:
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
                    self.ratio_list.append(ratio.quick_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 2:
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

        if self.selected_ratio[0] == 3:
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
                    self.ratio_list.append(ratio.debt_equity_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 4:
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
                    self.ratio_list.append(ratio.debt_capital_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 5:
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
                    self.ratio_list.append(ratio.proprietary_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 6:
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
                    self.ratio_list.append(ratio.icr())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 7:
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
                    self.ratio_list.append(ratio.gp_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 8:
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
                    self.ratio_list.append(ratio.operating_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 9:
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
                    self.ratio_list.append(ratio.operating_profit_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 10:
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
                    self.ratio_list.append(ratio.net_profit_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 11:
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
                    self.ratio_list.append(ratio.roi_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 12:
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
                    self.ratio_list.append(ratio.ronw_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 13:
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
                    self.ratio_list.append(ratio.eps_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 14:
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
                    self.ratio_list.append(ratio.bps_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 15:
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
                    self.ratio_list.append(ratio.dp_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 16:
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
                    self.ratio_list.append(ratio.pe_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 17:
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
                    self.ratio_list.append(ratio.inventory_turnover_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 18:
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
                    self.ratio_list.append(ratio.tr_turnover_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 19:
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
                    self.ratio_list.append(ratio.tp_turnover_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 20:
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
                    self.ratio_list.append(ratio.capital_turnover_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 21:
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
                    self.ratio_list.append(ratio.fixed_asset_turnover_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.selected_ratio[0] == 22:
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
                    self.ratio_list.append(ratio.working_capital_turnover_ratio())

            statement = RatioDisplay(year=self.year_list, ratio=self.ratio_list, table_frame=self.ratio_table_frame,
                                     graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

