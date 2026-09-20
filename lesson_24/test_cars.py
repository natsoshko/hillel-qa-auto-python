import logging

import pytest

BASE_URL = "http://127.0.0.1:8081"
logger = logging.getLogger(__name__)

class TestCars:
    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("price", 10),
            ("year", 5),
            ("year", 10),
            ("engine_volume", 5),
            ("engine_volume", 10),
            (None, 7),
        ]
    )
    def test_search_cars(self, session, sort_by, limit):
        params = {"sort_by": sort_by, "limit": limit}
        logger.info("GET /cars -> params: %s", params)
        response = session.get(f"{BASE_URL}/cars", params=params)
        logger.info("GET /cars -> status: %s", response.status_code)
        logger.info("GET /cars -> response: %s", response.text)

        assert response.status_code == 200
        cars = response.json()
        assert isinstance(cars, list)
        assert len(cars) == limit

        if sort_by:
            values = []

            for car in cars:
                values.append(car[sort_by])

            assert values == sorted(values)

        logger.info("Test passed: sort_by=%s, limit=%s", sort_by, limit)