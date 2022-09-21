# CMPE150_project-2

In this project, we were expected to implement a movie recommendation system. 
The system would make recommendations for a user based on ratings of other users.

We were given a file named ratings.csv containing movie rating history for a set of users. 
Each line of this file corresponds to the history of a user and includes user id and information 
of movies rated by this user separated by commas (,). For each movie, its name and rating are 
given and this pair is separated by a column (:). 

For instance, the line 

UserX,Toy Story:5,Up:5,Inside Out:4

indicates that this user has id UserX and watched three movies: Toy Story, Up, Inside Out and gave ratings of 5, 5, 4 respectively.
To make recommendations, the system will consider the similarity of user movie ratings and suggest movies from history of users with 
most "similar" tastes. The taste similarity of users will be computed as 1 over the sum of absolute difference between ratings of these users. 
If a movie has been rated by one user but not the other one, then the mean rating of the movie is considered as the rating of the user that has not rated yet.

<img width="906" alt="Screen Shot 2022-09-21 at 20 12 12" src="https://user-images.githubusercontent.com/69856039/191568581-7c10b85b-eade-4f9e-a557-50650c5c3dfe.png">
