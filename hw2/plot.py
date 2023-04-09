import seaborn as sns 
import json 
import pandas as pd
import matplotlib.pyplot as plt

def plot_q1_sb():
    with open('data/q1_json/q2_pg_q1_sb_no_rtg_dsa_CartPole-v0_07-04-2023_21-37-49.json', 'r') as no_rtg_dsa, \
         open('data/q1_json/q2_pg_q1_sb_rtg_dsa_CartPole-v0_07-04-2023_21-39-09.json', 'r') as rtg_dsa, \
         open ('data/q1_json/q2_pg_q1_sb_rtg_na_CartPole-v0_07-04-2023_21-42-32.json', 'r') as rtg_na:
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
        

def plot_q1_lb():
    with open('data/q1_json/q2_pg_q1_lb_no_rtg_dsa_CartPole-v0_07-04-2023_21-48-17.json', 'r') as no_rtg_dsa, \
            open('data/q1_json/q2_pg_q1_lb_rtg_dsa_CartPole-v0_07-04-2023_21-52-34.json', 'r') as rtg_dsa, \
            open('data/q1_json/q2_pg_q1_lb_rtg_na_CartPole-v0_07-04-2023_21-44-32.json', 'r') as rtg_na:
        n_rtg_dsa = json.load(no_rtg_dsa)
        y_rtg_dsa = json.load(rtg_dsa)
        a_rtg_na = json.load(rtg_na)

        n_rtg_dsa = [i[2] for i in n_rtg_dsa]
        y_rtg_dsa = [i[2] for i in y_rtg_dsa]
        a_rtg_na = [i[2] for i in a_rtg_na]

        num_iteration = len(n_rtg_dsa)

        preprocess_df = pd.DataFrame(
            {'No RTG DSA': n_rtg_dsa, 'RTG DSA': y_rtg_dsa, 'RTG NA': a_rtg_na, 'Iteration': range(num_iteration)})

        sns.set_theme('paper')

        out_plt = sns.lineplot(data=pd.melt(
            preprocess_df, ['Iteration']), x='Iteration', y='value', hue='variable')
        out_plt.get_legend().set_title('Experiment')
        out_plt.set_title('Q1: CartPole-v0 Average Return Large Batch')
        out_plt.legend(loc='center right')
        out_plt.set(xlabel='Iteration', ylabel='Average Return')

        plt.show()

def plot_q2():
    with open('data/q2_json/q2_b1000_r5e-2_InvertedPendulum-v4_08-04-2023_08-47-27.json', 'r') as b1000_r005, \
         open('data/q2_json/q2_b1000_r5e-3_InvertedPendulum-v4_08-04-2023_09-01-40.json', 'r') as b1000_r0005, \
         open('data/q2_json/q2_b100_r5e-1_InvertedPendulum-v4_08-04-2023_08-54-12.json') as b100_r05, \
         open('data/q2_json/q2_b300_r5e-2_InvertedPendulum-v4_08-04-2023_08-56-24.json', 'r') as b300_r005, \
         open('data/q2_json/q2_b500_r5e-3_InvertedPendulum-v4_08-04-2023_08-57-48.json', 'r') as b500_r0005:
             
        b1000_r005 = json.load(b1000_r005)
        b1000_r0005 = json.load(b1000_r0005)
        b100_r05 = json.load(b100_r05)
        b300_r005 = json.load(b300_r005)
        b500_r0005 = json.load(b500_r0005)
        
        num_iteration = len(b1000_r005)
        
        preprocess_df = pd.DataFrame({'b1000_r005': [i[2] for i in b1000_r005], 'b1000_r0005': [i[2] for i in b1000_r0005], 
                                      'b100_r05': [i[2] for i in b100_r05], 'b300_r005': [i[2] for i in b300_r005], 
                                      'b500_r0005': [i[2] for i in b500_r0005], 'Iteration': range(num_iteration)})
        
        sns.set_theme('paper')
        out_plt = sns.lineplot(data=pd.melt(
            preprocess_df, ['Iteration']), x='Iteration', y='value', hue='variable')
        out_plt.get_legend().set_title('Experiment')
        out_plt.set_title('Q2: InvertPendulum-v4 Average Return Learning Curve')
        out_plt.legend(loc='center left')
        out_plt.set(xlabel='Iteration', ylabel='Average Return')
        
        plt.show()
        
def plot_q3():
    with open('data/q3_json/q3_b40000_r0.005_LunarLanderContinuous-v2_08-04-2023_21-42-27.json', 'r') as b40000_r005:
        
        b40000_r005 = json.load(b40000_r005)
        
        num_iteration = len(b40000_r005)
        
        preprocess_df = pd.DataFrame({'b40000_r005': [i[2] for i in b40000_r005], 'Iteration': range(num_iteration)})
        
        sns.set_theme('paper')
        
        out_plt = sns.lineplot(data=pd.melt(
            preprocess_df, ['Iteration']), x='Iteration', y='value', hue='variable')
        out_plt.get_legend().set_title('Experiment')
        out_plt.set_title(
            'Q3: LunarLanderContinuous-v2 Average Return Learning Curve')
        out_plt.legend(loc='lower right')
        out_plt.set(xlabel='Iteration', ylabel='Average Return')
        
        plt.show()
        
def plot_q5():
    with open('data/q5_json/q5_b2000_r0.001_lambda0.95_Hopper-v4_09-04-2023_08-24-01.json','r') as lambda095, \
         open('data/q5_json/q5_b2000_r0.001_lambda0.99_Hopper-v4_09-04-2023_08-56-51.json','r') as lambda099, \
         open('data/q5_json/q5_b2000_r0.001_lambda0_Hopper-v4_09-04-2023_08-43-21.json','r') as lambda0, \
         open('data/q5_json/q5_b2000_r0.001_lambda1_Hopper-v4_09-04-2023_09-14-55.json', 'r') as lambda1:
             
        lambda095 = json.load(lambda095)
        lambda099 = json.load(lambda099)
        lambda0 = json.load(lambda0)
        lambda1 = json.load(lambda1)
        
        num_iteration = len(lambda095)
        
        preprocess_df = pd.DataFrame({'lambda095': [i[2] for i in lambda095], 'lambda099': [i[2] for i in lambda099],
                                      'lambda0': [i[2] for i in lambda0], 'lambda1': [i[2] for i in lambda1], 'Iteration': range(num_iteration)})
        
        sns.set_theme('paper')
        
        out_plt = sns.lineplot(data=pd.melt(
            preprocess_df, ['Iteration']), x='Iteration', y='value', hue='variable')
        out_plt.get_legend().set_title('Experiment')
        out_plt.set_title(
            'Q4: HopperV4 Average Return Learning Curve')
        out_plt.legend(loc='upper left')
        out_plt.set(xlabel='Iteration', ylabel='Average Return')
        
        plt.show()
                                      
        
        

def smoothing(data, exp = 0.9):
    smoothed_data = []
    for i in range(len(data)):
        if i == 0:
            smoothed_data.append(data[i])
        else:
            smoothed_data.append(exp * smoothed_data[i-1] + (1 - exp) * data[i])
    return smoothed_data


plot_q5()


        