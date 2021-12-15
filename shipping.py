weight = 8.4
# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print(cost_ground)
cost_ground_premium = 125.00
print(cost_ground_premium)
# Drone Shipping
if weight <= 2:
  cost_ground = weight * 4.50 + 20
elif weight <= 6:
  cost_ground = weight * 9.00 + 20
elif weight <= 10:
  cost_ground = weight * 12.00 + 20
else:
  cost_ground = weight * 14.75 + 20