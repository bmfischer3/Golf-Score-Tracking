# Golf
# Goal 1 - Keep track of score for multiple players during a round of 18
# Milesstones - Keep track of score for one player, and ask for the course name and location. 
# Later on, keep this in a database. 

import time

class Player:
    def __init__(self, player_name, handicap):
        self.player_name = player_name
        self.handicap = handicap

class Round:
    def __init__(self, course_name, course_location, slope, yardage, hole_list):
        self.course_name = course_name
        self.course_location = course_location
        self.slope = slope
        self.yardage = yardage
        self.players = []
        self.hole_list = hole_list
        self.scorecard = {}

    def add_players(self, player_list):
        self.player_list = player_list
        for i in player_list:
            self.players.append(i)
            print(f"{i} has been successfully added to the round.")
        # Create scorekeeping dictionary
        self.scorecard.update({player: self.hole_list.copy() for player in player_list})
    
    def remove_player(self, player_name):
        if player_name in self.players:
            self.players.remove(player_name)
            del self.scorecard[player_name]
            print(f"{player_name} has been successfully removed from this round.")
            print(self.scorecard)
        else:
            print(f"{player_name} is not in this round.")
    
    def modify_score(self, player_name, hole_number, stroke_count):
        player_score = self.scorecard.get(player_name)
        if player_score is not None:
            player_score[hole_number] = stroke_count
        print(player_score)

    def start_round(self):
        print("The round is starting...")
        time.sleep(2)
        for i in self.scorecard:
            if any([True for k, v in self.scorecard.items() if v == 0]):
                score = input(f"What did {i} score for hole number {self.scorecard[1]}?  ")
                self.scorecard[1] = score
            else:
                print(f"All scores are up to date")


pebble_hole_list = {
    1:0,
    2:0
}

brian = Player("Brian", 15)
pebble = Round("Pebble Beach", "Del Monte, CA", 145.0, 6828, pebble_hole_list)

players = ["Brian", "Kyle", "Jack", "Robin"]

print(pebble.add_players(players))

# pebble.modify_score("Brian", 2, 4)
# pebble.modify_score("Robin", 2, 3)

print(pebble.scorecard)

pebble.start_round()

# 
