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
	- **Writing**: present the scatter data with colors.
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
- **Wed Nov 16 13:39:42 CET 2016**	- Discussion with Niels:
		- kNN with 1 cluster always give very accurate result, why?
		- Is it possible to do k-fold cross validation for multiple variate?
	- **Presentation:** For the start, explain the dataset that was used.
	- ANN is the most sophisticated models, and it should give the least error.
	- Powerful package for machine learning
		- https://cran.r-project.org/web/packages/e1071/e1071.pdf
	- Cross validation result is similar with the predicted squared mean error?
	- Nice article about cross validation:
		- https://www.r-bloggers.com/cross-validation-for-predictive-analytics-using-r/
	- **Presenting**: use the graph of prediction error to estimate the error.
		- also for cross validation.

- **Thu Nov 17 12:06:07 CET 2016**
	- Continue learnig about tuning regression.
	- **Cross validation** in R:
		- http://www.katrinerk.com/courses/r-worksheets/r-code-classification-and-cross-validation
		- https://www.analyticsvidhya.com/blog/2015/11/improve-model-performance-cross-validation-in-python-r/
	- In ideal situation, the sum up of k-fold cross validation should be zero.
	- How to measure **bias** and **variance**:
		- Bias: the agerage of error
		- Variance: the average of std deviation
	- **Presenting**: show this graph
		- LOOCV
		- 10 fold cross validation
		- prediction error.
	- Create custom script for thecross validation.
	- The hat of the function indicates that it is an estimation.	- Found a book from Ricky Ho that summarizes the machine learning algorithm.		- http://blog.revolutionanalytics.com/2012/08/cheat-sheet-for-prediction-and-classification-models-in-r.html	- SVM parameters:		- http://www.svms.org/parameters/
	- Comparison of error:
		- http://stats.stackexchange.com/questions/110999/r-confused-on-residual-terminology- **Fri Nov 18 11:35:27 CET 2016** 	- Lasso regression:		- http://stats.stackexchange.com/questions/72251/an-example-lasso-regression-using-glmnet-for-binary-outcome	- Another:
		- https://www.r-bloggers.com/cross-validation-estimating-prediction-error/
		- https://rstudio-pubs-static.s3.amazonaws.com/2897_9220b21cfc0c43a396ff9abf122bb351.html
	- List of available train method in `caret` package:
		- https://rdrr.io/cran/caret/man/models.html
	- Nice example of how to do data analysis in R:
		- https://www.kaggle.com/c/overfitting/forums/t/456/modelling-algorithms-in-r/2787
	- Why squared error is preferred in statistics:
		- http://www.benkuhn.net/squared
		
- **Sat Nov 19 15:20:05 CET 2016**
	- Another blogpost for cross validation:
		- http://www.milanor.net/blog/cross-validation-for-predictive-analytics-using-r/
	- For doing the cross validation:
		- http://stats.stackexchange.com/questions/61090/how-to-split-a-data-set-to-do-10-fold-cross-validation
		
		```
		require(caret)
flds <- createFolds(y, k = 10, list = TRUE, returnTrain = FALSE)
names(flds)[1] <- "train"
		```
	- Functions in R:
		- https://www.r-bloggers.com/how-to-write-and-debug-an-r-function/
		- http://www.statmethods.net/management/userfunctions.html

- **Sun Nov 20 15:41:53 CET 2016**
	- Use `caret` class for training, specifically the method `train`, documentation:
		- http://artax.karlin.mff.cuni.cz/r-help/library/caret/html/train.html
	- Documentation for training and tuning in `caret`:
		- https://topepo.github.io/caret/model-training-and-tuning.html
		- https://topepo.github.io/caret/available-models.html (available models)
	- Machine Learning evaluation in R:
		- http://machinelearningmastery.com/machine-learning-evaluation-metrics-in-r/

November #4
-----------
- **Mon Nov 21 10:50:10 CET 2016**
	- Working on the slides, all models and validations.

- **Tue Nov 22 10:54:51 CET 2016**
	- Working on the paper of research internship.
	- Call Niels:
		- Explain the condition of time related dataset, says that it is possibly hard to extract social density data.
	- Patents about counting crowd:
		- https://worldwide.espacenet.com/publicationDetails/biblio?FT=D&date=20081211&DB=EPODOC&locale=nl_NL&CC=WO&NR=2008150170A2&KC=A2
		- https://www.google.com/patents/US20160315682
		
- **Wed Nov 23 11:04:21 CET 2016**
	- GLMnet practical documentation:
		- https://web.stanford.edu/~hastie/glmnet/glmnet_alpha.html
		- https://cran.r-project.org/web/packages/glmnet/glmnet.pdf (official documentation)
	- Add error bar in `ggplot`:
		- http://www.cookbook-r.com/Graphs/Plotting_means_and_error_bars_(ggplot2)/
	- **Writing**: explain how model selection works, from wide scope of parameter grid search (by exponential cost and not so precise epsilon) and then go deeper.
		- Show every graph
		- Compare the svm kernel in bar graph
	- SVM tuning result:
	
	```
	Parameters:
   SVM-Type:  eps-regression 
 SVM-Kernel:  radial 
       cost:  5 
      gamma:  0.25 
    epsilon:  0.3
    > mean(svm.accuracy)
	[1] 11.86627
	
	Parameter tuning of 'svm':
	sampling method: 10-fold cross validation 
	best parameters:
 	epsilon cost gamma
    0.02    1   0.4
	best performance: 173.8295
	> mean(svm.accuracy)
	[1] 12.03 
	```
	
	- Difference between `nu-regression` and `eps-regression` (and turns out also summary for SVM):
		- http://wiki.eigenvector.com/index.php?title=Svm#epsilon-SVR_and_nu-SVR
		- basically `nu` or `eps` are penalty parameters.
	- **Writing**: Also mention the starting search value for grid search of SVM.
	- Make sure the `seed` is always set.

- **Thu Nov 24 09:50:58 CET 2016**
	- Working on the model.
	- Got Warning: `WARNING: reaching max number of iterations`.
	- **Writing**: explain the best parameters for all kernels in svm.
		- Use notes in the block note.
		
- **Fri Nov 25 03:04:17 CET 2016**
	- Call Niels:
		- Report that a warning received: `WARNING: reaching max number of iterations`.
	- Different between nu and eps:
		- http://www.csie.ntu.edu.tw/~cjlin/papers/newsvr.pdf
		- https://www.quora.com/What-are-the-advantages-of-choosing-the-v-nu-SVM-formulation-VS-epsilon-SVM
	- Easy (seems like) explanation of SVM:
		- http://www.statsoft.com/Textbook/Support-Vector-Machines
	- **Writing tips**: present the figure with colors, e.g., orange for data dots and line, blue for the vertical bars, with dashed purple color line to mark the best value
	- Std dev and std error:
		- https://www.r-bloggers.com/standard-deviation-vs-standard-error/

- **Sat Nov 26 10:38:23 CET 2016**
	- Preparing for the presentation.
	- **Writing**: why we extract audio data to RMS, PKLV and Speaker count.
	- Residual plots:
		- http://blog.minitab.com/blog/adventures-in-statistics/why-you-need-to-check-your-residual-plots-for-regression-analysis
	- Errors comparison in regression and model assessment:
		- https://people.duke.edu/~rnau/compare.htm
		- http://www.theanalysisfactor.com/assessing-the-fit-of-regression-models/
		- http://stats.stackexchange.com/questions/56302/what-are-good-rmse-values
	- The effect of `cost` parameter in SVM:
		- http://stats.stackexchange.com/questions/31066/what-is-the-influence-of-c-in-svms-with-linear-kernel
	- A lecture explaining how SVM works:
		- http://www.robots.ox.ac.uk/~az/lectures/ml/lect2.pdf
	- **Writing**: explain the effect of noisy data that will decrease the accuracy of the model.

- **Sun Nov 27 16:12:20 CET 2016**
	- Working on the slides for monday's meeting.

November #5
-----------
- **Mon Nov 28 22:25:05 CET 2016**
	- Meeting with prof Aiello and prof Kas:
		- Now it's time to wrap up.
		- **Writing **: plot the error graph in each of the simulation (may be in result chapter), i.e., predicted vs actual value.
		- discussion: explain in what situation this method works well
			- location problem
			- timing problem
			- ambient sound discussion
		- future work: explain different settings, or using classification instead of regression.
	- Proposed table of contents:
	
	```
		- Introduction and background
			- background
			- research question
		- Related work and backgorund
			- wifi based crowd counting
				- probe request
			- bluetooth based crowd counting
			- mac address randomization
			- other crowd counting method
		- experimental setup
			- mac address randomization setuo
			- wifi experiment setup
				- measurements
				- location based				
				- timely based
		- modeling and validation
			- linear model
			- non linear model
		- results and discussion
			- the final result
			- interpretation and discussion
		- conclusion and future work
			- conclusion
			- future work
	```