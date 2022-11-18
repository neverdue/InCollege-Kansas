import json
from Code.Source.globalVariables import getJobFile
from Code.Source.utility import getJobsDataBase, parseData_newJobs, writeJson

def inputMyCollege_jobs(newJobs):
    jobsDataBase = getJobsDataBase()
    jobTitlesDataBase = [job["Title"] for job in jobsDataBase]
    newJobsTitles = [job["Title"] for job in newJobs]
    for title in newJobsTitles:
        if title not in jobTitlesDataBase and len(jobsDataBase) < 10:
            jobsDataBase.append(newJobs[newJobsTitles.index(title)])
    
    with open (getJobFile()) as jsonFile:
        data = json.load(jsonFile)
        data["jobPosts"] = jobsDataBase
        data["numPosts"] = len(jobsDataBase)
    
    writeJson(data, getJobFile())

def inputAPIs():
    newJobs = parseData_newJobs()
    inputMyCollege_jobs(newJobs)