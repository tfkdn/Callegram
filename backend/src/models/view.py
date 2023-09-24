class Schedule:

    def __init__(self, user_id: int, windows: list[list[int]]):
        self.user_id = user_id
        self.windows = windows


class User:

    def __init__(self, id: int, name: str, timezone: int, notification_time: list[int], schedule: Schedule = None):
        self.id = id
        self.name = name
        self.timezone = timezone
        self.notification_time = notification_time
        self.schedule = schedule
