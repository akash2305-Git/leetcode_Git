"""
Given a set of n jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time.
We earn the profit associated with a job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.
 Deadline of the job is the time on or before which job needs to be completed to earn the profit.

Examples :

Input: Jobs = [[1,4,20],[2,1,1],[3,1,40],[4,1,30]]
Output: 2 60
Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).
Input: Jobs = [[1,2,100],[2,1,19],[3,2,27],[4,1,25],[5,1,15]]
Output: 2 127
Explanation: 2 jobs can be done with maximum profit of 127 (100+27).


"""

class Jobs:

    def __init__(self,profit=0,deadline=0):

        self.profit = profit
        self.deadline = deadline
        self.id = 0


class Job_Sequence:

    def job_sequencing(self,Jobs):

        Jobs.sort(key=lambda x:x.profit,reverse=True)
        maxi = Jobs[0].deadline

        for i in range(1,len(Jobs)):
            maxi = max(maxi,Jobs[i].deadline)

        slot = [-1] * (maxi+1)
        countJobs = 0
        jobProfit = 0

        for i in range(len(Jobs)):
            for j in range(Jobs[i].deadline,0,-1):
                if slot[j] == -1:
                    slot[j] = i
                    countJobs += 1
                    jobProfit += Jobs[i].profit
                    break


        return countJobs,jobProfit



if __name__ == "__main__":

    jb = Job_Sequence()
    jobs = [[Jobs(20,4)],[Jobs(1,1)],[Jobs(40,1)],[Jobs(30,1)]]

    ans1 , ans2 = jb.job_sequencing(jobs)

    print(ans1,ans2)

