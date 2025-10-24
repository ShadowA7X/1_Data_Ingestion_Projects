# 1_Data_Ingestion_Projects
This repository will be totally focused on mini examples of how to Ingest data from different resources

------------------------
API_Ingestion.py
------------------------

This file will create a CSV file using the https://randomuser.me/ API. Each time you execute this file, 10 new
records will be added to the CSV (If it previously exist. If not, It will create a new one)


------------------------
add_records_to_csv.sh
------------------------

You can schedule a job in your Mac to trigger this file using Cron. For this:

A) Open your terminal and then type: crontab -e

B) If you want that the CSV gets new records every day at 12PM, then you need to use the Cron syntax:

0 12 * * * /full/path/to/your/add_records_to_csv.sh

You can use the "pwd" command to get the full path faster.

Once you paste the command, you need to press Esc and then write :wq to save the file and exit.

If eveything goes well, you will see the "crontab: installing new crontab". This means that this job will be executed
according to the schedule you defined.

You can verify the Job by using the command: crontab -l

