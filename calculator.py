git add calculator.py
git commit -m "Added cloud computing calculator script"
git push origin main
def cloud_computing_calculator():
    # Pricing model
    compute_price_per_hour = 0.05  # $ per vCPU per hour
    storage_price_per_gb_per_month = 0.01  # $ per GB per month
    data_transfer_price_per_gb = 0.10  # $ per GB transferred
    
    # Get user inputs
    print("Welcome to the Cloud Computing Cost Calculator!")
    compute_hours = float(input("Enter the number of virtual CPU hours used: "))
    storage_gb = float(input("Enter the amount of storage in GB: "))
    data_transfer_gb = float(input("Enter the amount of data transferred in GB: "))
    
    # Calculate costs
    compute_cost = compute_price_per_hour * compute_hours
    storage_cost = storage_price_per_gb_per_month * storage_gb
    data_transfer_cost = data_transfer_price_per_gb * data_transfer_gb
    
    # Total cost
    total_cost = compute_cost + storage_cost + data_transfer_cost
    
    # Print the breakdown
    print("\nCloud Computing Cost Breakdown:")
    print(f"Compute cost: ${compute_cost:.2f}")
    print(f"Storage cost: ${storage_cost:.2f}")
    print(f"Data transfer cost: ${data_transfer_cost:.2f}")
    
    print(f"\nTotal cloud computing cost: ${total_cost:.2f}")
    
# Run the calculator
cloud_computing_calculator()

