#This can be run with any amount of processes
#Master node will import data file as numpy array
#Array will be scattered evenly amongst nodes
#code at bottom will parse through array and locate 11 and the index it resides
#code will then stop and let us know their position (index)


from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

sendbuf = None

# master process
if rank == 0:
    sendbuf = np.loadtxt('data', dtype='i')


recvbuf = np.empty(size)
comm.Scatter(sendbuf, recvbuf, root=0)

index = np.where(sendbuf == 11)
if index[0] in sendbuf:
    print("Element with value 11 exists at following index", index[0], sep='\n')
else:
    print("Process %d ended at index %d" % (rank,  ))
