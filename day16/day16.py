# Day 16: Packet Decoder

import sys

# ==============================================================================

# If no specific input given, default to "day<X>.in"
if len(sys.argv) == 1:
  sys.argv.append(sys.argv[0].replace(".py", ".in"))

# Parse input
with open(sys.argv[1]) as f:
  hex_string = f.readline().strip()

class Packet:
  def __init__(self, version, type_ID, payload, size):
    self.version = version
    self.type_ID = type_ID
    self.payload = payload
    self.size = size
  def __repr__(self):
    if self.type_ID == 4:
      type_str = "literal"
    else:
      type_str = "operator"
    return "<version={}, type={}, payload={}, size={}>".format(self.version, type_str, str(self.payload), self.size)

def decode_hex_packet(hex_string):

  bits = ""
  for h in hex_string:
    bits += "{:b}".format(int(h, 16)).zfill(4)

  packet = decode_packet_rec(bits, 0)

  return packet

def decode_packet_rec(bits, s, lvl=0):
    
  # print("\n[{}] Decoding from s={}".format(lvl, s))

  version = int(bits[s:s+3], 2)
  type_ID = int(bits[s+3:s+6], 2)
  k = s+6
  
  global version_sum
  version_sum += version

  # Literal packet -- scan groups of 5 bits until leading bit is 0
  if type_ID == 4:

    # print("type: literal")
    
    num = ""
    done = False
    while not done:
      num += bits[k+1:k+5]
      if bits[k] == "0":
        done = True
      k += 5

    # Padding
    # if (k-s) % 4 != 0:
    #   k += 3-(k-s)%4

    payload = int(num, 2)
    size = k-s

    # print("literal packet:", Packet(version, type_ID, payload, size))
      
  # Operator packet
  elif type_ID != 4:

    # print("type: operator")

    payload = []

    length_type_ID = int(bits[k], 2)
    k += 1

    # Total length of sub-packets 
    if length_type_ID == 0:
      
      length = int(bits[k:k+15], 2)
      # print("payload length is", length)
      k += 15
      
      count = 0
      while count < length:
        subpacket = decode_packet_rec(bits, k, lvl+1)
        payload.append(subpacket)
        count += subpacket.size
        k += subpacket.size

      # print("Done parsing subpackets for lvl={}".format(lvl))

    # number of sub-packets immediately contained
    elif length_type_ID == 1:
      
      num_sub = int(bits[k:k+11], 2)
      # print("number of subpackets is", num_sub)
      k += 11

      for _ in range(num_sub):
        subpacket = decode_packet_rec(bits, k, lvl+1)
        payload.append(subpacket)
        k += subpacket.size

      # print("Done parsing subpackets for lvl={}".format(lvl))

  size = k-s
  return Packet(version, type_ID, payload, size)

# ------------------------------------------------------------------------------
# Part 1

# hex_string = "D2FE28"
# hex_string = "38006F45291200"
# hex_string = "EE00D40C823060"
# hex_string = "8A004A801A8002F478"
# hex_string = "620080001611562C8802118E34"
# hex_string = "C0015000016115A2E0802F182340"
# hex_string = "A0016C880162017C3686B18A3D4780"

version_sum = 0
top_packet = decode_hex_packet(hex_string)

print("Part 1:", version_sum)

# ------------------------------------------------------------------------------
# Part 2

def eval_packet(packet):

  if packet.type_ID == 4:
    
    return packet.payload

  else:

    values = [eval_packet(subpacket) for subpacket in packet.payload]

    if packet.type_ID == 0:
      return sum(values)
  
    elif packet.type_ID == 1:
      prod = 1
      for v in values:
        prod *= v
      return prod
  
    elif packet.type_ID == 2:
      return min(values)
  
    elif packet.type_ID == 3:
      return max(values)

    elif packet.type_ID == 5:
      return 1 if values[0] > values[1] else 0

    elif packet.type_ID == 6:
      return 1 if values[0] < values[1] else 0

    elif packet.type_ID == 7:
      return 1 if values[0] == values[1] else 0


ans2 = eval_packet(top_packet)

print("Part 2:", ans2)
