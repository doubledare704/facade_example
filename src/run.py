import logging

from src.dtos import ComputerDto
from src.facades import get_main_facade


def main():
    facade = get_main_facade()
    dto = ComputerDto(
        cpu_name="amd",
        cpu_cores=4,
        cpu_threads=4,
        board_name="msi",
        board_socket="am4",
        board_chipset="b550",
        gpu_name="nvidia",
        gpu_type_of_memory="gddr5",
        gpu_video_memory_amount=12000,
    )
    facade.create_computer(dto)
    dto.cpu_cores = 6
    dto.cpu_threads = 6
    facade.create_computer(dto)
    dto.cpu_cores = 6
    dto.cpu_threads = 12
    facade.create_computer(dto)
    dto.cpu_cores = 12
    dto.cpu_threads = 24
    facade.create_computer(dto)
    dto.cpu_cores = 16
    dto.cpu_threads = 32
    facade.create_computer(dto)

    all_parts = facade.get_all_pc_parts()
    logging.warning(f"All parts: {all_parts}")


if __name__ == "__main__":
    main()
