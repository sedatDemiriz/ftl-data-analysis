import matplotlib.pyplot as plt
import random as rd
import pandas as pd
import numpy as np
import sys

# Function to simulate a winstreak
def simulate_streak(odds):
    
    # Start at streak 0, no ships done
    result = 1
    streak = 0
    ships_done = []
    
    # While on a streak
    while result:
        
        # If looping after 28 ships
        if len(ships_done) == 28:
            ships_done = []
            
        # Roll random ship
        rnd_ship = rd.randint(0, 27)
        
        # If ship not done yet
        if rnd_ship not in ships_done:
            
            # Get probability of winning for ship
            win_prob = odds[rnd_ship]
            lose_prob = 1-win_prob
            
            # Roll win or loss
            result *= np.random.choice(a = [0, 1], p = [lose_prob, win_prob])
            
            # If win, increment streak, mark ship as done
            if result:
                streak += 1
                ships_done.append(rnd_ship)                
    
    # Print results
    #print("Streak length: " + str(streak))
    #print("Streak ended on ship: " + str(rnd_ship))
    
    return(streak, rnd_ship)

# Function for simulating num streaks
def run_streaks(odds, num):
    streak_lengths = []
    i = 0

    # Run streak num times
    while i < num:
        streak_lengths.append(simulate_streak(odds)[0])
        i += 1
    
    return streak_lengths

def main():

    # Parse and format input data
    input_data = pd.read_csv(str(sys.argv[1]))
    input_data['ship'] = ["Kestrel A", "Kestrel B", "Kestrel C", "Engi A", "Engi B", "Engi C", "Federation A", "Federation B", "Federation C", "Zoltan A", "Zoltan B", "Zoltan C", "Stealth A", "Stealth B", "Stealth C", "Rock A", "Rock B", "Rock C", "Slug A", "Slug B", "Slug C", "Mantis A", "Mantis B", "Mantis C", "Crystal A", "Crystal B", "Lanius A", "Lanius B"]
    input_data = input_data[['ship', 'wins', 'losses']]
    input_data['ratio'] = input_data['wins'] / (input_data['wins'] + input_data['losses'])

    # Create sorted ship winrate barplot
    ship_win_ratios = input_data.sort_values('ratio', ascending=False)
    plt.figure(0)
    plt.bar(ship_win_ratios.ship, ship_win_ratios.ratio)
    plt.xticks(rotation = 90)
    plt.savefig('./images/ship_winrates.png')

    # Create streak length plot based on input for number of runs
    all_streaks = run_streaks(input_data.ratio, int(sys.argv[2]))
    plt.figure(1)
    plt.hist(all_streaks, bins = range(1, max(all_streaks)));
    plt.xlabel('Streak length')
    plt.ylabel('Amount of streaks of given length')
    plt.title('Streak Lengths')
    plt.savefig('./images/streak_lengths.png')


if __name__ == '__main__':
    main()