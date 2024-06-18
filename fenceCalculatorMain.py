# Rebekah Shi
# fence calculator project 1
#1/28/2024

#The first step is to Prompt for info

#prompt for length and width and then cast to float.
# After convert to inches for the use of same measurement units

#prompt for width, then convert to inches
width = input('Please input the desired width of your fence in feet e.g 10')
width = float(width)
width = width * 12

#prompt for length, then convert to inches
length = input('Please input the desired length of your fence in feet e.g 10')
length = float(length)
length = length * 12

#prompt for how far the posts are
post_distance = input('Please tell me how far you want the posts to be in inches e.g 1')
post_distance = float(post_distance)


#check to see if the distance between posts are divisible,
# if divisible then divide the distance of posts by width or length.
# That is the number of posts need for that side. Then double the number of posts for both sides.
#2* number of posts needed for width + 2 * number of posts needed for

#width number of post
if width % post_distance == 0:
   num_of_post_width = width/post_distance
   num_of_post_width = 2 * num_of_post_width


else:
    print('Sorry, the distance between posts are not able to equally distributed. Please try again')

#length number of post
if length % post_distance == 0:
   num_of_post_length = length/post_distance
   num_of_post_length = 2 * num_of_post_length


else:
    print('Sorry, the distance between posts are not able to equally distributed. Please try again')


#calculate total number of posts need for all four sides
all_posts = num_of_post_length + num_of_post_width


# to calculate the amount of boards needed, ask user the board length
# if board length > distance between posts, then calculate number of boards.
board_length = input('Please type in the length of your board in inches to put across the posts')
board_length = float(board_length)
if board_length > post_distance:
   num_boards_W =  width/board_length
   num_boards_W = 2 * num_boards_W
   num_boards_L = length/board_length
   num_boards_L = 2 * num_boards_L
   num_boards = num_boards_L + num_boards_W
   print('Number of boards needed for the project if you only want one board across the fence posts: ' + str(num_boards) + '\n')


else:
    print('Sorry, board length is less than the post distances')

#prompt for the number of boards desired across the posts
total_boards = input('Input the number of boards you want across the posts')
total_boards =  float(total_boards)
total_boards = total_boards * num_boards


#prompt and calculate cost of boards
board_cost = input('Input the cost of boards e.g 20: ')
board_cost = float(board_cost) * float(total_boards)
print('Total cost of boards: $' + str(board_cost) + '\n')

#prompt and calculate cost of posts
post_cost = input('Input the cost of the posts e.g 20: ')
post_cost = float(post_cost) * float(num_boards)
print('Total cost of posts: $' + str(post_cost) + '\n')

#calculate grand total
grand_total = board_cost + post_cost
print('This is the total cost of the project: $' + str(grand_total) + '\n')

#Display the number of posts and boards needed
print('Number of posts needed for the project: ' + str(all_posts) + '\n')
print('This the total number of boards you need: ' + str(total_boards))
