import pandas as pd
data = {
    "Name" : ["Tejas", "Gayatri", "Shaurya"],
    "Maths" : [90,89,78],
    "English" : [78,55,58]
}
students=pd.DataFrame(data)
print(students)

import pandas as pd
sales = {
    "Product" : ["Laptop", "desktop", "Mouse",  "keyboard"],
    "Price" : [10000,8999,150, 250],
    "sold" : [780,550,508,900]
}
df = pd.DataFrame(sales)
print(df[["Product", "Price", "sold"]].head(1))