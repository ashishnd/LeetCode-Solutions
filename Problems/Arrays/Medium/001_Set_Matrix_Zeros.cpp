// Date solved: 28th May 2024

// Language used to solve: C++

// Problem Description:

// Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
// You must do it in place.

// Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
// Output: [[1,0,1],[0,0,0],[1,0,1]]

// Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
// Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

// Constraints:

// m == matrix.length
// n == matrix[0].length
// 1 <= m, n <= 200
// -231 <= matrix[i][j] <= 231 - 1
  
// Solution 1: 

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        vector<vector<int>> zeros;
        int rows = matrix.size();
        int cols = matrix[0].size();

        for(int i=0;i<rows;i++) {
            for(int j=0;j<cols;j++) {
                if(matrix[i][j] == 0)
                    zeros.push_back({i,j});
            }
        }
        for(int x=0;x<zeros.size();x++) {
            int row = zeros[x][0];
            int col = zeros[x][1];
            for(int m=0;m<cols;m++) {
                matrix[row][m] = 0;
            }
            for(int i=0;i<rows;i++) {
                matrix[i][col] = 0;
            }
        }
    }
};

// Solution 2:

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        bool isZeroRow = false;
        bool isZeroCol = false;
        for(int i=0;i<matrix[0].size();i++) {   //check for zeros in row
            if(matrix[0][i] == 0) {
                isZeroRow = true;
                break;
            }
        }
        for(int i=0;i<matrix.size();i++) {      //check for zeros in col
            if(matrix[i][0] == 0) {
                isZeroCol = true;
                break;
            }
        }
        for(int i=1;i<matrix.size();i++) {      //check for zeros in other part
            for(int j=1;j<matrix[0].size();j++) {
                if(matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        for(int i=1;i<matrix.size();i++) {      //process for zeros in other part
            for(int j=1;j<matrix[0].size();j++) {
                if(matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
        }
        if(isZeroRow) {                         //process for zeros in row
            for(int i=0;i<matrix[0].size();i++) {
                matrix[0][i] = 0;
            }
        }
        if(isZeroCol) {                         //process for zeros in col
            for(int i=0;i<matrix.size();i++) {
                matrix[i][0] = 0;
            }
        }
    }
};

// Solution 3:

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int col0 = 1, rows = matrix.size(), cols = matrix[0].size();
        for(int i=0;i<rows;i++) {
            if(matrix[i][0] == 0) col0 = 0;
            for(int j=1;j<cols;j++) {
                if(matrix[i][j] == 0) {
                    matrix[i][0] = matrix[0][j] = 0;
                }
            }
        }
        for(int i=rows-1;i>=0;i--) {
            for(int j=cols-1;j>=1;j--) {
                if(matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
            if(col0 == 0) matrix[i][0] = 0;
        }
    }
};
