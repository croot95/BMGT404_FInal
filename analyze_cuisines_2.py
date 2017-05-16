#!/usr/bin/python


import pandas as pd 

#create dataframe column names
col_names = ['Cuisine' , 'Avg Sentiment','Avg Rating','Restaraunts','Ratings']
#choose the file with the data
file_path = "/Users/christopherroot 1/Desktop/cuisines.csv"

#create a dataframe of the file
df = pd.read_csv(file_path, header = None, names = col_names)

#find mean and sdev for each metric
analyze_these = ['Avg Sentiment','Avg Rating','Restaraunts','Ratings']

for i in analyze_these:
	avg = df[i].mean()
	sdev = df[i].std()
	print i, "Avg: ", avg, "Sdev: ", sdev , "\n"

avg_rating = df["Ratings"].mean()
sdev_rating = df["Ratings"].std()
avg_sent = df["Avg Sentiment"].mean()
sdev_sent = df["Avg Sentiment"].std()


top_rating = []
top_sent = []

#find cuisines with above avg rating
for index, row in df.iterrows():
	if row["Ratings"] >= avg_rating:
		#add to list to compare with avg sentiment
		top_rating.append(row["Cuisine"])
		


#find cuisines with above avg sentiment
for index, row in df.iterrows():
	if row["Avg Sentiment"] >= avg_sent:
		#add to list to compare with avg rating
		top_sent.append(row["Cuisine"])
		
#see which cuisines have both above average sentiments and above average rating
in_both = []
for rest in top_sent:
	if rest not in top_rating:
		in_both.append(rest)
	

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
	if c in in_both and nt > 20:#at least 20 review
		top_cuisines.append(c)
		top_avg_sent.append(s)
		top_avg_rating.append(r)
		top_num_rest.append(nr)
		top_num_ratings.append(nt)
		
	else:
		continue
		

top_data_set = list(zip(top_cuisines,top_avg_sent,top_avg_rating,top_num_rest,top_num_ratings))

top_df = pd.DataFrame(data = top_data_set, columns= col_names)
#print "Here are all the above average cuisines for both sentiment and rating and ratings > 20: "

#print top_df

#create a dataframe of top 15 restaurants 

df_top15_sent = top_df.nlargest(15,'Avg Sentiment')
df_top15_rating = top_df.nlargest(15,'Avg Rating')

print " \n top 15 cuisines by rating:"
print df_top15_rating
print " \n top 15 cuisines by sentiment:"
print df_top15_sent

in_both_top = []
top_15_sent = []

for index, row in df_top15_sent.iterrows():
	top_15_sent.append(row["Cuisine"])

for index, row in df_top15_rating.iterrows():
	cytpe = row["Cuisine"]
	if cytpe  in top_15_sent:
		in_both_top.append(cytpe)

top_cuisines2 = []
top_avg_sent2 = []
top_avg_rating2 = []
top_num_rest2 =[]
top_num_ratings2 = []

for index, row in df.iterrows():
	c = row["Cuisine"]
	s = row["Avg Sentiment"]
	r = row["Avg Rating"]
	nr = row["Restaraunts"]
	nt = row["Ratings"]
	if c in in_both_top:
		top_cuisines2.append(c)
		top_avg_sent2.append(s)
		top_avg_rating2.append(r)
		top_num_rest2.append(nr)
		top_num_ratings2.append(nt)
		
	else:
		continue
final_data_set = list(zip(top_cuisines2,top_avg_sent2,top_avg_rating2,top_num_rest2,top_num_ratings2))
#cant get this to work
df_final = pd.DataFrame(data= final_data_set, columns = col_names)




print "\n Here are the cuisine types that appear in both the top 15 avg sentiment datframe and top 15 avg rating datframe:"


print df_final

#funtion to create a scoring method for rating and sentiment
def get_score(avg_r, avg_s):
	score = (.5 * avg_r) + (.5 * avg_s)
	return score

scores = []
score_list = []

for index, row in df_final.iterrows():
	a_r = row['Avg Rating']
	a_s = row['Avg Sentiment']
	c_score = get_score( a_r, a_s)
	score_list.append(row["Cuisine"])
	scores.append(c_score)

scores_dataset = list(zip(score_list, scores))

print "\ntop cuisines by score: "
df_scores = pd.DataFrame(data = scores_dataset, columns = ['Cuisines' , 'Score'])
print df_scores.sort('Score', ascending= False)









		


		




