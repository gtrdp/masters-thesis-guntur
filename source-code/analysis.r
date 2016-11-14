all_global_data <- read.table("global-dump.txt",
                   header = TRUE,
                   sep="\t", 
                   col.names=c("ap", "pr","au", "gt",
                               "rms", "pklv", "rssi", "snr", "loc"), 
                   fill=FALSE, 
                   strip.white=TRUE)

global_data <- all_global_data[c("ap", "pr", "gt", "rms", "pklv", "rssi")]

plot(global_data)
summary(lm(gt~pr))
summary(lowess(gt~pr))

# model1
model1 <- lm(gt~ap+rms+pklv+rssi, global_data)
summary(model1)

# model2
model2 <- lm(pr~ap+rms+pklv+rssi, global_data)
summary(model2)

# model3
model3 <- lm(gt~ap+rms+pklv, global_data)
model3
summary(model3)

# cross validation
library(DAAG)
cv.lm(data=global_data, model1, m=10)
cv.lm(data=global_data, model2, m=10)
cv.lm(data=global_data, model3, m=10)
