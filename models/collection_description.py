class CollectionDescription:
    def __init__(self, id, dataset, historical_collection):  # pragma: no cover
        self.id = id
        self.dataset = dataset
        self.historical_collection = historical_collection

    def __eq__(self, other):  # pragma: no cover
        if self.id == other.id:
            return True
        return False

    def __str__(self):  # pragma: no cover
        return_value = f'\nCD: ID: {self.id}\n\tDataset: {self.dataset}'
        for datapoint in self.historical_collection:
            return_value += f'\n\t\t{datapoint}'

        return return_value
