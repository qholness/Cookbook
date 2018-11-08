import unittest


class InitTests(unittest.TestCase):
    def test_units_system_select(self):
        import CookingCompendium as cc
        cc.get_units_system()  # Need to figure out how to pass args to input
        assert(cc.units is not None)
