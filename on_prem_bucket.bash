#!/bin/bash
# Usage: Cloud auth, create bucket, move data from on premises - bucket, create sql instance and insert uploaded data
# Author: Sabarish Gurajada
# ————————————————————————


# To get an active account to complete all the required task
# Generated key for the account created by default and attached as keyhole
echo "Enter Service account name"
read service_account
echo "Enter Path of key Json file"
read service_account_key_path
#gcloud auth activate-service-account tcsdemo2021@appspot.gserviceaccount.com --key-file=/Users/admin/Downloads/tcsdemo2021-04b6026c9cf9.json
gcloud auth activate-service-account ${service_account} --key-file=${service_account_key_path}

# Create a bucket in gcp to move data from on premise to cloud
echo “Please enter the bucket name you want to create - Note: Time stamp HHMMS will be attached at the end of the bucket name for uniqueness”
read bucket_name;
Cur_date=`date +%H%M%S`
# user specified bucket name_folder will be created
gsutil mb -c nearline gs://${bucket_name}_${Cur_date}
gsutil ls -l | grep "${bucket_name}_${Cur_date}"
echo "created.."

# To generate customer encryption key
echo ""
echo ""
echo "Please wait encryption key is getting generated...."
./key_gen.bash > key_${Cur_date}.txt

echo "Key Generated successfully"
KEY_GEN=`cat key_${Cur_date}.txt | awk '{ print $6 }'`

echo $KEY_GEN

echo " "
echo " "


# To get the folder path to move to cloud bucket
echo “Enter the folder directory which you want to move to cloud bucket”
read file_directory
# gsutil command to move folder to google cloud
# To use encrypted key while transferring data from on premise to Gcloud
#gsutil -m cp -r ${file_directory} gs://${bucket_name}_${Cur_date}

gsutil -o "GSUtil:encryption_key=${KEY_GEN}" cp -r ${file_directory} gs://${bucket_name}_${Cur_date}


# establish connection to cloud shell
gcloud cloud-shell ssh
