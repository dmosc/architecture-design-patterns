from math import sqrt


class SquarePeg:
    width: int

    def __init__(self, _width: int):
        self.width = _width

    def get_width(self):
        return self.width


class RoundPeg:
    radius: int

    def __init__(self, _radius: int):
        self.radius = _radius

    def get_radius(self):
        return self.radius


class SquarePegAdapter(RoundPeg):
    peg: SquarePeg

    def __init__(self, _peg: SquarePeg):
        self.peg = _peg

    def get_radius(self):
        return self.peg.get_width() * sqrt(2) / 2


class RoundHole:
    radius: int

    def __init__(self, _radius: int):
        self.radius = _radius

    def get_radius(self):
        return self.radius

    def fits(self, peg: RoundPeg):
        return self.radius >= peg.get_radius()


hole = RoundHole(5)
hole_rad = hole.get_radius()
round_peg = RoundPeg(5)
assert hole.fits(round_peg), f'{round_peg.get_radius()}u peg does not fit in {hole_rad}u hole.'

sm_square_peg = SquarePeg(5)
lg_square_peg = SquarePeg(10)
# hole.fits(sm_square_peg) doesn't compile since SquarePeg != RoundPeg

sm_square_peg_ad = SquarePegAdapter(sm_square_peg)
lg_square_peg_ad = SquarePegAdapter(lg_square_peg)
assert hole.fits(sm_square_peg_ad), f'{sm_square_peg_ad.get_radius()}u peg does not fit in {hole_rad}u hole.'
assert not hole.fits(lg_square_peg_ad), f'{lg_square_peg_ad.get_radius()}u peg does not fit in {hole_rad}u hole.'
