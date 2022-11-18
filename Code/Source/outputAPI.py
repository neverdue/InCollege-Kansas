import json
from Code.Source.globalVariables import getMyCollege_appliedJobs, getMyCollege_jobs, getMyCollege_savedJobs, getDataFile, getMyCollege_profiles, getMyCollege_user
from Code.Source.utility import getApplicationsDataBase, getJobsDataBase

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
def createMyCollege_usersOutput():
    print()
    #placeholder function for another time
    outputFile = getMyCollege_user()

    f = open(outputFile, "w") 

    with open(getDataFile()) as json_file:
        data = json.load(json_file)
        for user in data["accounts"]:
            subscription = ""
            if(user["subscription"] == "False"):
                subscription = "standard"
            else:
                subscription = "plus"
            f.write(user["username"] + ' ' + subscription + "\n")
            f.write("=====\n")

    f.close()
    return

def createMyCollege_profilesOutput():
    #placeholder function for another time
    outputFile = getMyCollege_profiles()
    tupleValue = 1
    f = open(outputFile, "w") 

    with open(getDataFile()) as json_file:
        data = json.load(json_file)
        for user in data["accounts"]:
            if(user["profile"]["education"]):
                # print(user["username"], "has a profile")
                # print(user["profile"])
                if(user["profile"]["title"]):
                    f.write(user["profile"]["title"] + "\n")
                if(user["profile"]["major"]):
                    f.write(user["profile"]["major"] + "\n")
                if(user["profile"]["university"]):
                    f.write(user["profile"]["university"] + "\n")
                if(user["profile"]["about"]):
                    f.write(user["profile"]["about"] + "\n")
                if(user["profile"]["experience"]):
                    for experience in user["profile"]["experience"]:
                        for entries in experience.items():
                            f.write(entries[tupleValue] + " ")
                        f.write("\n")
                if(user["profile"]["education"]):
                    for education in user["profile"]["education"]:
                        for entries in education.items():
                            f.write(entries[tupleValue] + " ")
                        f.write("\n")
                f.write("=====\n")
    f.close()
    return

def outputAPIs():
    jobsDataBase = getJobsDataBase()
    applications = getApplicationsDataBase()["applications"]
    saved = getApplicationsDataBase()["saved"]
    outputToMyCollege_jobs(jobsDataBase)
    outputToMyCollege_appliedJobs(applications, jobsDataBase)
    outputToMyCollege_savedJobs(saved, jobsDataBase)
    createMyCollege_profilesOutput()
    createMyCollege_usersOutput()