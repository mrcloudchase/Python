import ipaddress
import time
def check_cidr(cird1,cidr2):
  # Print statement and sleep
  print("Checking IP CIDRs Now...")
  time.sleep(3)
  # Set vars using function parameters
  n1 = ipaddress.IPv4Network(cird1)
  n2 = ipaddress.IPv4Network(cidr2)
  # if/else check for overlap
  if (n1.overlaps(n2)):
    print("Overlaps")
  else:
    print("No Overlap")
check_cidr('10.0.0.0/16','10.0.128.0/20')
