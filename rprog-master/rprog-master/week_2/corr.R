corr <- function(directory, threshold=0){
  id=1:332
  dfAll = data.frame(ID=integer(), threshold=integer(), covariance=double())
  
  for (x in id){
    dfFile <- read.csv(getFileName(directory, x))
    dfFile <- dfFile[complete.cases(dfFile$sulfate, dfFile$nitrate),]
    t <- nrow(dfFile)
    c <- cor(dfFile$sulfate, dfFile$nitrate)
    dfFileDetails <- data.frame(ID=x, threshold=t, covariance=c)
    dfAll <- rbind(dfAll, dfFileDetails)
    
  }
  
  dfAll[dfAll$threshold>threshold, "covariance"]
}



getFileName <- function(directory, x){
  x <- paste(c("00", toString(x)), collapse="")
  x <- substr(x, nchar(x)-2, nchar(x))
  x <- paste(c(directory, "/", x, ".csv"), collapse="")
  x
}