complete <- function(directory, id=1:332){
  dfAll <- data.frame(id=integer(), nobs=integer())
  
  for (x in id){
    fSpecFile <- read.csv(getFileName(directory, x))
    dfFileDetails <- data.frame(id=x, nobs=sum(complete.cases(fSpecFile$sulfate, fSpecFile$nitrate)))
    dfAll <- rbind(dfAll, dfFileDetails)    
  }
  dfAll
}

getFileName <- function(directory, x){
  x <- paste(c("00", toString(x)), collapse="")
  x <- substr(x, nchar(x)-2, nchar(x))
  x <- paste(c(directory, "/", x, ".csv"), collapse="")
  x
}