import numpy as np 

block_days = 28
n_shifts = {"chief":14,"senior":15,"junior":16,"intern":17}

def potential_allocation(rank):
	arr = np.array([1]*n_shifts[rank] + [0]*(block_days-n_shifts[rank]))
	np.random.shuffle(arr)
	while max(count_runs(arr)) > 5:
		np.random.shuffle(arr)
	return np.c_[arr,[0]*block_days].ravel()

def count_runs(arr):
	run_length = [1]
	run_length_index = 0
	for i in xrange(1,len(arr)):
		if arr[i] == arr[i-1] and arr[i] == 1:
			run_length[run_length_index] += 1
		elif arr[i] != arr[i-1] and arr[i] == 1:
			run_length += [1]
			run_length_index += 1
	return run_length

def decode(arr):
	decoded = []
	for item in np.reshape(arr,(-1,2)):
		if item[0] == 0 and item[1] == 0:
			decoded += ["Off"]
		elif item[0] == 0 and item[1] ==1:
			decoded += ["Night"]
		elif item[0] == 1 and item[1] == 0:
			decoded += ["Day"]
	print np.reshape(arr,(-1,2))

potential_shift = potential_allocation("senior")
print potential_shift
print decode(potential_shift)