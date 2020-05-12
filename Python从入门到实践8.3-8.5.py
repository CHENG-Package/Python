def make_shirt(size_input, pattern_input):
    print("The T-shirt is about to be " + str(size_input) + " size and " + str(pattern_input) + ".")

make_shirt('L', 'SNAKE')
make_shirt(size_input="M", pattern_input="SNAKE")
print('')

def make_shirt(size_input, pattern_input="I love Python"):
    print("The T-shirt is about to be " + str(size_input) + " size and " + str(pattern_input) + ".")

make_shirt('L')
make_shirt('M')
make_shirt('XXL', pattern_input="I love Computer")

print('')
def describe_cities(name = "Reykjavik", country = "Iceland"):
    print(name.title() + " is in " + country.title())

describe_cities("Shenzhen", "China")
describe_cities('New York', 'U.S.A')
describe_cities()