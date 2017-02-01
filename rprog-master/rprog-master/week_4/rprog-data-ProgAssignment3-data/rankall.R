setwd("C:/Users/Karim/SkyDrive/Documents/codebase/Coursera Data Science/rprog/Week_4/rprog-data-ProgAssignment3-data")

rankall <- function(outcome, num="best"){
  ## Read the outcome data
  data <- read.csv("outcome-of-care-measures.csv", colClasses="character")
  data <- data[, c(2,7,11,17,23)]
  data[, 3] <- as.numeric(data[, 3])
  data[, 4] <- as.numeric(data[, 4])
  data[, 5] <- as.numeric(data[, 5])
  names(data) <- c("name", "state", "heart_attack", "heart_failure", "pnuemonia")
  
  ## Check that the state and outcome are valid
  valid_outcomes <- c("heart attack", "heart failure", "pneumonia")
  if(!outcome %in% valid_outcomes){
    stop("invalid outcome")
  }
  
  if(!num %in% c("best", "worst") & !is.numeric(num)){
    stop("invalid ranking")
  }
  
  ## Handle numeric ranking for best and worst
  if(num=="best"){num=1}
  if(num=="worst"){num=999}
  
  ## For each state find the outcome of the given rank
  dfFinal <- data.frame(hospital=character(), state=character())
  
  ### Get a unique list of states
  state_list <- unique(data[, "state"])
  
  ### Get data set after outcome selection
  if(outcome == "heart attack"){
    outcome_num <- 3
  }
  else if(outcome == "heart failure"){
    outcome_num <- 4
  }
  else if(outcome == "pneumonia"){
    outcome_num <- 5
  }
  
  for (state in state_list){
    dfRecord <- data.frame(hospital=helper(data, outcome_num, num, state), state=state)
    dfFinal <- rbind(dfFinal, dfRecord)
  }
  
  ## Return a data frame with the hospital name and the 
  ## (abbreviated) state name
  dfFinal <- dfFinal[order(dfFinal["state"]),]
  return(dfFinal)
  
}

helper <- function(data, outcome_num, num, state){
  
  # Filter out only relevant outcome and relevant state
  data <- data[, c(1, 2, outcome_num)]
  data <- data[data$state == state,]
  
  data <- data[!is.na(data[,3]),] 
  if(num == 999){
    num = nrow(data)
  }
  data <- data[order(data[,3], data$name),]
  hosp_name <- data[num, "name"]
  return(hosp_name)
}

# tests
#head(rankall("heart attack", 20), 10)
#tail(rankall("pneumonia", "worst"), 3)
#tail(rankall("heart failure"), 10)
