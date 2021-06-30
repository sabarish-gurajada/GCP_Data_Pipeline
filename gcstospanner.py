def download_blob(bucket_name, source_blob_name, destination_file_name):  
    """Downloads a blob from the bucket."""
    import csv
    import codecs
    import argparse
    from google.cloud import storage, spanner
    import base64
    import osa
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob("staging/"+source_blob_name)
    blob.download_to_filename(destination_file_name)
    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

def insert_data(instance_id, database_id, bucket_name, table_id, batchsize, data_file, format_file):
  import csv
  import codecs
  import argparse
  from google.cloud import storage, spanner
  import base64
  import os
  spanner_client = spanner.Client()
  instance = spanner_client.instance(instance_id)
  database = instance.database(database_id)
  # Generate a unique local temporary file name to allow multiple invocations
  # of the tool from the same parent directory, and enable path to
  # multi-threaded loader in future
  local_file_name = 'tmp'
  # TODO (djrut): Add exception handling
  download_blob(bucket_name, data_file, local_file_name)
  # Figure out the source and target column names based on the schema file
  # provided, and add a uuid if that option is enabled
  storage_client = storage.Client()
  bucket = storage_client.get_bucket(bucket_name)
  format_file1 = "tmp1"
  blob = bucket.blob("staging/"+format_file)
  blob.download_to_filename(format_file1)
  print('Blob {} downloaded to {}.'.format(
      format_file,
      format_file1))

  fmtfile = open(format_file1, 'r')
  fmtreader = csv.reader(fmtfile)
  collist = []
  typelist = []
  icols = 0
  for col in fmtreader:
    collist.append(col[1])
    typelist.append(col[2])
    icols = icols + 1
  numcols = len(collist)
  ifile  = open(local_file_name, "r")
  reader = csv.reader(ifile,delimiter=',')
  next(reader)
  alist = []
  irows = 0
  for row in reader:
    for x in range(0,numcols):
      if typelist[x] == 'integer':
        row[x] = int(row[x])
      if typelist[x] == 'float':
        row[x] = float(row[x])
      if typelist[x] == 'bytes':
        row[x] = base64.b64encode(row[x])
    alist.append(row)
    irows = irows + 1
  ifile.close()
  rowpos = 0
  batchrows = int(batchsize)
  while rowpos < irows:
    with database.batch() as batch:
      batch.insert(
        table=table_id,
        columns=collist,
        values=alist[rowpos:rowpos+batchrows]
        )
    rowpos = rowpos + batchrows
  print('inserted {0} rows'.format(rowpos))
#   os.remove('tmp')
  # insert_data(args.instance_id, args.database_id, args.bucket_name, args.table_id, args.batchsize, args.data_file, args.format_file)
  insert_data(instance_id, database_id, bucket_name, table_id, batchsize, data_file, format_file)
