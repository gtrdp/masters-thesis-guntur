attach(mtcars)

plot(wt, mpg, main="Scatterplot Example 1",
     xlab="Car Weight ", ylab="Miles Per Gallon ", pch=19)

plot(wt, mpg, main="Scatterplot Example 2",
     xlab="Car Weight ", ylab="Miles Per Gallon ", pch=19)

abline(lm(mpg~wt), col="red") # regression line (y~x) 
lines(lowess(wt,mpg), col="blue") # lowess line (x,y)

pairs(~mpg+disp+drat+wt,data=mtcars, 
      main="Simple Scatterplot Matrix")
