# for i in range(1,6):              
#     for j in range(1,6):
#         if(j<=i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    

#     print() 
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(1,6):
#         if(j>=6-i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()  

#         *
#       * *
#     * * * 
#   * * * * 
# * * * * *

# for i in range(1,6):
#     for j in range(1,6):
#         if(j<=6-i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ") 
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *               

# for i in range(1,6):
#     for j in range(1,6):
#         if(j>=i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()          

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# for i in range(1,6):
#     for j in range(1,10):
#         if( j>=6-i and j<=4+i):    
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()             

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# for i in range(1,6):
#     for j in range(1,8):
#         if(j>=i and j<=8-i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#  * * * * * * *
#    * * * * *
#      * * * 
#        *        

# for i in range(1,5):
#     for j in range(1,8):
#         if(j<=5-i or j>=3+i):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()            

#   * * * * * * *
#   * * *   * * *
#   * *       * *
#   *           *

# for i in range(1,8):
#     for j in range(1,5):
#         if(j<=5-i or j<=i-3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()   

#  * * * *
#  * * *
#  * *
#  *
#  * *
#  * * *
#  * * * *    

# for i in range(1,8):
#     for j in range(1,5):
#         if(j>=5-i and j>=i-3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()       

#             *
#           * *
#         * * * 
#       * * * *
#         * * *
#           * *
#             *

# for i in range(1,5):
#     for j in range(1,5):
#         if(j<=i):
#             print(j,end=" ")    
#         else:
#             print(" ",end=" ")
#     print()       

#     1 
#     1 2
#     1 2 3
#     1 2 3 4


# k=int(1)
# for i in range(1,5):
#     for j in range(1,5):
#         if(j<=i):
#             print(k,end=" ") 
#             k=k+1   
#         else:
#             print(" ",end=" ")
#     print()        

#     1 
#     2 3
#     4 5 6
#     7 8 9 10

# k=ord("A")
# for i in range(1,5):
#     for j in range(1,5):
#         if(j<=i):
#             print(chr(k),end=" ")  
#             k=k+1
            
#         else:
#             print(" ",end=" ")
#     print()   

    # A
    # B C 
    # D E F
    # G H I I



# for i in range(1,5):
#     k=ord("A")
#     for j in range(1,5):
#         if(j<=i):
#             print(chr(k),end=" ")  
#             k=k+1
            
#         else:
#             print(" ",end=" ")
#     print()   

#     A
#     A B
#     A B C 
#     A B C D
