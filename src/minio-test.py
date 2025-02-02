import os
import asyncio

from dotenv import load_dotenv
from s3fs import S3FileSystem

load_dotenv()

MINIO_SERVER_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY')
MINIO_SERVER_SECRET_KEY = os.getenv('MINIO_SECRET_KEY')
MINIO_URL = os.getenv('MINIO_URL')

async def main():
    s3 = S3FileSystem(
        endpoint_url=MINIO_URL,
        key=MINIO_SERVER_ACCESS_KEY,
        secret=MINIO_SERVER_SECRET_KEY,
        use_ssl=False
    )

    buckets = await s3._lsbuckets()
    print(buckets)

if __name__ == '__main__':
    asyncio.run(main())