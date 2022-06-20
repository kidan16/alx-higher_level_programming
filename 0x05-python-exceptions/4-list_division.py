#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for j in range(list_length):
        try:
            new_list.append(my_list_1[j] / my_list_2[j])
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            new = new_list
    return new
