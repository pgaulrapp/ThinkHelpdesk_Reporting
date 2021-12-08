import MySQLdb
import sys
import csv
from datetime import datetime
from datetime import timedelta

LocationID = sys.argv[1]

db = MySQLdb.connect(host="localhost",user="root",passwd="am272!zop",db="mojo")
cur = db.cursor()

#open the CSV file. The CSV file is uploaded from another computer. A shell script wrapper will check for its existence :
#We want the ticket id, the create date, the user's email, the summary, description, room, school, the assigned agent, closed on date, the category, and then the star rating and star comment 1 field, for the survey stuff.

FieldsWeWant = ['TICKETID','CREATED_DATE','END_USER_EMAIL','ISSUE_TITLE','ISSUE_DETAIL','ROOM','SCHOOL','ASSIGNED','DATE_COMPLETED','CATEGORY','STARRATE1','STARCOMMENT1']

#Get headers:
with open('/home/phil/cch/uploads/ThinkHelpDeskTest.csv') as CSVFile:
	LineReader = csv.reader(CSVFile)
	Headers = next(LineReader)
	HeaderIndices = []
	for Header in Headers:
		#We want to know where the header fields live in the document in case the programmers add fields later on:
		for Field in FieldsWeWant:
			if Field == Header:
				HeaderIndex = Headers.index(Header)
				HeaderIndices.append(HeaderIndex)

	LineReader = csv.reader(CSVFile)
	for ContentRow in LineReader:
		#for ContentField in HeaderIndices:
		CreatedOn = ContentRow[HeaderIndices[1]]
		Email = ContentRow[HeaderIndices[2]]
		Rating = ContentRow[HeaderIndices[10]]
		Comment = ContentRow[HeaderIndices[11]]
		if Rating != "":
			if Rating > 7:
				Rating = "Very Satisfied"
			elif Rating == 5 or Rating == 6:
				Rating = "Satisfied"
			elif Rating < 5:
				Rating = "Less Than Satisfied"
			print CreatedOn
			print Email
			print Rating
			print Comment
			print ""

#print(HeaderIndices)
