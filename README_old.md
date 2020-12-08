## ENV859 Final Course Project
## Cristiana Falvo, November 2020
### Ship Traffic Exploration in Cape Cod Bay, MA

### Purpose: 
The purpose of this course project is to explore the shipping patterns in Cape Cod Bay, MA. 
This exploratory analysis will help in contextualizing the acoustic data that will
be used in my master's project. Since shipping is the primary source of underwater noise in Cape Cod Bay,
gaining a better understanding of the shipping traffic patterns in the bay should help gain a better 
understanding of the noise patterns. Understanding these patterns could ultimately help management decisions
related to shipping or conservation of species affected by underwater noise.

### Summary of Tasks:


-explores shipping traffic patterns in cape cod bay
-uses the near tool to at two points of interest in CCB
-
 
### Repository contents
 #### Scripts
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
				(need to draw out baby steps for this) .. tried a loop method, nogo
	- Jup_Near
		> (done)
			> imports arcpy, sets env to overwrite output
			> sets inputs
				+ ship points (ShipsCCB_cluster)
				+ ports (both are FCs I manually exported from a port I eyeballed to be at port)
					> PTown
					> Canal
			> runs Near analysis	
				~ two fields are added to input table
					> NearDist (= distance in meters from port)
						--> within search radius = value, outside radius = -1 (null)
					> NearFC (= the FC the point is within 100m from)
							
 
