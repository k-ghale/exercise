def get_avg_brand_followers(all_handles,brand_name):
    total = 0
    for handle in all_handles:
        for brand in handle:
            if brand_name in brand:
                total += 0

    avg = total / len(all_handles)
    return avg
