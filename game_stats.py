class GameStats():

    def __init__(self):
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.score = 0
        self.level = 1
        self.record = self.record_loader()
        self.bonus = 0
        self.min_speed = 1
        self.max_speed = 5

    def record_loader(self):
        try:
            with open("record.txt", "r") as file:
                record = int(file.read())
            return record
        except FileNotFoundError:
            print("Record file not found. Creating a new one.")
            with open("record.txt", "w") as file:
                file.write("0")  # Initialize with a default record of 0
            return 0
        except ValueError:
            print("Error: Invalid record file content. Resetting to 0.")
            with open("record.txt", "w") as file:
                file.write("0")
            return 0

    def record_saver(self, new_record):
        if new_record > self.record:
            self.record = new_record
            with open("record.txt", "w") as file:
                file.write(str(new_record))