from bfs import BFS
from ids import IDS

test_set = ['test_00.txt', 'test_01.txt', 'test_02.txt', 'test_03.txt']

#Testing BFS
print("****************** Testing BFS algorithm on the Test Set ******************")
print("----------------------------------------------------------------------------")
for i in range(len(test_set)):
     alg = BFS(test_set[i])
     output, time_taken, states_seen = alg.run()
     print("Running Test " + str(i + 1) + ":")
     print("output: " + output)
     print("output cost: " + str(len(output)))
     print("We have seen " + str(states_seen) + " states")
     print("Execution Time: " + str(int(time_taken*1000)) + " ms")


print("----------------------------------------------------------------------------")

#Testing IDS
print("****************** Testing IDS algorithm on the Test Set ******************")
print("----------------------------------------------------------------------------")
for i in range(len(test_set)):
    alg = IDS(test_set[i])
    output, time_taken, states_seen = alg.run()
    print("Running Test " + str(i + 1) + ":")
    print("output: " + output)
    print("output cost: " + str(len(output)))
    print("We have seen " + str(states_seen) + " states")
    print("Execution Time: " + str(int(10*time_taken)/10) + " s")

print("----------------------------------------------------------------------------")