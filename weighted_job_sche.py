from functools import cmp_to_key

class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit

def jobcomp(s1, s2):
    return s1.finish < s2.finish

def latestNonConflict(arr, i):
    for j in range(i - 1, -1, -1):
        if arr[j].finish <= arr[i - 1].start:
            return j
    return -1

def findMaxProfitRec(arr, n):
    if n == 0:
        return 0, [] 
    elif n == 1:
        return arr[0].profit, [arr[0]]  
    
    inclProf = arr[n - 1].profit
    i = latestNonConflict(arr, n)

    if i != -1:
        inclProf += findMaxProfitRec(arr, i + 1)[0]

    exclProf, jobs_excluded = findMaxProfitRec(arr, n - 1)

    if inclProf > exclProf:
        jobs_included = [arr[n - 1]] + findMaxProfitRec(arr, i + 1)[1]
        return inclProf, jobs_included
    else:
        return exclProf, jobs_excluded

def findMaxProfit(arr, n):
    arr = sorted(arr, key=cmp_to_key(jobcomp))
    return findMaxProfitRec(arr, n)

# Collect jobs from user input
arr = []
num_jobs = int(input("Enter the number of jobs: "))

for i in range(num_jobs):
    start = int(input(f"Enter start time for job {i + 1}: "))
    finish = int(input(f"Enter finish time for job {i + 1}: "))
    profit = int(input(f"Enter profit for job {i + 1}: "))
    arr.append(Job(start, finish, profit))

n = len(arr)

optimal_profit, optimal_jobs = findMaxProfit(arr, n)

print("The optimal profit is", optimal_profit)
print("Jobs contributing to the optimal profit:")
for job in optimal_jobs:
    print(f"Job: Start={job.start}, Finish={job.finish}, Profit={job.profit}")
