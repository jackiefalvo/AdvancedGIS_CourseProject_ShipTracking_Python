# CourseProject
 ENV859 Ship Tracker
 Cristiana Falvo
 November 2020
 
# Repository contents
 Scripts
	- Spy-BroadcastPoints.py # spyder file, intial data exploration 
		> looks at broadcast points, isolates list of voyage 35 points, flags speeding ships
	- Jup_Broadcast.ipynb # jupyter nb, further analysis
		> (done) 
			> looks at broadcast points (#records, fields)
			> creates broadcast search cursor
			> counts number of records where voyageID = 35 (8,515 points)
		> (to do)
			> create output feature class of voyage 35
				> look at lat/lon and timestamps
				> spatial analysis (flag ships that cross Ptown - test for later)
			> summarize data, bigger picture
				> how many unique voyage IDs?
				> how many unique MMSIs? (^same?)
			> actual / end goal spatial analysis	
				> looking at allll broadcast points.. (maybe narrow to one week)
					> flag points that hit Ptown	
						> somehow flag/store voyage IDs
						> get count (how many voyages/MMSIs hit Ptown in X time pd)
							> visualize / plot this count, compare dif time pds?
	- Jup_PTown
		> (done)
			> create point object for Ptown
		> (to do)
			> if shipping points go within X dist of this point..flag as 'hit ptown'
				(need to draw out baby steps for this)
							
 
