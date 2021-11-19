import hashlib
class NeuralCoinBlock:

  def __init__(self, previous_block_hash, transaction_list):
     self.previous_block_hash = previous_block_hash
     self.transaction_list = transaction_list

     self.block_data = "-".join(transaction_list)+ "-" + previous_block_hash
     self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 4 NC to Mike"
t3 = "Max sends 3.2 NC to Bob"
t4 = "Mike sends 1 NC to Anna"
t5 = "Mike sends 5.4 NC to Max"
t6 = "Anna sends 3 NC to Bob"
t7 = "Max sends 3.2 NC to Anna"
t8 = "Anna sends 1.5 NC to Peter"
t9 = "Anna sends 2.3 NC to joey"


initial_block = NeuralCoinBlock("Initial string", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3,t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5,t6])

print(third_block.block_data)
print(third_block.block_hash)

fourth_block = NeuralCoinBlock(third_block.block_hash, [t6,t7])

print(fourth_block.block_data)
print(fourth_block.block_hash)

fifth_block = NeuralCoinBlock(fourth_block.block_hash, [t8,t9])

print(fifth_block.block_data)
print(fifth_block.block_hash)


