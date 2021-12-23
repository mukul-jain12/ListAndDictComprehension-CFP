"""
    @File :   data_handle.py
    @Author : mukul
    @Date :   23-12-2021
"""
import json


class HandleJSONData:
    @staticmethod
    def load_json_data(json_file):
        """
            desc: read the json file and return object
            param: json_file (practice_data.json) contains json data
            return: dictionary
        """
        with open(json_file) as file:
            load_data = json.load(file)
        return load_data

    @staticmethod
    def dump_json_data():
        """
            desc: write the dictionary in a json file
        """
        string = {"users": [{"id": 0, "name": "AdamCarter", "work": "Unilogic", "email": "adam.carter@unilogic.com",
                             "dob": "1978", "address": "83WarnerStreet", "city": "Boston", "optedin": 'true'},
                            {"id": 1, "name": "MukulJain",
                             "work": "SDE", "email": "mukul@connic.org", "dob": "1953", "address": "NearGurudwara",
                             "city": "Dungarpur",
                             "optedin": 'false'},
                            {"id": 3, "name": "DibyeshMishra", "work": "SDE", "email": "dibyesh@connic.org",
                             "dob": "1950",
                             "address": "IKIDK", "city": "Balia", "optedin": 'true'},
                            {"id": 4, "name": "Shivam", "work": "SDE",
                             "email": "shivam@connic.org", "dob": "1947", "address": "IDK", "city": "Pune",
                             "optedin": 'false'}], "images": ["img0.png", "img1.png", "img2.png"],
                  "coordinates": {"x": 35.12, "y": -21.49}, "price": "$59,395"}

        json_file = "practice_data2.json"
        with open(json_file, 'w') as file:
            json.dump(string, file)
        file.close()


if __name__ == '__main__':
    data_handle = HandleJSONData()

    data_file = "practice_data.json"
    print(data_handle.load_json_data(data_file))
    data_handle.dump_json_data()
