import statistics


num_list = [20,90,8,10,45,24]
dict_stats = {}
def basic_stats(num_list):
    mean_list = statistics.mean(num_list)
    mode_list = statistics.mode(num_list)
    variance_list = statistics.variance(num_list)
    median_list = statistics.median(num_list)

    dict_stats = {
        'mean':mean_list,
        'mode':mode_list,
        'variance': variance_list,
        'medium':median_list
    }

    return dict_stats

print(basic_stats(num_list))