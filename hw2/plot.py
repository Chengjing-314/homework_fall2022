import seaborn as sns 
import json 
import pandas as pd
import matplotlib.pyplot as plt

def plot_q1_sb():
    with open('run_data/q1_sb_no_rtg_dsa_CartPole-v0_07-04-2023_21-17-59.json', 'r') as no_rtg_dsa, \
         open('run_data/q1_sb_rtg_dsa_CartPole-v0_07-04-2023_21-27-02.json', 'r') as rtg_dsa, \
         open ('run_data/q1_sb_rtg_na_CartPole-v0_07-04-2023_21-32-34.json', 'r') as rtg_na:
        n_rtg_dsa = json.load(no_rtg_dsa)
        y_rtg_dsa = json.load(rtg_dsa)
        a_rtg_na = json.load(rtg_na)
        
        n_rtg_dsa = [i[2] for i in n_rtg_dsa]
        y_rtg_dsa = [i[2] for i in y_rtg_dsa]
        a_rtg_na = [i[2] for i in a_rtg_na]
        
        num_iteration = len(n_rtg_dsa)
        
        prprocess_df = pd.DataFrame({'No RTG DSA': n_rtg_dsa, 'RTG DSA': y_rtg_dsa, 'RTG NA': a_rtg_na, 'Iteration': range(num_iteration)})
        
        sns.set_theme('paper')
        
        out_plt = sns.lineplot(data=pd.melt(prprocess_df, ['Iteration']), x='Iteration', y='value', hue = 'variable')
        out_plt.get_legend().set_title('Experiment')
        out_plt.set_title('Q1: CartPole-v0 Average Return Small Batch')
        out_plt.legend(loc='center right')
        out_plt.set(xlabel='Iteration', ylabel='Average Return')
        
        plt.show()
        
        


plot_q1_sb()


        