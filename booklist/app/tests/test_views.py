import json
from datetime import date, datetime
from zoneinfo import ZoneInfo

import pytest

@pytest.mark.django_db
class TestReadLog:
    """read_log APIをテストする"""

    @pytest.fixture
    def target_path(self):
        return "/api/read"

    def test_response(self, target_path, client):
        """登録したReadHistoryを返すこと"""

        # arrange
        from .factories import ReadHistoryFactory

        ReadHistoryFactory(
            pk=100,
            name="テストname1",
            category="tech",
            title="テスト書籍1",
            price=1000,
            read_at=date(2023, 1, 1),
            is_public=True,
            is_favorite=True,
        )

        # act
        res = client.get(target_path)

        # assert
        assert res.status_code == 200
        assert res.json() == {
            "result": [
                {
                    "id": 100,
                    "name": "テストname1",
                    "category": "tech",
                    "title": "テスト書籍1",
                    "price": 1000,
                    "readAt": "2023-01-01",
                    "isFavorite": True,
                }
            ]
        }

    def test_ids_ordered_by_id_desc(self, target_path, client):
        """結果はidの降順で並べられていること"""

        # arrange
        from .factories import ReadHistoryFactory

        ReadHistoryFactory(pk=101)
        ReadHistoryFactory(pk=102)
        ReadHistoryFactory(pk=103)
        ReadHistoryFactory(pk=104)
        ReadHistoryFactory(pk=105)

        # act
        res = client.get(target_path)

        # assert
        assert res.status_code == 200
        assert [row["id"] for row in res.json()["result"]] == [
            105, 104, 103, 102, 101
        ]

    def test_ids_filtered_non_public_rows(self, target_path, client):
        """公開フラグがONであるデータ以外はレスポンスから除外されていること。"""

        # arrange
        from .factories import ReadHistoryFactory

        ReadHistoryFactory(pk=101, is_public=False)
        ReadHistoryFactory(pk=102)
        ReadHistoryFactory(pk=103, is_public=False)
        ReadHistoryFactory(pk=104)

        # act
        res = client.get(target_path)

        # assert
        assert res.status_code == 200
        assert [row["id"] for row in res.json()["result"]] == [104, 102]
