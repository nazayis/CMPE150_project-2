# separator	Main.py_0_false.txt
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

# separator	Main.py_1_true.txt
f = open("ratings.csv")
all_ratings = {}
for line in f:
    inputs = line.rstrip("\n").split(",")
    inputs.pop(0)
    ratings_of_user = {}
    for i in inputs:
        movie_name = i.split(":")[0]
        rating = float(i.split(":")[1])
        ratings_of_user[movie_name] = rating
        if movie_name in all_ratings:
            all_ratings[movie_name].append(rating)
        else:
            all_ratings[movie_name] = [rating]

def read_dataset(file):
    f = open(file)
    dataset_dict = {}
    for line in f:
        inputs = line.rstrip("\n").split(",")
        user_id = inputs[0]
        inputs.pop(0)
        ratings_of_user = {}
        for i in inputs:
            movie_name = i.split(":")[0]
            rating = float(i.split(":")[1])
            ratings_of_user[movie_name] = rating
        dataset_dict[user_id] = ratings_of_user
    return dataset_dict
def compute_mean_ratings(history):
    mean_ratings = {}
    for movie_name in all_ratings:
        mean_ratings[movie_name] = sum(all_ratings[movie_name]) / len(all_ratings[movie_name])
    return mean_ratings
def find_most_similar_users(history, given_id, number):
    dataset = history
    similarity_dict = {}
    for key, item in dataset.items():
        summation = 0
        movie_list = []
        for key2, item2 in item.items():
            movie_list.append(key2)
        for movie in dataset[given_id]:
            if movie not in movie_list:
                movie_list.append(movie)
        for movie_name in movie_list:
            if movie_name in dataset[key]:
                user2_rating = dataset[key][movie_name]
            else:
                user2_rating = compute_mean_ratings(all_ratings)[movie_name]
            if movie_name in dataset[given_id]:
                user1_rating = dataset[given_id][movie_name]
            else:
                user1_rating = compute_mean_ratings(all_ratings)[movie_name]
            absolute_difference = abs(user2_rating - user1_rating)
            summation += absolute_difference
        similarity_dict[key] = summation
    similarity_dict.pop(given_id)
    min_value = 90
    min_key = None
    min_list = []
    for i in range(N):
        for key, item in similarity_dict.items():
            if item <= min_value:
                min_value = item
                min_key = key
        similarity_dict.pop(min_key)
        min_list.append(min_key)
        min_value = 90
        min_key = None
    return min_list
def make_recommendations(history, output_id):
    dataset = history
    recommendation_list = []
    for similar_user in output_id:
        for movie_name, rating in dataset[similar_user].items():
            if rating >= 3.0:
                recommendation_list.append(movie_name)
        for recommendation in recommendation_list:
            if recommendation in dataset[similar_user] and dataset[similar_user][recommendation] < 3:
                recommendation_list.remove(recommendation)
            if recommendation in dataset[user_id]:
                recommendation_list.remove(recommendation)
    return recommendation_list


# separator	Main.py_2_false.txt
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

def abs(v):
    return v if v > 0 else -v

user_id, N = input().split(',')
N = int(N)
rating_histories = read_dataset('ratings.csv')
mean_ratings = compute_mean_ratings(rating_histories)
most_similar_ids = find_most_similar_users(rating_histories, user_id, N)
movies = make_recommendations(rating_histories, most_similar_ids)
print(','.join(sorted(list(set(movies)))))

