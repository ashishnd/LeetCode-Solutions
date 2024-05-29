// Date solved: 28th May 2024

// Language used to solve: C++ and Python

// Problem Description:

// Given an integer numRows, return the first numRows of Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

// Example 1:
// Input: numRows = 5
// Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

// Example 2:
// Input: numRows = 1
// Output: [[1]]

// Constraints:

// 1 <= numRows <= 30

// Solution 1 (C++) : 

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        for(int i=0;i<numRows;i++) {
            vector<int> row(i+1,1);
            for(int j=1;j<i;j++) {
                row[j] = result[i-1][j-1] + result[i-1][j];
            }
            result.push_back(row);
        }
        return result;
    }
};

// Solution 2 (Python) :

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        result.append([1])

        for i in range(1, numRows):
            prev_row = result[i-1]
            curr_row = [1]

            for j in range(1, i):
                curr_row.append(prev_row[j-1] + prev_row[j])
            
            curr_row.append(1)
            result.append(curr_row)
        
        return result
