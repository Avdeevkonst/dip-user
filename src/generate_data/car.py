import random

from src.main import broker
from src.schemas import CarCreate
from src.utils import Topics


@broker.publisher(topic=Topics.CAR.value)
async def publish():
    pass


"""
plate_number = Letter + Figure + Figure + Figure + Letter + Letter + Figure + Figure
"""


def generate_car_payload():
    body = {
        "plate_number": generate_plate_number(),
        "model": random.choice(["BMW", "Mercedes-Benz", "Lada", "Toyota"]),
        "avarage_speed": random.randint(0, 50),
        "latitude": random.uniform(-90.0, 90.0),
        "longitude": random.uniform(-90.0, 90.0),
    }
    return CarCreate(**body)


def generate_plate_number() -> str:
    return (
        random.choice("АВЕКМНОРСТУХ")
        + "".join(random.choices("0123456789", k=3))
        + "".join(random.choices("АВЕКМНОРСТУХ", k=2))
        + "".join(random.choices("0123456789", k=2))
    )
