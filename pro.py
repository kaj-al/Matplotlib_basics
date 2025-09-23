import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_titles.csv")

df = df.dropna(subset=['show_id','type','title','director','cast','country','date_added','release_year','rating','duration','listed_in','description'])

# Movies and shows comparison
type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['pink','blue'])
plt.title("Number of movies vs TV shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_shows.png")
plt.show()

# country wise distribution
country_counts = df['country'].value_counts().head()
plt.figure(figsize=(10,6))
plt.barh(country_counts.index, country_counts.values, color=['pink','blue'])
plt.title("Top countries")
plt.xlabel("Numbers")
plt.ylabel("Countries")
plt.tight_layout()
plt.savefig("countries.png")
plt.show()

# Release years of movies 
release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values,marker='o',color='pink')
plt.title("Release of movie")
plt.xlabel("Release year")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("release.png")
plt.show()

# Content per year
content_by_year = df.groupby(["release_year",'type']).size().unstack().fillna(0)
fig,ax = plt.subplots(1,2, figsize=(12,5))
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies released per year')
ax[0].set_xlabel('year')
ax[0].set_ylabel('number of movies')

ax[0].plot(content_by_year.index, content_by_year['TV Show'], color='red')
ax[0].set_title('Shows released per year')
ax[0].set_xlabel('year')
ax[0].set_ylabel('number of shoes')

plt.suptitle('comparison of movies and shows')
plt.tight_layout()
plt.savefig('shows and movies.png')
plt.show()

# rating counts
rating_counts = df['rating'].value_counts()
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%' , startangle=90)
plt.tight_layout()
plt.title("Rating Counts")
plt.savefig("rating.png")
plt.show()

# Duration of movies
movie=df[df['type']=='Movie'].copy()
movie['duration_int']=movie['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(movie['duration_int'],bins=30,color='purple',edgecolor='black')
plt.title("Distribution of movie")
plt.xlabel("Duration")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("duration.png")
plt.show()
