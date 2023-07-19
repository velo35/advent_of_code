input_file = 1 and 'real.txt' or 'sample.txt'

with open('2021/day_16/input/' + input_file) as f:
    input = f.read().splitlines()

class Packet:
    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id
        self.value = None
        self.sub_packets = []

    def is_literal(self):
        return self.type_id == 4

    def __str__(self):
        return f'<version: {self.version}, type_id: {self.type_id}>' + ('' if not self.is_literal() else f' value: {self.value}')

hex_digit_to_binary = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

def hex_to_binary(hex):
    return "".join([hex_digit_to_binary[d] for d in hex])

def parse_packet(ndx, binary):
    version = int(binary[ndx:ndx+3], base = 2)
    ndx += 3
    type_id = int(binary[ndx:ndx+3], base = 2)
    ndx += 3

    packet = Packet(version, type_id)

    if packet.is_literal():
        words = []
        last = False
        while not last:
            last = binary[ndx] == '0'
            words.append(binary[ndx+1:ndx+5])
            ndx += 5
        packet.value = int(''.join(words), base = 2)
    else:
        length_id = binary[ndx]
        ndx += 1
        if length_id == '0':
            length = int(binary[ndx:ndx+15], base = 2)
            ndx += 15
            old_ndx = ndx
            while [x for x in binary[ndx:old_ndx + length] if x == '1']:
                ndx, sub_packet = parse_packet(ndx, binary)
                packet.sub_packets.append(sub_packet)
            ndx = old_ndx + length
        else:
            sub_count = int(binary[ndx:ndx+11], base = 2)
            ndx += 11
            for _ in range(sub_count):
                ndx, sub_packet = parse_packet(ndx, binary)
                packet.sub_packets.append(sub_packet)

    return ndx, packet

def _print_packet(indent, packet):
    print(indent + str(packet))
    for p in packet.sub_packets:
        _print_packet(indent + '   ', p)

def print_packet(packet):
    _print_packet('', packet)

def sum_versions(packet):
    val = packet.version
    for p in packet.sub_packets:
        val += sum_versions(p)
    return val

def task_1():
    for line in input:
        _, packet = parse_packet(0, hex_to_binary(line))
        print('task 1:', sum_versions(packet))
        
from functools import reduce
packet_op = [
    sum, 
    lambda a: reduce(lambda b, c: b * c, a),
    min,
    max,
    None,
    lambda a: 1 if a[0] > a[1] else 0,
    lambda a: 1 if a[0] < a[1] else 0,
    lambda a: 1 if a[0] == a[1] else 0
]

def eval_packet(indent, packet):
    if packet.is_literal():
        return packet.value
    args = [eval_packet(indent + '   ', p) for p in packet.sub_packets]
    result = packet_op[packet.type_id](args)
    return result

def task_2():
    for line in input:
        _, packet = parse_packet(0, hex_to_binary(line))
        print('task 2:', eval_packet('', packet))


task_1()
task_2()