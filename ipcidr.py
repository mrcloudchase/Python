# import necessary modules
import ipaddress
import time

# function that takes two IP CIDRs as parameters EX: 10.0.0.0/16
def check_cidr(cird1,cidr2):

  # Print statement and sleep
  print("Checking IP CIDRs Now...")
  time.sleep(3)
  
  # Set parameters in IP CIDR block notation rather than strings as variables
  n1 = ipaddress.IPv4Network(cird1)
  n2 = ipaddress.IPv4Network(cidr2)
  
  # If/else check for overlap
  if (n1.overlaps(n2)):
    # Print if IP CIDRs overlap
    print("Overlaps")
  else:
    # Print if IP CIDRs do not overlap
    print("No Overlap")
    
# Run function with these parameters
check_cidr('10.0.0.0/16','10.0.128.0/20')
