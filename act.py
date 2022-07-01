import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def gas():
    doc = pd.read_csv('./gas_prices.csv')
    # exp = doc.describe()
    # print(exp)
    # exp.to_csv('../../Desktop/export.csv')
    plt.figure(figsize=[10, 6], dpi=100)
    exclusion = ['Year', 'South Korea', 'Canada', 'Italy']
    for country in doc:
        if country not in exclusion:
            plt.plot(doc.Year, doc[country], label=country, marker='.', linewidth=1)
    plt.xticks(doc.Year[::3])
    plt.grid(color='#ababab', linewidth=1)
    plt.xlabel('Years')
    plt.ylabel('USD')
    plt.legend(loc=2)
    plt.savefig('./testpicture.png')
    plt.show()


def fifa(inp):
    if inp=='h':
        doc = pd.read_csv('./fifa_data.csv')
        num = np.arange(40,110,10,dtype=int)
        plt.hist(doc.Overall, bins=num, color='r')
        plt.xticks(num)
        plt.ylabel('rarity')
        plt.xlabel('overall')
        print(doc)
        plt.show()

    if inp=='p':
        doc=pd.read_csv('./fifa_data.csv')
        left = doc.loc[doc['Preferred Foot']=='Left'].count()[0]
        right = doc.loc[doc['Preferred Foot']=='Right'].count()[0]
        labels = ['Left','Right']
        color = ['#ababab','#ff33cc']
        explosion = [0,0.1]
        plt.pie([left,right],labels=labels,colors=color,explode=explosion,autopct='%.3f %%')
        plt.title('Foot Preferrence')
        plt.show()

    if inp=='w':
        doc=pd.read_csv('./fifa_data.csv')
        doc.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in doc.Weight]
        under = doc.loc[doc.Weight < 135].count()[0]
        std = doc.loc[(doc.Weight >= 135) & (doc.Weight < 145)].count()[0]
        std1= doc.loc[(doc.Weight >=145) & (doc.Weight < 155)].count()[0]
        std2 = doc.loc[(doc.Weight >=155) & (doc.Weight < 165)].count()[0]
        std3 = doc.loc[(doc.Weight >= 165) & (doc.Weight < 175)].count()[0]
        std4 = doc.loc[(doc.Weight >= 175) & (doc.Weight < 185)].count()[0]
        over = doc.loc[(doc.Weight >= 185)].count()[0]
        weights = [under,std,std1,std2,std3,std4,over]
        labels = ['under','std','std1','std2','std3','std4','over']
        plt.pie(weights,labels=labels,explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.1])
        plt.show()

# gas()
fifa('w')
