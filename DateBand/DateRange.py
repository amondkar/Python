import operator


class DateRange:
    def __init__(self, start_dt, end_dt):
        self.start_dt = start_dt
        self.end_dt = end_dt
        #self.keys = keys

    def __eq__(self, other):
        return ((self.start_dt == other.start_dt) and (self.end_dt == other.end_dt))

    def __contains__(self, other):
        return ((self.start_dt <= other.start_dt <= self.end_dt) and ((self.start_dt <= other.end_dt <= self.end_dt)))

    def contains(self, dt):
        return (self.start_dt <= dt <= self.end_dt)

    def __repr__(self):
        return '<DateRange({!r}, {!r})>'.format(
            self.start_dt, self.end_dt
        )
    def __hash__(self):
      return hash((self.start_dt, self.end_dt))


