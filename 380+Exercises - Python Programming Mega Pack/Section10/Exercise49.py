#TODO: Two customer ID sets are given. The first one tells you whether a person clicked on the banner ad. Second, whether the person purchased the product:
# is_clicked = {'9001', '9002', '9005'}
# is_bought = {'9002', '9004', '9005'}
# Return the ID of those customers who clicked on the ad and bought the product.

is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}

print(f"Customer ID: {is_bought.intersection(is_clicked)}")