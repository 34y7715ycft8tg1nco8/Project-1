# Project-1
## Milestone2

### Overview:
My A.I agent will be goal based agent that will predict and model meteorite fall frequencies(in 10 year spans), geographical locations(countries, cities, etc.) that are most likely to experience these meteorite landings, and predict the likelihood of the destruction a meteorite can cause, all with the help of the main meteorite dataset I'll be using from Nasa that allows for these predictions and calculations to be made and an additional worldwide dataset that correlates cities with countries.

### PEAS:
My agent's performance measure will be meteorite detection, that is, finding these fallen meteorites for the purpose of research and worldwide safely prediction by modeling how frequent these meteorites fall based on historical timeline to predict possible meteor showers and/or dangerous meteorites(given by mass). My agent will have a fully observable environment of planet earth, given geographical locations, a timeline, the masses of the meteorites, and more. My agent's actuators will be predictive outcomes on meteorite landings, that is, predicting the next decade of meteorite frequencies based on the given evidence(clustering data and finding patterns depending on time and location), predictive outcomes on specific meteorite landing locations(which depends on frequencies on a given location), and the predictive danger level of a meteorite(which depends on mass and frequencies), all which can be modeled in a probabilistic way using a Bayesian Network. Lastly, my agent will have sensors of gps(world map), time collection, and meteorite mass/material measurement.

### Conclusion:
So far, My 1st model predicts the next 10 year outcomes on meteorite frequencies based on prior 10 year spans. Although, I notice I can improve my next model with a more accurate prediction using an improved set of evidence, that is, utilizing the entire timeline of the dataset to preproccess and cluster the frequencies of the meteorite landings and find a pattern to predict not just the likelyhood of meteroite frequencies for the next given decade, but even for a given region. The data will be preproccesed and transformed into clusters with the help of sklearn, find patterns, and come up with a better inference. My model diagram (image pdf attached to branch) demonstrates each of the important variables for this model. The first set of nodes are the evidence, the frequency node depends on them to preproccess the data and the last two nodes depend on the frequency preproccessed data to come up with a more accurate inference going forward. Each of the nodes will be a function in my model.

### Link to code script I have so far:
https://github.com/34y7715ycft8tg1nco8/Project-1/blob/Milestone2/Meteorite_Inference.py
