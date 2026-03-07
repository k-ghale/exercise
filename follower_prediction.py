
def follower_prediction(follower_count, influencer_type, num_months):
    if influencer_type == "fitness":
        follower_count = (follower_count) * 4 ** num_months
    elif influencer_type == "cosmetic":
        follower_count = (follower_count) * 3 ** num_months
    else:
        follower_count = (follower_count) * 2 ** num_months
    
    return follower_count

# usage
print(follower_prediction(10, "fitness" , 8))
# expected answer :  655360 