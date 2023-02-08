from interfaces.six_interface import SixKataInterface


class SixKata(SixKataInterface):

    def process_string(self, input: str) -> dict:
        rows, cities = [], {}

        for data in input.split("\n"):
            rows.append(data.strip())

        for row in rows:
            rainfalls = []
            city, records = row.split(":")[0], row.split(":")[-1].split(",")
            if len(records) == 12:
                for rainfall in records:
                    rainfalls.append(float(rainfall.split()[-1]))
            cities[city] = rainfalls

        return cities
    
    def validation(self, data: dict, town: str) -> bool:
        return town in data and len(data[town]) != 0

    def mean(self, town: str, s: str) -> float:
        if not self.validation(self.process_string(s), town):
            return -1
        rainfalls = self.process_string(s)[town]
        sum_rainfalls = sum([rainfall for rainfall in rainfalls])
        return sum_rainfalls / len(rainfalls)
    
    def variance(self, town: str, s: str) -> float:
        if not self.validation(self.process_string(s), town):
            return -1
        rainfalls = self.process_string(s)[town]
        mean = sum([rainfall for rainfall in rainfalls]) / len(rainfalls)
        sum_rainfalls = sum(pow(mean - rainfall, 2) for rainfall in rainfalls)
        return sum_rainfalls / len(rainfalls)
    
    def stock_list(self, list_of_art: list, list_of_cat: list) -> str:
        result, output = {}, []

        if (len(list_of_art) == 0 or len(list_of_cat) == 0):
            return ""

        for letter in list_of_cat:
            result[letter] = 0
            for word in list_of_art:
                if letter == word[0]:
                    result[letter] += int(word.split()[-1])
        
        for key, value in result.items():
            output.append(f"({key} : {value})")
        
        return ' - '.join(output)
