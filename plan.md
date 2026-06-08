Plan:

- To be based on first past the post systems (seat based like england)

- Figure out how to either mathematically or algorithmically do a very simple version of the problem:
    - A n*n graph where every point can either be a 1 or 0
    - Regions such that:
        - No limit on number of regions but each region must contain k cells each, given that n^2 mod k = 0 
        - All points must belong to a region
        - All points in a region must be adjacent i.e. connected
    - The aim is to select a party to win i.e. the 1s
    - The program will optimise the region selections so that:
        - The highest number of regions have been dominated by 1
        - As in over 50% of votes belong to 1

- Generalise the problem so that each point can have any number of connections and can belong to several parties, a win just means the highest vote per electorate

- Create model touse a distribution to estimate the political affiliations within an area


tbc