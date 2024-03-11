import numpy
import pyarrow.parquet as pq
import requests
from io import BytesIO
from PIL import Image
from tqdm import tqdm

filename = "/content/part-00000-17da4908-939c-46e5-91d0-15f256041956-c000.snappy.parquet?download=true"
df = pq.read_table(filename).to_pandas()

li = []

for i in tqdm(range(len(df))):
    if i > 20:
        break
    try:
        response = requests.get(df.iloc[i]['url'])
        image_bytes = BytesIO(response.content)
        raw_image = Image.open(image_bytes)
        li.append(i)
    except:
        continue

df.iloc[li].reset_index(drop=True).to_csv('data.csv', index=False)
