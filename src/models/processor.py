__all__ = [
    "ProcessorModel",
    "get_proc_repo",
    "ProcessorRepo",
]

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ProcessorModel:
    name: str
    cores: int
    threads: int


global_processors: List[ProcessorModel] = []


class ProcessorRepo:
    """
    The source of data for services, methods are used only by services.
    At this layer, class doesn't know about facades and only does work related to data.
    CRUD queries, filtering, deletion are made here.
    """

    def add_new_proc(self, name: str, cores: int, threads: int) -> ProcessorModel:
        proc = ProcessorModel(
            name=name,
            cores=cores,
            threads=threads,
        )
        global_processors.append(proc)
        return proc

    def filter_by_cores(self, min_cores: int, max_cores: int) -> Optional[List[ProcessorModel]]:
        res = []
        for i in global_processors:
            if min_cores <= i.cores <= max_cores:
                res.append(i)
        return res

    def filter_by_threads(self, min_thr: int, max_thr: int) -> Optional[List[ProcessorModel]]:
        res = []
        for i in global_processors:
            if min_thr <= i.threads <= max_thr:
                res.append(i)
        return res

    def get_all(self) -> List[ProcessorModel]:
        return global_processors


def get_proc_repo() -> ProcessorRepo:
    return ProcessorRepo()
