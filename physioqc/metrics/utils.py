"""Miscellaneous utility functions for metric calculation."""
import logging

LGR = logging.getLogger(__name__)
LGR.setLevel(logging.INFO)


def print_metric_call(metric, args):
    """
    Log a message to describe how a metric is being called.

    Parameters
    ----------
    metric : function
        Metric function that is being called
    args : dict
        Dictionary containing all arguments that are used to parametrise metric

    Notes
    -----
    Outcome
        An info-level message for the logger.
    """
    msg = f"The {metric} regressor will be computed using the following parameters:"

    for arg in args:
        msg = f"{msg}\n    {arg} = {args[arg]}"

    msg = f"{msg}\n"

    LGR.info(msg)


def physio_or_numpy(signal):
    """
    Return data from a peakdet.physio.Physio object or a np.ndarray-like object.

    Parameters
    ----------
    data : peakdet.physio.Physio, np.ndarray, or list
        object to get data from

    Returns
    -------
    np.ndarray-like object
        Either a np.ndarray or a list
    """
    if hasattr(signal, "history"):
        signal = signal.data

    return signal
