# data.py is a fake data source, defining an instance of a model
from model import Creature


__creatures: list[Creature] = [
    Creature(name='yeti',
             description="Abominable Snowman",
             location="Himalayas"),
    Creature(name='sasquatch',
             description="Bigfoot",
             location="North America")]

# print("Name is", __creatures[1].name)


def get_creatures() -> list[Creature]:
    return __creatures
