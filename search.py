from mpi4py import MPI
import numpy as np

# describes all processes started by mpiexec
comm = MPI.COMM_WORLD

# gives a process an int id
rank = comm.Get_rank()

# the number of processes in the group (mpi.comm_world)
size = comm.Get_size()

sendbuf = None

# master process
if rank == 0:
    sendbuf = np.loadtxt('data', dtype='i')
    np.array_split(sendbuf, 4)
    print(sendbuf)
    #newbuf = np.array_split(sendbuf,4)
else:
    sendbuf = None

recvbuf = np.empty(int(40000/size), dtype='i')
comm.Scatter(sendbuf, recvbuf, root=0)
print('recvbuf on rank %d is: %s' % (rank,recvbuf))
