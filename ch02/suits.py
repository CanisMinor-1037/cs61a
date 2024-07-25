"""
1: 'coin', 'string', 'myriad'
2: 'coin'
3: 'coin', 'cup', 'sword', 'club'
4: 'coin', 'cup', 'spade', 'club'
5: 'heart', 'diamond', 'spade', 'club'
"""
# 
chinese = ['coin', 'string', 'myriad']
suits = chinese
print(suits)

# - myriad, - string
suits.pop()
suits.remove('string')
print(suits)

# + cup, + sword, + club
suits.append('cup')
suits.extend(['sword', 'club'])
print(suits)

# sword -> spade
suits[2] = 'spade'
print(suits)

# coin -> heart, cup -> diamond
suits[0:2] = ['heart', 'diamond']
print(suits)