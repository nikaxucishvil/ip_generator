import random  # Import the random module, which is used for generating random numbers

# Function to generate a random IP address in the format 192.168.1.X, where X is a number between 0 and 20
def generate_random_ip():
    return f"192.168.1.{random.randint(0,20)}"

# Function to check if the given IP address matches any firewall rules and return the corresponding action
def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():  # Iterate over all the rules in the rules dictionary
        if ip == rule_ip:  # If the IP address matches a rule
            return action  # Return the corresponding action ("block" or "allow")
    
    return "allow"  # If the IP address is not in the firewall rules, return "allow"

# Main function that generates random IP addresses and checks them against the firewall rules
def main():
    # Dictionary of firewall rules specifying actions for certain IP addresses
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block",
    }

    for i in range(12):  # Loop that runs 12 times
        ip_address = generate_random_ip()  # Generate a random IP address
        action = check_firewall_rules(ip_address, firewall_rules)  # Check the IP address against the firewall rules
        random_number = random.randint(0, 9999)  # Generate a random number between 0 and 9999
        print(f"Ip: {ip_address}, Action: {action}, Random: {random_number}")  # Print the IP address, action, and random number

# Check if the script is being run directly (and not imported as a module)
if __name__ == "__main__":
    main()  # Execute the main function
