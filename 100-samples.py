import pandas as pd 
import numpy as np
pd.read_csv("/Users/kiyok/desktop/for-13th-dec/Tokyo-listing-original.csv")


df = pd.read_csv("/Users/kiyok/desktop/for-13th-dec/Tokyo-listing-original.csv")
# extracted 100 randam samples from dataset  
df.sample(n = 100) 

transposedMatrix = np.transpose((df.sample(n = 100) )
print (transposedMatrix)