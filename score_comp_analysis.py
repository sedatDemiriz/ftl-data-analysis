import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

def gen_plots(input_table):

    # Prepare for 4 subplots side by side
    fig, ax = plt.subplots(1,4)
    fig.set_figwidth(40)
    
    # Set plot titles in order
    plot_titles = ['Avg. Score', 'Avg. Scrap', 'Avg. Jumps', 'Avg. Kills']

    # For each stat, make a plot
    for i in range(4):

        # Column to plot for the iteration
        col2plot = input_table.columns[i+1]
        
        # Sort input for nicer graph
        input_table = input_table.sort_values(col2plot, ascending = False)

        # Plot the data column, rotate labels and average line
        ax[i].bar(input_table['ship'], input_table[col2plot])
        ax[i].tick_params(rotation = 90)
        ax[i].title.set_text(plot_titles[i])
        ax[i].axhline(input_table[col2plot].mean(), color='orange', linestyle='--')

    # Save figure at high quality, proper bordering
    plt.savefig("./images/all_stats.png", dpi=500, bbox_inches='tight')

def main():

    # Read in the file, order columns, apply capitalization to ship names
    input_components = pd.read_csv(sys.argv[1])
    input_components = input_components[['ship', 'score', 'scrap', 'jumps', 'kills']]
    input_components['ship'] = input_components['ship'].str.title()

    # Average each ship's stats, reset index for easy access
    input_avgs = input_components.groupby(by='ship').agg('mean').reset_index()
    gen_plots(input_avgs)

if __name__ == "__main__":
    main()