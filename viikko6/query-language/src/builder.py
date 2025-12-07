from matchers import All, And, HasAtLeast, HasFewerThan, Not, Or, PlaysIn


class QueryBuilder:
    def __init__(self, matcher=None):
        self.matcher_olio = All() if matcher is None else matcher

    def has_at_least(self, val, attr):
        return QueryBuilder(And(self.matcher_olio, HasAtLeast(val, attr)))

    def has_fewer_than(self, val, attr):
        return QueryBuilder(And(self.matcher_olio, HasFewerThan(val, attr)))

    def plays_in(self, team):
        return QueryBuilder(And(self.matcher_olio, PlaysIn(team)))

    def one_of(self, *matchers):
        processed = []
        for m in matchers:
            if isinstance(m, QueryBuilder):
                processed.append(m.matcher_olio)
            else:
                processed.append(m)
        return QueryBuilder(Or(*processed))

    def not_(self):
        return QueryBuilder(Not(self.matcher_olio))

    def build(self):
        return self.matcher_olio