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
        assert [row["id"] for row in res.json()["result"]] == [105, 104, 103, 102, 101]

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


@pytest.mark.django_db
class TestInsertLog:
    """insert_log APIをテストする"""

    @pytest.fixture
    def target_path(self):
        return "/api/insert"

    @pytest.mark.parametrize(
        "input_data, expected_read_at",
        [
            (
                {
                    "name": "test_member123",
                    "category": "business",
                    "title": "test_title",
                    "price": 123,
                    "readAt": "2024-04-10",
                    "isPublic": True,
                    "isFavorite": True,
                },
                date(2024, 4, 10),
            ),
            (
                {
                    "name": "test_member234",
                    "category": "tech",
                    "title": "test_title2",
                    "price": 234,
                    "readAt": "2024-04-11",
                    "isPublic": False,
                    "isFavorite": False,
                },
                date(2024, 4, 11),
            ),
        ],
    )
    @pytest.mark.freeze_time("2024-04-10 09:00:00+9:00")
    def test_it(self, target_path, client, input_data, expected_read_at):
        """jsonをpostすると200を返し、ReadHistoryが作成されていること"""

        # arrange
        from ..models import ReadHistory

        executed_time = datetime(2024, 4, 10, 9, 0, 0, tzinfo=ZoneInfo("Asia/Tokyo"))

        # act
        res = client.post(
            target_path,
            json.dumps(input_data),
            content_type="application/json",
        )

        # assert
        assert res.status_code == 200

        last = ReadHistory.objects.last()
        assert (
            last.name,
            last.category,
            last.title,
            last.price,
            last.read_at,
            last.is_public,
            last.is_favorite,
            last.created_at,
            last.updated_at,
        ) == (
            input_data["name"],
            input_data["category"],
            input_data["title"],
            input_data["price"],
            expected_read_at,
            input_data["isPublic"],
            input_data["isFavorite"],
            executed_time,
            executed_time,
        )
