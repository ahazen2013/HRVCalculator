# HRVCalculator

This program was created for a research project looking at heart rate variability (HRV) in long COVID patients. HRV is a measure of the length of time between a person's hearbeats- also known as beat-to-beat intervals (BBIs). A lower HRV indicates a more stressed state, and a higher HRV inicates a more relaxed state.

This program takes a group of CSV files (in the source folder), which contain heart rate variability (HRV) data, and returns a group of CSV files (to the results folder), which contain the standard deviation (SD) and root mean square of successive differences (RMSSD) of the beat-to-beat intervals obtained from the input files. The data in this repository was collected by me, using a Garmin vivosmart 4 fitness tracker, the Garmin and physioQ phone apps, and labfront.com.

Each CSV file represents one day the fitness tracker was worn. The way this program analyzes the data is by splitting each day into 5-minute intervals, and finding the SD (a measure of how far each piece of data in a set is from the average of the set) and RMSSD (a measure of how far each piece of data in a set is from the one immediately preceding it) of each 5-minute interval. The program then outputs the results of this analysis in the form of one result excel file per day analyzed.
