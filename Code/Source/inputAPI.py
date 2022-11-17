from Code.Source.globalVariables import getNewJobs

def inputToMyCollege_jobs(newJobs):
    with open(getNewJobs(), 'w') as f:
        for title, jobData in newJobs.items():
            f.write(title + '\n')
            f.write(jobData["Description"] + '\n')
            f.write("&&&" + '\n')
            f.write(jobData["Name"] + '\n')
            f.write(jobData["Employer"] + '\n')
            f.write(jobData["Location"] + '\n')
            f.write(jobData["Salary"] + '\n')
            f.write("=====" + '\n')