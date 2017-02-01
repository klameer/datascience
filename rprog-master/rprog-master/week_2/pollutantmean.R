pollutantmean <- function(directory, pollutant, id = 1:332){
  totalList = c()
  for (x in id){
    df <- read.csv(getFileName(directory, x))
    fileList <- df[!is.na(df[pollutant]), pollutant]
    totalList <- append(totalList, fileList)
  }
  round(mean(totalList),3)
}

getFileName <- function(directory, x){
  x <- paste(c("00", toString(x)), collapse="")
  x <- substr(x, nchar(x)-2, nchar(x))
  x <- paste(c(directory, "/", x, ".csv"), collapse="")
  x
  
}
