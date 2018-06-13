# Equations are given in the format A / B = k, where A and B are variables represented as strings, 
# and k is a real number (floating point number).
# Given some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given a / b = 2.0, b / c = 3.0. 
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
#  where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # first, make a map of known relationships
        knownVariables = {}

        for i in range(0, len(values)):
            # if ["a", "b"] and values 2
            a = equations[i][0]
            b = equations[i][1]

            # create records for a = b * 2 
            if a not in knownVariables:
                knownVariables[a] = {}
            knownVariables[a][b] = values[i]
            # and b = a * 1/2
            if b not in knownVariables:
                knownVariables[b] = {}
            knownVariables[b][a] = 1 / values[i]
        
        results = []

        for q in queries:
            a = q[0]
            b = q[1]
            results.append(self.solve(a, b, knownVariables))
        
        return results
            
    
    def solve(self, numerator, denominator, knownVariables):
        """
        :type numerator: str
        :type denominator: str
        :type seed: int
        :type knownVariables: List[List[str][int]]]
        """
        # if we don't know the numerator or denominator, bail
        if numerator not in knownVariables or denominator not in knownVariables:
            return -1
        # if num == dom, 3/3 == 1, return 1 
        if numerator == denominator:
            return 1

        # ok, start working, get the known stuff for numerator
        n1 = knownVariables[numerator]

        # remove it from the set so we don't process it in the next call
        del knownVariables[numerator]

        result = -1
        # search all the children of numerator
        for n in n1:
            # eventually this will recurse down to b == b, and return 1
            result = self.solve(n, denominator, knownVariables)
            if result != -1:
                # then we multiply that by the value factor
                result = result * n1[n]
                break

        # add it back on the way back up so the next query can use it
        knownVariables[numerator] = n1

        return result

        
