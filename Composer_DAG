# RVSRDL DEMO - DAG 
# Version 1.4
import os
from airflow import models
from airflow.providers.google.cloud.operators.functions import CloudFunctionInvokeFunctionOperator
from airflow.utils import dates
from airflow.operators import bash_operator

GCP_PROJECT_ID = os.environ.get('GCP_PROJECT_ID', 'etl-pipeline-307118')
GCP_LOCATION = os.environ.get('GCP_LOCATION', 'europe-west2')


# [START howto_operator_gcf_default_args]
default_args = {'owner': 'airflow'}
# [END howto_operator_gcf_default_args]


with models.DAG(
    'Main_Data_Pipeline',
    schedule_interval=None,  # Override to match your needs
    start_date=dates.days_ago(1),
    tags=['example'],
) as dag:
    
    invoke_task0 = CloudFunctionInvokeFunctionOperator(
        task_id="invoke_file_validation",
        location=GCP_LOCATION,
        input_data={},
        function_id="invoke_Validation",
    )
    invoke_task1 = CloudFunctionInvokeFunctionOperator(
        task_id="invoke_stg_trading_trans",
        location=GCP_LOCATION,
        input_data={},
        function_id="test",
    )
    invoke_task2 = CloudFunctionInvokeFunctionOperator(
        task_id="invoke_stg_arrangement",
        location=GCP_LOCATION,
        input_data={},
        function_id="test1",
    )
    invoke_task3 = CloudFunctionInvokeFunctionOperator(
        task_id="invoke_stg_party",
        location=GCP_LOCATION,
        input_data={},
        function_id="test2",
    )
    invoke_task4 = CloudFunctionInvokeFunctionOperator(
        task_id="invoke_stg_facility",
        location=GCP_LOCATION,
        input_data={},
        function_id="test3",
    )
    invoke_task5 = CloudFunctionInvokeFunctionOperator(
        task_id="invoke_stg_fac_x_arr",
        location=GCP_LOCATION,
        input_data={},
        function_id="test4",
    )
    invoke_task6 = CloudFunctionInvokeFunctionOperator(
        task_id="invoke_stg_x_party",
        location=GCP_LOCATION,
        input_data={},
        function_id="test5",
    )

    make_bq_Staging = bash_operator.BashOperator(
        task_id='Make_Staging_Dataset',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq --location=europe-west2  mk -d --default_table_expiration 3600 --description "This is for staging" staging',
    )
    make_bq_rdw_dm_dataset = bash_operator.BashOperator(
        task_id='Make_rdw_dm_Dataset',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq --location=europe-west2  mk -d --default_table_expiration 3600 --description "This is for data mart" rdw_dm',
    )
    make_bq_rdw_dwh_dataset = bash_operator.BashOperator(
        task_id='Make_rdw_dwh_Dataset',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq --location=europe-west2  mk -d --default_table_expiration 3600 --description "This is for warehouse area" rdw_dwh',
    )
    make_bq_party_table = bash_operator.BashOperator(
        task_id='Create_Party_table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq mk --table --expiration 3600 --description "This is Party table" --label organization:development rdw_dwh.party_t Party_source_Code:INTEGER,PARTY_NAME:STRING,PARTY_TYPE:STRING,Start_date:DATE,End_Date:DATE',
    )
    make_bq_Facility_X_Arr_table = bash_operator.BashOperator(
        task_id='Create_Facility_X_Arr_table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq mk --table --expiration 3600 --description "This is Facility_X_Arr table" --label organization:development rdw_dwh.fac_x_arr_t FACILITY_ID:INTEGER,ARR_ID:INTEGER,Start_date:DATE,End_Date:DATE',
    )
    make_bq_Facility_table = bash_operator.BashOperator(
        task_id='Create_Facility_table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq mk --table --expiration 3600 --description "This is Facility table" --label organization:development rdw_dwh.facility_t Facility_id:INTEGER,Facility_name:STRING,Facility_Type:STRING,Currency_Code:STRING,Start_date:DATE,End_Date:DATE',
    )
    make_bq_Arrangement_table = bash_operator.BashOperator(
        task_id='Create_Arrangement_table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq mk --table --expiration 3600 --description "This is Arrangement table" --label organization:development rdw_dwh.arr_t Arr_Source_code:INTEGER,Source_System_CD:STRING,MATURITY_DATE_ID:DATE,ACCOUNT_FLAG:STRING,LARGE_PRINT_IDICATOR:INTEGER,Start_date:DATE,End_Date:DATE',
    )
    make_bq_Facility_X_Party_table = bash_operator.BashOperator(
        task_id='Create_Facility_X_Party_table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq mk --table --expiration 3600 --description "This Facility_X_Party table" --label organization:development rdw_dwh.fac_x_party_t PARTY_ID:INTEGER,FACILITY_ID:INTEGER,Start_date:DATE,End_Date:DATE',
    )
    make_bq_Trading_table = bash_operator.BashOperator(
        task_id='Create_Trading_table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq mk --table --expiration 3600 --description "This is Trading table" --label organization:development rdw_dwh.daily_trad_t ARR_ID:INTEGER,Snapshot_date:DATE,Snapshot_Date_ID:INTEGER,Limit_Value:NUMERIC,Limit_GBP:NUMERIC,Balance:NUMERIC,Balance_GBP:NUMERIC,BI_INSERT_DATE:DATE,BI_UPDATE_DATE:DATE,Undrawn_amount:NUMERIC,Undrawn_amount_GBP:NUMERIC,Cleared_Balance:NUMERIC,Cleared_Balance_GBP:NUMERIC',
    )
    # make_bq_Consoliated_table = bash_operator.BashOperator(
    #     task_id='Create_Consolidated_table',
    #     # Executing 'bq' command requires Google Cloud SDK which comes
    #     # preinstalled in Cloud Composer.
    #     bash_command='bq mk --table --expiration 3600 --description "This is my table" --label organization:development rdw_dm.currency_con_t c_Country:STRING,e_rate:NUMERIC',
    # )

    make_bq_DataMart_table = bash_operator.BashOperator(
        task_id='Create_table_DataMart',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command='bq mk --table --expiration 3600 --description "This is table created in datamart" --label organization:development rdw_dm.credit_parm_t Party_Name:STRING,Snapshot_DATE:DATE,max_Limit:NUMERIC,Total_BALANCE:NUMERIC',
    )
    
    make_json_table = bash_operator.BashOperator(
        task_id='Create_Json_Table_Rates',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command = 'bq mk --table --expiration 3600 --description "This is my table" --label organization:development rdw_dwh.currency_con_t c_Country:STRING,e_rate:NUMERIC' ,
    )

    load_party_table = bash_operator.BashOperator(
        task_id='Load_Party_Table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command="bq query --use_legacy_sql=false 'INSERT INTO rdw_dwh.party_t Select Party_source_Code ,PARTY_NAME ,PARTY_TYPE ,Start_date ,End_Date from staging.stg_data_with_ht_stg_party  where Key_value < 2228'",
    )
    load_Facility_X_Arr_table = bash_operator.BashOperator(
        task_id='Load_Facility_X_Arr_Table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command="bq query --use_legacy_sql=false 'INSERT INTO rdw_dwh.fac_x_arr_t  Select  FACILITY_ID ,ARR_ID ,Start_date ,End_Date   from staging.stg_data_with_ht_stg_fac_x_arr where Arr_Source_code = 1 '",
    )
    load_Facility_table = bash_operator.BashOperator(
        task_id='Load_Facility__Table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command="bq query --use_legacy_sql=false 'INSERT INTO rdw_dwh.facility_t Select  CAST(Facility_Source_code AS INT64) ,Facility_name,Facility_Type,Currency_Code,Start_date,End_Date from staging.stg_data_with_ht_stg_facility  where Key_value < 14379'",
    )
    load_Arrangement_table = bash_operator.BashOperator(
        task_id='Load_Arrangement_Table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command="bq query --use_legacy_sql=false 'INSERT INTO rdw_dwh.arr_t  Select  Arr_Source_code ,Source_System_CD ,MATURITY_DATE_ID ,ACCOUNT_FLAG,LARGE_PRINT_IDICATOR,Start_date,End_Date from staging.stg_data_with_ht_stg_arrangement where Key_value < 60216'",
    )
    load_Facility_X_Party_table = bash_operator.BashOperator(
        task_id='Load_Facility_X_Party_Table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command="bq query --use_legacy_sql=false 'INSERT INTO rdw_dwh.fac_x_party_t  Select  PARTY_ID ,FACILITY_ID ,Start_date ,End_Date  from staging.stg_data_with_ht_stg_fac_x_party  where PARTY_FAC_CODE = 1 '",
    )
    load_Trading_X_Party_table = bash_operator.BashOperator(
        task_id='Load_Trading_X_Party_Table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command="bq query --use_legacy_sql=false 'INSERT INTO rdw_dwh.daily_trad_t Select  ARR_ID,Snapshot_DATE,Snapshot_Date_ID,Limit_Value,Limit_GBP, Balance,Balance_GBP,BI_INSERT_DATE,BI_UPDATE_DATE,Undrawn_amount,Undrawn_amount_GBP,Cleared_Balance,Cleared_Balance_GBP  from staging.stg_data_with_ht_stg_trading_trans'",
    )

    load_Data_DataMart_table = bash_operator.BashOperator(
        task_id='Load_Data_DataMart_Table',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command="bq query --use_legacy_sql=false 'INSERT INTO rdw_dm.credit_parm_t SELECT    E.PARTY_NAME, A.Snapshot_date ,MAX(A.Limit_Value) , SUM(A.Balance)    FROM    rdw_dwh.daily_trad_t   A   INNER JOIN  rdw_dwh.arr_t  B ON  A.ARR_ID  = B.Arr_Source_code  INNER JOIN  rdw_dwh.fac_x_arr_t  C ON  B.Arr_Source_code  =  C.ARR_ID  INNER JOIN  rdw_dwh.fac_x_party_t   D ON  C.FACILITY_ID  =  D.FACILITY_ID  INNER JOIN  rdw_dwh.party_t  E ON D.PARTY_ID   =  E.Party_source_Code   GROUP  BY  E.Party_Name, A.Snapshot_DATE ORDER BY  E.Party_Name'",
    )
    
    push_data_gsutil_outbound = bash_operator.BashOperator(
        task_id='Push_Data_Outbound_Datastream',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command = "bq extract 'staging.stg_data_with_ht_stg_facility' gs://rvsrdldemo20/outbound/party_consolidated.csv" ,
    )

    load_json_table = bash_operator.BashOperator(
        task_id='Load_Currency_Rates',
        # Executing 'bq' command requires Google Cloud SDK which comes
        # preinstalled in Cloud Composer.
        bash_command = 'bq load --source_format=NEWLINE_DELIMITED_JSON rdw_dwh.currency_con_t gs://rvsrdldemo20/inbound/currency_load.json c_Country:STRING,e_rate:NUMERIC' ,
    )    


    invoke_task0 >> make_bq_Staging
    make_bq_Staging >> invoke_task1 
    make_bq_Staging >> invoke_task2 
    make_bq_Staging >> invoke_task3 
    make_bq_Staging >> invoke_task4 
    make_bq_Staging >> invoke_task5 
    make_bq_Staging >> invoke_task6

    [invoke_task1, invoke_task2, invoke_task3, invoke_task4, invoke_task5, invoke_task6] >> make_bq_rdw_dwh_dataset

    make_bq_rdw_dwh_dataset >> make_bq_party_table >> load_party_table
    make_bq_rdw_dwh_dataset >> make_bq_Facility_X_Arr_table >> load_Facility_X_Arr_table
    make_bq_rdw_dwh_dataset >> make_bq_Facility_table >> load_Facility_table
    make_bq_rdw_dwh_dataset >> make_bq_Arrangement_table >> load_Arrangement_table
    make_bq_rdw_dwh_dataset >> make_bq_Facility_X_Party_table >> load_Facility_X_Party_table
    make_bq_rdw_dwh_dataset >> make_bq_Trading_table >> load_Trading_X_Party_table
    make_bq_rdw_dwh_dataset >> make_json_table >> load_json_table

    [ load_party_table, load_Facility_X_Arr_table, load_Facility_table, load_Arrangement_table, load_Facility_X_Party_table, load_Trading_X_Party_table ] >> make_bq_rdw_dm_dataset >>  make_bq_DataMart_table >> load_Data_DataMart_table >> push_data_gsutil_outbound

