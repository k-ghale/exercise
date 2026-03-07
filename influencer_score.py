import math
def influencer_score(num_followers, average_engagement_percentage):
    influencer_score = average_engagement_percentage * math.log(num_followers, 2);
    return influencer_score

print(influencer_score(43000,0.1))