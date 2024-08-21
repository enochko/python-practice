# BOM Weather Plot

This script requests the JSON weather observation data from BOM for Melbourne, Australia, and plots the air temperature in a graph with Matplotlib.

## To Do - Someday/Maybe
- Parse and split date properly - currently splitting day by 24 hours. Should split day by date.
- Handle unusual observation times - BOM does not record observations strictly every 30 minutes. Sometimes, observations are delayed, and these unusual observation times are appended to the end of the x-axis, resulting in random zigzag patterns.

## To Do - Done
- Request JSON data from BOM
- Extract header
- Extract weather data
- Plot temperature data
- Plot temperature by day
- Add title, labels, legends
