"""
Created on Tue Nov  2 16:38:33 2021

@author: Elessar
"""

import numpy as np

matrix = np.random.randint(2, size=(4,4)) #4x4 matrix contains random 0s and 1s.

print("Matrix:")
print(matrix)
print("*****************")

   
location_x = np.random.randint(0,4) #Agent's random x position
location_y = np.random.randint(0,4) #Agent's random y position

def move(location_x,location_y,matrix):
    old_loc_x=0
    old_loc_y=0
    
    moves_count=0
        
    while np.count_nonzero(matrix) != 0 :  #Runs until all elements are 0
               
                print("Agent has the location ",location_x,location_y)
                moves_count += 1
                
                print(matrix)
                    
                if matrix[location_x][location_y] == 1 : #If the agent sees 1 in its position, it turns it into 0.
                    matrix[location_x][location_y] = 0
                    print("1 turn 0 in Location: ", location_x,location_y)
            
            #To understand the agent's random movement, we assign the location to the old location before the location changes.    
                old_loc_x= location_x 
                old_loc_y= location_y           
            
            #The agent's location changes.       
                location_x = np.random.randint(0,4)
                location_y = np.random.randint(0,4)
            
           
            #With the conditions here, we understand the direction of the agent's random movement.
                if location_x > old_loc_x :
                    print("Agent moves Down ")
                    
                    if location_y > old_loc_y :
                        print("and Right ! ")
                    elif location_y < old_loc_y :
                        print("and Left ! ")
                                     
                elif location_x < old_loc_x :
                    print("Agent moves Up ")
                    
                    if location_y > old_loc_y :
                        print("and Right ! ")
                    elif location_y < old_loc_y :
                        print("and Left ! ")
                        
                elif location_x == old_loc_x :
                    if location_y > old_loc_y :
                        print("Agent moves Right ! ")
                    elif location_y < old_loc_y :
                        print("Agent moves Left ! ")
                print("-------------------")
    print("Total Moves to clean the whole place: ", moves_count)

move(location_x,location_y,matrix)
print("Clean Area: ")
print(matrix)







                                      