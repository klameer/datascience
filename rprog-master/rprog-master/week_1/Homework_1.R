csv <- read.csv("hw1_data.csv")
print(names(csv)
head(csv)
tail(csv)
nrow(csv)
csv[[47]][[1]]
csvComplete <- complete.cases(csv$Ozone, csv$Temp, csv$Solar.R)
mean(csv$Solar.R[csvComplete])
max(csv$Ozone[complete.cases(csv$Month, csv$Ozone) & csv$Month == 5])