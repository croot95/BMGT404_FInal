#!/usr/bin/python


import pandas as pd 

#create dataframe column names
col_names = ['Cuisine' , 'Avg Sentiment','Avg Rating','Restaraunts','Ratings']
#choose the file with the data
file_path = "/Users/christopherroot 1/Desktop/cuisines.csv"

df = pd.read_csv(file_path, header = None, names = col_names)

#find mean and sdev for each metric

analyze_these = ['Avg Sentiment','Avg Rating','Restaraunts','Ratings']

for i in analyze_these:
	avg = df[i].mean()
	sdev = df[i].std()
	print i, " Avg: ", avg, " Sdev: ", sdev

avg_rating = df["Ratings"].mean()
sdev_rating = df["Ratings"].std()
avg_sent = df["Avg Sentiment"].mean()
sdev_sent = df["Avg Sentiment"].std()


top_rating = []
top_sent = []
#find cuisines with above avg rating
print "Here are all the cuisines with above average rating"
for index, row in df.iterrows():
	if row["Ratings"] >= avg_rating:
		top_rating.append(row["Cuisine"])
		print row["Cuisine"]
#find cuisines in top 33%
print "Here are all the cuisines with ratings greater than 1 sdev + mean:"
top_33 = avg_rating + sdev_rating
for index, row in df.iterrows():
	if row["Ratings"] >= top_33:
		print row["Cuisine"]


#find cuisines with above avg sentiment
print "Here are all the cuisines with above average sentiment"
for index, row in df.iterrows():
	if row["Avg Sentiment"] >= avg_sent:
		top_sent.append(row["Cuisine"])
		print row["Cuisine"]
#find cuisines in top 33%
print "Here are all the cuisines with sentiments greater than 1 sdev + mean:"
top_33_sent = avg_sent + sdev_sent
for index, row in df.iterrows():
	if row["Avg Sentiment"] >= top_33_sent:
		print row["Cuisine"]

#print a list of cuisines that are in top 50% of both avg rating and avg sent
in_both = []
for rest in top_sent:
	if rest not in in_both:
		in_both.append(rest)

list_len =  len(in_both)

print "Here is a list of " , list_len , " restaurants that are in both the top 50% of rating and sentiment: "
print in_both



top_cuisines = []
top_avg_sent = []
top_avg_rating = []
top_num_rest =[]
top_num_ratings = []
for index, row in df.iterrows():
	c = row["Cuisine"]
	s = row["Avg Sentiment"]
	r = row["Avg Rating"]
	nr = row["Restaraunts"]
	nt = row["Ratings"]
	if c not in in_both:
		continue
	else:
		top_cuisines.append(c)
		top_avg_sent.append(s)
		top_avg_rating.append(r)
		top_num_rest.append(nr)
		top_num_ratings.append(nt)

top_data_set = list(zip(top_cuisines,top_avg_sent,top_avg_rating,top_num_rest,top_num_ratings))

top_df = pd.DataFrame(data = top_data_set, columns= col_names)

print top_df
		


		




