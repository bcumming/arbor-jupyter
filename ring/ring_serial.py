import sys
import arbor

class ring_recipe (arbor.recipe):

    def __init__(self, n=4):
        # The base C++ class constructor must be called first, to ensure that
        # all memory in the C++ class is initialized correctly.
        arbor.recipe.__init__(self)
        self.ncells = n
        self.params = arbor.cell_parameters()

    # The num_cells method that returns the total number of cells in the model
    # must be implemented.
    def num_cells(self):
        return self.ncells

    # The cell_description method returns a cell
    def cell_description(self, gid):
        return arbor.make_cable_cell(gid, self.params)

    def num_targets(self, gid):
        return 1

    def num_sources(self, gid):
        return 1

    # The kind method returns the type of cell with gid.
    # Note: this must agree with the type returned by cell_description.
    def cell_kind(self, gid):
        return arbor.cell_kind.cable

    # Make a ring network
    def connections_on(self, gid):
        src = (gid-1)%self.ncells
        w = 0.01
        d = 10
        return [arbor.connection(arbor.cell_member(src,0), arbor.cell_member(gid,0), w, d)]

    # Attach a generator to the first cell in the ring.
    def event_generators(self, gid):
        if gid==0:
            sched = arbor.explicit_schedule([1])
            return [arbor.event_generator(arbor.cell_member(0,0), 0.1, sched)]
        return []

nthreads=1
context = arbor.context(threads=nthreads, gpu_id=None)

meters = arbor.meter_manager()
meters.start(context)

# Create a recipe
recipe = ring_recipe(1000)
meters.checkpoint('recipe-create', context)     # checkpoint

# Perform decomposition
decomp = arbor.partition_load_balance(recipe, context)
meters.checkpoint('load-balance', context)      # checkpoint

# Create the simulation
sim = arbor.simulation(recipe, decomp, context)
# Attach a spike recorder
recorder = arbor.attach_spike_recorder(sim)
meters.checkpoint('simulation-init', context)   # checkpoint

# Run the simulation for 100ms
sim.run(10)
meters.checkpoint('simulation-run', context)    # checkpoint

# Print the spikes
print('{:>5s}{:>10s}'.format('gid', 'time(ms)'))
for s in recorder.spikes:
    print('{:5d}{:10.3f}'.format(s.source.gid, s.time))

# Print a performance report
report = arbor.meter_report(meters, context)
print(report)

