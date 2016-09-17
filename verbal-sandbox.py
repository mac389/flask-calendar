import numpy as np 
import random, itertools, calendar

translation_table = {"Day" : [1,0], "Night" : [0,1], "Off" : [0,0]}

block_days = 28
n_shifts = {"chief":14,"senior":15,"junior":16,"intern":17}
n_nights = 8 

weekend_dates = [1,2,7,8]

def count_runs(arr):
	run_length = [1]
	run_length_index = 0
	for i in xrange(1,len(arr)):
		if arr[i] == arr[i-1] and arr[i] != "Off":
			run_length[run_length_index] += 1
		elif arr[i] != arr[i-1] and arr[i] != "Off":
			run_length += [1]
			run_length_index += 1
	return run_length

def day_follows_night(arr):
	return any([arr[i] == "Night" and arr[i+1] == "Day" for i in xrange(len(arr)-1)])

def no_weekends(arr,weekend_dates):
	return all([arr[i] == "Off" for i in weekend_dates])

def potential_allocation(rank, weekend_dates):
	arr = np.array(["Night"] * n_nights +  
				["Day"] * (block_days - n_nights) + 
				["Off"] * (block_days-n_shifts[rank])).astype(str)

	np.random.shuffle(arr)

	while any([max(count_runs(arr)) > 5, day_follows_night(arr),no_weekends(arr,weekend_dates)]):
		np.random.shuffle(arr)
	return arr

#Not trying to control for conference attendance
#Check after test run that conference attendance is exceptable

#Not trying to have blocks with same person, could be in version 2.0 
	
print potential_allocation("senior", weekend_dates)