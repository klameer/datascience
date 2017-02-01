testMe <- function(outcome){
  
  valid_outcomes <- c("heart attack", "heart failure", "pneumonia")
  
  if (!outcome %in% valid_outcomes){
    stop ("invalid outcome")
    
  } else{
    result <- "in else"
  }
  
  return(result)
    
}


# tests
print(testMe("heart attack"))