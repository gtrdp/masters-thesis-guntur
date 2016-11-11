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
	- creating the graph with color
		- also plot the timely grotemarkt with the db graphs
		- add location parameters to the global data dump: just combine the separated dumps.
	- starting coding with machine learning
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

November #3
-----------

November #4
-----------

November #5
-----------