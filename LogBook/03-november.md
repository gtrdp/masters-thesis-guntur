Timeline
--------
![alt tag](master-thesis-timeline.png)

LogBook
-------
- [August](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/00-august.md)
- [September](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/01-september.md)
- [October](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/02-october.md)
- [November](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/03-november.md)
- [December](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/04-december.md)
- [January](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/05-january.md)
- [February](https://github.com/gtrdp/masters-thesis-guntur/blob/master/LogBook/06-february.md)

November #1
-----------
- **Mon Oct 31 10:03:32 CET 2016**
	- Counting heads.
	- Extracting the data and creating graphs.
	
- **Tue Nov  1 20:08:01 CET 2016**
	- Call Niels:
		- Explain by conclusion, not using whole data
			- effect of day
			- effect of location
			- effect of scanning time
			- put it in a whole picture
			- signal strength: WiFi and probe request
		- Explain the MAC address randomization.
		- Working on decibels.
			- https://support.biamp.com/General/Audio/Peak_vs_RMS_Meters
			- **Important, writing**: also address the microphone sensitivity.
			- https://support.biamp.com/General/Audio/Microphone_sensitivity
			- Sound level decreases by 6dB with each doubling of distance from the source.
			- The sound is already using ambient noise reduction.
			- Those microphones are attuned to a specific (and rather narrow) range of sound intensity.
		- Found a magazine that explain the microphone sensitivity.

- **Wed Nov  2 12:06:43 CET 2016**
	- Working on getting the RMS and the Peak level using SoX.
	- Please try to make your working hours more productive.
	- Work on the conference paper.
	- Most modern microphone has built in ambient noise reduction.

- **Thu Nov  3 12:08:23 CET 2016**
	- Working on the slide.

- **Fri Nov  4 10:14:20 CET 2016**
	- Was not a productive day.
	
- **Sat Nov  5 10:14:20 CET 2016**
	- Kajian Tafsir.
	- Acara Didin.
	
- **Sun Nov  6 10:14:20 CET 2016**
	- Hoogezand.
	- Delfzijl.	

November #2
-----------
- **Mon Nov  7 10:14:20 CET 2016**
	- Presentation:
		- Work on the modeling of the data.
		
- **Tue Nov  8 10:14:20 CET 2016**
	- Working on the conference paper.
	
- **Wed Nov  9 10:14:20 CET 2016**
	- Delfzijl.
	- Working on the conference paper.
	
- **Thu Nov 10 14:11:35 CET 2016**
	- Looking for theoretical background for the data.
		- Bootstrapping
		- cross validation
		- machine learning

- **Fri Nov 11 14:23:08 CET 2016**
	- Learning about cross validation and statistics
		- https://www.cs.tau.ac.il/~nin/Courses/NC05/pr_l13.pdf (good example of cross validation)
	- also use time as a benchmarking paramaters to compare classifiers.
	- **Overfitting**: common problem if the parameters are large.
	- Email from Niels:
	
	> http://statweb.stanford.edu/~tibs/ElemStatLearn/
> This al you need to understand machine learning, bootstrap and cross validation. Do not try to understand the theory behind al the model but try to find some model that are suitable for your data set. Next you’ll need to find a way to validate your model, most likely by bootstrapping or cross validation. 
> The book also has some practical examples. For your one ease, try to use R. R has allot of packages for machine learning and requires minimum effort in very flexible coding environment.

	- As a rule of thumb, several hundred re-samples will be sufficient for most problems
	- For resampling:
		- http://stackoverflow.com/questions/3674409/numpy-how-to-split-partition-a-dataset-array-into-training-and-test-datasets
	- Nice article, different between machine learning and statistical modeling
		- https://www.analyticsvidhya.com/blog/2015/07/difference-machine-learning-statistical-modeling/
	- Good article to choose the estimator (algorithm), from scikit learn:
		- http://scikit-learn.org/stable/tutorial/machine_learning_map/
	- A sort of rule of thumb:
		- quantitative, continuous result: regression
		- classes, discrete result: classification
		
- **Sat Nov 12 13:51:01 CET 2016**
	- creating the graph with color
		- also plot the timely grotemarkt with the db graphs
		- add location parameters to the global data dump: just combine the separated dumps.
	- starting coding with machine learning
	- beginnin using R
	- Good summary of machine learning algorithm
		- machine learning regression algorithms for biophysical parameter retrieval
	- regression with multiple variable:
		- http://www.psychstat.missouristate.edu/multibook/mlt07.htm
		- http://onlinestatbook.com/2/regression/multiple_regression.html
		- http://www.stat.yale.edu/Courses/1997-98/101/linmult.htm
- **Sun Nov 13 12:00:20 CET 2016**
	- **Writing**: explain the data analysis using three-way data splits.
	- **Presenting**: to present data, use the square representation as in the machine learning seitosa dataset.
		- named scatterplot matrix.
	- possible models:
		- linear
		- poliniear
	- Useful bookmarks:
		- http://www.stat.columbia.edu/~martin/W2024/R6.pdf
		- http://www.statmethods.net/stats/regression.html
		- https://www.r-bloggers.com/r-tutorial-series-multiple-linear-regression/
		- https://www.r-bloggers.com/r-tutorial-series-simple-linear-regression/
		- https://www.r-bloggers.com/r-tutorial-series-basic-polynomial-regression/
		- http://www.statmethods.net/graphs/scatterplot.html
		- http://onlinestatbook.com/2/regression/intro.html
	- installing R and R Studio

November #3
-----------
- **Mon Nov 14 11:55:02 CET 2016**
	- Working on the R.
	- data table cheat sheet
		- https://s3.amazonaws.com/assets.datacamp.com/img/blog/data+table+cheat+sheet.pdf
	- getting used to R environment and programming.
	- possible models:
		- using different multivariate

- **Tue Nov 15 11:33:49 CET 2016**
	- learn about non linear regression in R
	- cross validation using multiple explanatory variable.
	- nice article about non linear regression in R
		- http://machinelearningmastery.com/non-linear-regression-in-r/
		- http://www.svm-tutorial.com/2014/10/support-vector-regression-r/ (tuning the svm)
	- From the book from Niels, page 465:
		> Because it uses only the training point closest to the query point, the bias of the 1-nearest-neighbor estimate is often low, but the variance is high. A famous result of Cover and Hart (1967) shows that asymptotically the error rate of the 1-nearest-neighbor classifier is never more than twice the Bayes rate. The rough idea of the proof is as follows (using squared-error loss). We assume that the query point coincides with one of the training points, so that the bias is zero. This is true asymptotically if the dimension of the feature space is fixed and the training data fills up the space in a dense fashion. Then the error of the Bayes rule is just the variance of a Bernoulli random variate (the target at the query point), while the error of 1-nearest-neighbor rule is twice the variance of a Bernoulli random variate, one contribution each for the training and query targets.
- **Wed**	- Discussion with Niels:
		- kNN with 1 cluster always give very accurate result, why?
		- Is it possible to do k-fold cross validation for multiple variate?	
November #4
-----------

November #5
-----------