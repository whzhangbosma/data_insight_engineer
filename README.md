# data_insight_engineer

## Problem
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years.

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the input directory, running the run.sh script should produce the results in the output folder without needing to change the code.

## Algorithm

(1) Go through the whole csv file and store the names of all occupations appeared in that csv file as keys and their corresponding frequencies as values in a dictionary called "occ_rec", and the names of all states and corresponding frequencies in another dictionary called "pos_rec". 
This takes O(N) time and O(N) extra space.

(2) Build a max heap based on the list of (key, value) tuples of dict "occ_rec". I wrote a heap class to do this and do "pop" in the next step, where"max" of the max heap is determined by the firstly compare frequency (which is the value in the tuple), if a tie, then compare the string (which is the key in the tuple).
This takes O(N) time and O(N) extra space.

(3) pop the first element of the max heap and output its key (which is the occupation name) and value (which is its frequency) to "top_10_occupations.txt". Repeat this "pop and output" for 10 times.
This takes O(10 logN) time and no extra space.

(4) Repeat step(2) for another dict "pos_rec"

(5) Repeat step(3) for another max heap built based on "pos_rec"

complexity:
In total, time is O(N), space is O(N).

## How to Run
give 3 arguments in run.sh, 1 arg is the directory and name of input file; 2 args are the directories and names of output files (top_10_occupation.txt and top_10_states.txt respectively)
then use the command (before this you may need chmod +x run.sh):
./run.sh 
