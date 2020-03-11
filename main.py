# coding: utf-8
import yaml
import os
from vanilla.package1 import Class1


def main():
    # Get environment from env variable
    environment = os.environ["ENVIRONMENT"] if ("ENVIRONMENT" in os.environ) else "development"

    print("ENVIRONMENT : {}".format(environment))

    # Load configuration from ENVIRONMENT variable
    with open("./config/{}.yml".format(environment), "r") as configuration_file:
        conf = yaml.load(configuration_file, Loader=yaml.FullLoader)

    # DO YOUR STUFFs
    my_class = Class1(conf["is_reversed"])
    print(my_class.say_hello("Fanch"))


if __name__ == '__main__':
    main()
