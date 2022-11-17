from Code.Source.globalVariables import dataFileInit, stackInit
from Code.Source.inputAPI import inputToMyCollege_jobs
from Code.Source.mainPage import mainPage
from Code.Source.outputAPI import outputToMyCollege_appliedJobs, outputToMyCollege_jobs, outputToMyCollege_savedJobs
from Code.Source.utility import getApplicationsDataBase, getJobsDataBase, parseData_newJobs, updateJobsDataBase


def main():
    dataFileInit()

    #Initialize stack and add login page
    stackInit()

    newJobs = {
        "Professional monkey trainer": {
            "Description": "Trains monkeys to do tricks",
            "Employer": "Circus",
            "Location": "Tampa, FL",
            "Salary": "$30000",
            "Name": "Chau Nguyen",
            "TimeCreated": "11/01/2022 23:59:59"
        },
        "Professional dog trainer": {
            "Description": "Trains dogs to do tricks",
            "Employer": "Circus",
            "Location": "Tampa, FL",
            "Salary": "$30000",
            "Name": "tommy truong",
            "TimeCreated": "11/16/2022 21:23:07"
        },
        "Honey badger": {
            "Description": "Honey badger don't care\nFor some reason this description is long\nActually it's not that long\nI'm kidding it's long",
            "Employer": "Self-employed",
            "Location": "Somewhere",
            "Salary": "$40000",
            "Name": "tommy truong",
            "TimeCreated": "11/16/2022 21:23:07"
        }
    }

    inputToMyCollege_jobs(newJobs)

    newJobs = parseData_newJobs()

    jobsDataBase = getJobsDataBase()

    updateJobsDataBase(jobsDataBase, newJobs)

    outputToMyCollege_jobs(jobsDataBase)
    
    applications = getApplicationsDataBase()["applications"]
    saved = getApplicationsDataBase()["saved"]
    outputToMyCollege_appliedJobs(applications, jobsDataBase)
    outputToMyCollege_savedJobs(saved, jobsDataBase)

    mainPage()


if __name__ == "__main__":
    main()