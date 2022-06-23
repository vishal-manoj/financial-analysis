class Pl:
    def __init__(self, **pl_data):
        self.com_rfo = None
        self.com_oi = None
        self.com_tr = None
        self.com_com = None
        self.com_purchases = None
        self.com_cii = None
        self.com_gp = None
        self.com_ebe = None
        self.com_fc = None
        self.com_dna = None
        self.com_ode = None
        self.com_oie = None
        self.com_pbt = None
        self.com_tax = None
        self.com_pat = None
        self.com_pl_values = None
        for key, value in pl_data.items():
            if key == 'name':
                self.company_name = value
            if key == 'year':
                self.year = value
            if key == 'rfo':
                self.rfo = value
            if key == 'oi':
                self.oi = value
            if key == 'com':
                self.com = value
            if key == 'purchases':
                self.purchases = value
            if key == 'cii':
                self.cii = value
            if key == 'ebe':
                self.ebe = value
            if key == 'fc':
                self.fc = value
            if key == 'dna':
                self.dna = value
            if key == 'ode':
                self.ode = value
            if key == 'oie':
                self.oie = value
            if key == 'tax':
                self.tax = value

        self.tr = self.rfo + self.oi
        self.cogs = self.com + self.purchases + self.cii + self.ode
        self.gp = self.rfo - self.cogs
        self.oe = self.cogs + self.ebe + self.fc + self.oie
        self.op = self.rfo - self.oe
        self.ebit = self.tr - (self.cogs + self.ebe + self.dna + self.oie)
        self.te = self.cogs + self.ebe + self.fc + self.dna + self.oie
        self.pbt = self.tr - self.te
        self.pat = self.pbt - self.tax

    def __sub__(self, other):
        self.comp_rfo = self.rfo - other.rfo
        self.comp_oi = self.oi - other.oi
        self.comp_tr = self.tr - other.tr
        self.comp_com = self.com - other.com
        self.comp_purchases = self.purchases - other.purchases
        self.comp_cii = self.cii - other.cii
        self.comp_gp = self.gp - other.gp
        self.comp_ebe = self.ebe - other.ebe
        self.comp_fc = self.fc - other.fc
        self.comp_dna = self.dna - other.dna
        self.comp_ode = self.ode - other.ode
        self.comp_oie = self.oie - other.oie
        self.comp_pbt = self.pbt - other.pbt
        self.comp_tax = self.tax - other.tax
        self.comp_pat = self.pat - other.pat

        self.comp_rfo_Change = (self.comp_rfo/self.rfo) * 100
        self.comp_oi_change = (self.comp_oi/self.oi) * 100
        self.comp_tr_change = (self.comp_tr/self.tr) * 100
        self.comp_com_change = (self.comp_com/self.com) * 100
        self.comp_purchases_change = (self.comp_purchases/self.purchases) * 100
        self.comp_cii_change = (self.comp_cii/self.cii) * 100
        self.comp_gp_change = (self.comp_gp/self.gp) * 100
        self.comp_ebe_change = (self.comp_ebe/self.ebe) * 100
        self.comp_fc_change = (self.comp_fc/self.fc) * 100
        self.comp_dna_change = (self.comp_dna/self.dna) * 100
        self.comp_ode_change = (self.comp_ode/self.ode) * 100
        self.comp_oie_change = (self.comp_oie/self.oie) * 100
        self.comp_pbt_change = (self.comp_pbt/self.pbt) * 100
        self.comp_tax_change = (self.comp_tax/self.tax) * 100
        self.comp_pat_change = (self.comp_pat/self.pat) * 100

        self.comp_pl_values = [('Revenue from Operations', other.rfo, self.rfo, self.comp_rfo, self.comp_rfo_Change),
                               ('Other Income', other.oi, self.oi, self.comp_oi, self.comp_oi_change),
                               ('Total Revenue', other.tr, self.tr, self.comp_tr, self.comp_tr_change),
                               ('Cost of Materials', other.com, self.com, self.comp_com, self.comp_com_change),
                               ('Purchases', other.purchases, self.purchases, self.comp_purchases,
                                self.comp_purchases_change),
                               ('Change in Inventory', other.cii, self.cii, self.comp_cii, self.comp_cii_change),
                               ('Other Direct Expenses', other.ode, self.ode, self.comp_ode, self.comp_ode_change),
                               ('Gross Profit', other.gp, self.gp, self.comp_gp, self.comp_gp_change),
                               ('Employee Benefit Expenses', other.ebe, self.ebe, self.comp_ebe, self.comp_ebe_change),
                               ('Finance Cost', other.fc, self.fc, self.comp_fc, self.comp_fc_change),
                               ('Depreciation and Amortization', other.dna, self.dna, self.comp_dna,
                                self.comp_dna_change),
                               ('Other Indirect Expenses', other.oie, self.oie, self.comp_oie, self.comp_oie_change),
                               ('Profit Before Tax', other.pbt, self.pbt, self.comp_pbt, self.comp_pbt_change),
                               ('Tax', other.tax, self.tax, self.comp_tax, self.comp_tax_change),
                               ('Profit After Tax', other.pat, self.pat, self.comp_pat, self.comp_pat_change)
                               ]
        return self.comp_pl_values

    def com_size_pl(self):
        self.com_rfo = (self.rfo / self.rfo) * 100
        self.com_oi = (self.oi / self.rfo) * 100
        self.com_tr = (self.tr / self.rfo) * 100
        self.com_com = (self.com / self.rfo) * 100
        self.com_purchases = (self.purchases / self.rfo) * 100
        self.com_cii = (self.cii / self.rfo) * 100
        self.com_gp = (self.gp / self.rfo) * 100
        self.com_ebe = (self.ebe / self.rfo) * 100
        self.com_fc = (self.fc / self.rfo) * 100
        self.com_dna = (self.dna / self.rfo) * 100
        self.com_ode = (self.ode / self.rfo) * 100
        self.com_oie = (self.oie / self.rfo) * 100
        self.com_pbt = (self.pbt / self.rfo) * 100
        self.com_tax = (self.tax / self.rfo) * 100
        self.com_pat = (self.pat / self.rfo) * 100

        self.com_pl_values = [('Revenue from Operations', self.rfo, self.com_rfo),
                              ('Other Income', self.oi, self.com_oi),
                              ('Total Revenue', self.tr, self.com_tr),
                              ('Cost of Materials', self.com, self.com_com),
                              ('Purchases', self.purchases, self.com_purchases),
                              ('Change in Inventory', self.cii, self.com_cii),
                              ('Other Direct Expenses', self.ode, self.com_ode),
                              ('Gross Profit', self.gp, self.com_gp),
                              ('Employee Benefit Expenses', self.ebe, self.com_ebe),
                              ('Finance Cost', self.fc, self.com_fc),
                              ('Depreciation and Amortization', self.dna, self.com_dna),
                              ('Other Indirect Expenses', self.oie, self.com_oie),
                              ('Profit Before Tax', self.pbt, self.com_pbt),
                              ('Tax', self.tax, self.com_tax),
                              ('Profit After Tax', self.pat, self.com_pat)
                              ]
        return self.com_pl_values


class Bs:
    def __init__(self, **bs_data):
        self.tl = None
        self.ta = None
        self.com_sf = None
        self.com_ltb = None
        self.com_oll = None
        self.com_tp = None
        self.com_ocl = None
        self.com_fa = None
        self.com_lti = None
        self.com_ltl = None
        self.com_ola = None
        self.com_inv = None
        self.com_tr = None
        self.com_cac = None
        self.com_oca = None
        self.com_bs_values = None
        for key, value in bs_data.items():
            if key == 'name':
                self.company_name = value
            if key == 'year':
                self.year = value
            if key == 'sf':
                self.sf = value
            if key == 'ps':
                self.ps = value
            if key == 'ltb':
                self.ltb = value
            if key == 'oll':
                self.oll = value
            if key == 'tp':
                self.tp = value
            if key == 'ocl':
                self.ocl = value
            if key == 'fa':
                self.fa = value
            if key == 'lti':
                self.lti = value
            if key == 'ltl':
                self.ltl = value
            if key == 'ola':
                self.ola = value
            if key == 'inv':
                self.inv = value
            if key == 'tr':
                self.tr = value
            if key == 'cac':
                self.cac = value
            if key == 'oca':
                self.oca = value
            if key == 'share_no':
                self.share_no = value
            if key == 'dps':
                self.dps = value
            if key == 'mps':
                self.mps = value

    def __sub__(self, other):
        self.comp_sf = self.sf - other.sf
        self.comp_ltb = self.ltb - other.ltb
        self.comp_oll = self.oll - other.oll
        self.comp_tp = self.tp - other.tp
        self.comp_ocl = self.ocl - other.ocl
        self.comp_fa = self.fa - other.fa
        self.comp_lti = self.lti - other.lti
        self.comp_ltl = self.ltl - other.ltl
        self.comp_ola = self.ola - other.ola
        self.comp_inv = self.inv - other.inv
        self.comp_tr = self.tr - other.tr
        self.comp_cac = self.cac - other.cac
        self.comp_oca = self.oca - other.oca

        self.comp_sf_change = (self.comp_sf/self.sf) * 100
        self.comp_ltb_change = (self.comp_ltb/self.ltb) * 100
        self.comp_oll_change = (self.comp_oll/self.oll) * 100
        self.comp_tp_change = (self.comp_tp/self.tp) * 100
        self.comp_ocl_change = (self.comp_ocl/self.ocl) * 100
        self.comp_fa_change = (self.comp_fa/self.fa) * 100
        self.comp_lti_change = (self.comp_lti/self.lti) * 100
        self.comp_ltl_change = (self.comp_ltl/self.ltl) * 100
        self.comp_ola_change = (self.comp_ola/self.ola) * 100
        self.comp_inv_change = (self.comp_inv/self.inv) * 100
        self.comp_tr_change = (self.comp_tr/self.tr) * 100
        self.comp_cac_change = (self.comp_cac/self.cac) * 100
        self.comp_oca_change = (self.comp_oca/self.oca) * 100

        self.comp_bs_values = [('Shareholders Fund', other.sf, self.sf, self.comp_sf, self.comp_sf_change),
                               ('Long Term Borrowings', other.ltb, self.ltb, self.comp_ltb, self.comp_ltb_change),
                               ('Other Long Term Liabilities', other.oll, self.oll, self.comp_oll,
                                self.comp_oll_change),
                               ('Trade Payable', other.tp, self.tp, self.comp_tp, self.comp_tp_change),
                               ('Other Current Liabilities', other.ocl, self.ocl, self.comp_ocl, self.comp_ocl_change),
                               ('Fixed Asset', other.fa, self.fa, self.comp_fa, self.comp_fa_change),
                               ('Long Term Investments', other.lti, self.lti, self.comp_lti, self.comp_lti_change),
                               ('Long Term Loans', other.ltl, self.ltl, self.comp_ltl, self.comp_ltl_change),
                               ('Other Long Term Assets', other.ola, self.ola, self.comp_ola, self.comp_ola_change),
                               ('Inventory', other.inv, self.inv, self.comp_inv, self.comp_inv_change),
                               ('Trade Receivables', other.tr, self.tr, self.comp_tr, self.comp_tr_change),
                               ('Cash and Cash Equivalents', other.cac, self.cac, self.comp_cac, self.comp_cac_change),
                               ('Other Current Assets', other.oca, self.oca, self.comp_oca, self.comp_oca_change),
                               ]

        return self.comp_bs_values

    def com_size_bs(self):
        self.tl = self.sf + self.ltb + self.oll + self.tp + self.ocl
        self.ta = self.fa + self.lti + self.ltl + self.ola + self.inv + self.tr + self.cac + self.oca
        self.com_sf = (self.sf / self.tl) * 100
        self.com_ltb = (self.ltb / self.tl) * 100
        self.com_oll = (self.oll / self.tl) * 100
        self.com_tp = (self.tp / self.tl) * 100
        self.com_ocl = (self.ocl / self.tl) * 100
        self.com_fa = (self.fa / self.ta) * 100
        self.com_lti = (self.lti / self.ta) * 100
        self.com_ltl = (self.ltl / self.ta) * 100
        self.com_ola = (self.ola / self.ta) * 100
        self.com_inv = (self.inv / self.ta) * 100
        self.com_tr = (self.tr / self.ta) * 100
        self.com_cac = (self.cac / self.ta) * 100
        self.com_oca = (self.oca / self.ta) * 100

        self.com_bs_values = [('Shareholders Fund', self.sf, self.com_sf),
                              ('Long Term Borrowings', self.ltb, self.com_ltb),
                              ('Other Long Term Liabilities', self.ltl, self.com_ltl),
                              ('Trade Payable', self.tp, self.com_tp),
                              ('Other Current Liabilities', self.ocl, self.com_ocl),
                              ('Fixed Assets', self.fa, self.com_fa),
                              ('Long Term Investments', self.lti, self.com_lti),
                              ('Long Term Loans', self.ltl, self.com_ltl),
                              ('Other Long Term Assets', self.ola, self.com_ola),
                              ('Inventory', self.inv, self.com_inv),
                              ('Trade Receivables', self.tr, self.com_tr),
                              ('Cash and Cash Equivalents', self.cac, self.com_cac),
                              ('Other Current Assets', self.oca, self.com_oca),
                              ]
        return self.com_bs_values


class Ratios:
    def __init__(self, pl, bs):
        self.pl = pl
        self.bs = bs
        self.current_r = None
        self.quick_r = None
        self.absolute_r = None
        self.debt_equity_r = None
        self.debt_capital_r = None
        self.proprietary_r = None
        self.debt_asset_r = None
        self.icr_r = None
        self.gp_r = None
        self.operating_r = None
        self.operating_profit_r = None
        self.net_profit_r = None
        self.roi_r = None
        self.ronw_r = None
        self.eps = None
        self.bps = None
        self.dpr = None
        self.per = None
        self.inv_turnover_r = None
        self.tr_turnover_r = None
        self.tp_turnover_r = None
        self.capital_turnover_r = None
        self.fa_turnover_r = None
        self.wc_turnover_r = None

    def current_ratio(self):
        self.current_r = (self.bs.inv + self.bs.tr + self.bs.cac + self.bs.oca)/(self.bs.tp + self.bs.ocl)
        return self.current_r

    def quick_ratio(self):
        self.quick_r = (self.bs.cac + self.bs.tr)/(self.bs.tp + self.bs.ocl)
        return self.quick_r

    def absolute_ratio(self):
        self.absolute_r = self.bs.cac/(self.bs.tp + self.bs.ocl)
        return self.absolute_r

    def debt_equity_ratio(self):
        self.debt_equity_r = self.bs.ltb/(self.bs.sf-self.bs.ps)
        return self.debt_equity_r

    def debt_capital_ratio(self):
        self.debt_capital_r = self.bs.ltb/(self.bs.sf + self.bs.ltb)
        return self.debt_capital_r

    def proprietary_ratio(self):
        self.proprietary_r = self.bs.sf/(self.bs.sf + self.bs.ltb)
        return self.proprietary_r

    def debt_asset_ratio(self):
        self.debt_asset_r = self.bs.ltb/(self.bs.fa + self.bs.lti + self.bs.ltl + self.bs.ola + self.bs.inv + self.bs.tr
                                         + self.bs.cac + self.bs.oca)
        return self.debt_asset_r

    def icr(self):
        self.icr_r = self.pl.ebit/self.bs.ltb
        return self.icr_r

    def gp_ratio(self):
        self.gp_r = self.pl.gp/self.pl.rfo
        return self.gp_r

    def operating_ratio(self):
        self.operating_r = (self.pl.cogs + self.pl.oe)/self.pl.rfo
        return self.operating_r

    def operating_profit_ratio(self):
        self.operating_profit_r = self.pl.op/self.pl.rfo
        return self.operating_profit_r

    def net_profit_ratio(self):
        self.net_profit_r = self.pl.pat/self.pl.rfo
        return self.net_profit_r

    def roi_ratio(self):
        self.roi_r = self.pl.ebit/(self.bs.fa + self.bs.lti + self.bs.ltl + self.bs.ola + self.bs.inv + self.bs.tr
                                   + self.bs.cac + self.bs.oca) - (self.bs.tp + self.bs.ocl)
        return self.roi_r

    def ronw_ratio(self):
        self.ronw_r = self.pl.pat/self.bs.sf
        return self.ronw_r

    def eps_ratio(self):
        self.eps = self.pl.pat/self.bs.share_no
        return self.eps

    def bps_ratio(self):
        self.bps = (self.bs.sf - self.bs.ps)/self.bs.share_no
        return self.bps

    def dp_ratio(self):
        self.dpr = self.bs.dps/(self.pl.pat/self.bs.share_no)
        return self.dpr

    def pe_ratio(self):
        self.per = self.bs.mps/(self.pl.pat/self.bs.share_no)
        return self.per

    def inventory_turnover_ratio(self):
        self.inv_turnover_r = self.pl.cogs/self.bs.inv
        return self.inv_turnover_r

    def tr_turnover_ratio(self):
        self.tr_turnover_r = self.pl.cogs/self.bs.tr
        return self.tr_turnover_r

    def tp_turnover_ratio(self):
        self.tp_turnover_r = self.pl.purchases/self.bs.tp
        return self.tp_turnover_r

    def capital_turnover_ratio(self):
        self.capital_turnover_r = self.pl.rfo/(self.bs.sf + self.bs.ltb)
        return self.capital_turnover_r

    def fixed_asset_turnover_ratio(self):
        self.fa_turnover_r = self.pl.rfo/self.bs.fa
        return self.fa_turnover_r

    def working_capital_turnover_ratio(self):
        self.wc_turnover_r = self.pl.rfo/(self.bs.inv + self.bs.tr + self.bs.cac + self.bs.oca) -\
                             (self.bs.tp + self.bs.ocl)
        return self.wc_turnover_r
















