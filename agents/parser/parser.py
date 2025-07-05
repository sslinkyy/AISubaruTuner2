# parser.py
"""
Parse a 16-bit Subaru ROM using Carberry XML definitions.
"""

def parse_rom(rom_path: str, xml_defs_path: str) -> dict:
    """
    Reads the binary and XML, returns a dict with:
      - tables: { name: str, dims: [int, int], data: List[List[float]] }
      - scalars: { name: str, value: float }
    """
    # TODO: implement parsing logic
    return {}