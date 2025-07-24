'''
4
{"order_id": "ORD001", "customer_name": "John Smith", "customer_tier": "Premium", "customer_years": 3, "order_value": 150, "urgent": false, "same_day_delivery": true, "region": "East"}
{"order_id": "ORD002", "customer_name": "Alice Johnson", "customer_tier": "VIP", "customer_years": 6, "order_value": 200, "urgent": true, "same_day_delivery": false, "region": "West"}
{"order_id": "ORD003", "customer_name": "Bob Wilson", "customer_tier": "Standard", "customer_years": 1, "order_value": 80, "urgent": false, "same_day_delivery": false, "region": "Central"}
{"order_id": "ORD004", "customer_name": "Carol Davis", "customer_tier": "Premium", "customer_years": 4, "order_value": 120, "urgent": true, "same_day_delivery": true, "region": "East"}
'''

import math

# Step 1 & 2: Process and calculate scores
for order in orders:
    # Base priority (rounded down)
    priority_score = math.floor(order['order_value'] / 10)
    
    # Customer tier multiplier
    if order['customer_tier'] == 'VIP':
        priority_score *= 1.5
    elif order['customer_tier'] == 'Premium':
        priority_score *= 1.3
    
    # Urgency bonuses
    if order['urgent']:
        priority_score += 25
    if order['same_day_delivery']:
        priority_score += 15
    
    # Loyalty bonus (fixed: += not *=)
    if order['customer_years'] >= 5:
        priority_score += 20
    elif order['customer_years'] >= 2:
        priority_score += 10  # You had *= 10
    
    # Regional adjustment
    if order['region'] == 'West':
        priority_score -= 5
    elif order['region'] == 'East':
        priority_score += 10
    
    order['priority_score'] = int(priority_score)

# Step 3: Sort with customer tier mapping
tier_order = {'VIP': 0, 'Premium': 1, 'Standard': 2}

sorted_orders = sorted(orders, key=lambda x: (
    -x['priority_score'],                    # Descending
    tier_order[x['customer_tier']],          # VIP first
    -x['order_value'],                       # Descending  
    x['customer_name']                       # Ascending
))

return sorted_orders