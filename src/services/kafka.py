import json
from typing import Any

from faststream import FastStream
from faststream.kafka import KafkaBroker
from loguru import logger

from src.config import settings
from src.schemas import CarCreate, RoadConditionCreate, RoadCreate
from src.utils import Topics

broker = KafkaBroker(settings.KAFKA_BOOTSTRAP_SERVERS)

app = FastStream(broker)


async def publish_car_data(msg: CarCreate):
    await broker.publish(msg, topic=Topics.CAR.value)
    logger.info(f"Published car data: {msg}")


async def publish_road_condition_data(msg: RoadConditionCreate):
    await broker.publish(msg, topic=Topics.ROAD_CONDITION.value)
    logger.info(f"Published road condition data: {msg}")


async def publish_road_data(msg: RoadCreate):
    await broker.publish(msg, topic=Topics.ROAD.value)
    logger.info(f"Published road data: {msg}")


def serializer(value: Any) -> bytes:
    return json.dumps(value).encode()


def deserializer(serialized: bytes) -> Any:
    return json.loads(serialized)
