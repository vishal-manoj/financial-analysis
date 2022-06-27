import tkinter.ttk
from financial_statements import *
from analysis import *

# A GUI based financial analysis software


class FinancialAnalysis:
    def __init__(self, root):
        self.x = None
        self.y = None
        self.com_pl = None
        self.com_bs = None
        self.base_year = None
        self.current_year = None
        self.p_l1 = None
        self.b_s1 = None
        self.company_data1 = None
        self.p_l2 = None
        self.b_s2 = None
        self.company_data2 = None
        self.p_l3 = None
        self.b_s3 = None
        self.company_data3 = None
        self.p_l4 = None
        self.b_s4 = None
        self.company_data4 = None
        self.p_l5 = None
        self.b_s5 = None
        self.company_data5 = None
        self.p_l6 = None
        self.b_s6 = None
        self.company_data6 = None
        self.count = 1
        self.clear_list = None
        self.item = None
        self.delete_list = None
        self.no_of_years = None
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
        self.root = root
        self.root.state('zoomed')
        self.root.title('Financial Analysis Software')
        name_label = Label(self.root, text='Financial Analysis', bg='orange', relief=GROOVE, font=10, height=3,
                           width=140)
        name_label.grid(row=0, column=0)

        # Main window and Tabs
        style = tkinter.ttk.Style()
        current_theme = style.theme_use()
        style.theme_settings(current_theme, {'TNotebook.Tab': {'configure': {'padding': [40, 5]}}})
        style.configure('TNotebook.Tab', background='orange')
        style.map('TNotebook', background=[('selected', 'orange')])
        tabs = tkinter.ttk.Notebook()
        tabs.grid(row=1, column=0)
        data_frame = Frame(tabs, highlightbackground='orange', highlightthickness=3, height=680, width=1515)
        comparative_frame = Frame(tabs, highlightbackground='orange', highlightthickness=3, height=680, width=1515)
        common_frame = Frame(tabs, highlightbackground='orange', highlightthickness=3, height=680, width=1515)
        ratio_frame = Frame(tabs, highlightbackground='orange', highlightthickness=3, height=680, width=1515)
        trend_frame = Frame(tabs, highlightbackground='orange', highlightthickness=3, height=680, width=1515)
        tabs.add(data_frame, text='Data')
        tabs.add(comparative_frame, text='Comparative Statement')
        tabs.add(common_frame, text='Common size Statement')
        tabs.add(ratio_frame, text='Ratios')
        tabs.add(trend_frame, text='Trend Analysis')
        company_frame = Frame(data_frame, highlightbackground='orange', highlightthickness=2, height=50, width=1510)
        company_frame.place(x=0, y=0)
        company_label = Label(company_frame, text='Enter Company name :')
        company_label.place(x=10, y=10)
        self.company_entry = Entry(company_frame, width=50, state=DISABLED)
        self.company_entry.place(x=150, y=12)
        year_label = Label(company_frame, text='Year :')
        year_label.place(x=1095, y=10)
        self.year_entry = Entry(company_frame, width=50, state=DISABLED)
        self.year_entry.place(x=1145, y=10)
        # Treeview row height settings
        s = tkinter.ttk.Style()
        s.configure('Treeview', rowheight=30)

        # Profit and loss statement data
        self.p_l_frame = Frame(data_frame, highlightbackground='orange', highlightthickness=2, height=550, width=760)
        self.p_l_frame.place(x=0, y=50)
        p_l_label = Label(self.p_l_frame, text='Statement of Profit and Loss Data', bg='orange', width=108)
        p_l_label.place(x=0, y=0)
        rfo_label = Label(self.p_l_frame, text='Revenue from Operations :')
        rfo_label.place(x=5, y=30)
        self.rfo_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.rfo_entry.place(x=320, y=30)
        oi_label = Label(self.p_l_frame, text='Other Income :')
        oi_label.place(x=5, y=60)
        self.oi_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.oi_entry.place(x=320, y=60)
        com_label = Label(self.p_l_frame, text='Cost of Materials :')
        com_label.place(x=5, y=90)
        self.com_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.com_entry.place(x=320, y=90)
        purchase_label = Label(self.p_l_frame, text='Purchases :')
        purchase_label.place(x=5, y=120)
        self.purchase_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.purchase_entry.place(x=320, y=120)
        cii_label = Label(self.p_l_frame, text='Change in Inventory :')
        cii_label.place(x=5, y=150)
        self.cii_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.cii_entry.place(x=320, y=150)
        ebe_label = Label(self.p_l_frame, text='Employee Benefit Expenses :')
        ebe_label.place(x=5, y=180)
        self.ebe_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.ebe_entry.place(x=320, y=180)
        fc_label = Label(self.p_l_frame, text='Finance Cost :')
        fc_label.place(x=5, y=210)
        self.fc_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.fc_entry.place(x=320, y=210)
        dna_label = Label(self.p_l_frame, text='Depreciation and Amortization :')
        dna_label.place(x=5, y=240)
        self.dna_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.dna_entry.place(x=320, y=240)
        ode_label = Label(self.p_l_frame, text='Other Direct expenses :')
        ode_label.place(x=5, y=270)
        self.ode_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.ode_entry.place(x=320, y=270)
        oie_label = Label(self.p_l_frame, text='Other Indirect Expenses :')
        oie_label.place(x=5, y=300)
        self.oie_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.oie_entry.place(x=320, y=300)
        tax_label = Label(self.p_l_frame, text='Tax :')
        tax_label.place(x=5, y=330)
        self.tax_entry = Entry(self.p_l_frame, width=40, state=DISABLED)
        self.tax_entry.place(x=320, y=330)

        # Balance sheet data
        self.b_s_frame = Frame(data_frame, highlightbackground='orange', highlightthickness=2, height=550, width=750)
        self.b_s_frame.place(x=760, y=50)
        b_s_label = Label(self.b_s_frame, text='Balance Sheet Data', bg='orange', width=108)
        b_s_label.place(x=0, y=0)
        share_fund_label = Label(self.b_s_frame, text='Shareholders Fund :')
        share_fund_label.place(x=0, y=30)
        self.share_fund_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.share_fund_entry.place(x=320, y=30)
        ps_label = Label(self.b_s_frame, text='Preference Share :')
        ps_label.place(x=0, y=60)
        self.ps_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.ps_entry.place(x=320, y=60)
        ltb_label = Label(self.b_s_frame, text='Long Term Borrowings :')
        ltb_label.place(x=0, y=90)
        self.ltb_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.ltb_entry.place(x=320, y=90)
        oll_label = Label(self.b_s_frame, text='Other Long Term Liabilities :')
        oll_label.place(x=0, y=120)
        self.oll_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.oll_entry.place(x=320, y=120)
        tp_label = Label(self.b_s_frame, text='Trade Payable :')
        tp_label.place(x=0, y=150)
        self.tp_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.tp_entry.place(x=320, y=150)
        ocl_label = Label(self.b_s_frame, text='Other Current Liabilities :')
        ocl_label.place(x=0, y=180)
        self.ocl_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.ocl_entry.place(x=320, y=180)
        fa_label = Label(self.b_s_frame, text='Fixed Assets :')
        fa_label.place(x=0, y=210)
        self.fa_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.fa_entry.place(x=320, y=210)
        lti_label = Label(self.b_s_frame, text='Long Term Investments :')
        lti_label.place(x=0, y=240)
        self.lti_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.lti_entry.place(x=320, y=240)
        ltl_label = Label(self.b_s_frame, text='Long Term Loans (Asset) :')
        ltl_label.place(x=0, y=270)
        self.ltl_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.ltl_entry.place(x=320, y=270)
        ola_label = Label(self.b_s_frame, text='Other Long Term Assets :')
        ola_label.place(x=0, y=300)
        self.ola_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.ola_entry.place(x=320, y=300)
        inv_label = Label(self.b_s_frame, text='Inventory :')
        inv_label.place(x=0, y=330)
        self.inv_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.inv_entry.place(x=320, y=330)
        tr_label = Label(self.b_s_frame, text='Trade Receivables :')
        tr_label.place(x=0, y=360)
        self.tr_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.tr_entry.place(x=320, y=360)
        cac_label = Label(self.b_s_frame, text='Cash and Cash Equivalents :')
        cac_label.place(x=0, y=390)
        self.cac_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.cac_entry.place(x=320, y=390)
        oca_label = Label(self.b_s_frame, text='Other Current Assets :')
        oca_label.place(x=0, y=420)
        self.oca_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.oca_entry.place(x=320, y=420)
        nes_label = Label(self.b_s_frame, text='Number of equity shares :')
        nes_label.place(x=0, y=450)
        self.nes_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.nes_entry.place(x=320, y=450)
        mps_label = Label(self.b_s_frame, text='Market Price per Share :')
        mps_label.place(x=0, y=480)
        self.mps_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.mps_entry.place(x=320, y=480)
        dps_label = Label(self.b_s_frame, text='Dividend per Share :')
        dps_label.place(x=0, y=510)
        self.dps_entry = Entry(self.b_s_frame, width=40, state=DISABLED)
        self.dps_entry.place(x=320, y=510)

        # Data button frame and buttons
        data_button_frame = Frame(data_frame, highlightbackground='orange', highlightthickness=3, height=75, width=760)
        data_button_frame.place(x=0, y=600)
        year_count_frame = Frame(data_frame, highlightbackground='orange', highlightthickness=3, height=75, width=750)
        year_count_frame.place(x=760, y=600)
        self.upload_button = Button(data_button_frame, text='Upload Data', height=2, width=30, state=DISABLED,
                                    command=self.upload_data)
        self.upload_button.place(x=10, y=15)
        self.clear_button = Button(data_button_frame, text='Clear Data', height=2, width=30, state=DISABLED,
                                   command=self.clear_data)
        self.clear_button.place(x=450, y=15)
        year_count_label = Label(year_count_frame, text='Number of Years: ')
        year_count_label.place(x=0, y=20)
        self.year_count = StringVar()
        self.year_count_spin_box = Spinbox(year_count_frame, from_=2, to=6, textvariable=self.year_count, wrap=True)
        self.year_count_spin_box.place(x=110, y=22)
        self.submit_spin_button = Button(year_count_frame, text='Submit', height=2, width=30, command=self.count_year)
        self.submit_spin_button.place(x=500, y=15)

        # Comparative statement, frames and radio buttons
        comparative_label = Label(comparative_frame, text='Comparative Statement', bg='orange', height=1, width=220)
        comparative_label.place(x=0, y=0)
        self.comp_p_l_frame = Frame(comparative_frame, highlightbackground='orange', highlightthickness=3, height=600,
                                    width=755)
        self.comp_p_l_frame.place(x=0, y=75)
        comp_p_l_label = Label(self.comp_p_l_frame, text='Comparative Profit and Loss Statement', bg='orange', height=1,
                               width=110)
        comp_p_l_label.place(x=0, y=1)
        self.comp_bs_frame = Frame(comparative_frame, highlightbackground='orange', highlightthickness=3, height=600,
                                   width=755)
        self.comp_bs_frame.place(x=755, y=75)
        comp_bs_label = Label(self.comp_bs_frame, text='Comparative BalanceSheet', bg='orange', height=1, width=110)
        comp_bs_label.place(x=0, y=1)
        base_year_label = Label(comparative_frame, text='Base Year :')
        base_year_label.place(x=0, y=35)
        self.base_year_entry = Entry(comparative_frame, width=30)
        self.base_year_entry.place(x=80, y=35)
        current_year_label = Label(comparative_frame, text='Current Year :')
        current_year_label.place(x=300, y=35)
        self.current_year_entry = Entry(comparative_frame, width=30)
        self.current_year_entry.place(x=400, y=35)
        self.comp_submit_b = Button(comparative_frame, text='Submit', width=30, height=2, command=self.comp_statement)
        self.comp_submit_b.place(x=1250, y=26)

        # Common size statement, frames and radio buttons
        common_label = Label(common_frame, text='Common Size Statement', bg='orange', height=1, width=220)
        common_label.place(x=0, y=0)
        self.common_p_l_frame = Frame(common_frame, highlightbackground='orange', highlightthickness=3, height=600,
                                      width=755)
        self.common_p_l_frame.place(x=0, y=75)
        common_p_l_label = Label(self.common_p_l_frame, text='Common Size Profit and Loss Statement', bg='orange',
                                 height=1, width=110)
        common_p_l_label.place(x=0, y=1)
        self.common_bs_frame = Frame(common_frame, highlightbackground='orange', highlightthickness=3, height=600,
                                     width=755)
        self.common_bs_frame.place(x=755, y=75)
        common_bs_label = Label(self.common_bs_frame, text='Common Size BalanceSheet Statement', bg='orange', height=1,
                                width=110)
        common_bs_label.place(x=0, y=1)
        self.com_submit_b = Button(common_frame, text='Submit', width=30, height=2, command=self.com_size_statement)
        self.com_submit_b.place(x=1250, y=26)
        com_year_label = Label(common_frame, text='Enter Year: ')
        com_year_label.place(x=0, y=35)
        self.com_year_entry = Entry(common_frame, width=40)
        self.com_year_entry.place(x=100, y=35)

        # Ratio frames and components
        self.ratio_option_frame = Frame(ratio_frame, bg='orange', highlightbackground='orange', highlightthickness=3,
                                        width=325, height=675)
        self.ratio_option_frame.place(x=0, y=0)
        self.liquidity_ratio = StringVar()
        self.liquidity_ratio.set('Liquidity Ratios')
        liquidity_list = ['Current Ratio', 'Quick Ratio', 'Cash Ratio']
        liquidity_menu = OptionMenu(self.ratio_option_frame, self.liquidity_ratio, *liquidity_list)
        liquidity_menu.configure(width=46, height=3)
        liquidity_menu.place(x=0, y=0)

        self.solvency_ratio = StringVar()
        self.solvency_ratio.set('Solvency Ratios')
        solvency_list = ['Debt to Equity Ratio', 'Debt to Capital Employed Ratio', 'Proprietary Ratio',
                         'Interest Coverage Ratio']
        solvency_menu = OptionMenu(self.ratio_option_frame, self.solvency_ratio, *solvency_list)
        solvency_menu.configure(width=46, height=3)
        solvency_menu.place(x=0, y=98)

        self.profitability_ratio = StringVar()
        self.profitability_ratio.set('Profitability Ratios')
        profitability_list = ['Gross Profit Ratio', 'Operating Ratio', 'Operating Profit Ratio', 'Net Profit Ratio',
                              'Return on Investment Ratio', 'Return on Networth Ratio', 'Earnings Per Share',
                              'Book Value Per Share', 'Dividend Payout Ratio', 'Price Earning Ratio']
        profitability_menu = OptionMenu(self.ratio_option_frame, self.profitability_ratio, *profitability_list)
        profitability_menu.configure(width=46, height=3)
        profitability_menu.place(x=0, y=196)

        self.turnover_ratio = StringVar()
        self.turnover_ratio.set('Turnover Ratios')
        turnover_list = ['Inventory Turnover Ratio', 'Debtors Turnover Ratio', 'Creditors Turnover Ratio',
                         'Capital Turnover Ratio', 'Fixed Asset Turnover Ratio', 'Working Capital Turnover Ratio']
        turnover_menu = OptionMenu(self.ratio_option_frame, self.turnover_ratio, *turnover_list)
        turnover_menu.configure(width=46, height=3)
        turnover_menu.place(x=0, y=294)
        self.ratio_button = Button(self.ratio_option_frame, text='Submit', width=44, height=3, command=self.ratio)
        self.ratio_button.place(x=0, y=490)

        self.ratio_table_frame = Frame(ratio_frame, highlightbackground='orange', highlightthickness=3, width=1185,
                                       height=320)
        self.ratio_table_frame.place(x=325, y=0)
        self.ratio_graph_frame = Frame(ratio_frame, highlightbackground='orange', highlightthickness=3, width=1185,
                                       height=350)
        self.ratio_graph_frame.place(x=325, y=325)

        # Trend frame and components
        trend_button_frame = Frame(trend_frame, bg='orange', highlightbackground='orange', highlightthickness=3,
                                   width=325, height=675)
        trend_button_frame.place(x=0, y=0)
        self.rfo_trend_button = Button(trend_button_frame, text='Revenue From Operations', width=44, height=3,
                                       command=self.trend_rfo)
        self.rfo_trend_button.place(x=0, y=0)
        self.gp_trend_button = Button(trend_button_frame, text='Gross Profit', width=44, height=3,
                                      command=self.trend_gp)
        self.gp_trend_button.place(x=0, y=98)
        self.op_trend_button = Button(trend_button_frame, text='Operating Profit', width=44, height=3,
                                      command=self.trend_op)
        self.op_trend_button.place(x=0, y=196)
        self.np_trend_button = Button(trend_button_frame, text='Net Profit', width=44, height=3, command=self.trend_np)
        self.np_trend_button.place(x=0, y=294)
        self.debt_trend_button = Button(trend_button_frame, text='Debt', width=44, height=3, command=self.trend_debt)
        self.debt_trend_button.place(x=0, y=392)
        self.ox_button = Button(trend_button_frame, text='Operating Expenses', width=44, height=3,
                                command=self.trend_ox)
        self.ox_button.place(x=0, y=490)
        self.trend_table_frame = Frame(trend_frame, highlightbackground='orange', highlightthickness=3, width=1185,
                                       height=320)
        self.trend_table_frame.place(x=325, y=0)
        self.trend_graph_frame = Frame(trend_frame, highlightbackground='orange', highlightthickness=3, width=1185,
                                       height=350)
        self.trend_graph_frame.place(x=325, y=325)

    def count_year(self):
        self.no_of_years = int(self.year_count_spin_box.get())
        entry_list = [self.company_entry, self.year_entry, self.rfo_entry, self.oi_entry, self.com_entry,
                      self.purchase_entry, self.cii_entry, self.ebe_entry, self.fc_entry, self.dna_entry,
                      self.ode_entry, self.oie_entry, self.tax_entry, self.share_fund_entry, self.ps_entry,
                      self.ltb_entry, self.oll_entry, self.tp_entry, self.ocl_entry, self.fa_entry,
                      self.lti_entry, self.ltl_entry, self.ola_entry, self.inv_entry, self.tr_entry,
                      self.cac_entry, self.oca_entry, self.nes_entry, self.dps_entry, self.mps_entry,
                      self.upload_button, self.clear_button]
        for entry in entry_list:
            entry['state'] = NORMAL

    def upload_data(self):
        self.delete_list = [self.company_entry, self.year_entry, self.rfo_entry, self.oi_entry, self.com_entry,
                            self.purchase_entry, self.cii_entry, self.ebe_entry, self.fc_entry, self.dna_entry,
                            self.ode_entry, self.oie_entry, self.tax_entry, self.share_fund_entry, self.ps_entry,
                            self.ltb_entry, self.oll_entry, self.tp_entry, self.ocl_entry, self.fa_entry,
                            self.lti_entry, self.ltl_entry, self.ola_entry, self.inv_entry, self.tr_entry,
                            self.cac_entry, self.oca_entry, self.nes_entry, self.dps_entry, self.mps_entry]
        if self.count == 1 and self.count <= self.no_of_years:
            self.p_l1 = Pl(name=self.company_entry.get(), year=self.year_entry.get(),
                           rfo=int(self.rfo_entry.get()), oi=int(self.oi_entry.get()), com=int(self.com_entry.get()),
                           purchases=int(self.purchase_entry.get()), cii=int(self.cii_entry.get()),
                           ebe=int(self.ebe_entry.get()), fc=int(self.fc_entry.get()), dna=int((self.dna_entry.get())),
                           ode=int(self.ode_entry.get()), oie=int(self.oie_entry.get()),
                           tax=int((self.tax_entry.get())))

            self.b_s1 = Bs(name=self.company_entry.get(), year=self.year_entry.get(),
                           sf=int(self.share_fund_entry.get()), ps=int(self.ps_entry.get()),
                           ltb=int(self.ltb_entry.get()), oll=int(self.oll_entry.get()), tp=int(self.tp_entry.get()),
                           ocl=int(self.ocl_entry.get()), fa=int(self.fa_entry.get()), lti=int(self.lti_entry.get()),
                           ltl=int(self.ltl_entry.get()), ola=int(self.ola_entry.get()), inv=int(self.inv_entry.get()),
                           tr=int(self.tr_entry.get()), cac=int(self.cac_entry.get()), oca=int(self.oca_entry.get()),
                           share_no=int(self.nes_entry.get()), dps=int(self.dps_entry.get()),
                           mps=int(self.mps_entry.get()))

            self.company_data1 = (self.p_l1, self.b_s1)

            for self.item in self.delete_list:
                self.item.delete(0, END)

        if self.count == 2 and self.count <= self.no_of_years:
            self.p_l2 = Pl(name=self.company_entry.get(), year=self.year_entry.get(),
                           rfo=int(self.rfo_entry.get()), oi=int(self.oi_entry.get()), com=int(self.com_entry.get()),
                           purchases=int(self.purchase_entry.get()), cii=int(self.cii_entry.get()),
                           ebe=int(self.ebe_entry.get()), fc=int(self.fc_entry.get()), dna=int((self.dna_entry.get())),
                           ode=int(self.ode_entry.get()), oie=int(self.oie_entry.get()),
                           tax=int((self.tax_entry.get())))

            self.b_s2 = Bs(name=self.company_entry.get(), year=self.year_entry.get(),
                           sf=int(self.share_fund_entry.get()), ps=int(self.ps_entry.get()),
                           ltb=int(self.ltb_entry.get()), oll=int(self.oll_entry.get()), tp=int(self.tp_entry.get()),
                           ocl=int(self.ocl_entry.get()), fa=int(self.fa_entry.get()), lti=int(self.lti_entry.get()),
                           ltl=int(self.ltl_entry.get()), ola=int(self.ola_entry.get()), inv=int(self.inv_entry.get()),
                           tr=int(self.tr_entry.get()), cac=int(self.cac_entry.get()), oca=int(self.oca_entry.get()),
                           share_no=int(self.nes_entry.get()), dps=int(self.dps_entry.get()),
                           mps=int(self.mps_entry.get()))

            self.company_data2 = (self.p_l2, self.b_s2)

            for self.item in self.delete_list:
                self.item.delete(0, END)

        if self.count == 3 and self.count <= self.no_of_years:
            self.p_l3 = Pl(name=self.company_entry.get(), year=self.year_entry.get(),
                           rfo=int(self.rfo_entry.get()), oi=int(self.oi_entry.get()), com=int(self.com_entry.get()),
                           purchases=int(self.purchase_entry.get()), cii=int(self.cii_entry.get()),
                           ebe=int(self.ebe_entry.get()), fc=int(self.fc_entry.get()), dna=int((self.dna_entry.get())),
                           ode=int(self.ode_entry.get()), oie=int(self.oie_entry.get()),
                           tax=int((self.tax_entry.get())))

            self.b_s3 = Bs(name=self.company_entry.get(), year=self.year_entry.get(),
                           sf=int(self.share_fund_entry.get()), ps=int(self.ps_entry.get()),
                           ltb=int(self.ltb_entry.get()), oll=int(self.oll_entry.get()), tp=int(self.tp_entry.get()),
                           ocl=int(self.ocl_entry.get()), fa=int(self.fa_entry.get()), lti=int(self.lti_entry.get()),
                           ltl=int(self.ltl_entry.get()), ola=int(self.ola_entry.get()), inv=int(self.inv_entry.get()),
                           tr=int(self.tr_entry.get()), cac=int(self.cac_entry.get()), oca=int(self.oca_entry.get()),
                           share_no=int(self.nes_entry.get()), dps=int(self.dps_entry.get()),
                           mps=int(self.mps_entry.get()))

            self.company_data3 = (self.p_l3, self.b_s3)

            for self.item in self.delete_list:
                self.item.delete(0, END)

        if self.count == 4 and self.count <= self.no_of_years:
            self.p_l4 = Pl(name=self.company_entry.get(), year=self.year_entry.get(),
                           rfo=int(self.rfo_entry.get()), oi=int(self.oi_entry.get()), com=int(self.com_entry.get()),
                           purchases=int(self.purchase_entry.get()), cii=int(self.cii_entry.get()),
                           ebe=int(self.ebe_entry.get()), fc=int(self.fc_entry.get()), dna=int((self.dna_entry.get())),
                           ode=int(self.ode_entry.get()), oie=int(self.oie_entry.get()),
                           tax=int((self.tax_entry.get())))

            self.b_s4 = Bs(name=self.company_entry.get(), year=self.year_entry.get(),
                           sf=int(self.share_fund_entry.get()), ps=int(self.ps_entry.get()),
                           ltb=int(self.ltb_entry.get()), oll=int(self.oll_entry.get()), tp=int(self.tp_entry.get()),
                           ocl=int(self.ocl_entry.get()), fa=int(self.fa_entry.get()), lti=int(self.lti_entry.get()),
                           ltl=int(self.ltl_entry.get()), ola=int(self.ola_entry.get()), inv=int(self.inv_entry.get()),
                           tr=int(self.tr_entry.get()), cac=int(self.cac_entry.get()), oca=int(self.oca_entry.get()),
                           share_no=int(self.nes_entry.get()), dps=int(self.dps_entry.get()),
                           mps=int(self.mps_entry.get()))

            self.company_data4 = (self.p_l4, self.b_s4)

            for self.item in self.delete_list:
                self.item.delete(0, END)

        if self.count == 5 and self.count <= self.no_of_years:
            self.p_l5 = Pl(name=self.company_entry.get(), year=self.year_entry.get(),
                           rfo=int(self.rfo_entry.get()), oi=int(self.oi_entry.get()), com=int(self.com_entry.get()),
                           purchases=int(self.purchase_entry.get()), cii=int(self.cii_entry.get()),
                           ebe=int(self.ebe_entry.get()), fc=int(self.fc_entry.get()), dna=int((self.dna_entry.get())),
                           ode=int(self.ode_entry.get()), oie=int(self.oie_entry.get()),
                           tax=int((self.tax_entry.get())))

            self.b_s5 = Bs(name=self.company_entry.get(), year=self.year_entry.get(),
                           sf=int(self.share_fund_entry.get()), ps=int(self.ps_entry.get()),
                           ltb=int(self.ltb_entry.get()), oll=int(self.oll_entry.get()), tp=int(self.tp_entry.get()),
                           ocl=int(self.ocl_entry.get()), fa=int(self.fa_entry.get()), lti=int(self.lti_entry.get()),
                           ltl=int(self.ltl_entry.get()), ola=int(self.ola_entry.get()), inv=int(self.inv_entry.get()),
                           tr=int(self.tr_entry.get()), cac=int(self.cac_entry.get()), oca=int(self.oca_entry.get()),
                           share_no=int(self.nes_entry.get()), dps=int(self.dps_entry.get()),
                           mps=int(self.mps_entry.get()))

            self.company_data5 = (self.p_l5, self.b_s5)

            for self.item in self.delete_list:
                self.item.delete(0, END)

        if self.count == 6 and self.count <= self.no_of_years:
            self.p_l6 = Pl(name=self.company_entry.get(), year=self.year_entry.get(),
                           rfo=int(self.rfo_entry.get()), oi=int(self.oi_entry.get()), com=int(self.com_entry.get()),
                           purchases=int(self.purchase_entry.get()), cii=int(self.cii_entry.get()),
                           ebe=int(self.ebe_entry.get()), fc=int(self.fc_entry.get()), dna=int((self.dna_entry.get())),
                           ode=int(self.ode_entry.get()), oie=int(self.oie_entry.get()),
                           tax=int((self.tax_entry.get())))

            self.b_s6 = Bs(name=self.company_entry.get(), year=self.year_entry.get(),
                           sf=int(self.share_fund_entry.get()), ps=int(self.ps_entry.get()),
                           ltb=int(self.ltb_entry.get()), oll=int(self.oll_entry.get()), tp=int(self.tp_entry.get()),
                           ocl=int(self.ocl_entry.get()), fa=int(self.fa_entry.get()), lti=int(self.lti_entry.get()),
                           ltl=int(self.ltl_entry.get()), ola=int(self.ola_entry.get()), inv=int(self.inv_entry.get()),
                           tr=int(self.tr_entry.get()), cac=int(self.cac_entry.get()), oca=int(self.oca_entry.get()),
                           share_no=int(self.nes_entry.get()), dps=int(self.dps_entry.get()),
                           mps=int(self.mps_entry.get()))

            self.company_data6 = (self.p_l6, self.b_s6)

            for self.item in self.delete_list:
                self.item.delete(0, END)
        self.count += 1

    def clear_data(self):
        self.clear_list = [self.p_l1, self.b_s1, self.company_data1, self.p_l2, self.b_s2, self.company_data2,
                           self.p_l3, self.b_s3, self.company_data3, self.p_l4, self.b_s4, self.company_data4,
                           self.p_l5, self.b_s5, self.company_data5, self.p_l6, self.b_s6, self.company_data6]
        for self.item in self.clear_list:
            del self.item

    def comp_statement(self):
        self.base_year = self.base_year_entry.get()
        self.current_year = self.current_year_entry.get()
        statement = ComparativeStatement(base=self.base_year, current=self.current_year, pl_frame=self.comp_p_l_frame,
                                         bs_frame=self.comp_bs_frame, data1=self.company_data1,
                                         data2=self.company_data2, data3=self.company_data3, data4=self.company_data4,
                                         data5=self.company_data5, data6=self.company_data6)
        statement.create_statement()

    def com_size_statement(self):
        if self.company_data1 is not None:
            if self.com_year_entry.get() == self.company_data1[0].year:
                self.com_pl = self.company_data1[0].com_size_pl()
                self.com_bs = self.company_data1[1].com_size_bs()
                statement = CommonSizeStatement(pl=self.com_pl, bs=self.com_bs, pl_frame=self.common_p_l_frame,
                                                bs_frame=self.common_bs_frame)
                statement.create_statement()
        if self.company_data2 is not None:
            if self.com_year_entry.get() == self.company_data2[0].year:
                self.com_pl = self.company_data2[0].com_size_pl()
                self.com_bs = self.company_data2[1].com_size_bs()
                statement = CommonSizeStatement(pl=self.com_pl, bs=self.com_bs, pl_frame=self.common_p_l_frame,
                                                bs_frame=self.common_bs_frame)
                statement.create_statement()
        if self.company_data3 is not None:
            if self.com_year_entry.get() == self.company_data3[0].year:
                self.com_pl = self.company_data3[0].com_size_pl()
                self.com_bs = self.company_data3[1].com_size_bs()
                statement = CommonSizeStatement(pl=self.com_pl, bs=self.com_bs, pl_frame=self.common_p_l_frame,
                                                bs_frame=self.common_bs_frame)
                statement.create_statement()
        if self.company_data4 is not None:
            if self.com_year_entry.get() == self.company_data4[0].year:
                self.com_pl = self.company_data4[0].com_size_pl()
                self.com_bs = self.company_data4[1].com_size_bs()
                statement = CommonSizeStatement(pl=self.com_pl, bs=self.com_bs, pl_frame=self.common_p_l_frame,
                                                bs_frame=self.common_bs_frame)
                statement.create_statement()
        if self.company_data5 is not None:
            if self.com_year_entry.get() == self.company_data5[0].year:
                self.com_pl = self.company_data5[0].com_size_pl()
                self.com_bs = self.company_data5[1].com_size_bs()
                statement = CommonSizeStatement(pl=self.com_pl, bs=self.com_bs, pl_frame=self.common_p_l_frame,
                                                bs_frame=self.common_bs_frame)
                statement.create_statement()
        if self.company_data6 is not None:
            if self.com_year_entry.get() == self.company_data6[0].year:
                self.com_pl = self.company_data6[0].com_size_pl()
                self.com_bs = self.company_data6[1].com_size_bs()
                statement = CommonSizeStatement(pl=self.com_pl, bs=self.com_bs, pl_frame=self.common_p_l_frame,
                                                bs_frame=self.common_bs_frame)
                statement.create_statement()

    def trend_rfo(self):
        self.x = []
        self.y = []
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
        trend_statement = TrendAnalysis(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                        graph_frame=self.trend_graph_frame, title='Revenue From Operations')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_gp(self):
        self.x = []
        self.y = []
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
        trend_statement = TrendAnalysis(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                        graph_frame=self.trend_graph_frame, title='Revenue From Operations')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_op(self):
        self.x = []
        self.y = []
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
        trend_statement = TrendAnalysis(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                        graph_frame=self.trend_graph_frame, title='Operating Profit')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_np(self):
        self.x = []
        self.y = []
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
        trend_statement = TrendAnalysis(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                        graph_frame=self.trend_graph_frame, title='Net Profit')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_debt(self):
        self.x = []
        self.y = []
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
        trend_statement = TrendAnalysis(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                        graph_frame=self.trend_graph_frame, title='Debt')
        trend_statement.create_table()
        trend_statement.create_graph()

    def trend_ox(self):
        self.x = []
        self.y = []
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
        trend_statement = TrendAnalysis(trend=self.y, year=self.x, table_frame=self.trend_table_frame,
                                        graph_frame=self.trend_graph_frame, title='Operating Expenses')
        trend_statement.create_table()
        trend_statement.create_graph()

    def ratio(self):
        ratios1 = Ratios(self.company_data1[0], self.company_data1[1])
        ratios2 = Ratios(self.company_data2[0], self.company_data2[1])
        ratios3 = Ratios(self.company_data3[0], self.company_data3[1])
        ratios4 = Ratios(self.company_data4[0], self.company_data4[1])
        ratios5 = Ratios(self.company_data5[0], self.company_data5[1])
        ratios6 = Ratios(self.company_data6[0], self.company_data6[1])

        if self.liquidity_ratio.get() == 'Current Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.current_ratio(), ratios2.current_ratio(), ratios3.current_ratio(),
                          ratios4.current_ratio(), ratios5.current_ratio(), ratios6.current_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()
        if self.liquidity_ratio.get() == 'Quick Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.quick_ratio(), ratios2.quick_ratio(), ratios3.quick_ratio(),
                          ratios4.quick_ratio(), ratios5.quick_ratio(), ratios6.quick_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.liquidity_ratio.get() == 'Cash Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.absolute_ratio(), ratios2.absolute_ratio(), ratios3.absolute_ratio(),
                          ratios4.absolute_ratio(), ratios5.absolute_ratio(), ratios6.absolute_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.solvency_ratio.get() == 'Debt to Equity Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.debt_equity_ratio(), ratios2.debt_equity_ratio(), ratios3.debt_equity_ratio(),
                          ratios4.debt_equity_ratio(), ratios5.debt_equity_ratio(), ratios6.debt_equity_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.solvency_ratio.get() == 'Debt to Capital Employed Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.debt_capital_ratio(), ratios2.debt_capital_ratio(), ratios3.debt_capital_ratio(),
                          ratios4.debt_capital_ratio(), ratios5.debt_capital_ratio(), ratios6.debt_capital_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.solvency_ratio.get() == 'Proprietary Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.proprietary_ratio(), ratios2.proprietary_ratio(), ratios3.proprietary_ratio(),
                          ratios4.proprietary_ratio(), ratios5.proprietary_ratio(), ratios6.proprietary_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.solvency_ratio.get() == 'Interest Coverage Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.icr(), ratios2.icr(), ratios3.icr(), ratios4.icr(), ratios5.icr(), ratios6.icr()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Gross Profit Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.gp_ratio(), ratios2.gp_ratio(), ratios3.gp_ratio(), ratios4.gp_ratio(),
                          ratios5.gp_ratio(), ratios6.gp_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Proprietary Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.proprietary_ratio(), ratios2.proprietary_ratio(), ratios3.proprietary_ratio(),
                          ratios4.proprietary_ratio(), ratios5.proprietary_ratio(), ratios6.proprietary_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Operating Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.operating_ratio(), ratios2.operating_ratio(), ratios3.operating_ratio(),
                          ratios4.operating_ratio(), ratios5.operating_ratio(), ratios6.operating_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Operating Profit Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.operating_profit_ratio(), ratios2.operating_profit_ratio(),
                          ratios3.operating_profit_ratio(), ratios4.operating_profit_ratio(),
                          ratios5.operating_profit_ratio(), ratios6.operating_profit_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Net Profit Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.net_profit_ratio(), ratios2.net_profit_ratio(), ratios3.net_profit_ratio(),
                          ratios4.net_profit_ratio(), ratios5.net_profit_ratio(), ratios6.net_profit_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Return on Investment Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.roi_ratio(), ratios2.roi_ratio(), ratios3.roi_ratio(),  ratios4.roi_ratio(),
                          ratios5.roi_ratio(), ratios6.roi_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Return on Networth Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.ronw_ratio(), ratios2.ronw_ratio(), ratios3.ronw_ratio(), ratios4.ronw_ratio(),
                          ratios5.ronw_ratio(), ratios6.ronw_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()
        if self.profitability_ratio.get() == 'Earnings Per Share':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.eps_ratio(), ratios2.eps_ratio(), ratios3.eps_ratio(), ratios4.eps_ratio(),
                          ratios5.eps_ratio(), ratios6.eps_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Book Value Per Share':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.bps_ratio(), ratios2.bps_ratio(), ratios3.bps_ratio(), ratios4.bps_ratio(),
                          ratios5.bps_ratio(), ratios6.bps_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Dividend Payout Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.dp_ratio(), ratios2.dp_ratio(), ratios3.dp_ratio(), ratios4.dp_ratio(),
                          ratios5.ronw_ratio(), ratios6.ronw_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.profitability_ratio.get() == 'Price Earning Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.pe_ratio(), ratios2.pe_ratio(), ratios3.pe_ratio(), ratios4.pe_ratio(),
                          ratios5.pe_ratio(), ratios6.pe_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Inventory Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.inventory_turnover_ratio(), ratios2.inventory_turnover_ratio(),
                          ratios3.inventory_turnover_ratio(), ratios4.inventory_turnover_ratio(),
                          ratios5.inventory_turnover_ratio(), ratios6.inventory_turnover_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Debtors Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.tr_turnover_ratio(), ratios2.tr_turnover_ratio(), ratios3.tr_turnover_ratio(),
                          ratios4.tr_turnover_ratio(), ratios5.tr_turnover_ratio(), ratios6.tr_turnover_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Creditors Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.tp_turnover_ratio(), ratios2.tp_turnover_ratio(), ratios3.tp_turnover_ratio(),
                          ratios4.tp_turnover_ratio(), ratios5.tp_turnover_ratio(), ratios6.tp_turnover_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Capital Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.capital_turnover_ratio(), ratios2.capital_turnover_ratio(),
                          ratios3.capital_turnover_ratio(), ratios4.capital_turnover_ratio(),
                          ratios5.capital_turnover_ratio(), ratios6.capital_turnover_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Fixed Asset Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.fixed_asset_turnover_ratio(), ratios2.fixed_asset_turnover_ratio(),
                          ratios3.fixed_asset_turnover_ratio(), ratios4.fixed_asset_turnover_ratio(),
                          ratios5.fixed_asset_turnover_ratio(), ratios6.fixed_asset_turnover_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()

        if self.turnover_ratio.get() == 'Working Capital Turnover Ratio':
            year_list = [self.company_data1[0].year, self.company_data2[0].year, self.company_data3[0].year,
                         self.company_data4[0].year, self.company_data5[0].year, self.company_data6[0].year]
            ratio_list = [ratios1.working_capital_turnover_ratio(), ratios2.working_capital_turnover_ratio(),
                          ratios3.working_capital_turnover_ratio(), ratios4.working_capital_turnover_ratio(),
                          ratios5.working_capital_turnover_ratio(), ratios6.working_capital_turnover_ratio()]
            statement = RatioAnalysis(year=year_list, ratio=ratio_list, table_frame=self.ratio_table_frame,
                                      graph_frame=self.ratio_graph_frame)
            statement.create_table()
            statement.create_graph()


master = Tk()
obj = FinancialAnalysis(master)
master.mainloop()


