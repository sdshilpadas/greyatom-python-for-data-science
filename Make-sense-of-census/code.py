# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
#concatenate new_record to data
census=np.concatenate([data, new_record])
print(census)

#create new array age
age=census[:,0]
max_age= np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)
print(max_age,min_age,age_mean,age_std)

#subsetting the array based on race
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

race_list=[len_0, len_1,len_2, len_3, len_4]
#find minority race
minority_race=race_list.index(min(race_list))
print(minority_race)

#subsetting the array based on age
senior_citizens=census[census[:,0]>60]
#add working hours
working_hours_sum=senior_citizens.sum(axis=0)[6]
#length of senior_citizen variable
senior_citizens_len=len(senior_citizens)
#average working hour of senior citizen
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)

#Creating an array based on 'education' column
high=census[census[:,1]>10]
#Finding the average pay
avg_pay_high=high[:,7].mean()
#Printing the average pay
print(avg_pay_high)
#Creating an array based on 'education' column
low=census[census[:,1]<=10]
#Finding the average pay
avg_pay_low=low[:,7].mean()
#Printing the average pay
print(avg_pay_low)
#Code ends here












