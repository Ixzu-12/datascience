import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as p


data= p.DataFrame({
"play type":["run","pass","run","pass","pass"],
"down":[1,2,3,4,1],
"yards to go":[10,5,7,3,8],
"yards gained":[7,3,5,2,9],
"passer":["tom brady","harry","ash","serena","shogun"],
"reciver":["kaneki","rintaro","suga","hinata","nishinoya"],
"rusher":["naruto","sauske","itachi","madara","obito"],
"result":["first down","first down","incomplete","incomplete","touchdown"]
})
# sns.barplot(x="play type",y="yards gained",data=data,palette="bwr")
# plt.title("FootBall")
# sns.set_context("poster",font_scale=2)

# plt.grid()
# plt.figure(figsize=(11,11))

# player_data=data.groupby("passer")["yards gained"].sum()
# colors = ['#4B9CD3', '#28527A', '#8AC6D1', '#9AD3BC', '#BFD8B8']
# passchart=sns.barplot(x=player_data.index,y=player_data.values,palette=colors)
# plt.xticks(rotation=45)
# plt.show()
# sns.pairplot(data,hue="play type",palette="bwr")

# plt.show()
