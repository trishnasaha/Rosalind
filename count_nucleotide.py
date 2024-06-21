# take file name as input
fname = input("Enter file name: ")

fh = open(fname, 'r') # open and read file
# read line from file
strand = fh.readline()

# count number of A, T, G, C using python count function
a_count = strand.count('A')
t_count = strand.count('T')
g_count = strand.count('G')
c_count = strand.count('C')

print (str(a_count) + ' ' + str(c_count) + ' ' + str(g_count) + ' ' + str(t_count))

# index = len(strand) -1
# A = 0
# T = 0
# G = 0
# C = 0
# while index > -1:
#     for j in strand[index]:
#         if j == A:
#             A += 1
#         elif j == T:
#             T += 1
#         elif j == G:
#             G += 1
#         elif j == C:
#             C += 1
# index = index -1
# print(str(A) + ' ' + str(T) + ' ' + str(G) + ' ' + str(C))

# DNAseq = raw_input("enter a DNA sequence : ")
# seqlength = len(DNAseq)

# basekey = list(set(DNAseq))

# Dict = {}

# for char in basekey:
#     Dict[char] = DNAseq.count(char)
# print Dict


