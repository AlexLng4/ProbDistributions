from generator.data_generator import DataGenerator
import json

def main():
    with open("config/data_config.json") as data:
        data_cofiguration = json.load(data)

    data = DataGenerator(data_configuration=data_cofiguration)

if __name__ == "__main__":
    main()