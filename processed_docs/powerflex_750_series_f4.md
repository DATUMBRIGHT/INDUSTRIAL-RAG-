<!-- image -->

## PowerFlex 755TM Non-Regenerative Supply

Catalog Number 20J

<!-- image -->

<!-- image -->

## Important User Information

Read this document and the documents listed in the additional resources section about installation, configuration, and operation of this equipment before you install, configure, operate, or maintain this product. Users are required to familiarize themselves with installation and wiring instructions in addition to requirements of all applicable codes, laws, and standards.

Activities including installation, adjustments, putting into service, use, assembly, disassembly, and maintenance are required to be carried out by suitably trained personnel in accordance with applicable code of practice.

If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss.

<!-- image -->

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

IMPORTANT Identifies information that is critical for successful application and understanding of the product.

These labels may also be on or inside the equipment to provide specific precautions.

<!-- image -->

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

<!-- image -->

<!-- image -->

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective Equipment (PPE).

The following icon may appear in the text of this document.

<!-- image -->

Identifies information that is useful and can help to make a process easier to do or easier to understand.

## Table of Contents

|                           | Preface  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                 | . . . . . . . . . . . . . . . . . . 7               |
|---------------------------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
|                           | Summary of Changes. . . . . . . . .  . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . 7                 |
|                           | Terminology. . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  | . . . . . . . . 7                                   |
|                           | Who Should Use This Manual . . .  . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . 7                   |
|                           | Chapter 1                                                                                              |                                                     |
| Product Overview          | Plan Your System . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      | . . . . . . . 11                                    |
|                           | Product Advisories . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                | . . . . . . . . . . . . 15                          |
|                           | Remove Power from the System . . . . . . . . . .                                                       | . . . . . . . . . . . . .  . . . . . . . . . . . 16 |
|                           | Main Control Circuit Board . . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 18                  |
|                           | Product Nameplate. . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . 26                |
|                           | Catalog Number Explanation . . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 27                  |
|                           | Commonly Used Tools. . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .              | . . . . . . . . 30                                  |
|                           | Hardware Installation Diagrams .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . 31                    |
|                           | Fastener Torque Sequences . . . .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . 32                  |
|                           | Chapter 2                                                                                              |                                                     |
| Receiving, Handling, and  | Receiving . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . 33                                  |
| Storage                   | Shipment Configurations. . . . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 35                  |
|                           | Handling. . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . 36                                  |
|                           | Storage . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .     | . . . . . . . . . . . 39                            |
|                           | Chapter 3                                                                                              |                                                     |
| Prepare for Installation  | CE Conformity . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . 41                |
|                           | Location Planning. . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . . 44                        |
|                           | Minimum Clearances and Access Requirements . . . . . . . . . . . . . . . . . . . 47                    |                                                     |
|                           | Installation Site Requirements . .  . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . 50                  |
|                           | Floor Mounting Preparation  . . . . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . . 51                |
|                           | Bay Configurations . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . 58                |
|                           | Approximate Dimensions. . . . . . .  . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . 59                  |
|                           | Chapter 4                                                                                              |                                                     |
| Mechanical and Electrical | Installation of Products with Corrosive Gas Protection (XT). . . . . . . . . 69                        |                                                     |
| Installation              | Remove Shipping Hardware . . . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 70                  |
|                           | Protective Touch Guards. . . . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . . 72                |
|                           | Remove NRS Modules . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . 74                            |
|                           | Attach Floor Mounting Hardware to the Bays . . . . . . . . . . . . . . . . . . . . . . 80              |                                                     |
|                           | Position the First NRS Bay . . . . .  . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . 80                  |
|                           | Add a Bay to the Lineup.   . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . . . . . 81                          |
|                           | Secure and Seal Roof Panels. . .  . . . . . . . . . . . . . . . . . . . . . . . . . . .                | . . . . . . . . 90                                  |
|                           | Affix the Bays to the Floor. . . . . . . . . . . .  . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . 90                        |
|                           | Make NRS Bay-to-Bay Electrical Connections. . . . . . . . . . . . . . . . . . . . . . 90               |                                                     |
|                           | Install NRS Modules. . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . 105                         |

|                           | Chapter 5                                                                                                                                                       |                                                    |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| Power Wiring and System   | AC Supply Source Considerations . . . . . . . .                                                                                                                 | . . . . . . . . . . . . .  . . . . . . . . . . 115 |
| Configuration             | Grounding Requirements. . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                        | . . . . . . . . . . . . . . 115                    |
|                           | Dual Input and Dual Output Power Wiring Requirements . . . . . . . . . 118                                                                                      |                                                    |
|                           | NRS Output Bay Connections to Drive Bays . . . . . . . . . . . . . . . . . . . . . . 119                                                                        |                                                    |
|                           | Power Cable Specifications . . . .  . . . . . . . . . . . . . . . . . .                                                                                         | . . . . . . . . . . . . . . . 121                  |
|                           | Power Cable Connections . . . . . .  . . . . . . . . . . . . . . . . . .                                                                                        | . . . . . . . . . . . . . . . 122                  |
|                           | Recommended Cable Spacing . . . . . . . . . . . . .                                                                                                             | . . . . . . . . . . . . .  . . . . . . . . . 126   |
|                           | Bus Bar Locations . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                                                  | . . . . . . . . . . . . . . . . 129                |
|                           | Control Transformers . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                                                     | . . . . . . . . . . . . . . . 131                  |
|                           | Fuses and Circuit Breakers. . . . .  . . . . . . . . . . . . . . . . . .                                                                                        | . . . . . . . . . . . . . . . 134                  |
|                           | Power Jumper Configuration . . . .  . . . . . . . . . . . . . . . . .                                                                                           | . . . . . . . . . . . . . . 137                    |
|                           | Main Control Circuit Board Configuration . . .                                                                                                                  | . . . . . . . . . . .  . . . . . . . . . 140       |
|                           | System Schematics. . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                 | . . . . . . 143                                    |
|                           | Chapter 6                                                                                                                                                       |                                                    |
| Troubleshooting           | View Status Indicators on the Main Control Circuit Board . . . . . . . . . 147                                                                                  |                                                    |
|                           | Main Control Circuit Board Seven-segment LED Display . . . . . . . . . . 148                                                                                    |                                                    |
|                           | NRS Module Status Indicator . . . .  . . . . . . . . . . . . . . . . .                                                                                          | . . . . . . . . . . . . . . 157                    |
|                           | Input and Output Status Indicators. . . . . . . .                                                                                                               | . . . . . . . . . . . . .  . . . . . . . . . 157   |
|                           | Parallel NRS module Precharge Synchronization. . . . . . . . . . . . . . . . . . 159                                                                            |                                                    |
|                           | Fault and SYNC Signal Diagrams . . . . . . . . . .                                                                                                              | . . . . . . . . . . . . .  . . . . . . . . . 159   |
|                           | Chapter 7                                                                                                                                                       |                                                    |
| Preventive Maintenance    | Maintenance of Industrial Control Equipment.   . . . . . . . . . . .                                                                                            | . . . . . . . . 165                                |
|                           | Maintenance Task Code Explanation . . . . . . .                                                                                                                 | . . . . . . . . . . . .  . . . . . . . . . 168     |
|                           | Recommended Maintenance Schedules . . . . . .                                                                                                                   | . . . . . . . . . . . .  . . . . . . . . 169       |
|                           | Chapter 8                                                                                                                                                       |                                                    |
| Renewal Parts Replacement | Available Renewal Kits. . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                                                            | . . . . . . . . . . . 171                          |
| Instructions              | Remove the Power Bay Protective Guard . . . .                                                                                                                   | . . . . . . . . . . . .  . . . . . . . . . 173     |
|                           | System Communication Interconnect Harness Replacement. . . . . . . 174                                                                                          |                                                    |
|                           | NRS Module N-1 Jumper Replacement . . . . . . . . . . . . . . . . . . . . . . . . . . . 175                                                                     |                                                    |
|                           | Control Transformer T1 Primary Fuses (FH1, FH2) Replacement. . . . 176                                                                                          |                                                    |
|                           | Control Transformer T1 Secondary Fuse (FH3) Replacement . . . . . . . 177                                                                                       |                                                    |
|                           | Control Transformer T2 Primary Fuses (FH4, FH5) Replacement . . . 178                                                                                           |                                                    |
|                           | Control Transformer T2 Secondary Fuse (FH6) Replacement . . . . . . . 179                                                                                       |                                                    |
|                           | IP54/IP21 Power Bay Exhaust Vent Filters Replacement. . . . . . . . . . . . 180                                                                                 |                                                    |
|                           | IP54, 400 mm (15.75 in.) Wide Power Bay Door Vent Filter Replacement . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   | . . . . . . 181                                    |
|                           | IP21, 400 mm (15.75 in.) Wide Power Bay Door Vent Filter Replacement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . .  . . . . . . . 182             |
|                           | IP54/IP21, 400/800 mm (15.75/31.5 in.) Wide Wire Bay Door Vent . . . . . . . . . . . . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . 183                          |
|                           | Filters Replacement . . . . .  IP54/IP21, 400/800 mm (15.75/31.5 in.) Wide Wire Bay Door Vent Exhaust Fan and Filter Assembly Replacement.  . . . . . . . . 184 | . . . . . . . . . . .                              |
|                           | Thermal Switch Replacement . . . .  . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 185                                                          |                                                    |
|                           | Single-Density NRS Module DC Link Fuse Replacement . . . . . . . . . . . 187                                                                                    |                                                    |

| Dual-Density NRS Module DC Link Fuse Replacement . . . . . . . . . . . . 189                               |                                                |
|------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| NRS Module Heatsink Fan Assembly Replacement . . . . . . . . . . . . . . . . 190                           |                                                |
| NRS Module Power Supply Replacement . . . . . . . . . . . . . . . . . . . . . . . . . 192                  |                                                |
| Main Control Circuit Board Replacement . . . . . . . . . . . . . . . . . . . . . . . . 195                 |                                                |
| NRS Module Replacement . .  . . . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . 198            |
| NRS Module AC Input Fuse Replacement . . .                                                                 | . . . . . . . . . . . .  . . . . . . . . . 201 |
| NRS Module DC Bus Capacitor Assembly Replacement . . . . . . . . . . . . 204                               |                                                |
| Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . .213                             |
| Additional Resources . . . .  . . . . . . . . . . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . 219                      |

## Notes:

## Summary of Changes

## Terminology

## Who Should Use This Manual

This manual provides procedures for the mechanical and electrical installation of a PowerFlex® 755TM Non-Regenerative Supply (NRS). This manual includes the basic steps to transport, position, and join the product bays, to make internal electrical connections, to connect AC input power and DC output power, and to wire basic I/O.

This manual provides instructions for an initial product installation. Assembly procedures in chapters 1...4 assume that supply power is not connected. Once the product is connected to a power supply, always verify that system power is not present before performing any work on the product. See safety-related practices that are contained in publication NFPA 70E, Standard for Electrical Safety in the Work Place.

This manual contains new and updated information as indicated in the following table.

| Topic                                                                                   | Page   |
|-----------------------------------------------------------------------------------------|--------|
| Added information about the minimum DC bus capacitance required to power up the NRS. 11 |        |
| Added NRS module input and output connectors to the renewal parts list.                 | 172    |

The term "bay" is used to refer to the assembly that includes both an enclosure and all internal components contained in that enclosure. The term "enclosure" is used to refer to the exterior of the bay, or in some cases another enclosure that is not a bay enclosure.

This manual is intended for two types of personnel:

- Qualified personnel familiar with handling heavy equipment.
- Qualified electricians or other personnel who have experience with electrical terminology, equipment, methods, and safety precautions.

Additional Resources on page 219 is a directory of Rockwell Automation publications that provide detailed drive and bus supply information from wiring and grounding recommendations to troubleshooting and repair.

## Notes:

## Product Overview

The PowerFlex® 755TM Non-Regenerative Supply (NRS) is an Architecture Class bus supply. An NRS system is a customized solution that is built with NRS modules. These modules come in two types based on power output capability, single-density (1X) and dual-density (2X). An NRS dual-density module provides approximately twice the power output of a single-density module or a standard PowerFlex 755TM power module, but is the same physical size. Figure 2 on page 10 shows the internal components of single and dual-density modules.

NRS modules include integral line reactors to support efficient parallel module installations and to build bus supply systems that support PowerFlex 755TM common bus inverters and DC input drives. The customer can build an NRS system with power ratings up to 4000 kW and 6000 Hp by connecting singledensity and dual-density modules in parallel. Figure 1 shows the place of an NRS in an example installation.

Figure 1 - NRS In an Example DC Common Bus Installation

<!-- image -->

1

This publication provides information about the use and installation of the NRS, not the other components of a DC common bus installation. For information about those components, see the publications for those components and Additional Resources on page 219 .

Figure 2 - Internal Components of Single-Density and Dual-Density NRS Modules

Single-Density Module (1X)

<!-- image -->

Dual-Density Module (2X)

<!-- image -->

| Item Description                         |    | Item Description                                                            |
|------------------------------------------|----|-----------------------------------------------------------------------------|
| 1 AC input terminals                     | 5  | DC bus capacitors(1)                                                        |
| 2 AC input fuses                         |    | 6 DC output terminals                                                       |
| 3 Integral line reactor                  | 7  | NRS module power supply (used for internal circuit boards and heatsink fan) |
| 4 Silicon-controlled rectifiers (SCRs) 8 |    | Main control circuit board (not shown for clarity only)                     |

(1) DC bus capacitors are optional, and are sized to complete the required total capacitance when the NRS is paired with PowerFlex 755TM common bus inverter power modules. When DC bus capacitors are not used, only internal DC bus bars are used instead.

## Plan Your System

When planning to build a new NRS system or add modules to an existing NRS system, use the following information:

- Determine your common bus system power needs. Use the data in NRS Module Selection and System Ratings on page 12 and NRS System Configurations on page 14 to plan your NRS system and choose NRS modules to meet your power needs.
- The actual current that is consumed by the bus supply system must not exceed the current rating of the AC bus bars and the actual output current must not exceed the current rating of the DC bus bars. See NRS Module Selection and System Ratings on page 12 .
- Some common bus systems require a back-to-back or inline bay configuration with two entry wire bays and two exit wire bays. See Bay Configurations on page 58 for back-to-back and inline examples. These configurations are required for any system that combines four or more NRS modules in parallel at the following ratings:
- 400/480V above 4100 A (ND)
- 600/690V above 3300 A (ND)
- Systems that include multiple NRS modules in parallel require IP00 interconnect wire harness kits, which enable module-to-module communication for precharge and fault coordination. Systems that consist of a single NRS module require a loop-back jumper on each side of the power bay. See System Communication Interconnection Harnesses on page 96 .
- Coordinated precharge and status communication capabilities support a maximum of six NRS modules in parallel.
- A minimum DC bus capacitance is required to power up the NRS. The design of the final installation must assure that the minimum capacitance is connected whenever the NRS is to be enabled. Calculate the minimum DC bus capacitance for your system as follows:

| Variable Description                                 |
|------------------------------------------------------|
| M Minimum DC bus capacitance                         |
| S Number of single density NRS modules in the system |
| D Number of dual density NRS modules in the system   |

The PowerFlex 755TM non-regenerative supply does not include any internal DC bus capacitance as standard, but systems with internal DC bus capacitors (item 5 in Figure 2 on page 10) are available. If your system does not have internal DC bus capacitors, then to power up the bus supply, you must provide the minimum DC bus capacitance using one of the following methods:

- Connect DC drives or common bus inverters (CBIs) to the DC bus. 110 μF of capacitance is typical of a 5 HP or 3.7 kW drive. Make sure that enough drives or CBIs are connected to the DC bus to achieve the minimum capacitance. To find DC bus capacitances for specific PowerFlex drives, refer to the Drives in Common Bus Configurations with PowerFlex 755TM Bus Supplies Application Technique, publication DRIVES-AT005 .
- If no drives or CBIs are connected to the DC bus, such as during commissioning, provide DC bus capacitance using one or more customer-provided external capacitor banks. Connect external capacitor banks to the DC bus in the same way that a drive is connected to the bus. See Power Wiring and System Configuration on page 115 .

## IMPORTANT

## NRS Module Selection and System Ratings

The following are the base NRS module power bays. All NRS systems include one or more of these bays.

Table 1 - Base NRS Module Power Bays

|   Voltage | Output Amps DC (LD/ND/HD)   | kW Ratings (LD/ND/HD) Input Amps AC (LD/ND/HD) Module Density  Base Cat. No.   |
|-----------|-----------------------------|--------------------------------------------------------------------------------|
|       400 |                             | 518/479/400 799/739/616 959/887/740 1X 20JEHxC770LNANNNNN                      |
|       400 |                             | 938/910/731 1517/1406/1128 1821/1685/1354 2X 20JEHxC1K4LNANNNNN                |
|       480 |                             | 527/529/441 736/681/568 883/817/681 1X 20JEHxD740LNANNNNN                      |
|       480 |                             | 1087/977/812 1398/1256/1044 1678/1507/1253 2X 20JEHxD1K3LNANNNNN               |
|       600 |                             | 518/488/403 534/501/414 640/602/497 1X 20JEHxE545LNANNNNN                      |
|       600 |                             | 986/876/738 1014/901/759 1217/1082/911 2X 20JEHxE980LNANNNNN                   |
|       690 |                             | 596/561/463 534/501/414 640/602/497 1X 20JEHxF505LNANNNNN                      |
|       690 |                             | 1134/1008/849 1014/901/759 1217/1082/911 2X 20JEHxF920LNANNNNN                 |

Table 2 through Table 5 on page 13 provide power ratings for all NRS products, including the following:

- Individual NRS modules (individual ratings also provided in Table 1)
- Parallel NRS module systems, which combine multiple base NRS module power bays

NRS modules do not limit current output. Use these ratings to determine the maximum NRS system power only. For NRS module watts loss data, see the PowerFlex 755TM Non-Regenerative Supply Technical Data, publication 750-TD103 .

The DC output current rating of the bus supply system must not exceed the current rating of the DC bus bars and bus bar splices. See the Extruded DC Bus Bar Derating section in the PowerFlex 755TM Non-Regenerative Supply Technical Data, publication 750-TD103 .

Table 2 - 400V Single and Parallel NRS Module Ratings

|   Voltage | Output Amps DC (LD/ND/HD)   | kW Ratings (LD/ND/HD) Input Amps AC (LD/ND/HD) Quantity of 1X Module Power Bays 1X Module Power Bay Base Cat. No. Quantity of 2X Module Power Bays   | 2X Module Power Bay Base Cat. No.                                     |
|-----------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
|       400 |                             | 518/479/400 799/739/616 959/887/740 1 20JEHxC770LNANNNNN — —                                                                                         |                                                                       |
|       400 |                             |                                                                                                                                                      | 938/910/731 1517/1406/1128 1821/1685/1354 — — 1 20JEHxC1K4LNANNNNN    |
|       400 |                             | 1450/1341/1119 2237/2069/1725 2685/2484/2072 1 20JEHxC770LNANNNNN 1 20JEHxC1K4LNANNNNN                                                               |                                                                       |
|       400 |                             |                                                                                                                                                      | 1916/1772/1479 2956/27342279 3548/3282/2738 — — 2 20JEHxC1K4LNANNNNN  |
|       400 |                             | 2382/2203/1886 3675/3399/2834 4411/4080/3493 1 20JEHxC770LNANNNNN 2 20JEHxC1K4LNANNNNN                                                               |                                                                       |
|       400 |                             |                                                                                                                                                      | 2848/2634/2198 4395/4065/3388 5275/4879/4070 — — 3 20JEHxC1K4LNANNNNN |
|       400 |                             | 2848/2634/2198 4395/4065/3388 5275/4879/4070 2 20JEHxC770LNANNNNN 2 20JEHxC1K4LNANNNNN                                                               |                                                                       |
|       400 |                             |                                                                                                                                                      | 3780/3497/2917 5833/5395/4497 7001/6475/5402 — — 4 20JEHxC1K4LNANNNNN |
|       400 |                             | 4713/4359/3636 7271/6725/5606 8727/8072/6734 2 20JEHxC770LNANNNNN 4 20JEHxC1K4LNANNNNN                                                               |                                                                       |
|       400 | 8727/8072/6734(1)           | 4713/4359/3636(1)  7271/6725/5606(1)  —  —  6                                                                                                        | 20JEHxC1K4LNANNNNN                                                    |
|       400 | 10453/9668/8066(2)          | 5645/5221/4356(2)  —  —  6                                                                                                                           | 8709/8055/6714(2)  20JEHxC1K4LNANNNNN                                 |

## Table 3 - 480V Single and Parallel NRS Module Ratings

|   Voltage | Output Amps DC (LD/ND/HD)   | kW Ratings (LD/ND/HD) Input Amps AC (LD/ND/HD) Quantity of 1X Module Power Bays 1X Module Power Bay Base Cat. No. Quantity of 2X Module Power Bays   | 2X Module Power Bay Base Cat. No.                                     |
|-----------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
|       480 |                             | 527/529/441 736/681/568 883/817/681 1 20JEHxD740LNANNNNN — —                                                                                         |                                                                       |
|       480 |                             |                                                                                                                                                      | 1087/977/812 1398/1256/1044 1678/1507/1253 — — 1 20JEHxD1K3LNANNNNN   |
|       480 |                             | 1603/1482/1236 2061/1907/1590 2473/2288/1907 1 20JEHxD740LNANNNNN 1 20JEHxD1K3LNANNNNN                                                               |                                                                       |
|       480 |                             |                                                                                                                                                      | 2118/1959/1633 2723/2520/2102 3268/3023/2520 — — 2 20JEHxD1K3LNANNNNN |
|       480 |                             | 2633/2435/2132 3386/3133/2613 4063/3758/3290 1 20JEHxD740LNANNNNN 2 20JEHxD1K3LNANNNNN                                                               |                                                                       |
|       480 |                             |                                                                                                                                                      | 3147/2912/2427 4048/3746/3124 4857/4494/3746 — — 3 20JEHxD1K3LNANNNNN |
|       480 |                             | 3147/2912/2427 4048/3746/3124 4857/4494/3746 2 20JEHxD740LNANNNNN 2 20JEHxD1K3LNANNNNN                                                               |                                                                       |
|       480 |                             |                                                                                                                                                      | 4177/3865/3221 5373/4971/4146 6446/5964/4971 — — 4 20JEHxD1K3LNANNNNN |
|       480 |                             | 5207/4818/4016 6698/6197/5169 8035/7435/6197 2 20JEHxD740LNANNNNN 4 20JEHxD1K3LNANNNNN                                                               |                                                                       |
|       480 | 8035/7435/6197(1)           | 5207/4818/4016(1)  6698/6197/5169(1)  —  —  6                                                                                                        | 20JEHxD1K3LNANNNNN                                                    |
|       480 | 9625/8905/7423(2)           | 6237/5771/4810(2)  8022/7423/6191(2)  —  —  6                                                                                                        | 20JEHxD1K3LNANNNNN                                                    |

## Table 4 - 600V Single and Parallel NRS Module Ratings

|   Voltage | kW Ratings (LD/ND/HD) Input Amps AC (LD/ND/HD)   | (LD/ND/HD) Quantity of 1X Module Power Bays 1X Module Power Bay Base Cat. No. Quantity of 2X Module Power Bays   | Output Amps DC 2X Module Power Bay Base Cat. No.                                       |
|-----------|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
|       600 |                                                  | 518/488/403 534/501/414 640/602/497 1 20JEHxE545LNANNNNN — —                                                     |                                                                                        |
|       600 |                                                  |                                                                                                                  | 986/876/738 1014/901/759 1217/1082/911 — — 1 20JEHxE980LNANNNNN                        |
|       600 | 1452/1365/1127 1495/1403/1159                    | 1792/1686/1392 1 20JEHxE545LNANNNNN 1 20JEHxE980LNANNNNN                                                         |                                                                                        |
|       600 |                                                  |                                                                                                                  | 1918/1804/1490 1976/1854/1532 2368/2227/1839 — — 2 20JEHxE980LNANNNNN                  |
|       600 |                                                  | 2385/2243/1852 2456/2305/1904 2944/2769/2286 1 20JEHxE545LNANNNNN 2 20JEHxE980LNANNNNN                           |                                                                                        |
|       600 |                                                  |                                                                                                                  | 2851/2682/2214 2937/2756/2277 3520/3311/2734 — — 3 20JEHxE980LNANNNNN                  |
|       600 |                                                  |                                                                                                                  | 2851/2682/2214 2937/2756/2277 3520/3311/2734 2 20JEHxE545LNANNNNN 2 20JEHxE980LNANNNNN |
|       600 |                                                  |                                                                                                                  | 3784/3560/2939 3898/3657/3022 4672/4395/3628 — — 4 20JEHxE980LNANNNNN                  |
|       600 |                                                  | 4717/4437/3663 4859/4559/3767 5824/5478/4523 2 20JEHxE545LNANNNNN 4 20JEHxE980LNANNNNN                           |                                                                                        |
|       600 |                                                  |                                                                                                                  | 5651/5315/4388 5821/5461/4513 6976/6562/5417 — — 6 20JEHxE980LNANNNNN                  |

## Table 5 - 690V Single and Parallel NRS Module Ratings

|   Voltage | Output Amps DC (LD/ND/HD)   | kW Ratings (LD/ND/HD) Input Amps AC (LD/ND/HD) Quantity of 1X Module Power Bays 1X Module Power Bay Base Cat. No. Quantity of 2X Module Power Bays   | 2X Module Power Bay Base Cat. No.                                     |
|-----------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
|       690 |                             | 596/561/463 534/501/414 640/602/497 1 20JEHxF505LNANNNNN — —                                                                                         |                                                                       |
|       690 |                             |                                                                                                                                                      | 1134/1008/849 1014/901/759 1217/1082/911 — — 1 20JEHxF920LNANNNNN     |
|       690 |                             | 1669/1570/1296 1495/1403/1159 1792/1686/1392 1 20JEHxF505LNANNNNN 1 20JEHxF920LNANNNNN                                                               |                                                                       |
|       690 |                             |                                                                                                                                                      | 2206/2075/1713 1976/1854/1532 2368/2227/1839 — — 2 20JEHxF920LNANNNNN |
|       690 |                             | 2742/2580/2130 2456/2305/1904 2944/2769/2286 1 20JEHxF505LNANNNNN 2 20JEHxF920LNANNNNN                                                               |                                                                       |
|       690 |                             |                                                                                                                                                      | 3279/3084/2546 2937/2756/2277 3520/3311/2734 — — 3 20JEHxF920LNANNNNN |
|       690 |                             | 3279/3084/2546 2937/2756/2277 3520/3311/2734 2 20JEHxF505LNANNNNN 2 20JEHxF920LNANNNNN                                                               |                                                                       |
|       690 |                             |                                                                                                                                                      | 4352/4094/3380 3898/3657/3022 4672/4395/3628 — — 4 20JEHxF920LNANNNNN |
|       690 |                             | 5425/5103/4213 4859/4559/3767 5824/5478/4523 2 20JEHxF505LNANNNNN 4 20JEHxF920LNANNNNN                                                               |                                                                       |
|       690 |                             |                                                                                                                                                      | 6498/6112/5046 5821/5461/4513 6976/6562/5417 — — 6 20JEHxF920LNANNNNN |

## NRS System Configurations

This table provides the recommended NRS module system configurations and the PowerFlex 755TM common bus inverter that each configuration supports. For single and parallel module ratings, see NRS Module Selection and System Ratings on page 12. When modules are listed in parentheses in the following table and throughout this document, the parentheses indicate the following:

- Those modules are inside individual 400 mm (15.75 in.) wide power bays that are installed next to each other to one side of a wire entry bay.
- Those modules are all supplied with AC input from that wire entry bay.

See Bay Configurations on page 58 for example lineups.

Table 6 - Single and Parallel NRS Module System Configurations

| Bay Topology                   | NRS Module Combinations   | Voltage Class        | Quantity of Dual Density (2X) Modules   | Quantity of Single Density (1X) Modules Total Quantity of Modules Supports PowerFlex 755TM Common Bus Inverter                                   |
|--------------------------------|---------------------------|----------------------|---|-----------------------------------|
| Left-to-Right or Right-to-Left | 1X                        | 400/480/ 600/690V AC |   | 1 — 1 Frame 8                     |
| Left-to-Right or Right-to-Left |                           | 400/480/ 600/690V AC |   | 2X — 1 1 Up to frame 9            |
| Left-to-Right or Right-to-Left |                           | 400/480/ 600/690V AC |   | 400/480/ 600/690V AC 1X+2X 1 1 2 Up to frame 10                                   |
| Left-to-Right or Right-to-Left |                           | 400/480/ 600/690V AC |   | 2X+2X — 2 2 Up to frame 11        |
| Left-to-Right or Right-to-Left |                           | 400/480/ 600/690V AC |   | 2X+2X+1X 1 2 3 Up to frame 12     |
| Left-to-Right or Right-to-Left | 2X+2X+2X(1)               | 600/690V AC(2)       | 3 | —  3 Up to frame 13               |
| Inline or Back-to-back         | 2 (2X+1X)(1)              | 400/480/ 600/690V AC |   | 2 2 4 Up to frame 13              |
| Inline or Back-to-back         |                           | 400/480/ 600/690V AC |   | 400/480/ 600/690V AC 2 (2X+2X) — 4 4 Up to frame 14                                   |
| Inline or Back-to-back         |                           | 400/480/ 600/690V AC |   | 2 (2X+2X+1X) 2 4 6 Up to frame 15 |
| Inline or Back-to-back         | 2 (2X+2X+2X)              | 600/690V AC(2)       | 6 | —  6 Up to frame 15               |

## Product Advisories

Read the following precautions before you begin installation of the product.

## Qualified Personnel

<!-- image -->

ATTENTION: Only qualified personnel familiar with PowerFlex 750T products and associated machinery should plan or implement the installation, startup, and subsequent maintenance of the system. Failure to comply can result in personal injury and/or equipment damage.

## Personal Safety

<!-- image -->

ATTENTION: To avoid an electric shock hazard, verify that the voltage on the bus capacitors has discharged completely before servicing. Remove power and wait 5 minutes before you open a bay door. Measure the DC bus voltage at the -DC and +DC TESTPOINT sockets on the front of the module (see Figure 3 on page 17 for location).

<!-- image -->

<!-- image -->

ATTENTION: Hazard of personal injury or equipment damage exists when using bipolar input sources. Noise and drift in sensitive input circuits can cause unpredictable changes in motor speed and direction. Use speed command parameters on connected drives to help reduce input source sensitivity.

ATTENTION: The NRS start/stop/enable control circuitry includes solid-state components. If hazards due to accidental contact with moving machinery or unintentional flow of liquid, gas or solids exists, an additional hardwired stop circuit may be required to remove the AC line to the NRS. An auxiliary braking method may be required.

<!-- image -->

ATTENTION: A possible hazard of personal injury due to prolonged exposure to high sound levels. Follow applicable local, national, and international codes, standards, regulations, or industry guidelines for hearing protection when exposed to potentially damaging noise hazards.

## Product Safety

<!-- image -->

ATTENTION: An incorrectly applied or installed NRS system can result in component damage or a reduction in product life. Wiring or application errors such as incorrect or inadequate AC supply, a corrosive environment, or excessive surrounding air temperatures can result in malfunction of the system.

<!-- image -->

ATTENTION: This product contains Electrostatic Discharge (ESD) sensitive parts and assemblies. Static control precautions are required when you install these assemblies. Component damage can result if ESD control procedures are not followed. If you are not familiar with static control procedures, reference any applicable ESD protection handbook.

## Remove Power from the System

The following procedures must be followed before attempting to service any part of a PowerFlex 755TM Non-Regenerative Supply.

<!-- image -->

ATTENTION: Remove power before you remove or make cable connections. When you remove or insert a cable connector with power applied, an electric arc can occur. An electric arc can cause personal injury or property damage in theses ways:

- An electric arc can send an erroneous signal to system field devices, which can cause unintended machine motion
- An electric arc can cause an explosion in a hazardous environment Electric arcs cause excessive wear to contacts on both the module and its receiving connector. Worn contacts can create electrical resistance.
1. Turn off and lock out all input power, including any external power sources.

<!-- image -->

ATTENTION: To avoid an electric shock hazard when servicing the NRS, a means for lockout/tagout of the external, single-phase 120/240V power source and, if present, external 120V uninterruptible power supply source, must be provided.

2. If present, turn off and lock out any external, single-phase 120/240V power source.
3. Wait 15 minutes.
4. Open the power bay door.
5. Locate the AC testpoints. See Figure 3 on page 17 for the AC testpoints location.
6. Verify that there is no voltage at the AC input-power terminals.
7. Locate the DC bus testpoints. See Figure 3 on page 17 for the DC bus testpoints location.
8. For a single-density NRS module, verify that there is no voltage at the rear DC testpoints.
9. For a dual-density NRS module, verify that there is no voltage at the rear DC testpoints and the front DC testpoints.

## IMPORTANT

Do not use testpoints to verify that incoming power has been removed from the product. Access testpoints only after incoming power has been removed and the input power system is locked and tagged out.

Figure 3 - Testpoints Locations

<!-- image -->

## Main Control Circuit Board

Figure 4 - Main Control Circuit Board

<!-- image -->

SK-RM-MCB3-PF755-CD (400V/480V)

SK-RM-MCB3-PF755-EF (600V/690V)

| Item Description                                                                     |
|--------------------------------------------------------------------------------------|
| 1 J4 power board (front) connector                                                   |
| 2 J3 power board (rear) connector                                                    |
| 3 J13 connector for DC bus conditioner (optional)                                    |
| 4 J2 DC fuse connector                                                               |
| 5  J10 10-pin I/O connector for output to customer connection(1)                     |
| 6  J11 8-pin I/O connector for input from customer connection(1)                     |
| 7 S1 interface configuration rocker DIP switches (default position = all up)         |
| 8 S2 precharge configuration selector rotary switch (default position = 2)           |
| 9 DS1 7-segment condition display                                                    |
| 10 STS (Status) indicator                                                            |
| 11  Alarm and fault indicators: CAB FLT, CLR FLT, FAULT, ALARM, USER EN, PC COMPLETE |
| 12 Rear DC bus testpoints                                                            |
| 13 Front DC bus testpoints (dual-density NRS modules only)                           |

(1) See Customer Input and Output Connections to Main Control Circuit Board on page 19 .

## Customer Input and Output Connections to Main Control Circuit Board

Table 7 - Customer Input Terminal Block (J11) Connection Details

| Terminal Name                  | Description                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 P24V Clear Faults Input +    | Clears latched faults and clears the fault and alarm queue.                                                                                                                                                                                                                                                                                                                |
| 2 Clear Faults Input Common    | Clears latched faults and clears the fault and alarm queue.                                                                                                                                                                                                                                                                                                                |
| 3 120V AC Clear Faults Input + | Clears latched faults and clears the fault and alarm queue.                                                                                                                                                                                                                                                                                                                |
| 4 —                            | This terminal has no connection.                                                                                                                                                                                                                                                                                                                                           |
| 5 —                            | This terminal has no connection.                                                                                                                                                                                                                                                                                                                                           |
|                                | 6 P24V User Enable Input + Enables bus supply when signal applied. De-energizes bus supply when signal removed. This input is ignored when the main control circuit board S1 CONFIG switch 1 is in the down (closed) position. For the location of switch 1 and instructions on setting configuration switches, see Main Control Circuit Board Configuration on page 140 . |
| 7 User Enable Input Common     | 6 P24V User Enable Input + Enables bus supply when signal applied. De-energizes bus supply when signal removed. This input is ignored when the main control circuit board S1 CONFIG switch 1 is in the down (closed) position. For the location of switch 1 and instructions on setting configuration switches, see Main Control Circuit Board Configuration on page 140 . |
| 8 120V AC User Enable Input +  | 6 P24V User Enable Input + Enables bus supply when signal applied. De-energizes bus supply when signal removed. This input is ignored when the main control circuit board S1 CONFIG switch 1 is in the down (closed) position. For the location of switch 1 and instructions on setting configuration switches, see Main Control Circuit Board Configuration on page 140 . |

Table 8 - Customer Output Terminal Block (J10) Connection Details

| Terminal Name                        | Description                                                                                                                         |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| 1 Precharge Complete Normally Open   | There is continuity between this terminal and terminal 2 when the NRS module has completed the precharge function.                  |
| 2 Precharge Complete Common          | This is the common terminal between the normally open contact and normally closed contact on the internal Precharge Complete relay. |
| 3 Precharge Complete Normally Closed | There is continuity between this terminal and terminal 2 when the NRS module has NOT completed the precharge function.              |
| 4 Not Fault Normally Open            | There is continuity between this terminal and terminal 5 when a fault is NOT present in the NRS module.                             |
| 5 Not Fault Common                   | This is the common terminal between the normally open contact and normally closed contact on the internal Fault relay.              |
| 6 Not Fault Normally Closed          | There is continuity between this terminal and terminal 5 when a fault is present in the NRS module.                                 |
| 7 Not Alarm Normally Open            | There is continuity between this terminal and terminal 8 when an alarm is NOT present in the NRS module.                            |
| 8 Not Alarm Common                   | This is the common terminal between the normally open contact and normally closed contact on the internal Alarm relay.              |
| 9 Not Alarm Normally Closed          | There is continuity between this terminal and terminal 8 when an alarm is present in the NRS module.                                |
| 10 —                                 | This terminal has no connection.                                                                                                    |

## Input and Output Wiring Specifications

Customer input and output wiring are provided by the customer, and must meet the following specifications.

Table 9 - NRS Main Control Circuit Board Customer Input and Output Terminal Block Specifications

| Wire Size Range Terminal Torque   | Wire Size Range Terminal Torque   |                     |                                            | Wire Strip      |
|-----------------------------------|-----------------------------------|---------------------|--------------------------------------------|-----------------|
|                                   |                                   |                     | Length Maximum Minimum Maximum Recommended |                 |
| 3.3 mm 2 (12 AWG)                 | 0.05 mm 2 (30 AWG)                | 0.6 N•m (5.3 lb•in) | 0.5 N•m (4.4 lb•in)                        | 7 mm (0.28 in.) |

## Routing Input and Output Wiring

We recommend routing input and output wiring before installing the NRS module into the power bay and making input and output connections to the module. Route the input and output wires to either side of the power bay and then up to the control wireway, as other harnesses are routed. From the control wireway, the input and output cables can be routed into adjacent bays.

Figure 5 - Control Bus Wireway

<!-- image -->

## Making Input and Output Connections

## Make the connections as follows:

1. Make sure that P11 is connected to J11.
2. Connect customer input wiring into connector P11.
3. Make sure that P10 is connected to J10.
4. Connect customer output wiring into connector P10.

To support the wires that connect to the input/output connectors, you can use tie wraps, which can be secured to the tie wrap supports above the input/ output connectors. You can also terminate the system using the tie wrap supports. To do this, expose the shield on the cable assembly and use a metal wire tie wrap, secured to one of the tie wrap supports.

When you reinstall the main control circuit board protective touch guard, route input and output wiring through the slots in the top of the guard.

Figure 6 - Customer Input and Output Tie Wrap Supports

<!-- image -->

## Example Input and Output Wiring Diagrams

The following diagrams provide conceptual representations of the main control circuit board to show customer input and output wiring, and wiring connected to the J12 connector. For actual board layout, see Figure 4 on page 18 .

Figure 7 - Single NRS Module System, Main Control Circuit Board without Customer Input and Output

<!-- image -->

Figure 8 - Single NRS Module System, Main Control Circuit Board with Customer Input and Output

<!-- image -->

Figure 9 - Two NRS Module System, Main Control Circuit Boards with Customer Input and Output, Wired In Series Giving No Support for N-1 Operation

<!-- image -->

Figure 10 - Two NRS Module System, Main Control Circuit Boards with Customer Input and Output, Wired Individually to Support N-1 Operation

<!-- image -->

20-750-MNIH-JMP3

## Product Nameplate

The product nameplate includes the catalog number, which provides information about ratings and features of the product. See Catalog Number Explanation on page 27 .

Figure 11 - Nameplate

<!-- image -->

<!-- image -->

## Catalog Number Explanation

This section explains the catalog number of a base NRS module power bay. A complete NRS product can be a single power bay, or a system of paralleled power bays along with one or more wire entry bays and, if a back-to-back configuration is used, two DC voltage balance bays. Each power bay in a parallel system has its own catalog number. Bays other than the power bays are provided based on the quantity and type of power bays in your installation and the topology of your installation.

Catalog number positions 1…7 identify the product type and voltage rating.

<!-- image -->

|      | A                                         |
|------|-------------------------------------------|
| Code | Product                                   |
| 20J  | PowerFlex 755TM Bus Supplies              |
| B    | B                                         |
| Code | Corrosive Gas Protection and Cooling Type |
| E    | Corrosive Gas Protection (XT), Forced Air |
| C    | C                                         |
| Code | Input Type                                |
| H    | Non-Regenerative, 755TM Bus Supply        |
| D    | D                                         |
| Code | Enclosure                                 |
| 3    | IP21, UL Type 1; Floor Mount              |
| 4    | IP54, UL Type 12; Floor Mount             |
| E    | E                                         |
| Code | Voltage Rating                            |
|      | C 400V AC; 3 PH                           |
| D    | 480V AC; 3 PH                             |
|      | E 600V AC; 3 PH                           |
|      | F 690V AC; 3 PH                           |

1 … 20J

Catalog number positions 8…10 identify the product normal duty rating.

34 5 6 7 8

E

… 740 F1 … F4

10 11 12 13 14 15 16 17 18

H

3

D

L

N

| F1  PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 400V AC, 50 Hz Input 540V DC Output   | F1  PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 400V AC, 50 Hz Input 540V DC Output   | F1  PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 400V AC, 50 Hz Input 540V DC Output   | F1  PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 400V AC, 50 Hz Input 540V DC Output   |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Code                                                                                             | Amps                                                                                             |                                                                                                  | kW Module Density                                                                                |
| 770                                                                                              | 770                                                                                              | 400                                                                                              | 1X                                                                                               |
| 1K4                                                                                              | 1463                                                                                             | 800                                                                                              | 2X                                                                                               |

| F3  PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 600V AC, 60 Hz Input 810V DC Output   | F3  PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 600V AC, 60 Hz Input 810V DC Output   | F3  PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 600V AC, 60 Hz Input 810V DC Output   | F3  PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 600V AC, 60 Hz Input 810V DC Output   |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Code                                                                                             | Amps                                                                                             |                                                                                                  | kW Module Density                                                                                |
| 545                                                                                              | 545                                                                                              | 550                                                                                              | 1X                                                                                               |
| 980                                                                                              | 980                                                                                              | 1000                                                                                             | 2X                                                                                               |

N

N

N

N

N

-C1-P18 …

| F2 PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 480V AC, 60 Hz Input 648V DC Output   | F2 PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 480V AC, 60 Hz Input 648V DC Output   | F2 PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 480V AC, 60 Hz Input 648V DC Output   | F2 PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 480V AC, 60 Hz Input 648V DC Output   |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Code                                                                                            | Amps                                                                                            |                                                                                                 | kW Module Density                                                                               |
| 740                                                                                             | 740                                                                                             | 650                                                                                             | 1X                                                                                              |
| 1K3                                                                                             | 1365                                                                                            | 1100                                                                                            | 2X                                                                                              |

| F4 PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 690V AC, 50 Hz Input 932V DC Output   | F4 PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 690V AC, 50 Hz Input 932V DC Output   | F4 PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 690V AC, 50 Hz Input 932V DC Output   | F4 PowerFlex 755TM ND Non-Regenerative Bus Supply Ratings 690V AC, 50 Hz Input 932V DC Output   |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Code                                                                                            | Amps                                                                                            |                                                                                                 | kW Module Density                                                                               |
| 505                                                                                             | 505                                                                                             | 500                                                                                             | 1X                                                                                              |
| 920                                                                                             | 920                                                                                             | 900                                                                                             | 2X                                                                                              |

Catalog number positions 11…13 identify additional product configuration.

8 … 10 740

G 11 L

H I 12 13 N A

14 15 16 17 18

N

N

N

N

G

| Filtering and CM Cap Configuration   | Filtering and CM Cap Configuration       | Filtering and CM Cap Configuration   | Filtering and CM Cap Configuration   |
|--------------------------------------|------------------------------------------|--------------------------------------|--------------------------------------|
| Code                                 | EMC Filtering C3 Conducted, and Radiated | PE-A PE-B                            |                                      |
|                                      |                                          | L Yes Installed —                    |                                      |

H

| Dynamic Braking   | Dynamic Braking                            | Dynamic Braking   |
|-------------------|--------------------------------------------|-------------------|
|                   | Code Internal Resistor Internal Transistor |                   |
|                   | N No No                                    |                   |

I

Door-mounted HIM

Code Operator Interface and Control

A No HIM Provided

N

A

34 5 6 7

E

H

3

D

1 … 20J

-C1-P18 …

34 5 6 7

E

1 … 20J

H

3

D

34 5 6 7

E

H

3

D

1 … 20J

Catalog number positions 14…18 are not used.

8 … 10 740

11 12 13 14 15 16 17 18

L

N

A

N

N

N

N

N

-C1-P18 …

Control and power options are listed in the unnumbered field to right of position 18.

10 11 12 13 14 15 16 17 18

L

8 … 740

N

A

N

N

N

N

N

## 20J Control and Power Options Selection

-C1-P18 …

| Code   | Option                                     |
|--------|--------------------------------------------|
| C1     | Bus Supply and CBI Control Transformer     |
| C2     | Bus Supply Control Transformer Only        |
| P18    | NRS Wire Entry Bay (Default for X2 Rating) |
| P46    | System DC Bus (4700 Amp, Copper)           |
| P47    | System AC & DC Bus                         |
| P50    | Standard DC Bus Conditioner                |
| P72    | Integral NRS Module Bus Capacitor          |

## Commonly Used Tools

This list includes the tools that are needed for installation and test measurements.

## IMPORTANT

Make sure that tools and/or hardware components do not fall into open assemblies. Do not energize the NRS system unless all loose tools and/ or hardware components have been removed from all assemblies and bays.

| Tool Description                              | Details                                                                                                                                                                           |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                               | Allen socket wrench 3 mm, 4 mm, 5 mm (with long extension)                                                                                                                        |
| Allen socket wrench extension 254 mm (10 in.) |                                                                                                                                                                                   |
| Box wrench                                    | 7 mm, 8 mm, 10 mm, 13 mm, 15 mm, 17 mm, 19 mm, 22 mm                                                                                                                              |
| Ratcheting wrench 17 mm                       |                                                                                                                                                                                   |
| Crimp tools                                   | For cable terminals 1.5...240                                                                                                                                                     |
| Current clamp                                 | 1000 A (AC, rms), signal output                                                                                                                                                   |
|                                               | ESD-protected place of work Work surface, floor cover, seat, and ground connections                                                                                               |
|                                               | ESD-protective clothing Wrist wrap, shoes, overall clothing (coat)                                                                                                                |
| Flashlight                                    | —                                                                                                                                                                                 |
|                                               | Flat-nose screwdriver 3 mm (0.12 in.), 5 mm (0.19 in.), 6.4 mm (0.25 in.)                                                                                                         |
| Fuse puller                                   | —                                                                                                                                                                                 |
| Torx, star, or hexalobular screw driver/bit   | #15, #20, #25, #30, #40, #45                                                                                                                                                      |
|                                               | Hexagonal socket wrench 2.5 mm, 7 mm, 8 mm, 10 mm, 12 mm, 13 mm, 17 mm, 18 mm                                                                                                     |
| Insulation tester                             | 1000V DC                                                                                                                                                                          |
| Level                                         | —                                                                                                                                                                                 |
| Module service cart                           | The optional module service cart (20-750-MCART1) is recommended to handle and transport NRS modules. Important: The service cart is required to handle and transport NRS modules. |
| DCPC module lift                              | Used together with the module service cart to remove DC precharge modules.                                                                                                        |
| Module storage hardware                       | Module storage hardware (20-750-MINV-ATIP) helps to stabilize power and filter modules during temporary storage after removal.                                                    |
| Multi-meter                                   | Digital multi-meter, capable of AC and DC voltage, continuity, resistance, capacitance measurements, and forward diode bias tests. Fluke model 87 III or equivalent.              |
| Nose pliers                                   | —                                                                                                                                                                                 |
| Oscilloscope                                  | Portable, digitizing, dual channel scope, with isolation                                                                                                                          |
| Phillips screwdriver/bit #1, #2               |                                                                                                                                                                                   |
| Torque wrench                                 | 1...12 N•m (8.8…106 lb•in)                                                                                                                                                        |
| Torque wrench                                 | 6...50 N•m (53…443 lb•in)                                                                                                                                                         |
|                                               | Ratcheting Wrench 1...12 N•m (8.8…106 lb•in)                                                                                                                                      |
| Wire cutter                                   | —                                                                                                                                                                                 |

## Hardware Installation Diagrams

The assembly illustrations throughout this manual contain diagrams (as shown here) that identify the following: corresponding step number (if necessary), type of fastener, fastener size, tool type and size, and final assembly torque.

<!-- image -->

## Fastener Torque Sequences

<!-- image -->

ATTENTION: Components can be damaged if initial tightening procedure is not performed to specification.

The following illustrates initial and final torque sequences for components that are fastened with two, four, and six screws. Initial torque is 1/3 (33%) of final torque, except six-point mountings, which require 0.7 N·m (6 lb·in) initial torque. The numeric illustration labels are for your assistance. Components do not contain these labels.

Figure 12 - Two-point Mounting

1

1

2

Initial Sequence

Final Sequence

Figure 13 - Four-point Mounting

<!-- image -->

Figure 14 - Six-point Mounting

<!-- image -->

2

2

1

## Receiving

## Receiving, Handling, and Storage

PowerFlex® 755TM NRS floor mount products are bolted to wooden skids for shipment. For ease of handling, we recommend leaving the products bolted to the skids until you move them to the final installation area. Floor mount bays must remain in an upright position during handling.

<!-- image -->

ATTENTION: To avoid personal injury or structural damage, never attempt to lift or move the product by any means other than the handling methods outlined in this publication. PowerFlex 755TM NRS bays are top-heavy and front-heavy.

ATTENTION: Exercise caution when moving the product to make sure that the equipment is not scratched, dented, or damaged in any manner. Stabilize the product during handling to help prevent tipping and injury to personnel.

Standard packaged PowerFlex 755TM NRS floor mount products are shipped upright as a whole unit or in shipping sections as required. See Shipment Configurations on page 35. Each unit or shipping section is bolted to a shipping skid with removable shipping cleats and is covered with clear plastic wrap. Protection is for upright shipping and is not waterproof or watertight.

Heavy duty/export packaging is similar to standard packaging, but uses a plastic wrap suitable for occasional light water-spray. In addition, wood framing and sheeting surround the unit or shipping section. Heavy duty/ export packaging is not waterproof, watertight, or intended for long-term storage.

Upon delivery of the PowerFlex 755TM NRS product, refer to the packing slip for sizes and exact shipment weights. The packing slip also lists the items that are included in the shipment.

Inspect the shipment for damaged or lost items. If the packaging appears to be damaged, unpack the equipment for further inspection. Open the doors or remove covers and inspect the major components for signs of damage. PowerFlex 755TM NRS floor mount bays are equipped with a key-operated door latch. A double-bit door key, shown in Figure 15 on page 34 is taped to the bay door.

<!-- image -->

Figure 15 - Key-operated Door Latch

<!-- image -->

If there is evidence of damage or loss, follow this procedure:

- Note on the delivery receipt that the equipment being received is damaged.
- Contact the carrier that made the delivery and schedule an inspection.
- Inform your local Rockwell Automation representative that the equipment is damaged.
- Retain all product packaging for review by the carrier.

For further assistance, contact your Rockwell Automation representative.

## Shipment Configurations

Some PowerFlex 755TM NRS floor mount products are divided into sections for shipment. The approximate weight of each section and the approximate total weight of the product is listed in the following tables.

When lifting and handling these components, follow all applicable local, national, and international codes, standards, regulations, or industry guidelines for safe practices.

## Approximate Maximum Shipping Section Weights

Some products are divided for shipment. The weight of each section is listed in the following table.

Figure 16 - Shipping Sections for Single-Density and Dual-Density Products

<!-- image -->

Table 10 - Approximate Maximum Unit Weights [kg (lb)]

| Description                                                                                   |            | Weight Packaging Included   |
|-----------------------------------------------------------------------------------------------|------------|-----------------------------|
| Power bay, single-density                                                                     | 295 (650)  | 490 (1080)                  |
| Power bay, single-density with integral bus capacitors 304 (670)                              |            | 533 (1175)                  |
| Power bay, single-density with optional 3 kVA control transformer                             | 332 (732)  | 561 (1237)                  |
| Power bay, single-density with integral bus capacitors and optional 3 kVA control transformer | 341 (752)  | 604 (1332)                  |
| Power bay, dual-density with entry wire bay                                                   | 553 (1219) | 828 (1825)                  |
| Power bay, dual-density with integral bus capacitor                                           | 571 (1259) | 880 (1940)                  |
| Power bay, dual-density with optional 3 kVA control transformer                               | 590 (1301) | 899 (1982)                  |
| Power bay, dual-density with integral bus capacitor and optional 3 kVA control transformer    | 608 (1340) | 951 (2097)                  |
| 400 mm (15.75 in.) entry wire bay                                                             | 126 (278)  | 188 (414)                   |
| 800 mm (31.5 in.) entry wire bay                                                              | 242 (534)  | 309 (681)                   |
| DC voltage balance and exit wire bay                                                          | 291 (642)  | 353 (800)                   |

## Handling

## Approximate Maximum NRS Module Weights

If you order an individual NRS module, without the surrounding power bay, you can find the weight of the module in the following table. NRS modules ordered individually must be installed in a power bay before operation.

Table 11 - NRS Modules [kg (lb)]

| Description                                       | Cat. No.                                | Max Module Weight with Packaging   |           |
|---------------------------------------------------|-----------------------------------------|------------------------------------|-----------|
| Single-density NRS Modules with bus capacitors    | 20-750-MN1-C770D740 20-750-MN1-E545F505 | 134 (295)                          | 157 (345) |
| Single-density NRS Modules without bus capacitors | 20-750-MN2-C770D740 20-750-MN2-E545F505 | 125 (275)                          | 147 (325) |
| Dual-density NRS Modules with bus capacitors      | 20-750-MN1-C1K4D1K3 20-750-MN1-E980F920 | 204 (450)                          | 227 (500) |
| Dual-density NRS Modules without bus capacitors   | 20-750-MN2-C1K4D1K3 20-750-MN2-E980F920 | 186 (410)                          | 209 (460) |

Two methods of handling PowerFlex 755TM floor-mounted bay products within the receiving facility are acceptable.

- Transport by lift truck
- Overhead lifting (crane or hoist)

PowerFlex 755TM floor-mounted bay products must be handled in the upright vertical position. Failure to comply with this requirement can lead to damage to internal components and enclosures.

<!-- image -->

ATTENTION: Follow local codes and guidelines and your company safety procedures when you handle PowerFlex 755TM NRS products.

To avoid personal injury and structural damage to the PowerFlex 755TM NRS product, do not lift or move the equipment by any means other than what is described in this publication. PowerFlex 755TM NRS products are top- and front-heavy.

The following guidelines are provided to help avoid personal injury and equipment damage during handling and to help stabilize the product during transport to the installation site.

- Keep the product bolted to the shipping skid to minimize possibility of tipping.
- The factory-installed structural angles must remain secured to the bay during handling. Structural angles provide lift points and help minimize flexing of the bay during handling.
- Handle the PowerFlex 755TM NRS product carefully to avoid damage to the bays including the paint on the exterior of the bays.
- Keep the product in an upright position. PowerFlex 755TM NRS products are not to be tipped or laid flat during handling.

Before moving the product, verify that the route is clear of all obstructions and that other workers are a safe distance away.

## Transport by Lift Truck

PowerFlex 755TM NRS floor mount products are bolted to shipping skids that facilitate transport by a lift truck. If you are using a lift truck, refer to the following procedure.

<!-- image -->

ATTENTION: Verify that the lift truck can handle the weight and size of the PowerFlex 755TM NRS product safely. Shipment weights can be found on the packing slip that is included with each shipment. Approximate weights are listed on page 35 .

1. Lift only from underneath the shipping skid. Position the PowerFlex 755TM NRS product on the forks so that the load is balanced and does not tilt. The balance of each bay may be different. For example, some bays may be more top heavy or front heavy than others.
2. Keep the load against the load backrest of the lift truck. Use a belt to secure the PowerFlex 755TM NRS product to the lift truck. Tilt the load a few degrees backward toward the lift truck mast.

## IMPORTANT

The use of a belt is to help prevent the load from slipping forward during a sudden stop. Do not excessively tighten the belt. Belt tension must not bend, buckle, or otherwise distort the bay.

3. Start and stop the lift truck gradually and slowly to avoid jerky movements. When traveling with the load, drive slowly with the forks carried as low as possible, consistent with safe operation.

Figure 17 - Use a Lift Truck to Transport a PowerFlex 755TM Shipping Section

<!-- image -->

## Overhead Lifting (Crane or Hoist)

All lifting equipment and components (hooks, bolts, lifts, slings, chains, and so forth) must be properly sized and rated to lift and hold the weight of the equipment safely. Shipment weights can be found on the packing slip that is included with each shipment. Approximate weights are listed on page 35 . Structural angles with lifting holes are affixed to the top of the product bays.

<!-- image -->

ATTENTION: To guard against possible personal injury and/or equipment damage:

- Inspect all lifting hardware for proper attachment before lifting the equipment.
- Do not allow any part of the equipment or lifting device to contact electrically charged conductors or components.
- Do not subject the equipment to high rates of acceleration or deceleration while transporting to the installation site or when lifting.
- Do not allow personnel or their limbs directly underneath the equipment when it is being lifted and mounted.

## Attach Lifting Rigging to Structural Angles

1. Attach rigging to overhead crane, hoist, or similar lifting device.
2. Do not pass straps or cables through the lifting holes in the structural angle. Use slings with load-rated hooks or shackles.
3. Adjust the rigging lengths to compensate for any unequal weight distribution of the load and support the product in an upright position.
4. To reduce tension on the rigging and compression on the structural angle, verify that the angle between the straps or cables and horizontal plane is greater than 60°.

Figure 18 - Bay Lifting Points and Rigging

<!-- image -->

## Storage

PowerFlex 755TM NRS products are wrapped in plastic to help prevent dirt and dust from entering the bay during shipment. If you must store the equipment after you receive it, take the following precautions.

<!-- image -->

ATTENTION: PowerFlex 755TM NRS products are designed for indoor applications and do not have sufficient packaging for outdoor storage. Store PowerFlex 755TM NRS products in a heated building that offers adequate air circulation and protection from dirt and moisture.

- Do not remove the protective plastic wrap.
- Do not store the product outdoors.
- Do not store the product in an area where it is exposed to a corrosive atmosphere.
- Store the product in an area that is clean and dry.
- Store the product in a conditioned building with adequate air circulation.
- Maintain a storage temperature of -40…+70 °C (-40…+158 °F).
- Maintain a relative humidity of 5…95% noncondensing.
- Heating and moisture protection devices must be used if the rate of change in relative humidity and/or ambient temperature can lead to condensation on the stored equipment.
- If the product is in storage with no voltage applied for more than 2 years, reform the bus capacitors before use. For instructions on how to reform the bus capacitors, see the Preventive Maintenance Checklist of Industrial Control and Drive System Equipment Service Bulletin, publication DRIVES-TD001 .

## Notes:

## CE Conformity

## Prepare for Installation

This chapter provides requirements and recommendations for a successful and appropriate installation of PowerFlex® 755TM Non-Regenerative Supply (NRS) products.

Compliance with the Low Voltage Directive and Electromagnetic Compatibility Directive has been demonstrated using harmonized European Norm (EN) standards, which are referenced by the Official Journal of the European Union. PowerFlex 755TM NRS products comply with the EN standards that are listed in this section when installed according to these installation instructions.

EU Declarations of Conformity are available online at: rok.auto/certifications

## Low Voltage Directive (LVD)

- EN 61800-5-1 Adjustable speed electrical power drive systems – Part 5-1: Safety requirements – Electrical, thermal, and energy.

## EMC Directive

- EN 61800-3 Adjustable speed electrical power drive systems – Part 3: EMC requirements and specific test methods.

## General Considerations

- For EU compliance, NRS systems must satisfy installation requirements that are related to both EN 61800-5-1 and EN 61800-3 provided in this document.
- PowerFlex 755TM NRS products comply with the EMC requirements of EN 61800-3 when installed according to good EMC practices and the instructions that are provided in this document. However, many factors can influence the EMC compliance of an entire machine or installation, and compliance of the NRS itself does not ensure compliance of end-user applications.
- PowerFlex 755TM NRS products are not intended to be used on public low-voltage networks that supply domestic premises. Without additional mitigation, radio frequency interference is expected if used on such a network. The installer is responsible to take measures such as supplementary line filters and enclosures to prevent interference, and the installation requirements of this document.
- Requirements for supplementary mitigation that is related to specific high-frequency emission limits are provided in Table 12 on page 43 .

<!-- image -->

- PowerFlex 755TM NRS products generate harmonic current emissions on the AC supply system. When operated on a public low-voltage network, it is the responsibility of the installer or user to ensure that applicable requirements of the distribution network operator have been met. Consultation with the network operator and Rockwell Automation may be necessary.

<!-- image -->

ATTENTION: PowerFlex 755TM NRS products produce DC current in the protective earthing conductor which can reduce the ability of RCDs (residual current-operated protective devices) or RCMs (residual current-operated monitoring devices) of type A or AC to provide protection for other equipment in the installation. Where an RCD or RCM is used for protection in case of direct or indirect contact, only an RCD or RCM of Type B is allowed on the supply side of this product.

## Installation Requirements Related to EN 61800-5-1 and the Low Voltage Directive

- Voltage classes up to 690V PowerFlex 755TM products are compliant with the CE LVD when used on center-grounded, corner-grounded, highresistance grounded and ungrounded supply systems for altitudes up to and including 2000 m (6562 ft).
- When used at altitudes between 2000 m (6562 ft) and 4800 m (15,748 ft), PowerFlex 755TM NRS products of voltage classes up to 480V cannot be powered from a 'corner-grounded' supply system. This requirement is to maintain compliance with the CE LVD. Altitude derating guidelines are provided in the PowerFlex 755TM Non-Regenerative Supply Technical Data, publication 750-TD103 .
- PowerFlex 755TM NRS products that are provided in the IP54, UL Type 12 enclosure are compliant with the CE LVD when installed in pollution degree 1…4 environments where no gaseous contaminants are present. All other enclosure types must be installed in a pollution degree 1 or 2 environment to be compliant with the CE LVD. Characteristics of the different pollution degree ratings are provided in the PowerFlex 755TM Non-Regenerative Supply Technical Data, publication 750-TD103 .
- PowerFlex 755TM NRS products produce leakage current in the protective earthing conductor that exceeds 3.5 mA AC and/or 10 mA DC. The minimum size of the protective earthing (grounding) conductor that is used in the application must comply with local safety regulations for high-protective earthing conductor current equipment.

<!-- image -->

ATTENTION: PowerFlex 755TM NRS products produce DC current in the protective earthing conductor which can reduce the ability of RCDs (residual current-operated protective devices) or RCMs (residual current-operated monitoring devices) of type A or AC to provide protection for other equipment in the installation. Where an RCD or RCM is used for protection in case of direct or indirect contact, only an RCD or RCM of Type B is allowed on the supply side of this product.

## Installation Requirements Related to EN 61800-3 and the EMC Directive

- PowerFlex 755TM NRS products must be earthed (grounded) as described in Grounding Requirements on page 115 .
- All control (I/O) and signal wiring to the NRS must use cable with a braided shield providing 75% or greater coverage, or the cables must be housed in metal conduit, or equivalent shielding must be provided. When shielded cable is used, the cable shield is terminated with a lowimpedance connection to earth at only one end of the cable, preferably the end where the receiver is located. When the cable shield is terminated at the NRS end, it can be terminated by clamping the cable shield to the tie wrap supports that are shown in Figure 6 on page 21 .
- The NRS must be powered from an earthed supply system such as a TN or TT system and the PE-A and PE-B jumpers in the NRS modules must be correctly configured (see Power Jumper Configuration on page 137).
- Power cables must be separated from control and signal wiring wherever possible.

## Table 12 - PowerFlex 755TM Non-Regenerative Supply Input Product RF Emission Compliance

| NRS Bus Supply Module                | NRS Bus Supply Module Cat. No.   | Compliance with EN61800-3 Category C3 I > 100 A   |
|--------------------------------------|----------------------------------|---------------------------------------------------|
| 400V AC, 50 Hz Input, Single-Density | 20JExxC770                       | Yes                                               |
| 400V AC, 50 Hz Input, Dual-Density   | 20JExxC1K4                       | Yes                                               |
| 480V AC, 60 Hz Input, Single-Density | 20JExxD740                       | Yes                                               |
| 480V AC, 60 Hz Input, Dual-Density   | 20JExxD1K3                       | Yes                                               |
| 600V AC, 60 Hz Input, Single-Density | 20JExxE545                       | Yes                                               |
| 600V AC, 60 Hz Input, Dual-Density   | 20JExxE980                       | Yes                                               |
| 690V AC, 50 Hz Input, Single-Density | 20JExxF505                       | Yes                                               |
| 690V AC, 50 Hz Input, Dual-Density   | 20JExxF920                       | Yes                                               |

## Location Planning

When choosing the installation location for your product, make sure that the location meets the following requirements:

- Allows the product to be installed in a vertical orientation, square, and not deformed in any way.
- Provides a flat and level mounting surface (± 1 mm per meter [± 0.036 in. per 36 in.] of product length in all directions), allowing the product to make full contact with the mounting surface and stay stable. If necessary, use metal shims to level the bays before joining them.
- Provides a mounting surface that can support the weight of the product. See Approximate Maximum Shipping Section Weights on page 35 .
- Provides a mounting surface that can accommodate one of the various mounting options:
- Corner base/plinth system (See page 52)
- Structural steel system (See page 55)
- Anchor bolt system (See page 57)
- Concrete screw system (See page 57)
- Does not expose the product to environmental conditions that are incompatible with the Environmental Specifications on page 45 .
- Provides sufficient space for the product given its dimensions, required clearances, and access requirements. These topics are covered in the following sections:
- -Approximate Dimensions on page 59
- -Overhead Clearance on page 47
- -Airflow Clearances and Considerations on page 48
- -Service Cart Access Requirements on page 49

Also consider the following when choosing the installation location for your product:

- Ventilation and air conditioning concerns beyond meeting the ambient temperature requirements
- AC input power cable entry points
- The space required for the common bus inverters or DC input drives that the NRS powers through the DC common bus.
- Alignment with other equipment
- Future needs

Table 13 - Environmental Specifications

| Category                                     | Specifications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ambient temperature at 100% of rated current | IP21, UL Type 1: -20…+40 °C (-4…+104 °F) all ratings °° ypg IP54, UL Type 12: -20…+40 °C (-4…+104 °F) all ratings                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                              | Ambient temperature with derating See Derating Guidelines in the PowerFlex 755TM Non-Regenerative Supply Technical Data, publication 750-TD103 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                              | Storage temperature -40…+70 °C (-40…+158 °F)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Relative humidity                            | 5…95% noncondensing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Particulate pollution degree                 | IP21, UL Type 1: Pollution Degree 1 or 2 per UL61800-5-1. IP54, UL Type 12: Pollution Degree 1…4 per UL61800-5-1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Corrosive gas and vapor pollution degree     | The PowerFlex 755TM Non-Regenerative Supply comes with corrosive gas protection features standard. A corrosive gas harsh environment, in which this protection is needed, is defined as a copper or silver reactivity level greater than 1000 angstroms per 30 days exposure. No condensation allowed. To determine whether your environment is a corrosive gas harsh environment, see ISA-71.04-2013 for details on how to measure reactivity levels on copper and silver test coupons. To maintain effective corrosive gas protection you must also maintain the conditions listed in Corrosive Environment Installations on page 46 . |
| Shock (acceleration)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Operating shock                              | Cabinet packaged products – 10 g peak for 11 ms duration (±1.0 ms), three shocks in each direction in each axis. See Shock Events on page 46 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                              | Packaged for shipment shock Meets ASTM International standards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Vibration                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Operating vibration                          | Cabinet packaged products – 1.000 mm (0.040 in.) displacement, 1 g peak                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                              | Packaged for shipment vibration Meets ASTM International standards                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Environmental Specifications

The installation site must be compatible with the degree of protection that is provided by the enclosure. PowerFlex 755TM NRS products are only intended for indoor use. Make sure that filters and debris screens are installed. Filter and screen installation and replacement information is available in Chapter 8 on page 171 .

## Make sure that the product is not exposed to the following:

- Dust, metallic particles, or conductive pollutants that are incompatible with the pollution degree specification of the product. Acceptable pollution degree depends on the level of protection provided by the enclosure. Enclosure ingress protection is either IP21, UL Type 1, or IP54, UL Type 12. To determine the level of protection of your product, see the catalog number on the Product Nameplate (page 26) and code D on page 27. Acceptable pollution degrees for each level of protection are provided in the following table. Characteristics of the different pollution degree ratings are provided in the PowerFlex 750-Series Products with TotalFORCE Control Technical Data, publication 750-TD100. Even with the protection provided by the enclosure, we recommend to minimize exposure to these pollutants.
- Moisture and direct sunlight.
- Any conditions that are incompatible with the specifications in the following table.

## Corrosive Environment Installations

For PowerFlex 755TM NRS installations in environments where corrosive gases are prevalent, all unused wire harness connectors, circuit board connectors, terminal bocks, and ports must be sealed with protective covers.

## Seismic Qualified Installations

In a seismic qualified installation, NRS products must be rigidly mounted according to local standards and codes. In addition, the installation must comply with any guidance that is provided by a qualified Structural Professional Engineer.

Install the seismic hardware at the proper time in the installation process. Instructions for installation begin at Install Top Bracket Sets - Seismic Installations on page 86 .

## Shock Events

PowerFlex 755T products can withstand a finite number of shock events. The maximum allowable number of shock events increases as the peak amplitude decreases. Below 0.7 g peak, the maximum total shock events should not exceed 2000 cycles.

<!-- image -->

## Minimum Clearances and Access Requirements

Consider the following clearance and access requirements when choosing the installation location of your product.

## Overhead Clearance

The overhead clearance is required to allow access to the roof exhaust vent.

Figure 19 - Overhead Clearance

<!-- image -->

## Airflow Clearances and Considerations

Make sure that the air-intake and exhaust locations are not obstructed. Make sure that there is a clearance of at least 76 mm (3 in.) in front of each air-intake and exhaust location. Airflow through the bay is required to maintain proper cooling.

Regularly inspect and replace the filter media at air-intake and exhaust locations to maintain proper airflow and cooling. For filter maintenance schedules, see Recommended Maintenance Schedules on page 169 .

Figure 20 - Airflow Clearances

<!-- image -->

## Service Cart Access Requirements

Figure 21 - Service Cart Access Requirements

<!-- image -->

For the PowerFlex 750-Series service cart (20-750-MCART1) to be able to access the power bay, the following requirements must be met:

- Floor mounting hardware or platform height — The maximum height of the floor mounting hardware or platform is 254 mm (10 in.). This measurement is also an installation limit per NEC requirements for the disconnect switch.
- Bay setback — If the bay is mounted on a platform that is raised above the floor in front of the bays, the maximum distance from the bay to the platform edge is 203 mm (8 in.).
- Service cart side clearance — There must be clearance for the service cart in front of each power bay. The clearance must be at least 152 mm (6 in.) to the right of the bay and 152 mm (6 in.) to the left of the bay.
- Aisle clearance — The aisle in front of the bays must have a minimum width of 914 mm (36 in.) for the cart to be able to maneuver.

<!-- image -->

## Installation Site Requirements

<!-- image -->

Install the product on a flat and level surface such that all bays in the lineup are in a vertical orientation.

<!-- image -->

ATTENTION: Install bays on a level surface (± 1 mm per meter [± 0.036 in. per 36 in.] of total product length in all directions). If necessary, metal shims must be used to level the bays before joining them; any attempt to level after joining can twist or misalign the bays.

## Floor Mounting Preparation

Before performing the installation steps in Chapter 4 on page 69, prepare the installation site by measuring and drilling holes into the floor. Use this section and Approximate Dimensions on page 59 to determine where to drill holes. Perform other floor mounting tasks, such as attaching floor mounting hardware to the bays, and attaching floor mounting hardware to the floor, at the times stated in Chapter 4 on page 69 .

All mounting options use the bay mounting holes at the corners of the base of the bay, shown in Figure 24. All four mounting holes must be used to secure the bay properly. Remove the debris plug before installing mounting hardware in a mounting hole. For locations and dimensions between mounting holes, see Approximate Dimensions on page 59 .

Figure 24 - Typical Bay Mounting Holes

<!-- image -->

Table 14 - Recommended Mounting Fasteners

|     | Bay Fastener Size Usage   |                                                                                                                                                                                                                                                     | Notes                                            |
|-----|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| All | M12 (0.5 in.)             | • Secure the bay to the mounting system (corner base/plinth system or structural steel) by threading the fastener into the bay mounting hole. • Secure the mounting system (corner base/plinth system or structural steel) to the mounting surface. | Property Class 8.8 or better (Grade 5 or better) |
| All | M10 (0.375 in.)           | • Secure the bay to the mounting surface by passing the fastener through the bay mounting hole and anchoring it (anchor bolt) or threading it (concrete screw) into the mounting surface.                                                           | Property Class 8.8 or better (Grade 5 or better) |

## Rittal Base/Plinth System

The Rittal Base/Plinth System VX25 is available from Rittal Corporation in 100 mm (4.0 in.) and 200 mm (8.0 in.) heights. To find the total height of a bay and its mounting hardware, add the mounting hardware height to the bay height stated in PowerFlex 755TM Non-Regenerative Supply Approximate Dimensions on page 60. Consider the height of the mounting hardware for Overhead Clearance on page 47 .

This mounting system provides a base for each corner of a Rittal TS 8 enclosure. Use four corner bases to support each bay, including each individual bay that is part of a shipping section. Optional trim panels can be used along the perimeter of the lineup. Each corner base attaches to a corner of the enclosure using an M12 screw that is included with the system. Hardware for attaching the corner base to the mounting surface is not included. The recommended hardware for attaching a corner base to the mounting surface is an M12 anchor bolt, like the one shown in Figure 28 on page 57 .

Use one of the following types of mounting hardware when mounting the bays to the floor:

- Rittal Base/Plinth System on page 52
- Structural Steel System on page 55
- Anchor Bolt System on page 57
- Concrete Screw System on page 57

When choosing a mounting hardware system, consider that some mounting hardware limits which types of tools that can be used to transport an NRS module into or out of a power bay:

- To use the PowerFlex 755T power module service ramp, catalog number 20-750-MRAMP1, publication 750-IN108, all bays must be mounted directly to the floor, using the Anchor Bolt System or the Concrete Screw System. The service ramp cannot be used if the bays are mounted with mounting hardware between the bay and the floor, such as with the Rittal Base/Plinth System or Structural Steel System .
- The PowerFlex 750-Series module service cart, catalog number 20-750MCART1, publication 750-IN105, can be used with any of the types of mounting hardware that are listed in this section.

See the recommended fastener size for the type of mounting hardware that you choose.

Table 15 shows some configurations of the base system under a single bay. These drawings provide simplified block diagram views of the system. The arrow on the left side of each drawing indicates the front side of the bay. For images of the actual base system, see rittal.com .

Table 15 - Example Base Systems for a Single Bay

<!-- image -->

| Base Height Basic Form   | Example Cable Entry Options   | Example Cable Entry Options   | Example Cable Entry Options   |
|--------------------------|-------------------------------|-------------------------------|-------------------------------|
| 100 mm (4 in.)           |                               |                               |                               |
| 200 mm (8 in.)           |                               |                               |                               |

Figure 25 - Examples of Adjacent Base Systems Under a Bay Lineup

<!-- image -->

Follow the installation instructions that come with the base system. For a list of base system components, see Table 16 on page 54 .

Table 16 - Rittal Base System Components

| Components                                                                     | Height of Bottom of Bay Off of Mounting Surface [] [mm (in.)]             | Length of Side of Bay Component is Used With (1) [mm (in.)]   |
|--------------------------------------------------------------------------------|-------------|---------------------------------------------------------------|
| Corner base (required for base/plinth system)                                  | 100 (4.0) — |                                                               |
| Corner base (required for base/plinth system)                                  | 200 (8.0)   | —                                                             |
| Trim panels for between adjacent corner bases where bays are joined (optional) | 100 (4.0)   | —                                                             |
| Trim panels for between adjacent corner bases where bays are joined (optional) | 200 (8.0)   | —                                                             |
| Trim panels to cover the corner bases (optional)                               | 100 (4.0)   | —                                                             |
| Trim panels to cover the corner bases (optional)                               | 200 (8.0)   | —                                                             |
| Trim panels for front, back, and sides of bay                                  | 100 (4.0)   | 300 (11.8)                                                    |
| Trim panels for front, back, and sides of bay                                  | 100 (4.0)   | 400 (15.7)                                                    |
| Trim panels for front, back, and sides of bay                                  | 100 (4.0)   | 600 (23.6) (2)                                                |
| Trim panels for front, back, and sides of bay                                  | 100 (4.0)   | 800 (31.5)                                                    |
| Trim panels for front, back, and sides of bay                                  | 100 (4.0)   | 1000 (39.4)                                                   |
| (optional)                                                                     | 200 (8.0)   | 300 (11.8)                                                    |
| (optional)                                                                     | 200 (8.0)   | 400 (15.7)                                                    |
| (optional)                                                                     | 200 (8.0)   | 600 (23.6) (2)                                                |
| (optional)                                                                     | 200 (8.0)   | 800 (31.5)                                                    |
| (optional)                                                                     | 200 (8.0)   | 1000 (39.4)                                                   |

## Structural Steel System

Bays can be mounted to structural steel that is anchored to concrete and meets the following specifications and minimum dimensions.

Material: ASTM A-36 / ASME SA36, or equivalent

Figure 26 - Structural Steel Beam Cross-sections

<!-- image -->

Table 17 - Steel Beam Minimum Dimensions

| Style  Depth (d) [mm (in.)]                                   | Width (b) [mm (in.)]   | Thickness (tw) [mm (in.)]   | Flange (tf) []  g [mm (in.)]                                                                     | Length [ (1)  (l) g [mm (in.)]   |
|---------------------------------------------------------------|------------------------|-----------------------------|---------------------------------------------------------------------|---|
|                                                               |                        |                             | Wide Flange Beam 100 (4.0) 100 (4.0) 7.6 (0.3) 10.2 (0.4) 100 (4.0) |   |
| Channel Beam 100 (4.0) 43 (1.7) 7.6 (0.3) 7.6 (0.3) 100 (4.0) |                        |                             |                                                                     |   |

To find the total height of a bay and its mounting hardware, add the mounting hardware height (d) to the bay height stated in PowerFlex 755TM NonRegenerative Supply Approximate Dimensions on page 60. Consider the height of the mounting hardware for Overhead Clearance on page 47. To allow for service cart access, the mounting hardware must be no more than 254 mm (10 in.) tall.

## Structural Steel Mounting Configurations

Bays can be mounted directly to structural steel beams by using M12-1.75 screws threaded into the threaded corner holes. The bays must be secured to the anchor bolts in all four corners by using M12 nuts and lock washers. Secure the steel beam to the concrete floor by using M12 (0.5 in.) anchor bolts.

We recommend that you orient the beams so that the "I" shape of the I beam or the "C" shape of the C beam is visible when viewing the beam from the side of the bay, not the front of the bay. This orientation allows for the removal of the bay from the lineup using a forklift.

Figure 27 - Structural Steel Mounting Cross-section

<!-- image -->

<!-- image -->

<!-- image -->

## Anchor Bolt System

Bays can be mounted directly to a level concrete surface by using M10 (0.375 in.) anchor bolts. Use M10 nuts and lock washers to secure the bays to the anchor bolts in all four corners.

Figure 28 - Anchor Bolt System Cross-section

<!-- image -->

## Concrete Screw System

Bays can be mounted directly to a level concrete surface by using M10 (0.375 in.) concrete screws. Secure each bay with concrete screws in all four corners.

Figure 29 - Concrete Screw System Cross-section

<!-- image -->

## Bay Configurations

NRS products can be assembled in various configurations. These illustrations provide an overview of the bay configurations that are depicted in Approximate Dimensions. Inline NRS products that are composed of an entry wire bay and up to three power bays can be assembled in either a left-to-right or a right-to-left orientation.

Figure 30 - Inline Configuration—Right-To-Left and Left-To-Right Orientations, Top View

<!-- image -->

Figure 31 - Inline Configuration, Top View

<!-- image -->

Figure 32 - Back-to-Back Configuration, Top View

<!-- image -->

## Approximate Dimensions

The following table lists the dimensional drawings that are provided in this section. All drawings depict configurations in the left-to-right orientation.

Table 18 - Dimension Drawings

| Description                                                                                                                | Page   |
|----------------------------------------------------------------------------------------------------------------------------|--------|
| 1X without Optional Wire Bay: Top, Front, and Bottom Views [mm (in.)]                                                      | 60     |
| 2X with Required Wire Bay, 1X with Optional Wire Bay: Top, Front, and Bottom Views [mm (in.)] 61                           |        |
| 2X+1X: Top, Front, and Bottom Views [mm (in.)]                                                                             | 62     |
| 2X+2X: Top, Front, and Bottom Views [mm (in.)]                                                                             | 63     |
| 2X+2X+1X or 2X+2X+2X: Top, Front, and Bottom Views [mm (in.)]                                                              | 64     |
| 1X+2X Left + 2X+1X Right or 2X+2X Left + 2X+2X Right: Top, Front, and Bottom Views [mm (in.)] 65                           |        |
| (1X+2X+2X Left + 2X+2X+1X Right) or (2X+2X+2X Left + 2X+2X+2X Right): Top, Front, and Bottom Views [mm (in.)]              | 67     |
| (1X+2X Left + 2X+1X Right) or (2X+2X Left + 2X+2X Right) Back-to-Back: Top, Front, and Bottom Views [mm (in.)]             | 66     |
| (1X+2X+2X Left + 2X+2X+1X Right) or (2X+2X+2X Left + 2X+2X+2X Right) Back-to-Back: Top, Front, and Bottom Views [mm (in.)] | 68     |

## PowerFlex 755TM Non-Regenerative Supply Approximate Dimensions

<!-- image -->

<!-- image -->

Figure 33 - 1X without Optional Wire Bay: Top, Front, and Bottom Views [mm (in.)]

<!-- image -->

Input Power Cables - Bottom Entry Used for 1X Only Systems (Plate is marked with recommended gland or conduit hole pattern.)

Figure 34 - 2X with Required Wire Bay, 1X with Optional Wire Bay: Top, Front, and Bottom Views [mm (in.)]

183

(7.2)

<!-- image -->

This configuration can be assembled in either a left-to-right or a right-to-left orientation. The left-to-right orientation is shown.

Figure 35 - 2X+1X: Top, Front, and Bottom Views [mm (in.)]

<!-- image -->

This configuration can be assembled in either a left-to-right or a right-to-left orientation. The left-to-right orientation is shown.

Figure 36 - 2X+2X: Top, Front, and Bottom Views [mm (in.)]

<!-- image -->

This configuration can be assembled in either a left-to-right or a right-to-left orientation. The left-to-right orientation is shown.

Figure 37 - 2X+2X+1X or 2X+2X+2X: Top, Front, and Bottom Views [mm (in.)]

<!-- image -->

This configuration can be assembled in either a left-to-right or a right-to-left orientation. The left-to-right orientation is shown.

Figure 38 - 1X+2X Left + 2X+1X Right or 2X+2X Left + 2X+2X Right: Top, Front, and Bottom Views [mm (in.)]

<!-- image -->

Figure 39 - (1X+2X Left + 2X+1X Right) or (2X+2X Left + 2X+2X Right) Back-to-Back: Top, Front, and Bottom Views [mm (in.)]

<!-- image -->

Figure 40 - (1X+2X+2X Left + 2X+2X+1X Right) or (2X+2X+2X Left + 2X+2X+2X Right): Top, Front, and Bottom Views [mm (in.)]

<!-- image -->

Figure 41 - (1X+2X+2X Left + 2X+2X+1X Right) or (2X+2X+2X Left + 2X+2X+2X Right) Back-to-Back: Top, Front, and Bottom Views [mm (in.)]

<!-- image -->

Installation of Products with Corrosive Gas Protection (XT)

<!-- image -->

## Mechanical and Electrical Installation

The PowerFlex® 755TM Non-Regenerative Supply installation process is divided into the following principal tasks:

- Mechanically install the bays
- Make the electrical interconnections between bays if necessary
- Make AC input power connections and DC output power connections (Chapter 5 on page 115)

This section assumes that the installation site has been prepared and that all requirements for proper installation of the equipment as outlined in Chapter 3 on page 41 are met.

PowerFlex 755TM NRS products are manufactured with XT, and use protective covers to help seal connectors against environments with corrosive gases. To help provide improved performance in these environments, only remove protective covers to make a required connection. Do not remove protective covers from unused connectors.

## Remove Shipping Hardware

Use the following procedure to remove the shipping hardware from all bays that are shipped as part of your product.

1. Follow the guidelines in Chapter 2: Receiving, Handling, and Storage to transport the bays to the installation site.
2. Attach lifting hardware to the bays. See Overhead Lifting (Crane or Hoist) on page 38 for additional details.

Figure 42 - Typical Lifting Points

<!-- image -->

3. Remove the 3/8 inch lag bolts that fasten the bay cleats to the shipping skid.
4. Use the crane or hoist to lift the bay off the shipping skid and place the bay on supports, such as wood beams. These supports must provide enough space to remove the bolts that secure the shipping cleats to the bay.
5. Use the crane or hoist to lift the bay off the supports and place it on the floor.

Figure 43 - Release Bay From Shipping Skid

<!-- image -->

Figure 44 - Remove Shipping Cleats

<!-- image -->

## Protective Touch Guards

Follow these steps to remove and replace protective touch guards in a wire bay, power bay, or DC voltage balance bay.

1. Review the Product Advisories on page 15 .
2. Open the bay door.

## Figure 45 - Key-operated Door Latch

<!-- image -->

<!-- image -->

ATTENTION: Hazard of personal injury or equipment damage exists when protective touch guards are removed. Guards help to protect against accidental contact with exposed electrical connections and components. Guards can also provide electrical insulation between components. Remove guards only when access is required. Replace guards promptly. Never operate PowerFlex 755TM NRS products without all guards in place.

3. Loosen the M5.5 screws that secure the protective touch guards. When you reinstall the guards, tighten the screws to the torque listed.

<!-- image -->

You do not need to remove the M5.5 screws. Loosen and leave in place.

Figure 46 - Typical Touch Guard Fasteners

<!-- image -->

Figure 47 - Wire Bay and DC Voltage Balance Bay Touch Guards

<!-- image -->

Touch Guards Removed and Installed for:

- 400 mm (15.7 in.) Wire Bay
- DC Voltage Balance Bay
- (Example Shows Wire Bay)

Figure 48 - Power Bay Touch Guards

<!-- image -->

<!-- image -->

Touch Guards Installed for

800 mm (31.5 in.) Wire Bay

## Remove NRS Modules

NRS modules must be removed to access to the power bay interior. This access is required to complete the following installation tasks:

- Join bays
- Anchor bays to the mounting surface
- Make electrical interconnections

## Figure 49 - NRS Module Labeling

<!-- image -->

## NRS Module Handling

<!-- image -->

ATTENTION: NRS Modules have a high center of gravity and a tip-over hazard exists. To guard against death, serious personal injury, or equipment damage, do not subject the module to high rates of acceleration or deceleration while transporting. Do not push or pull above the points that are indicated on the module.

The PowerFlex 750-Series Service Cart (20-750-MCART1) is recommended to handle modules during installation. See Recommended Equipment and Accessories on page 75 .

## Temporary NRS Module Storage

During installation, we recommend that you designate a secure temporary storage area for the NRS modules that you remove from the power bays. An NRS module presents a tip-over hazard when removed from the power bay. Make sure that modules are stored in such a way that they do not pose a hazard.

Do not store components in active isles or work areas. We recommend that you designate an area for the temporary storage of the components that are removed during the installation process. Loose components can be hazardous and easily damaged.

## Recommended Equipment and Accessories

Equipment is available that is designed to help you safely handle NRS modules. The following equipment is recommended:

- PowerFlex 750-Series module service cart, catalog number 20-750-MCART1, publication 750-IN105
- PowerFlex 755T power module service ramp, catalog number 20-750-MRAMP1, publication 750-IN108

## IMPORTANT

The service ramp can only be used to transport an NRS module in or out of a power bay if all bays are mounted directly to the floor, using the Anchor Bolt System or the Concrete Screw System on page 57. Before you use the service ramp, review the instructions.

For a list of Commonly Used Tools, see page 30 .

## Remove an NRS Module from a Power Bay

1. Open the power bay.
2. Remove the touch guard that covers the DC link fuse assembly.
3. Remove the M10 nuts that secure the NRS module flexible bus bars to the DC link/fuse assembly.
- Single-density NRS modules have two flexible bus bars.
- Dual-density NRS modules have four flexible bus bars.

<!-- image -->

<!-- image -->

4. Remove the touch guard that covers the main control circuit board. Lift the cover up and then pull it out from the module.

<!-- image -->

5. Make sure that the following main control circuit board connectors have all wire harness connectors disconnected (J2, J12, J13) and all wires disconnected (J10, J11).

<!-- image -->

| Connector Description                                                                        |
|----------------------------------------------------------------------------------------------|
| J2 DC fuse condition signal from connector P2 on the DC link fuses.                          |
| J10 Customer output connections for NRS module precharge complete, fault, and alarm signals. |
| J11 Customer input connections for NRS module clear faults and precharge enable signals.     |
| J12 240V AC and thermal switch control signals from bay harness connector P12.               |
| J13 DC bus conditioner signals from connector P13 on the DC bus conditioner, if present.     |

6. Remove the two M10 x 20 mm Torx screws that secure the upper NRS module chassis to the top PE ground bracket.
7. Prepare the PowerFlex 750-Series service cart or service ramp. See step 9 .
8. Once the service cart or ramp is ready, remove the two M10 x 20 mm screws that secure the module chassis to the bay floor PE ground bracket.
9. Remove the NRS module from the bay. The following methods are available:
- To remove the module by using a PowerFlex 750-Series Service Cart, follow the detailed instructions in the PowerFlex 750-Series Service Cart and DCPC Module Lift Installation Instructions, publication 750-IN105 .
- To remove the module by using a PowerFlex 755TM service ramp, follow the procedures that are detailed in the PowerFlex 755T Module Service Ramp Instructions, publication 750-IN108 .

<!-- image -->

<!-- image -->

ATTENTION: NRS modules have a high center of gravity and a tip-over hazard exists. To guard against death, serious personal injury, or equipment damage, do not subject the module to high rates of acceleration or deceleration while transporting. Do not push or pull above the points that are indicated on the module.

## Attach Floor Mounting Hardware to the Bays

## Position the First NRS Bay

If you are using the Rittal Base/Plinth System on page 52 or Structural Steel System on page 55 for floor mounting, attach the floor mounting hardware to the bottom of the bays, but not the floor. See the section for your floor mounting system and any installation instructions that came with your floor mounting hardware.

If your product includes multiple bays, see Approximate Dimensions on page 59 for drawings showing how the bays are arranged.

For configurations that are not back-to-back, we recommend to position a wire bay as the first bay, and then proceed to add more bays to either side of the first bay using the procedure Add a Bay to the Lineup on page 81 .

For a back-to-back configuration, two wire bays are shipped connected backto-back, and two DC voltage balance bays are shipped connected back-to-back. The power bays are shipped individually. For a back-to-back configuration, we recommend that you install bays in the following order.

Figure 50 - Recommended Order of Bay Installation for a Back-to-Back Configuration, Top View

<!-- image -->

1. Position the first bay (or section of bays) in the lineup using the method in Overhead Lifting (Crane or Hoist) on page 38, with the exception that the skids are no longer attached.

<!-- image -->

ATTENTION: When positioning the bays into their final installation location, the skids are not attached. Without the skid attached, a bay or section of bays may be less stable than they were when you moved them with the skids attached. Make sure bays stay in an upright orientation while being moved into position.

2. If your product includes any other bays, proceed to add them to the lineup as described in Add a Bay to the Lineup on page 81 .

## Add a Bay to the Lineup

This section describes how to join a bay to one that is already in its installed position.

1. Make sure that both bays you are joining have the side sheet removed from the side of the bay that will be joined to the other bay. To remove a side sheet, use the following steps:
- a. Remove the six screws and six washers that secure the side sheet to the bay.
- b. Remove the side sheet. You may want to save the side sheet and the hardware for attaching it, particularly if you may rearrange your NRS system in the future. For example, removing a 1X power bay from a lineup and using it as a standalone power bay would require you to reinstall the side sheets on that bay. If you ever choose to reinstall a side sheet, you should not need a new gasket to install the side sheet because it includes a factory-installed gasket. If you reinstall a side sheet, tighten the bolts to the torque listed in Figure 51 .

IMPORTANT Use care not to damage the factory-installed gasket on the side sheet.

Figure 51 - Removing or Installing a Bay Side Sheet

<!-- image -->

2. Locate the required hardware for joining two bays.

## Figure 52 - Hardware Required to Join Two Bays

Top Bracket Hardware for Standard Installation

Standard Bracket Set for Front of Bays

Top Bracket Hardware for Seismic Installation

<!-- image -->

Standard Bracket Set for Back of Bays

<!-- image -->

Seismic Bracket Set for Front of Bays

Standard Bracket Set for Back of Bays

<!-- image -->

<!-- image -->

Gasket Material

<!-- image -->

<!-- image -->

3. Apply gasket material in one continuous strip around the mating surface of the placed bay. Seam the gasket at the approximate middle of the bottom of the bay.

<!-- image -->

4. Align the new bay to the lineup and slowly bring it into contact with the lineup. If necessary, use metal shims to level the bays before joining them. Make sure that the two sides fit together tightly along the gasket.

IMPORTANT

Make sure that no position and leveling adjustments are required before proceeding to step 5 .

<!-- image -->

5. Remove the structural angles from the bays.

IMPORTANT Once the structural angles are off, you cannot make any more position or leveling adjustments to the bays.

<!-- image -->

## Install Top Bracket Sets – Standard Installation

Use two standard top bracket sets to join two bays together.

1. Use the M12 bolts and washers to install the top bracket sets to the bay roof panels.
2. Verify that the bays are aligned, level, and pushed together tightly.

IMPORTANT The paint-piercing rubber washers are required for both grounding purposes and to meet the enclosure rating.

2. Use the M12 bolts and nuts that join the two angle brackets and tighten.

<!-- image -->

## Install Top Bracket Sets - Seismic Installations

1. Use the M12 bolts and washers to install a seismic top bracket set in the bay joining front position shown in the following figure.
2. Use the M12 bolts and washers to install a standard top bracket set to the back position of the bays.

Make sure that the bays are aligned, level, and pushed together tightly.

IMPORTANT The paint-piercing rubber washers are required for both grounding purposes and to meet the enclosure rating.

3. Install the bolts and washers that join each bracket set and tighten.
4. At each end bay non-joining front position, install a seismic door stop top bracket. In the following figure, the power bay is used as an example of an end bay, but there would actually be one or more bays to the right of it.
5. If you want to disable opening of the bay doors, secure the door stops by inserting the M8 self-locking pin and wing screw.

<!-- image -->

<!-- image -->

## Install Frame Clamps - All Installations

1. Place the interior frame clamps. Nine frame clamps are used to join two bays. The approximate positions are shown in this illustration. See Figure 53 on page 88 for the exact positions.
2. Tighten the interior frame clamps.

<!-- image -->

IMPORTANT

Do not attempt to lift bays that are joined with this hardware.

Figure 53 - Interior Frame Clamp Spacing

<!-- image -->

## Add All Bays to the Lineup

Repeat the procedures on page 82 through page 88 as many times as required to add all bays in your installation. This procedure covers all bay joining that may be required. It covers joining of NRS bays, including NRS wire bays, NRS power bays, and NRS DC voltage balance bays, and drive bays (a bay that contains a PowerFlex 755TM Common Bus Inverter, or a DC input drive).

Drive bays must be joined to the lineup on the output side of the NRS output bay or bays. An output bay in an NRS system can be either a power bay, for systems that are not back-to-back, or a DC voltage balance bay, for systems that are back-to-back.

Drive bays must use Rittal enclosures of the same height and depth as the NRS bays. These dimensions allow a drive bay to be joined to the NRS output bay using the same floor mounting and bay joining methods that are described for the NRS bays. The width of drive bays may be 400 mm (16 in.), 600 mm (24 in.), or 800 mm (31 in.).

When all bays in your installation are joined, proceed to Secure and Seal Roof Panels on page 90 .

<!-- image -->

## Secure and Seal Roof Panels

## Affix the Bays to the Floor

## Make NRS Bay-to-Bay Electrical Connections

To secure and seal the roof panels, use the M12 screws with integral paintpiercing rubber washers.

IMPORTANT The paint-piercing rubber washers are required for both grounding purposes and to meet the enclosure rating.

<!-- image -->

When all bays are joined and the roof panels are sealed, affix the bays to the mounting surface using the method you chose in Floor Mounting Preparation on page 51 .

After the bays are mechanically joined and properly anchored to the mounting surface, electrically connect the bays together. The following electrical interconnections are required:

- Bus Bar Splice Connections on page 91, including the following:
- DC bus
- Control bus
- AC bus
- PE ground
- Wire Bay Fan Power Connections on page 94 (if a wire bay is present)
- System Communication Interconnection Harnesses on page 96

For bay-to-bay connections between the NRS output bay and the drive bays, see NRS Output Bay Connections to Drive Bays on page 119 .

## Bus Bar Splice Connections

1. Determine what splices you must make:
- Figure 55 shows what splices to make between different types of bays in an inline configuration.
- Figure 56 on page 92 shows what splices to make between different types of bays in a back-to-back configuration.
2. Locate the hardware required for the bus bar splice connections.

## Figure 54 - Bus Bar Splice Kits

<!-- image -->

DC Bus Bar Control Bus Bar AC Bus Bar

<!-- image -->

<!-- image -->

<!-- image -->

PE Ground Bus Bar

3. Make the splice connections using the final torque specifications for each type of splice provided in Figure 57 on page 93 .

## Figure 55 - Bus Bar Splices for Inline Configurations

<!-- image -->

| A                                                                                                                                                                                                                                             | B                                                                                                                        | C                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Wire Bay to Wire Bay                                                                                                                                                                                                                          | Wire Bay to Power Bay                                                                                                    | Power Bay to Power Bay                                                                                                    |
| Inline Configuration • Splice the DC buses • Do not splice the control bus • Do not splice the AC buses • Do not splice the PE ground bus bar Important: An electrical connection between the PE ground bars in two wire bays is not allowed. | Inline Configuration • Splice the DC buses • Splice the control bus • Splice the AC buses • Splice the PE ground bus bar | Inline Configurations • Splice the DC buses • Splice the control bus • Splice the AC buses • Splice the PE ground bus bar |

| A                                                                                                                            | B                                                                                                                            | C                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Wire Bay to Power Bay                                                                                                        |                                                                                                                              | Power Bay to Power Bay Power Bay to DC Voltage Balance Bay                                               |
| Back-to-Back Configuration • Splice the DC buses • Splice the control bus • Splice the AC bus • Splice the PE ground bus bar | Back-to-Back Configuration • Splice the DC buses • Splice the control bus • Splice the AC bus • Splice the PE ground bus bar | Back-to-Back Configuration • Splice the DC buses • Splice the control bus • Splice the PE ground bus bar |

Figure 56 - Bus Bar Splices for Each Lineup in a Back-to-Back Configuration

<!-- image -->

Figure 57 - Splicing Hardware and Torques

<!-- image -->

## Wire Bay Fan Power Connections

Use the following steps to make wire bay fan power connections.

1. Locate the wire bay fan harness:
- If the wire bay was ordered as part of a complete NRS system, only one wire bay fan harness is provided with the wire bay.
- If the wire bay was ordered separately, not as part of a complete system, it comes with two wire bay fan harnesses. For an NRS system, use the fan harness with part number PN-625780. To identify the correct harness, see Figure 58 .

Figure 58 - NRS Wire Bay Fan Harness

<!-- image -->

Route and connect the wire bay fan power harness as shown in Figure 59 and Figure 60 on page 95 .

Figure 59 - NRS Wire Bay Fan Schematic

<!-- image -->

Figure 60 - NRS Wire Bay Fan Power Harness Routing and Connections

<!-- image -->

## System Communication Interconnection Harnesses

IP00 system communication interconnection harness kits must be installed as needed in wire entry, power, and DC voltage balance bays of IP21 and IP54 NRS systems to provide module-to-module and bay-to-bay communication for precharge and fault coordination. This section describes how to install the interconnect harnesses.

1. To determine which types of interconnect harnesses your system needs, see the System Communication Interconnect Harness Installation Examples on page 103 and Table 19. If you want your system to use N-1 operation, also see NRS System N-1 Operation on page 105 for information on the interconnect harness configuration for N-1 operation.
2. Locate the interconnect harness kits required for your system.

Table 19 - Non-Regenerative Supply System Communication Interconnection Harness Kits

|                  |                                                                                                                                                 | From To                                                                 | From To                 | From To                                                                   |                                |                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------------------|--------------------------------|-------------------|
|                  | Cat. No. Description                                                                                                                            | Bay  Bay Connector                                                      | Harness Connector       | Bay or Module                                                             | Bay or Module Connector        | Harness Connector |
| 20-750-MNIH-JMP1 | End power bay NRS module loop-back signal interconnect harness. See End Power Bay NRS Module Loop-back Signal Interconnect Harness on page 97 . | Left end power bay                                                      | J25 P25                 | Same end power bay                                                        | J25 (J25 loops back to itself) | P25               |
| 20-750-MNIH-JMP1 | End power bay NRS module loop-back signal interconnect harness. See End Power Bay NRS Module Loop-back Signal Interconnect Harness on page 97 . | Right end power bay                                                     | J26 P26                 | Same end power bay                                                        | J26 (J26 loops back to itself) | P26               |
|                  | 20-750-MNIH-JMP2 Power-bay-to-power-bay signal interconnect harness Power bay J26 P26                                                           |                                                                         |                         | Next paralleled power bay to the right of the “From” bay                  |                                | J25 P25           |
| 20-750-MNIH-JMP3 | Wire-bay-to-power-bay thermal switch and signal interconnect harness for single input/single output configurations only                         | Wire bay J28 P28                                                        |                         | The adjoining power bay when it is on the right of the wire bay           |                                | J25 P25           |
| 20-750-MNIH-JMP3 | Wire-bay-to-power-bay thermal switch and signal interconnect harness for single input/single output configurations only                         | Wire bay J28 P28                                                        |                         | The adjoining power bay when it is on the left of the wire bay            | J26 P26                        |                   |
| 20-750-MNIH1     | NRS-module-to-power-bay signal interconnect and 240V AC harness                                                                                 | Power bay                                                               | J25 P25                 | NRS module(1)                                                             | J12(1)                         | P12               |
| 20-750-MNIH1     | NRS-module-to-power-bay signal interconnect and 240V AC harness                                                                                 | Power bay                                                               | J26 P26                 | NRS module(1)                                                             | J12(1)                         | P12               |
| 20-750-MNIH1     | NRS-module-to-power-bay signal interconnect and 240V AC harness                                                                                 | TB1-L1 (240V AC L)                                                      | End stripped black wire | NRS module(1)                                                             | J12(1)                         | P12               |
| 20-750-MNIH1     | NRS-module-to-power-bay signal interconnect and 240V AC harness                                                                                 | TB1-N2 (240V AC N)                                                      | End stripped white wire | NRS module(1)                                                             | J12(1)                         | P12               |
| 20-750-MNIH3     | Thermal switch and signal interconnect harness for back-to-back (two lineups back-to-back with dual input/dual output) configurations only      | Back wire bay (left side wire bay when standing next to the wire bays)  | J28 P28                 | Front wire bay (right side wire bay when standing next to the wire bays)  |                                | J28 P28           |
| 20-750-MNIH3     | Thermal switch and signal interconnect harness for back-to-back (two lineups back-to-back with dual input/dual output) configurations only      | Power bay next to back wire bay                                         | J26 P26                 | Power bay next to front wire bay                                          | J25 P25                        |                   |
| 20-750-MNIH4     | Thermal switch and signal interconnect harness for dual output, inline (one lineup with dual input, dual output) configurations only            | Left wire bay (left side wire bay when standing in front of the lineup) | J28 P28                 | Right wire bay (right side wire bay when standing in front of the lineup) |                                | J28 P28           |
| 20-750-MNIH4     | Thermal switch and signal interconnect harness for dual output, inline (one lineup with dual input, dual output) configurations only            | Power bay next to left wire bay                                         | J26 P26                 | Power bay next to right wire bay                                          | J25 P25                        |                   |

End Power Bay NRS Module Loop-back Signal Interconnect Harness

This harness must be installed on the side of a power bay if that side is not joined to a wire bay or another power bay:

- For an installation that uses only one power bay and no wiring bay, both sides of the power bay must have their own loop back harness installed.
- For an end power bay in a multiple power bay (paralleled) system, a loop back harness must be installed on the side of the bay opposite from the adjoining power bay. This is true whether or not a DC voltage balance bay is joined to the end power bay.

Every NRS power bay comes from the factory with two loop-back harnesses installed, one on J25 and one on J26. If you must connect a different signal interconnect harness to a J25 or J26 connector, you must disconnect the loopback harness first.

3. Install the jumper (JMP) interconnect harnesses required for your configuration. See the connection points in Table 19 on page 96, and Figure 61 .

<!-- image -->

Figure 61 - Communication Interconnect Harness Jumpers Example for a 2X+2X System

<!-- image -->

4. If your system has a back-to-back configuration, install the thermal switch signal interconnect harness for back-to-back configurations. See the connection points in Table 19 on page 96 , Figure 62 , Figure 63 on page 100, and the example in Figure 70 on page 104 .

Figure 62 - Back-to-Back Configurations Thermal Switch Routing and Connections (Isometric View)

<!-- image -->

Figure 63 - Back-to-Back Configurations Thermal Switch Routing and Connections (Top View)

<!-- image -->

5. If your system has an inline configuration, install the thermal switch signal interconnect harness for inline configurations. See the connection points in Table 19 on page 96 , Figure 64 , Figure 65 on page 102, and the example in Figure 69 on page 104 .

Figure 64 - Inline Configurations Thermal Switch Routing and Connections (Isometric View)

<!-- image -->

Figure 65 - Inline Configurations Thermal Switch Routing and Connections (Top View)

<!-- image -->

6. If you want your system to use N-1 operation, then in the power bay that will not contain an NRS module, connect the NRS-module-to-bay interconnect harness from J25 and J26 to the N-1 Bypass Jumper (J27). See NRS System N-1 Operation on page 105 .
7. Proceed to Install NRS Modules on page 105. While installing each NRS module into its power bay, you will use an NRS-module-to-bay interconnect harness to connect the NRS module to the power bay. See the connection points in Table 19 on page 96 and the example Figure 66 .

System Communication Interconnect Harness Installation Examples

Figure 66 - Single Power Bay Interconnection Harnesses Example

<!-- image -->

Figure 67 - Wire Entry Bay and One Power Bay Interconnection Harnesses Example

<!-- image -->

Figure 68 - Wire Entry Bay and Two Power Bays Interconnection Harnesses Example

<!-- image -->

Figure 69 - Inline Topology Interconnection Harnesses Example

<!-- image -->

Figure 70 - Back-to-Back Topology Interconnection Harnesses Example

<!-- image -->

## NRS System N-1 Operation

An NRS system can operate at a reduced capacity when one or more of the NRS modules is removed (N-1 operation). To use N-1 operation, you must remove an NRS module and connect the NRS module interconnection wire harness (cat. no. 20-750-MNIH1) to the N-1 bypass jumper (J27) terminal block in the NRS power bay. This connection provides the module-to-module communication for precharge and fault coordination.

Figure 71 - NRS System N-1 Operation Interconnection Wire Harness Configuration Example

<!-- image -->

## Install NRS Modules

Use the following procedure to install an NRS module into a power bay. You can also refer to Summary of NRS Module Connections on page 113, which shows all NRS module connections in one figure.

1. If your system consists of only a single power bay containing a 1X NRS module, with no entry wiring bay, then do the following before installing the NRS module:
- a. Connect customer power wiring to the power bay DC bus and AC power bus. Do not energize customer power supply. For instructions on connecting customer power wiring, see Chapter 5 on page 115 .
- b. Once all customer power wiring is connected to the power bay buses, proceed to install the NRS module with step 2 .
2. Route any customer input and output wiring through the power bay, but do not make input and output connections to the NRS module yet. See Routing Input and Output Wiring on page 20 .
3. Move the NRS module into the power bay:
- a. Use one of the following methods.
- To move the module by using a PowerFlex 750-Series Service Cart, follow the detailed instructions in the PowerFlex 750-Series Service Cart and DCPC Module Lift Installation Instructions, publication 750-IN105. Remove the cart once the module is in place.
- To move the module by using a PowerFlex 755TM service ramp, follow the procedures that are detailed in the PowerFlex 755T Module Service Ramp Instructions, publication 750-IN108. This method is shown in Figure 72 on page 106. Remove the ramp once the module is in place.

<!-- image -->

ATTENTION: NRS modules have a high center of gravity and a tip-over hazard exists. To guard against death, serious personal injury, or equipment damage, do not subject the module to high rates of acceleration or deceleration while transporting. Do not push or pull above the points that are indicated on the module.

- b. Roll the NRS module backward into the power bay until it contacts the PE ground brackets, which are shown in Figure 72 and Figure 73 on page 107. Moving the module backward into the bay makes the AC input connections to the module using stab receptacle connections, which are shown in Figure 73 .
4. Make the PE ground connection from the top of the module to the top PE ground bracket as follows. Secure the top of the module in place using the two M10 x 20 mm Torx screws at the top of the module.
5. Make the PE ground connection from the bottom of the module to the bay floor PE ground bracket as follows. Secure the bottom of the module in place using the two M10 x 20 mm Torx screws at the bottom of the module.

Figure 72 - Placing and Securing the NRS Module into the Power Bay

<!-- image -->

Figure 73 - NRS Module AC Input Connections

<!-- image -->

6. Connect wire harness connectors to the main control circuit board connectors J2 and J12. See Figure 74 for connector descriptions. Figure 75 on page 109 shows the wire harnesses connected to J2 and J12.
7. Make sure that connector P10 is connected to J10 and connector P11 is connected to J11.
8. Connect customer-provided input and output wiring to main control circuit board connectors P10 and P11. You can anchor and shield these wires using the 'T' shaped tie wrap supports above J10 and J11. Make connections as described in Customer Input and Output Connections to Main Control Circuit Board on page 19 .

<!-- image -->

Figure 74 - Main Control Circuit Board Connectors

| Connector Description                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------|
| J2 DC fuse condition signal from connector P2 on the DC link fuses.                                                      |
| J10 Customer output connections for NRS module precharge complete, fault, and alarm signals.                             |
| J11 Customer input connections for NRS module clear faults and precharge enable signals.                                 |
| J12 240V AC and thermal switch control signals from bay harness connector P12.                                           |
| J13  DC bus conditioner signals from connector P13 on the DC bus conditioner (optional, connect if present, see step 9). |

Figure 75 - J2 and J12 Wire Harnesses Connected to Main Control Circuit Board

<!-- image -->

9. If the power bay contains a DC bus conditioner, connect wire harness connector P13 on the DC bus conditioner to J13 on the NRS module main control circuit board.

Figure 76 - DC Bus Conditioner

<!-- image -->

## DC Bus Conditioner Connections

|       | Item Connection Description                                                                                                                                                                               | Terminal Torque      |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| 1 GND | Connection to PE ground.(1) (2)                                                                                                                                                                                                           | 5 N•m (44 lb•in) (2) |
| 2 -DC | Connection to -DC.                                                                                                                                                                                        | 5 N•m (44 lb•in) (2) |
| 3 +DC | Connection to +DC.(2)                                                                                                                                                                                     | 5 N•m (44 lb•in) (2) |
| 4 P13 | DC bus conditioner status signal connection to J13 on the NRS module main control circuit board. This connection is the only connection that must be made for the DC bus conditioner during installation. | —                    |

- (1) When multiple DC bus conditioner modules are installed, the ground wire length must be the same for all modules.
- (2) All wiring and connections are made at the factory and do not need to be made during installation.

10. Install the touch guard that covers the main control board. Insert the tabs on the side of the touch guard into the slots on the module and lower the guard into place.

<!-- image -->

11. Install the M10 nuts that secure the NRS module flexible bus bars to the DC link/fuse assembly.
- Single-density NRS modules have two flexible bus bars.
- Dual-density NRS modules have four flexible bus bars.
12. Install the touch guard that covers the DC link fuse assembly.
13. Close the power bay door.

<!-- image -->

<!-- image -->

## Summary of NRS Module Connections

The NRS module connections are identified in this illustration and table. Also see Main Control Circuit Board on page 18 for connection details.

<!-- image -->

Table 20 - Summary of NRS Module Connections

| Item Connection Description                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 +DC +DC bus connection to DC/link bus bar and fuse.                                                                                                                                                                                                                                 |
| 2 -DC -DC bus connection to DC/link bus bar and fuse.                                                                                                                                                                                                                                 |
| 3 R/L1 AC bus connection from the stab receptacle assembly.                                                                                                                                                                                                                           |
| 4 S/L2 AC bus connection from the stab receptacle assembly.                                                                                                                                                                                                                           |
| 5 T/L3 AC bus connection from the stab receptacle assembly.                                                                                                                                                                                                                           |
| 6 GND PE chassis ground connection.                                                                                                                                                                                                                                                   |
| 7 +DC, -DC +DC and -DC bus test points (not a required connection during installation).                                                                                                                                                                                               |
| 8 J2 DC fuse condition signal from connector P2 on the DC link fuses.                                                                                                                                                                                                                 |
| 9 J10  Customer output connections for NRS module precharge complete, fault, and alarm signals. Customer wires connect to P10 and P10 connects to J10. See Customer Input and Output Connections to Main Control Circuit Board on page 19 for details.                                |
| 10 J11  Customer input connections for NRS module clear faults and precharge enable signals. Customer wires connect to P11 and P11 connects to J11. See Customer Input and Output Connections to Main Control Circuit Board on page 19 for details.                                   |
| 11 J12  240V AC and thermal switch control signals from bay harness connector P12. See Non-Regenerative Supply System Communication Interconnection Harness Kits on page 96 for details.                                                                                              |
| 12 J13 DC bus conditioner signals from connector P13 on the DC bus conditioner (if present).                                                                                                                                                                                          |
| 13  Tie wrap supports These supports can be used for the following: • support the input and output wires with tie wraps • terminate input and output wires to provide a shield ground connection See Customer Input and Output Connections to Main Control Circuit Board on page 19 . |

## IMPORTANT

<!-- image -->

<!-- image -->

Front Protective Cover Removal

Do not remove protective covers from wire harnesses, circuit board connectors, and terminal blocks unless used at the time of installation. For the product to meet the corrosive atmosphere rating, protective covers must remain installed in unused connectors during storage and operation.

## Notes:

## AC Supply Source Considerations

## Grounding Requirements

<!-- image -->

## Power Wiring and System Configuration

Most start-up difficulties are the result of incorrect wiring. Every precaution must be taken to make sure that the wiring is done as instructed. All items must be read and understood before the actual installation begins.

<!-- image -->

ATTENTION: The following information is merely a guide for proper installation. Rockwell Automation, Inc. cannot assume responsibility for the compliance or the noncompliance to any code, national, local or otherwise for the proper installation of this product or associated equipment. A hazard of personal injury and/or equipment damage exists if codes are ignored during installation.

The PowerFlex® 755TM Non-Regenerative Supply is suitable for use on a circuit capable of delivering up to a maximum of 100,000 rms symmetrical amperes at 400/480V and 65,000 rms symmetrical amperes at 600/690V.

The PowerFlex 755TM Non-Regenerative Supply must not be used on undersized or high-impedance supply systems. The supply system kVA must be equal to or greater than the product-related kW, and the system impedance must be less than 10%. Operation outside these limits can cause instability and product shutdown.

System Impedance = (PowerFlex 755TM kVA ÷ Transformer kVA) x Transformer % Impedance

You must account for the kVA of all PowerFlex 755T drives and bus supplies on the distribution system and the system impedance of upstream transformers.

<!-- image -->

ATTENTION: To guard against personal injury and/or equipment damage that is caused by improper fusing or circuit breaker selection, use only the recommended line fuses/circuit breakers that are specified in the Fuses and Circuit Breakers section on page 134 .

If a Residual Current Detector (RCD) is used as a ground fault monitor, use only Type B (adjustable) devices to avoid nuisance tripping.

The safety ground-PE must be connected to system ground. Ground impedance must conform to the requirements of national and local industrial safety regulations and/or electrical codes. Periodically check the integrity of all ground connections as part of preventive maintenance.

## Recommended Grounding Scheme

These diagrams show products that are connected to a solid ground single point (PE only) power source.

For installations within an enclosure, a single safety ground point or ground bus bar connected directly to building steel should be used. All circuits including the AC input ground conductor should be grounded independently and directly to this point/bar.

Figure 77 - Typical Grounding

<!-- image -->

## Grounding Clamps

The clamp kits that are listed in this table can be used to secure round copper ground conductors to 9.5 mm (0.37 in.) thick ground bus bars.

Table 21 - Grounding Clamp Ordering Information and Specifications

| Conductor Cross-section                            | Conductor Cross-section                   | Conductor Cross-section   |
|----------------------------------------------------|-------------------------------------------|---------------------------|
| Kit Catalog Number ISO (mm 2 )                     | AWG/MCM Tightening Torque N•m (lb•in)     |                           |
| SK-RM-GRNDCLMP-16 2.5…16 14…6 AWG 3 (27)           |                                           |                           |
| SK-RM-GRNDCLMP-50 16…50 6…0 AWG 8 (71)             |                                           |                           |
|                                                    | SK-RM-GRNDCLMP-75 35…75 2…00 AWG 12 (106) |                           |
| SK-RM-GRNDCLMP-185 70…185 00 AWG …350 MCM 15 (133) |                                           |                           |

The final assembly Safety Ground-PE must be connected to system ground. Ground impedance must conform to the requirements of national and local industrial safety regulations and/or electrical codes. Periodically check the integrity of all ground connections. For more information on grounding requirements, see PowerFlex 755TM IP00/Open Type Kits Installation Instructions, publication 7 750-IN101, and Wiring and Grounding Guidelines for Pulse Width Modulated (PWM) AC Drives, publication DRIVES-IN001 .

## Radio Frequency Interference (RFI) Filter Grounding

Using optional RFI filters can result in relatively high ground leakage currents. Therefore, the filter must only be used in installations with grounded AC supply systems and be permanently installed and solidly grounded (bonded) to the building power distribution ground. Be sure that the incoming supply neutral is solidly connected (bonded) to the same building power distribution ground. Grounding must not rely on flexible cables and must exclude any form of plug or socket that would permit inadvertent disconnection. Some local codes can require redundant ground connections. Periodically check the integrity of all connections. See the instructions that are supplied with the filter.

## Dual Input and Dual Output Power Wiring Requirements

This section provides strict guidance for input and output power sources and wiring for NRS systems with two 3-phase AC inputs and two DC outputs. These systems have either an inline or back-to-back topology. Use the table and diagrams in this section to verify that your product and application meets these requirements.

Table 22 - Dual Input and Dual Output NRS System Power Wiring Requirements

| Power Connections   | Configuration Rule     |                                                                                                                                                                                                                                                                      |
|---------------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC Input            | Inline or Back-to-Back | Two entry wire bays (WB) must be used for independent three-phase AC input power connections (AC Input-1 and AC Input-2).                                                                                                                                            |
| AC Input            | Inline or Back-to-Back | AC Input-1 and AC Input-2 must have the same power source and phase sequence.                                                                                                                                                                                        |
| AC Input            | Inline or Back-to-Back | The cable length and impedance from the AC power source to AC Input-1 and AC Input-2 must be the same.                                                                                                                                                               |
| DC Bus              |                        | Inline Must be continuous.                                                                                                                                                                                                                                           |
| DC Bus              | Back-to-Back           | A single balance connection must be provided at the motor end of the shared DC bus. This balance connection must be removed from the bus supply DC bus output when a DC balance connection is used at the motor end of a common bus inverter running a single motor. |
| DC Output           |                        | Back-to-Back A DC voltage balance bay (DCVBB) must be used.                                                                                                                                                                                                          |
| DC Output           | Inline or Back-to-Back | The DC bus bar or cable length and impedance from the DC bus output (DC Output-1 and DC Output-2) to the common bus inverter DC input (where applicable) must be the same.                                                                                           |
| DC Output           | Inline or Back-to-Back | All connected common bus inverters must have a common DC bus.                                                                                                                                                                                                        |
| DC Output           | Inline or Back-to-Back | The load on DC Output-1 or DC Output-2 must not exceed 55% of the total bus supply rating.                                                                                                                                                                           |
| DC Output           | Inline or Back-to-Back | The total load must not exceed 100% of the bus supply rating.                                                                                                                                                                                                        |

Figure 78 - NRS System Inline Power Wiring Diagram

<!-- image -->

Figure 79 - NRS System Back-to-Back Configuration Power Wiring Diagram

<!-- image -->

2 (2X +1X) Shown

2 (2X +1X) Shown

## NRS Output Bay Connections to Drive Bays

An output bay in an NRS system can be either a power bay, for systems that are not back-to-back, or a DC voltage balance bay, for systems that are back-toback. Drive bays must be connected to an NRS output bay. The following example shows the connections between the following bays:

- An NRS output bay (in this example a DC voltage balance bay), and a drive bay that contains a DC input drive.
- A drive bay and another drive bay. Additional drive bays can be added using the same splice connections.

Figure 80 - NRS Output Bay Connections to Drive Bays

<!-- image -->

If the drive bay is a PowerFlex 755TM common bus inverter of frame size 8 or higher, it comes with DC buses, a PE ground bar, and a control bus bar installed.

If you are connecting a PowerFlex 755TM common bus inverter or a DC input drive that does not come in a bay with a DC bus installed, you must build a drive bay starting with an empty Rittal enclosure. You must install the following in the enclosure to make it into a drive bay:

- Two DC bus bars from Rockwell Automation. See Drive Bay DC Bus Bars .
- One PE ground bar from Rittal. See Drive Bay PE Ground Bars on page 120 .
- One or more PowerFlex 755TM common bus inverters or one or more DC input drives. Each common bus inverter or DC input drive must connect to the DC common bus within the same bay it is installed in.

Optionally, you can also install a control bus bar in your drive bays. See Drive Bay Control Bus Bars on page 121. To make splice connections between an NRS output bay and a drive bay, or a drive bay and a drive bay, use the torque specifications in Figure 57 on page 93 .

## Drive Bay DC Bus Bars

Select from the following DC bus bar kits. You must use two identical bus bars in each drive bay.

Table 23 - DC Bus Bar Kits

| Enclosure Width mm (in.)   | Cat. No.  Material  Thickness mm (in.) Weight kg (lb)  Amps    |
|----------------------------|----------------------------------------------------------------|
|                            | 20-750-MDCBUS4-3K0 400 (16) Aluminum 27 (1.1) < 22.7 (50) 3000 |
|                            | 20-750-MDCBUS4-4K7 400 (16) Copper 37 (1.5) < 22.7 (50) 4700   |
|                            | 20-750-MDCBUS6-3K0 600 (24) Aluminum 27 (1.1) < 22.7 (50) 3000 |
|                            | 20-750-MDCBUS6-4K7 600 (24) Copper 37 (1.5) 25.2 (56) 4700     |
|                            | 20-750-MDCBUS8-3K0 800 (31) Aluminum 27 (1.1) < 22.7 (50) 3000 |
|                            | 20-750-MDCBUS8-4K7 800 (31) Copper 37 (1.5) 39.5 (87) 4700     |

Once the DC bus bars are installed and the bay is joined to the lineup, splice the DC bus bars to the DC common buses. If this bay is the first bay next to the NRS output bay, it must be spliced to the DC bus bars of the NRS output bay. If it is a bay that is installed farther downstream from the NRS output bay, it must be spliced to the DC bus bars of the previous PowerFlex 755TM common bus inverter or DC input drive bay. Use two identical splice kits, one for each DC bus bar. Choose from the following kits.

Table 24 - DC Bus Bar Splice Kits

| Cat. No.                             | Material Thickness mm (in.)   |   Amps |
|--------------------------------------|-------------------------------|--------|
| 20-750-MDCSPL1-3K0 Aluminum 25 (1.0) |                               |   3000 |
| 20-750-MDCSPL1-4K7 Copper 25 (1.0)   |                               |   4700 |

## Drive Bay PE Ground Bars

The customer must provide PE ground bars in drive bays. PE ground bars must meet the following specifications.

Table 25 - Ground Bus Bar Specifications

| Tin-plated Copper (1)   | Tin-plated Aluminum (2)   |
|-------------------------|---------------------------|
| 483 mm 2  (0.75 in. 2   | ) 483 mm 2  (0.75 in. 2 ) |

(1) UNS C11000 ETP tin-plated Copper

(2) 1100-H12, 1100-H14, 6063-T5, or 6101-T61, tin-plated aluminum

PE ground bars in all drive bays must be connected through splicing back to the NRS output bay PE ground bar.

Table 26 - Ground Bus Bar Splice

|                                     | Cat. No. Material Thickness mm (in.)   |
|-------------------------------------|----------------------------------------|
| 20-750-MGNDSPL1 Aluminum 9.5 (0.37) |                                        |

## Power Cable Specifications

## Drive Bay Control Bus Bars

A control bus bar is optional in drive bays. If you choose to include one, select from the following kits.

Table 27 - Control Bus Assemblies

| Cat. No.                               | Voltage Amps Cabinet Width mm (in.)   |
|----------------------------------------|---------------------------------------|
| 20-750-MCBUS1-IB-F8M 240 100 400 (16)  |                                       |
| 20-750-MCBUS1-PB-F10M 240 100 800 (31) |                                       |

If you use a control bus bar in a drive bay, it must be connected through splicing back to the NRS output bay control bus bar.

Table 28 - Control Bus Splice

| Cat. No.                    | Voltage Amps   |
|-----------------------------|----------------|
| 20-750-MCTRLBUS-SPL 240 100 |                |

The following types of power cables are used with the NRS and the DC common bus that is powered by the NRS.

- Cables for AC input power to the NRS
- Cables for DC power connections between a DC common bus, which is powered by the NRS, and a PowerFlex 755TM common bus inverter or DC input drive.

Various cable types are acceptable for NRS installations. For an in-depth discussion of cable types, see the Wiring and Grounding Guidelines for Pulse Width Modulated (PWM) AC Drives, publication DRIVES-IN001 .

## Power Cable Types Acceptable for 400…690 Volt Installations

<!-- image -->

ATTENTION: National codes and standards (NEC, BSI, and so forth) and local codes outline provisions for safely installing electrical equipment. Installation must comply with specifications regarding wire types, conductor sizes, branch circuit protection, and disconnect devices. Failure to do so can result in personal injury and/or equipment damage.

Table 29 - Power Cable Recommendations

| Type                  | Cable Description   | Min Insulation Rating                                                                                                                                                                                                  |    |
|-----------------------|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|
| AC Input Power (1)(2) | Standard            | • Three tinned copper conductors with XLPE insulation. • Copper braid/aluminum foil combination shield and tinned copper drain wire, three drain wires per cable assembly. • PVC jacket. • Maximum 500 MCM conductors. | 400…600V systems: 600V, 75 °C (167 °F) (3) 690V systems: ° y 2000V, 90 °C (194 °F)    |
| DC Output Power (4)   |                     | • Two tinned copper conductors with XLPE insulation. • Maximum 500 MCM conductors.                                                                                                                                     | 400…600V systems: °° y 600V, 75 °C (167 °F) 690V systems: ° y 2000V, 90 °C (194 °F)    |

## Power Cable Connections

Observe the specifications that are listed in this section for AC line input power and DC output cable connections. AC line and DC output cables that are fitted with barrel lugs connect directly to the bus bar or to L-brackets as indicated in the following table.

Table 30 - Power Input and Output Connections

| Connection Type Bay   |                                                                                                                 | L-Brackets Included (1)    |
|-----------------------|-----------------------------------------------------------------------------------------------------------------|----|
| AC line input         | NRS Power bay No                                                                                                |    |
| AC line input         | NRS Entry wire bay Yes                                                                                          |    |
| DC output             | PowerFlex 755TM common bus inverter of frame size 8 or higher power bay                                         | No |
| DC output             | Rittal bay with Rockwell Automation bus bar kits to house PowerFlex 755TM common bus inverter or DC input drive | No |

## UL Listed Barrel Lugs

Use UL Listed barrel lugs to make AC line input power and DC output connections to bus bars and L-brackets.

- Barrel lugs are customer-supplied.
- Use only copper barrel lugs with tin or zinc plating.
- Barrel lugs can be either crimp or mechanical type.
- Use the vendor-recommended tooling to fasten crimp type terminals to cabling.
- Torque mechanical type terminals according to vendor instructions.
- Barrel lugs must have the dimensions that are shown in Figure 81 .

Figure 81 - UL Listed Barrel Lug Dimensions

<!-- image -->

## Barrel Lug to Bus Bar Connections

For an NRS system that consists of a single 1X power bay and no entry wire bay, power cable barrel lugs must be connected directly to the AC input bus bars in the 1X power bay. There must not be an L-bracket between the barrel lugs and bus bars due to limited space.

For an NRS system that includes an entry wire bay, use the following rules about when to use barrel lug to bus bar connections for AC input:

- If the only power bay is a 1X power bay, you can use either barrel lug to bus bar connections, or barrel lug to L-bracket to bus bar connections.
- If there is any other power bay than a single 1X power bay, such as a single 2X power bay, or multiple power bays, you must use barrel lug to Lbracket to bus bar connections. See Barrel Lug to L-Bracket to Bus Bar Connections on page 124 .

Barrel lug to bus bar connections can be used for the following types of output connections. Alternatively, these output connections could also use barrel lug to L-bracket to bus bar connections:

- DC output connected to the DC common bus in a PowerFlex 755TM common bus inverter bay
- DC output connected to the DC common bus in a DC input drive bay

Barrel lugs must have the specifications that are listed in UL Listed Barrel Lugs on page 122. Connect the barrel lug with the fastening hardware that is provided. Keep the wire connections at least 51 mm (2 in.) away from the ends of the slotted bus bar. Fastening hardware can be inserted into the channel of a slotted bus bar through the opening in the center of the bus bar, or at the end of the bus bar.

<!-- image -->

## Barrel Lug to L-Bracket to Bus Bar Connections

For an NRS system that includes an entry wire bay, use the following rules about when to use barrel lug to L-bracket to bus bar connections for AC input:

- If the only power bay is a 1X power bay, you can use either Barrel Lug to Bus Bar Connections on page 123, or barrel lug to L-bracket to bus bar connections.
- If there is any other power bay than a single 1X power bay, such as a single 2X power bay, or multiple power bays, you must use barrel lug to Lbracket to bus bar connections.

Barrel lug to L-bracket to bus bar connections can be used for the following types of output connections. Alternatively, these output connections could also use barrel lug to bus bar connections:

- DC output connected to the DC common bus in a PowerFlex 755TM common bus inverter bay
- DC output connected to the DC common bus in a DC input drive bay

Barrel lugs must have the specifications that are listed in UL Listed Barrel Lugs on page 122. The M10 hardware that is required to fasten the L-brackets to the slotted bus bar is provided. Power cables with the appropriate barrel lugs can be bolted to both sides of the L-brackets if necessary. Up to four conductors can be attached to each L-bracket. Attach the conductors to the L-brackets using customer supplied M12 or 0.5 in. diameter bolts, nuts, and washers. Bellville spring washers, or equivalent, are recommended. Keep the L-bracket connections at least 51 mm (2 in.) away from the ends of the slotted bus bar.

<!-- image -->

## Additional Power Terminal L-Brackets

The entry wire bays of NRS products come equipped with L-brackets. If an application requires additional L-brackets, kit number 20-750-MLBRKT-F8M is available. Each kit contains three L-brackets and mounting hardware.

Figure 82 - L-Bracket Approximate Dimensions

<!-- image -->

When using mechanical barrel lugs, which may be large, be sure to maintain adequate spacing to adjacent wires, terminals, and other parts.

Figure 83 - Typical Barrel Lug Connection to L-Bracket Options

<!-- image -->

## Recommended Cable Spacing

NRS products require multiple conductors in parallel. Use the rated current of the product, specific application needs, local codes, and operating conditions to determine wire size and the number of conductors needed. When using multiple conductors per phase, symmetrical spacing of the input and output power cabling over the span of the bus bar for each phase is required.

When using multiple conductors per phase, wires must be arranged so that each conduit, bundle, or cable contains equal numbers of conductors from all three phases.

<!-- image -->

Figure 85 - Recommended Cable Spacing Example

<!-- image -->

Figure 86 - Recommended L-bracket Spacing Example

<!-- image -->

## Bus Bar Locations

<!-- image -->

Figure 87 - Single-Density (1X) and Dual-Density (2X) Power Bay Power Structures

|                    | Item Name Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                    | 1 DC Bus DC+, DC- Output                                                                                                                                                                                                                                                                                                                                                                                                                |
|                    | 2 Control bus Control power supply                                                                                                                                                                                                                                                                                                                                                                                                      |
|                    | 3 AC Power Bus R/L1, S/L2, T/L3 AC line input power connections.                                                                                                                                                                                                                                                                                                                                                                        |
| 4 PE Grounding Bar | Terminating point to chassis ground for the following: • incoming AC line in the power bay if there is no wire entry bay • motor shield in the PowerFlex 755TM common bus inverters or DC input drives that are downstream from the NRS bays (no motor shield connection is made in any NRS bays including entry wire bays, power bays, and DC voltage balance bays) PE ground bar clamps, kit number SK-RM-GRNDCLMP-nn, are available. |
| 5 AC Testpoints    | R/L1, S/L2, T/L3 voltage testpoint sockets. Always replace the protective caps on the AC testpoints if present.                                                                                                                                                                                                                                                                                                                         |
| 6 DC Testpoints    | DC+, DC- voltage testpoint sockets. Always replace the protective caps on the DC testpoints if present.                                                                                                                                                                                                                                                                                                                                 |

## Use the DC bus and AC power bus as follows:

- Connect customer power directly to these buses only if your system consists of only a single power bay containing a 1X NRS module, with no wire entry bay. Customer power wiring must enter through the bottom of the power bay, as described on page 50 and page 60 .
- If your system includes a wire entry bay, shown in Figure 88 on page 130 , connect customer power to the buses in the wire entry bay or bays. Those buses supply all paralleled power bays through the spliced bus system. See Bus Bar Splice Connections on page 91 .

<!-- image -->

Figure 88 - Entry Wire Bays and DC Voltage Balance Bay

| Item Name Description                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 DC bus DC power supply                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2 Control bus Control power supply                                                                                                                                                                                                                                                                                                                                                                                             |
| 3 AC power bus R/L1, S/L2, T/L3 AC line input power connections                                                                                                                                                                                                                                                                                                                                                                |
| 4 PE grounding bar Termination point to chassis ground for the following: • incoming AC line in wire entry bays • motor shield in the PowerFlex 755TM common bus inverters or DC input drives that are downstream from the NRS bays (no motor shield connection is made in any NRS bays including entry wire bays, power bays, and DC voltage balance bays) PE ground bar clamps, kit number SK-RM-GRNDCLMP-nn, are available. |

## Control Transformers

Your product uses one of two possible control transformer options. Which option it uses can be found in the product catalog number, as described in 20J Control and Power Options Selection on page 29. The options are the following:

| Code   | Option                                                                                                         |
|--------|----------------------------------------------------------------------------------------------------------------|
| C1     | Bus Supply Control Transformer (T1 standard transformer) and CBI Control Transformer (T2 optional transformer) |
| C2     | Bus Supply Control Transformer (T1 standard transformer) Only                                                  |

All NRS modules (control codes C1 and C2) use the T1 standard transformer, which provides 240V AC power to the NRS module bus supply.

## IMPORTANT

Do not power the NRS module with an external 240V AC control power source.

A control bus is optional in the PowerFlex 755TM common bus inverters (CBIs) or DC input drives that are powered by the NRS. If you choose to use a control bus in these CBIs or drives, there are two options to provide power the control bus:

- NRS products with control code C1 have the T2 optional transformer, which provides 240V AC power to the control bus. The T2 transformer is only for the control bus and does not provide power to the NRS module.
- NRS products with control code C2 do not provide power to the control bus. In this situation, to power the control bus, you must use a customer provided external control power supply. This external power supply may be a 240V AC power supply, a 120V AC power supply, or a 24V DC power supply, depending on what type of equipment must be connected to the control bus. See Customer Provided Control Bus Power on page 133

Figure 89 - Control Transformers Voltage Taps

<!-- image -->

T2 Optional Transformer (included in option C1 only)

Figure 90 - Control Transformers Fuse Locations

<!-- image -->

Table 31 - Control Transformer (FH1…FH6) Fuses

|         | Item Description                                                                | Input Voltage Cat. No.   | Rating [V/A] Qty.                      |
|---------|---------------------------------------------------------------------------------|--------------------------|----------------------------------------|
| FH1…FH3 | T1, 1 kVA (Standard transformer)                                                |                          | 400/480/600 SK-RM-NRSF1F2-CDE 600/6 3  |
| FH1…FH3 | T1, 1 kVA (Standard transformer)                                                | 690                      | SK-RM-NRSF1F2-F 690/4 3                |
| FH4…FH6 | T2, 3 kVA (Optional transformer used with PowerFlex 755TM common bus inverters) |                          | 400/480/600 SK-RM-NRSF4F5-CDE 600/20 3 |
| FH4…FH6 |                                                                                 | 690                      | SK-RM-NRSF4F5-F 690/12 3               |

## Customer Provided Control Bus Power

If you choose to use a control bus (optional) in the CBIs or drives that are powered by the NRS, there are multiple options for providing customer provided power to the control bus. All of these options use the control bus connector (cat. no. 20-750-MCTRLBUS-CONN1). The options are the following:

- 240V AC. This voltage could alternatively be provided by a T2 Optional Transformer (only available in products with control code C2, see Control Transformers on page 131).
- 120V AC
- 24V DC

The control bus connector provides tension clamp terminals for customer provided power cable. The location of the control bus is shown in Figure 88 on page 130. Use a customer provided harness to support the power cable.

## Control Bus Connector Ratings

| Cat. No.                 |   Max Voltage Max Amps No. of Terminals Per Pole |                   |
|--------------------------|--------------------------------------------------|-------------------|
| 20-750-MCTRLBUS-CONN1(1) |                                              240 | 10 per terminal 2 |

- (1) Up to five 20-750-MCTRLBUS-CONN1 connectors can be used in parallel on the control bus assembly to reach a maximum of 100 amps per circuit (240V AC, 240/120V AC, or 24V DC).

Figure 91 - Control Bus Connector 20-750-MCTRLBUS-CONN1

<!-- image -->

## Control Bus Connector 20-750-MCTRLBUS-CONN1 Connections

| Item Name Description                 | Conductor Cross Sections(2)   | Conductor Cross Sections(2)   | Conductor Cross Sections(2)   |
|---------------------------------------|-------------------------------|-------------------------------|-------------------------------|
| Item Name Description                 | ISO (mm 2 )                   | AWG Strip Length              |                               |
| 1 L 240V 240V AC Line                 |                               | 0.2…1.5 26…14 7 mm (0.28 in.) |                               |
| 2 N 240V 240V AC Neutral              |                               | 0.2…1.5 26…14 7 mm (0.28 in.) |                               |
| 3 L 120V/240V  120/240V AC Line(1)    |                               | 0.2…1.5 26…14 7 mm (0.28 in.) |                               |
| 4 N 120V/240V  120/240V AC Neutral(1) |                               | 0.2…1.5 26…14 7 mm (0.28 in.) |                               |
| 5 +24V 24V DC Power                   |                               | 0.2…1.5 26…14 7 mm (0.28 in.) |                               |
| 6 COM 24V 24V DC Common               |                               | 0.2…1.5 26…14 7 mm (0.28 in.) |                               |

## Fuses and Circuit Breakers

The tables on the following pages provide recommended AC line input fuse and circuit breaker information. Sizes that are listed are the recommended sizes that are based on 40 °C (104 °F) and the U.S. NEC. Other country, state, or local codes can require different ratings. In addition, floor mount bus supplies include AC line and DC bus fuses (with blown fuse indicators) to provide short circuit protection.

## Fuses

The recommended fuse types are listed here. If available current ratings do not match the ratings that are listed in the tables that are provided, choose the next higher fuse rating.

- IEC – Use type gG or equivalent conforming to EN60269-1, Parts 1 and 2.
- UL – Use Class T, RK1, J, or L type conforming to UL 248.

## Circuit Breakers

The 'non-fuse' listings in the following tables include inverse time circuit breakers and instantaneous trip circuit breakers (motor circuit protectors). Both types of circuit breakers are acceptable for IEC installations.

| IMPORTANT   | We recommend that you use external fuses for branch circuit protection. External fusing helps protect the NRS if an industrial accident causes an internal short while the NRS is energized. Circuit breakers can be used in series with fuses as means for disconnection.   |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table 32 - 400V AC and 480V AC Input Protection Devices

| Motor CircuitProtector(2)  (2)                   | Motor CircuitProtector(2)  (2)   | 00/1500 1000/900/800                        |                                                                 | 0 1900/1800/1400                              | 00 1700/1600/1300                                              | 4300 2800/2600/2200                         | 4000 2600/2400/2000                          | 5700 3700/3400/2800                                                            | 5300 3400/3200/2600                        | 6000 4600/4200/3500 6000 4200/3900/3300                 |                                                                                                                                                              | . AC input protection devices f or                                                                   |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
|--------------------------------------------------|----------------------------------|---------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|----------------------------------------------------------------|---------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|--------------------------------------------------|
| Circuit Breaker (1)                              | Max  (LD/ND/HD)                  |                                             | 900/700 1800/1700/1400 900/900/700                              | 00/1400 3800/3500/280                         |                                                                | 00/2200 5600/5200/                          |                                              | 400/3200/2600 6000/6000/                                                       | 4600/4200/3500 6000/6000/                  | 3300 6000/6000/                                         |                                                                                                                                                              |                                                                                                      |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| Circuit Breaker (1)                              | Min  (LD/ND/HD)                  | 1000/900/800 2000/18                        |                                                                 |                                               | 100 1700/1600/1300 3500/3100/26                                |                                             | 00/4800 2600/2400/2000 5200/4800/            | 5200/4800/4000 3700/3400/2800 6000/6000/6000 3700/3400/2800 6000/6000/         |                                            | /6000 4200/3900/                                        |                                                                                                                                                              |                                                                                                      |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| Dual Element Time Delay Fuse Non-Time Delay Fuse | Max (4)  (LD/ND/HD)              | 00/800 2400/2200/1800                       | 00/1000 900/900/700 2200/2000/1700 900/                         | 4600/4200/3400 1900/18                        |                                                                | 000/5200 2800/26                            |                                              |                                                                                | 00/4200/3500 6000/6000/6000                |                                                         |                                                                                                                                                              | each of the two sections must be determined from the values that are provided for the lower ratings. |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| Dual Element Time Delay Fuse Non-Time Delay Fuse | 1/Phase  Min (3)  (LD/ND/HD)     |                                             |                                                                 | 500/2000 1900/1800/1400                       |                                                                | 2600/2200 6000/6                            | 00/3300/2800 2600/2400/2000 6000/57          |                                                                                |                                            | 00/4600 4200/3900/3300 6000/6000                        |                                                                                                                                                              | For these 12 highest ratings, the NRS has to be configured as two sections (inline or back-back)     |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| AC Input Protection Devices                      | Max (4)  (LD/ND/HD)              |                                             |                                                                 |                                               |                                                                | 3900/3600/3000 2800/                        |                                              |                                                                                | 6000/5900/5000 46                          |                                                         |                                                                                                                                                              |                                                                                                      |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| AC Input Protection Devices                      | 1/Phase Min (3)  (LD/ND/HD)      | 1000/900/800 1400/1300/1100 1000/9          | 480 527/529/441 736/681/568 883/817/681 1 — 900/900/700 1300/12 | — 1 1900/1800/1400 2700/2                     | 3 — 1 1700/1600/1300 2400/2200/1800 1700/1600/1300 4200/3800/3 | /2072 1 1 2800/2600/2200                    | 1907 1 1 2600/2400/2000 36                   | 68/3023/2520 — 2 3400/3200/2600 4800/4400/3700 3400/3200/2600 6000/6000/6300 3 | 0/3493 1 2 4600/4200/3500                  | 200/3900/3300 6000/55                                   |                                                                                                                                                              |                                                                                                      |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| Quantity of 2X Modules                           | Quantity of 2X Modules           |                                             |                                                                 |                                               |                                                                |                                             |                                              |                                                                                |                                            |                                                         |                                                                                                                                                              |                                                                                                      |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| Quantity of 1X Modules                           | Quantity of 1X Modules           |                                             |                                                                 |                                               |                                                                |                                             |                                              | 9 3548/3282/2738 — 2 3700/3400/2800                                            |                                            |                                                         |                                                                                                                                                              | 75/5402 — 4                                                                                          |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| Output Amps DC (LD/ND/HD)                        | Output Amps DC (LD/ND/HD)        | 400 518/479/400 799/739/616 959/887/740 1 — |                                                                 |                                               |                                                                |                                             |                                              |                                                                                |                                            | 400 2848/2634/2198 4395/4065/3388 5275/4879/4070 — 3    | 480 3147/2912/2427 4048/3746/3124 4857/4494/3746 — 3400 2848/2634/2198 4395/4065/3388 5275/4879/4070 2 2480 3147/2912/2427 4048/3746/3124 4857/4494/3746 2 2 | 95/4497 7001/64                                                                                      | 480 4177/3865/3221 5373/4971/4146 6446/5964/4971 — 4400 4713/4359/3636 7271/6725/5606 8727/8072/6734 — 5480 5207/4818/4016 6698/6197/5169 8035/7435/6197 — 5400 4713/4359/3636 7271/6725/5606 8727/8072/6734 2 4480 5207/4818/4016 6698/6197/5169 8035/7435/6197 2 4 | 5645/5221/4356 8709/8055/6714 10453/9668/8066 — 6 | 6237/5771/4810 8022/7423/6191 9625/8905/7423 — 6 |
| Input Amps AC (LD/ND/HD)                         | Input Amps AC (LD/ND/HD)         |                                             |                                                                 | 400 938/910/731 1517/1406/1128 1821/1685/1354 | 480 1087/977/812 1398/1256/1044 1678/1507/125                  | 400 1450/1341/1119 2237/2069/1725 2685/2484 | 480 1603/1482/1236 2061/1907/1590 2473/2288/ | 480 2118/1959/1633 2723/2520/2102 32                                           | 400 2382/2203/1886 3675/3399/2834 4411/408 | 480 2633/2435/2132 3386/31 33/2613 4063/3758/3290 1 2 4 |                                                                                                                                                              | 400 3780/3497/2917 5833/53                                                                           |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| kW Ratings (LD/ND/HD)                            | kW Ratings (LD/ND/HD)            |                                             |                                                                 |                                               |                                                                |                                             |                                              | 400 1916/1772/1479 2956/2734/227                                               |                                            |                                                         |                                                                                                                                                              |                                                                                                      |                                                                                                                                                                                                                                                                      |                                                   |                                                  |
| Voltage                                          | Voltage                          |                                             |                                                                 |                                               |                                                                |                                             |                                              |                                                                                |                                            |                                                         |                                                                                                                                                              |                                                                                                      |                                                                                                                                                                                                                                                                      | 400 (5)                                           | 480 (5)                                          |

Rockwell Automation Publication 750-UM100B-EN-P - May 2022

(1) Inverse time circuit breaker. For U.S. NEC, minimum size is 125% of rated AC input current. (2) Instantaneous trip circuit breaker. The trip setting should be set to the input current of the NRS and should be sized based on the continuous current of the system. (3) Minimum protection device size is the lowest rated device th at provides protection without nu isance tripping. For U.S. NEC, minimum size is 125% of rated AC input current. (4) Maximum protection device size is the highest rated device that provides protection to the NRS. (5) The available Rockwell Automation IP00 Open Type bus bar kits do not support a higher rating, but this configuration can be used for reserve capacity for NRS system N-1 operation.

Table 33 - 600V AC and 690V AC Input Protection Devices

| Motor Circuit Protector(2)  (2)   | Motor Circuit Protector(2)  (2)   | 1300/1000 700/600/500                         | 1300/1000 700/600/500                         | 1100/900                                                                                 | 0/1100/900                                                                             | 2900 1900/1800/1400                 | 2900 1900/1800/1400                          | 3800 2500/2300/1900 3800 2500/2300/1900                                | 4800 3100/2900/2400                     | 4800 3100/2900/2400                                                            | 5700 3700/3400/2800                                     | 5700 3700/3400/2800                                     |                                                         |                                                         | 5700 3700/3400/2800 5700 3700/3400/2800              | s for                                                                                                                                                                                                                                                                                                                    | s for                      | s for   | s for   | s for   |
|-----------------------------------|-----------------------------------|-----------------------------------------------|-----------------------------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------|----------------------------------------------|------------------------------------------------------------------------|-----------------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|---------|---------|---------|
|                                   | Max  (LD/ND/HD)                   |                                               |                                               |                                                                                          |                                                                                        |                                     |                                              | 1900 4900/4600/ 1900 4900/4600/                                        | 00/2400 6000/5800/                      |                                                                                |                                                         |                                                         |                                                         |                                                         |                                                      | two sections (inline or back-back). AC input protection device                                                                                                                                                                                                                                                           |                            |         |         |         |
|                                   | Min  (LD/ND/HD)                   | 00 700/600/500 1300/                          | 00 700/600/500 1300/                          |                                                                                          |                                                                                        | 200/3500 1900/1800/1400 3700/3500/  | 200/3500 1900/1800/1400 3700/3500/           | 00/4600 2500/2300/ 5600/4600 2500/2300/                                |                                         |                                                                                |                                                         |                                                         |                                                         |                                                         |                                                      |                                                                                                                                                                                                                                                                                                                          |                            |         |         |         |
|                                   | Max (4)  (LD/ND/HD)               |                                               | 00/600/500 1600/1500/12                       | /1100/900 1800/1600/1300 1300/1100/900 3000/2700/2300 1300/1100/900 2500/2300/1900 1300/ | /1100/900 1800/1600/1300 1300/1100/900 3000/2700/2300 1300/1100/900 2500/2300/1900 130 |                                     |                                              | /2300/1900 5900/56                                                     | 00/6000/5700 3100/29                    | 00/2400 4300/4000/3300 3100/2900/2400 6000/6000/5700 3100/2900/2400 6000/5800/ | 3700/3400/2800 6000/6000/6000 3700/3400/2800 6000/6000/ | 3700/3400/2800 6000/6000/6000 3700/3400/2800 6000/6000/ | 3700/3400/2800 6000/6000/6000 3700/3400/2800 6000/6000/ | 3700/3400/2800 6000/6000/6000 3700/3400/2800 6000/6000/ |                                                      | each section must be determined from the values that are provided for the lower ratings.                                                                                                                                                                                                                                 |                            |         |         |         |
|                                   | 1/Phase  Min (3)  (LD/ND/HD)      | 00/600/500 1600/1500/12                       |                                               |                                                                                          |                                                                                        | 00/2500/2000 1900/1800/1400 4500/4  | 00/2500/2000 1900/1800/1400 4500/4           | 00/3200/2700 2500/2300/1900 5900/                                      |                                         |                                                                                |                                                         |                                                         |                                                         |                                                         |                                                      |                                                                                                                                                                                                                                                                                                                          |                            |         |         |         |
|                                   | Max (4)  (LD/ND/HD)               | 00/600/500 900/900/700 7                      | 00/600/500 900/900/700 7                      |                                                                                          |                                                                                        |                                     |                                              |                                                                        | 00 4300/4000/3300 3100/2900/2400 60     |                                                                                |                                                         |                                                         |                                                         |                                                         |                                                      | For these eight highest ratings, the NRS has to be configured as                                                                                                                                                                                                                                                         |                            |         |         |         |
|                                   | 1/Phase  Min (3)  (LD/ND/HD)      |                                               |                                               |                                                                                          |                                                                                        | 792/1686/1392 1 1 1900/1800/1400 26 | 1392 1 1 1900/1800/1400 26                   | 368/2227/1839 — 2 2500/2300/1900 3500/3200/2700 2500                   | 05/1904 2944/2769/2286 1 2 3100/2900/24 |                                                                                | 7 3520/3311/2734 — 3 3700/3400/2800 5100/4800/4000      | 7 3520/3311/2734 — 3 3700/3400/2800 5100/4800/4000      | 7 3520/3311/2734 2 2 3700/3400/2800 5100/4800/4000      |                                                         |                                                      |                                                                                                                                                                                                                                                                                                                          |                            |         |         |         |
| Quantity of 2X Modules            | Quantity of 2X Modules            |                                               |                                               |                                                                                          |                                                                                        |                                     |                                              |                                                                        |                                         |                                                                                |                                                         |                                                         |                                                         |                                                         |                                                      |                                                                                                                                                                                                                                                                                                                          |                            |         |         |         |
| Quantity of 1X Modules            | Quantity of 1X Modules            |                                               |                                               |                                                                                          |                                                                                        |                                     |                                              |                                                                        |                                         |                                                                                |                                                         |                                                         | 7 3520/3311/2734 2 2 3700/3400/2800 5100/4800/4000      |                                                         |                                                      |                                                                                                                                                                                                                                                                                                                          | 61/4513 6976/6562/5417 — 6 |         |         |         |
| Output Amps DC (LD/ND/HD)         | Output Amps DC (LD/ND/HD)         | 600 518/488/403 534/501/414 640/602/497 1 — 7 | 690 596/561/463 534/501/414 640/602/497 1 — 7 | 600 986/876/738 1014/901/759 1217/1082/911 — 1 1300                                      | 690 1134/1008/849 1014/901/759 1217/1082/911 — 1 1300                                  |                                     | 690 1669/1570/1296 1495/1403/1159 1792/1686/ |                                                                        |                                         | 690 2742/2580/2130 2456/2305/1904 2944/2769/2286 1 2 3100/29                   |                                                         |                                                         | 690 3279/3084/2546 2937/2756/227                        |                                                         | 600 3784/3560/2939 3898/3657/3022 4672/4395/3628 — 4 |                                                                                                                                                                                                                                                                                                                          |                            |         |         |         |
| Input Amps AC (LD/ND/HD)          | Input Amps AC (LD/ND/HD)          |                                               |                                               |                                                                                          |                                                                                        | 600 1452/1365/1127 1495/1403/1159 1 |                                              | 600 1918/1804/1490 1976/1854/1532 2                                    |                                         |                                                                                | 600 2851/2682/2214 2937/2756/227                        | 690 3279/3084/2546 2937/2756/227                        | 600 2851/2682/2214 2937/2756/227                        |                                                         |                                                      | 690 4352/4094/3380 3898/3657/3022 4672/4395/3628 — 4600 4717/4437/3663 4859/4559/3767 5824/5478/4523 — 5690 5425/5103/4213 4859/4559/3767 5824/5478/4523 — 5600 4717/4437/3663 4859/4559/3767 5824/5478/4523 2 4690 5425/5103/4213 4859/4559/3767 5824/5478/4523 2 4600 5651/5315/4388 5821/5461/4513 6976/6562/5417 — 6 |                            |         |         |         |
| kW Ratings (LD/ND/HD)             | kW Ratings (LD/ND/HD)             |                                               |                                               |                                                                                          |                                                                                        |                                     |                                              |                                                                        | 600 2385/2243/1852 2456/23              |                                                                                |                                                         |                                                         |                                                         |                                                         |                                                      |                                                                                                                                                                                                                                                                                                                          | 690 6498/6112/5046 5821/54 |         |         |         |
|                                   |                                   |                                               |                                               |                                                                                          |                                                                                        |                                     |                                              | 690 2206/2075/1713 1976/1854/1532 2368/2227/1839 — 2 2500/2300/1900 35 |                                         |                                                                                |                                                         |                                                         |                                                         |                                                         |                                                      |                                                                                                                                                                                                                                                                                                                          |                            |         |         |         |

(1) Inverse time circuit breaker. For U.S. NEC, minimum size is 125% of rated AC input current. (2) Instantaneous trip circuit breaker. The trip setting should be set to the input current of the NRS and should be sized based on the continuous current of the system. (3) Minimum protection device size is the lowest rated device th at provides protection without nu isance tripping. For U.S. NEC, minimum size is 125% of rated AC input current. (4) Maximum protection device size is the highest rated device that provides protection to the NRS.

## Power Jumper Configuration

PowerFlex 755TM NRS products contain protective AC and DC common mode capacitor circuits. To guard against product damage and operational problems, these devices must be properly configured using the following power jumpers:

- Single-density NRS module power jumpers:
- PE-A jumper, which is connected to J8 on the rear power circuit board
- PE-B jumper, which is connected to J9 on the rear power circuit board
- Dual-density NRS module power jumpers:
- PE-A jumper (J8) on the rear power circuit board
- PE-B jumper (J9) on the rear power circuit board
- PE-A jumper (J8) on the front power circuit board
- PE-B jumper (J9) on the front power circuit board

All PE-A and PE-B jumpers for both the front and rear power circuit boards are located under the front power circuit board that is shown in Figure 93 on page 139 .

Figure 92 - Common Mode Capacitor Circuits

<!-- image -->

DC Common Mode Capacitor

<!-- image -->

See Determine Jumper Settings on page 138 and Set the Jumpers on page 139 .

## Determine Jumper Settings

Use the following tables to determine the correct jumper settings for your system.

## IMPORTANT

The default power jumper settings for an NRS module are to set the PEA and PE-B jumpers to the connected (IN) position.

If necessary, reconfigure these jumpers as determined by the power source type that is available.

<!-- image -->

<!-- image -->

ATTENTION: Risk of equipment damage exists. The NRS power source type must be accurately determined. The power jumpers must be configured for the power source type according to the recommendations in the PowerFlex 755TM Input Product RF Emission Compliance and Installation Requirements table on page 43 .

ATTENTION: Hazard of equipment damage exists if jumpers are not properly disconnected or are set differently between NRS modules. Secure a disconnected jumper in the socket or on the insulated spacer that is provided and verify that all modules are configured identically.

## Table 34 - NRS PE-A and PE-B Connections

| Grounding Scheme                                                                           |                 | PE-A PE-B                                         |
|--------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------|
|                                                                                            |                 | AC Common Mode Capacitor DC Common Mode Capacitor |
| Factory Default                                                                            | Connected (In)  | Connected (In)                                    |
| Grounded                                                                                   | Connected (In)  | Connected (In)                                    |
| Ungrounded/High-resistance Ground  (1) AC fed ungrounded Impedance grounded B phase ground | Insulated (Out) | Insulated (Out)                                   |

## Set the Jumpers

Set the PE-A and PE-B power jumpers so that they match the settings you found in Determine Jumper Settings on page 138 as follows:

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. To access the power jumpers, remove the eight M5 x 10 mm Torx screws that secure the panel to the front of the module and remove the panel. This reveals the PE-A and PE-B power jumpers, which are connected to the power circuit board (Figure 93).
5. Connect (set to IN position) or disconnect (set to OUT position) the power jumpers to match your required settings. A dual density NRS module has two PE-A jumpers and two PE-B jumpers. A single density NRS module has one PE-A jumper and one PE-B jumper.

Figure 93 - NRS Power Jumper Configurations

<!-- image -->

## Main Control Circuit Board Configuration

This section provides instructions on how to configure precharge, user enable input, and AC line settings using the main control circuit board switches S1 and S2. You must set S1 and S2 switch settings to match on all parallel NRS modules.

1. Review the Product Advisories on page 15 .
2. Remove power from the system and verify zero energy. See Remove Power from the System on page 16 .
3. To release the tabs on the protective cover from the slots in the chassis, lift vertically and pull the cover off the module. This reveals the S1 and S2 switches on the main control circuit board.

Figure 94 - Accessing the Main Control Circuit Board

<!-- image -->

Figure 95 - S1 (CONFIG) and S2 (PRECHARGE) on Main Control Circuit Board

<!-- image -->

4. On the S1 CONFIG dual inline package of switches, configure the user enable input using switch 1. If there are multiple NRS modules in the system, all S1 switch settings must match. Choose from the following options:
5. On the S1 CONFIG dual inline package of switches, configure the AC line phase setting by using switch 2. If there are multiple NRS modules in the system, all S1 switch settings must match. Choose from the following options:
6. Select the precharge setting for your system as follows.
- a. Find the per-single-density-module precharge bus capacitance as follows: Sum the total bus capacitance of all loads that are connected to the NRS outputs (CBIs, drives, or other outputs) and any optional internal bus capacitance in the NRS modules. Divide that total by the number of single-density-units; For the purposes of this calculation, a single-density module = 1 single-density-unit and a dual-density module = 2 single-density-units. So for a system with two dual-density modules and one single-density module, the number of single-densityunits is 5.
- b. If your product includes any dual-density modules, find the per-dualdensity-module precharge bus capacitance by multiplying the persingle-density-module precharge bus capacitance by 2.
- c. If your product includes a single-density module, find the shortest sweep time in the following table that supports a capacitance greater than or equal to the per-single-density-module precharge bus capacitance.

| Switch Position(1)   | Setting                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Open                 | Activates user enable input. The system commences precharge when the user enable input is provided. This functionality allows you to start up the PowerFlex 755TM NRS product by using the user enable input connections on the P11 terminal block. This functionality also allows you to disable the NRS and bring it into a low-power state. For information on these connections, see Customer Input and Output Connections to Main Control Circuit Board on page 19 . |
| Closed               | Deactivates user enable input. This option provides autonomous operation, in which the system commences precharge immediately after power-up.                                                                                                                                                                                                                                                                                                                             |

Figure 96 - S1 CONFIG Dual Inline Package of Switches Example

<!-- image -->

| Switch Position(1)   | Setting                                                                               |
|----------------------|---------------------------------------------------------------------------------------|
|                      | Open Three-phase AC line                                                              |
|                      | Closed Single-phase AC line. Single-phase mode disables phase loss alarms and faults. |

- d. If your product includes any dual-density modules, find the shortest sweep time in the following table that supports a capacitance greater than or equal to the per-dual-density-module precharge bus capacitance.
- e. Find the longest time out of the time or times that were found in step c and step d. This is the minimum sweep time you can use for the precharge setting of all NRS modules in your system, both single and dual-density.
- f. Consider that some situations may benefit from choosing a longer sweep time than the minimums found in step e. Such situations include those in which you want to limit the start-up current from the power lines that provide power into the NRS. Examples include the following:
- Initial product commissioning at an alternate location with reduced circuit breaker ratings.
- Systems with large capacitances to support brief impulse loads.
- Dual output NRS systems where local motoring regeneration energy exceeds energy that is consumed from the DC output power lines.
- g. On all NRS modules in your system, turn the S2 precharge rotary switch (Figure 95) to one of the following positions:
- The position for the time found in step e
- The position for a longer time than that found in step e
- The position to bypass the between-startup-and-operation precharge (can only be used if the user system provides an external means of controlling pre-charge).

| Maximum Capacitance with 0.2 s sweep (uF)   | Maximum Capacitance with 1.3 s sweep (uF)   | Maximum Capacitance with 2 s sweep (uF)   | Maximum Capacitance with 5 s sweep (uF)   | Maximum Capacitance with 10 s sweep (uF)   | NRS Module Maximum Capacitance with 20 s sweep (uF)                                   | Maximum Capacitance with 30 s sweep (uF)                                                   | Maximum Capacitance with 60 s sweep (uF)                                               |
|---------------------------------------------|---------------------------------------------|-------------------------------------------|-------------------------------------------|--------------------------------------------|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
|                                             |                                             |                                           |                                           |                                            |                                                                                       |                                                                                            | 400/480V 1X 81,700 408,500 817,000 2,042,500 4,085,000 8,170,000 12,255,000 24,510,000 |
|                                             |                                             |                                           |                                           |                                            |                                                                                       | 400/480V 2X 150,700 753,500 1,507,000 3,767,500 7,535,000 15,070,000 22,605,000 45,210,000 |                                                                                        |
|                                             |                                             |                                           |                                           |                                            |                                                                                       |                                                                                            | 600/690V 1X 27,800 139,000 278,000 695,000 1,390,000 2,780,000 4,170,000 8,340,000     |
|                                             |                                             |                                           |                                           |                                            | 600/690V 2X 50,700 253,500 507,000 1,267,500 2,535,000 5,070,000 7,605,000 15,210,000 |                                                                                            |                                                                                        |

Make sure that the setting is the same on all NRS modules in the system. See the following table.

| Switch Position Action (sweep times in seconds)   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0  Bypass precharge                               | The NRS product does not perform a silicon-controlled rectifier (SCR) phase angle sweep before operation. This option allows for immediate full-power operation when starting to run, but requires the user system to provide a separate precharge before startup. If this option is used, make sure the user-system-provided precharge supports the capacitance that was found in step a for a single-density NRS module, and the capacitance that was found in step b for any dual-density NRS modules. |
| 1 0.2 s sweep                                     | Before operation, the system performs an SCR phase angle sweep lasting the specified amount of time. This is the precharge time.                                                                                                                                                                                                                                                                                                                                                                          |
| 2 (1) 1.3 s sweep                                                   | Before operation, the system performs an SCR phase angle sweep lasting the specified amount of time. This is the precharge time.                                                                                                                                                                                                                                                                                                                                                                          |
| 3 2 s sweep                                       | Before operation, the system performs an SCR phase angle sweep lasting the specified amount of time. This is the precharge time.                                                                                                                                                                                                                                                                                                                                                                          |
| 4 5 s sweep                                       | Before operation, the system performs an SCR phase angle sweep lasting the specified amount of time. This is the precharge time.                                                                                                                                                                                                                                                                                                                                                                          |
| 5 10 s sweep                                      | Before operation, the system performs an SCR phase angle sweep lasting the specified amount of time. This is the precharge time.                                                                                                                                                                                                                                                                                                                                                                          |
| 6 20 s sweep                                      | Before operation, the system performs an SCR phase angle sweep lasting the specified amount of time. This is the precharge time.                                                                                                                                                                                                                                                                                                                                                                          |
| 7 30 s sweep                                      | Before operation, the system performs an SCR phase angle sweep lasting the specified amount of time. This is the precharge time.                                                                                                                                                                                                                                                                                                                                                                          |
| 8 60 s sweep                                      | Before operation, the system performs an SCR phase angle sweep lasting the specified amount of time. This is the precharge time.                                                                                                                                                                                                                                                                                                                                                                          |
| 9 Not allowed —                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## System Schematics

This section includes schematics of power bays and NRS modules.

Figure 97 - 1X NRS Module Power Bay Schematic

<!-- image -->

Note 2: If the optional control transformer - 3KVA is used, it must be in the exact polarity as shown.

Note 3: 1X is a single NRS module with one power board. 2X is a single NRS module with two power boards. See Figure 99 on page 145 and Figure 100 on page 146 for more information.

Note 4: The wire bay fan harness is only required in a power bay that is next to a wire entry bay.

Note 5: Connects to P12 when NRS module is removed.

Note 6: Each of the six connections listed above Note 6 is required only if equipment connected to the control bus downstream from the NRS requires the connection. See Customer Provided Control Bus Power on page 133 .

Figure 98 - 2X NRS Module Power Bay Schematic

<!-- image -->

Note 1: See System Communication Interconnection Harnesses on page 96 for more information.

Note 2: If the optional control transformer - 3KVA is used, it must be in the exact polarity as shown.

Note 3: 1X is a single NRS module with one power board. 2X is a single NRS module with two power boards. See Figure 99 on page 145 and Figure 100 on page 146 for more information.

Note 4: The wire bay fan harness is only required in a power bay that is next to a wire entry bay.

Note 5: Connects to P12 when NRS module is removed.

Note 6: Each of the six connections listed above Note 6 is required only if equipment connected to the control bus downstream from the NRS requires the connection. See Customer Provided Control Bus Power on page 133 .

Figure 99 - 1X NRS Module Schematic

<!-- image -->

Figure 100 - 2X NRS Module Schematic

<!-- image -->

Note 1: For a 2X NRS module configuration, if the optional laminated bus capacitor assemblies are used, both must be present. A single laminated bus capacitor assembly cannot be used without the other.

## View Status Indicators on the Main Control Circuit Board

## Troubleshooting

This section provides information about status indicators, faults, and alarms that can be used to troubleshoot the PowerFlex® 755TM Non-Regenerative Supply.

On each NRS module main control circuit board, there are Input and Output Status Indicators, an NRS Module Status Indicator, and a Main Control Circuit Board Seven-segment LED Display. View indicators as follows:

1. Make sure that the system is powered.
2. View the status indicators on the main control board through the window in the power bay door. This window enables you to check indicator statuses without encroaching arc flash boundaries. Do not open the power bay door or remove the main-control-circuit-board touch guard to view status indicators. If you cannot see the status indicators clearly because the door window or touch guard is dirty, clean them. Before cleaning or performing other maintenance, see Chapter 7 on page 165 .

Figure 101 - Status Indicator Viewing Window in the Power Bay Door

Figure 102 - Main Control Circuit Board and Translucent Touch Guard (1)

<!-- image -->

<!-- image -->

- (1) The touch guard is shown removed to show the main control circuit board location. Do not remove the touch guard to view the status indicators.

<!-- image -->

## Main Control Circuit Board Seven-segment LED Display

On the main control circuit board, there is a seven-segment LED control module display that includes two seven-segment digits, and two decimal points.

Figure 103 - Seven-segment LED Display

<!-- image -->

## Power-up Displays

When the NRS gets powered up, the display shows a pattern to verify that each LED segment can be illuminated. Once the pattern completes, the display shows the field programmable gate array (FPGA) revision number. The revision number may flash on the display one or multiple times.

## System Status Displays

Once the power-up displays are complete, the display provides information about the status of the system. Status may include faults, alarms, or normal operation.

All faults and alarms are latched for display until you send the "clear faults" input signal. Once the "clear faults" signal is received, all faults and alarms for which the fault or alarm condition is no longer present are cleared. The faults and alarms for any conditions that are still present remain latched and continue to be displayed. Faults and alarms are also cleared when power is lost.

## Fault Display

If any faults are latched for display, the display begins the following operations:

1. The display shows "FL" to indicate that it is going to show the fault list.
2. The display shows each fault that is latched, one at a time.
- If the fault condition is still present, the fault number blinks a few times and then shows without blinking for a short time.
- If the fault condition is no longer present, the fault number shows without blinking.
3. Once all faults have been displayed, the display does one of the following:
- If any alarms are latched for display, the display begins the operations that are described in Alarm Display .
- If no alarms are latched for display, the display repeats displaying faults.

## Alarm Display

If any alarms are latched for display, the display begins the following operations:

1. The display shows "AL" to indicate that it is going to show the alarm list.
2. The display shows each fault that is latched, one at a time.
- If the alarm condition is still present, the alarm number blinks a few times and then shows without blinking for a short time.
- If the alarm condition is no longer present, the alarm number shows without blinking.
3. Once all alarms have been displayed, the display does one of the following:
- If any faults are latched for display, the display begins the operations that are described in Fault Display .
- If no faults are latched for display, the display repeats displaying alarms.

## Normal Operation Display

If no faults or alarms are latched for display, the display indicates normal operation with a "heartbeat" pattern. In this pattern, the digit 1 decimal point illuminates, and then the digit 2 decimal point illuminates. This pattern repeats until a fault or alarm is detected.

## Faults

Faults de-assert the Not Fault Out user output relay. When a fault is detected in an NRS module, it stops current gating and prevents further gating of the front and rear SCRs of that module. Faults are divided into the following categories:

- A local NRS module fault only disables gating of the affected module.
- A system hard fault disables gating of the affected module and sends a system hard fault output to the bay harness J12 to stop gating of all parallel NRS modules.

Gating can resume once the condition that caused the fault is no longer present and the fault is cleared.

Fault codes are latched to the seven-segment display queue when detected.

## System Hard Faults

Agency certification requires that the following conditions cause a system hard fault, causing all parallel NRS modules of the system to stop:

- Bus capacitor bank imbalance
- AC fuse open
- DC fuse open
- Input wiring bay busbar overtemp
- Failure of monitoring system for the faults listed in this list. Failure of the monitoring system may be caused by the following:
- Bad contact or unplugged connection in interconnect harnesses
- Loss of control power in NRS module
- Non-operational NRS module main control board

The following conditions also cause a system hard fault:

- Mismatched configuration switch settings of parallel NRS modules
- Mismatched voltage ratings of parallel NRS modules
- SYNC harness interconnection failure
- PLL loss during precharge

## Fault Wiring and Function

A hard-wired system cabinet fault scheme is used for fault control of parallel NRS modules. For a simplified view of fault wiring, see Fault and SYNC Signal Diagrams on page 159. This system has the following features:

- Daisy chain interconnection is used to connect NRS modules. Busbar overtemperature switches in input wiring bays are placed in series with the daisy chain.
- For fail-safe behavior, the fault interconnection wiring is defined as energized = not faulted. An open connection results in a faulted state.
- System hard faults trigger the hard fault output of an NRS module, which goes to the cabinet fault input of the next NRS module in the chain. See Fault List on page 152 .
- A cabinet fault input into an NRS module cascades into the module's hard fault output. This cascade causes any hard fault source to automatically propagate through the daisy-chain of all NRS modules in the system. Once the hard fault has propagated through the chain, the following are true:
- All NRS modules display a cabinet fault.
- The NRS module that was the original source of the hard fault may also display the corresponding hard fault code.
- If none of the NRS modules display anything but a cabinet fault, then the source of the fault is either an open wiring bay busbar overtemp switch, an unplugged harness connection, or a faulty connection contact.
- The cabinet fault lines are also used for low-speed serial communication at initial powerup to verify that the configuration switch settings of parallel NRS modules match.

Clearable and Non-clearable Faults

Faults are also divided into the following categories:

- Clearable: These faults can be cleared using the clear fault input.
- Non-clearable: These faults cannot be cleared using the clear fault input. They can only be removed from the seven-segment display queue by powering down the system and correcting the condition that causes the fault.

Table 35 - Fault List

| Fault Code                                                |                                                                                                                                                                                                                                                                | Fault Name Fault Type Fault Description Recommended Actions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 Fan 2 Under Speed (Rear) Local NRS module fault         | The rear fan has been below minimum speed for 60 s. This fault is only enabled when the NRS module is enabled.                                                                                                                                                 | • Make sure that there is no open connection on the harness that connects the fan assembly (J21) to the main control board (J1). See page 192 and page 18 . • The fan assembly may need replacement. See page 190 .                                                                                                                                                                                                                                                                                                                                        |
| 1 Fan 1 Under Speed (Front) Local NRS module fault        | The front fan (only present on dual density NRS modules) has been below minimum speed for 60 s. This fault is only enabled when the NRS module is enabled.                                                                                                     | • Make sure that the front fan is present. That is, make sure that a dual density fan assembly is installed, and a single density fan assembly (which includes only a rear fan) was not installed in this dual density NRS module by mistake. • Make sure that there is no open connection on the harness that connects the fan assembly (J21) to the main control board (J1). • Make sure that the right side 1606 power supply at the bottom of the NRS module has all connections made and is supplying power. • The fan assembly may need replacement. |
| 2 Incompatible Fan Assembly Local NRS module fault        | A dual density fan assembly (with two fans) has been installed in a single density NRS module. This fault only enabled in single density NRS modules.                                                                                                          | Replace the dual density fan assembly with a single density fan assembly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 3 Line R-S Over Voltage Local NRS module fault            | Line R-S exceeded maximum voltage fault threshold: • 480V rated modules: 550V rms for 3.5 s. • 690V rated modules: 795V rms for 3.5 s. This fault is only enabled when the line configuration switch (S1 switch 2) is in the three-phase position (up / open). | Determine the cause of the high line voltage and reduce the voltage to a level below the maximum voltage fault threshold. It is suggested to keep the AC input voltage within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC                                                                                                                                                                                                                 |
| 4 Line S-T Over Voltage Local NRS module fault            | Line S-T exceeded maximum voltage fault threshold: • 480V rated modules: 550V rms for 3.5 s. • 690V rated modules: 795V rms for 3.5 s. This fault is only enabled when the line configuration switch (S1 switch 2) is in the three-phase position (up / open). | Determine the cause of the high line voltage and reduce the voltage to a level below the maximum voltage fault threshold. It is suggested to keep the AC input voltage within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC                                                                                                                                                                                                                 |
| 5 Line T-R Over Voltage Local NRS module fault            | Line T-R exceeded maximum voltage fault threshold: • 480V rated modules: 550V rms for 3.5 s. • 690V rated modules: 795V rms for 3.5 s. This fault is always enabled regardless of switch settings.                                                             | Determine the cause of the high line voltage and reduce the voltage to a level below the maximum voltage fault threshold. It is suggested to keep the AC input voltage within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC                                                                                                                                                                                                                 |
| 6 Line R-S Under Voltage Local NRS module fault           | Line R-S was below minimum voltage threshold: • 480V rated modules: 234V rms for 3.5 s. • 690V rated modules: 351V rms for 3.5 s. This fault is only enabled when line configuration switch (S1 switch 2) is in the three-phase position (up / open).          | Determine the cause of the low line voltage and increase the voltage to a level above the minimum voltage threshold. It is suggested to keep the AC input voltage within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC                                                                                                                                                                                                                      |
| 7 Line S-T Under Voltage Local NRS module fault           | Line S-T was below minimum voltage threshold: • 480V rated modules: 234V rms for 3.5 s. • 690V rated modules: 351V rms for 3.5 s. This fault is only enabled when line configuration switch (S1 switch 2) is in the three-phase position (up / open).          | Determine the cause of the low line voltage and increase the voltage to a level above the minimum voltage threshold. It is suggested to keep the AC input voltage within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC                                                                                                                                                                                                                      |
| 8 Line T-R Under Voltage Local NRS module fault           | Line T-R was below minimum voltage threshold: • 480V rated modules: 234V rms for 3.5 s. • 690V rated modules: 351V rms for 3.5 s. This fault is always enabled regardless of switch settings.                                                                  | Determine the cause of the low line voltage and increase the voltage to a level above the minimum voltage threshold. It is suggested to keep the AC input voltage within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC                                                                                                                                                                                                                      |
| 9  Rear Bus Capacitor Bank Imbalance  System Hard Fault   | Excessive voltage imbalance of rear capacitor bank. This fault is only enabled in NRS modules with capacitor banks.                                                                                                                                            | Replace one or more of the rear bus capacitors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 10  Front Bus Capacitor Bank Imbalance  System Hard Fault | Excessive voltage imbalance of front capacitor bank. This fault is only enabled in dual density NRS modules with capacitor banks.                                                                                                                              | Replace one or more of the front bus capacitors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 11 240VAC Over Voltage Local NRS module fault             | 240V from the 1 kVA control transformer exceeded maximum voltage threshold of 276V for 3.5 s.                                                                                                                                                                  | • Make sure that transformer and tap connections of 1 kVA control transformer are made correctly. • Determine the cause of the high incoming line voltage to the transformer and reduce the voltage to a level below the maximum voltage threshold.                                                                                                                                                                                                                                                                                                        |
| 12 240VAC Under Voltage Local NRS module fault            | 240V from the 1 kVA control transformer was below minimum voltage threshold of 85V for 3.5 s.                                                                                                                                                                  | • Make sure that transformer and tap connections of 1 kVA control transformer are made correctly. • Determine the cause of the low incoming line voltage to the transformer and increase the voltage to a level above the minimum voltage threshold.                                                                                                                                                                                                                                                                                                       |
| 13 Rear Heatsink Bank Over Temp Local NRS module fault    | Rear heatsink maximum temperature limit exceeded. This may be because the NRS module output current was exceeded, the max ambient temperature limit was exceeded, or both.                                                                                     | • Reduce the load on the NRS module output. • Reduce the ambient temperature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Fault List

In the fault type column in the following table, non-clearable faults are labeled as non-clearable. All other faults are clearable.

Table 35 - Fault List (Continued)

| Fault Code   |                                                        |                                        |                                                                                                                                                                                                                                     | Fault Name Fault Type Fault Description Recommended Actions                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------|--------------------------------------------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 14           | Rear Heatsink Bank Under Temp                          |                                        | Local NRS module fault Rear heatsink temperature is at or below -30 °C (-22 °F).                                                                                                                                                    | • Increase the environmental ambient temperature. • Make sure that there is no open connection between the heatsink sensor and the rear power board (J6). • Make sure that there is no open connection on the ribbon cable that connects the rear power board (J1) to the main control board (J3).                                                                                                                                                                                                 |
| 15           | Front Heatsink Bank Over Temp                          | Local NRS module fault                 | Front heatsink maximum temperature limit exceeded. This may be because the NRS module output current was exceeded, the max ambient temperature limit was exceeded, or both. This fault is only enabled in dual density NRS modules. | • Reduce the load on the NRS module output. • Reduce the ambient temperature.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 16           | Front Heatsink Bank Under Temp                         | Local NRS module fault                 | Front heatsink temperature is at or below -30 °C (-22 °F). This fault is only enabled in dual density NRS modules.                                                                                                                  | • Increase the environmental ambient temperature. • Make sure that there is no open connection between the heatsink sensor and the rear power board (J6). • Make sure that there is no open connection on the ribbon cable that connects the front power board (J1) to the main control board (J4).                                                                                                                                                                                                |
|              | 17 Ambient Intake Air Over Temp Local NRS module fault |                                        | Intake air at fan assembly of NRS module is at or above °° 80 °C (176 °F).                                                                                                                                                                                                                                     | Decrease environmental ambient temperature.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 18           | Ambient Intake Air Sensor Failure                      | Local NRS module fault                 | Intake air at fan assembly of NRS module is reading below °° -30 °C (-22 °F).                                                                                                                                                                                                                                     | • Make sure that there is no open connection on the harness that connects the fan assembly (J21) to the main control board (J1). • Increase environmental ambient temperature.                                                                                                                                                                                                                                                                                                                     |
|              |                                                        |                                        | 19 Rear Line Reactor Over Temp Local NRS module fault Rear line reactor temperature limit exceeded.                                                                                                                                 | • Reduce the load current. • Reduce the ambient temperature. • Make sure that there is no open connection on the harness that connects the thermal switches on the rear line reactor to the main control board (J7).                                                                                                                                                                                                                                                                               |
|              | 20 Front Line Reactor Over Temp Local NRS module fault |                                        | Front line reactor temperature limit exceeded. This fault is only enabled in dual density NRS modules.                                                                                                                              | • Reduce the load current. • Reduce the ambient temperature. • Make sure that there is no open connection on the harness that connects the thermal switches on front line reactor to the main control board (J9).                                                                                                                                                                                                                                                                                  |
|              |                                                        |                                        | 21 AC fuse open System Hard Fault One or more open AC input fuses in NRS module.                                                                                                                                                    | • Replace one or more fuses. • Make sure that there is no open connection on the harness that connects the AC fuse indicator switches to the main control board (J1).                                                                                                                                                                                                                                                                                                                              |
|              |                                                        |                                        | 22 DC Fuse Open System Hard Fault One or more open DC output fuses of NRS module.                                                                                                                                                   | • Replace one or more fuses. • Make sure that there is no open connection on the harness that connects the DC fuse indicator switches to the main control board (J2).                                                                                                                                                                                                                                                                                                                              |
|              | 23 Rear Power Board Fault Local NRS module fault       |                                        | Gate drive power supplies on rear power board are not all present.                                                                                                                                                                  | • Replace the NRS module. • Make sure that there is no open connection on the ribbon cable that connects the rear power board (J1) to the main control board (J3).                                                                                                                                                                                                                                                                                                                                 |
|              | 24 Front Power Board Fault Local NRS module fault      |                                        | Gate drive power supplies on front power board are not all present. This fault is only enabled in dual density NRS modules.                                                                                                         | • Replace the NRS module. • Make sure that there is no open connection on the ribbon cable that connects the front power board (J1) to the main control board (J4).                                                                                                                                                                                                                                                                                                                                |
| 25           | Rear Power Board Not Connected                         | Local NRS module fault - Non-clearable | Rear power board is not connected to main control board.                                                                                                                                                                            | Make sure that there is no open connection on the ribbon cable that connects the rear power board (J1) to the main control board (J3).                                                                                                                                                                                                                                                                                                                                                             |
| 26           | Front Power Board Not Connected                        | Local NRS module fault - Non-clearable | Front power board is not connected to main control board. This fault is only enabled in dual density NRS modules. This fault can only be detected after the NRS module is enabled.                                                  | Make sure that there is no open connection on the ribbon cable that connects the front power board (J1) to the main control board (J4).                                                                                                                                                                                                                                                                                                                                                            |
| 27           | Invalid Capacitor Configuration - Additional Cap       | Local NRS module fault - Non-clearable | Front bus capacitor bank is detected on single density NRS module.                                                                                                                                                                  | • If this fault is displaying on a single density NRS module, remove the front bus capacitor bank assembly. Single density NRS modules are not allowed to have two bus capacitor banks. • If this fault is displaying on a dual density NRS module, make sure that there is no open connection on the ribbon cable that connects the front power board (J1) to the main control board (J4). An open connection on this cable would cause the NRS module to incorrectly identify as single density. |
| 28           | Invalid Capacitor Configuration - Rear Missing         | Local NRS module fault - Non-clearable | Rear capacitor bank is not present when front cap bank has been detected. This fault is only enabled in dual density NRS modules.                                                                                                   | Dual density NRS modules must either have no bus capacitor banks, or have both front and rear capacitor banks. That is, dual density NRS modules are not allowed to have one capacitor bank without the other. If both capacitor banks are present, make sure that there is no open connection on the harness that connects the rear capacitor bank to the main control board (J6).                                                                                                                |

## Table 35 - Fault List (Continued)

| Fault Code   |                                                              |                                        |                                                                                                                                                                                                                                                                                                                          | Fault Name Fault Type Fault Description Recommended Actions                                                                                                                                                                                                                                                                                                                                                                              |
|--------------|--------------------------------------------------------------|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 29           | Invalid Capacitor Configuration - Front Missing              | Local NRS module fault - Non-clearable | Front capacitor bank is not present when rear capacitor bank has been detected. This fault is only enabled in dual density NRS modules.                                                                                                                                                                                  | Dual density NRS modules must either have no bus capacitor banks, or have both front and rear cap banks. That is, dual density NRS modules are not allowed to have one capacitor bank without the other. If both capacitor banks are present, make sure that there is no open connection on the harness that connects the front capacitor bank to the main control board (J9).                                                           |
|              |                                                              | 30 Cabinet Fault System Hard Fault     | A system hard fault has been detected from an NRS Module or wiring bay overtemperature switch that is upstream in the cabinet harness interconnect system. For information on the path of propagation of fault signals and which NRS module is downstream from another, see Fault and SYNC Signal Diagrams on page 159 . | Correct the fault upstream from the NRS module that is displaying the cabinet fault. For information on determining the cause of the fault upstream, see Fault and SYNC Signal Diagrams on page 159 .                                                                                                                                                                                                                                    |
|              | 31 Rx UART Start Timeout                                     | System Hard Fault - Non-clearable      | Communication issue between NRS modules at powerup.                                                                                                                                                                                                                                                                      | • Make sure that there is no open connection in the cabinet harness interconnect system. • The main control board may need replacement.                                                                                                                                                                                                                                                                                                  |
|              | 32 Rx UART Timeout                                           | System Hard Fault - Non-clearable      | Communication issue between NRS modules at powerup.                                                                                                                                                                                                                                                                      | • Make sure that there is no open connection in the cabinet harness interconnect system. • The main control board may need replacement.                                                                                                                                                                                                                                                                                                  |
|              | 33 Rx UART Parity Error                                      | System Hard Fault - Non-clearable      | Communication issue between NRS modules at powerup.                                                                                                                                                                                                                                                                      | • Make sure that there is no open connection in the cabinet harness interconnect system. • The main control board may need replacement.                                                                                                                                                                                                                                                                                                  |
|              | 34 Rx CRC Error                                              | System Hard Fault - Non-clearable      | Communication issue between NRS modules at powerup.                                                                                                                                                                                                                                                                      | • Make sure that there is no open connection in the cabinet harness interconnect system. • The main control board may need replacement.                                                                                                                                                                                                                                                                                                  |
|              | 35 System NRS module Count                                   | System Hard Fault - Non-clearable      | More than six NRS modules interconnected in system.                                                                                                                                                                                                                                                                      | Make sure that no more than six NRS modules are interconnected in a single system.                                                                                                                                                                                                                                                                                                                                                       |
|              | 36 SYNC Interconnection Failure                              | System Hard Fault - Non-clearable      | SYNC Bus interconnection verification failed at powerup.                                                                                                                                                                                                                                                                 | • Make sure that there is no open connection in the cabinet harness interconnect system. • The main control board may need replacement.                                                                                                                                                                                                                                                                                                  |
|              | 37 Invalid Precharge Selection                               | System Hard Fault - Non-clearable      | Precharge configuration switch (S2) set to position 9. Position 9 is not allowed.                                                                                                                                                                                                                                        | Set the precharge configuration switch (S2) to a position other than 9 that is appropriate for your application.                                                                                                                                                                                                                                                                                                                         |
| 38           | Precharge Selection Switch Error                             | System Hard Fault - Non-clearable      | Invalid code read from precharge configuration switch (S2).                                                                                                                                                                                                                                                              | • Rotate the precharge configuration switch and set the switch to a position that is appropriate for your application. • The main control board may need replacement.                                                                                                                                                                                                                                                                    |
| P0           | Parallel Configuration Mismatch - Precharge Switch           | System Hard Fault - Non-clearable      | Precharge configuration switch (S2) settings do not match on parallel NRS modules.                                                                                                                                                                                                                                       | Make sure that all NRS modules in the same paralleled system have matching precharge configuration switch settings.                                                                                                                                                                                                                                                                                                                      |
| P1           | Parallel Configuration Mismatch - Interface Config Switch    | System Hard Fault - Non-clearable      | Interface configuration switch (S1) settings do not match on parallel NRS modules.                                                                                                                                                                                                                                       | Make sure that all NRS modules in the same paralleled system have matching interface configuration switch settings.                                                                                                                                                                                                                                                                                                                      |
| P2           | Parallel Configuration Mismatch - 480V / 690V Control Boards | System Hard Fault - Non-clearable      | 480V and 690V NRS modules are intermixed within a paralleled system.                                                                                                                                                                                                                                                     | • Make sure that all NRS modules in the same paralleled system have matching voltage ratings, all 480V or all 690V. • Make sure that each NRS module in the system contains the correct version of the main control board based on the voltage rating of NRS module. That is, if the modules are 480V, make sure they all contain 480V main control boards, and if the modules are 690V, make sure they all contain 690V control boards. |
|              |                                                              | P3 Lost PLL Lock System Hard Fault     | Main control board unable to synchronize to incoming AC line.                                                                                                                                                                                                                                                            | • Check quality of incoming AC line voltage. • Make sure that there is no open connection on the harness that connects the AC line input (internal to NRS module) to the main control board (J5).                                                                                                                                                                                                                                        |

Table 36 - Alarm List

| Alarm Code                      |                                                                                                                                                                                                                                              | Alarm Name Alarm Description Recommended Action                                                                                                                                                                                                                                |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 50 Fan 2 Speed Low (Rear)       | Rear fan running slower than normal for 60 s. This alarm is only enabled when the NRS module is enabled.                                                                                                                                     | • Make sure that the fan airflow is not obstructed. • The fan assembly may need replacement.                                                                                                                                                                                   |
| 51 Fan 1 Speed Low (Front)      | Front fan running slower than normal for 60 s. This alarm is only enabled when the NRS module is enabled and is only enabled on dual density NRS modules.                                                                                    | • Make sure that the fan airflow is not obstructed. • The fan assembly may need replacement.                                                                                                                                                                                   |
| 53 Line R-S High Voltage        | Line R-S exceeded normal operating range: • 480V rated modules: 528V rms • 690V rated modules: 759V rms This alarm is only active when the line configuration switch (S1 switch 2) is in the three-phase position (up / open).               | If the condition persists, determine the cause of the high line voltage and reduce the voltage to a level within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC  |
| 54 Line S-T High Voltage        | Line S-T exceeded normal operating range: • 480V rated modules: 528V rms • 690V rated modules: 759V rms This alarm is only active when the line configuration switch (S1 switch 2) is in the three-phase position (up / open).               | If the condition persists, determine the cause of the high line voltage and reduce the voltage to a level within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC  |
| 55 Line T-R High Voltage        | Line T-R exceeded normal operating range: • 480V rated modules: 528V rms • 690V rated modules: 759V rms                                                                                                                                      | If the condition persists, determine the cause of the high line voltage and reduce the voltage to a level within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC  |
| 56 Line R-S Low Voltage         | Line R-S was below the minimum voltage alarm threshold: • 480V rated modules: 260V rms • 690V rated modules: 390V rms This alarm is only active when the line configuration switch (S1 switch 2) is in the three-phase position (up / open). | If the condition persists, determine the cause of the low line voltage and increase the voltage to a level within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC |
| 57 Line S-T Low Voltage         | Line S-T was below the minimum voltage alarm threshold: • 480V rated modules: 260V rms • 690V rated modules: 390V rms This alarm is only active when the line configuration switch (S1 switch 2) is in the three-phase position (up / open). | If the condition persists, determine the cause of the low line voltage and increase the voltage to a level within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC |
| 58 Line T-R Low Voltage         | Line T-R was below the minimum voltage alarm threshold: • 480V rated modules: 260V rms • 690V rated modules: 390V rms                                                                                                                        | If the condition persists, determine the cause of the low line voltage and increase the voltage to a level within the normal operating AC input voltage range: • 480V rated module normal operating range: 342…528V AC • 690V rated module normal operating range: 540…759V AC |
| 61 240VAC Line High Voltage     | 240V from 1 kVA control transformer exceeded normal operating range (271V).                                                                                                                                                                  | • Make sure that the transformer or tap connections of the 1 kVA control transformer are correct. • Make sure that the incoming line voltage to the transformer is within the normal operating range, below 271V.                                                              |
| 62 240VAC Line Low Voltage      | 240V from 1 kVA control transformer was below normal operating range (94V).                                                                                                                                                                  | • Make sure that the transformer or tap connections of the 1 kVA control transformer are correct. • Make sure that the incoming line voltage to the transformer is within the normal operating range, above 94V.                                                               |
|                                 | 63 Rear Heatsink Bank High Temp Rear heatsink above normal operating temperature.                                                                                                                                                            | If the condition persists, reduce load or ambient temperature.                                                                                                                                                                                                                 |
|                                 | 64 Rear Heatsink Bank Low Temp Rear heatsink temperature is at or below -25 °C (-13 °F).                                                                                                                                                     | If the condition persists, increase environmental ambient temperature.                                                                                                                                                                                                         |
|                                 | 65 Front Heatsink Bank High Temp Front heatsink above normal operating temperature.                                                                                                                                                          | If the condition persists, reduce load or ambient temperature.                                                                                                                                                                                                                 |
| 66 Front Heatsink Bank Low Temp | Front heatsink temperature is at or below -25 °C (-13 °F). This alarm is only enabled in dual density NRS modules.                                                                                                                           | If the condition persists, increase environmental ambient temperature.                                                                                                                                                                                                         |
|                                 | 67 Ambient Intake Air High Temp Intake air at fan assembly of NRS module is at or above 75 °C (167 °F). Decrease environmental ambient temperature.                                                                                          |                                                                                                                                                                                                                                                                                |
|                                 | 68 Ambient Intake Air Low Temp Intake air at fan assembly of NRS module is at or below -25 °C (-13 °F). Increase environmental ambient temperature.                                                                                          |                                                                                                                                                                                                                                                                                |
| 89  Bus Conditioner Fault(1)    | Bus conditioner that is monitored by NRS module has a blown fuse or overtemperature fault. This alarm is only enabled if the bus conditioner is connected to the main control board (J13).                                                   | • Make sure that bus conditioner fuses are intact. • If the condition persists, reduce load or ambient temperature. • Make sure that there is no open connection on the harness that connects the bus conditioner to the main control board (J13).                             |

## Alarms

Alarms are for notification only. They do not stop or prevent gating of the SCRs.

Active alarms de-assert the Not Alarm Out user output relay. The Not Alarm Out relay de-asserts for a minimum of 3 seconds for momentary alarms. If all alarm conditions cease, then all alarms are inactive and the Not Alarm Out relay asserts.

Alarm codes are latched to the seven-segment display queue when they are detected.

## Table 36 - Alarm List

| Alarm Code                         |                                                                                                                                                                                                                                                                                                                                                              | Alarm Name Alarm Description Recommended Action                                                                                                                                                                                                                      |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 90 Rear DC Bus High                | Rear DC Bus has exceeded maximum voltage: • 480V rated modules: 812V for 1 ms • 690V rated modules: 1170V for 1 ms The NRS module temporarily suspends SCR gating during this high bus condition and then resumes normal operation when the bus lowers to within its normal range.                                                                           | A downstream load from the NRS, such as a regenerating common bus inverter (CBI) motor drive, is causing excessive voltage on the bus. Configure the CBI to prevent the bus from further exceeding the voltage limit.                                                |
| 91 Rear DC Bus Low                 | Rear DC Bus has gone below its normal operating range: • 480V rated modules: 453V for 100 ms • 690V rated modules: 678V for 100 ms                                                                                                                                                                                                                           | • If the condition is transient, it does not require any action to be taken. • If the condition persists, it will likely trigger other alarms or faults. If this occurs, perform the recommended action to address those alarms or faults.                           |
| 92 Front DC Bus High               | Front DC Bus has exceeded maximum voltage: • 480V rated modules: 812V for 1 ms • 690V rated modules: 1170V for 1 ms The NRS module temporarily suspends SCR gating during this high bus condition and then resumes normal operation when the bus lowers to within its normal range. This alarm is only enabled in dual density NRS modules.                  | A downstream load from the NRS, such as a regenerating common bus inverter (CBI) motor drive, is causing excessive voltage on the bus. Configure the CBI to prevent the bus from further exceeding the voltage limit.                                                |
| 93 Front DC Bus Low                | Rear DC Bus has gone below its normal operating range: • 480V Rated Modules: 453V for 100 ms • 690V Rated Modules: 678V for 100 ms This alarm is only enabled in dual density NRS modules.                                                                                                                                                                   | • If the condition is transient, it does not require any action to be taken. • If the condition persists, it will likely trigger other alarms or faults. If this occurs, perform the recommended action to address those alarms or faults.                           |
| 94 Line Frequency Low              | Incoming line frequency is below normal operating range (40 Hz for 100 ms). This alarm is based on only the T-R phase when the line configuration switch (S1 switch 2) is in the single-phase position (down / closed). This alarm is based on all three phases when the line configuration switch (S1 switch 2) is in the three-phase position (up / open). | If the condition persists, determine the cause of the low line frequency and increase the frequency to greater than 40 Hz, but less than 65 Hz.                                                                                                                      |
| 95 Line Frequency High             | Incoming line frequency is above normal operating range (65 Hz for 100 ms). This alarm is based on only the T-R phase when the line configuration switch (S1 switch 2) is in the single-phase position (down / closed). This alarm is based on all three phases when the line configuration switch (S1 switch 2) is in the three-phase position (up / open). | If the condition persists, determine the cause of the high line frequency and decrease the frequency to less than 65 Hz, but greater than 40 Hz.                                                                                                                     |
| 96 Output Relay Power Supply Loss  | Power supply for fault / alarm / precharge complete relay coils is below tolerance (lost). The relays revert to their default 'normal' position when the coil power supply is lost.                                                                                                                                                                          | If the condition persists, replace the main control board.                                                                                                                                                                                                           |
|                                    | 97 Main Control Board High Temp Air temperature around main control board is at or above 75 °C (167 °F). Decrease environmental ambient temperature.                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                      |
|                                    | 98 Main Control Board Low Temp Air temperature around main control board is at or below -25 °C (-13 °F). Increase environmental ambient temperature.                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                      |
| 99 Phase Imbalance                 | Mismatch of incoming AC line phases (20% for 2 s). This alarm is only enabled when the line configuration switch (S1 switch 2) is in the three-phase position (up / open).                                                                                                                                                                                   | If the condition persists, determine the cause of the phase imbalance and correct the imbalance.                                                                                                                                                                     |
| b0 Rear Precharge Bypass - DC Low  | Rear DC bus has not completed external precharge. SCR gating is held off until the rear DC bus >= 95% of rectified line T-R.                                                                                                                                                                                                                                 | This alarm is for when the precharge configuration switch (S2) is set to 'Precharge Bypass' (position 0). When the precharge configuration                                                                                                                           |
| b1 Front Precharge Bypass - DC Low | Front DC bus has not completed external precharge. SCR gating is held off until the front DC bus >= 95% of rectified line T-R.                                                                                                                                                                                                                               | switch is set to this position, make sure that the user system precharges the DC bus with some method external to the NRS module before enabling the NRS module. This alarm function helps protect the system from improper implementation of an external precharge. |

(1) This alarm is called a fault but functions as an alarm.

NRS Module Status Indicator The status of the NRS module is constantly monitored and is indicated through the main control circuit board STS LED. For more detail about the status descriptions, see Faults on page 150 and Alarms on page 155 .

Figure 104 - STS LED

<!-- image -->

Table 37 - NRS Module Status Indicator States

|                |                      | Color State Description                                                                                                                                                                                                   |
|----------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Green          |                      | Flashing NRS module is ready but not running, and no faults or alarms are present.                                                                                                                                        |
| Green          |                      | Steady NRS module is running, no faults or alarms are present.                                                                                                                                                            |
|                | Yellow Steady        | NRS module is ready but not running, and an alarm has occurred. An alarm does not prevent the module from being started.                                                                                                  |
| Red            | Flashing             | A clearable fault has occurred. The NRS module stops, and it cannot be started until the fault is cleared.                                                                                                                |
| Red            | Steady               | A non-clearable fault has occurred. These faults cannot be cleared using the clear fault user input. To remove these faults, you must power down the system and correct the conditions causing the faults. See page 151 . |
| Yellow / Green | Flashing Alternately | NRS module is running, but an alarm has occurred. An alarm does not prevent the module from continuing to run or starting again after being turned off.                                                                   |

Each input and output on the main control circuit board has its own discrete light-emitting diode (LED) to indicate its status. These LEDs are below the NRS module status indicator (STS LED) on the main control circuit board. In the following descriptions, the LED off state descriptions assume that the NRS module is powered. When the NRS module is not powered, all LEDs are off.

Figure 105 - Input and Output Status Indicators

<!-- image -->

## Input and Output Status Indicators

## Cabinet Fault Indicator (CAB FLT LED):

- Off: No system hard fault is present.
- Steady red: A system hard fault is present. See Faults on page 150 .

## Clear Fault Indicator (CLR FLT LED):

- Off: The Clear Faults input is not asserted.
- Steady yellow: The Clear Faults input is asserted. When asserted, the system clears faults and removes the codes of all inactive faults and alarms from the seven-segment display queue. The system also reruns start-up communications.

## Fault Indicator (FAULT LED):

- Off: No fault is present in the NRS module.
- Steady red: A fault is present in the NRS module. The Not Fault Out relay is de-asserted.

## Alarm Indicator (ALARM LED):

- Off: No active alarm is present in the NRS module.
- Steady yellow: An active alarm is present in the NRS module. The Not Alarm Out relay is de-asserted.

## User Enable Input Indicator (USER EN LED):

- Off: The User Enable input is not asserted. Situations in which the User Enable input is not asserted, can include the following:
- The User Enable input has been configured to be deactivated. If this is true, the system either precharges or runs when power is applied, rather than waiting for a User Enable input. To configure the User Enable input, see Main Control Circuit Board Configuration on page 140 .
- The User Enable input has been configured to be activated but you have not provided the input to start running.
- The User Enable input has been configured to be activated and the input was asserted, and then deasserted. When the input is deasserted, SCR firing stops and cooling fans continue running until the end of a cool-down period.
- Steady green: The User Enable input is asserted. You have provided the input to run and the system is either precharging to run or running.

## Precharge Complete Indicator (PC COMPLETE LED):

- Off: The precharge is not complete and the user system cannot draw full power from the DC bus. The Precharge Complete Out relay is de-asserted.
- Steady green: The precharge is complete and the user system can draw full power from the DC bus. The Precharge Complete Out relay is asserted. This indicator functionality applies whether the precharge was provided by a user system or by the NRS system. To configure the precharge, see Main Control Circuit Board Configuration on page 140 .

## Parallel NRS module Precharge Synchronization

## Fault and SYNC Signal Diagrams

This section provides information about precharge synchronization that can be used to troubleshoot precharge related faults and alarms. The cabinet wiring provides precharge sweep synchronization for parallel NRS modules as follows:

- A SYNC bus signal is connected in a wire-or configuration.
- All NRS modules assert the SYNC bus at powerup.
- Each NRS module de-asserts its control of the SYNC bus when it is ready to start precharge. The module is ready to start precharge when the following conditions are met:
- Main control board initialization is complete.
- No faults are active.
- The user enable input has been asserted by the user system (this is only required if the user enable input configuration switch is set to the 'active' position).
- When the last NRS module de-asserts control of the SYNC bus, all NRS modules start the precharge sweep simultaneously.
- If there is only one NRS module (non-parallel system), it starts as soon as it de-asserts its own SYNC bus signal.

Each NRS system power bay and wire bay has a harness to support the cabinet fault daisy chain and precharge SYNC interconnection between parallel NRS modules. This section includes diagrams of these harnesses. The following harness details have been omitted from these diagrams for visual simplification:

- The cabinet harnesses also provide 240V AC power to the NRS modules.
- Fault and SYNC bus signals are wire pairs.
- The SYNC bus signals going to the left and the right in each cabinet harness are separate wire pairs that are electrically tied together by the main control board, rather than having a 'T' splice in the harness itself. The N-1 bypass jumper also ties these SYNC bus wires together.

The red arrows in the following diagrams indicate the path that fault signals travel.

A 'T' shaped power bay cabinet harness supports multiple system configurations with a common design.

<!-- image -->

End loop-back jumpers are connected on either side of the 'T' harness when there is no adjacent power bay.

<!-- image -->

Harness couplers are used between adjacent power bays.

<!-- image -->

When a wire bay is next to a power bay, an adapter is used to connect the wire bay overtemperature switch to the power bay:

<!-- image -->

For inline and back-to-back configurations, a wiring bay pass-through harness connects the system SYNC and cabinet fault signals, and also provides a connection for busbar overtemperature switches:

<!-- image -->

For N-1 operation, an NRS module bypass jumper inside the power bay is used.

<!-- image -->

## Single NRS Module Without Wiring Bay

A single NRS module without a wiring bay is the most basic configuration possible. The NRS module hard fault output is routed through the harness back into its own cabinet fault input. The NRS module does not run unless these harness loop-backs are in place to complete the cabinet fault loop.

The SYNC bus does not connect the NRS module to anything else in this configuration, so precharge commences as soon as the single NRS module is ready.

<!-- image -->

## Two NRS Modules and a Wiring Bay

The left NRS module hard fault output is routed through the harness into the cabinet fault input of the right NRS module. The right NRS module Hard Fault output loops back to the left side, then passes through a normally closed busbar overtemperature switch, then passes into the cabinet fault input of the left NRS module. If the overtemp switch opens, it interrupts the cabinet fault signal. The cabinet fault input of the left NRS module can be triggered either by the hard fault output of the right NRS module, or by the overtemp switch in the wiring bay.

The SYNC bus of the two NRS modules is wired together in a wire-or configuration, so that precharge commences when both modules are ready.

<!-- image -->

system. The diagram shows the inline version of a six module system, but the signal paths apply to a back-to-back configuration as well. From the leftmost NRS module, each hard fault output is routed through the harness into the cabinet fault input of th e next NRS module to the right. The cabinet fault signal passes through the overtemp switches of the two wiring bays in the center of the system. If an overtemp switch opens, it interrupts the cabinet fault signal. The hard fault output of the rightmost NRS module is looped back into the cabinet fault input of the leftmost NRS module.

## Six NRS Modules with Two Wiring BaysThis configuration is the largest NRS system

A cabinet fault input to an NRS module is one possible source of an NRS module hard fault output. This causes any hard fault source to automatically daisy-chain through all NRS modules of the system. When a hard fault occurs, all NRS modules display a cabinet fault, and the NRS module with the o original hard fault source al so displays the corresponding fault code. If none of the NRS modules display anything but a ca binet fault, then the source of f the fault is either an open wiring bay overtemp switch, unplugged co nnection, or faulty y connection contact.

The SYNC Bus of all six NRS modules are wired together in a wire-or configuration, so that precharge commences when the last module is ready.

Wiring Bay Pass-through

<!-- image -->

## N-1 Operation

The NRS system allows operation at a re duced capacity when one or more of the NRS modules is removed. In this situation, it is necessary to connect a bypass jumper in place of the NRS module to complete the cabinet fault signal chain.

There is a bypass jumper (J27) mounted in each power bay. A Access to this jumper is blocked when an NRS module is present in the power bay, so the jumper can only be used when the NRS module is removed.

Wiring Bay Pass-through

<!-- image -->

## Maintenance of Industrial Control Equipment

## Preventive Maintenance

This chapter provides information about maintaining your PowerFlex® 755TM NRS product to achieve the highest level of uptime.

<!-- image -->

ATTENTION: Performing service on energized Industrial Control Equipment can be hazardous. Severe injury or death can result from electrical shock, bump, or unintended actuation of controlled equipment. Recommended practice is to disconnect and lockout control equipment from power sources, and release stored energy, if present. See National Fire Protection Association Standard No. NFPA 70E Part II, and (as applicable) OSHA rules for Control of Hazardous Energy Sources (lockout/tagout) and OSHA Electrical Safety Related Work Practices for safety-related work practices. These publications include procedural requirements for lockout/tagout, and appropriate work practices, personnel qualifications, and required training where it is not feasible to de-energize and lockout or tagout electric circuits and equipment before working on or near exposed circuit parts. See Product Advisories on page 15 and Remove Power from the System on page 16 .

This section describes general maintenance tasks applicable to various industrial control equipment. Maintenance tasks and schedules for specific NRS components are provided in Maintenance Task Code Explanation on page 168 and Recommended Maintenance Schedules on page 169 .

An annual preventive maintenance program includes the following general tasks:

- A visual inspection of all components that are accessible when a bay door is opened and the touch guards are removed
- Resistance checks on the power components
- Power-supply voltage level checks
- General cleaning
- Tightness checks on all accessible power connections

<!-- image -->

## Periodic Inspection

Periodically inspect industrial control equipment. Base inspection intervals on the environmental and operating conditions and adjust the intervals as necessary. An initial inspection within 3 to 4 months after installation is suggested. See National Electrical Manufacturers Association NEMA) Standard No. ICS 1.3, Preventive Maintenance of Industrial Control and Systems Equipment, for general guidelines for defining a periodic maintenance program. Some specific guidelines for Rockwell Automation products are listed here.

## Contamination

If inspection reveals that dust, dirt, moisture, or other contamination has reached the control equipment, the cause must be removed. Contamination can indicate an incorrectly selected or ineffective enclosure, unsealed enclosure openings (conduit or other), or incorrect operating procedures. Replace any improperly selected enclosure with one that is suitable for the environmental conditions. See the Industry Installation Guidelines for Pulse Width Modulated (PWM) AC Drives, publication DRIVES-AT003, for guidance on environmental considerations. See NEMA Standard No. 250, Enclosures for Electrical Equipment, or UL 50E Electrical Equipment Enclosures, for enclosure type descriptions and test criteria.

Replace any damaged or cracked elastomer seals and repair or replace any other damaged or malfunctioning parts (for example, hinges and fasteners). Dirty, wet, or contaminated control devices must be replaced. Compressed air is not recommended for cleaning because it can displace dirt, dust, or debris into other parts or equipment, or damage delicate parts.

PowerFlex 755T products with XT use dielectric grease to protect critical connections from the effects of corrosive gases. When you disconnect or reconnect a greased connection, always inspect for dust, dirt, conductive debris, or other contaminants. If contamination is found, thoroughly clean receiving surfaces and reapply dielectric grease as described in the PowerFlex 750-Series Products with TotalFORCE Control Hardware Service Manual, publication 750-TG100-EN-P .

## Blowers and Fans

Inspect blowers and fans that are used for forced air cooling. Replace any that have bent, chipped, or missing blades, or if the shaft does not turn freely. Apply power momentarily to check operation. If the unit does not operate, check and replace wiring, fuse, or blower or fan motor as appropriate. Clean or replace air filters as recommended in the Recommended Maintenance Schedules on page 169. See the filter replacement procedures in Chapter on page 171 for information on how to access filters for cleaning or replacement. Also, clean the fins of heat exchangers so convection cooling is not impaired.

## Terminals

Loose connections in power circuits can cause overheating that can lead to equipment malfunction or failure. Loose connections in control circuits can cause control malfunctions. Loose bond or ground connections can increase hazards of electrical shock and contribute to electromagnetic interference (EMI). Check the tightness of all terminals and bus bar connections and torque any loose connections properly. Infrared technology can be used to check for hot (high resistance/loose) connections during periodic maintenance. Replace any parts or wiring that is damaged by overheating, and any broken wires or bond straps.

## Solid-state Devices

<!-- image -->

ATTENTION: Use of other than factory-recommended test equipment for solid-state controls can result in damage to the control or test equipment or unintended actuation of the controlled equipment. See paragraph titled HIGH VOLTAGE TESTING.

Solid-state devices require little more than a periodic visual inspection. Discolored, charred, or burned components can indicate the need to replace the component or circuit board. Make necessary replacements only at the circuit board or plug-in component level. Inspect printed circuit boards to determine whether they are properly seated in the edge board connectors. Board locking tabs must also be in place. Solid-state devices must also be protected from contamination, and temperature control provisions must be maintained. See Contamination on page 166 and Blowers and Fans on page 166. Do not use solvents on printed circuit boards.

High-Voltage Testing

Do not perform high-voltage insulation resistance (IR) and dielectric withstanding voltage (DWV) tests to check solid-state control equipment. When measuring IR or DWV of electrical equipment such as transformers or motors, a solid-state device that is used for control or monitoring must be disconnected before performing the test. Even though no damage is readily apparent after an IR or DWV test, the solid-state devices are degraded and repeated application of high voltage can lead to failure.

## Maintenance After a Fault Condition

An open short circuit protective device (such as a fuse or circuit breaker) in a properly coordinated motor branch circuit is an indication of a fault condition in excess of operating overload. Such conditions can damage control equipment. Before power is restored, the fault condition must be corrected and any necessary repairs or replacements must be made to restore the control equipment to good working order. See NEMA Standards Publication No. ICS2, Part ICS2-302 for procedures. To maintain the integrity of the equipment, use only replacement parts and devices that Rockwell Automation recommends. Make sure that the parts are properly matched to the model, series, and revision level of the equipment.

## Maintenance Task Code Explanation

## Final Check Out

After maintenance or repair of industrial controls, always test the control system for proper function under controlled conditions to avoid a control malfunction hazard. For additional information, see NEMA ICS 1.3, Preventive Maintenance Of Industrial Control And Systems Equipment, published by the National Electrical Manufacturers Association, and NFPA 70B, Electrical Equipment Maintenance, published by the National Fire Protection Association.

## Locking Devices

Check these devices for proper working condition and capability of performing their intended functions. Make any necessary replacements only with Rockwell Automation renewal parts or kits. Adjust or repair only in accordance with Rockwell Automation instructions.

The following codes are used in the Recommended Maintenance Schedules tables on pages 169 and 170 .

|            | Code Task Description                                                                                                                                                                                                                                            |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I Inspect  | Inspect the component for signs of excessive accumulation of dust, dirt, or external damage. For example, inspect the filters/fan inlet screens for debris that can block the airflow path.                                                                      |
| C Clean    | Clean the components that can be reused, specifically the door-mounted air filters and fan inlet screens.                                                                                                                                                        |
| M Maintain | This type of maintenance task can include an inductance test of line reactors/DC links, or a full test of an isolation transformer, and so on.                                                                                                                   |
| R Replace  | This component has reached its mean operational life. Replace the component to decrease the chance of failure. It is likely that components can exceed the designed life in the product, but component life is dependent on many factors such as usage and heat. |
| Rv Review  | A discussion with Rockwell Automation personnel is recommended to help determine whether any of the enhancements/changes made to the product hardware and control could benefit the application.                                                                 |

## Recommended Maintenance Schedules

To help achieve the highest level of uptime, we recommend that you follow the maintenance schedule for the temperature in your operating environment:

- Recommended Maintenance Schedule for Operating Conditions Below 40 °C (104 °F) on page 169 .
- Recommended Maintenance Schedule for Operating Conditions Above 40 °C (104 °F) on page 170 .

## IMPORTANT

In addition to operating environment temperature, duty cycle and load profile can greatly affect reliability of PowerFlex 755TM NRS products. These factors may affect how frequently maintenance is required.

For instructions on component replacement, see Renewal Parts Replacement Instructions on page 171 .

Table 38 - Recommended Maintenance Schedule for Operating Conditions Below 40 °C (104 °F)

| Components                                                                       | Years of Operation   |                                                                                     |                                                                                     |                                                 |                                                      |
|----------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------|------------------------------------------------------|
|                                                                                  |                      |                                                                                     |                                                                                     |                                                 | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 |
| NRS Module Components                                                            |                      |                                                                                     |                                                                                     |                                                 |                                                      |
| 480V Balance Resistors and Bus Capacitors Assembly (cat. no. SK-RM-DCCAP1-CD)(1) |                      |                                                                                     | ———————R—                                                                           | —————R——————                                    |                                                      |
| 690V Balance Resistors and Bus Capacitors Assembly (cat. no. SK-RM-DCCAP1-EF)(1) |                      |                                                                                     | ———————R—                                                                           | —————R——————                                    |                                                      |
| Main control circuit board (400V/480V) (cat. no. SK-RM-MCB3-PF755-CD)            |                      |                                                                                     | ————————————R                                                                       |                                                 | ————————                                             |
| Main control circuit board (600V/690V) (cat. no. SK-RM-MCB3-PF755-EF)            |                      |                                                                                     | ————————————R                                                                       |                                                 | ————————                                             |
| NRS module power supply (cat. no. 1606-XLE480FPC)                                |                      |                                                                                     | —————————R———                                                                       |                                                 | —————R——                                             |
| Heatsink fan assembly for single density NRS module (cat. no. SK-RM-MFAN-NRS)                                                                                  |                      |                                                                                     | —I I I I I IRI I I I I IRI I I I I I                                                |                                                 |                                                      |
| Heatsink fan assembly for dual density NRS module (cat. no. SK-RM-MFAN-F7)                                                                                  |                      |                                                                                     | —I I I I I IRI I I I I IRI I I I I I                                                |                                                 |                                                      |
| Enclosure Components (2)                                                         |                      |                                                                                     |                                                                                     |                                                 |                                                      |
| Door-mounted Ventilation Air Filters                                             |                      | C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R |                                                                                     |                                                 |                                                      |
| Roof-mounted Ventilation Air Filters                                             |                      |                                                                                     | C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R |                                                 |                                                      |
| Wiring Bay Fan (if system includes a wiring bay)                                 |                      |                                                                                     | —I I I I I IRI I I I I IRI I I I I I                                                |                                                 |                                                      |
| Spare Parts                                                                      |                      |                                                                                     |                                                                                     |                                                 |                                                      |
| Inventory/Needs                                                                  |                      |                                                                                     |                                                                                     | — I I Rv I I Rv I I Rv I I Rv I I Rv I I Rv I I |                                                      |

Table 39 - Recommended Maintenance Schedule for Operating Conditions Above 40 °C (104 °F)

| Components                                                                       | Years of Operation   |                                                                                     |                                                 |                                                                                     |                                                      |
|----------------------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------------|-------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------------|
|                                                                                  |                      |                                                                                     |                                                 |                                                                                     | 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 |
| NRS Module Components                                                            |                      |                                                                                     |                                                 |                                                                                     |                                                      |
| 480V Balance Resistors and Bus Capacitors Assembly (cat. no. SK-RM-DCCAP1-CD)(1) |                      |                                                                                     | ———— R ———R———R———R———R                         |                                                                                     |                                                      |
| 690V Balance Resistors and Bus Capacitors Assembly (cat. no. SK-RM-DCCAP1-EF)(1) |                      |                                                                                     | ———— R ———R———R———R———R                         |                                                                                     |                                                      |
| Main control circuit board (400V/480V) (cat. no. SK-RM-MCB3-PF755-CD)            |                      |                                                                                     | ————————R                                       | ———————R————                                                                        |                                                      |
| Main control circuit board (600V/690V) (cat. no. SK-RM-MCB3-PF755-EF)            |                      |                                                                                     | ————————R                                       | ———————R————                                                                        |                                                      |
| NRS module power supply (cat. no. 1606-XLE480FPC)                                |                      |                                                                                     | —————— R—————R                                  |                                                                                     | —————R——                                             |
| Heatsink fan assembly for single density NRS module (cat. no. SK-RM-MFAN-NRS)                                                                                  |                      |                                                                                     | —I I I R I I IRI I IRI I IRI I IR               |                                                                                     |                                                      |
| Heatsink fan assembly for dual density NRS module (cat. no. SK-RM-MFAN-F7)                                                                                  |                      |                                                                                     | —I I I R I I IRI I IRI I IRI I IR               |                                                                                     |                                                      |
| Enclosure Components (2)                                                         |                      |                                                                                     |                                                 |                                                                                     |                                                      |
| Door-mounted Ventilation Air Filters                                             |                      | C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R |                                                 |                                                                                     |                                                      |
| Roof-mounted Ventilation Air Filters                                             |                      |                                                                                     |                                                 | C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R C/R |                                                      |
| Wiring Bay Fan (if system includes a wiring bay)                                 |                      |                                                                                     | —I I I I R I I I IRI I I IRI I I IR             |                                                                                     |                                                      |
| Spare Parts                                                                      |                      |                                                                                     |                                                 |                                                                                     |                                                      |
| Inventory/Needs                                                                  |                      |                                                                                     | — I I Rv I I Rv I I Rv I I Rv I I Rv I I Rv I I |                                                                                     |                                                      |

## Available Renewal Kits

<!-- image -->

## Renewal Parts Replacement Instructions

This chapter provides detailed instructions for how to remove and replace PowerFlex® Non-Regenerative Supply product components. Some components have recommended replacement schedules provided in Recommended Maintenance Schedules on page 169. Components that have no recommended replacement schedule should be replaced only if they fail or an inspection determines they need replacement.

This table lists the renewal kits available for PowerFlex Non-Regenerative Supply (NRS) products.

Table 40 - Available Renewal Kits

| Description                                                                                       | Cat. No.  Quantity    | Replacement Instructions Page Number   |
|---------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------|
| Bay Components Other Than NRS Module Components                                                   |                       |                                        |
| System Communication Interconnect Harness Multiple, see section 1                                 |                       | 174                                    |
| NRS module N-1 jumper                                                                             | SK-RM-JMPR-N1 1       | 175                                    |
| Control transformer T1 (FH1, FH2) primary fuses (400V/480V/600V)                                  | SK-RM-NRSF1F2-CDE 2   | 176                                    |
| Control transformer T1 (FH1, FH2) primary (690V) SK-RM-NRSF1F2-F 2                                |                       | 176                                    |
| Control transformer T1 (FH3) secondary fuse (400V/480V/600V/690V)                                 | SK-RM-NRSF3 1         | 177                                    |
| Control transformer T2 (FH4, FH5) primary fuses (400V/480V/600V)                                  | SK-RM-NRSF4F5-CDE 2   | 178                                    |
| Control transformer T2 (FH4, FH5) primary fuses (690V) SK-RM-NRSF4F5-F 2                          |                       | 178                                    |
| Control transformer T2 (FH6) secondary fuse (400V/480V/600V/690V)                                 | SK-RM-NRSF6 1         | 179                                    |
| IP54/IP21 Power Bay Exhaust Vent Filters                                                          | SK-RM-PBAY-FLTR-NRS 2 | 180                                    |
| IP54, 400 mm (15.75 in.) Wide Power Bay Door Vent Filters SK-RM-PB4DR-54FLTR1 1                   |                       | 181                                    |
| IP21, 400 mm (15.75 in.) Wide Power Bay Door Vent Filter SK-RM-PB4DR-21FLTR1 1                    |                       | 182                                    |
| IP54/IP21, 400/800 mm (15.75/31.5 in.) Wide Wire Bay Door Vent Filters Replacement                | SK-RM-IB4DR-FLTR1 1   | 183                                    |
| IP54/IP21, 400 mm (15.75 in.) Wide Wire Bay Door Vent Exhaust Fan and Filter Assembly Replacement | SK-RM-WBDR-FANFLR1 1  | 184                                    |
| IP54/IP21, 800 mm (31.5 in.) Wide Wire Bay Door Vent Exhaust Fan and Filter Assembly Replacement  | SK-RM-WBDR-FANFLR2 1  | 184                                    |
| Thermal Switch                                                                                    | SK-RM-THRMSW-WB 1     | 185                                    |
| DC Link / Fuse Assembly Components                                                                |                       |                                        |
| DC link fuses (for C770D740 modules)                                                              | SK-RM-DCFUSE1-NRS 2   | 187                                    |
| DC link fuses (for E545F505 modules) SK-RM-DCFUSE2-NRS 2                                          |                       | 187                                    |
| DC link fuses (for C1K4D1K3 modules)                                                              | SK-RM-DCFUSE1-F8 2    | 189                                    |
| DC link fuses (for E980F920 modules) SK-RM-DCFUSE2-F8 2                                           |                       | 189                                    |

Table 40 - Available Renewal Kits (Continued)

| Description                                                          | Cat. No.                            | Quantity   | Replacement Instructions Page Number   |
|----------------------------------------------------------------------|-------------------------------------|------------|----------------------------------------|
| NRS Module Components                                                |                                     |            |                                        |
| Heatsink fan assembly for single-density NRS module SK-RM-MFAN-NRS 1 |                                     |            | 190                                    |
| Heatsink fan assembly for dual-density NRS module SK-RM-MFAN-F7 1    |                                     |            | 190                                    |
| NRS module power supply                                              | 1606-XLE480FPC 1                    |            | 192                                    |
| Main control circuit board (400V/480V)                               | SK-RM-MCB3-PF755-CD 1               |            | 195                                    |
| Main control circuit board (600V/690V)                               | SK-RM-MCB3-PF755-EF 1               |            | 195                                    |
| NRS module                                                           | 20JEHxxxxxxxxxxxxx(1)               | 1          | 198                                    |
| AC fuses (for C770D740 NRS modules) SK-RM-ACFUSE2-F8 3               |                                     |            | 201                                    |
| AC fuses (for E545F505 NRS modules)                                  | SK-RM-ACFUSE4-F9 3                  |            | 201                                    |
| AC fuses (for C1K4D1K3 NRS modules)                                  | SK-RM-ACFUSE1-F8 3                  |            | 201                                    |
| AC fuses (for E980F920 NRS modules) SK-RM-ACFUSE1-NRS 3              |                                     |            | 201                                    |
| Balance resistors and DC bus capacitors assembly (400V/480V)         | SK-RM-DCCAP1-CD(2)                  | 1          | 204                                    |
| Balance resistors and DC bus capacitors assembly (600V/690V)         | SK-RM-DCCAP1-EF(2)                  | 1          | 204                                    |
| P10 plug connector for output to the customer.                       | Phoenix Contact part number 1752865 |            | 1 —                                    |
| P11 plug connector for input from the customer.                      | Phoenix Contact part number 1752687 |            | 1 —                                    |

## Remove the Power Bay Protective Guard

You must remove the protective guard to access components inside the upper part of a power bay.

## Remove the Protective Guard

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Loosen the six M6 x 12 mm slotted-torx screws that secure the guard to the power bay and remove the guard.

<!-- image -->

## Install the Protective Guard

Install the protective guard in the reverse order of removal.

## System Communication Interconnect Harness Replacement

For system communication interconnect harness catalog numbers, see System Communication Interconnection Harnesses on page 96. Use the following procedure to remove and replace a system communication interconnect harness.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Remove the harness that requires replacement. For information about the locations where you must disconnect the harness, see System Communication Interconnection Harnesses on page 96 through page 104 .
4. Install the new harness. Routing and connection points are shown in System Communication Interconnection Harnesses on page 96 through page 104 .

## NRS Module N-1 Jumper Replacement

Replace the NRS module N-1 jumper with kit catalog number SK-RM-JMPR-N1.

## Remove the NRS Module N-1 Jumper

Follow these steps to remove the NRS module N-1 jumper.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the protective guard from the bay. See Remove the Power Bay Protective Guard on page 173 .
5. If necessary, disconnect the NRS module interconnection harness connector P12 from connector J27 on the testpoint plate on the bay side rail.
6. Disconnect the test point wire harnesses from the terminals on the plate.
7. Remove the three M5 x 13 mm torx screws that secure the test point plate to the bay side rail.
8. Press inward on the N-1 terminal block lock tabs and remove the jumper from the plate.

<!-- image -->

## Install the NRS Module N-1 Jumper

Install the NRS module N-1 jumper in the reverse order of removal.

## Control Transformer T1 Primary Fuses (FH1, FH2) Replacement

Replace the control transformer T1 primary fuses (FH1, FH2) with one of the kits listed in this table.

Table 41 - Control Transformer T1: FH1 and FH2 Fuse Kits

| Voltage     | Cat. No.  Rating (V/A)   |   Quantity |
|-------------|--------------------------|------------|
| 400/480/600 | SK-RM-NRSF1F2-CDE 600/6  |          2 |
| 690         | SK-RM-NRSF1F2-F 690/4    |          2 |

## Remove the Control Transformer T1 Primary Fuses (FH1, FH2)

Follow these steps to remove the primary fuses.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the protective guard from the bay. See Remove the Power Bay Protective Guard on page 173 .
5. Pull down on the tabs at the top of the fuse holders FH1 and FH2.
6. Remove the fuses.

<!-- image -->

## Install the Control Transformer T1 Primary Fuses (FH1, FH2)

Install the primary fuses in the reverse order of removal.

## Control Transformer T1 Secondary Fuse (FH3) Replacement

Replace the control transformer T1 secondary fuse (FH3) with the kit listed in this table.

Table 42 - Control Transformer T1: FH3 Fuse Kit

| Voltage                     | Cat. No.   | Rating (V/A)   |   Quantity |
|-----------------------------|------------|----------------|------------|
| 400/480/600/690 SK-RM-NRSF3 |            | 600/6          |          1 |

## Remove the Control Transformer T1 Secondary Fuse (FH3)

Follow these steps to remove the secondary fuse.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the protective guard from the bay. See Remove the Power Bay Protective Guard on page 173 .
5. Pull down on the tabs at the top of the fuse holder FH3.
6. Remove the fuse.

<!-- image -->

## Install the Control Transformer T1 Secondary Fuse (FH3)

Install the secondary fuses in the reverse order of removal.

## Control Transformer T2 Primary Fuses (FH4, FH5) Replacement

Replace the control transformer T2 primary fuses (FH4, FH5) with one of the kits listed in this table.

Table 43 - Control Transformer T2: FH4 and FH5 Fuse Kits

| Voltage     | Cat. No.  Rating (V/A)   |   Quantity |
|-------------|--------------------------|------------|
| 400/480/600 | SK-RM-NRSF4F5-CDE 600/20 |          2 |
| 690         | SK-RM-NRSF4F5-F 690/12   |          2 |

## Remove the Control Transformer T2 Primary Fuses (FH4, FH5)

Follow these steps to remove the primary fuses.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the protective guard from the bay. See Remove the Power Bay Protective Guard on page 173 .
5. Pull down on the tabs at the top of the fuse holders FH4 and FH5.
6. Remove the fuses.

<!-- image -->

## Install the Control Transformer T2 Primary Fuses (FH4, FH5)

Install the primary fuses in the reverse order of removal.

## Control Transformer T2 Secondary Fuse (FH6) Replacement

Replace the control transformer T2 secondary fuse (FH6) with the kit listed in this table.

Table 44 - Control Transformer T2: FH6 Fuse Kit

| Voltage                     | Cat. No.   | Rating (V/A)   |   Quantity |
|-----------------------------|------------|----------------|------------|
| 400/480/600/690 SK-RM-NRSF6 |            | 600/15         |          1 |

## Remove the Control Transformer T2 Secondary Fuse (FH6)

Follow these steps to remove the secondary fuse.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the protective guard from the bay. See Remove the Power Bay Protective Guard on page 173 .
5. Pull down on the tabs at the top of the fuse holder FH6.
6. Remove the fuse.

<!-- image -->

## Install the Control Transformer T2 Secondary Fuse (FH6)

Install the secondary fuses in the reverse order of removal.

## IP54/IP21 Power Bay Exhaust Vent Filters Replacement

Replace the IP54/IP21 power bay exhaust vent filters on a power bay with kit catalog number SK-RM-PBAY-FLTR-NRS.

## Remove the IP54/IP21 Power Bay Exhaust Vent Filters

Follow these steps to remove the IP54/IP21 power bay exhaust vent filters on a power bay.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Slide the vent up to release the tabs from the slots in the vent assembly and remove the vent.
4. Remove the filter from the vent cover.

<!-- image -->

## Install the IP54/IP21 Power Bay Exhaust Vent Filters

IMPORTANT Verify that the "X" on the fiber filter media points outward, toward the vent cover.

Install the IP54/IP21 power bay exhaust vent filters on a power bay in the reverse order of removal.

## IP54, 400 mm (15.75 in.) Wide Power Bay Door Vent Filter Replacement

Replace the IP54, 400 mm (15.75 in.) wide power bay door vent filters with kit catalog number SK-RM-PB4DR-54FLTR1.

## Remove an IP54, 400 mm (15.75 in.) Wide Power Bay Door Vent Filter

Follow these steps to remove the filter.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Loosen the two or three slotted-Phillips head, captive screws that secure the filter cover to the chassis on the door.
4. Open the filter cover by lowering the top downward. The bottom of the cover remains attached to the chassis with hinges.
5. If the metal mesh filter must be replaced, remove it.
6. If the fiber filter must be replaced, pull the top edge of the fiber filter out and remove the fiber filter from the filter cassette.

<!-- image -->

## IP21, 400 mm (15.75 in.) Wide Power Bay Door Vent Filter Replacement

## Install an IP54, 400 mm (15.75 in.) Wide Power Bay Door Vent Filter

Install the metal mesh filter, fiber filter, or both in the reverse order of removal.

| IMPORTANT   | Verify that the weep holes on the metal mesh filter are at the bottom of the filter when installed.              |
|-------------|------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | Verify that the airflow direction arrow on the fiber filter media points inward, toward the interior of the bay. |

Replace the IP21, 400 mm (15.75 in.) wide power bay door vent filter with kit catalog number SK-RM-PB4DR-21FLTR1.

## Remove an IP21, 400 mm (15.75 in.) Wide Power Bay Door Vent Filter

Follow these steps to remove the filter.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Loosen the two or three slotted-Phillips head, captive screws that secure the filter cover to the chassis on the door.
4. Open the filter cover by lowering the top downward. The bottom of the cover remains attached to the chassis with hinges.
5. Remove the metal mesh filter from the cover.

<!-- image -->

## IP54/IP21, 400/800 mm (15.75/31.5 in.) Wide Wire Bay Door Vent Filters Replacement

## Install an IP21, 400 mm (15.75 in.) Wide Power Bay Door Vent Filter

Install the filter in the reverse order of removal.

IMPORTANT

Verify that the weep holes on the metal mesh filter are at the bottom of the filter when installed.

Replace the IP54/IP21, 400/800 mm (15.75/31.5 in.) wide wire bay door vent filters with kit catalog number SK-RM-IB4DR-FLTR1.

<!-- image -->

The 400 mm (15.75 in.) wide wire bay contains two vents; one at the top and one at the bottom of the door. The 800 mm (31.5 in.) wide wire bay contains three vents; two at the top and one at the bottom of the door. Kit catalog number SK-RM-IB4DRFLTR1 contains two filters. Order the appropriate number of kits for your wire bay.

## Remove the IP54/IP21, 400/800 mm (15.75/31.5 in.) Wide Wire Bay Door Vent Filters

Follow these steps to remove the filters.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Lift the tab on the top center of the vent cover and rotate out the cover.
4. Remove the fiber filter from the vent housing.

<!-- image -->

## Install the IP54/IP21, 400/800 mm (15.75/31.5 in.) Wide Wire Bay Door Vent Filters

IMPORTANT

Verify that the Rittal logo on the fiber filter media points inward, toward the interior of the bay.

Install the filters in the reverse order of removal.

## IP54/IP21, 400/800 mm (15.75/31.5 in.) Wide Wire Bay Door Vent Exhaust Fan and Filter Assembly Replacement

Replace the IP54/IP21, 400/800 mm (15.75/31.5 in.) wide wire bay door vent exhaust fan and filter assembly with the appropriate kit catalog number:

- 400 mm (15.75 in.), SK-RM-WBDR-FANFLR1
- 800 mm (31.5 in.), SK-RM-WBDR-FANFLR2

## Remove the IP54/IP21, 400/800 mm (15.75/31.5 in.) Wide Wire Bay Door Vent Exhaust Fan and Filter Assembly

Follow these steps to remove the fan and filter assembly.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the wire bay door.
4. On the inside of the door, remove the M8 hex nut and washer that secures the two ground wire lugs to the door, and remove the wires.
5. Disconnect the fan power wires from connector P1 on the fan assembly.
6. Press the tabs on the fan assembly inward and move the fan/filter assembly out of the door through the front of the door.

<!-- image -->

## Install the IP54/IP21, 400/800 mm (15.75/31.5 in.) Wide Wire Bay Door Vent Exhaust Fan and Filter Assembly

Install the fan and filter assembly in the reverse order of removal.

## Thermal Switch Replacement

Replace the thermal switch with kit catalog number SK-RM-THRMSW-WB.

## Remove the Thermal Switch

Follow these steps to remove the thermal switch.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the wire bay door.
4. Loosen the 12 screws that secure the guards to the bay and remove the guards.

<!-- image -->

5. Remove the two M6 x 25 mm torx screws that secure the thermal switch assembly to the mounting bracket on the bus bar and remove the assembly. Retain the screws, guard, and clamp for reuse.
6. Disconnect the wires from the two terminals on the thermal switch.

<!-- image -->

## Install the Thermal Switch

Install the thermal switch in the reverse order of removal.

## Single-Density NRS Module DC Link Fuse Replacement

Replace the DC link fuses for a single-density NRS module with one of the kits listed in this table.

| NRS Module Cat. No. Voltage  Amps/Leg Quantity       | Cat. No.   |
|------------------------------------------------------|------------|
| 20-750-MNn-C770D740 400/480 SK-RM-DCFUSE1-NRS 1400 2 |            |
| 20-750-MNn-E545F505 600/690 SK-RM-DCFUSE2-NRS 1100 2 |            |

## Remove the Single-Density NRS Module DC Link Fuses

Follow these steps to remove the single-density NRS module DC link fuses.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the protective guard from the bay. See Remove the Power Bay Protective Guard on page 173 .
5. Disconnect the fuse sense harness leads from the stab terminals on the fuse indicator switches.

<!-- image -->

6. Remove the lower two M12 x 13 mm hex nuts that secure the fuses to the lower DC link bus bars.
7. Remove the upper two M12 x 13 mm hex nuts that secure the fuses to the upper DC link bus bars and remove the fuses.

<!-- image -->

## Install the Single-Density NRS Module DC Link Fuses

Install the single-density NRS module DC link fuses in the reverse order of removal.

IMPORTANT

Verify that the DC link fuse sense wire harness leads are installed on the N.C. (outer) fuse indicator switch terminals only. The middle terminal is not used.

## Dual-Density NRS Module DC Link Fuse Replacement

Replace the DC link fuses for a dual-density NRS module with one of the kits listed in this table.

| NRS Module Cat. No. Voltage  Amps/Leg Quantity      | Cat. No.   |
|-----------------------------------------------------|------------|
| 20-750-MNn-C1K4D1K3 400/480 SK-RM-DCFUSE1-F8 1400 4 |            |
| 20-750-MNn-E980F920 600/690 SK-RM-DCFUSE2-F8 1100 4 |            |

## Remove the Dual-Density NRS Module DC Link Fuses

Follow these steps to remove the dual-density NRS module DC link fuses.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the protective guard from the bay. See Remove the Power Bay Protective Guard on page 173 .
5. Disconnect the fuse sense harness leads from the stab terminals on the fuse indicator switches.
6. For the front fuse, remove the lower two M12 x 13 mm hex nuts that secure the fuses to the lower DC link bus bars.
7. For the front fuse, remove the upper two M12 x 13 mm hex nuts that secure the fuses to the upper DC link bus bars and remove the fuses.
8. For the rear fuse, repeat steps 6 and 7.

<!-- image -->

<!-- image -->

## Install the Dual-Density NRS Module DC Link Fuses

Install the dual-density NRS module DC link fuses in the reverse order of removal.

| IMPORTANT   | Verify that the DC link fuse sense wire harness leads are installed on the N.C. (outer) fuse indicator switch terminals only. The middle terminal is not used.   |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Replace the NRS module heatsink fan assembly with one of the kits listed in this table.

| NRS Module Cat. No. Voltage   | Cat. No.         |
|-------------------------------|------------------|
| 20-750-MNn-C770D740 400/480   | SK-RM-MFAN-NRS 1 |
| 20-750-MNn-E545F505 600/690   | SK-RM-MFAN-NRS 1 |
| 20-750-MNn-C1K4D1K3 400/480   | SK-RM-MFAN-F7 2  |
| 20-750-MNn-E980F920 600/690   | SK-RM-MFAN-F7 2  |

## NRS Module Heatsink Fan Assembly Replacement

## Remove the NRS Module Heatsink Fan Assembly

Follow these steps to remove the NRS module heatsink fan assembly.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Loosen the four captive M5 screws on the front of the fan assembly and pull the assembly out of the chassis partially.

Pull the fan assembly far enough out of the module chassis to provide access to the power-supply wire harness connector on the bottom of the assembly, which is shown in step 5 .

<!-- image -->

## NRS Module Power Supply Replacement

5. Disconnect the power-supply wire harness connector P21 from J21 on the bottom of the fan assembly and remove the assembly from the module chassis.

<!-- image -->

## Install the NRS Module Heatsink Fan Assembly

Install the NRS module heatsink fan assembly in the reverse order of removal.

## Remove an NRS Module Power Supply

Follow these steps to remove the NRS module power supply.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.

4. Remove the two screws that secure the power supply tray to the module chassis.
5. Slide the power supply tray out of the module chassis far enough to access the back of the power supply tray.
6. Unplug the connector from the back of the power supply tray.

<!-- image -->

Unplugging the connector from the back of the power supply tray allows you to take the tray to a workbench to replace the power supply. Alternatively, you can choose to replace the power supply in the tray while the connector remains connected to the back of the tray.

7. Disconnect all wires from the power supply by loosening the slottedPhillips head screw connections. See Figure 106 and Figure 107 on page 194 .
8. Disconnect the power supply from the DIN rail and remove it.

<!-- image -->

Figure 106 - 1X NRS Module Power Supply Wiring

<!-- image -->

Figure 107 - 2X NRS Module Power Supply Wiring

<!-- image -->

## Main Control Circuit Board Replacement

## Install an NRS Module Power Supply

Install the NRS module power supply in the reverse order of removal. When connecting wires to the power supply, follow the labeling. For output connections, positive wires must be connected to positive terminals and negative wires must be connected to negative terminals. However, it does not matter which positive wires go to which positive terminals and which negative wires go to which negative terminals. For input wiring, make sure line, neutral, and ground wires are connected to their proper terminals.

Replace the main control circuit board on the NRS module with one of these kit catalog numbers.

- SK-RM-MCB3-PF755-CD (400V/480V NRS modules)
- SK-RM-MCB3-PF755-EF (600V/690V NRS modules)

IMPORTANT

For dual-density NRS modules, we recommended that you replace both main control boards at the same time.

## Remove the Main Control Circuit Board

Follow these steps to remove the main control circuit board.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. To release the tabs on the protective cover from the slots in the chassis, lift vertically and pull the cover off the module.

<!-- image -->

## 5. Disconnect the following wire harness connectors from the main control board.

<!-- image -->

| Connection Description                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------|
| P1 to J1  240V AC control power and 48V fan power supply, and AC fuse indicator, fan control, and tachometer, inlet air NTC signals |
| P2 to J2 DC fuse connector                                                                                                          |
| P3 to J3 Power board (rear) connector                                                                                               |
| P4 to J4 Power board (front) connector, if present                                                                                  |
| P5 to J5 Three-phase AC supply present signal                                                                                       |
| P6 to J6 DC bus sense harness connector (1X module)                                                                                 |
| P7 to J7 Line reactor thermal switch signal (1X module)                                                                             |
| P8 to J8 DC bus sense harness connector (2X module), if present                                                                     |
| P9 to J9 Line reactor thermal switch signal (2X module), if present                                                                 |
| P10 to J10 10-pin I/O connector for customer connection                                                                             |
| P11 to J11 8-pin I/O connector for customer connection                                                                              |
| P12 to J12 240V AC and thermal switch control signals connector                                                                     |
| P13 to J13 DC bus conditioner, if present                                                                                           |

6. Loosen the seven captive M3 screws that secure the circuit board to the standoffs on the chassis and remove the board.
7. Remove the protective circuit board insulator sheet.

<!-- image -->

## Install the Main Control Circuit Board

Install the main control circuit board in the reverse order of removal.

| IMPORTANT   | Verify that the protective insulator sheet is in place behind the main control circuit board before installation.                                                      |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | Do not remove the protective covers from the following locations unless used at the time of installation: Connectors J4, J8, and J9 on the main control circuit board. |

## NRS Module Replacement

Replace the NRS module with the appropriate kit catalog number:

| Output Amps DC (normal duty)   | Cat. No.                                | Cat. No.   |
|--------------------------------|-----------------------------------------|------------|
| Output Amps DC (normal duty)   | With Bus Capacitors No Bus Capacitors   |            |
| 400 739 887                    | 20-750-MN1-C770D740 20-750-MN2-C770D740 |            |
| 480 681 817                    | 20-750-MN1-C770D740 20-750-MN2-C770D740 |            |
| 400 1406 1685                  | 20-750-MN1-C1K4D1K3 20-750-MN2-C1K4D1K3 |            |
| 480 1256 1507                  | 20-750-MN1-C1K4D1K3 20-750-MN2-C1K4D1K3 |            |
| 600 501 602                    | 20-750-MN1-E545F505 20-750-MN2-E545F505 |            |
| 690 501 602                    | 20-750-MN1-E545F505 20-750-MN2-E545F505 |            |
| 600 901 1082                   | 20-750-MN1-E980F920 20-750-MN2-E980F920 |            |
| 690 901 1082                   | 20-750-MN1-E980F920 20-750-MN2-E980F920 |            |

<!-- image -->

ATTENTION: NRS modules have a high center of gravity and a tip-over hazard exists. To guard against death, serious personal injury, or equipment damage, do not subject the module to high rates of acceleration or deceleration while transporting. Do not push or pull above the points that are indicated on the module.

Equipment is available that is designed to help you safely handle NRS modules. The following equipment is recommended:

- PowerFlex 750-Series module service cart, catalog number 20-750MCART1, publication 750-IN105 .
- PowerFlex 750TM power and LCL filter module storage hardware, catalog number 20-750-MINV-ATIP, publication 750-IN106 .
- PowerFlex 755T power module service ramp, catalog number 20-750-MRAMP1, publication 750-IN108 .

## IMPORTANT

The service ramp can only be used to transport an NRS module in or out of a power bay if all bays are mounted directly to the floor, using the Anchor Bolt System or the Concrete Screw System on page 57. Before you use the service ramp, review the instructions.

## Remove the NRS Module

Follow these steps to remove the NRS module from the power bay.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the protective guard from the bay. See Remove the Power Bay Protective Guard on page 173 .

5. To release the tabs on the protective cover from the slots in the chassis, lift vertically and pull the cover off the module.
6. Disconnect the following wire harness from the main control board.

<!-- image -->

<!-- image -->

<!-- image -->

| Connector Description                                                                        |
|----------------------------------------------------------------------------------------------|
| J2 DC fuse condition signal from connector P2 on the DC link fuses.                          |
| J10 Customer output connections for NRS module precharge complete, fault, and alarm signals. |
| J11 Customer input connections for NRS module clear faults and precharge enable signals.     |
| J12 240V AC and thermal switch control signals from bay harness connector P12.               |
| J13 DC bus conditioner signals from connector P13 on the DC bus conditioner, if present.     |

7. Remove the M10 hex nuts that secure the module flexible bus bars to the DC link fuse terminals.
- For a single-density NRS module, remove two hex nuts.
- For a dual-density NRS module, remove four hex nuts.
8. Remove the two M10 x 20 mm torx screws that secure the top of the module chassis to the control bus frame.
9. Leave the two M10 x 20 mm torx screws that secure the module chassis to the floor mounting bracket while preparing the PowerFlex 750-Series service cart or service ramp.
10. Remove the module by using the instructions in the appropriate manual:
- To remove the module by using the service cart, follow the detailed instructions in the PowerFlex 750-Series Service Cart and DCPC Module Lift Installation Instructions, publication 750-IN105 .
- To remove the module using PowerFlex 755TM service ramp, follow the procedures that are detailed in the PowerFlex 755T Module Service Ramp Instructions, publication 750-IN108 .
11. To release the module, remove the two remaining M10 x 20 mm screws that secure the module to the floor mounting bracket.
12. Remove the module from the power bay.

<!-- image -->

## NRS Module AC Input Fuse Replacement

## Install the NRS Module

Install the NRS module in the reverse order of removal.

| IMPORTANT   | Do not remove the protective covers from the following locations unless used at the time of installation: • Connectors J4, J8, and J9 on the main control circuit board                           |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | Verify that the PE-A and PE-B jumpers in the NRS module are installed in the correct position as required for your grounding scheme and application. See Power Jumper Configuration on page 137 . |

Replace the AC input fuses for an NRS module with one of the kits listed in this table.

| NRS Module Cat. No. Module Type    |         |                        |   Voltage Cat. No. Amps/Leg Quantity |
|------------------------------------|---------|------------------------|--------------------------------------|
| 20-750-MNn-C770D740 Single-Density | 400/480 | SK-RM-ACFUSE2-F8 1250  |                                    3 |
| 20-750-MNn-C1K4D1K3 Dual-Density   | 400/480 | SK-RM-ACFUSE1-F8 900   |                                    3 |
| 20-750-MNn-E545F505 Single-Density | 600/690 | SK-RM-ACFUSE4-F9 2000  |                                    3 |
| 20-750-MNn-E980F920 Dual-Density   | 600/690 | SK-RM-ACFUSE1-NRS 1400 |                                    3 |

## IMPORTANT

AC fuse removal requires a 19 mm open-end J-shank bit on a changeable-head torque wrench capable of 45 N·m (398 lb·in).

## Remove the NRS Module AC Input Fuses

Follow these steps to remove the NRS module AC input fuses.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the NRS module from the bay. See Remove the NRS Module on page 198 .

5. On the right side of the module, remove the eight M5 x 8 mm torx screws that secure the fuse access panel to the module chassis.
6. Disconnect the AC line fuse sense wire harness leads from the fuse indicator terminals.

<!-- image -->

<!-- image -->

7. Remove the top M12 hex nut that secures the fuse to the flexible AC input terminal.
8. Loosen the bottom M12 hex nut that secures the fuse to the AC input terminal and remove the fuse.

<!-- image -->

## Install the NRS Module AC Input Fuses

Install the NRS module AC input fuses in the reverse order of removal.

## IMPORTANT

Verify that the AC line fuse sense wire harness leads are installed on the N.C. (outer) fuse indicator terminals only. The two outer terminals are used. The middle terminal is not used.

<!-- image -->

## NRS Module DC Bus Capacitor Assembly Replacement

Replace the DC bus capacitor assembly for an NRS module with one of these kits.

- Catalog number: SK-RM-DCCAP1-CD (400V/480V)
- Catalog number: SK-RM-DCCAP1-EF (600V/690V)

## IMPORTANT

These kits contain one DC bus capacitor assembly. Dual-density NRS modules require two DC bus capacitor assemblies. For dual-density NRS modules, we recommend that you replace both assemblies.

## Remove the DC Bus Capacitor Assembly

Follow these steps to remove the NRS module DC bus capacitor assembly.

1. Review the Product Advisories on page 15 .
2. Remove power from the system. See Remove Power from the System on page 16 .
3. Open the power bay door.
4. Remove the NRS module from the bay. See Remove the NRS Module on page 198 .

5. Disconnect the DC bus sense wire harness from the main control circuit board:
- For a single-density NRS module, disconnect P6 from J6 on the main control board. P6 is the connector on the rear DC bus capacitor harness.
- For a dual-density NRS module, disconnect P6 from J6 and P8 from J8 on the main control board. P6 is the connector on the rear DC bus capacitor harness and P8 is the connector on the front DC bus capacitor harness.

IMPORTANT The DC bus sense wire harness must be retained for reuse. Take care not to damage the wire harness during removal.

<!-- image -->

6. Remove the ten M5 x 12 mm torx screws that secure the top cover to the module chassis and remove the cover.

<!-- image -->

7. Remove the M8 hex nuts that secure the flexible DC link bus bars to the DC bus terminals on the capacitor assembly and remove the bus bars.
- For a single-density NRS module, remove four hex nuts.
- For a dual-density NRS module, remove eight hex nuts.

Note: This drawing shows internal bus bars instead of the optional DC bus capacitor banks. However, the illustrations of the step still apply to accessing the DC bus capacitor banks.

<!-- image -->

8. Remove the M4 x 14 mm torx screws that secure the sides of the DC bus capacitor assembly to the module chassis.
- For a single-density NRS module, remove six screws.
- For a dual-density NRS module, remove 12 screws.

<!-- image -->

9. For a dual-density NRS module, remove the screws that secure the front panel to the chassis and remove the panel.

<!-- image -->

10. Remove the eight M5 x 10 mm torx screws that secure the access panel to the chassis and remove the panel.

<!-- image -->

11. Remove the M8 x 25 mm torx screws that secure the DC bus capacitor assembly to the module chassis.
- For a single-density NRS module, remove four screws.
- For a dual-density NRS module, remove eight screws.
12. Cut the cable ties that secure the DC bus sense wire harness to the inside of the module chassis. Of the three tie-down locations that are labeled 12 in the previous figure, the front DC bus sense wire harness is tied at the two tie-down locations farthest to the left. The rear DC bus sense wire harness is tied at all three tie-down locations.

<!-- image -->

IMPORTANT The DC bus capacitor assembly weights 11.3 kg (25 lb). We recommend that two persons lift and remove the assembly.

13. Lift the DC bus capacitor assembly up and out of the module chassis.

<!-- image -->

If the capacitor assemblies do not release from the module chassis easily, loosen the five screws on right, top side panel, to loosen the chassis.

14. Disconnect the DC bus sense wire harness connector from the stab terminal on the DC- bus terminal.
15. Remove the two M4 hex nuts and washers that secure the DC bus sense wire harness leads to the DC+ and middle DC laminated bus bars.

<!-- image -->

## Install the NRS Module DC Bus Capacitor Assembly

Install the DC bus capacitor assembly in the reverse order of removal.

## IMPORTANT

After the DC bus capacitor assemblies are installed in the NRS module chassis, by using cable ties, secure the DC bus sense wire harness to the inside of the module chassis.

## Numerics

755TM common bus inverter frame sizes 14

## A

AC line phase configuration switch 141

airflow 48

alarm codes 155

definition 155

descriptions display 149 indicator 158 names 155 types 155

155

recommended actions 155

anchor bolt floor mounting system 57

## B

back-to-back configuration 58

order of bay installation 80

back-to-back thermal switch signal interconnect harness 96

base floor mounting system 52

bay

14

configuration dimensions 59 key 33 topology 14

bay configurations 58

bays join 81

bay-to-bay communication 96

blower inspection 166

bus bar connections 123

bus bar locations 129

bus bar splice connections 91

bypass precharge 142

## C

cabinet fault indicator r 158

cable spacing 126

capacitance 142

catalog number explanation

location 26

CE conformity certifications 41

check interlocking device 168

locking device 168

circuit breakers 134

clear fault indicator 158

clear fault input 151

terminals 19

27

## clearable faults 151 clearance

airflow 48

overhead 47

service cart 49

## codes

alarm 155

fault 152

common mode capacitor circuits 137

component replacement schedules 169

concrete screw floor mounting system 57

CONFIG switch 140

contamination

equipment 166

control bus bar kits 121

control bus power

customer provided 133

via control bus connector 133

via T2 optional transformer 131

control bus wireway 20

control transformer

fuse locations 132

control transformer T1 primary fuses (FH1,

## FH2)

install 176

remove 176

control transformer T1 secondary fuse (FH3)

install 177

remove 177

control transformer T2 primary fuses (FH4,

## FH5)

install 178

remove 178

control transformer T2 secondary fuse (FH6)

install 179

remove 179

control transformers 131

T1 standard transformer 131

T2 optional transformer 131

## corrosive environment

installation requirements 46 , 69

specifications 45

customer input connections 19

procedure 21

termination 21

tie wrap supports 21

customer input wire

routing 20

specifications 20

customer output connections 19

procedure 21

termination 21

tie wrap supports 21

## customer output wire

routing 20

specifications 20

## fan

## D

## DC bus

connections to CBIs 119

connections to drives 119

minimum capacitance for powerup 11

DC bus bar kits 120

## DC bus capacitor assembly

install 212

remove 204

## DC voltage balance bay

bus bars 130

## dielectric withstand voltage

test 167

dimensions 59

## door

disable opening enable opening 86 key 33 stops 86

86

## drive bay

connections to NRS output 119

control bus bars 121

DC bus bars 120

enclosure specifications PE ground bars 120

89

## dual-density NRS module DC link fuses

install 190

remove 189

## E

## electrical connections

bay-to-bay 90 bus bar splice 91

wire bay fan power 94

emission compliance 43

## end power bay

loop-back signal interconnect harness 97

## entry wire bay

bus bars 130

## environmental specifications 45

## equipment

contamination 166

inspection

166

maintenance 165

## F

inspection

166

wire bay fan power connections 94

## fastener

final assembly torque 31

size 31

tool type and size 31

torque sequence 32

type 31

## fault

clear fault input terminals 19 clearable and non-clearable 151 codes 152 definition 150 display 149 function 151 indicator 158 maintenance after a fault 167 names 152 propogation diagram 159 recommended actions 152 system hard fault 150 types 152 wiring 151

## field programmable gate array

revision number 148

## final check

after maintenance 168

## floor mounting

affix bays to the floor 90

anchor bolt system 57 attach hardware to bottom of bays

80

attach hardware to the bottom of the bays

80

concrete screw system 57

hardware types 52

preparation 51

Rittal base/plinth system 52

structural steel system 55

## floor mounting hardware

maximum height 49

maximum setback 49

## frame clamps 87

fuses 134

## H

## handling 36

NRS module 74

heartbeat display 149

## I

ingress protection 45

inline configuration 58

inline thermal switch signal interconnect harness 96

## input protection 134

circuit breakers 134 fuses 134

input status indicators 157

## inspection

blower 166

166

equipment fan 166 terminal 167

## inspection schedules 169

## installation

add a bay to the lineup 81

affix bays to the floor 90 back-to-back configuration 80 bay-to-bay electrical connections floor mounting hardware 80 interior frame clamps 87 location 44 NRS module 105 paint-piercing rubber washers 90 position the first bay 80 seismic top brackets 86 site requirements 50 standard top bracket set 85

temporary storage 75

tools 30

## insulation resistance

test 167

interconnect harness 96

interior frame clamps 87

## interlocking device

check 168

IP21, 400 mm wide power bay door vent filter install 183

remove 182

IP54, 400 mm (15.75 in.) wide power bay door vent filter

install 182

remove 181

IP54/IP21 400/800 mm wire bay exhaust vent filters

install 183

remove 183

## IP54/IP21 power bay exhaust vent filters

install 180

remove 180

IP54/IP21, 400/800 mm (15.75/31.5 in.) wide wire bay door vent exhaust fan and

## filter assembly

install 184

remove 184

## J

## join bays 81

interior frame clamps 87

## K

key 33

kits renewal 171

## L

laminated bus capacitor 146

L-bracket connections 124

kit 125

spacing 128

## location

planning 44

lock

33

90

## locking device

check 168

loop-back signal interconnect harness 96 , 97

## M

## main control circuit board 18

AC line phase configuration switch 141 alarm display 149 alarm indicator 158 cabinet fault indicator 158 clear fault indicator 158 clear fault input 19 CONFIG switch 140 configuration 140 customer input and output connections 19 fault display 149 fault indicator 158 input status indicators 157 install 197 normal operation display 149 NRS module status indicator 157 output status indicators 157 power-up displays 148 precharge complete indicator 158 precharge switch 140 remove 195 seven-segment LED display 148 status indicators 147 system status displays 148 touch guard 147 user enable input 19 user enable input configuration switch 141

user enable input indicator 158

## maintenance

equipment 165

final check 168

schedules 169

task codes 168

maximum capacitance 142

minimum DC bus capacitance for powerup 11

module-to-module communication 96

mounting surface

50

## N

N-1 operation 105

signal propogation diagram 164

nameplate

26

non-clearable faults 151

normal operation display 149

## NRS module

1X schematics 145 2X schematics 146 AC input fuse replacement 201 DC bus capacitor assembly replacement 204 dual-density main internal components 10 dual-density NRS module DC link fuse replacement 189 handling 74 heatsink fan assembly replacement 190 install as a replacement 201 install for the first time 105 main control circuit board replacement 195 N-1 Jumper replacement 175 power ratings 12 power supply replacement 192 power-bay signal interconnect harness 96 recommened handling equipment 75 remove 198 remove from power bay during installation 74 service ramp requirements 52 single-density main internal components 10 single-density NRS module DC link fuse replacement 187 status indicator 157 temporary storage 75 NRS module AC input fuses install 203 remove 201 NRS module heatsink fan assembly install 192 remove 191 NRS module N-1 jumper install 175 remove 175 NRS module power supply install 195 remove 192 NRS output bay 119 NRS-module-to-power-bay signal interconnect harness 96 O output status indicators 157 overhead clearance 47 P packing slip 33 paint-piercing rubber washers 90 part replacement schedules 169 particulate pollution 45 PE ground bar specifications 120 PE-A jumper 137 PE-B jumper 137 periodic inspection 166 plinth floor mounting system 52 pollution corrosive gas and vapor 45 particulate 45

## power

ratings 12

remove 16

## power bay

bus bars 129

schematics for 1X NRS module power bay

143

schematics for 2X NRS module power bay 144

status indicator viewing window 147

## power bay protective guard

install 173

remove 173

power jumper configuration 137

## power-bay-to-power-bay signal interconnect

harness 96

## powerup

displays 148

minimum DC bus capacitance 11

## precharge

bypass 142

complete indicator 158

switch 140

synchronization 159

preventive maintenance

165

protective touch guards 72

## R

receiving 33

reduced capacity operation 105

## remove

NRS module 74

protective touch guards 72 shipping hardware 70

remove power 16

renewal kits 171

replace protective touch guards 72

replacement components 171

Rittal base/plinth system 52

roof panels 90

## S

S1 switch 140

S2 switch 140

schedules of maintenance tasks 169

seismic installation 46

install top brackets 86 top brackets 82

## service cart

access requirements 49

## service ramp

requirements 52

seven-segment LED display 148

alarm display 149

normal operation display 149

148

fault display 149 power-up displays 148 system status displays

## shipment

configurations damage 34 loss 34 weights 33

35

## shipping hardware removal 70

## side sheet

install 81

remove 81

## single-density NRS module DC link fuses

install 188

remove 187

## specifications

environmental 45

## status indicators 147

alarm 158 cabinet fault 158 clear fault 158 fault 158 input and output 157 precharge complete 158 user enable input 158 viewing window 147

storage 39

structural steel floor mounting system 55

STS LED

157

sweep times 142

SYNC bus signal 159

diagrams 159

## system communication interconnect harness

96

back-to-back thermal switch signal interconnect harness 96 inline thermal switch signal interconnect harness 96 installation examples 103 loop-back 96 NRS-module-to-power-bay 96 power-bay-to-power-bay 96 replacement 174

wire-bay-to-power-bay-thermal-switch 96

## system communication signal propogation

diagrams 159

system hard fault 150

## system schematics 143

1X NRS module 145

1X NRS module power bay 143

2X NRS module 146

2X NRS module power bay 144

## system status displays 148

## T

T1 standard transformer 131

T2 optional transformer 131

## terminal

inspection 167

## test

dielectric withstand voltage 167 insulation resistance 167 17

testpoint locations

## thermal switch (wire bay)

install 186

remove 185

## tools 30

NRS module handling 75

## top brackets

seismic installation 82 , 86 standard installation 82 , 85

touch guards 72

## U

unlock 33

## user enable input

configuration switch 141 indicator 158 terminals 19

## V

## viewing window 147

## W

## weight

approximage section weight 35 exact shipment weight 33

## wire bay

fan power connections 94

## wire bay thermal switch

install 186

remove 185

## wire-bay-to-power-bay-thermal-switch

signal interconnect harness 96

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                                                               | Description                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PowerFlex 755TM Non-Regenerative Supply Technical Data, publication 750-TD103                                          | Provides detailed information on: • NRS specifications • NRS system guidance • Option specifications                                                                                                                                        |
| PowerFlex 755TM IP00 Open Type Kits Technical Data, publication 750-TD101                                              | Provides detailed information on: • Kit selection • Kit ratings and specifications • Option specifications                                                                                                                                  |
| PowerFlex 750-Series Products with TotalFORCE® Control Installation Instructions, publication 750-IN100                | Provides the basic steps to install PowerFlex 755TL low harmonic drives, PowerFlex 755TR regenerative drives, and PowerFlex 755TM drive systems.                                                                                            |
| PowerFlex 755TM IP00 Open Type Kits Installation Instructions, publication 750-IN101                                   | Provides instructions to install IP00 Open Type kits in user-supplied enclosures.                                                                                                                                                           |
| Drives in Common Bus Configurations with PowerFlex 755TM Bus Supplies Application Techniques, publication DRIVES-AT005 | Provides basic information to properly wire and ground the following products in common bus applications: • PowerFlex 755TM drive system for common bus solutions • PowerFlex 750-Series AC and DC input drives • Kinetix 5700 servo drives |
| PowerFlex 755TM Power and Filter Modules Unpacking and Lifting Instructions, publication 750-IN104                     | These publications provide detailed information on: • Precautions and recommendations • Hardware attachment points • Lifting the component out of the packaging                                                                             |
| PowerFlex 750-Series Service Cart Instructions, publication 750-IN105                                                  | Provides detailed set-up and operating instructions for the module service cart and DC precharge module lift.                                                                                                                               |
| PowerFlex 755T Module Service Ramp Instructions, publication 750-IN108                                                 | Provides detailed usage instructions for the module service ramp.                                                                                                                                                                           |
| Wiring and Grounding Guidelines for Pulse Width Modulated (PWM) AC Drives, publication DRIVES-IN001                    | Provides basic information to properly wire and ground PWM AC drives.                                                                                                                                                                       |

To view or download publications, go to rok.auto/literature .

To access declarations of conformity, certificates, and other certification details, go to rok.auto/certifications .

## Rockwell Automation Support

Use these resources to access support information.

| Technical Support Center                         | Find help with how-to videos, FAQs, chat, user forums, and product notification updates.           | rok.auto/support       |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------|
| Knowledgebase                                    | Access Knowledgebase articles.                                                                     | rok.auto/knowledgebase |
| Local Technical Support Phone Numbers            | Locate the telephone number for your country.                                                      | rok.auto/phonesupport  |
| Literature Library                               | Find installation instructions, manuals, brochures, and technical data publications.               | rok.auto/literature    |
| Product Compatibility and Download Center (PCDC) | Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes. | rok.auto/pcdc          |

## Documentation Feedback

Your comments help us serve your documentation needs better. If you have any suggestions on how to improve our content, complete the form at rok.auto/docfeedback .

## Waste Electrical and Electronic Equipment (WEEE)

<!-- image -->

At the end of life, this equipment should be collected separately from any unsorted municipal waste.

Rockwell Automation maintains current product environmental compliance information on its website at rok.auto/pec .

Allen-Bradley, expanding human possibility, PowerFlex, Rockwell Automation, and TotalFORCE are trademarks of Rockwell Automation, Inc. Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation,1201SouthSecondStreet,Milwaukee,WI53204-2496USA,Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV.PegasusPark,DeKleetlaan12a:1831DiegemBelgium.Tel:(32)26630600,Fax:(32)26630640 ASlAPACIFIC:RockwellAutomation,Level14.CoreF,Cyberport3,100 Cyberport Road.HongKong.Tel:(852)28874788.Fax:(852)25081846