addTwo <- function(x, y){
  x + y
  
}
##Functions return the last statement

above10 <- function(x){
  above <- x>10
  x[above]
}

above <- function(x, n){
  above <- x>n
  x[above]
}

## Default Value
aboveDefault <- function(x, n=10){
  above <- x>n
  x[above]
}


##Dates in R
x <- as.date(1979,01,01)
print(unclass(x)) ##Because it is stored as time after 1970-01-01

x <- sys.time
print(x)
p <- as.POSIXlt(x)
print(unclass(p))
print(p$sec)

datestring <- ("Janury 10, 2012, 10:40", "December 9, 2011, 9:10")
x <- striptime(datestring, "%B %d, %Y %H %M")
print(x)
print(class(x))

####
##Week 2 Quiz

cube <- function(x, n){
  x^3
}

