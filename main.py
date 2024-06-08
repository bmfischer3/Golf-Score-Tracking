# Golf
# Functions
# 1 - Keep track of the scores for up to 4 players in a database by date and course.  
# 2 - Based on those scores, run functions to determine who's the winner of various games. 
# 2A - Give updates on the extra games to determine standings and what needs to be done by each individual party to win. 
# 3 - Incorporate scorecard API to pull in course data, pars, etc. https://golfbert.com/api/tutorial 
# 4 - 



# import psycopg2
# from config import load_config
import time

class Player:
    def __init__(self, player_name, handicap):
        self.player_name = player_name
        self.handicap = handicap

class Round:
    STARTING_SCORES = {
            1:0,
            2:0,
            3:0,
            4:0,
            5:0,
            6:0,
            7:0,
            8:0,
            9:0,
            10:0,
            11:0,
            12:0,
            13:0,
            14:0,
            15:0,
            16:0,
            17:0,
            18:0
        }
    
    FRONT_BACK_FULL_TOTALS = {
        'front9_total': 0,
        'back9_total': 0,
        'full18_total': 0
        }
    
    def __init__(self, course_name, course_location, slope, yardage, hole_list):
        self.course_name = course_name
        self.course_location = course_location
        self.slope = slope
        self.yardage = yardage
        self.players = []
        self.hole_list = hole_list
        self.scorecard = {}
        self.round_totals = {}
        self._title = ""
 
    def start_round(self) -> None:
        """Initiates the a round. 
    
        """
        # Asks for number of players and their names. 
        num_players = int(input("Enter the number of players: "))
        starting_list = []
        for i in range(0, num_players):
            counter = int(i+1)
            ele = str(input(f"Please provide the name of player {counter}: "))
            starting_list.append(ele)
        self.add_players(starting_list)

       # Loops through the dictionary created for those players and updates with inputs. 
        for hole_number in range(1, 19):
            for player_name in self.players:
                if hole_number > 18:
                    break
                else:
                    stroke_count = int(input(f"Enter strokes for {player_name} on hole {hole_number}: "))
                    self.modify_score(player_name, hole_number, stroke_count)
        
        # Provides the results of the round. 
        
        self.get_round_totals()
    
    def get_all_totals(self) -> dict:
        """Get totals of all players in 

        Returns:
            dict: ex
            {
                "brye": 69
            } 
        """
        return NotImplementedError
    
    @property
    def title(self) -> None:
        """set current total
        """
        return self._title
    
    @title.setter
    def set_title(self, name: str):
        self._title = name.strip("The ")

    def add_players(self, player_list):
        """ Adds a list of players to the round. 

        player_list = ['John', 'James', 'Jane']

        Args:
            player_list (list): list of players. 
        """
        self.player_list = player_list
        for i in player_list:
            self.players.append(i)
            print(f"{i} has been successfully added to the round.")
        # Create scorekeeping dictionary
        self.scorecard.update({player: Round.STARTING_SCORES.copy() for player in player_list})


    def get_round_totals(self):    
        self.round_totals.update({player: Round.FRONT_BACK_FULL_TOTALS.copy() for player in self.player_list})
        print(self.round_totals)
        for player_name, scores in self.scorecard.items():
            self.round_totals['front9_total'] = sum(list(scores.values())[:9])
            self.round_totals['back9_total'] = sum(list(scores.values())[10:18])
            self.round_totals['full18_total'] = self.round_totals['front9_total'] + self.round_totals['back9_total']
            print(f"{player_name}'s front 9 total is {self.round_totals['front9_total']}.")
            print(f"{player_name}'s back 9 total is {self.round_totals['back9_total']}.")
            print(f"{player_name}'s 18 hole total is {self.round_totals['full18_total']}")

    
    def remove_player(self, player_name):
        if player_name in self.players:
            self.players.remove(player_name)
            del self.scorecard[player_name]
            print(f"{player_name} has been successfully removed from this round.")
            print(self.scorecard)
        else:
            print(f"{player_name} is not in this round.")
    
    def modify_score(self, player_name, hole_number, stroke_count):
        """Updates score for a specific player and hole number. 

        Args:
            player_name (string): player_name that is in players list. 
            hole_number (int): hole number
            stroke_count (int): number of strokes for hole
        """
        player_score = self.scorecard.get(player_name)
        if player_score is not None:
            player_score[hole_number] = stroke_count

    def get_indv_score(self):
        name = input("What is the player's name you are requesting: ")
        hole = input("What is the hole number you are requesting? \n Valid responses are: Front 9, Back 9, All: ")

        if name in players:
            if hole == 'Front 9':
                for k, v in self.scorecard.items():
                    if k < 10:
                        print(k, v)
                pass
            elif hole == 'Back 9':
                # return back 9 scorecard
                pass
            elif hole == 'All': 
                # return entire scorecard:
                pass
            else:
                print(f"{hole} is not a valid response")
        else:
            print(f"{name} is not a player in this round, please check the spelling on the name you submitted")

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
        starting_hole_num = int(input(f"What hole number are you updating?"))
        for name, scorecard in self.scorecard.items():
            for hole_num, score in scorecard.items():
                hole_key = (list(scorecard)[0] + starting_hole_num - 1)
                if hole_num == hole_key:
                    strokes = input(f"What did {name} score for hole number {hole_num}: ")
                    self.modify_score(name, hole_num, strokes)
                    print(f"{name}'s score for hole #{hole_num} has been updated to {strokes}.")

    def submit_round(self):
        for name, scorecard in self.scorecard.items():
            scorecard_values = scorecard.values()
            if 0 in scorecard_values:
                print(f"There are still 0s in {name}'s the scorecard, please review.")
                # start function to fix scorecards. Will insert this later. 
            else:
                print(f"{name}'s scorecard is complete and you are ready to submit.")
                # start uplading scorecard here. 
                print(f"{name}'s scorecard is being uploaded...")
                # course_name = self.course_name

                # sql = """INSERT INTO golf_scores """
                # conn = psycopg2.connect(dsn)
                # cur = conn.cursor()




                
        # Check that all holes have been completed by all parties, if not, go back through and add those scores to the state. 
        # Determine what the date is for this round. 
        # Submit the scores to the database as if they were all logged individually. 
        # Data will need to be manipulated nad parsed so it will correclty enter the database. 




pebble_hole_list = {
    1:4,
    2:5,
    3:4,
    4:4,
    5:3,
    6:5,
    7:3,
    8:4,
    9:4,
    10:4,
    11:4,
    12:3,
    13:4,
    14:5,
    15:4,
    16:4,
    17:3,
    18:5
    }

brian = Player("Brian", 15)
pebble = Round("Pebble Beach", "Del Monte, CA", 145.0, 6828, pebble_hole_list)

players = ["Brian", "Kyle", "Jack", "Robin"]

# print(pebble.add_players(players))

# pebble.modify_score("Brian", 2, 5)
# pebble.modify_score("Robin", 2, 3)

# print(pebble.scorecard)

# pebble.get_all_totals()

pebble.start_round()

# pebble.get_round_totals()
