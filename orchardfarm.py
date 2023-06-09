orange_plantation = 8 # total number of trees that can be planted on the farm
apple_plantation = 7
Mango_plantation = 5
lemon_plantation = 8
coconut_plantation = 5
max_coverage = 0.4 # maximum coverage limit for each type of tree

# Step 2
apple_trees = max(1, int(apple_plantation * 0.2 * max_coverage)) # at least one apple tree and up to 40% of total plantation
orange_trees = max(1, int(orange_plantation * 0.2 * max_coverage)) # at least one orange tree and up to 40% of total plantation
mango_trees = max(1, int(Mango_plantation * 0.2 * max_coverage)) # at least one mango tree and up to 40% of total plantation
lemon_trees = max(1, int(lemon_plantation * 0.2 * max_coverage)) # at least one lemon tree and up to 40% of total plantation
coconut_trees = max(1, int(coconut_plantation * 0.2 * max_coverage)) # at least one coconut tree and up to 40% of total plantation

# Step 3
apple_fruits = apple_trees * 400 # number of apples generated by all apple trees
orange_fruits = orange_trees * 280 # number of oranges generated by all orange trees
mango_fruits = mango_trees * 2200 # number of mangoes generated by all mango trees
lemon_fruits = lemon_trees * 1500 # number of lemons generated by all lemon trees
coconut_fruits = coconut_trees * 75 # number of coconuts generated by all coconut trees

# Step 4
apple_income = (apple_fruits / 5) * 150 # income generated by selling all apples
orange_income = (orange_fruits / 7) * 250 # income generated by selling all oranges
mango_income = (mango_fruits / 8) * 100 # income generated by selling all mangoes
lemon_income = (lemon_fruits / 10) * 50 # income generated by selling all lemons
coconut_income = (coconut_fruits / 15) * 1600 # income generated by selling all coconuts

# Step 5
total_income = apple_income + orange_income + mango_income + lemon_income + coconut_income

# Step 6
print("Total income generated:", total_income, "rupees") 