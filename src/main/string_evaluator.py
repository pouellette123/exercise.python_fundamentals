# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
	return "Hello World"
        #return None # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
	return value_to_be_added_to + value_to_add
        #return None # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
	return string_to_fetch_from(starting_index:ending_index+1)
        #return None # TODO - Implement solution

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
	return string_to_fetch_from(starting_index+1, ending_index-1)
        #return None # TODO - Implement solution

    def compare(self, first_value, second_value):
	if first_value == second_value:
		return True
	else:
		return False
        #return None # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
	len_string = len(string_to_fetch_from)
	middle=len_string/2
	return string_to_fetch_from(middle:middle+1)
        #return None # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
	tmp_list=string_to_fetch_from.split()
	return tmp_list[0]
        #return None # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
	tmp_list=string_to_fetch_from.split()
	return tmp_list[1]
        #return None # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
	return string_to_be_reversed[::-1]
        #return None # TODO - Implement solution
