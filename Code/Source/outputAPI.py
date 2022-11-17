from Code.Source.globalVariables import getMyCollege_appliedJobs, getMyCollege_jobs, getMyCollege_savedJobs


def outputToMyCollege_jobs(jobsDataBase):
    with open(getMyCollege_jobs(), 'w') as f:
        for job in jobsDataBase:
            f.write(job["Title"] + '\n')
            f.write(job["Description"] + '\n')
            f.write("&&&" + '\n')
            f.write(job["Employer"] + '\n')
            f.write(job["Location"] + '\n')
            f.write(job["Salary"] + '\n')
            f.write('=====' + '\n')

def outputToMyCollege_appliedJobs(applications, jobs):
    allJobIDs = [job["id"] for job in jobs]
    appliedJobIDs = []
    with open(getMyCollege_appliedJobs(), 'w') as f:
        for username, applications in applications.items():
            for jobID, data in applications.items():
                f.write(data["Title"] + '\n')
                f.write("{},{}".format(username, data["paragraph"]) + '\n')
                f.write('=====' + '\n')
                appliedJobIDs.append(jobID)
        unAppliedJobIds = list(set(allJobIDs) - set(appliedJobIDs))
        for jobID in unAppliedJobIds:
            for job in jobs:
                if job["id"] == jobID:
                    f.write(job["Title"] + '\n')
                    f.write('=====' + '\n')

def outputToMyCollege_savedJobs(saved, jobs):
    jobs_dict = {job["id"]: job for job in jobs}
    with open(getMyCollege_savedJobs(), 'w') as f:
        for username, savedList in saved.items():
            f.write(username + ',')
            for i in range(len(savedList) - 1):
                f.write(jobs_dict[savedList[i]]["Title"] + ',')
            f.write(jobs_dict[savedList[-1]]["Title"] + '\n')
            f.write('=====' + '\n')