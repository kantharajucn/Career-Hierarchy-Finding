# Career-Hierarchy-Finding

Dataset:
1. JSON file with 50k career paths, one career path per line
2. Each career path has multiple JSON objects per each job and it is is descending order from present to previous job positions.
3. Each JSON object has start date, Job name and end date 

My Approach:
1. For finding the usual duration
     1a. Calculated the duration from start date and end date for all jobs
     1b. Obtained all the unique job positions and the number of occurrence using collection "Counter"
     1c. For all unique job positions calculated the sum of duration.
     1d. Found out the average of duration.
     1e. Result is written to averageDuration.json file in the format {job:average duration} 
2. For finding the Hierarchy
     2a. found out the similar jobs and their number of occurrence for the level from which the hierarchy needs to be find.
     2b. In second level, find out different possibilities of job positions for each previous level job positions.
            Example: First level internship occurred 10 times
                             In next level what are the possibilities for each occurrence in first level like {Internship: junior Engineer} or {Internship:  Master Thesis} etc
     2c. Found out the probability for job position in first level to all other possible next job positions.
     2d. Result is written to probability.json file in the format {first job -> next job: probability}

All these tasks are done using simple Dictionary, Counter, List etc.

How to Run:
1. Extract the SaacCo.rar file.
2. Keep the input file in input directory(It is already present)
3. Execute main.py file
4. Enter the starting level from which the hierarchy needs to be find.
5. Results can be found in output folder.
Other approaches can also be applied but with limited time, I could do this approach.
