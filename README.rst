ARTIQ network device support package for the PXI 6733 DAC hardware
==================================================================

Warning: This experimental software is provided "as-is". It is untested and
unmaintained, and is likely to contain bugs.


The controller gives network access to the PXI6733 card.

The mediator provides a wavesynth-like interface (similar to the PDQ), handles
loading of waveforms by connecting to the controller, and triggers samples
using a RTIO TTL clock generator. The hardware must be set up in a way that
each TTL pulse triggers the output of one DAC sample.


To use the controller you need first to install the NI-DAQmx driver from
http://www.ni.com/downloads/ni-drivers/f/.

Then you also need to install PyDAQmx python module::

    $ git clone https://github.com/clade/PyDAQmx
    $ cd PyDAQmx
    $ C:\Python34\Tools\Scripts\2to3.py -w .
    $ python3.5 setup.py build
    $ python3.5 setup.py install

Then, you can run the PXI6733 controller::

    $ pxi6733_controller -d Dev1

Then, send a load_sample_values command to it via the ``artiq_rpctool`` utility::

    $ artiq_rpctool ::1 3256 list-targets
    Target(s):   pxi6733
    $ artiq_rpctool ::1 3256 call load_sample_values 'np.array([1.0, 2.0, 3.0, 4.0], dtype=float)'

This loads 4 voltage values as a numpy float array: 1.0 V, 2.0 V, 3.0 V, 4.0 V

Then the device is set up to output those samples at each rising edge of the clock.


Copyright (C) 2015-2016 M-Labs Limited. Licensed under GNU GPL version 3.
