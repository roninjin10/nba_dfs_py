# -*- coding: utf-8 -*-
"""
Lineup Optimizer in Python
@author: William Cory
"""

import csv

class Player:

    def __init__(self, name=None, team=None, opp=None, position=(None, None), projection=None, salary=None, real_value = None, site_id = None):
        self.player_info = {}
        self.player_info['name'] = name
        self.player_info['team'] = team
        self.player_info['opp'] = opp
        self.player_info['position'] = position
        self.player_info['projection'] = projection
        self.player_info['salary'] = salary
        self.player_info['real_value'] = real_value
        self.player_info['site_id'] = site_id

    def copy_player(self):
        #returns an identical player
        new_player = Player
        new_player.player_info = self.player_info
        return new_player

    def change_player_info(self, info_dic):
        #info_dic is a dictionary containing some player_info
        for info in info_dic.keys:
            self.player_info[info] = info_dic[info]

    def get_info(self, info_to_get):
        return self.player_info[info_to_get]

    def set_info(self, info_to_set, info_value):
        self.player_info[info_to_set] = info_value


class Lineup:

    def __init__(self, salary_cap = 50000, pg = None, sg = None, sf = None, pf = None, c = None, g = None, f = None, flex = None):
        self.roster = {}
        self.roster['pg'] = pg
        self.roster['sg'] = sg
        self.roster['sf'] = sf
        self.roster['pf'] = pf
        self.roster['c'] = c
        self.roster['g'] = g
        self.roster['f'] = f
        self.roster['flex'] = flex
        self.salary_cap = salary_cap


    def player_list(self):
        return [self.roster['pg'], self.roster['sg'], self.roster['sf'], self.roster['pf'], self.roster['c'], self.roster['g'], self.roster['f'], self.roster['flex']]

    def player_dic(self):
        return self.roster

    def salary(self):
        return sum(plr.salary for plr in self.roster.items() if not plr is None)

    def points(self):
        return sum(plr.projection for plr in self.roster.items() if not plr is None)

    def create_key(self, current_position, current_player_num):
        return "Pos: " + current_position + " PlNum: " + current_player_num + " Sal: " + str(self.salary()) + " Positions: " + ''.join(pos for pos in self.roster.keys() if not self.roster[pos] is None)


    def merge_lineup(self, lineup):
        for pos in self.roster.keys():
            if self[pos] = None:
                self[pos] = lineup[pos]

    def erase_lineup(self):
        self.roster = {}

    def add_player(self, new_player, roster_spot=''):
        #adds a player to a lineup to a specified roster_spot. Overwrites player if roster_spot specified
        # If roster_spot is not given, it puts the player in the valid, empty roster spot that provides most future roster flexibility
        # method returns a boolean based on if the player was added or not
        if roster_spot != '':
            self.roster[roster_spot] = new_player
        else:
            position = new_player.get_info('position')
            #don't need this functionality atm


    def is_valid_salary(self):
        return self.salary() <= self.salary_cap

    def is_valid_team(self):
        team_opponent = []
        for position in self.roster.items():
            if team_opponent == []:
                team_opponent.append(position.get_info('team'))
                team_opponent.append(position.get_info('opp'))
            else:
                if not position.get_info('team') in team_opponent:
                    return True
        return False

    def is_valid_positional(self):
        #returns boolean based on if the lineup has every position filled
        for roster_spot in self.roster.items():
            if roster_spot is None:
                return False
        return True

    def is_valid(self):
        return self.is_valid_positional() and self.is_valid_salary() and self.is_valid_team()

    def copy_lineup(self):
        #returns a copy of the same lineup
        out = Lineup()
        out.roster = self.roster
        return out

class Player_Pool:

    def __init__(self, pool_list):
        __pool = pool_list
        __orig_pool = pool_dic

    def create_pool_from_csv(self, csv):
        #specifically creates a player pool from a standardized csv file.
        pass

    def create_positional_list(self, pos):
        #creates a list of players eligible for a specific position. PG, SG, SF, PF, C, G, F, Flex
        out = {}
        if pos == 'f':
            return [player for player in self.__pool if 'sf' in player.get_info('position') or 'pf' in player.get_info('position')]
        elif pos == 'g':
            return [player for player in self.__pool if 'pg' in player.get_info('position') or 'sg' in player.get_info('position')]
        else:
            return [player for player in self.__pool if pos in player.get_info('position')]

    def remove_player(self, player_name='', index=-1):
        #removes player from a list
        if index != -1:
            removed_player =__pool.pop(index)
        elif player_name != '':
            removed_player = __pool.pop(__pool.index(player_name))

    def pop_player(self, player_name='', index=-1):
        #removes player from a list and returns that player
        if index != -1:
            return __pool.pop(index)
        elif player_name != '':
            return __pool.pop(__pool.index(player_name))

    def add_player(self, player_name):
        #adds a player to the player_pool not necessary atm
        pass

    def restore_player_pool(self):
        self.__pool = self.__orig_pool

    def get_player_index(self, current_position, current_player_num):
        pass
        #gets the player index in __pool based on current position and player_num at position

def optimizer(player_pool, current_lineup, current_position, current_player_num):
    dic_key = current_lineup.create_key(current_position, current_player_num)
    if dic_key in memoize.keys():
        memoized_lineup = current_lineup.merge_lineup(memoize[dic_key])
        if memoized_lineup.is_valid:
            return memoized_lineup

    #likely have to check how many players are left at the position here
    lineup_if_pass = optimizer(player_pool, current_lineup.copy_lineup(), current_position, current_player_num + 1)

    #lineup if take must be eveluated after lineup if pass because the player pool gets altered when taking

    lineup_if_take = current_lineup.add_player(player_pool.pop_player(player_pool.get_player_index(current_position, current_player_num)))
    if not lineup_if_take.is_valid_salary:
        lineup_if_take = None
    else:
        lineup_if_take = optimizer(player_pool, lineup_if_take, current_position + 1, 0)

    if lineup_if_pass is None and lineup_if_take is None:
        return None
    elif lineup_if_pass is None:
        memoized[dic_key] = lineup_if_take
        return lineup_if_take
    elif lineup_if_take is None:
        memoized[dic_key] = lineup_if_pass
        return lineup_if_pass
    elif lineup_if_pass.points > lineup_if_take.points:
        memoized[dic_key] = lineup_if_pass
        return lineup_if_pass
    else: #if lineup_if_take.points >= lineup_if_pass.points
        memoized[dic_key] = lineup_if_take
        return lineup_if_take

if __name__ == "__main__":
    memoize = {}
    player_pool = PlayerPool()
    empty_lineup = Lineup
    #player_pool.create_pool_from_csv(get_csv(file_path)) #need a function to get a csv from a file path and the method to parse it
    optimal_lineup = optimizer(player_pool, empty_lineup, 0, 0)
    print(optimal_lineup.player_list(), optimal_lineup.points, optimal_lineup.salary)
        

"""
Pseudo code for optimizer

Main()
	*MinValue = Prompt for MinValue
	*New PlayerPoolObject
	*PlayerPoolObject.CreatePlayerPool(MinValue)
	New Lineup Object

	New DKLineupObject That is empty
	OptimalLineup = Optimizer(PlayerPoolObject, DkLineupObject, CurrentPosition="PG", CurrentPlayer = 1) OptimalLineup as DkLineupObject
	
	Call SetLineupsToLineup(OptimalLineup)
	


Optimizer(PlayerPoolObject, DKLineupObject, CurrentPosition, CurrentPlayer) As DKLIneupObject
	#Optimizer starts with Player 1 of position 1 (PG) and moves down teh positions/players 1 by 1 with each recursion
	Check to see if the key exists and if so Call the MergeLineup Method on the lineup associated with key
	
	New DKLIneupObject LineupIfPass that is equal to current lineup
	CalculatePlayersLeft at the position
	If no players left at the position set LineupIfPass = Nothing
	Else LineupifPass = Optimizer(SamePlayerPool, SameLineup, SamePosition, NextPlayer)
	
	New DKLIneupObject LineupIfTake 
	LineupIfTake = CurrentLineup.AddPlayerTolineup(player being considered now)
	Test LIneupifTake.IsValidSalary, set LUIfTake = nothing if it is not valid
	Else LineupIfTake = Optimizer(LineupIfTake, CurrentPlayerPool.RemoveFromPool(PlayerThatJustGotAdded), NextPosition, CurrentPlayer = 1)
	

	If LUIfTake and LUIFPass are both nothing then return Nothing
	ElseIf 1 of the lineups are nothing, return the lineup that isn't nothing
	Else Return the lineup that scored the most fantasy points and add the result to the dictionary.


	
SetLineupsToOptimalLineup(Lineup As DKLineupObject)
	Sets every cash lineup in teh csv to teh dkoptimal
	displays the lineup if successful
****************************Classes********************************************
Class PlayerClass
	Properties:
		Name
		Team
		Position(FD DK and FDrft)
		Projection(FD and DK and FDrft)
		Salary(FD and DK and Fdrft)
		RealValue(FD and DK and Fdrft)
		CSVCodes(FD and DK and FDrft)
	Methods
		CreatePlayer:
			Gets all the information for a player when given a name


Class DKLineupClass
	-Properties
		PG as a PlayerClass
		SG as a PlayerClass
		SF as a PlayerClass
		PF as a PlayerClass
		C as a PlayerClass
		G as a PlayerClass
		F as a PlayerClass
		Flex As A PlayerClass

	Methods:
		-Get Salary
		-Get FantasyPoints
		-Get DictionaryKey( PositionToConsider, PlayerTOConsider, PlayerPoolLeft)
			Create A Unique key based on the lineup and which players are being considered to be in the lineup
		-CreateDic
			Creates a dictionary with all the players currently in lineup.  Returns nothing if there are duplicate players
		-MergeLineup(LineupToMerge As DKLIneupClass) As Lineup
			for any position in the lineup that does not currently already have a player in it mergelineup puts the analogous player from LineupToMerge
		EraseLU
		AddPlayer(PlayerToAdd As PlayerClass, CurrentPosition as Long)
			Adds a player to a specific position
		IsValidSalary
			Returns boolean based on if a lineup satisfies SalaryCap
		IsValidTeam
			Returns a boolean based on if a lineup satisfies dks rules for number of players on 1 team and having players from more than 1 game
		IsValidPositional
			Returns a boolean based on if every position is filled and the player in the positions are valid
		
Class PlayerPoolClass
	Properties
		CurrentPool As dictionary
			A dictionary containing every PlayerObject currently in the playerpool
		OriginalPool As dictionary
			A dictionary containing every player in original PlayerPoiol

	Methods
		CreatePlayerPool(ValueThreshold As double)
			Creates the playerpool fromt eh projections based on a minimum RealValue threshold for being allowed in the pool
		CreatePosition(Position As String) As Dictionary
			Creates a dictionary containing all the players in teh CurrentPool of a specific position
		RemoveFromPool(PlayerName As String)
		AddToPool(playerName As String)
		RestorePlayerPool
			Restores playerpool to original


				
"""