from mpi4py import MPI
import numpy as np

# searches for the number 11 in an array, notifies other procs if found, and returns a tuple with index and proc rank
def findTarget(rank, array):
	targetTuple = None
	array.sort()
	
	for i in range(len(array)):
		if array[i] == 11:
			#notifyProcs()
			targetTuple = (rank, i)	
			return targetTuple

		elif array[i] > 11:
			return None

# describes all processes started by mpiexec
comm = MPI.COMM_WORLD

# gives a process an int id
rank = comm.Get_rank()

# the number of processes in the group (mpi.comm_world)
size = comm.Get_size()

subArrSize = int(40000/size)


sendbuf = None

# master process
if rank == 0:
    sendbuf = np.loadtxt('data.txt', dtype='i')
    np.array_split(sendbuf, size)
    #print(sendbuf)

else:
    sendbuf = None


# each subarray in recvbuf must be 40k/4 or subArrSize
recvbuf = np.empty(subArrSize, dtype='i')
comm.Scatter(sendbuf, recvbuf, root=0)
targetTuple = findTarget(rank, recvbuf)
if (targetTuple != None):
    print("Process rank %d found 11 at index %d" % (targetTuple[0], targetTuple[1]))
else:
	print('Process rank %d ended at index %d' % (rank, recvbuf[0]))




		

