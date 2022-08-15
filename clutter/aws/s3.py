import boto3
import fnmatch
from botocore.exceptions import UnknownKeyError

SESSION_OPTS = {
    "aws_access_key_id": None,
    "aws_secret_access_key": None,
    "aws_session_token": None,
    "region_name": None,
    "botocore_session": None,
    "profile_name": None,
}


def list_objects(bucket, prefix=None, pattern=None, session=None, session_opts=None):
    # correct
    prefix = prefix if prefix else ""
    pattern = "*" + pattern if pattern else pattern
    session_opts = session_opts if session_opts else {}

    # get list of objects
    contents = []
    session = session if session else boto3.Session(**session_opts)
    client = session.client("s3")
    paginator = client.get_paginator("list_objects_v2")
    for response in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for content in response.get("Contents", []):
            if not pattern or fnmatch.fnmatch(content["Key"], pattern):
                contents.append(content)

    return contents


def delete_objects(bucket, prefix, pattern=None, session=None, session_opts=None):
    # correct
    prefix = prefix if prefix else ""
    session_opts = session_opts if session_opts else {}

    # list objects to delete
    session = session if session else boto3.Session(**session_opts)
    contents = list_objects(bucket=bucket, prefix=prefix, pattern=pattern, session=session)
    if len(contents) > 0:
        delete = {"Objects": [{"Key": content["Key"]} for content in contents]}

        # delete objects
        client = session.client("s3")
        response = client.delete_objects(Bucket=bucket, Delete=delete)

        return response["Deleted"]

    raise FileNotFoundError(f"no pattern '{pattern}' in prefix '{bucket}/{prefix}'!")
