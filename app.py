#!/usr/bin/env
import csv

class Reader:

    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.dict = {}

    def read(self):
        with open(self.filename) as csvfile:
            csv_reader = csv.reader(csvfile)

            for row in csv_reader:
                self.data.append(row)
            return self.data

    def flip_name(self):
        data = []
        for x in self.data:
                split = x[0].split(",")
                x[0] = split[1] + " " + split[0]
                data.append([x[0], x[1]])
        self.data = data

    def print_data(self):
        print(self.data)

    def dictionarify(self, key_number):
        for x in self.data:
            if x[key_number] != 'Name':
                key = x[key_number]
                self.dict[key] = x

class Writer:

    def __init__(self):
        self.data = []
        self.is_on_list = {}
        self.is_not_on_list = {}

    def compare(self, first_data_set, second_data_set):

        for x in second_data_set:

            if x[0] != ' First Name Last Name' and x[0] in first_data_set:
                key = x[0]
                self.is_on_list[key] = True
            elif x[0] != ' First Name Last Name':
                key = x[0]
                self.is_not_on_list[key] = True

        for key in self.is_not_on_list:
            print(key)

a = Reader()
b = Reader()
a.read()
a.dictionarify(2)
b.read()
b.flip_name()

writer = Writer()
writer.compare(a.dict, b.data)
