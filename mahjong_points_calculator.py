
players = []
points = {0:0.1, 1:0.2, 2:0.4, 3:0.8, 4:1.6, 5:3.2}
records = []
balances = []

class Player:
    def __init__(self, username, balance):
        self.username = username
        self.balance = round(balance, 2)
    def display_player(self):
        print(f"player:{self.username} balance:{self.balance}")
    def format_data(self):
        return f"{self.username},{self.balance}\n"

class Record:
    def __init__(self, record_id, winner, points, loser):
        self.record_id = record_id
        self.winner = winner
        self.points = points
        self.loser = loser
    def display_record(self):
        print(f"record id:{self.record_id} winner:{self.winner.username} points:{self.points} loser:{self.loser.username if self.winner.username != self.loser.username else None}")
    def format_data(self):
        return f"{self.record_id},{self.winner.username},{self.points},{self.loser.username}\n"

def load_players_data():
    try:
        with open("players.csv", "x+") as players_data:
            file_content = players_data.read()
            lines = file_content.splitlines()
            for line in lines:
                player_data = line.split(",")
                username = player_data[0]
                balance = float(player_data[1])
                loaded_player = Player(username, balance)
                players.append(loaded_player)
    except FileExistsError:
        try:
            with open("players.csv", "r+") as players_data:
                file_content = players_data.read()
                lines = file_content.splitlines()
                for line in lines:
                    player_data = line.split(",")
                    username = player_data[0]
                    balance = float(player_data[1])
                    loaded_player = Player(username, balance)
                    players.append(loaded_player)
        except Exception as e:
            print(e)
    except Exception as e2:
        print(e2)


def load_records_data():
    try:
        with open("records.csv", "x+") as records_data:
            file_content = records_data.read()
            lines = file_content.splitlines()
            for line in lines:
                record_data = line.split(",")
                record_id = record_data[0]
                winner = None
                winner_username = record_data[1]
                for i in players:
                    if i.username == winner_username:
                        winner = i
                points = int(record_data[2])
                loser = None
                loser_username = record_data[3]
                for i in players:
                    if i.username == loser_username:
                        loser = i
                loaded_record = Record(record_id, winner, points, loser)
                records.append(loaded_record)
    except FileExistsError:
        try:
            with open("records.csv", "r+") as records_data:
                file_content = records_data.read()
                lines = file_content.splitlines()
                for line in lines:
                    record_data = line.split(",")
                    record_id = record_data[0]
                    winner = None
                    winner_username = record_data[1]
                    for i in players:
                        if i.username == winner_username:
                            winner = i
                    points = int(record_data[2])
                    loser = None
                    loser_username = record_data[3]
                    for i in players:
                        if i.username == loser_username:
                            loser = i
                    loaded_record = Record(record_id, winner, points, loser)
                    records.append(loaded_record)
        except Exception as e:
            print(e)
    except Exception as e2:
        print(e2)

def load_balances_data():
    try:
        with open("balances.csv", "x+") as balances_data:
            file_content = balances_data.read()
            lines = file_content.splitlines()
            for line in lines:
                balances.append(line)
    except FileExistsError:
        try:
            with open("balances.csv", "r+") as balances_data:
                file_content = balances_data.read()
                lines = file_content.splitlines()
                for line in lines:
                    balances.append(line)
        except Exception as e:
            print(e)
    except Exception as e2:
        print(e2)

load_players_data()
load_records_data()
load_balances_data()

def create_new_record():
    record_id = None
    if len(records) == 0:
        record_id = str(0).zfill(5)
    else:
        record_id = str(int(records[-1].record_id) + 1).zfill(5)
    input_winner = input("Who won?: ")
    winner_points = input("By how many points?: ")
    try:
        winner_points = int(winner_points)
        if winner_points not in range(0,6): 
            return print("Invalid input")
    except Exception as e:
        print(f"Invalid input! {e}")
        return
    input_loser = input("Whose tile got them the win?: ")
    found_loser = None
    found_winner = None
    for loser in players:
        if loser.username == input_loser:
            found_loser = loser
    if found_loser == None: 
        print("Winner user not found")
        return
    for winner in players:
        if winner.username == input_winner:
            found_winner = winner
    if found_winner == None: 
        print("Loser user not found")
        return
    if found_loser.username != found_winner.username:
        found_winner.balance += round(points[winner_points] * 2, 2)
        found_loser.balance -= round(points[winner_points] * 2, 2)
        for player in players:
            if player.username != found_winner.username and player.username != found_loser.username:
                found_winner.balance += round(points[winner_points], 2)
                player.balance -= round(points[winner_points], 2)
    else:
        for player in players:
            if player.username != found_winner.username:
                found_winner.balance += round(points[winner_points] * 2, 2)
                player.balance -= round(points[winner_points] * 2, 2)
    new_record = Record(record_id, found_winner, winner_points, found_loser)
    records.append(new_record)
    print(f"winner:{found_winner.username} points:{winner_points} loser:{found_loser.username if found_loser.username != found_winner.username else None}")
    new_balance = ""
    for i in players:
        i.display_player()
        new_balance += f"{i.username}:{round(i.balance,2)} "
    balances.append(new_balance)

def display_records():
    for i in records:
        i.display_record()

def save_players_data():
    with open("players.csv", "w") as players_data:
        for i in players:
            players_data.write(i.format_data())

def save_records_data():
    with open("records.csv", "w") as records_data:
        for i in records:
           records_data.write(i.format_data())

def save_balances_data():
    with open("balances.csv", "w") as balances_data:
        for i in balances:
           balances_data.write(i + "\n")

def main_menu():
    while True:
        print("""
    Mahjong Points Calculator
    ==============================
    [1] Add New Record
    [2] Display All Records
    [3] Delete a Record
    [4] Edit a Record
    [0] Exit Program
    ==============================
    """)
        user_input = input("Choose an option: ")
        try:
            user_input = int(user_input)
            if user_input not in range(0,5):
                raise ValueError
        except ValueError:
            print("Invalid input")
        else:
            if user_input == 0:
                print("Saving data...")
                save_players_data()
                save_records_data()
                save_balances_data()
                print("Ending program.")
                exit()
            if user_input == 1:
                create_new_record()
            if user_input == 2:
                display_records()

if __name__ == "__main__":
    main_menu()