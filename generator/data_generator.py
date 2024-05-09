import random

class DataGenerator:
    
    def __init__(self, data_configuration):
        
        if type(data_configuration) is dict:
            self.data = self.generate_samples(data_configuration) 

    def generate_samples(self, data_configuration):
        
        data = {}
        for class_name in data_configuration:
            samples = {}
            for _ in range(class_name.get("number_of_samples", None)):
                sample = []
                for _ in range(class_name.get("number_of_features", None)):
                    sample.append(random.uniform(-500, 500))
                samples.update(sample)
            data[class_name] = samples
            
        return data