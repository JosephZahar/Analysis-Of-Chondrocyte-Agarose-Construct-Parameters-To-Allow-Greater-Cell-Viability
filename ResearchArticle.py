import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import researchpy as rp
import scipy.stats as stats

Group_A_df = pd.read_excel(r'/Users/macbookpro/Desktop/MAT311 - Tissue Engineering and Regenerative Medicine - 2020:21/'
                           r'Coursework 1 (marking  criteria)-20201114/Data_Group A.xlsx')

Group_A_4_D0 = pd.read_excel(r'/Users/macbookpro/Desktop/MAT311 - Tissue Engineering and Regenerative Medicine - '
                             r'2020:21/Coursework 1 (marking  criteria)-20201114/Data_Group A.xlsx',
                             sheet_name='4% Day 0 Grp A')

Group_A_4_D7 = pd.read_excel(r'/Users/macbookpro/Desktop/MAT311 - Tissue Engineering and Regenerative Medicine - '
                             r'2020:21/Coursework 1 (marking  criteria)-20201114/Data_Group A.xlsx',
                             sheet_name='4% Day7 Grp A')

Group_A_6_D0 = pd.read_excel(r'/Users/macbookpro/Desktop/MAT311 - Tissue Engineering and Regenerative Medicine - '
                             r'2020:21/Coursework 1 (marking  criteria)-20201114/Data_Group A.xlsx',
                             sheet_name='6% Day 0 Grp A')

Group_A_6_D7 = pd.read_excel(r'/Users/macbookpro/Desktop/MAT311 - Tissue Engineering and Regenerative Medicine - '
                             r'2020:21/Coursework 1 (marking  criteria)-20201114/Data_Group A.xlsx',
                             sheet_name='6% Day 7 Grp A')

r = 2.5
cross_sectional_area = math.pi * (r ** 2)
length = 5

# Lets start with the Data of Grp A for 4% at Day 0

Group_A_4_D0 = Group_A_4_D0.assign(Stress1=(Group_A_4_D0['Load 1'] / cross_sectional_area) * (10 ** 6),
                                   Stress2=(Group_A_4_D0['Load 2'] / cross_sectional_area) * (10 ** 6),
                                   Stress3=(Group_A_4_D0['Load 3'] / cross_sectional_area) * (10 ** 6),
                                   Stress4=(Group_A_4_D0['Load 4'] / cross_sectional_area) * (10 ** 6),
                                   Stress5=(Group_A_4_D0['Load 5'] / cross_sectional_area) * (10 ** 6))

Group_A_4_D0 = Group_A_4_D0.assign(Strain1=(Group_A_4_D0['Extension 1'] / length) * 100,
                                   Strain2=(Group_A_4_D0['Extension 2'] / length) * 100,
                                   Strain3=(Group_A_4_D0['Extension 3'] / length) * 100,
                                   Strain4=(Group_A_4_D0['Extension 4'] / length) * 100,
                                   Strain5=(Group_A_4_D0['Extension 5'] / length) * 100)

# Lets continue with the Data of Grp A for 4% at Day 7

Group_A_4_D7 = Group_A_4_D7.assign(Stress1=(Group_A_4_D7['Load 1'] / cross_sectional_area) * (10 ** 6),
                                   Stress2=(Group_A_4_D7['Load 2'] / cross_sectional_area) * (10 ** 6),
                                   Stress3=(Group_A_4_D7['Load 3'] / cross_sectional_area) * (10 ** 6),
                                   Stress4=(Group_A_4_D7['Load 4'] / cross_sectional_area) * (10 ** 6),
                                   Stress5=(Group_A_4_D7['Load 5'] / cross_sectional_area) * (10 ** 6))

Group_A_4_D7 = Group_A_4_D7.assign(Strain1=(Group_A_4_D7['Extension 1'] / length) * 100,
                                   Strain2=(Group_A_4_D7['Extension 2'] / length) * 100,
                                   Strain3=(Group_A_4_D7['Extension 3'] / length) * 100,
                                   Strain4=(Group_A_4_D7['Extension 4'] / length) * 100,
                                   Strain5=(Group_A_4_D7['Extension 5'] / length) * 100)

# Lets continue with the Data of Grp A for 6% at Day 0

Group_A_6_D0 = Group_A_6_D0.assign(Stress1=(Group_A_6_D0['Load 1'] / cross_sectional_area) * (10 ** 6),
                                   Stress2=(Group_A_6_D0['Load 2'] / cross_sectional_area) * (10 ** 6),
                                   Stress3=(Group_A_6_D0['Load 3'] / cross_sectional_area) * (10 ** 6),
                                   Stress4=(Group_A_6_D0['Load 4'] / cross_sectional_area) * (10 ** 6),
                                   Stress5=(Group_A_6_D0['Load 5'] / cross_sectional_area) * (10 ** 6))

Group_A_6_D0 = Group_A_6_D0.assign(Strain1=(Group_A_6_D0['Extension 1'] / length) * 100,
                                   Strain2=(Group_A_6_D0['Extension 2'] / length) * 100,
                                   Strain3=(Group_A_6_D0['Extension 3'] / length) * 100,
                                   Strain4=(Group_A_6_D0['Extension 4'] / length) * 100,
                                   Strain5=(Group_A_6_D0['Extension 5'] / length) * 100)

# Lets continue with the Data of Grp A for 6% at Day 0

Group_A_6_D7 = Group_A_6_D7.assign(Stress1=(Group_A_6_D7['Load 1'] / cross_sectional_area) * (10 ** 6),
                                   Stress2=(Group_A_6_D7['Load 2'] / cross_sectional_area) * (10 ** 6),
                                   Stress3=(Group_A_6_D7['Load 3'] / cross_sectional_area) * (10 ** 6),
                                   Stress4=(Group_A_6_D7['Load 4'] / cross_sectional_area) * (10 ** 6),
                                   Stress5=(Group_A_6_D7['Load 5'] / cross_sectional_area) * (10 ** 6))

Group_A_6_D7 = Group_A_6_D7.assign(Strain1=(Group_A_6_D7['Extension 1'] / length) * 100,
                                   Strain2=(Group_A_6_D7['Extension 2'] / length) * 100,
                                   Strain3=(Group_A_6_D7['Extension 3'] / length) * 100,
                                   Strain4=(Group_A_6_D7['Extension 4'] / length) * 100,
                                   Strain5=(Group_A_6_D7['Extension 5'] / length) * 100)

# Lets Plot the Stress - Strain graphs for each % and Day
fonttype = {'fontname': 'Times New Roman'}
with plt.style.context('seaborn-notebook'):
    ax1 = plt.subplot(221)
    ax1.plot(Group_A_4_D0['Strain1'], Group_A_4_D0['Stress1'])
    ax1.plot(Group_A_4_D0['Strain2'], Group_A_4_D0['Stress2'])
    ax1.plot(Group_A_4_D0['Strain3'], Group_A_4_D0['Stress3'])
    ax1.plot(Group_A_4_D0['Strain4'], Group_A_4_D0['Stress4'])
    ax1.plot(Group_A_4_D0['Strain5'], Group_A_4_D0['Stress5'])
    plt.rcParams['figure.dpi'] = 360
    ax1.set_xlim([0, 20])
    ax1.set_title('Day 0 - 4%', fontsize=12, **fonttype, weight="bold")
    ax1.set_ylabel('Stress Pa', fontsize=12, **fonttype)
    ax1.set_xlabel('Strain %', fontsize=12, **fonttype)
    ax1.legend(['Specimen 1', 'Specimen 2', 'Specimen 3', 'Specimen 4', 'Specimen 5'],
               bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., prop={"size": 12,
                                                                                   "family": 'Times New Roman'})
    for tick in ax1.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax1.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax2 = plt.subplot(222)
    ax2.plot(Group_A_4_D7['Strain1'], Group_A_4_D7['Stress1'])
    ax2.plot(Group_A_4_D7['Strain2'], Group_A_4_D7['Stress2'])
    ax2.plot(Group_A_4_D7['Strain3'], Group_A_4_D7['Stress3'])
    ax2.plot(Group_A_4_D7['Strain4'], Group_A_4_D7['Stress4'])
    ax2.plot(Group_A_4_D7['Strain5'], Group_A_4_D7['Stress5'])
    ax2.set_xlim([0, 20])
    plt.rcParams['figure.dpi'] = 360
    ax2.set_title('Day 7 - 4%', fontsize=12, **fonttype, weight="bold")
    ax2.set_ylabel('Stress Pa', fontsize=12, **fonttype)
    ax2.set_xlabel('Strain %', fontsize=12, **fonttype)
    for tick in ax2.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax2.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax3 = plt.subplot(223)
    ax3.plot(Group_A_6_D0['Strain1'], Group_A_6_D0['Stress1'])
    ax3.plot(Group_A_6_D0['Strain2'], Group_A_6_D0['Stress2'])
    ax3.plot(Group_A_6_D0['Strain3'], Group_A_6_D0['Stress3'])
    ax3.plot(Group_A_6_D0['Strain4'], Group_A_6_D0['Stress4'])
    ax3.plot(Group_A_6_D0['Strain5'], Group_A_6_D0['Stress5'])
    ax3.set_xlim([0, 20])
    plt.rcParams['figure.dpi'] = 360
    ax3.set_title('Day 0 - 6%', fontsize=12, **fonttype, weight="bold")
    ax3.set_ylabel('Stress Pa', fontsize=12, **fonttype)
    ax3.set_xlabel('Strain %', fontsize=12, **fonttype)
    for tick in ax3.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax3.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax4 = plt.subplot(224)
    ax4.plot(Group_A_6_D7['Strain1'], Group_A_6_D7['Stress1'])
    ax4.plot(Group_A_6_D7['Strain2'], Group_A_6_D7['Stress2'])
    ax4.plot(Group_A_6_D7['Strain3'], Group_A_6_D7['Stress3'])
    ax4.plot(Group_A_6_D7['Strain4'], Group_A_6_D7['Stress4'])
    ax4.plot(Group_A_6_D7['Strain5'], Group_A_6_D7['Stress5'])
    ax4.set_xlim([0, 20])
    plt.rcParams['figure.dpi'] = 360
    ax4.set_title('Day 7 - 6%', fontsize=12, **fonttype, weight="bold")
    ax4.set_ylabel('Stress Pa', fontsize=12, **fonttype)
    ax4.set_xlabel('Strain %', fontsize=12, **fonttype)
    for tick in ax4.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax4.get_yticklabels():
        tick.set_fontname("Times New Roman")

plt.tight_layout(pad=0.2)
# plt.show()

# Lets Plot the Stress - Time graphs for each % and Day

fonttype = {'fontname': 'Times New Roman'}
with plt.style.context('seaborn-notebook'):
    ax1 = plt.subplot(221)
    plt.rcParams['figure.dpi'] = 360
    ax1.plot(Group_A_4_D0['Time 1'], Group_A_4_D0['Stress1'])
    ax1.plot(Group_A_4_D0['Time 2'], Group_A_4_D0['Stress2'])
    ax1.plot(Group_A_4_D0['Time 3'], Group_A_4_D0['Stress3'])
    ax1.plot(Group_A_4_D0['Time 4'], Group_A_4_D0['Stress4'])
    ax1.plot(Group_A_4_D0['Time 5'], Group_A_4_D0['Stress5'])
    ax1.set_title('Day 0 - 4%', fontsize=12, **fonttype, weight="bold")
    ax1.set_ylabel('Stress Pa', fontsize=12, **fonttype)
    ax1.set_xlabel('Time (s)', fontsize=12, **fonttype)
    ax1.legend(['Specimen 1', 'Specimen 2', 'Specimen 3', 'Specimen 4', 'Specimen 5'],
               bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., prop={"size": 12,
                                                                                   "family": 'Times New Roman'})
    for tick in ax1.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax1.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax2 = plt.subplot(222)
    ax2.plot(Group_A_4_D7['Time 1'], Group_A_4_D7['Stress1'])
    ax2.plot(Group_A_4_D7['Time 2'], Group_A_4_D7['Stress2'])
    ax2.plot(Group_A_4_D7['Time 3'], Group_A_4_D7['Stress3'])
    ax2.plot(Group_A_4_D7['Time 4'], Group_A_4_D7['Stress4'])
    ax2.plot(Group_A_4_D7['Time 5'], Group_A_4_D7['Stress5'])
    ax2.set_title('Day 7 - 4%', fontsize=12, **fonttype, weight="bold")
    ax2.set_ylabel('Stress Pa', fontsize=12, **fonttype)
    ax2.set_xlabel('Time (s)', fontsize=12, **fonttype)
    plt.rcParams['figure.dpi'] = 360
    for tick in ax2.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax2.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax3 = plt.subplot(223)
    ax3.plot(Group_A_6_D0['Time 1'], Group_A_6_D0['Stress1'])
    ax3.plot(Group_A_6_D0['Time 2'], Group_A_6_D0['Stress2'])
    ax3.plot(Group_A_6_D0['Time 3'], Group_A_6_D0['Stress3'])
    ax3.plot(Group_A_6_D0['Time 4'], Group_A_6_D0['Stress4'])
    ax3.plot(Group_A_6_D0['Time 5'], Group_A_6_D0['Stress5'])
    ax3.set_title('Day 0 - 6%', fontsize=12, **fonttype, weight="bold")
    ax3.set_ylabel('Stress Pa', fontsize=12, **fonttype)
    ax3.set_xlabel('Time (s)', fontsize=12, **fonttype)
    plt.rcParams['figure.dpi'] = 360
    for tick in ax3.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax3.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax4 = plt.subplot(224)
    ax4.plot(Group_A_6_D7['Time 1'], Group_A_6_D7['Stress1'])
    ax4.plot(Group_A_6_D7['Time 2'], Group_A_6_D7['Stress2'])
    ax4.plot(Group_A_6_D7['Time 3'], Group_A_6_D7['Stress3'])
    ax4.plot(Group_A_6_D7['Time 4'], Group_A_6_D7['Stress4'])
    ax4.plot(Group_A_6_D7['Time 5'], Group_A_6_D7['Stress5'])
    plt.rcParams['figure.dpi'] = 360
    ax4.set_title('Day 7 - 6%', fontsize=12, **fonttype, weight="bold")
    ax4.set_ylabel('Stress Pa', fontsize=12, **fonttype)
    ax4.set_xlabel('Strain %', fontsize=12, **fonttype)
    for tick in ax4.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax4.get_yticklabels():
        tick.set_fontname("Times New Roman")

plt.tight_layout(pad=0.2)
# plt.show()

# Lets calculate 15% Tangent Modulus, mean and sdv for each curve of Group_A_4_D0

Table_15_Spec1 = Group_A_4_D0.loc[Group_A_4_D0['Strain1'] == 15]
Tangent_Modulus_Spc1 = Table_15_Spec1['Stress1'].values / 0.15

Table_15_Spec2 = Group_A_4_D0.loc[Group_A_4_D0['Strain2'] == 15]
Tangent_Modulus_Spc2 = Table_15_Spec2['Stress2'].values / 0.15

Table_15_Spec3 = Group_A_4_D0.loc[Group_A_4_D0['Strain3'] == 15]
Tangent_Modulus_Spc3 = Table_15_Spec3['Stress3'].values / 0.15

Table_15_Spec4 = Group_A_4_D0.loc[Group_A_4_D0['Strain4'] == 15]
Tangent_Modulus_Spc4 = Table_15_Spec4['Stress4'].values / 0.15

Table_15_Spec5 = Group_A_4_D0.loc[Group_A_4_D0['Strain5'] == 15.0]
Tangent_Modulus_Spc5 = Table_15_Spec5['Stress5'].values / 0.15

Tangent_mean_4_D0 = np.mean(
    [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3, Tangent_Modulus_Spc4, Tangent_Modulus_Spc5])
Tangent_stdv_4_D0 = np.std(
    [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3, Tangent_Modulus_Spc4, Tangent_Modulus_Spc5])

T1 = {'15% Tangent Modulus of Grp A 4% D0': [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3,
                                             Tangent_Modulus_Spc4,
                                             Tangent_Modulus_Spc5, Tangent_mean_4_D0, Tangent_stdv_4_D0]
      }
T1 = pd.DataFrame(T1, columns=['15% Tangent Modulus of Grp A 4% D0'], index=['Specimen 1', 'Specimen 2',
                                                                             'Specimen 3', 'Specimen 4', 'Specimen 5',
                                                                             'Mean', 'Standard Deviation'])

print('\n', T1)

# Lets calculate 15% Tangent Modulus, mean and sdv for each curve of Group_A_4_D7

Table_15_Spec1 = Group_A_4_D7.loc[Group_A_4_D7['Strain1'] == 15.02]
Tangent_Modulus_Spc1 = Table_15_Spec1['Stress1'].values / 0.15

Table_15_Spec2 = Group_A_4_D7.loc[Group_A_4_D7['Strain2'] == 15.02]
Tangent_Modulus_Spc2 = Table_15_Spec2['Stress2'].values / 0.15

Table_15_Spec3 = Group_A_4_D7.loc[Group_A_4_D7['Strain3'] == 15.02]
Tangent_Modulus_Spc3 = Table_15_Spec3['Stress3'].values / 0.15

Table_15_Spec4 = Group_A_4_D7.loc[Group_A_4_D7['Strain4'] == 15.02]
Tangent_Modulus_Spc4 = Table_15_Spec4['Stress4'].values / 0.15

Table_15_Spec5 = Group_A_4_D7.loc[Group_A_4_D7['Strain5'] == 15.02]
Tangent_Modulus_Spc5 = Table_15_Spec5['Stress5'].values / 0.15

Tangent_mean_4_D7 = np.mean(
    [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3, Tangent_Modulus_Spc4, Tangent_Modulus_Spc5])
Tangent_stdv_4_D7 = np.std(
    [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3, Tangent_Modulus_Spc4, Tangent_Modulus_Spc5])

T2 = {'15% Tangent Modulus of Grp A 4% D7': [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3,
                                             Tangent_Modulus_Spc4,
                                             Tangent_Modulus_Spc5, Tangent_mean_4_D7, Tangent_stdv_4_D7]
      }
T2 = pd.DataFrame(T2, columns=['15% Tangent Modulus of Grp A 4% D7'], index=['Specimen 1', 'Specimen 2',
                                                                             'Specimen 3', 'Specimen 4', 'Specimen 5',
                                                                               'Mean', 'Standard Deviation'])

print('\n', T2)

# Lets calculate 15% Tangent Modulus, mean and sdv for each curve of Group_A_6_D0

Table_15_Spec1 = Group_A_6_D0.loc[Group_A_6_D0['Strain1'] == 15]
Tangent_Modulus_Spc1 = Table_15_Spec1['Stress1'].values / 0.15

Table_15_Spec2 = Group_A_6_D0.loc[Group_A_6_D0['Strain2'] == 15.02]
Tangent_Modulus_Spc2 = Table_15_Spec2['Stress2'].values / 0.15

Table_15_Spec3 = Group_A_6_D0.loc[Group_A_6_D0['Strain3'] == 15.02]
Tangent_Modulus_Spc3 = Table_15_Spec3['Stress3'].values / 0.15

Table_15_Spec4 = Group_A_6_D0.loc[Group_A_6_D0['Strain4'] == 15]
Tangent_Modulus_Spc4 = Table_15_Spec4['Stress4'].values / 0.15

Table_15_Spec5 = Group_A_6_D0.loc[Group_A_6_D0['Strain5'] == 15.02]
Tangent_Modulus_Spc5 = Table_15_Spec5['Stress5'].values / 0.15

Tangent_mean_6_D0 = np.mean(
    [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3, Tangent_Modulus_Spc4, Tangent_Modulus_Spc5])
Tangent_stdv_6_D0 = np.std(
    [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3, Tangent_Modulus_Spc4, Tangent_Modulus_Spc5])

T3 = {'15% Tangent Modulus of Grp A 6% D0': [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3,
                                             Tangent_Modulus_Spc4,
                                             Tangent_Modulus_Spc5, Tangent_mean_6_D0, Tangent_stdv_6_D0]
      }
T3 = pd.DataFrame(T3, columns=['15% Tangent Modulus of Grp A 6% D0'], index=['Specimen 1', 'Specimen 2',
                                                                             'Specimen 3', 'Specimen 4', 'Specimen 5',
                                                                             'Mean', 'Standard Deviation'])

print('\n', T3)

# Lets calculate 15% Tangent Modulus, mean and sdv for each curve of Group_A_6_D7

Table_15_Spec1 = Group_A_6_D7.loc[Group_A_6_D7['Strain1'] == 15]
Tangent_Modulus_Spc1 = Table_15_Spec1['Stress1'].values / 0.15

Table_15_Spec2 = Group_A_6_D7.loc[Group_A_6_D7['Strain2'] == 15]
Tangent_Modulus_Spc2 = Table_15_Spec2['Stress2'].values / 0.15

Table_15_Spec3 = Group_A_6_D7.loc[Group_A_6_D7['Strain3'] == 15]
Tangent_Modulus_Spc3 = Table_15_Spec3['Stress3'].values / 0.15

Table_15_Spec4 = Group_A_6_D7.loc[Group_A_6_D7['Strain4'] == 15]
Tangent_Modulus_Spc4 = Table_15_Spec4['Stress4'].values / 0.15

Table_15_Spec5 = Group_A_6_D7.loc[Group_A_6_D7['Strain5'] == 15.0]
Tangent_Modulus_Spc5 = Table_15_Spec5['Stress5'].values / 0.15

Tangent_mean_6_D7 = np.mean(
    [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3, Tangent_Modulus_Spc4, Tangent_Modulus_Spc5])
Tangent_stdv_6_D7 = np.std(
    [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3, Tangent_Modulus_Spc4, Tangent_Modulus_Spc5])

T4 = {'15% Tangent Modulus of Grp A 6% D7': [Tangent_Modulus_Spc1, Tangent_Modulus_Spc2, Tangent_Modulus_Spc3,
                                             Tangent_Modulus_Spc4,
                                             Tangent_Modulus_Spc5, Tangent_mean_6_D7, Tangent_stdv_6_D7]
      }
T4 = pd.DataFrame(T4, columns=['15% Tangent Modulus of Grp A 6% D7'], index=['Specimen 1', 'Specimen 2',
                                                                             'Specimen 3', 'Specimen 4', 'Specimen 5',
                                                                             'Mean', 'Standard Deviation'])

print('\n', T4)

# Lets plot Tangent Modulus mean and sdv for each % and D

data = {'Sample Preparation': ['Day 0 - 4% Agarose', 'Day 0 - 6% Agarose', 'Day 7 - 4% Agarose', 'Day 7 - 6% Agarose'],
        'Tangent Modulus Mean (Pa)': [Tangent_mean_4_D0, Tangent_mean_4_D7, Tangent_mean_6_D0, Tangent_mean_6_D7],
        'Tangent Modulus SD (Pa)': [Tangent_stdv_4_D0, Tangent_stdv_4_D7, Tangent_stdv_6_D0, Tangent_stdv_6_D7], }

Mean_Stdv_TM = pd.DataFrame(data,
                            columns=['Sample Preparation', 'Tangent Modulus Mean (Pa)', 'Tangent Modulus SD (Pa)'])
print('\n', Mean_Stdv_TM)

fig = plt.figure()
ax = fig.add_subplot(221)
ax.bar('Sample Preparation', 'Tangent Modulus Mean (Pa)', data=Mean_Stdv_TM, linewidth=1.5, facecolor="deeppink",
       edgecolor="deeppink", capsize=0.05, width=0.5)
plt.rcParams['figure.dpi'] = 360
ax.set_title('Tangent Modulus Mean After 0 & 7 Days - 4% vs 6% Agarose', fontsize=12, **fonttype, weight="bold")
ax.set_ylabel('Tangent Modulus Mean (Pa)', fontsize=12, **fonttype)
ax.set_xlabel('')
for tick in ax.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax.get_yticklabels():
    tick.set_fontname("Times New Roman")
sns.despine()

ax2 = fig.add_subplot(222)
ax2.bar('Sample Preparation', 'Tangent Modulus SD (Pa)', data=Mean_Stdv_TM, linewidth=1.5, facecolor="mediumvioletred",
        edgecolor="mediumvioletred", capsize=0.05, width=0.5)
plt.rcParams['figure.dpi'] = 360
ax2.set_title('Tangent Modulus SD After 0 & 7 Days - 4% vs 6% Agarose', fontsize=12, **fonttype, weight="bold")
ax2.set_ylabel('Tangent Modulus SD (Pa)', fontsize=12, **fonttype)
ax2.set_xlabel('')
for tick in ax2.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax2.get_yticklabels():
    tick.set_fontname("Times New Roman")
sns.despine()

# Lets plot Tangent Modulus boxplot for each % and D

T1.reset_index(drop=True, inplace=True)
T2.reset_index(drop=True, inplace=True)
T3.reset_index(drop=True, inplace=True)
T4.reset_index(drop=True, inplace=True)

D0_4 = T1.loc[:, ['15% Tangent Modulus of Grp A 4% D0']]
D7_4 = T2.loc[:, ['15% Tangent Modulus of Grp A 4% D7']]
D0_6 = T3.loc[:, ['15% Tangent Modulus of Grp A 6% D0']]
D7_6 = T4.loc[:, ['15% Tangent Modulus of Grp A 6% D7']]

box_table = pd.concat([D0_4, D7_4, D0_6, D7_6], axis=1, sort=False)
box_table.drop(box_table.tail(2).index, inplace=True)
box_table.rename(columns={'15% Tangent Modulus of Grp A 4% D0': '4%_D0', '15% Tangent Modulus of Grp A 4% D7': '4%_D7',
                          '15% Tangent Modulus of Grp A 6% D0': '6%_D0', '15% Tangent Modulus of Grp A 6% D7': '6%_D7'},
                 inplace=True)
box_table = box_table.astype(int)
print('\n', box_table.to_markdown())

color = {'boxes': 'crimson', 'whiskers': 'crimson',
         'medians': 'green', 'caps': 'crimson'}

labels = ['Day 0 - 4% Agarose', 'Day 7 - 4% Agarose', 'Day 0 - 6% Agarose', 'Day 7 - 6% Agarose']

ax3 = fig.add_subplot(212)
ax3.boxplot(box_table, patch_artist=True, labels=labels, vert=False,
            boxprops=dict(facecolor='lavenderblush', color='darkmagenta'),
            capprops=dict(color='darkmagenta'),
            whiskerprops=dict(color='darkmagenta'),
            flierprops=dict(markeredgecolor='darkmagenta'),
            medianprops=dict(color='darkmagenta'))
ax3.set_title('Boxplot', fontsize=12, **fonttype, weight="bold")
ax3.set_xlabel('Tangent Modulus at 15%', fontsize=12, **fonttype)
ax3.set_ylabel('Sample Preparation', fontsize=12, **fonttype)
plt.rcParams['figure.dpi'] = 360
for tick in ax3.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax3.get_yticklabels():
    tick.set_fontname("Times New Roman")
# plt.show()

GAG_content = pd.read_excel(r'/Users/macbookpro/Desktop/MAT311 - Tissue Engineering and Regenerative Medicine - '
                            r'2020:21/Coursework 1 (marking  criteria)-20201114/GAGcontent_28thOct2020.xlsx',
                            sheet_name='DataSet1')

Dataset1 = GAG_content.iloc[0:24, [0, 1, 5]]
Dataset1.rename(columns={'Sample': 'Day & Concentration', 'Total GAG (ug/ml)': 'Mean'}, inplace=True)
Dataset = Dataset1.groupby('Day & Concentration', axis=0).mean()
Dataset['Standard Deviation'] = Dataset1.groupby('Day & Concentration', axis=0).std()
Dataset.index = ['4%-Day 0', '6%-Day 0', '4%-Day 7', '6%-Day 7']
Dataset = Dataset.reset_index()
print('\n', Dataset)

fig2 = plt.figure()
ax1 = fig2.add_subplot(221)
ax1.bar('index', 'Mean', data=Dataset, linewidth=1.5, facecolor="darkturquoise",
        edgecolor="darkturquoise", capsize=0.05, width=0.5)
plt.rcParams['figure.dpi'] = 360
ax1.set_title('Mean GAG Concentrations After 0 & 7 Days - 4% vs 6% Agarose', fontsize=12, **fonttype, weight="bold")
ax1.set_ylabel('Mean GAG Concentrations', fontsize=12, **fonttype)
ax1.set_xlabel('')
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
sns.despine()

ax2 = fig2.add_subplot(222)
ax2.bar('index', 'Standard Deviation', data=Dataset, linewidth=1.5, facecolor="gold",
        edgecolor="gold", capsize=0.05, width=0.5)
plt.rcParams['figure.dpi'] = 360
ax2.set_title('SD GAG Concentrations After 0 & 7 Days - 4% vs 6% Agarose', fontsize=12, **fonttype, weight="bold")
ax2.set_ylabel('SD GAG Concentrations', fontsize=12, **fonttype)
ax2.set_xlabel('')
for tick in ax2.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax2.get_yticklabels():
    tick.set_fontname("Times New Roman")
sns.despine()
plt.tight_layout(pad=2.5)
plt.savefig('books_read.png')


# INDEPENDENT T-TEST USING RESEARCHPY
ANOVA = pd.read_excel(r'/Users/macbookpro/Desktop/MAT311 - Tissue Engineering and Regenerative Medicine - '
                      r'2020:21/Coursework 1 (marking  criteria)-20201114/GAGcontent_28thOct2020.xlsx',
                      sheet_name='ANOVA')
ANOVA = ANOVA.iloc[0:6, 0:4]
print('\n', ANOVA.to_markdown())

summary, results = rp.ttest(group1=ANOVA['4% agarose Day 0'], group1_name="4% agarose Day 0",
                            group2=ANOVA['6% agarose Day 0'], group2_name="6% agarose Day 0")
print('\n', summary.to_markdown())
print('\n', results.to_markdown())

summary, results = rp.ttest(group1=ANOVA['4% agarose Day 7'], group1_name="4% agarose Day 7",
                            group2=ANOVA['6% agarose Day 7'], group2_name="6% agarose Day 7")
print('\n', summary.to_markdown())
print('\n', results.to_markdown())

summary, results = rp.ttest(group1=ANOVA['4% agarose Day 0'], group1_name="4% agarose Day 0",
                            group2=ANOVA['4% agarose Day 7'], group2_name="4% agarose Day 7")
print('\n', summary.to_markdown())
print('\n', results.to_markdown())

summary, results = rp.ttest(group1=ANOVA['6% agarose Day 0'], group1_name="6% agarose Day 0",
                            group2=ANOVA['6% agarose Day 7'], group2_name="6% agarose Day 7")
print('\n', summary)
print('\n', results)

# ANOVA
from bioinfokit.analys import stat
data = {'Day 0 - 4% Agarose': [Tangent_mean_4_D0,Tangent_stdv_4_D0],
        'Day 0 - 6% Agarose': [ Tangent_mean_6_D0,Tangent_stdv_6_D0],
        'Day 7 - 4% Agarose': [Tangent_mean_4_D7,Tangent_stdv_4_D7],
        'Day 7 - 6% Agarose':[Tangent_mean_6_D7,Tangent_stdv_6_D7]}

pg = pd.DataFrame(data, columns=['Day 0 - 4% Agarose', 'Day 0 - 6% Agarose', 'Day 7 - 4% Agarose', 'Day 7 - 6% Agarose'])

pg = pd.melt(pg.reset_index(), id_vars=['index'], value_vars=['Day 0 - 4% Agarose', 'Day 0 - 6% Agarose', 'Day 7 - 4% Agarose', 'Day 7 - 6% Agarose'])
# replace column names
pg.columns = ['index', 'treatments', 'value']
pg = pg.set_index(['index'])
pg.to_csv('ANOVA.csv')

res = stat()
res.anova_stat(df=pg, res_var='value', anova_model='value ~ C(treatments)')
res.anova_summary.to_csv('file2.csv')

res.tukey_hsd(df=pg, res_var='value', xfac_var='treatments', anova_model='value ~ C(treatments)')
print('\n',res.tukey_summary)
res.tukey_summary.to_csv('file1.csv')
# plt.show()

import seaborn as sns
fig2 = plt.figure(figsize=(6, 6))
ax1 = fig2.add_subplot(111)
ax6 = sns.boxplot(x='treatments', y='value', data=ANOVA, color='plum')
ax6 = sns.swarmplot(x="treatments", y="value", data=ANOVA, color='indigo')
ax6.set_ylabel('Total GAG (ug/ml)', fontsize=12, **fonttype)
ax6.set_xlabel('Sample Preparation',fontsize=12, **fonttype)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
plt.savefig('ghs.png')