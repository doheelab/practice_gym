import ray

# Create a Dataset of Python objects.
ds = ray.data.range(10000)
# -> Dataset(num_blocks=200, num_rows=10000, schema=<class 'int'>)

ds.take(5)
ds.count()
ds = ray.data.from_items([{"col1": i, "col2": str(i)} for i in range(10000)])

ds.show(5)
ds.schema()

import pandas as pd
import dask.dataframe as dd

# Create a Dataset from a list of Pandas DataFrame objects.
pdf = pd.DataFrame({"one": [1, 2, 3], "two": ["a", "b", "c"]})
ds = ray.data.from_pandas([pdf])


# Create a Dataset from a Dask-on-Ray DataFrame.
dask_df = dd.from_pandas(pdf, npartitions=10)
ds = ray.data.from_dask(dask_df)


ds = ray.data.range(10000)
ds = ds.map(lambda x: x * 2)
# -> Map Progress: 100%|████████████████████| 200/200 [00:00<00:00, 1123.54it/s]
# -> Dataset(num_blocks=200, num_rows=10000, schema=<class 'int'>)
ds.take(5)
# -> [0, 2, 4, 6, 8]

ds.filter(lambda x: x > 5).take(5)
# -> [6, 8, 10, 12, 14]

ds.flat_map(lambda x: [x, -x]).take(5)
# -> [0, 0, 2, -2, 4]
