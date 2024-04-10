from datetime import date

import factory
import factory.fuzzy


class ReadHistoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "app.ReadHistory"

    name = factory.Sequence(lambda n: f"test_numers{n}")
    category = factory.fuzzy.FuzzyChoice(["tech", "business"])
    title = factory.Sequence(lambda n: f"テスト書籍{n}")
    price = factory.fuzzy.FuzzyInteger(100000)
    read_at = factory.fuzzy.FuzzyDate(date(2020, 1, 1), date(2023, 12, 31))
    is_public = True
