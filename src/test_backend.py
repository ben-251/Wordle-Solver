import colorama

clear = colorama.Style.RESET_ALL
green = colour = colorama.Fore.GREEN
red = colorama.Fore.RED
cyan = colorama.Fore.CYAN


def get_colour(state):
	if state == "fail":
		return red
	elif state == "pass":
		return green
	
def display_message(state, actual, expected):
	colour = get_colour(state)
	if state == "pass":
		print(f"{colour}Ok.{clear}")
		...
	else:
		print(f"{colour}Failed. \nResult:\n{actual}\nExpected:\n{expected}{clear}")

def assert_equals(actual,expected):
	if actual != expected:
		display_message("fail", actual, expected)
		exit()
	else:
		display_message("pass",actual, expected)
	return