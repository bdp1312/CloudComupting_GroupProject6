from mpi4py import MPI
import numpy as np

# searches for the number 11 in an array, notifies other procs if found, and returns a tuple with index and proc rank
def findTarget(rank, array):
	
	req = comm.irecv(source=MPI.ANY_SOURCE, tag=11)

	isFound = False
	target = None
	
	comm.Barrier()	
	for i in range(len(array)):
		
		if req.Test() == True:
			print("Process of rank %d stopped searching at index %d" % (rank, i))
			return None
			
		if array[i] == 11:
			
			isFound = True
			target = (rank, i)
			
			for r in range(size):
				comm.isend(isFound, dest=r, tag=11)		
			
			return target
		
			
	return target



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
  
else:
    sendbuf = None


# each subarray in recvbuf must be 40k/4 or subArrSize
recvbuf = np.empty(subArrSize, dtype='i')

# Every process will call this, then the root process will scatter the data to all procs including itself
comm.Scatter(sendbuf, recvbuf, root=0)

print('recvbuf on rank %d is: %s' % (rank,recvbuf))

# Every proc calls this on their subarray, seeking a target of 11
target = findTarget(rank, recvbuf)

if (target != None):
    print("Process of rank %d found target of 11 at index %d" % (target[0], target[1]))


		

