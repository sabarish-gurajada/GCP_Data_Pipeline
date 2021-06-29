def invoke(status):
  import requests
  requests.get('https://europe-west2-etl-pipeline-307118.cloudfunctions.net/validation?bucketname=tcsdemo2021&datafile=stg_loc_x_client.csv')
  requests.get('https://europe-west2-etl-pipeline-307118.cloudfunctions.net/validation?bucketname=tcsdemo2021&datafile=stg_trading_trans.csv')
  requests.get('https://europe-west2-etl-pipeline-307118.cloudfunctions.net/validation?bucketname=tcsdemo2021&datafile=stg_client.csv')
  requests.get('https://europe-west2-etl-pipeline-307118.cloudfunctions.net/validation?bucketname=tcsdemo2021&datafile=stg_loc_x_bus_rep.csv')
  requests.get('https://europe-west2-etl-pipeline-307118.cloudfunctions.net/validation?bucketname=tcsdemo2021&datafile=stg_location.csv')
  requests.get('https://europe-west2-etl-pipeline-307118.cloudfunctions.net/validation?bucketname=tcsdemo2021&datafile=stg_bus_rep.csv')
  requests.get('https://europe-west2-etl-pipeline-307118.cloudfunctions.net/validation?bucketname=tcsdemo2021&datafile=stg_client_date.csv')
  requests.get('https://europe-west2-etl-pipeline-307118.cloudfunctions.net/validation?bucketname=tcsdemo2021&datafile=stg_trading_trans_record.csv')
  print(status)


status = "success"
invoke(status)
