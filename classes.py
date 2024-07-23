class OSV:

    def __init__(
            self, account,
            period, counterpart,
            deb_start, kred_start,
            deb_turnover, kred_turnover,
            deb_end, kred_end
    ):
        self.account = account
        self.period = period
        self.counterpart = counterpart
        self.deb_start = deb_start
        self.kred_start = kred_start
        self.deb_turnover = deb_turnover
        self.kred_turnover = kred_turnover
        self.deb_end = deb_end
        self.kred_end = kred_end


class OSV60(OSV):
    pass


class OSV62(OSV):
    pass


class OSV76(OSV):
    pass
