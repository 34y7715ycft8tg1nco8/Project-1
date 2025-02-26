
from sklearn.cluster import DBSCAN
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
import csv
import string

# Transforming data from csv to a matrix (2D list). 
Meteor_path = "/Users/eduardolopez858/Downloads/Project-1/meteorite-landings.csv"
with open(Meteor_path, mode="r", newline="") as file1:
    MeteorData = list(csv.reader(file1))

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
    def __init__(self, meteor_data):
        self.meteor_data = meteor_data[1:]
    # categorizing mass of meteorite based on Nasa classification
    def mass_evidence(self, meteor):
        mass_kg = int(meteor[4])
        if mass_kg <= 1:
            return 'Harmless. Most likely burn up in the atmosphere'
        if mass_kg > 1 and mass_kg <= 10:
            return 'Some property damage'
        if mass_kg > 10 and mass_kg <= 100:
            return "More localized damage, may cause injuries"
        if mass_kg > 100 and mass_kg <= 10000:
            return "Huge shockwave. May destory buildings"
        if mass_kg > 10000 and mass_kg <= 1000000:
            return "Regional threat. May destory entire cities and even cause tsunamis"
        if mass_kg > 1000000:
            return "Global threat. Mass extinctions"
        
    # getting all decade frequencies
    def frequency_by_decade(self, name):
        decade_counts = {}
        # getting past decade of current year
        for meteor in self.meteor_data:
            if name == meteor[0]:
                year = int(meteor[6])
                decade = (year // 10) * 10
                decade_counts[decade] = decade_counts.get(decade, 0) + 1
        return decade_counts

    # inference of the next decade of given city
    def likelyhood_city_next10(self,city):
        # collecting frequencies of given city
        frequencies = self.frequency_by_decade(city)
        if not frequencies:
            return 0
        # prior
        total = sum(frequencies.values())
        priors = {decade: count / total for decade, count in frequencies.items()}
        if not priors:
            return 0
        # naive bayes
        posterior = {decade + 10: priors[decade] for decade in priors}
        if not posterior:
            return 0
        # normalization
        for i in posterior:
            posterior[i] /= sum(posterior.values())
        # max likelyhood
        predicted_decade = max(posterior, key=posterior.get)
        return int(posterior[predicted_decade] * sum(frequencies.values()))

    # inference of the danger level of the meteor on city based on mass
    def danger_likelyhood(self, city):
        mass_data = []
        for meteor in self.meteor_data:
            if city == meteor[0]:
                mass_data.append(self.mass_evidence(meteor))
        freq_inference = self.likelyhood_city_next10(city)
        counts = Counter(mass_data)
        # highest likelyhood mass
        if not counts:
            return 0
        highest_likelyhood_mass = max(counts, key=counts.get)
        # likelyhood mass and normalization
        probabilty_mass = 0
        for mass in mass_data:
            if mass == highest_likelyhood_mass:
                probabilty_mass += 1
        # normalize
        probabilty_mass /= len(mass_data)
        print("Mass: ", highest_likelyhood_mass, " With kikelyhood: ", str(probabilty_mass))

# user input (using my model)
city_input = input("Enter City: ")
# inference call
meteorite_bn = BN(MeteorData)
prediction_for_city = meteorite_bn.likelyhood_city_next10(city_input)
danger_level = meteorite_bn.danger_likelyhood(city_input)
if prediction_for_city == 0:
    print("In the next decade, there will be ", prediction_for_city, " meteorite landings in ", city_input,".")
else:
    print("In the next decade, there will be ", prediction_for_city, " meteorite landings in ", city_input,".")
