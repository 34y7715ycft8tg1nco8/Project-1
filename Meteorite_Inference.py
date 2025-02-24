
from sklearn.cluster import DBSCAN
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import string

# Transforming data from csv to a matrix (2D list). 
Meteor_path = "/Users/eduardolopez858/Downloads/Project-1/meteorite-landings.csv"
WorldCities_path = "/Users/eduardolopez858/Downloads/Project-1/worldcitiespop.csv"
with open(Meteor_path, mode="r", newline="") as file1:
    MeteorData = list(csv.reader(file1))
with open (WorldCities_path, mode="r", newline="") as file2:
    CityData = list(csv.reader(file2))

'''
# Data Analysis
print("Total number of observations: ", len(MeteorData) - 1)
print("For each observation, we are given the following information about each meteorite: ", MeteorData[0])
# Analyzing each column 
print("The name, Geolocation, reclat, and reclong columns give the location where the meteorite was found, that is, the name of the location and the exact coordinates it was found: ", data[0][0], data[0][9])
print("The id column gives us a unique identification number for each metoerite: ", MeteorData[0][1])
print("The nametype column will either be valid, meaning the meteorite was found as a meteorite object or relict, meaning it was once a meteorite: ", data[0][2])
print("The reclass column gives the type/class of meteorite based on the material it's made out of: ", MeteorData[0][3])
print("The mass column gives the mass of the metoerite: ", MeteorData[0][4])
print("The fall column tells us whether the meteorite was observed falling or had already landed: ", MeteorData[0][5])
print("The year column tells us the year the meteorite was discovered or fell given the evidence: ", MeteorData[0][6])
# Each of these obervations gives us the proper information we need to reach the goal of my probabilistic agent
# Our data is both distributed discretly and continuously:
# Discretly distributed: id, classification, year, fall
# Continuously distributed: name, nametype, mass, reclat, reclong, Geolocation. Although, this data can be categorized in a way that makes it discrete.
'''


# Main Inference
class BN:
    # constructer (not including headers of data)
    def __init__(self, meteor_data, city_data):
        self.meteor_data = meteor_data[1:]
        self.city_data = city_data[1:]

    # categorizing mass of meteorite based on Nasa classification
    def mass_evidence(self, meteor):
        mass_kg = meteor[4]
        if mass_kg <= 10:
            return 'Small'
        if mass_kg > 10 and mass_kg <= 1000:
            return 'Medium'
        if mass_kg > 1000:
            return "Large"
        
    # getting all decade's frequencies
    def frequency_by_decade(self, city):
        decade_counts = {}
        # getting past decade of current year
        for meteor in self.meteor_data:
            if city == meteor[0]:
                year = int(meteor[6])
                decade = (year // 10) * 10
                decade_counts[decade] = decade_counts.get(decade, 0) + 1
        return decade_counts
    
    # computing prior's based on time (partitioned into decades)
    def prior(self, decade_counts):
        total = sum(decade_counts.values())
        return {decade: count / total for decade, count in decade_counts.items()}

    # main computation 1: predicting next decade on city and country (user preference)

    # frequency by city
    def likelyhood_city_next10(self,city):
        frequencies = self.frequency_by_decade(city)
        if not frequencies:
            return None
        priors = self.prior(frequencies)
        if not priors:
            return None
        # naive bayes
        posterior = {decade + 10: priors[decade] for decade in priors}
        if not posterior:
            return None
        # normalization
        for i in posterior:
            posterior[i] /= sum(posterior.values())
        # max likelyhood
        predicted_decade = max(posterior, key=posterior.get)
        return int(posterior[predicted_decade] * sum(frequencies.values()))

    ## improved inference with the use of data clustering will go below
   










meteorite_bn = BN(MeteorData, CityData)
prediction = meteorite_bn.likelyhood_city_next10("Phum Sambo")
print(prediction)



    
    
