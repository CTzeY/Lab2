import statistics
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_min_max_temperature(num_list)
    cal_average_temperature(num_list)
    cal_median_temperature(num_list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32)")
    return 0
def get_user_input():
    x = input("Enter: ")
    print(x)
    input_list = x.split(",")
    print(input_list)
    num_list = list(map(float, input_list))
    print(num_list)
    return num_list
def cal_average_temperature(num_list):
    average = sum(num_list)/len(num_list)
    print("Average Temperature: " + str(average))
    return average
def calc_min_max_temperature(num_list):
    max_value = max(num_list)
    print("Maximum number: " + str(max_value))
    min_value = min(num_list)
    print("Minimum number: " + str(min_value))

def cal_median_temperature(num_list):
    median = statistics.median(num_list)
    print("Median Temperature: " + str(median))
    return median

if __name__== "__main__":
    main()

