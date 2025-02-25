from docarray import BaseDoc
from docarray.typing import NdArray

class ToyDoc(BaseDoc):
  text: str = ''
  embedding: NdArray[128]

from docarray import DocList
import numpy as np
from vectordb import InMemoryExactNNVectorDB, HNSWVectorDB

# Specify your workspace path
# db = InMemoryExactNNVectorDB[ToyDoc](workspace='./workspace_path')
db = HNSWVectorDB[ToyDoc](workspace='./workspace_path')

# Index a list of documents with random embeddings
doc_list = [ToyDoc(text=f'toy doc {i}', embedding=np.random.rand(128)) for i in range(1000)]
db.index(inputs=DocList[ToyDoc](doc_list))

# Perform a search query
query = ToyDoc(text='query', embedding=np.random.rand(128))
results = db.search(inputs=DocList[ToyDoc]([query]), limit=10)

# Print out the matches
i = 0
len_res = len(results[0].matches)
for m in results[0].matches:
  if i == len_res - 1:
    print(m)
  print(f'{i+1} matching\n')
  i += 1
  