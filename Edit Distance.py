# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:01:25 2019

@author: Mikef
"""

def edit_distance(original, editing):
    original = original.lower()
    editing = editing.lower()
    comparison_matrix = []
    for item in range(len(original) + 1):
        comparison_matrix.append([])
        for letter in range(len(editing) + 1):
            comparison_matrix[item].append(0)
            
            
    for shelf in range(len(comparison_matrix)):
        comparison_matrix[shelf][0] = shelf
    for item in range(len(comparison_matrix[0])):
        comparison_matrix[0][item] = item
    
    for shelf in range(1, len(comparison_matrix)):
        for item in range(1, len(comparison_matrix[shelf])):
            if original[shelf - 1] == editing[item - 1]:
                comparison_matrix[shelf][item] = comparison_matrix[shelf - 1][item - 1]
            else:
                if comparison_matrix[shelf - 1][item] < comparison_matrix[shelf - 1][item - 1] and comparison_matrix[shelf - 1][item] < comparison_matrix[shelf][item - 1]:
                    comparison_matrix[shelf][item] = comparison_matrix[shelf - 1][item] + 1
                elif comparison_matrix[shelf - 1][item - 1] < comparison_matrix[shelf][item - 1]:
                    comparison_matrix[shelf][item] = comparison_matrix[shelf - 1][item - 1] + 1
                else:
                    comparison_matrix[shelf][item] = comparison_matrix[shelf][item - 1] + 1
    return comparison_matrix[-1][-1]

def main():
    print(edit_distance("Spoopiness", "Poopies"))
    


if __name__ == "__main__":
    main()