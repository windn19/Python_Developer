from Light import Desk
import pytest


class Test_Desk:

    def setup(self):
        self.desk = Desk()

    def test_issue_cards(self):
        card = self.desk.issue_cards(2)
        assert sum(len(x) for x in card.values()) == 2

    def test_is_empty(self):
        assert not self.desk.is_empty


if __name__=='__main__':
    pytest.main()
