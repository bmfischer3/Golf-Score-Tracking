# Golf
# Functions
# 1 - Keep track of the scores for up to 4 players in a database by date and course.  
# 2 - Based on those scores, run functions to determine who's the winner of various games. 
# 2A - Give updates on the extra games to determine standings and what needs to be done by each individual party to win. 
# 3 - Incorporate scorecard API to pull in course data, pars, etc. https://golfbert.com/api/tutorial 
# 4 - 




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


    def get_nth_hole(self, n=0):
        if n < 0:
            n += len(self.hole_list)
        for i, key in enumerate(self.hole_list.keys()):
            if i == n:
                return key
        raise IndexError("Hole index out of range.")

    def complete_hole(self):
        print("The round is starting...")
        time.sleep(2)
        starting_hole_num = int(input(f"What hole number are you starting on? "))
        for name, scorecard in self.scorecard.items():
            for hole_num, score in scorecard.items():
                hole_key = (list(scorecard)[0] + starting_hole_num - 1)
                if hole_num == hole_key:
                    strokes = input(f"What did {name} score for hole number {hole_num}: ")
                    self.modify_score(name, hole_num, strokes)
                    print(f"{name}'s score for hole #{hole_num} has been updated to {strokes}.")



pebble_hole_list = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0
}

brian = Player("Brian", 15)
pebble = Round("Pebble Beach", "Del Monte, CA", 145.0, 6828, pebble_hole_list)

players = ["Brian", "Kyle", "Jack", "Robin"]

print(pebble.add_players(players))

# pebble.modify_score("Brian", 2, 4)
# pebble.modify_score("Robin", 2, 3)

print(pebble.scorecard)
pebble.complete_hole()

# 
