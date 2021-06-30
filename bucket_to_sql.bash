#!/bin/bash
# Usage: Cloud auth, create bucket, move data from on premises - bucket, create sql instance and insert uploaded data
# Author: Sabarish Gurajada
# ————————————————————————

echo "Please enter the key generated on premise to decrypt the data"
read KEY_GEN
echo "Please copy required folder from bucket ex:gs://bucket/foldername/"
# To list all files inside this folder so we can choose which file we want to move
gsutil ls -d gs://*
echo " "
echo " "
echo "---------------------------"
read GSUTIL_FOLDER
gsutil -o "GSUtil:encryption_key=${KEY_GEN}" cp -r ${GSUTIL_FOLDER} /home/tcsdem02021/ejournal/

#  get sql instance and create using cloud command
echo “Enter SQL instance name must be composed of lowercase letters, numbers, and hyphens must start with a letter”
read sqlname
gcloud sql instances create ${sqlname} --tier=db-n1-standard-1 --activation-policy=ALWAYS

#  get sql instance password
echo “Enter SQL instance password. Please remember the password as it is reused multiple times”
read password
gcloud sql users set-password root --host % --instance ${sqlname}  --password ${password}



#Allowlist the Cloud Shell instance for management access to your SQL instance. (Optional)
export ADDRESS=$(wget -qO - http://ipecho.net/plain)/32

# ADDRESS=34.76.41.217/32


gcloud sql instances patch ${sqlname} --authorized-networks $ADDRESS

#Get the IP address of your Cloud SQL instance by running
MYSQLIP=$(gcloud sql instances describe ${sqlname} --format="value(ipAddresses.ipAddress)")

#Create the flights table using the create_table.sql file
echo “Enter the create table sql path”
read create_table_path
mysql --host=$MYSQLIP --user=root --password --verbose < /home/tcsdem02021/ejournal/GCP_Ejournal/create_table.sql



#  Import CSV file into cloud SQL

mysqlimport --local --host=$MYSQLIP --user=root --password --ignore-lines=1 --fields-terminated-by=',' Ejournal /home/tcsdem02021/ejournal/GCP_Ejournal/Ejournal_live_data.csv

