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
    input_list = x.split(",")
    num_list = list(map(float, input_list))
    num_list = input_list
    print(num_list)
    return num_list
def cal_average_temperature(num_list):
    average = sum(num_list)/len(num_list)
    print("Average temperature = " + str(average))
    return average
def calc_min_max_temperature(num_list):
    max_value = max(num_list)
    print("Maximum number is " + max_value)
    min_value = min(num_list)
    print("Minimum number is " + min_value)

def cal_median_temperature(input_list):
    sorted_list = sorted(input_list)
    n = len(sorted_list)
    middle = n // 2
    if n % 2 == 0:
        median = (sorted_list[middle - 1] + sorted_list[middle]) / 2
    else:
        median = sorted_list[middle]
    print("Median temperature = " + median)
    return median

if __name__ == "__main__":
    main()
