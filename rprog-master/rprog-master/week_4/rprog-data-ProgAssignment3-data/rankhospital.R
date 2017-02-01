setwd("C:/Users/Karim/SkyDrive/Documents/codebase/Coursera Data Science/rprog/Week_4/rprog-data-ProgAssignment3-data")

rankhospital <- function(state, outcome, num="best"){
  ## Read outcome data
  data <- read.csv("outcome-of-care-measures.csv", colClasses="character")
  
  ## Prepare data
  data[,11] <- as.numeric(data[,11])
  data[,17] <- as.numeric(data[,17])
  data[,23] <- as.numeric(data[,23])
  
  data <- data[, c(2, 7, 11, 17, 23)]
  names(data) <- c("name", "state", "heart_attack", "heart_failure", "pneumonia")
  
  
  ## Check that state and outcome are valid
  valid_outcomes <- c("heart attack", "heart failure", "pneumonia")
  
  if(!state %in% data$state){
    stop("invalid state")
  }
  
  if(!outcome %in% valid_outcomes){
    stop("invalid outcome")
  }
  
  if(!num %in% c("best", "worst") & !is.numeric(num)){
    stop("invalid ranking")
  }
  
  ## handle best and worst
  if(num == "best"){
    num = 1
  }
  else if(num == "worst"){
    num = 999
  }
  
  ## Return hospital name in that state with the given rank
  ## 30-day death rate
  ### subset state
  
  data <- data[data$state == state,]
  
  if(outcome == "heart attack"){
    hosp_name <- helper(data, 3, num)
  }
  
  if(outcome == "heart failure"){
    hosp_name <- helper(data, 4, num)
  }
  
  if(outcome == "pneumonia"){
    hosp_name <- helper(data, 5, num)
    
  }
  
  return(hosp_name)
}

# helper function to shorten the code

helper <- function(data, outcome_num, num){
  
  # Filter out only relevant outcome
  data <- data[, c(1, 2, outcome_num)]
  data <- data[!is.na(data[,3]),] 
  if(num == 999){
    num = nrow(data)
  }
  data <- data[order(data[,3], data$name),]
  hosp_name <- data[num, "name"]
  return(hosp_name)
}

# test
#rankhospital("TX", "heart attack", 5)
rankhospital("TX", "heart failure", 4)
