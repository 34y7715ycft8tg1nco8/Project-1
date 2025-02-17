import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# Transforming data from csv to a matrix (2D list). The purpose of this transformation is for scaling and simplicity for my probabilistic agent
Meteor_path = "/Users/eduardolopez858/Downloads/Project-1/meteorite-landings.csv"
WorldCities_path = "/Users/eduardolopez858/Downloads/Project-1/worldcitiespop.csv"
with open(Meteor_path, mode="r", newline="") as file1:
    MeteorData = list(csv.reader(file1))
with open (WorldCities_path, mode="r", newline="") as file2:
    CityData = list(csv.reader(file2))

'''
# Number of observations
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

'''
# Modeling our Data using NetworkX
model = nx.DiGraph()
variables = ['Mass', 'Location', 'Time', 'Frequency', 'Frequency on location', 'Danger level']
model.add_nodes_from(variables)
model.add_edge('Mass', 'Danger level')
model.add_edge('Location', 'Frequency on location')
model.add_edge('Time', 'Frequency')
model.add_edge('Frequency', 'Danger level')
model.add_edge('Frequency', 'Frequency on location')
nx.draw(model, with_labels = True)
plt.show()
'''

# Main Inference
class Meteorite_BN:
    # constructer (not including headers of data)
    def __init__(self, MeteorData, CityData):
        self.MeteorData = MeteorData[1:]
        self.CityData = CityData[1:]

    # categorizing meteor mass on low, medium, or high
    def mass_category(meteor):
            mass = meteor[0][4]
            if mass <= 10:
                return 'low'
            elif mass < 10 and mass <= 1000:
                return 'medium'
            elif mass >= 1000:
                return 'high'
            
    # getting 10 year span frequency and putting it into a category of low, medium, or high
    def frequency_decade(year, MeteorData):
        # getting past decade of current year
        counts = {}
        for meteor in MeteorData:
            try:
                year = int(meteor[0][6])  
                decade = (year // 10) * 10
                counts[decade] = counts.get(decade, 0) + 1
            except ValueError:
                continue  # Skip missing years

        # Get frequency for the given decade
        frequency = counts.get(decade, 0)
        # returning the frequency category
        if frequency <= 50:
            return 'low'
        elif frequency > 50 and frequency <= 150:
            return 'medium'
        elif frequency < 150:
            return 'high'

    # 


     
            
            

    
    
