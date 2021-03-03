# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, a in cars.iterrows() :
    print(lab)
    print(a)
    
    
    
    
    #loop over dataframe 2
    # Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab+ ": " +str(row['cars_per_cap']))
    
#add coluimn 1
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column

for lab, a in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = a["country"].upper() 
   


# Print cars
print(cars)

#add col 2
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
#for lab, row in cars.iterrows() :
 #   cars.loc[lab, "COUNTRY"] = row["country"].upper()
cars["COUNTRY"]= cars["country"].apply(str.upper)
print(cars)
