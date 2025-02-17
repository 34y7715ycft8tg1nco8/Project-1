# Project-1
## Milestone2

### Overview:
My A.I agent will be goal based agent that will predict and model meteorite fall frequencies(in 10 year spans), geographical locations(countries) that are most likely to experience these meteorite landings, and predict the likelihood of the destruction a meteorite can cause, all with the help of the main meteorite dataset I'll be using from Nasa that allows for these predictions and calculations to be made and an additional worldwide dataset that correlates cities with countries.

### PEAS:
My agent's performance measure will be meteorite detection, that is, finding these fallen meteorites for the purpose of research and worldwide safely prediction by modeling how frequent these meteorites fall based on historical timeline to predict possible meteor showers and/or dangerous meteorites (also based on their given mass). My agent will have a fully observable environment of planet earth, given geographical locations, a timeline, the masses of the meteorites, and more. 
My agent's actuators will be predictive outcomes on meteorite landings(by frequency of 10 year spans which will depend on time and location), predictive outcomes on specific meteorite landing locations(which depends on frequency), and the predictive outcomes of a meteorite being a worldwide emergency(which depends on mass and frequency), all which can be modeled in a probabilistic way using a Bayesian Network. Lastly, my agent will have sensors of gps(world map), time collection, and meteorite mass/material measurement.

### Conclusion:
So far, My 1st model is not looking too bad. I am yet to create the full CPT's as I first need to create the probability functions. My plan going forward is to create a probabilty function for the danger level of a given meteorite. To do that, I will create a cpt by classifying the meteor mass and frequency (with the functions I made) and then predicting the danger level based on destruction (mass) and frequency. After that, I will focus on the next main computation of this Agent which is predicting the frequency of meteorite landings based on a given location.

### Link to code script I have so far:
https://github.com/34y7715ycft8tg1nco8/Project-1/blob/Milestone2/Meteorite_Inference.py
