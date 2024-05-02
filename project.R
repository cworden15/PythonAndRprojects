df <- read.csv("~/Downloads/GDP.csv")
df1 <- read.csv('~/Downloads/CO2_emission.csv') 
#----------year 1990------------------------------------------------------------
plot(x = df$X1990,y = df1$X1990,
     xlab = "GDP",
     ylab = "CO2 Emissions",
     main = "1990"
)
max(df1$X2000, na.rm = TRUE)  
abline(lm(df1$X1990 ~ df$X1990)) 
lm(df1$X1990 ~ df$X1990)
cor(df$X1990,df1$X1990,use = "complete.obs")



#--------year 1995--------------------------------------------------------------
plot(x = df$X1995,y = df1$X1995,
     xlab = "GDP",
     ylab = "CO2 Emissions",
     main = "1995"
)
barplot(df$X1995,ylim = c(0, 100000))
abline(lm(df1$X1995 ~ df$X1995)) 
lm(df1$X1995 ~ df$X1995)
cor(df$X1995,df1$X1995,use = "complete.obs")

#---------------2000------------------------------------------------------------
plot(x = df$X2000,y = df1$X2000,
     xlab = "GDP",
     ylab = "CO2 Emissions",
     main = "2000"
)
max(df$X2010)
abline(lm(df1$X2000 ~ df$X2000)) 
lm(df1$X2000 ~ df$X2000)
cor(df$X2000,df1$X2000,use = "complete.obs")




#---------------2005------------------------------------------------------------
plot(x = df$X2005,y = df1$X2005,
     xlab = "GDP",
     ylab = "CO2 Emissions",
     main = "2005"
)

abline(lm(df1$X2005 ~ df$X2005)) 
lm(df1$X2005 ~ df$X2005)
cor(df$X2005,df1$X2005,use = "complete.obs")

#---------------2010------------------------------------------------------------
plot(x = df$X2010,y = df1$X2010,
     xlab = "GDP",
     ylab = "CO2 Emissions",
     main = "2010"
)
abline(lm(df1$X2010 ~ df$X2010)) 
lm(df1$X2010 ~ df$X2010)
cor(df$X2010,df1$X2010,use = "complete.obs")


#---------------2015------------------------------------------------------------
plot(x = df$X2015,y = df1$X2015,
     xlab = "GDP",
     ylab = "CO2 Emissions",
     main = "2015"
)
abline(lm(df1$X2015 ~ df$X2015)) 
lm(df1$X2015 ~ df$X2015)
cor(df$X2015,df1$X2015,use = "complete.obs")


#---------------2018------------------------------------------------------------
plot(x = df$X2018,y = df1$X2018,
     xlab = "GDP",
     ylab = "CO2 Emissions",
     main = "2018"
)
abline(lm(df1$X2018 ~ df$X2018)) 
lm(df1$X2018 ~ df$X2018)
cor(df$X2018,df1$X2018,use = "complete.obs")



mean(df$X1990,na.rm=TRUE)
mean(df$X1995,na.rm=TRUE)
mean(df$X2000,na.rm=TRUE)
mean(df1$X1990,na.rm=TRUE)
mean(df1$X1995,na.rm=TRUE)
mean(df1$X2000,na.rm=TRUE)
mean(df$X2005,na.rm=TRUE)
mean(df1$X2005,na.rm=TRUE)
mean(df$X2010,na.rm=TRUE)
mean(df1$X2010,na.rm=TRUE)
mean(df$X2015,na.rm=TRUE)
mean(df1$X2015,na.rm=TRUE)
mean(df$X2019,na.rm=TRUE)
mean(df1$X2019,na.rm=TRUE)
