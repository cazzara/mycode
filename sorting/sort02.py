firewallports = [ 5060, 5061, 80, 443, 22, 25565 ]
def modTen(x):
    return x%10
print('Currently firewallports looks like this: ' + str(firewallports))
print('\nThe results of sorted(firewallports, key=modTen) function:', sorted(firewallports, key=modTen))
print('\nBut firewallports has not actually changed:', firewallports)


simpsons = [ ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34) ]
def byAge(x):
    return x[1]

simpsonsAge = sorted(simpsons, key=byAge)
print('Result of sorted(simpsons, key=byAge): ', simpsonsAge)

def secondChar(x):
    return x[0][1]

simpsonsChar = sorted(simpsons, key=secondChar)
print('Result of sorted(simpsons, key=secondChar): ', simpsonsChar)
