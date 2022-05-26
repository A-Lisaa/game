import attr


@attr.define
class Quest:
    name: str
    objectives: dict[int, str]
    completed: dict[int, str] = {}
    failed: dict[int, str] = {}
    time_for_quest: int = 0

    def __attrs_post_init__(self):
        self.time = 0


if __name__ == "__main__":
    quest1 = Quest("Quest 1", {11: "Talk to your dad", 12: "Help him", 13: ""})
