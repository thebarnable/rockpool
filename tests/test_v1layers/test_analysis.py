"""
Test analysis methods
"""

import numpy as np
from rockpool import TSEvent
from rockpool.analysis import lv, fano_factor


def test_lv_FF():
    # generate Poisson spike train

    numNeurons = 100
    numSpikes = 1000

    inter_spk_intvls = -np.log(np.random.rand(numNeurons, numSpikes))
    spikeTimes = np.array([np.cumsum(isi) for isi in inter_spk_intvls])
    nids = np.array([[i] * numSpikes for i in range(numNeurons)])

    # cut to min time
    minTime = np.min(spikeTimes[:, -1])
    nids = np.array([nids[i][train <= minTime] for i, train in enumerate(spikeTimes)])
    spikeTimes = np.array([train[train <= minTime] for train in spikeTimes])

    spikeTimes = np.hstack(spikeTimes)
    nids = np.hstack(nids)

    order = np.argsort(spikeTimes)
    spikeTimes = spikeTimes[order]
    nids = nids[order]

    tse = TSEvent(spikeTimes, nids, t_stop=spikeTimes[-1] + 0.001)

    assert np.abs(lv(tse).all() - 1) < 0.001
    assert np.abs(fano_factor(tse).all() - 1) < 0.001


def test_entropy():
    from rockpool import TSEvent
    import numpy as np

    # generate Poisson spike train

    numNeurons = 10
    numSpikes = 100

    inter_spk_intvls = -np.log(np.random.rand(numNeurons, numSpikes))
    spikeTimes = np.array([np.cumsum(isi) for isi in inter_spk_intvls])
    nids = np.array([[i] * numSpikes for i in range(numNeurons)])

    # cut to min time
    minTime = np.min(spikeTimes[:, -1])
    nids = np.array([nids[i][train <= minTime] for i, train in enumerate(spikeTimes)])
    spikeTimes = np.array([train[train <= minTime] for train in spikeTimes])

    spikeTimes = np.hstack(spikeTimes)
    nids = np.hstack(nids)

    order = np.argsort(spikeTimes)
    spikeTimes = spikeTimes[order]
    nids = nids[order]

    tse = TSEvent(spikeTimes, nids, t_stop=spikeTimes[-1] + 0.001)

    assert np.abs(lv(tse).all() - 1) < 0.001
    assert np.abs(fano_factor(tse).all() - 1) < 0.001
