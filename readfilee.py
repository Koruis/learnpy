import unittest


def get_name(*names):
    name = ""
    for n in names:
        name += n
    return name


class NameTest(unittest.TestCase):

    def test_first_last_name(self):
        f_name = get_name('Zbl', 'anana')
        self.assertEqual(f_name, 'Zblanana')
    def test_first_mid_last_name(self):
        f_name = get_name('Zbl', 'anana', 'so')
        self.assertEqual(f_name, 'Zblananaso')

unittest.main()