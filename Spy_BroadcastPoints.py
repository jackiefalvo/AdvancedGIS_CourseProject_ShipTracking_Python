#################
# AIS data in arcpy, take 1
# Friday 10/23
#################
#%% set up
import arcpy, os, sys

arcpy.env.workspace = r"V:\CourseProject\Data\Zone19_2014_01.gdb"
arcpy.env.overwriteOutput = True
wkspace = "V:\CourseProject\Data\Zone19_2014_01.gdb" # est this for update cursor (edit sesh)

broadcast = r"Zone19_2014_01_Broadcast"
# voyage = r"V:\CourseProject\Scratch\voyage35.shp"

#%% broadcast data
arcpy.ListFeatureClasses() # fcs in our workspace (2014 gdb)

# describe data
desc_bc = arcpy.Describe(broadcast)
#desc_v = arcpy.Describe(voyage)

## broadcast points info via describe function
# print(desc_bc.featureType)
# print(desc_bc.shapeType)
# print(desc_bc.hasSpatialIndex)
# print(desc_bc.name)
# print(desc_bc.dataType)
# print(desc_bc.catalogPath)

# number of records
broadcast_count = arcpy.GetCount_management(broadcast)

# field names 
fields_bc = arcpy.ListFields(broadcast)

for field in fields_bc:
    print(field.name)
    
print(f"There are {broadcast_count} records in the broadcast points shapefile.")

#%% search cursor - broadcast points
# create new field in broadcast points fc
arcpy.AddField_management(broadcast, 'SpeedingStatus', 'TEXT')

# fields of interest
fields = ['MMSI', 'VoyageID', 'SOG', 'SpeedingStatus']

# Create a cursor (this is like opening a file)
rows = arcpy.da.SearchCursor(broadcast, fields)

# voyage35 list
voyage35 = []

# how many points are in voyage 35?
for record in rows:
    
    MMSI = record[0]
    VoyageID = record[1]
    Speed = record[2]
    
    # add all points with Voyage ID 35 to a list (probs would be better to copy feat class)
    if VoyageID == 35:
        voyage35.append(record)
    
    else:
        pass
        
print("There are", len(voyage35), "points in voyage 35") 

del rows
        
#%%
# flag speeding ships
cursor = arcpy.da.UpdateCursor(broadcast, fields)

# counts
count1 = 0 # speeding
count2 = 0 # not speeding
count3 = 0 # unknown

# start edit session
with arcpy.da.Editor(wkspace) as edit:
    
    # distinguish speeding from not speeding
    for row in cursor:
        
        # establish fields
        SpeedingStatus = row[3]
        Speed = row[2]
        
        # 
        if Speed > 10:
            SpeedingStatus == 'Yes'
            count1 += 1
            
        elif Speed <= 10:
            SpeedingStatus == 'No'
            count2 += 1
            
        else:
            SpeedingStatus == 'Unknown'
            count3 += 1
        
# delete cursor once done
del cursor

print(count1, "ships speeding,", count2, "compliant,", count3, "unknown")

#%%
# select subset of vessels that
    # travel through canal
    # hit Ptown
    
# how:
    # create / draw polygon in canal (or just determine bounding box and use those as conditions..)
