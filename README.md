# TwitterConsensusAnalysis
Used data mining tool to analyze the correlation between tweets public opinion and real event (the 89th Academy Awards), including related tweets collection (web crawler by Tweepy), tweets pre-processing (NLTK) and sentiment analysis using Naive Bayes (NLTK).

Twitter provides convenient access to its huge amount of data to its developers and researchers through several Twitter API. This project used Tweepy to access Twitter API in data collection.

According to Twitter Developer Policy, users who want to get access to Twitter API must firstly be an authorized user of Twitter. Meanwhile, the developer must register an application binding with his/her Twitter account. A token will be issued with the application to the developer so that she/he can get authority to Twitter API.

To increase the speed of data collection on Twitter, this project registered five applications. Meanwhile, Twitter also has rate limitat ion for API usage. Therefore, the project included sleep scheme in crawler program, and the process to collect all related data cost 16 days.

The file getFollowers.py is used to obtain all followers information of the Academy Awards official Twitter account. Authority is required before accessing the Twitter API.

The source code tweetsCollector.py is used to collect all tweets ever posted by these followers. Users’ tweets were stored in a local file. Each users's statuses_count and friends_count are recorded with tweets. There are several problems that need to pay attention here. First, Twitter requires that only authorized users' information can be collected, and an error will occur when crawler reach an unauthorized user. Meanwhile, rate limitation is also a problem. Finally, if the total number of connection to Twitter API exceed a pre-set number, API connection will be denied. All there problem should be considered seriously to avoid programming crash.

The source code consensusAnalysis.py implements a classifier based on Naive Bayer, including classifier training and tweets pre-processing. An example of moview Moonlight was given at the end of the program to show how the classifier works.

There is also a poster Twitter_Poster.pdf to demonstrate the overall structure and method of this project.
