from dataclasses import dataclass


@dataclass
class ComputerDto:
    cpu_name: str
    cpu_cores: int
    cpu_threads: int
    board_name: str
    board_socket: str
    board_chipset: str
    gpu_name: str
    gpu_type_of_memory: str
    gpu_video_memory_amount: int
