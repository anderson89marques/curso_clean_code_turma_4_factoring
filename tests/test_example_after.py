from datetime import datetime

import pytest
from refactor.example_after import calculate_ride


def test_calcula_corrida_taxi_em_dias_comuns():
    # given
    distance = 1000
    day = datetime(2021, 12, 9, 13, 0, 0)

    # when
    ride_price = calculate_ride(distance, day)

    # then
    assert ride_price == 2100.0


def test_calcula_corrida_taxi_no_domingo():
    # given
    distance = 1000
    day = datetime(2021, 12, 5, 13, 0, 0)

    # when
    ride_price = calculate_ride(distance, day)

    # then
    assert ride_price == 2900.0


# def test_calcula_corrida_taxi_a_noite():
#     # given
#     distance = 1000
#     day = datetime(2021, 12, 9, 23, 0, 0)

#     # when
#     ride_price = calculate_ride(distance, day)

#     # then
#     assert ride_price == 3900.0


def test_calcula_corrida_taxi_distancia_como_string():
    # given
    distance = "1000"
    day = datetime(2021, 12, 9, 23, 0, 0)

    # when
    with pytest.raises(Exception, match=r'Invalid distance parameter') as err:
        calculate_ride(distance, day)


def test_calcula_corrida_taxi_distancia_menor_que_zero():
    # given
    distance = -1000
    day = datetime(2021, 12, 9, 23, 0, 0)

    # when
    with pytest.raises(Exception, match=r'Invalid distance parameter') as err:
        calculate_ride(distance, day)


# def test_calcula_corrida_taxi_data_invalida():
#     # given
#     distance = 1000
#     day = "datetime(2021, 12, 9, 23, 0, 0)"

#     # when/then
#     with pytest.raises(Exception, match=r'Invalid day parameter') as err:
#         calculate_ride(distance, day)
