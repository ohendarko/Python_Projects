def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print("%s == %s" % (key, value))

def main():
    greet_me(name="awef")
main()