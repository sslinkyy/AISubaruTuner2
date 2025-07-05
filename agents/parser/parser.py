# parser.py
"""
Parse a 16-bit Subaru ROM using Carberry XML definitions.
"""

import xml.etree.ElementTree as ET
import struct

def parse_rom(rom_path: str, xml_defs_path: str) -> dict:
    """
    Reads binary and XML, returns a dict with:
      - tables: List[Dict] of { name: str, dims: [rows, cols], data: List[List[float]] }
      - scalars: Dict of { name: float }
    """
    # Load XML definitions
    tree = ET.parse(xml_defs_path)
    root = tree.getroot()

    # Read ROM binary
    with open(rom_path, 'rb') as f:
        rom = f.read()

    tables = []
    scalars = {}

    # Namespace handling if needed
    ns = {'c': root.tag.split('}')[0].strip('{')}

    # Parse all <Table> elements
    for tbl in root.findall('.//c:Table', ns):
        name = tbl.get('Name')
        start = int(tbl.find('c:Start', ns).text, 0)
        length = int(tbl.find('c:Length', ns).text, 0)
        cols = int(tbl.find('c:Columns', ns).text)
        rows = int(tbl.find('c:Rows', ns).text)
        scale = float(tbl.find('c:Scale', ns).text)
        offset = float(tbl.find('c:Offset', ns).text)

        # Extract raw bytes and unpack as 16-bit unsigned ints
        raw = rom[start:start+length]
        fmt = '>' + 'H' * (length // 2)
        vals = struct.unpack(fmt, raw)

        # Convert to scaled floats and shape into 2D list
        data = []
        for r in range(rows):
            row = []
            for c_idx in range(cols):
                idx = r * cols + c_idx
                v = vals[idx] * scale + offset
                row.append(v)
            data.append(row)

        tables.append({'name': name, 'dims': [rows, cols], 'data': data})

    return {'tables': tables, 'scalars': scalars}