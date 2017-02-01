setwd("C:/Users/Karim/SkyDrive/Documents/codebase/Coursera Data Science/rprog/Week_4/rprog-data-ProgAssignment3-data")

best <- function(state, outcome){
  
  # Open data set
  data <- read.csv("outcome-of-care-measures.csv", colClasses = "character")

  # Prepare data set
  data[, 11] = as.numeric(data[, 11])
  data[, 17] = as.numeric(data[, 17])
  data[, 23] = as.numeric(data[, 23])
  data <- data[, c(2,7,11,17,23)]
  names(data) <- c("name", "state", "heart_attack", "heart_failure", "pneumonia")
  
  valid_outcomes <- c("heart attack", "heart failure", "pneumonia")

  if(!state %in% data$state){
    stop("invalid state")
  }
  
  if(!outcome %in% valid_outcomes){
    stop("invalid data")
  }
  
  # As there are no parameter errors the processing can take place
  # Filter out only relevant state data
  data <- data[data$state == state,]
  
  if (outcome == "heart attack"){
    #Get Minimum 
    iMin <- min(data[,3], na.rm=TRUE)
    hosp_name <- data[which(data$heart_attack == iMin),]["name"]
  }
  
  if (outcome == "heart failure"){
    #Get Minimum 
    iMin <- min(data[,4], na.rm=TRUE)
    hosp_name <- data[which(data$heart_failure == iMin),]["name"]
  }
  
  if (outcome == "pneumonia"){
    #Get Minimum 
    iMin <- min(data[,5], na.rm=TRUE)
    hosp_name <- data[which(data$pneumonia == iMin),]["name"]
  }
  
  return(as.character(hosp_name))
  
}

