# Alex Hicks (awh4kc)

from polling import load_state_polls, polls_average, current_winner

print(load_state_polls('wisconsin'))
print(polls_average('wisconsin', '2016-09-20', '2016-10-18'))
print(current_winner(polls_average('wisconsin', '2016-09-20', '2016-10-18')))

print(load_state_polls('wisconsin'))
print(polls_average('wisconsin', '2016-10-16', '2016-10-16'))
print(current_winner(polls_average('wisconsin', '2016-10-16', '2016-10-16')))

print(load_state_polls('wisconsin'))
print(polls_average('wisconsin', '2016-09-11', '2016-10-27'))
print(current_winner(polls_average('wisconsin', '2016-09-11', '2016-10-27')))

