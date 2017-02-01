sayHi <- function(name){
  print("Hi" + name)
}

## c() function
## Concatenates to create vectors
x <- c(0.5, 0.6)      #numeric
x <- c(TRUE, FALSE)   #boolean
x <- c(T, F)          #boolean
x <- c("a", "b", "c") #character
x <- 9:29             #integer
x <- c(1+0i, 2+4i)    #complex

## Using the vector() function
x <- vector("numeric", length=10)

## Explicit Coersion
x <- 1:10
print(as.character(x))
print(as.logical(x))

## Matrix
x <- matrix(nrow=2, ncol=4)
print(x)
print(dim(x))
print(attributes(x))

m <- 1:10
dim(m) <- c(2,5)
print(m)

## cbind and rbind
x <- 10:12
y <- 1:3
print(cbind(x, y))
print(rbind(x, y))

## Factors
f <- factor(c("yes", "yes", "no", "no", "yes"))
print(f)
print(unclass(f))

## Set the levels of the factor
f <- factor(c("yes", "yes", "no", "no", "yes"), levels=c("yes", "no"))

## Data Frames
x <- data.frame(foo=1:4, bar=c(T,T,F,F))
print(x)
print(nrow(x))
print(ncol(x))

## Names of R objects
x <- c(1:3)
print(names(x))
names(x) <- c("foo", "bar", "norf")
print(names(x))

## Names in Matrices
x <- matrix(1:4, nrow=2, ncol=2)
dimnames(x) <- list(c("a", "b"), c("c", "d"))
print(x)


## Subsetting
## Subsetting a Vector
x = c('a','b','c','d','e')
print(x[1])
print(x[2])
print(x[2:4])
print(x[x > 'a'])
u <- x>'a'
print(u)
print(x[u])

##Subsetting a Matrix
m = matrix(1:6, 2,3)
print(m[1,2])
print(m[2,1])
print(m[1,])
print(m[,2])

##If you want to return a matrix
print(m[1,2,drop=FALSE])

##Subsetting Lists
x <- list(foo=1:6, bar=0.6, baz="Hello")
print(x[1])
print(x[[1]])
print(x$bar)
print(x["bar"])

##Subsetting nested elements of a list
x <- list(a=list(10,12,14), b=c(13.04,1.21))
print(x[[c(1,3)]])
print(x[[1]][[3]])


##Partial Matching
x <- list(aardwark=1:5)
print(x$a)
print(x[["a", exact=FALSE]])

##Remove na values
print("Removing NA values")
x <- c(1,2,NA, 3, NA, 5,6)
bad <- is.na(x)
print(bad)
print(x[!bad])

##Use complete.cases to remove missing values from multiple lists and dataframes
x=c(1, 2, 3, NA, 5, NA)
y=c(NA, 2, 3, 4, NA, NA)
good <- complete.cases(x,y)
print(good)

##dput ing R objects
y <- data.frame(a=1, b="a")
print(dput(y))

dput(y, file="y.R")
new.y <- dget("y.R")
print(new.y)

##dump ing R objects
x <- "foo"
y <- data.frame(a=1, b="Hello")
dump(c("x", "y"), file="data.R")
rm(x,y)
source("data.R")
print(y)
