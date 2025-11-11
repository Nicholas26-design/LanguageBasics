##Removes Duplicates from the dataframe
Responsibilities_df2 <- Responsibilities_df[!duplicated(Responsibilities_df[,c(1)]),]



Owning_Area_df <- as.data.frame(str_split_fixed(Summary_df$`DNB Errors - Owners`, ",", 5))
colnames(Owning_Area_df) <- c("OwningArea1","OwningArea2","OwningArea3","OwningArea4","OwningArea5")

 #######################



######### EMAIL ###########


library("devtools")

#install_github('omegahat/RDCOMClient')

install.packages('RDCOMClient', repos = 'http://www.omegahat.net/R/')

require(RDCOMClient)


OutApp <- COMCreate("Outlook.Application")
outMail = OutApp$CreateItem(0)
outMail[["To"]] = "first.last@ensemblehp.com; first.last@ensemblehp.com"
outMail[["subject"]] = "Adena ATB File"
outMail[["body"]] = "
       
insert text
         
        
       
 " 

outMail$Send() 


###### LOOPS IN R

https://www.datacamp.com/community/tutorials/tutorial-on-loops-in-r
