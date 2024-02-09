
import pandas as pd 
from plotnine import ggplot, aes, facet_grid, labs, geom_col, theme_xkcd 
  
# reading dataset 
df = pd.read_csv("tips.csv") 
  
plot = ( 
    ggplot(df) 
    + facet_grid(facets="~sex") 
    + aes(x="day", y="total_bill", fill="time") 
    + labs( 
        x="day", 
        y="total_bill", 
    ) 
    + geom_col() 
    + theme_xkcd() 
) 
  
# plot.save("gfg plotnine tutorial.png")




