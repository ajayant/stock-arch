import csv; import riak ; from riak import RiakClient;

print("\nWelcome to Google Stock Archive")
print("Ente name of document in current directory to be archived in Riak")

y = raw_input()
	
file1 = open(y , "r")
reader = csv.reader(file1)

client= RiakClient()
my_bucket = client.bucket('Stock Data')


for row in reader: 
	list = {'Date' : row[0] ,
					'Open' : row[1] ,
					'High' : row[2] ,
					'Low'  : row[3] ,
					'Close': row[4] ,
					'Volume' : row[5] ,
					'Adj Close' : row[6] }
		
	x = my_bucket.new(data = list)
	x.store()

print("Please Enter Date in following format\nYYYY-MM-DD:")
val = raw_input()
count = 0

for key in my_bucket.get_keys():
	if(val == my_bucket.get(key).data['Date']):
		print(my_bucket.get(key).data)
		count = 1
		break

if (count == 0) :
	print "invalid date"

