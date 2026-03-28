"""
Allen-Bradley / Rockwell Automation Publication Catalog
========================================================
Organized by product family with pub type and number.
Types:
  um  = User Manual
  rm  = Reference Manual
  pm  = Programming Manual
  in  = Installation Instructions
  qr  = Quick Reference
  td  = Technical Data
  ap  = Application Note
  pp  = Product Profile
  sr  = Selection Guide
"""

PUBLICATIONS = {

    # ─────────────────────────────────────────────
    # CONTROLLOGIX
    # ─────────────────────────────────────────────
    "controllogix": [
        ("um", "1756-um001"),   # ControlLogix System User Manual
        ("um", "1756-um543"),   # ControlLogix 5580 Controllers User Manual
        ("um", "1756-um535"),   # ControlLogix 5570 Controllers User Manual
        ("rm", "1756-rm003"),   # Logix5000 General Instructions Ref
        ("rm", "1756-rm006"),   # Logix5000 Procedures Ref
        ("rm", "1756-rm085"),   # Logix5000 Motion Ref
        ("rm", "1756-rm094"),   # Logix5000 Tasks Programs Routines Ref
        ("pm", "1756-pm001"),   # Logix5000 Import Export Reference
        ("um", "1756-um009"),   # ControlLogix EtherNet/IP Communication
        ("um", "1756-um004"),   # ControlLogix System Selection Guide
        ("in", "1756-in001"),   # ControlLogix Chassis Installation
        ("um", "1756-um560"),   # GuardLogix 5580 Safety Controllers
        ("um", "1756-um020"),   # GuardLogix Controllers User Manual
        ("qr", "1756-qr107"),   # ControlLogix Quick Reference
        ("um", "1756-um523"),   # ControlLogix 5560 User Manual
    ],

    # ─────────────────────────────────────────────
    # COMPACTLOGIX
    # ─────────────────────────────────────────────
    "compactlogix": [
        ("um", "1769-um011"),   # CompactLogix 5370 User Manual
        ("um", "1769-um006"),   # CompactLogix L3x Controllers
        ("um", "1769-um021"),   # CompactLogix 5380 Controllers
        ("um", "1769-um022"),   # CompactLogix 5480 Controllers
        ("um", "1769-um040"),   # Compact GuardLogix 5380 Safety
        ("in", "1769-in113"),   # CompactLogix 5380 Installation
        ("um", "1769-um002"),   # CompactLogix Communication Modules
        ("td", "1769-td005"),   # CompactLogix L3x Technical Data
        ("td", "1769-td007"),   # CompactLogix 5370 Technical Data
    ],

    # ─────────────────────────────────────────────
    # MICRO800 / MICROLOGIX
    # ─────────────────────────────────────────────
    "micro800": [
        ("um", "2080-um002"),   # Micro820 Controller User Manual
        ("um", "2080-um004"),   # Micro830/850/870 User Manual
        ("um", "2080-um009"),   # Micro870 Controller User Manual
        ("rm", "2080-rm001"),   # Micro800 Instructions Ref
        ("in", "2080-in001"),   # Micro830 Installation Instructions
        ("um", "2080-um003"),   # Connected Components Workbench
    ],
    "micrologix": [
        ("um", "1766-um001"),   # MicroLogix 1400 User Manual
        ("um", "1764-um001"),   # MicroLogix 1500 User Manual
        ("um", "1762-um001"),   # MicroLogix 1200 User Manual
        ("um", "1763-um001"),   # MicroLogix 1100 User Manual
        ("rm", "1766-rm001"),   # MicroLogix 1400 Instruction Set
    ],

    # ─────────────────────────────────────────────
    # SLC-500 / PLC-5 (Legacy)
    # ─────────────────────────────────────────────
    "slc500": [
        ("um", "1747-um011"),   # SLC 500 Modular Hardware Style
        ("rm", "1747-rm001"),   # SLC 500 Instruction Set Ref
        ("um", "1747-um009"),   # SLC 500 Fixed Hardware Style
        ("in", "1746-in001"),   # SLC 500 I/O Modules Installation
        ("um", "1747-um005"),   # SLC 500 Communication Protocols
    ],
    "plc5": [
        ("um", "1785-um012"),   # PLC-5 Programmable Controllers
        ("rm", "1785-rm001"),   # PLC-5 Instruction Set Ref
        ("um", "1785-um013"),   # PLC-5 EtherNet Interface
    ],

    # ─────────────────────────────────────────────
    # POWERFLEX DRIVES
    # ─────────────────────────────────────────────
    "powerflex_520_series": [
        ("um", "520-um001"),    # PowerFlex 520 User Manual
        ("um", "520-um002"),    # PowerFlex 525 User Manual
        ("um", "520-um003"),    # PowerFlex 523 User Manual
        ("rm", "520-rm001"),    # PowerFlex 520 Reference Manual
        ("in", "520-in001"),    # PowerFlex 520 Installation
        ("qr", "520-qr001"),    # PowerFlex 520 Quick Reference
    ],
    "powerflex_700": [
        ("um", "20b-um001"),    # PowerFlex 700 User Manual
        ("rm", "20b-rm001"),    # PowerFlex 700 Reference Manual
        ("in", "20b-in001"),    # PowerFlex 700 Installation
        ("um", "20b-um002"),    # PowerFlex 700S User Manual
        ("qr", "20b-qr001"),    # PowerFlex 700 Quick Reference
    ],
    "powerflex_750_series": [
        ("um", "750-pm001"),    # PowerFlex 750 Programming Manual
        ("rm", "750-rm002"),    # PowerFlex 750 Reference Manual
        ("um", "750-um001"),    # PowerFlex 755 User Manual
        ("um", "750-um004"),    # PowerFlex 753 User Manual
        ("in", "750-in001"),    # PowerFlex 750 Installation
        ("qr", "750-qr001"),    # PowerFlex 750 Quick Reference
        ("um", "750-um100"),    # PowerFlex 755T User Manual
        ("rm", "750-rm100"),    # PowerFlex 755T Reference
    ],
    "powerflex_400": [
        ("um", "22c-um001"),    # PowerFlex 400 User Manual
        ("rm", "22c-rm001"),    # PowerFlex 400 Reference Manual
    ],
    "powerflex_4": [
        ("um", "22a-um001"),    # PowerFlex 4 User Manual
        ("um", "22b-um001"),    # PowerFlex 40 User Manual
        ("um", "22f-um001"),    # PowerFlex 4M User Manual
    ],

    # ─────────────────────────────────────────────
    # KINETIX SERVO DRIVES
    # ─────────────────────────────────────────────
    "kinetix_5700": [
        ("um", "2198-um001"),   # Kinetix 5700 User Manual
        ("rm", "2198-rm001"),   # Kinetix 5700 Reference Manual
        ("in", "2198-in001"),   # Kinetix 5700 Installation
        ("um", "2198-um002"),   # Kinetix 5700 Single Axis
    ],
    "kinetix_5500": [
        ("um", "2094-um001"),   # Kinetix 5500 User Manual
        ("rm", "2094-rm001"),   # Kinetix 5500 Reference Manual
        ("in", "2094-in001"),   # Kinetix 5500 Installation
    ],
    "kinetix_6500": [
        ("um", "2094-um002"),   # Kinetix 6500 User Manual
        ("rm", "2094-rm002"),   # Kinetix 6500 Reference Manual
    ],
    "kinetix_6000": [
        ("um", "2094-um001"),   # Kinetix 6000 User Manual
        ("in", "2094-in001"),   # Kinetix 6000 Installation
    ],
    "kinetix_300": [
        ("um", "2097-um001"),   # Kinetix 300 User Manual
        ("in", "2097-in001"),   # Kinetix 300 Installation
    ],

    # ─────────────────────────────────────────────
    # ETHERNET/IP & COMMUNICATION MODULES
    # ─────────────────────────────────────────────
    "ethernet_ip": [
        ("um", "enet-um001"),   # EtherNet/IP Communication Modules
        ("um", "enet-um006"),   # EtherNet/IP Network Config
        ("um", "1756-um050"),   # ControlLogix EtherNet/IP Bridge
        ("rm", "enet-rm002"),   # EtherNet/IP Reference Manual
        ("in", "1756-in050"),   # 1756-EN2T Installation
        ("um", "1783-um006"),   # Stratix 5700 Switch User Manual
        ("um", "1783-um007"),   # Stratix 5900 User Manual
        ("um", "1783-um014"),   # Stratix 5400 User Manual
    ],
    "devicenet": [
        ("um", "dnet-um004"),   # DeviceNet Network Config
        ("rm", "dnet-rm002"),   # DeviceNet Reference Manual
        ("um", "1756-um010"),   # ControlLogix DeviceNet Module
    ],
    "controlnet": [
        ("um", "cnet-um001"),   # ControlNet Network Config
        ("rm", "cnet-rm001"),   # ControlNet Reference Manual
    ],

    # ─────────────────────────────────────────────
    # PANELVIEW / HMI
    # ─────────────────────────────────────────────
    "panelview_plus": [
        ("um", "2711p-um001"),  # PanelView Plus 7 User Manual
        ("um", "2711p-um006"),  # PanelView Plus 6 User Manual
        ("um", "2711p-um010"),  # PanelView Plus 7 Standard
        ("rm", "2711p-rm001"),  # FactoryTalk View ME Reference
        ("in", "2711p-in001"),  # PanelView Plus Installation
    ],
    "panelview_800": [
        ("um", "2711r-um001"),  # PanelView 800 User Manual
        ("in", "2711r-in001"),  # PanelView 800 Installation
    ],

    # ─────────────────────────────────────────────
    # SAFETY
    # ─────────────────────────────────────────────
    "safety": [
        ("um", "1791es-um001"), # GuardLogix Safety Application
        ("rm", "1791es-rm001"), # Safety Reference Manual
        ("um", "440c-um001"),   # Guard Master Safety Relay
        ("um", "440r-um001"),   # MSR Safety Relay Modules
        ("um", "1732ds-um001"), # ArmorBlock Guard I/O
        ("ap", "safety-at001"), # Safety Application Techniques
        ("um", "1756-um056"),   # ControlLogix SIL2 Safety
    ],

    # ─────────────────────────────────────────────
    # FACTORYTALK / SOFTWARE
    # ─────────────────────────────────────────────
    "factorytalk_view": [
        ("um", "viewme-um004"),  # FactoryTalk View ME
        ("um", "viewse-um006"),  # FactoryTalk View SE
        ("rm", "viewme-rm001"),  # FactoryTalk View ME Reference
        ("um", "ftlogview-um001"), # FactoryTalk Logix View
    ],
    "studio_5000": [
        ("um", "9324-um001"),   # Studio 5000 Logix Designer
        ("rm", "9324-rm001"),   # Logix Designer Reference
        ("um", "9324-um006"),   # Studio 5000 View Designer
    ],

    # ─────────────────────────────────────────────
    # I/O MODULES
    # ─────────────────────────────────────────────
    "controllogix_io": [
        ("um", "1756-um058"),   # ControlLogix Analog I/O
        ("um", "1756-um009"),   # ControlLogix Digital I/O
        ("in", "1756-in579"),   # 1756-IB16 Installation
        ("in", "1756-in580"),   # 1756-OB16 Installation
        ("um", "1756-um014"),   # ControlLogix HART Analog
    ],
    "flex_io": [
        ("um", "1794-um001"),   # FLEX I/O Selection Guide
        ("um", "1794-um002"),   # FLEX I/O Digital Modules
        ("um", "1794-um003"),   # FLEX I/O Analog Modules
    ],
    "point_io": [
        ("um", "1734-um001"),   # POINT I/O System
        ("um", "1734-um013"),   # POINT I/O EtherNet/IP Adapter
        ("in", "1734-in001"),   # POINT I/O Installation
    ],

    # ─────────────────────────────────────────────
    # MOTION
    # ─────────────────────────────────────────────
    "motion": [
        ("rm", "motion-rm003"), # Logix5000 Motion Instructions
        ("um", "motion-um001"), # CIP Motion Configuration
        ("ap", "motion-ap001"), # Motion Application Guide
        ("um", "2198-um004"),   # iTrak System User Manual
    ],

    # ─────────────────────────────────────────────
    # OVERLOADS / MOTOR CONTROL
    # ─────────────────────────────────────────────
    "motor_control": [
        ("um", "193-um002"),    # E300 Electronic Overload Relay
        ("um", "193-um001"),    # E1 Plus Electronic Overload
        ("um", "150-um011"),    # SMC-50 Smart Motor Controller
        ("um", "150-um009"),    # SMC Flex User Manual
        ("um", "284-um001"),    # ArmorStart Distributed Motor
    ],
}

# Flat list for easy iteration
def get_all_publications():
    """Returns list of (family, pub_type, pub_num) tuples."""
    all_pubs = []
    for family, pubs in PUBLICATIONS.items():
        for pub_type, pub_num in pubs:
            all_pubs.append((family, pub_type, pub_num))
    return all_pubs

def get_family_publications(family_name):
    """Returns publications for a specific product family."""
    return PUBLICATIONS.get(family_name, [])

def list_families():
    """Returns all available product families."""
    return list(PUBLICATIONS.keys())