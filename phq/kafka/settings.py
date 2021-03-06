def consumer_base_configuration():
    return {
        'auto.offset.reset': 'latest',
        'fetch.max.bytes': 1048576,
        'request.timeout.ms': 305000,
        'heartbeat.interval.ms': 3000,
        'session.timeout.ms': 10000,
        'max.poll.interval.ms': 300000,
        'queued.max.messages.kbytes': 10000,  # Internal queue size in Kbytes which determine the size of the internal buffer per topic/partition
        'enable.auto.commit': False,  # Following default convention
        'queued.min.messages': 100  # overide default configuration of 100000
    }.copy()


def producer_base_configuration():
    return {
        'compression.type': 'snappy',
        'acks': -1,
        'retries': 3
    }.copy()
