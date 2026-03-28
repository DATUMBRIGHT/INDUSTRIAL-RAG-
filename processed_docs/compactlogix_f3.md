<!-- image -->

## Compact High-speed Counter Module

Catalog Number 1769-HSC

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Important User Information

Solid-state equipment has operational characteristics differing from those of electromechanical equipment. Safety Guidelines for the Application, Installation and Maintenance of Solid State Controls (publication SGI-1.1 available from your local Rockwell Automation sales office or online at http://www.rockwellautomation . co m/literature/) describes some important differences between solid-state equipment and hard-wired electromechanical devices. Because of this difference, and also because of the wide variety of uses for solid-state equipment, all persons responsible for applying this equipment must satisfy themselves that each intended application of this equipment is acceptable.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which can lead to personal injury or death, property damage, or economic loss.

<!-- image -->

<!-- image -->

<!-- image -->

## IMPORTANT

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence

SHOCK HAZARD: Labels can be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage can be present.

BURN HAZARD: Labels can be on or inside the equipment, for example, a drive or motor, to alert people that surfaces can reach dangerous temperatures.

Identifies information that is critical for successful application and understanding of the product.

Allen-Bradley, Rockwell Software, Rockwell Automation, RS Logix, RSLogix 5000, RSLogix 500, CompactLogix, Compact I/O, ControlLogix, MicroLogix, and TechConnect are trademarks of Rockwell Automation, Inc. Trademarks not belonging to Rockwell Automation are property of their respective companies.

## New and Updated Information

This manual contains new and updated information. Changes throughout this revision are marked by change bars, as shown to the right of this paragraph.

This table contains the changes made to this revision.

| Topic                                                                                 | Pages                                                                                                                                                      |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Changes were made to differentiate between the available high speed counters modules. | 31 ,  32 ,  37 ,  40 ,  66 ,  70 ,  72 , 73 ,  74 ,  76 ,  80 ,  81 ,  84 ,  85 , 86 ,  88 ,  89 ,  95 ,  96 ,  97 ,  98 , 100 ,  101 ,  105 ,  107 ,  121 |

## Notes:

## Table of Contents

| Preface          | Packaged Controller Functionality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
|                  | Additional Resources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9              |
|                  | Chapter 1                                                                                                                       |
| Module Overview  | Counters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12     |
|                  | Inputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12 |
|                  | Outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12    |
|                  | Hardware Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13              |
|                  | Status Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14          |
|                  | Chapter 2                                                                                                                       |
| Module Operation | Counter Defaults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15             |
|                  | Module Operation Block Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16                              |
|                  | Inputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16         |
|                  | Outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17            |
|                  | Number of Counters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18                 |
|                  | Summary of Available Counter Configurations . . . . . . . . . . . . . . . . . . . . . 18                                        |
|                  | Input Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20        |
|                  | Operational Mode Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21                       |
|                  | Direction Inhibit and Direction Invert Output Control Bits . . . . . 21                                                         |
|                  | Pulse/External Direction Mode Selection. . . . . . . . . . . . . . . . . . . . . . . 22                                         |
|                  | Pulse/Internal Direction Mode Selection . . . . . . . . . . . . . . . . . . . . . . . 23                                        |
|                  | Up and Down Pulses Mode Selection . . . . . . . . . . . . . . . . . . . . . . . . . . 24                                        |
|                  | X1 Quadrature Encoder Mode Selection . . . . . . . . . . . . . . . . . . . . . . . 25                                           |
|                  | X2 Quadrature Encoder Mode Selection . . . . . . . . . . . . . . . . . . . . . . . 26                                           |
|                  | X4 Quadrature Encoder Mode Selection . . . . . . . . . . . . . . . . . . . . . . . 26                                           |
|                  | Input Frequency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28            |
|                  | Counter Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28          |
|                  | Linear Counter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28                  |
|                  | Ring Counter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                 |
|                  | Modifying Count Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29                    |
|                  | Counter Enable/Disable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30                           |
|                  | Z Input Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30                    |
|                  | Inhibit and Invert . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30                   |
|                  | Direct Write . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30               |
|                  | Preset/Reset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31               |
|                  | Rate/Timer Functionality. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32                    |
|                  | Pulse Interval Rate Calculation Method . . . . . . . . . . . . . . . . . . . . . . . . 32                                       |
|                  | Cyclic Rate Calculation Method (current rate). . . . . . . . . . . . . . . . . . 32                                             |
|                  | Hysteresis Detection and Configuration. . . . . . . . . . . . . . . . . . . . . . . . 33                                        |
|                  | Scalar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34       |
|                  | Rate Valid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34             |
|                  | Rate Method Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35                        |

|                               | Output Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                                                                    |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                               | Masks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                                                                  |
|                               | Ranges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37                                                                  |
|                               | Overcurrent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40                                                                       |
|                               | Safe State Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40                                                                            |
|                               | Output Control Example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43                                                                                     |
|                               | Readback/Loopback . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44                                                                                 |
|                               | Chapter 3                                                                                                                                                                                |
| Installation and Wiring       | Power Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47                                                                        |
|                               | General Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47                                                                          |
|                               | Selecting a Location to Reduce Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . 47                                                                                            |
|                               | Protect the Circuit Board from Contamination . . . . . . . . . . . . . . . . . 48                                                                                                        |
|                               | Power Supply Distance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48                                                                                 |
|                               | System Assembly . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49                                                                     |
|                               | Mount the Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                                                                        |
|                               | Minimum Spacing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                                                                               |
|                               | Panel Mounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                                                                            |
|                               | DIN Rail Mounting. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52                                                                                |
|                               | Replace the Module within a System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53                                                                                      |
|                               | Field Wiring Connections. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54                                                                             |
|                               | Considerations for Reducing Noise. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                                                                                            |
|                               | Remove and Replace the Terminal Block . . . . . . . . . . . . . . . . . . . . . . . 55                                                                                                   |
|                               | Wire the Finger-safe Terminal Block . . . . . . . . . . . . . . . . . . . . . . . . . . . 55                                                                                             |
|                               | Wire the Modules. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57                                                                             |
|                               | Terminal Door Label. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58                                                                                |
|                               | Terminal Block Wiring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58                                                                                  |
|                               | Wire Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59                                                                           |
|                               | Output Wiring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                                                                           |
|                               | Chapter 4                                                                                                                                                                                |
| Module Configuration, Output, | Configure the Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65                                                                          |
| and Input Data                | Configuration Array . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66                                                                       |
|                               | General Configuration Bits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72                                                                                    |
|                               | Filter Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                                                                        |
|                               | Program Mode and Program State Run . . . . . . . . . . . . . . . . . . . . . . . . . 76                                                                                                  |
|                               | Output Program Value (Out0ProgramValue through                                                                                                                                           |
|                               | Out3ProgramValue) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77 Output Fault Mode and Output Fault State Run . . . . . . . . . . . . . . . . 77 |
|                               | Output Fault Value (Out0FaultValue through Out3FaultValue) . 78                                                                                                                          |
|                               | Counter Maximum Count (CtrnMaxCount) . . . . . . . . . . . . . . . . . . . 78 Counter Minimum Count (CtrnMinCount) . . . . . . . . . . . . . . . . . . . 79                              |
|                               | Counter Preset (CtrnPreset). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79                                                                                      |
|                               | Counter Hysteresis (CtrnHysteresis) . . . . . . . . . . . . . . . . . . . . . . . . . . . 80                                                                                             |
|                               | Counter Scalar (CtrnScalar) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80                                                                                     |

Diagnostics and

Troubleshooting

| Cyclic Rate Update Time (CtrnCyclicRateUpdateTime) . . . . . . . . 81                                                      |
|----------------------------------------------------------------------------------------------------------------------------|
| Configuration Flags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82                 |
| Range High Limit (Range0To11[n].HighLimit) and Range Low                                                                   |
| Limit (Range0To11[n].LowLimit) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84                                  |
| Range Output Control (Range0To11[n].OutputControl). . . . . . . 85                                                         |
| Range Configuration Flags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86                       |
| Output Array . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88    |
| Output on Mask (OutputOnMask.0 through OutputOnMask.15) . .                                                                |
| RBF - Reset Blown Fuse (ResetBlownFuse) . . . . . . . . . . . . . . . . . . . . . 92                                       |
| Control Bits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92          |
| Range High Limit or Direct Write Value                                                                                     |
| (Range12To15[n].HiLimOrDirWr). . . . . . . . . . . . . . . . . . . . . . . . . . . 94                                      |
| Range Low Limit (Range12To15[n].LowLimit) . . . . . . . . . . . . . . . . 95                                               |
| Range Output Control (Range12To15[n].OutputControl). . . . . . 96                                                          |
| Range Configuration Flags (12To15) . . . . . . . . . . . . . . . . . . . . . . . . . . 96                                  |
| Input Array . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98 |
| Input State (InputStateA0 through InputStateZ1) . . . . . . . . . . . . . 101                                              |
| Readback (Readback.0 through Readback.15). . . . . . . . . . . . . . . . . . 101                                           |
| Status Flags . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101         |
| Range Active (RangeActive.0 through RangeActive.15). . . . . . . . . 103                                                   |
| Current Count (Ctr[n].CurrentCount). . . . . . . . . . . . . . . . . . . . . . . 104                                       |
| Stored Count (Ctr[n].StoredCount). . . . . . . . . . . . . . . . . . . . . . . . . . 104                                   |
| Current Rate (Ctr[0].CurrentRate to Ctr[3].CurrentRate) . . . . . 105                                                      |
| Chapter 5                                                                                                                  |
| Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109            |
| Status Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109              |
| Stand Clear of the Machine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                         |
| Program Alteration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110                 |
| Safety Circuits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110            |
| Module Operation versus Counter Operation . . . . . . . . . . . . . . . . . . . . . 111                                    |
| Module Diagnostics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112           |
| Power-up Diagnostics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112                    |
| Post Configuration Diagnostics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113                            |
| Non-critical versus Critical Module Errors . . . . . . . . . . . . . . . . . . . . . . . . 113                             |
| Non-critical Errors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113                |
| Critical Errors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113           |

|                                 | Module Error Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114                        |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
|                                 | Module Error Field . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114                           |
|                                 | Extended Error Information Field. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114                                        |
|                                 | Error Codes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116            |
|                                 | Appendix A                                                                                                                           |
| Specifications                  | Throughput and Timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126                          |
|                                 | Rate Accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127              |
|                                 | Temperature Derating . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 128                       |
|                                 | Dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130                     |
|                                 | Appendix B                                                                                                                           |
| Program a 1769-HSC Module,      | System Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131                 |
| CompactLogix Controller, and    | 845F Encoder Wiring to the 1769-HSC Module . . . . . . . . . . . . . . . . . . . 132                                                 |
| 845F Incremental Encoder with   | Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132      |
|                                 | Add a 1769-HSC Module to a CompactLogix System . . . . . . . . . . . . . . 133                                                       |
| RSLogix 5000 Software           | Configure the 1769-HSC Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136                                    |
|                                 | Monitor the Current Count and Verify Output Operation . . . . . . . . . 140                                                          |
|                                 | Appendix C                                                                                                                           |
| Program a 1769-HSC Module,      | System Diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141                 |
| MicroLogix 1500 Controller, and | 845F Encoder Wiring to the 1769-HSC Module . . . . . . . . . . . . . . . . . . . 142                                                 |
| 845F Incremental Encoder with   | Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142      |
|                                 | Add a 1769-HSC Module to a MicroLogix 1500 System . . . . . . . . . . . . 143                                                        |
| RSLogix 500 Software            | Configure Your 1769-HSC Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145                                       |
|                                 | Monitor the Current Count and Verify Output Operation . . . . . . . . . 148                                                          |
|                                 | Appendix D                                                                                                                           |
| Programming Quick Reference     | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 149 |
|                                 | Appendix E                                                                                                                           |
| History of Changes              | 1769-UM006C-EN-P, November 2010 . . . . . . . . . . . . . . . . . . . . . . . . . . . 155                                            |
| Glossary                        | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 157 |
| Index                           | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  . 165 |

## Packaged Controller Functionality

## Additional Resources

Use this manual if you are responsible for designing, installing, programming, or troubleshooting control systems that use Compact I/O and/or MicroLogix 1500 or CompactLogix controllers.

Both the 1769-L24ER-QBFC1B and 1769-L27ERM-QBFC1B packaged controllers provide the same high-speed counter (HSC) functionality as the 1769-HSC except for the input frequency.

While many features of the 1769-HSC module are available with the embedded high-speed counters, some of the features of the 1769-HSC module are not available with the embedded high-speed counters of the CompactLogix packaged controllers. Features not available on the embedded high-speed counters include rate/timer functions and limited output range control (4 ranges instead of the 16 available with the 1769-HSC module). Specific differences between the 1769-HSC module and the packaged controller functionality are noted throughout this manual.

The CompactLogix Packaged Controllers Quick Start and User Manual, publication IASIMP-QS010, provides wiring diagrams, configuration procedures, and tag descriptions for the embedded high-speed counters.

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                                | Description                                                                                                       |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| CompactLogix System User Manual, publication 1769-UM007                                 | Describes how to install, use, and program your CompactLogix controller.                                          |
| Compact I/O 1769-ADN DeviceNet Adapter User Manual, publication 1769-UM001              | Describes how to install, and use the 1769-ADN DeviceNet adapter.                                                 |
| Compact I/O Selection Guide, publication 1769-SG002                                     | Describes the 1769 Compact I/O modules.                                                                           |
| CompactLogix Packaged Controllers Quick Start and User Manual, publication IASIMP-QS010 | Provides a quick start and information on how to install, use, and program your CompactLogix packaged controller. |
| MicroLogix 1500 Programmable Controllers User Manual, publication 1764-UM001            | Describes how to install, use, and program your MicroLogix 1500 controller.                                       |
| MicroLogix Programmable Controllers Family Selection Guide, publication 1761-SG001      | Provides an overview of the MicroLogix 1500 system.                                                               |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1             | Provides general guidelines for installing a Rockwell Automation industrial system.                               |
| Product Certifications website, http://www.ab.com                                       | Provides declarations of conformity, certificates, and other certification details.                               |

You can view or download publications at http://www.rockwellautomation . co m/ literature/. To order paper copies of technical documentation, contact your local Allen-Bradley distributor or Rockwell Automation sales representative.

## Notes:

## Module Overview

The 1769-HSC module is an intelligent counter module with its own microprocessor and I/O that is capable of reacting to high-speed input signals. The module can interface with up to two channels of quadrature or four channels of pulse/count inputs. The signals received at the inputs are filtered, decoded, and counted. They are also processed to generate rate and time-between-pulses (pulse interval) data. Count and rate values can then be used to activate outputs based on user-defined ranges.

| IMPORTANT   | For the 1769-L23E-QBFC1B and 1769-L23-QBFC1B packaged controllers HSC functionality, there is no processing to generate rate or time between-pulses data. Only count data is used to activate outputs based on ranges.   |
|-------------|---|

The module counts pulses at up to 1 MHz (250 kHz for the packaged controllers) from devices such as proximity switches, pulse generators, turbine flowmeters, and quadrature encoders. The module has four on-board, high-speed switching outputs. These outputs can be under user program or direct module control, based on the count value or frequency.

The 1769-HSC module is compatible with MicroLogix 1500 packaged controllers (1764-LSP/C and 1764-LRP/C modules, firmware revision 6.0 and later), CompactLogix controllers (generic profiles required for firmware revisions prior to 11.0), and the 1769-ADN/B DeviceNet adapter.

| Topic             |   Page |
|-------------------|--------|
| Counters          |     12 |
| Inputs            |     12 |
| Outputs           |     12 |
| Hardware Features |     13 |
| Status Indicators |     14 |

1

## Counters

## Inputs

## Outputs

The module is capable of counting pulses in either direction (forward, reverse, up, down). A maximum of four pulse counters (or two quadrature counters) are available. Each 32-bit counter can count to ±2 billion as a ring or linear counter. In addition to providing a count value, the module provides a rate value up to ±1 MHz, dependent upon the type of input (the L23 packaged controller's HSC module functionality does not provide rate values). The rate value (as modified by scalar) is the input frequency to the counter. When the count value is increasing, the rate value is positive. When the count value is decreasing, the rate value is negative.

Counters can also be reset or preset to any value between user-defined minimum and maximum values. Preset can be accomplished from the user program or at a Z-input event. The Z-input can also generate a capture value and/or freeze (gate) the counters.

The module features six, high-speed differential inputs labeled ±A0, ±B0, ±Z0, ±A1, ±B1, and ±Z1. These inputs support two quadrature encoders with ABZ inputs and/or up to four discrete count inputs. In addition, x1, x2, and x4 encoder configurations are provided to fully use the capabilities of high resolution quadrature encoders. The inputs can be wired for standard differential line driver output devices, as well as single-ended devices such as limit switches, photo eyes, and proximity sensors. Inputs are optically isolated from the bus and from one another, and have an operational range of 2.6…30V DC.

Sixteen outputs are available: four on-board (real) and twelve virtual bits. All 16 outputs can be individually controlled by the module or by the user control program.

The four on-board (real) outputs are DC sourcing, powered by a user-supplied (5…30V DC) power source. These outputs are electronically protected from current overloads and short-circuit conditions. Overcurrent status is monitored and fed back to the user program. Output states are determined by a combination of output data, configuration data, ranges, and overcurrent status.

See Output Control Example on page 44 for a description of how the module determines output status.

## Hardware Features

The module's hardware features are illustrated in Figure 1. Refer to Chapter 3 on page 45 for detailed information on installation and wiring.

For information about the packaged controllers' hardware features, see the CompactLogix Packaged Controllers Quick Start and User Manual, publication IASIMP-QS010 .

Figure 1 - Hardware Features

<!-- image -->

| Item Description                                             |
|--------------------------------------------------------------|
| 1 Bus lever                                                  |
| 2a Upper panel mounting tab                                  |
| 2b Lower panel mounting tab                                  |
| 3 Module status indicators (6 Input, 4 Output, 1 Fuse, 1 OK) |
| 4 Module door with terminal identification label             |
| 5 Removable terminal block (RTB) with finger-safe cover      |
| 5a RTB upper-retaining screw                                 |
| 5b RTB lower-retaining screw                                 |
| 6a Movable bus connector (bus interface) with female pins    |
| 6b Stationary bus connector (bus interface) with male pins   |
| 7 Nameplate label                                            |
| 8a Upper tongue-and-groove slots                             |
| 8b Lower tongue-and-groove slots                             |
| 9a Upper DIN-rail latch                                      |
| 9b Lower DIN-rail latch                                      |
| 10 Write-on label for user identification tags               |

## Status Indicators

<!-- image -->

45272

The front panel of the 1769-HSC module has a total of 12 status indicators.

For information about the packaged controllers' status indicators, see the CompactLogix Packaged Controllers Quick Start and User Manual, publication IASIMP-QS010 .

Table 1 - Diagnostic Indicators

| Indicator Status   | Description                                                                                                                                                                                                                                             |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 OUT  Amber       | ON/OFF logic status of output 0                                                                                                                                                                                                                         |
| 1 OUT  Amber       | ON/OFF logic status of output 1                                                                                                                                                                                                                         |
| 2 OUT  Amber       | ON/OFF logic status of output 2                                                                                                                                                                                                                         |
| 3 OUT  Amber       | ON/OFF logic status of output 3                                                                                                                                                                                                                         |
| FUSE  Red          | Overcurrent                                                                                                                                                                                                                                             |
| OK  Off            | No power is applied                                                                                                                                                                                                                                     |
|                    | Red (briefly) Performing self-test                                                                                                                                                                                                                      |
|                    | Solid green OK, normal operating condition                                                                                                                                                                                                              |
|                    | Flashing green OK, module in Program or Fault mode                                                                                                                                                                                                      |
|                    | Solid red or amber Hardware error. Cycle power to the module. If problem persists, replace the module.                                                                                                                                                  |
|                    | Flashing red Recoverable fault. Reconfigure, reset, or perform error recovery. See Non-critical versus Critical Module Errors on page 113. The OK indicator flashes red for all of the error codes in the Configuration Error Codes table on page 117 . |
| A0                 | Amber ON/OFF status of input A0                                                                                                                                                                                                                         |
| A1                 | Amber ON/OFF status of input A1                                                                                                                                                                                                                         |
| B0                 | Amber ON/OFF status of input B0                                                                                                                                                                                                                         |
| B1                 | Amber ON/OFF status of input B1                                                                                                                                                                                                                         |
| Z0                 | Amber ON/OFF status of input Z0                                                                                                                                                                                                                         |
| Z1                 | Amber ON/OFF status of input Z1                                                                                                                                                                                                                         |

ALL ON

Possible causes for all status indicators to be On include the following:

- Bus error has occurred—controller hard fault. Cycle power.
- During load upgrade of controller—normal operation. Do not cycle power during the load upgrade.
- All indicators flash on briefly during powerup—normal operation.

## Counter Defaults

## Module Operation

This chapter details the operation of the 1769-HSC module. We strongly suggest that you review this information before configuring your module.

| Topic                                          | Page   |
|------------------------------------------------|--------|
| Counter Defaults                               | 15     |
| Module Operation Block Diagrams                | 16     |
| Number of Counters                             | 18     |
| Summary of Available Counter Configurations 18 |        |
| Input Filtering                                | 20     |
| Operational Mode Selection                     | 21     |
| Input Frequency                                | 28     |
| Counter Types                                  | 28     |
| Modifying Count Value                          | 29     |
| Rate/Timer Functionality                       | 32     |
| Output Control                                 | 36     |

When the module powers up, all output array and configuration array values are set to their default values. Refer to Chapter 4 on page 65 or Appendix D on page 149 for default values. All input array values are cleared. None of the module data is retentive through a power cycle.

Power cycling the module has the following effects:

- Clears stored counts and configurations
- Clears faults and flags
- Turns outputs off

<!-- image -->

## Module Operation Block Diagrams

To provide an overview of the module operation, the block diagrams indicate relationships between module functions and configuration parameters.

## Inputs

The following diagram illustrates how the inputs function.

<!-- image -->

## Outputs

The following diagram illustrates how the outputs function.

<!-- image -->

- (1) In the packaged controller, the Type parameter is fixed at Count because the rate measurement is not supported.

## Number of Counters

## Summary of Available Counter Configurations

The module has six input points: A0, B0, Z0, A1, B1, and Z1. Through these inputs, the module can function with 1, 2, 3, or 4 counters depending upon the number of counters and the operational mode configuration of the input points.

The table summarizes the input configurations available for all counters, based on the number of counters.

| No. of Counters Counter Operational Mode Gate or Preset Functionality   |                           |
|-------------------------------------------------------------------------|---------------------------|
| 1 Counter 0 Any All                                                     |                           |
| 1 through 3 Not available                                               | 1 through 3 Not available |
| 2 Counters 0 Any All                                                    |                           |
| 1 Any All                                                               |                           |
| 2 and 3 Not available                                                   | 2 and 3 Not available     |
| 3 Counters 0 Any All                                                    |                           |
| 1 Pulse/Internal Direction All                                          |                           |
| 2 Pulse/Internal Direction None                                         |                           |
| 3 Not available                                                         | 3 Not available           |
| 4 Counters 0 Pulse/Internal Direction All                               |                           |
| 1 Pulse/Internal Direction All                                          |                           |
| 2 Pulse/Internal Direction None                                         |                           |
| 3 Pulse/Internal Direction None                                         |                           |

45273

The counter options and operating modes are summarized in Figure 2.

Figure 2 - Summary of Available Counters

<!-- image -->

(1) The number of counters is defined by the NumberOfCounters bits in word 0 of the configuration array.

## Input Filtering

In many industrial environments, high frequency noise can be inadvertently coupled to the sensor wires. The module can help reject some noise by means of built-in filters. Inputs are filtered by means of user-selectable, low-pass filters (1) set up during module configuration.

The available nominal pulse width filters are shown in the table.

| Input   | Filter                                                                                                                 |
|---------|------------------------------------------------------------------------------------------------------------------------|
|         | A0, A1, B0, B1, Z0, Z1 5 ms, 500 s, 10 s, no filter (7.1 ms, 715 s, 18.5 s, no filter for the packaged controller) |

The filters are selected for each input in the Filter Selection word of the module's configuration array.

TIP

The input state bits (InputStateA0 through InputStateZ1) reflect the filter's inputs, but are NOT affected by the signal inhibit or invert operations described on page 30 .

| Nom Filter Settings   | Nom Filter Settings   | Max Guaranteed Blocked Pulse Width Min Guaranteed Pass Pulse Width   | Max Guaranteed Blocked Pulse Width Min Guaranteed Pass Pulse Width   |         |        |
|-----------------------|-----------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|---------|--------|
| Pulse Width Equivalent (                       | Frequency t (1)                       | Pulse Width Equivalent (                                                                      | Frequency t (1)                                                                      | Pulse Width Equivalent (         | Frequency t (1)        |
| No filter             | 1 MHz                 | N/A                                                                  | N/A                                                                  | 250 ns  | 2 MHz  |
| 10 µs                 | 50 kHz                | 7.4 µs                                                               | 67.5 kHz                                                             | 25 µs   | 20 kHz |
| 500 µs                | 1 kHz                 | 370 µs                                                               | 1.35 kHz                                                             | 1.25 ms | 400 Hz |
| 5 ms                  | 100 Hz                | 3.7 ms                                                               | 135 Hz                                                               | 12.5 ms | 40 Hz  |

(1) Equivalent frequency assumes a perfect 50% duty cycle and are for reference purposes only. Hence, the no-filter setting is guaranteed to pass 4 MHz even though the module's maximum is 1 MHz. This lets the sensor and wiring to attenuate the pulse to 25% duty cycle while the module maintains pulse recognition.

| Nom Filter Settings   | Nom Filter Settings   | Max Guaranteed Blocked Pulse Width Min Guaranteed Pass Pulse Width   | Max Guaranteed Blocked Pulse Width Min Guaranteed Pass Pulse Width   |         |          |
|-----------------------|-----------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|---------|----------|
| Pulse Width Equivalent (                       | Frequency t (1)                       | Pulse Width Equivalent (                                                                      | Frequency t (1)                                                                      | Pulse Width Equivalent (         | Frequency t (1)          |
| No filter             | 250 kHz               | 0.83 µs                                                              | 600 kHz                                                              | 2.5 µs  | 200 kHz  |
| 18.5 µs               | 27 kHz                | 12.3 µs                                                              | 40.5 kHz                                                             | 28.6 µs | 17.5 kHz |
| 715 µs                | 700 Hz                | 495 µs                                                               | 1.01 kHz                                                             | 1.25 ms | 400 Hz   |
| 7.1 ms                | 70 Hz                 | 4.95 ms                                                              | 101 Hz                                                               | 12.5 ms | 40 Hz    |

(1) Equivalent frequency assumes a perfect 50% duty cycle and are for reference purposes only. Hence, the no-filter setting is guaranteed to pass 4 MHz even though the module's maximum is 1 MHz. This lets the sensor and wiring to attenuate the pulse to 25% duty cycle while the module maintains pulse recognition.

## IMPORTANT

The built-in filters are simple, averaging, low-pass filters. They are designed to block noise pulses of width equal to the values presented in Table Filter Pulse Width and Frequency. Applying full amplitude, 50% duty cycle signals that are of frequency above the selected filter's threshold frequency can result in an average value signal of sufficient amplitude to turn the input on. A transition from no input to the full amplitude, 50% duty cycle signal (or back to no signal) can result in inadvertent input transitions.

(1) Low-pass filters block frequencies above the threshold frequency.

## Operational Mode Selection

A count channel's operational mode configuration selection determines how the A and B inputs cause a counter channel to increment or decrement. The six available mode selections are the following:

- Pulse/External Direction Input
- Pulse/Internal Direction Input
- Up and Down Pulse Input
- X1 Quadrature Encoder Input
- X2 Quadrature Encoder Input
- X4 Quadrature Encoder Input

## IMPORTANT

The operational mode selection is limited by the number of counters selected.

- With two counters selected, Counters 0 and 1 can be assigned any operational mode.
- With three counters selected, Counter 0 can be assigned any mode, but Counters 1 and 2 can only be configured as pulse/internal direction.
- With four counters selected, all counters must be configured for the pulse/internal direction mode.

See Figure 2 on page 19 for the operational modes available for the counters, based on the number of counters configured.

## Direction Inhibit and Direction Invert Output Control Bits

These bits apply to all of the counter modes.

TIP

When set, the Direction Inhibit bit disables any physical input from affecting count direction.

When set, the Direction Invert bit changes the direction of the counter in all operational modes.

When Direction Inhibit is set, then Direction Invert is the direction.

## Pulse/External Direction Mode Selection

In this mode, the B input controls the direction of the counter, as shown in Figure 3. If the B input is low (0), the counter increments on the rising edges of input A. If the input B is high (1), the counter decrements on the rising edges of input A.

TIP

Two Output Control bits let you modify the operation of the B input from your control program or during configuration. The Direction Inhibit bit, when set (1), disables the operation of the B input.

The Direction Invert bit, when set (1), reverses the operation of the B input, but only if the Direction Inhibit bit is not set. If the Direction Inhibit bit is set, then the Direction Invert bit controls counter direction:

- When the Direction Inhibit bit is set (1) and Direction Invert = 0, count direction is up (forward).
- When the Direction Inhibit bit is set (1) and Direction Invert = 1, count direction is down (reversed).

Figure 3 - Pulse/External Direction Mode (direction inhibit = 0, direction invert = 0)

<!-- image -->

Table 2 - Pulse External Direction Counting

| Direction Invert Bit   |         | Input A (count) Input B (direction) Change in Count Value   |
|------------------------|---------|-------------------------------------------------------------|
| 0 0                    |        | 0 or open 1                                                 |
| 0 0                    |        | 1 -1                                                        |
| 0 0                    | 0, 1,  | Don’t care 0                                                |
| 0 1                    |        | 0 or open -1                                                |
| 0 1                    |        | 1 1                                                         |
| 0 1                    | 0, 1,  | Don’t care 0                                                |
| 1 0                    |        | 0 or open 1                                                 |
| 1 0                    |        | 1 1                                                         |
| 1 0                    | 0, 1,  | Don’t care 0                                                |
| 1 1                    |        | 0 or open -1                                                |
| 1 1                    |        | 1 -1                                                        |
| 1 1                    | 0, 1,  | Don’t care 0                                                |

See Direction Inhibit and Direction Invert Output Control Bits on page 21 for more information.

## Pulse/Internal Direction Mode Selection

When the Pulse/Internal Direction mode is selected, the status of the Direction Invert bit, as controlled by the user program, determines the direction of the counter. The counter increments on the rising edge of the module's A input when the Direction Invert bit is reset (0). The counter decrements on the rising edge of the A input when the Direction Invert bit is set (1).

Table 3 - Pulse Internal Direction Counting - Counters 0 and 1

| Direction Inhibit Bit   | Direction Invert Bit   | Input A (count) Input B Change in Count   | Value         |
|-------------------------|------------------------|-------------------------------------------|---------------|
| Don’t care 0            |                        |                                          | Don’t care 1  |
| Don’t care 0            |                        | 0, 1,                                    | Don’t care 0  |
| Don’t care 1            |                        |                                          | Don’t care -1 |
| Don’t care 1            |                        | 0, 1,                                    | Don’t care 0  |

Table 4 - Pulse Internal Direction Counting - Counters 2 and 3

| Direction Inhibit Bit   | Direction Invert Bit   |                         |    |   Input A Input B (count) Change in Count Value |
|-------------------------|------------------------|-------------------------|----|-------------------------------------------------|
|                         |                        | Don’t care 0 Don’t care |   |                                               1 |
|                         |                        | Don’t care 0, 1,       |    |                                               0 |
|                         |                        | Don’t care 1 Don’t care |   |                                              -1 |
|                         |                        | Don’t care 0, 1,       |    |                                               0 |

## Up and Down Pulses Mode Selection

In this mode, the counter channel increments on the rising edge of pulses applied to input A and decrements on the rising edge of pulses applied to input B. When set, the Direction Inhibit bit causes both A and B to increment. When set, the Direction Invert bit causes B to increment and A to decrement. When the Direction Invert and Direction Inhibit bits are both set, both A and B decrement.

TIP When both inputs transition simultaneously or near simultaneously, the net result is no change to the count value.

Figure 4 - Up and Down Pulse Mode (direction inhibit = 0, direction invert = 0)

<!-- image -->

Table 5 - Up and Down Counting

| Direction Invert Bit   | Input A (count) Input B (direction) Change in   |   Count Value |
|------------------------|-------------------------------------------------|---------------|
| 0 0                    |   0, 1,                                       |             1 |
| 0 0                    | 0, 1,                                         |            -1 |
| 0 0                    |                                               |             0 |
| 0 1                    |   0, 1,                                       |            -1 |
| 0 1                    | 0, 1,                                         |             1 |
| 0 1                    |                                               |             0 |
| 1 0                    |   0, 1,                                       |             1 |
| 1 0                    | 0, 1,                                         |             1 |
| 1 0                    |                                               |             0 |
| 1 1                    |   0, 1,                                       |            -1 |
| 1 1                    | 0, 1,                                         |            -1 |
| 1 1                    |                                               |             0 |

## X1 Quadrature Encoder Mode Selection

In this mode, when a quadrature encoder is attached to inputs A and B, the count direction is determined by the phase relation of inputs A and B. If A leads B, the counter increments. If B leads A, the counter decrements. In other words, when B is low, the count increments on the rising edge of input A and decrements on the falling edge of input A. If B is high, all rising transitions on input A are ignored. The counter changes value only on one edge of input A as shown in Figure 5.

TIP

When both A and B transition at the same time, instead of in the defined 90° phase separation, the quadrature signal is invalid.

For more information see Direction Inhibit and Direction Invert Output Control Bits on page 21 and their effect on Quadrature signals on page 27 .

Figure 5 - Quadrature Encoder Modes (direction inhibit = 0, direction invert = 0)

<!-- image -->

## X2 Quadrature Encoder Mode Selection

The X2 Quadrature Encoder mode operates much like the X1 Quadrature Encoder except that the resolution is doubled as shown in Figure 5 on page 26 .

## X4 Quadrature Encoder Mode Selection

The X4 Quadrature Encoder mode operates much like the X1 Quadrature Encoder except that the resolution is quadrupled, as shown in Figure 5 on page 26 .

Figure 6 shows how Direction Inhibit and Direction Invert affect the counter.

Figure 6 - Operation Using Various Direction Inhibit and Direction Invert Settings

<!-- image -->

## Input Frequency

## Counter Types

Maximum input frequency is determined by the input configuration as shown in the table.

| Input Configuration  Input Frequency 1769-HSC Module   | Input Frequency Packaged Controller   |
|--------------------------------------------------------|---------------------------------------|
| X4 Quadrature encoder 250 kHz                          | 250 kHz                               |
| X2 Quadrature encoder 500 kHz                          | 250 kHz                               |
| All other configurations 1 MHz                         | 250 kHz                               |

Each of the four possible counters can be configured to stop counting and set a flag at its limits (linear counter) or to rollover and set a flag at its limits (ring counter). A counter's limits are programmed by the CtrnMaxCount and CtrnMinCount words in the module's configuration array. Both types are described below.

## Linear Counter

Figure 7 illustrates linear counter operation. In linear operation, the current count (Ctr[n].CurrentCount) value remains between, or equal to, the user-programmed minimum count (CtrnMinCount) and maximum count (CtrnMaxCount) values. If the Ctr[n].CurrentCount value goes above (&gt;) or below (&lt;) these values, the counter stops counting, and an overflow/underflow bit is set. The overflow/underflow bits can be reset using the CtrnResetCounterOverflow and CtrnResetCounterUnderflow bits.

Figure 7 - Linear Counter Diagram

<!-- image -->

Pulses are not accumulated in an overflow/underflow state. The counter begins counting again when pulses are applied in the proper direction. For example, if you exceed the maximum by 1000 counts, you do not need to apply 1000 counts in the opposite direction before the counter begins counting down. The first pulse in the opposite direction decrements the counter.

## Modifying Count Value

## Ring Counter

Figure 8 demonstrates ring counter operation. In ring counter operation, the current count (Ctr[n].CurrentCount) value changes between user-programmable minimum count (CtrnMinCount) and maximum count (CtrnMaxCount) values. If, when counting up, the counter reaches the CtrnMaxCount value, it rolls over to the CtrnMinCount value upon receiving the next count and sets the overflow bit. If, when counting down, the counter reaches the CtrnMinCount value, it rolls under to the CtrnMaxCount value upon receiving the next count and sets the underflow bit. These bits can be reset using the CtrnResetCounterOverflow and CtrnResetCounterUnderflow bits.

Figure 8 - Ring Counter Diagram

<!-- image -->

The count value (Ctr[n].CurrentCount) can be stored, reset, or preset using the Z-input, CtrReset bit in the configuration array, control bits in the output array, or overwritten using a Direct Write command.

Table 6 - Available Z Functions

| Setting For function                                                                     |
|------------------------------------------------------------------------------------------|
| Store(1) On rising edge of Z, store count in the Stored Count input word                 |
| Hold While Z = 1, hold counter at its current value                                      |
| Preset/Reset On rising edge of Z, preset the count value to the value in the preset word |

## IMPORTANT

Because only the Z-inputs are used for external gating and presetting, these functions are not available for Counters 2 and 3, which do not have Z-inputs. All options are always available for Counters 0 and 1, regardless of input operational mode.

## Counter Enable/Disable

The counter can be enabled or disabled using the CtrnEn control bit. Be aware that disabling the counter does not inhibit any current count loading functions (for example, preset or direct write) or any Z function.

## Z Input Functions

There are three Z input functions: store, gate, and Z preset.

Store

The Z-input can be used to capture the current count value even when the counter is counting at full 1 MHz speed.

Gate

The Z-inputs can be used to gate (hold) the counter at its current value regardless of incoming A or B inputs. A gating function is typically one that lets pulses reach the counter (gate open) or not (gate closed).

Z Preset

Preset can be programmed to occur based on the actions of the Z-input signal.

## Inhibit and Invert

The Z-input signals can be inverted and/or inhibited, depending on the user configuration of the CtrnZInvert and CtrnZInhibit output control bits. If the signal is inhibited, the invert bit is the Z signal for the actions described above.

For an explanation of those bits, see Z Inv - Z Invert (CtrnZInvert) on page 93 and Z Inh - Z Inhibit (CtrnZInhibit) on page 93 .

## Direct Write

You can arbitrarily change the current count value (Ctr[n].CurrentCount) to the direct write control value (Range12To15[n].HiLimOrDirWr). This ability applies to ranges 12…15. The direct write value takes effect when the Load Direct Write bit (Range12To15[n].LoadDirectWrite) transitions from 0 to 1.

If you attempt to preset and load direct write to a counter at the same time, only the preset (CtrnPreset) will take effect.

## Preset/Reset

Preset sets the counter to a zero or non-zero value you define. Reset the counter by setting this value (CtrnPreset) to zero.

## Counter Reset

Refer to page 73 in Chapter 4 for details on performing a default counter reset for the CMX 5370 L2 packaged controller and the 1769-HSC/B module only. The L23E packaged controller and the 1769-HSC/A module do not have this functionality.

## Soft Preset

Preset can be programmed to occur by setting the appropriate output control bits via your control program. Setting the CtrnSoftPreset bit in the output array causes the counter to be preset, changing the count to the value in CtrnPreset.

## Z Preset

Preset can be programmed to occur based on the actions of the Z-input signal.

## Autopreset

If the module is configured such that CtrnMaxCount &lt; Ctr[n].CurrentCount or CtrnMinCount &gt; Ctr[n].CurrentCount, then the module will automatically change Ctr[n].CurrentCount to the CtrnPreset value and set the CtrnPresetWarning bit.

## Rate/Timer Functionality

To ensure maximum accuracy, the module offers two different methods to calculate the rate.

- Per Pulse = 1/Pulse Interval
- Cyclic = Number of Pulses/User-defined Time Interval

You select the method used, depending upon the pulse speed as defined below. These are continuously available regardless of input operational mode.

IMPORTANT

The Rate/Timer Functionality information does not apply to the L23E packaged controller.

## Pulse Interval Rate Calculation Method

<!-- image -->

The pulse interval rate method is very accurate for slower rates, that is, when the pulse interval (or time between pulses) is large compared to the system clock timer (1 μs). A timer is used to measure the time between two successive pulses. The inverse of this value is the pulse interval rate. The pulse interval rate cannot be read directly from the module. It needs to be calculated. The calculation can be performed in the user control program.

This method is not as accurate for higher pulse rates. When the pulse interval shrinks, two factors can distort the per pulse calculation. If the pulse interval is close to the measuring timer's clock frequency, 1 MHz, the granularity of the time increments has a greater effect on rate inaccuracy. In addition, the rate can be calculated many times over the course of a single backplane scan. As a result, the rate data obtained at a backplane scan is only that of the very last pair of pulses and disregards the other rate calculations that have occurred during that interval. This can result in rate inaccuracy if the pulses are unevenly spaced.

## Cyclic Rate Calculation Method (current rate)

The module continuously calculates rates for each of its four possible counters, regardless of operational mode (for example, up/down count). The 32-bit signed integer rate from each counter is reported in the Ctr[n].CurrentRate words of the input array.

In this method, the rates are calculated at the end of a counter's configured cycle time. This is configured via the CtrnCyclicRateUpdateTime configuration word/menu. Valid entries are 1…32,767 ms. The number of net counts, net change in Ctr[n].CurrentCount, during that period is converted into a rate value, providing an average pulse rate.

The generalized rate calculation is Rate =  count/  time.

| IMPORTANT   | The rate calculation is based on net counts. If a counter goes up 500 counts and down 300 counts, the net count is 200. Therefore, changes in direction and speed affect the Ctr[n].CurrentRate value.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The cyclic method is better suited to high pulse rates.

## Hysteresis Detection and Configuration

Because physical vibration can cause an encoder to generate pulses that you do not wish to consider as valid motion, a hysteresis value is used to eliminate a certain number of pulses in either direction as vibration-generated. These pulses are not used to calculate the Ctr[n].CurrentRate value. You program the minimum number of counts that are considered to be valid motion, using the CtrnHysteresis configuration word/menu. If the change in counts over the update time cycle is equal to or less than the minimum number of programmed counts, the Ctr[n].CurrentRate is reported as zero.

This concept is not used to alter actual count values.

| IMPORTANT   | Hysteresis does not depend on the direction of the change in count. Therefore, creeping, a slow change in count in one direction only, can also be reported as zero frequency when it falls below the hysteresis threshold.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Scalar

You can configure the CtrnScalar value to scale or convert the raw rate value to application-specific information, such as RPM (Revolutions Per Minute). Setting CtrnScalar to 1 leaves the rate value in cycles per second (Hertz).

The actual rate equation is the following.

<!-- formula-not-decoded -->

TIP

To configure the Ctr[n].CurrentRate value to show an RPM value, set CtrnScalar to (counts per revolution)/60.

For example, where Ctr0CyclicRateUpdateTime = 80, the encoder has 360 counts per revolution, and the change in Ctr[0]. CurrentCount is 96.

<!-- formula-not-decoded -->

```
60 sec/min RPM = 80 Cyclic Rate Update Time x 360 counts/revolution 1000 Cyclic Rate Update Time/sec x 96 counts 60 sec/min = 200 RPM
```

## Rate Valid

The Ctr[n].RateValid bit indicates calculation integrity. When the bit is set, it indicates that the accompanying Ctr[n].CurrentRate value is accurate.

The Ctr[n].RateValid bit is reset when the overflow or underflow events have occurred, that is, at rising edges of Ctr[n].Overflow or Ctr[n].Underflow bits. It also happens when the count is abruptly modified via a preset (CtrnSoftPreset, CtrnCtrPresetWarning or Z based preset event) or direct write (Range12To15[n].LoadDirectWrite). When this occurs, the Ctr[n].CurrentRate value is frozen at the last known good value so that effects of erroneous rates will not propagate to range comparisons. The value remains frozen until the current cycle time plus one more cycle time are elapsed (this can be up to twice the CtrnCyclicRateUpdateTime). If the overflow/underflow occurrence lasts for more than one cycle time, the value is frozen that entire time plus up to two more cycle times.

Ensure that another overflow/underflow does not happen during this recovery time. The rate will remain invalid until a full update time has occurred with no such events. If the Ctr[n].RateValid bit is seldom or never set, the CtrnMinCount and CtrnMaxCount values can be configured too close to each other.

## Rate Method Selection

By knowing when to use each method, an optimal rate determination can be made.

TIP Fractional rates are not reported by the module, but can be calculated from Ctr[n].PulseInterval in your control program.

Use the following information to choose the appropriate calculation method. In general, consider the effect of having the count off by ±1 in each method at frequencies of interest to see if the resulting inaccuracy is acceptable.

## Per Pulse Method Example

If the frequency of interest has 100 counts (of the 1 μs clock) between pulses, an error of 1 count results in a 1-in-100, or 1%, error. If there are 1000 counts between pulses, then the error is 1-in-1000, or 0.1%. Error for a variety of pulse values is shown below.

Table 7 - Per Pulse Errors

| Actual 1 µs Internal ( Internal Pulses(1)   | Reported Pulses Real Frequency Reported Frequency % Error   |
|---|-------------------------------------------------------------|
|   | 2 1 500 kHz 1 MHz 100%                                      |
|   | 9 10 111 kHz 100 kHz 11.1%                                  |
|   | 101 100 9.901 kHz 10.000 kHz 1.00%                          |
|   | 1001 1000 999 Hz 1000 Hz 0.10%                              |
|   | 9999 10,000 100.01 Hz 100.00 Hz 0.010%                      |
|   | 99,999 100,000 10.00010 Hz 10.00000 Hz 0.001%               |

(1) 1.9999 can be rounded to 2 and so on.

## Cyclic Method

Because the update time is programmable, there is more flexibility in choosing the correct fit when using the Cyclic Method.

Error estimates are shown below for a variety of update times.

Table 8 - Maximum Cyclic Rate Errors

| CyclicRateUpdate Time x Scalar   |                                           |
|----------------------------------|-------------------------------------------|
| CyclicRateUpdate Time x Scalar   | 100 Hz 1 kHz 10 kHz 100 kHz 1 MHz         |
|                                  | 1 N/A N/A 20.02% 2.011% 0.210%            |
|                                  | 10 N/A 20.11% 2.020% 0.210% 0.030%        |
|                                  | 100 20.01% 2.110% 0.220% 0.031% 0.012%    |
|                                  | 1000 3.010% 0.310% 0.040% 0.013% 0.010%   |
|                                  | 10,000 1.210% 0.130% 0.022% 0.011% 0.010% |

## Output Control

All 16 outputs can be controlled by any of the four counters or by the user's control program, via the output mask function. Output states are determined by count, rate (not supported in packaged controller), ranges, mask configuration data, overcurrent status, and safe state settings and conditions.

The 16 outputs are made up of four real (physical) outputs and 12 virtual outputs. The status of the real and virtual outputs is available to the user program. The real outputs are electronically protected from overloads.

## IMPORTANT

To turn outputs on, you must use both the Output On Mask and the Output Off Mask.

## Masks

You can use an Output On Mask or an Output Off Mask.

## Output On Mask

Using the Output On Mask, all of the module's outputs can be turned on directly by the user control program, like discrete outputs. A bit that is set in the mask turns on the corresponding real or virtual output.

## Output Off Mask

The Output Off Mask has veto power over any output. It can turn any or all of the module's outputs off. When a bit in this mask is set to 0, the output will be turned off. Each bit is logically ANDed with the Output On Mask and masks of active and enabled ranges. If the bit in this mask is set to 1, the output can be turned on or off by the ranges, or the Output On Mask. The final result is available as the Readback.n bit.

## Ranges

For the 1769-HSC module and the embedded HSC in the CMX 5370 L2 packaged controllers, up to 16 dynamically configurable ranges are available. Ranges activate outputs based on the current count value or the current rate value. Each range is programmed with a type, counter number, two limit values, an invert bit, and an output mask.

For the embedded HSC in the L23E packaged controller, up to four dynamically configurable ranges are available. Ranges activate outputs based on the current count value. Each range is programmed with a counter number, two limit values, an invert bit, and an output mask.

Each range is programmed with high and low limits for the chosen value. The range's invert bit indicates whether the range is active between or outside the range limits. When the chosen value fulfills the configuration parameters, the range is active as indicated in the input array. When a range is active and enabled (RangeEn.n = 1), the range turns on all outputs indicated by the Range Output Mask except those that are prevented from being enabled by the other factors such as Output Off Mask or Overcurrent. The status of a range is provided by the range active status word, where 1 equals range active and zero equals inactive.

TIP Ranges can be disabled while the module is running using the RangeEn.n bit in the output file. However, even a disabled range will report when it is active or not. For example, an unprogrammed range has limits of 0, and points to the Ctr[0].CurrentCount value. If this value is 0, that range is reported as active.

## Count Range

In a non-inverted count range, the outputs are active if the count value is within the user-defined range. In an inverted count range, the outputs are active if the count value is outside the user-defined range. Valid limits for the range are -2…2 billion regardless of programmed minimum and maximum values.

Figure 9 shows all ranges referring to one counter. The module is capable of individually assigning each range to any counter. Each counter can also have a combination of count and rate ranges.

Figure 9 - Count Range Example

<!-- image -->

Table 9 - Count Range Example Values

| Range   | Range Type (1)   | Range Low Limit Range High Limit Range Invert Bit      | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                                                             | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   | Outputs (2) (Range[n].OutputControl word) (Range[n].OutputControl word) Outputs Affected 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0   |
|---------|------------------|--------------------------------------------------------|---|-------------------------------------------------------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Range   | Range Type (1)   | 1 01 0 -7000 -5000 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 |   |                                                             |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|         |                  | 2 01 0 -1000 4500 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1  |   |                                                             |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|         |                  | 3 01 0 -4000 3000 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 2  |   |                                                             |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|         |                  |                                                        |   | 4 01 0 -9000 9000 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 and 3 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |

## Rate Range

IMPORTANT The Rate Range information does not apply to the packaged controller.

In a non-inverted rate range, the outputs are active if the rate measurement is within the user-defined range. In an inverted rate range, the outputs are active if the rate measurement is outside the user-defined range. The input rate can be up to 1 MHz in either direction.

Figure 10 shows all ranges referring to one counter. The module is capable of individually assigning each range to any counter. Each counter can also have a combination of count and rate ranges.

Figure 10 - Rate Range Example

<!-- image -->

Table 10 - Rate Range Example Values

| Range   | Range Counter Number Range Type(1)  (1)   | Range Low Limit Range High Limit Range Invert Bit   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs Affected                        | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   | Outputs (2) (Range[n].OutputControl word)   |
|---------|-------------------------------------------|-----------------------------------------------------|---------------------------------------------|---------------------------------------------|-----------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|---------------------------------------------|
| Range   | Range Counter Number Range Type(1)  (1)   | Range Low Limit Range High Limit Range Invert Bit   |                                             | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0       | Outputs Affected                        |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |
|         |                                           | 1 00 1 -7000 -5000 0                                |                                             | 00000000000000010                           |                                         |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |
|         |                                           | 2 00 1 -1000 4500 0                                 |                                             | 00000000000000101                           |                                         |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |
|         |                                           | 3 00 1 -4000 3000 0                                 |                                             | 00000000000001002                           |                                         |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |
|         |                                           | 4 00 1 -20,000 20,000 1                             |                                             |                                             | 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 and 3 |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |                                             |

## Overcurrent

If the module detects a real output point overcurrent condition, it reports it to the input file and turns off that output. You can also program the module to latch each of the four real outputs off, emulating a physical fuse, or to automatically reset. The 12 virtual outputs do not have this function.

When the OvercurrentLatchOff bit is set and an overcurrent situation occurs, even momentarily, the associated real output is latched off until the ResetBlownFuse bit transitions from 0 to 1.

If the OvercurrentLatchOff bit is reset and an overcurrent situation occurs, the output turns off for 1 second and is then retried (auto-reset). The module continues to attempt to turn the output back on until the overcurrent situation is no longer detected and the output is successfully turned back on.

## IMPORTANT

The outputs will be on momentarily while they are retried. The length of time they are on depends on the magnitude of the load.

## Safe State Control

The 1769-HSC module combines the Hold Last State and User-defined Safe State options with a safe-state run alternative that lets the module to continue to control outputs under program or fault states (1) . These Safe State options are not available in the packaged controllers.

Only the physical outputs are affected by safe state settings and conditions. Virtual outputs, inputs, and counting are not affected by program or fault states.

## Hold Last State (HLS)

This condition applies depending on the mode of the controller. When the hold last state option is set, the module holds the outputs at the state they were at just before the control system transitioned from Run to Program or Run to Fault.

HLS sets the module according to the values configured for Program mode (described on page 76) and Output Fault mode (described on page 77).

User-defined Safe State (UDSS)

In this configuration, the module sets the outputs to a user-defined safe state when the control system transitions from Run to Program or Run to Fault.

UDSS sets the module according to the values configured for Output Program Value (described on page 77) and Output Fault Value (described on page 78).

(1) The module continues to update the input array and count inputs in all modes. The operation of the outputs will vary according to mode, configuration, and the capabilities of the controller or bus master.

Program State Run (PSR)

Program State Run lets you specify that the output should continue to be controlled by the module as if it were in the Run state. That is, events on the module or changes in the output image will affect the physical outputs without regard to the Program\_HLS or UDSS state indicated. When this bit is set, the corresponding OutnProgramMode and OutnProgramValue bits are ignored.

PSR sets the module according to the value configured for Output Program State Run, as described on page 76 .

<!-- image -->

ATTENTION: Selecting this option lets outputs change state while ladder logic is not running. You must take care to assure that this does not pose a risk of injury or equipment damage when selecting this option.

## IMPORTANT

The prescan initiated by some controllers could have an effect on the outputs. To overcome any changes in physical output states caused by this, retentive output instructions (for example, latch or unlatch) should be used when bit manipulations are done on the output image of this module in ladder logic.

This applies to a wide range of bits when Program State Run is selected, because presetting a counter, enabling a range, changing a mask, and changing module configuration array settings can cause ranges and outputs to change state.

## Fault State Run (FSR)

Similar to Program State Run, Fault State Run lets you specify, on a bit basis, that the output should continue to be controlled by the module as if it were Run state. That is, events on the module or changes in the output image will affect the physical outputs without regard to the Fault\_HLS or UDSS state indicated. When this bit is set, the corresponding Fault mode and fault value bits are ignored.

FSR sets the module according to the value configured for Output Fault State Run, as described on page 77 .

<!-- image -->

ATTENTION: Selecting this option lets outputs change state while ladder logic is not running. You must take care to assure that this does not pose a risk of injury or equipment damage when selecting this option.

## IMPORTANT

The prescan initiated by some controllers can have an effect on the outputs. To overcome any changes in physical output states caused by this, use retentive output instructions (for example, latch or unlatch) when bit manipulations are done on the Output image of this module in ladder logic.

This applies to a wide range of bits when Fault State Run is selected, because presetting a counter, enabling a range, changing a mask, and changing configuration array settings can cause ranges and outputs to change state.

Program to Fault Enable (PFE)

The ProgToFaultEn bit lets you select which data value (Program Value or Fault Value) to apply to the output when the Output State Logic state Prog\_HLS changes to indicate Fault\_HLS.

If PFE is 0, the module leaves the Program value applied. If PFE is set to 1, the Fault value is applied.

TIP

If the module is in a safe state such as Program or Fault which is configured to turn an output ON and excessive current is drawn from the output, the output will still turn off according to the programmed OverCurrentLatchOff bit configuration.

The module's Default Safe State configuration is all zeros, resulting in the following:

- Program State = UDSS
- Program Value = OFF
- Program State Run = No
- Fault State = UDSS
- Fault Value = OFF
- Fault State Run = No
- PFE = leave program value applied

## Output Control Example

The following example illustrates the module's output control flow. The following conditions are reflected in the Output Control Example on page 44:

- Range 0 is enabled and active.
- Range 1 is disabled.
- Range 2 is enabled but not active.
- An overcurrent condition exists on real output 3.
- OvercurrentLatchOff is set.
- The system is in Run mode.

Table 11 - Output Control Example

| Output Parameter Mask Information   | Logical Operation Result (1)   |
|-------------------------------------|--------------------------------|

Table 11 illustrates the step-by-step logical operations that are performed to determine the final output state. For example, Range 1 values do not affect the output because Range 1 is disabled, and the Output Off Mask causes some of the outputs to change to zero because it takes priority over the range masks.

The output parameters shown have been discussed in the previous sections.

## Readback/Loopback

The Readback/Loopback function is the feedback of the module's outputs via its input array. This 16-bit image includes both real (4) and virtual (12) outputs.

If the module's output is OFF due to overcurrent, both the Overcurrent status flag and the Readback bit will indicate the condition being 1 and 0, respectively. Conversely, should the output be ON due to any module control, such as UDSS, this will be indicated by Readback.

<!-- image -->

## Installation and Wiring

This chapter explains how to install and wire the 1769-HSC module.

| Topic                                 | Page   |
|---------------------------------------|--------|
| Power Requirements                    | 47     |
| General Considerations                | 47     |
| System Assembly                       | 49     |
| Mount the Module                      | 50     |
| Replace the Module within a System 53 |        |
| Field Wiring Connections              | 54     |

## IMPORTANT

For information about installing and wiring the packaged controllers, refer to the CompactLogix Packaged Controller Installation Instructions, publication 1769-IN082 .

## ATTENTION: Environment and Enclosure

This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment is considered Group 1, Class A industrial equipment according to IEC/CISPR 11. Without appropriate precautions, there can be difficulties with electromagnetic compatibility in residential and other environments due to conducted and radiated disturbances.

This equipment is supplied as open-type equipment. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to prevent or minimize the spread of flame, complying with a flame spread rating of 5VA, V2, V1, V0 (or equivalent) if non-metallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain additional information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for additional installation requirements
- NEMA Standard 250 and IEC 60529, as applicable, for explanations of the degrees of protection provided by enclosures

<!-- image -->

## North American Hazardous Location Approval

<!-- image -->

| The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | The following information applies when operating this equipment in hazardous locations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Informations sur l’utilisation de cet équipement en environnements dangereux.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local Authority Having Jurisdiction at the time of installation. | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. | Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | EXPLOSION HAZARD •  Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous. •  Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product. •  Substitution of any component may impair suitability for Class I, Division 2. •  If this product contains batteries, they must only be changed in an area known to be nonhazardous.     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | RISQUE D’EXPLOSION •  Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher l'équipement. •  Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher les connecteurs. Fixer tous les connecteurs externes reliés à cet équipement à l'aide de vis, loquets coulissants, connecteurs filetés ou autres moyens fournis avec ce produit. •  La substitution de tout composant peut rendre cet équipement inadapté à une utilisation en environnement de Classe I, Division 2. •  S'assurer que l'environnement est classé non dangereux avant de changer les piles.                                                 |

<!-- image -->

<!-- image -->

<!-- image -->

## ATTENTION: Prevent Electrostatic Discharge

This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Store the equipment in appropriate static-safe packaging when not in use.

## WARNING: Hazardous Location Enclosure

When used in a Class I, Division 2, hazardous location, this equipment must be mounted in a suitable enclosure with proper wiring method that complies with the governing electrical codes.

## Power Requirements

## General Considerations

The modules receive power through the Compact bus interface from the 5V DC/24V DC system power supply. The maximum current drawn by the modules is shown in the table.

| Module Current Draw 5V DC   | 24V DC   |
|-----------------------------|----------|
| 425 mA                      | 0 mA     |

<!-- image -->

<!-- image -->

WARNING: When you insert or remove the module while backplane power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations.

By sure that power is removed or the area is nonhazardous before proceeding. Repeated electrical arcing causes excessive wear to contacts on both the module and its mating connector. Worn contacts can create electrical resistance that can affect module operation.

## WARNING: Removable Terminal Block (RTB) Under Power

When you connect or disconnect the removable terminal block (RTB) with field side power applied, an electrical arc can occur. This could cause an explosion in hazardous location installations.

Be sure that power is removed or the area is nonhazardous before proceeding.

Compact I/O is suitable for use in an industrial environment when installed in accordance with these instructions.

## Selecting a Location to Reduce Noise

Most applications require installation in an industrial enclosure to reduce the effects of electrical interference. The module is highly susceptible to electrical noise. Electrical noise coupled to the inputs will reduce the performance (accuracy) of the module.

Group your modules to minimize adverse effects from radiated electrical noise and heat. When selecting a location for a module, position the module away from the following:

- Sources of electrical noise, such as hard-contact switches, relays, and AC motor drives.
- Modules that generate significant radiated heat, such as the 1769-IA16 module. Refer to the module's heat dissipation specification.

In addition, route shielded, twisted-pair analog input and output wiring away from any high voltage I/O wiring.

## Protect the Circuit Board from Contamination

The printed circuit boards of the modules must be protected from dirt, oil, moisture, and other airborne contaminants. To protect these boards, we recommend installing the system in an enclosure suitable for the environment. Keep the interior of the enclosure should clean and the enclosure door closed whenever possible.

## Power Supply Distance

You can install as many modules as your power supply can support. However, the module has a power supply distance rating of four, which means that it can not be more than four modules away from the system power supply.

The illustration provides an example of determining power supply distance.

<!-- image -->

## System Assembly

The module can be attached to an adjacent controller, power supply, or I/O module. For mounting instructions, see Panel Mounting on page 50, or DIN Rail Mounting on page 52 .

To work with a system that is already mounted, see Replace the Module within a System on page 53 .

Refer to the illustration when assembling the Compact I/O system.

<!-- image -->

1. Disconnect the power.
2. Check that the bus lever of the module (A) is in the unlocked (fully right) position.
3. Use the upper and lower tongue-and-groove slots (B) to secure the modules together.
4. Move the module back along the tongue-and-groove slots until the bus connectors (C) line up with each other.
5. Use your fingers or a small screwdriver to push the bus lever back slightly to clear the positioning tab (D).
6. Move the module's bus lever fully to the left (E) until it clicks, making sure it's locked firmly in place.

<!-- image -->

ATTENTION: When attaching I/O modules, it is very important that the bus connectors are securely locked together to provide proper electrical connection.

7. Attach an end cap terminator (F) to the last module in the system by using the tongue-and-groove slots as before.
8. Lock the end cap bus terminator (G).

IMPORTANT A 1769-ECR right- or 1769-ECL left-end cap must be used to terminate the end of the serial communication bus.

## Mount the Module

Use these procedures to mount your module.

<!-- image -->

ATTENTION: During panel or DIN-rail mounting of all devices, be sure that all debris (metal chips, wire strands) is kept from falling into the module. Debris that falls into the module could cause damage at powerup.

## Minimum Spacing

Maintain spacing from enclosure walls, wireways, adjacent equipment, and so forth. Allow 50 mm (2 in.) of space on all sides for adequate ventilation, as shown.

<!-- image -->

## Panel Mounting

Mount the module to a panel by using two screws per module. Use M4 or #8 panhead screws. Mounting screws are required on every module.

<!-- image -->

ATTENTION: This product is intended to be mounted to a well-grounded mounting surface such as a metal panel. Additional grounding connections from the power supply's mounting tabs or DIN rail (if used) are not required unless the mounting surface cannot be grounded. Refer to Industrial Automation Wiring and Grounding Guidelines, Rockwell Automation publication 1770-4.1, for additional information.

Figure 11 - Compact I/O Module with CompactLogix Controller and Power Supply

<!-- image -->

Important: Hole spacing tolerance: ±0.04 mm (0.016 in.).

45198

Figure 12 - Compact I/O Module with MicroLogix 1500 Base Unit and Processor

<!-- image -->

Important: Hole spacing tolerance: ±0.04 mm (0.016 in.).

45199

Panel Mounting Procedure By Using Modules as a Template

This procedure lets you use the assembled modules as a template for drilling holes in the panel. Due to module mounting hole tolerance, it is important to follow these procedures:

1. On a clean work surface, assemble no more than three modules.
2. Using the assembled modules as a template, carefully mark the center of all module-mounting holes on the panel.
3. Return the assembled modules to the clean work surface, including any previously mounted modules.
4. Drill and tap the mounting holes for the recommended M4 or #8 screw.
5. Place the modules back on the panel, and check for proper hole alignment.
6. Attach the modules to the panel using the mounting screws.

TIP

If mounting more modules, mount only the last one of this group and put the others aside. This reduces remounting time during drilling and tapping of the next group.

7. Repeat steps 1 through 6 for any remaining modules.

## DIN Rail Mounting

The module can be mounted on the following DIN rails:

- EN 50 022 - 35 x 7.5 mm (1.38 x 0.3 in.)
- EN 50 - 35 x 15 mm (1.38 x 0.59 in.)
1. Before mounting the module on a DIN rail, close the DIN rail latches.
2. Press the DIN rail mounting area of the module against the DIN rail.

The latches will momentarily open and lock into place.

Figure 13 - DIN Rail Mounting Dimensions

<!-- image -->

| Dimension Height    |
|---------------------|
| A 118 mm (4.65 in.) |
| B 59 mm (2.325 in.) |
| C 59 mm (2.325 in.) |

## Replace the Module within a System

The module can be replaced while the system is mounted to a panel or DIN rail.

1. Remove power, referring to the Warning on page 47 .
2. Remove terminal block or disconnect input and/or output wiring from the module.
3. Remove the upper and lower mounting screws from the module (or open the DIN latches using a screwdriver).
4. On the module to be replaced and the right-side adjacent module (or end cap if the module is the last module in the bank), move the bus levers to the right (unlock) to disconnect the module from the adjacent modules.
5. Gently slide the disconnected module forward.

If you feel excessive resistance, make sure that you disconnected the module from the bus and that you removed both mounting screws (or opened the DIN latches).

TIP

It may be necessary to rock the module slightly from front to back to remove it, or, in a panel-mounted system, to loosen the screws of adjacent modules.

6. Before installing the replacement module, be sure that the bus lever on the right-side adjacent module is in the unlocked (fully-right) position.
7. Slide the replacement module into the open slot.
8. Connect the modules together by locking (fully-left) the bus levers on the replacement module and the right-side adjacent module or end cap.
9. Replace the mounting screws (or snap the module onto the DIN rail).
10. Replace the terminal block or connect the input and/or output wiring to the module.

## Field Wiring Connections

Consider these system wiring guidelines when wiring your system.

## General Guidelines

- Make sure the system is properly grounded.
- Input and output channels are isolated from the 1769 Compact bus. Input channels are isolated from one another; output channels are not.
- Shielded cable is required for high-speed input signals A, B, and Z. Use individually shielded, twisted-pair cable for lengths up to 300 m (1000 ft).
- Group this module and other low voltage DC modules away from AC I/O or high voltage DC modules.
- Route field wiring away from any other wiring and as far as possible from sources of electrical noise, such as motors, transformers, contactors, and AC devices.
- Routing field wiring in a grounded conduit can reduce electrical noise.
- If field wiring must cross AC or power cables, make sure that they cross at right angles.

## Terminal Block Guidelines

- For optimum accuracy, limit overall cable impedance by keeping cable as short as possible. Locate the module as close to input devices as the application permits.
- Tighten terminal screws with care. Excessive tightening can strip a screw.

## Grounding Guidelines

- This product is intended to be mounted to a well-grounded mounting surface, such as a metal panel. Additional grounding connections from the module's mounting tabs or DIN rail (if used) are required only when the mounting surface is non-conductive and cannot be grounded.
- Keep shield connection to ground as short as possible.
- Ground the shield drain wire at the 1769-HSC module, input end only.

Refer to the Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for additional installation requirements.

## Considerations for Reducing Noise

In high-noise environments, the 1769-HSC module inputs can accept 'false' pulses, particularly when using low frequency input signals with slowly sloping pulse edges. To minimize the effects of high frequency noise on low frequency signals, perform the following:

- Identify and remove noise sources.
- Route input cabling away from noise sources.
- Use your programming software to select low-pass filters on input signals. Filter values depend on the application and can be determined empirically.
- Use devices which output differential signals, such as differential encoders, to minimize the possibility that a noise source will cause a false input.

## Remove and Replace the Terminal Block

When wiring the module, you do not have to remove the terminal block. If you remove the terminal block, use the write-on label on the side of the terminal block to identify the module location and type.

<!-- image -->

To remove the terminal block, loosen the upper- and lower-retaining screws. The terminal block will back away from the module as you remove the screws. When replacing the terminal block, torque the retaining screws to 0.46 N·m (4.1 lb·in).

## Wire the Finger-safe Terminal Block

When wiring the terminal block, keep the finger-safe cover in place.

<!-- image -->

Follow these steps.

1. Loosen the terminal screws to be wired.
2. Route the wire under the terminal pressure plate.

You can use the bare wire or a spade lug. The terminals accept a 6.35 mm (0.25 in.) spade lug.

TIP

The terminal screws are non-captive. Therefore, it is possible to use a ring lug (6.35 mm (0.25 in.) maximum outside diameter with 3.53 mm (0.139 in.) minimum inside diameter) with the module.

3. Tighten the terminal screw making sure the pressure plate secures the wire. Recommended torque when tightening terminal screws is 0.68 N·m (6 lb·in).

TIP

If you need to remove the finger-safe cover, insert a screwdriver into one of the square, wiring holes and gently pry the cover off. If you wire the terminal block with the finger-safe cover removed, you will not be able to put it back on the terminal block because the wires will be in the way.

## Wire Size and Terminal Screw Torque

Each terminal accepts up to two wires with these restrictions.

| Wire Type   | Wire Size                                                           | Terminal Screw Torque   | Retaining Screw Torque   |
|-------------|---------------------------------------------------------------------|-------------------------|--------------------------|
|             | Solid Cu-90 °C (194 °F) 0.32... 2.1 mm 2  (22...14 AWG) 0.68 N•m    | (6 lb•in)               | 0.46 N•m (4.1lb•in)      |
|             | Stranded Cu-90 °C (194 °F) 0.32... 1.3 mm 2  (22...16 AWG) 0.68 N•m | (6 lb•in)               | 0.46 N•m (4.1 lb•in)     |

## Wire the Modules

After the module is properly installed, wire the modules by using this procedure. To provide proper operation and high immunity to electrical noise, always use shielded wire.

<!-- image -->

ATTENTION: To prevent shock hazard, care should be taken when wiring the module to signal sources. Before wiring any module, disconnect power from the system power supply and from any other source to the module.

Do not wire more than two conductors on any single terminal.

<!-- image -->

Follow these steps to wire your module.

1. At each end of the cable, strip some casing to expose the individual wires.
2. Trim the signal wires to 5 cm (2 in.) lengths, stripping about 5 mm (0.2 in.) of insulation away to expose the end of the wire.

<!-- image -->

ATTENTION: Be careful when stripping wires. Wire fragments that fall into a module could cause damage at powerup.

3. At the 1769-HSC module input end of the cable, twist the drain wire and foil shield together, bending them away from the cable, and apply shrink wrap, grounding the shield at this end.
4. At the other end of the cable, cut the drain wire and foil shield back to the cable and apply shrink wrap.
5. Connect the signal wires to the terminal block, connecting the other end of the cable to the input device.
6. Repeat steps 1 through 5 for each channel on the module.

## Terminal Door Label

A removable, write-on label is provided with the module. Remove the label from the door, mark the identification of each terminal with permanent ink, and slide the label back into the door. Your markings (ID tag) will be visible when the module door is closed.

## Terminal Block Wiring

The input and output terminals are shown below. Both inputs and outputs are isolated from the 1769 Compact bus.

<!-- image -->

45276

## Wire Diagrams

The following pages show wiring examples for a differential encoder, single-ended encoder, and discrete device.

Inputs

The module utilizes differential inputs. Therefore, two input terminals are required for each input point. For example, the A0+ and A0- terminals are required for input point A0. Each input point is isolated from other input points, the 1769 Compact bus, and the entire output terminal group.

The inputs are compatible with standard differential line driver output devices as well as single-ended devices such as limit switches, photo-eyes, and proximity sensors. Examples of differential and single-ended circuits are shown in Figure 14 and Figure 15 .

Figure 14 - Differential Encoder Wiring

<!-- image -->

Figure 15 - Single-ended Encoder Wiring

<!-- image -->

- (1) Refer to your encoder manual for proper cable type. The type of cable used should be twisted-pair, individually shielded cable with a maximum length of 300 m (1000 ft).
- (2) External resistors are required if they are not internal to the encoder. The pull-up resistor (R) value depends on the power supply value. The table below shows the maximum resistor values for typical supply voltages. To calculate the maximum resistor value, use the following formula:

<!-- formula-not-decoded -->

where:

R = maximum pull-up resistor value

VDC = power supply voltage

Vmin = 2.6V DC

Imin = 6.8 mA

|   Power Supply Voltage (V DC) | Pull-up Resistor Value (R), Max (1)   |
|-------------------------------|---------------------------------------|
|                             5 | 352                                  |
|                            12 | 1382                                 |
|                            24 | 3147                                 |

The minimum resistor (R) value depends on the current sinking capability of the encoder. Refer to your encoder's documentation.

Figure 16 - Discrete Device Wiring

<!-- image -->

- (1) External resistors are required if they are not internal to the sensor. The pull-up resistor (R) value depends on the power supply value. The table below shows the maximum resistor values for typical supply voltages. To calculate the maximum resistor value, use the following formula:

<!-- formula-not-decoded -->

where:

R = maximum pull-up resistor value

VDC = power supply voltage

Vmin = 2.6V DC

Imin = 6.8 mA

|   Power Supply Voltage (V DC) | Pull-up Resistor Value (R), Max (1)   |
|-------------------------------|---------------------------------------|
|                             5 | 352                                  |
|                            12 | 1382                                 |
|                            24 | 3147                                 |

The minimum resistor (R) value depends on the current sinking capability of the sensor. Refer to your sensor's documentation.

## Outputs

The four output terminals must be powered by a user-supplied external source. User-power range is from 5…30V DC. See the Output Specifications in Appendix A on page 124 .

There is no isolation between the outputs, but the outputs are isolated from the inputs and the 1769 Compact bus.

## Electronic Protection

The electronic protection of the 1769-HSC module has been designed to provide protection for current overload and short-circuit conditions. The protection is based on a thermal cut-out principle. In the event of a short-circuit or current overload condition on an output channel, that channel will turn off within milliseconds after the thermal cut-out temperature has been reached.

## Overcurrent Autoreset Operation

The module detects overcurrent situations and reports them to the backplane in the OutnOverCurrent bits of the input array. When the overcurrent condition is detected, the outputs are turned off.

The module can latch outputs off to emulate the behavior of a physical fuse. Use the OvercurrentLatchOff bit to enable or disable this feature. When the OvercurrentLatchOff bit is set and an overcurrent situation occurs (even momentarily) the physical output will be latched off until the ResetBlownFuse bit is cycled from off to on (rising edge triggered). During the latched off time, the Readback.n bit in the input array also shows that the output is off.

If the OvercurrentLatchOff bit is not set, the output will be turned off for 1 second and then be retried (if still directed to be on). Retries will repeat until the overcurrent situation is corrected.

The four physical outputs can be latched off only. The virtual outputs are not affected.

| IMPORTANT   | During the retry period, the physical output and the Readback.n bits will be on briefly (until the overcurrent causes them to shut off again). Take this into consideration and configure your system accordingly.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TIP         | Correct short-circuit and overload conditions as soon as possible. If short-circuit and overload conditions occur for extended periods, damage can occur.                                                            |

## Transistor Output Transient Pulses

The maximum duration of the transient pulse occurs when minimum load is connected to the output. However, for most applications, the energy of the transient pulse is not sufficient to energize the load.

<!-- image -->

ATTENTION: A transient pulse occurs in transistor outputs when the external DC supply voltage is applied to the output common terminals (for example, via the master control relay). The sudden application of voltage creates this transient pulse. This condition is inherent in transistor outputs and is common to solid state devices. A transient pulse can occur regardless of the controller having power. Refer to your controller's user manual to reduce inadvertent operation.

Figure 17 illustrates that the duration of the transient is proportional to the load current. Therefore, as the on-state load current increases, the transient pulse decreases. Power-up transients do not exceed the time duration shown below, for the amount of loading indicated, at 60 °C (140 °F).

Figure 17 - Transient Pulse Duration as a Function of Load Current

<!-- image -->

## Output Wiring

Basic wiring (1) of output devices (2) to the module is shown in Figure 18.

<!-- image -->

ATTENTION: Follow these guidelines:

- Miswiring of the module to an AC power source or applying reverse polarity will damage the module.
- Be careful when stripping wires. Wire fragments that fall into a module could cause damage at powerup. Once wiring is complete, make sure the module is free of all metal fragments.

Figure 18 - Output Device Wiring

<!-- image -->

45200

(1) Recommended Surge Suppression - The module has built-in suppression which is sufficient for most applications, however, for high-noise applications, use a 1N4004 diode reverse-wired across the load for transistor outputs switching 24V DC inductive loads. For additional details, refer to the Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .

(2) Sourcing Output - Source describes the current flow between the I/O module and the field device. Sourcing output circuits supply (source) current to sinking field devices. Field devices connected to the negative side (DC Common) of the field power supply are sinking field devices. Field devices connected to the positive side (+V) of the field supply are sourcing field devices. Europe: DC sinking input and sourcing output module circuits are the commonly used options.

## Configure the Module

<!-- image -->

## Module Configuration, Output, and Input Data

After installing the 1769-HSC module, you must configure it for operation by using the programming software compatible with the controller, such as RSLogix 500 or RSLogix 5000 software.

TIP

Normal counter configuration is done using programming software. In that case, it is not necessary to know the meaning of the bit location. However, some systems let the control program change configuration.

Information on programming the module by using specific controllers and software is contained in the following appendices.

| Controller                             | Software     | See                    |
|----------------------------------------|--------------|------------------------|
| CompactLogix Controller                | RSLogix 5000 | Appendix B on page 131 |
| MicroLogix 1500 Controller RSLogix 500 |              | Appendix C on page 141 |

The table describes the topics in this chapter.

| Topic Page              |
|-------------------------|
| Configure the Module 65 |
| Configuration Array 66  |
| Output Array 88         |
| Input Array 98          |

The module uses three arrays: configuration array, output array, and input array. You configure the module by establishing settings in the configuration and output arrays. The input array shows the data that the module sends to the controller.

| IMPORTANT   | Both the configuration array and output array settings affect the module configuration. Changing certain configuration parameters from defaults can necessitate changing other values to avoid configuration errors.   |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Configuration Array

The configuration array, which consists of 118 words (46 words for the packaged controller), lets you specify how the module's counters will function. The default value is all zeros with the exception of the following:

- NumberofCounters (see page 75)
- CtrnMaxCount (see page 78)
- CtrnMinCount (see page 79)
- CtrnScalar (see page 80)
- CtrnCyclicUpdateTime (see page 81)

TIP

Normal counter configuration is done using programming software. In that case, it is not necessary to know the bit location. However, some systems let the control program change configuration. Refer to your controller's documentation for details.

## IMPORTANT

When changing configuration values, verify that only valid configurations are created for the module. For example, changing NumberofCounters from its default of 1 to 0 requires that Ctr1MinCount and Ctr1MaxCount also be set to 0, and so forth.

See the Configuration Error Codes table on page 117 if you encounter configuration errors.

Word 0 contains general configuration bits. Word 1 contains the filter settings. Words 2 through 5 refer to the physical outputs. Words 6 through 45 are counter configuration words. Words 46 through 117 are range configuration words. More detailed descriptions of the configuration words and bits follow the configuration array below.

## IMPORTANT

Certain values (noted below) cannot be changed while a counter or range is enabled. Attempting to do so will cause a configuration error and the entire configuration array will be rejected until the error is eliminated.

## Table 12 - Configuration Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC

| Word   | Bit       | Bit      | Bit       | Bit      | Bit                 | Bit                 | Bit          | Bit          | Bit       | Bit          | Bit          | Bit                                             | Bit     | Function                                         | Bit   | Bit   |
|--------|-----------|----------|-----------|----------|---------------------|---------------------|--------------|--------------|-----------|--------------|--------------|-------------------------------------------------|---------|--------------------------------------------------|-------|-------|
| Word   |           |          |           |          |                     |                     |              |              |           |              |              | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 |         | Function                                         |       |       |
| 0      | Individual Counter Reset ()  ddua Disable (1)           | Individual Counter Reset ()  ddua Disable (1)          | Individual Counter Reset ()  ddua Disable (1)           |          | NumberOf Counters   | Not used PFE        | Not used PFE | Not used PFE |           | Not used Ctr | Not used Ctr | Rst                                             | OCL O   | General Configuration Bits                       |       |       |
| 1      | Filter_Z1 | Not used | Filter_B1 | Not used | Filter_A1 Filter_Z0 | Filter_A1 Filter_Z0 |              | Not used     | Filter_B0 | Filter_B0    | Not used     |                                                 |         | Filter_A0 Filter Selection                       |       |       |
| 2      | Not used  | Not used | Not used  | Not used | Not used            | Out 3 PSR           | Out 2 PSR    | Out1 PSR     | Out0 PSR  | Out3 PM      | Out2 PM      | Out1 PM                                         | Out0 PM | Output Program Mode and Output Program State Run |       |       |
| 3      | Not used  | Not used | Not used  | Not used | Not used            | Not used            | Not used     | Not used     | Not used  | Out3 PV      | Out2 PV      | Out1 PV                                         | Out0 PV | Output Program Value                             |       |       |

Table 12 - Configuration Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC (Continued)

| Word   | Bit                      |                          |                          |                          | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                            |                            |                            | Function                                     |                          |                          |                          |                          |                          |                          |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|---------------------------------------------------|----------------------------|----------------------------|----------------------------|----------------------------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|
| 4      | Not used                 | Out 2 FSR                | Out 1 FSR                | Out0 FSR                 | Out3 FM                                           | Out 2 FM                   | Out1 FM                    | Out0 FM                    | Output Fault Mode and Output Fault State Run |                          |                          |                          |                          |                          |                          |
| 5      | Not used                 | Not used                 | Not used                 | Not used                 | Out3 FV                                           | Out 2 FV                   | Out1 FV                    | Out0 FV                    | Output Fault Value                           |                          |                          |                          |                          |                          |                          |
| 6  7   | Ctr0MaxCount             | Ctr0MaxCount             | Ctr0MaxCount             | Ctr0MaxCount             | Ctr0MaxCount                                      | Ctr0MaxCount               | Ctr0MaxCount               | Ctr0MaxCount               | Counter 0 Maximum Count                      | Ctr0MaxCount             | Ctr0MaxCount             | Ctr0MaxCount             | Ctr0MaxCount             | Ctr0MaxCount             | Ctr0MaxCount             |
| 8      | Ctr0MinCount             | Ctr0MinCount             | Ctr0MinCount             | Ctr0MinCount             | Ctr0MinCount                                      | Ctr0MinCount               | Ctr0MinCount               | Ctr0MinCount               | Counter 0 Minimum Count                      | Ctr0MinCount             | Ctr0MinCount             | Ctr0MinCount             | Ctr0MinCount             | Ctr0MinCount             | Ctr0MinCount             |
| 10     | Ctr0Preset               | Ctr0Preset               | Ctr0Preset               | Ctr0Preset               | Ctr0Preset                                        | Ctr0Preset                 | Ctr0Preset                 | Ctr0Preset                 | Counter 0 Preset                             | Ctr0Preset               | Ctr0Preset               | Ctr0Preset               | Ctr0Preset               | Ctr0Preset               | Ctr0Preset               |
| 12     | Ctr0Hysteresis           | Ctr0Hysteresis           | Ctr0Hysteresis           | Ctr0Hysteresis           | Ctr0Hysteresis                                    | Ctr0Hysteresis             | Ctr0Hysteresis             | Ctr0Hysteresis             | Counter 0 Hysteresis                         | Ctr0Hysteresis           | Ctr0Hysteresis           | Ctr0Hysteresis           | Ctr0Hysteresis           | Ctr0Hysteresis           | Ctr0Hysteresis           |
| 13     | Ctr0Scalar               |                          |                          |                          |                                                   |                            |                            |                            | Counter 0 Scalar                             |                          |                          |                          |                          |                          |                          |
| 14     | Ctr0CyclicRateUpdateTime | Ctr0CyclicRateUpdateTime | Ctr0CyclicRateUpdateTime | Ctr0CyclicRateUpdateTime | Ctr0CyclicRateUpdateTime                          | Ctr0CyclicRateUpdateTime   | Ctr0CyclicRateUpdateTime   | Ctr0CyclicRateUpdateTime   | Counter 0 Cyclic Rate Update Time            | Ctr0CyclicRateUpdateTime | Ctr0CyclicRateUpdateTime | Ctr0CyclicRateUpdateTime | Ctr0CyclicRateUpdateTime | Ctr0CyclicRateUpdateTime | Ctr0CyclicRateUpdateTime |
| 15     | Not used Lin ear Not used Storage mode  Not used                          | Not used Lin ear Not used Storage mode  Not used                          | Not used Lin ear Not used Storage mode  Not used                          | Not used Lin ear Not used Storage mode  Not used                          | Not used Lin ear Not used Storage mode  Not used                                                   | Operational mode Counter 0 | Operational mode Counter 0 | Operational mode Counter 0 | Configuration Flags                          | Not used Lin ear Not used Storage mode  Not used                          | Not used Lin ear Not used Storage mode  Not used                          | Not used Lin ear Not used Storage mode  Not used                          |                          |                          |                          |
| 16     | Ctr1MaxCount             | Ctr1MaxCount             | Ctr1MaxCount             | Ctr1MaxCount             | Ctr1MaxCount                                      | Ctr1MaxCount               | Ctr1MaxCount               | Ctr1MaxCount               | Counter 1 Maximum Count                      | Ctr1MaxCount             | Ctr1MaxCount             | Ctr1MaxCount             | Ctr1MaxCount             | Ctr1MaxCount             | Ctr1MaxCount             |
| 18     | Ctr1MinCount             | Ctr1MinCount             | Ctr1MinCount             | Ctr1MinCount             | Ctr1MinCount                                      | Ctr1MinCount               | Ctr1MinCount               | Ctr1MinCount               | Counter 1 Minimum Count                      | Ctr1MinCount             | Ctr1MinCount             | Ctr1MinCount             | Ctr1MinCount             | Ctr1MinCount             | Ctr1MinCount             |
| 20     | Ctr1Preset               | Ctr1Preset               | Ctr1Preset               | Ctr1Preset               | Ctr1Preset                                        | Ctr1Preset                 | Ctr1Preset                 | Ctr1Preset                 | Counter 1 Preset                             | Ctr1Preset               | Ctr1Preset               | Ctr1Preset               | Ctr1Preset               | Ctr1Preset               | Ctr1Preset               |
| 22     | Ctr1Hysteresis           | Ctr1Hysteresis           | Ctr1Hysteresis           | Ctr1Hysteresis           | Ctr1Hysteresis                                    | Ctr1Hysteresis             | Ctr1Hysteresis             | Ctr1Hysteresis             | Counter 1 Hysteresis                         | Ctr1Hysteresis           | Ctr1Hysteresis           | Ctr1Hysteresis           | Ctr1Hysteresis           | Ctr1Hysteresis           | Ctr1Hysteresis           |
| 23     | Ctr1Scalar               | Ctr1Scalar               | Ctr1Scalar               | Ctr1Scalar               | Ctr1Scalar                                        | Ctr1Scalar                 | Ctr1Scalar                 | Ctr1Scalar                 | Counter 1 Scalar                             | Ctr1Scalar               | Ctr1Scalar               | Ctr1Scalar               | Ctr1Scalar               | Ctr1Scalar               | Ctr1Scalar               |
| 24     | Ctr1CyclicRateUpdateTime | Ctr1CyclicRateUpdateTime | Ctr1CyclicRateUpdateTime | Ctr1CyclicRateUpdateTime | Ctr1CyclicRateUpdateTime                          | Ctr1CyclicRateUpdateTime   | Ctr1CyclicRateUpdateTime   | Ctr1CyclicRateUpdateTime   | Counter 1 Cyclic Rate Update Time            | Ctr1CyclicRateUpdateTime | Ctr1CyclicRateUpdateTime | Ctr1CyclicRateUpdateTime | Ctr1CyclicRateUpdateTime | Ctr1CyclicRateUpdateTime | Ctr1CyclicRateUpdateTime |
| 25     | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                                                   | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                            | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                            | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                            | Configuration Flags Counter 2 Maximum        | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          | Not used Lin ear Not used Storage mode  Not used  Operational mode Counter 1                          |
| 26  27 | Ctr2MaxCount             | Ctr2MaxCount             | Ctr2MaxCount             | Ctr2MaxCount             | Ctr2MaxCount                                      | Ctr2MaxCount               | Ctr2MaxCount               | Ctr2MaxCount               | Count                                        | Ctr2MaxCount             | Ctr2MaxCount             | Ctr2MaxCount             | Ctr2MaxCount             | Ctr2MaxCount             | Ctr2MaxCount             |
| 28     | Ctr2MinCount             | Ctr2MinCount             | Ctr2MinCount             | Ctr2MinCount             | Ctr2MinCount                                      | Ctr2MinCount               | Ctr2MinCount               | Ctr2MinCount               | Counter 2 Minimum Count                      | Ctr2MinCount             | Ctr2MinCount             | Ctr2MinCount             | Ctr2MinCount             | Ctr2MinCount             | Ctr2MinCount             |
| 30     | Ctr2Preset               | Ctr2Preset               | Ctr2Preset               | Ctr2Preset               | Ctr2Preset                                        | Ctr2Preset                 | Ctr2Preset                 | Ctr2Preset                 | Counter 2 Preset                             | Ctr2Preset               | Ctr2Preset               | Ctr2Preset               | Ctr2Preset               | Ctr2Preset               | Ctr2Preset               |
| 32     | Ctr2Hysteresis           | Ctr2Hysteresis           | Ctr2Hysteresis           | Ctr2Hysteresis           | Ctr2Hysteresis                                    | Ctr2Hysteresis             | Ctr2Hysteresis             | Ctr2Hysteresis             | Counter 2 Hysteresis                         | Ctr2Hysteresis           | Ctr2Hysteresis           | Ctr2Hysteresis           | Ctr2Hysteresis           | Ctr2Hysteresis           | Ctr2Hysteresis           |
| 33     | Ctr2Scalar               | Ctr2Scalar               | Ctr2Scalar               | Ctr2Scalar               | Ctr2Scalar                                        | Ctr2Scalar                 | Ctr2Scalar                 | Ctr2Scalar                 | Counter 2 Scalar                             | Ctr2Scalar               | Ctr2Scalar               | Ctr2Scalar               | Ctr2Scalar               | Ctr2Scalar               | Ctr2Scalar               |
| 34     | Ctr2CyclicRateUpdateTime | Ctr2CyclicRateUpdateTime | Ctr2CyclicRateUpdateTime | Ctr2CyclicRateUpdateTime | Ctr2CyclicRateUpdateTime                          | Ctr2CyclicRateUpdateTime   | Ctr2CyclicRateUpdateTime   | Ctr2CyclicRateUpdateTime   | Counter 2 Cyclic Rate Update Time            | Ctr2CyclicRateUpdateTime | Ctr2CyclicRateUpdateTime | Ctr2CyclicRateUpdateTime | Ctr2CyclicRateUpdateTime | Ctr2CyclicRateUpdateTime | Ctr2CyclicRateUpdateTime |

Table 12 - Configuration Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC (Continued)

| Word   | Bit                             |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                 | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                                 |                                 |                                 |                                 | Function                                       |                                 |
|--------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|------------------------------------------------|---------------------------------|
| 35     | Not used Lin                                 | Not used Lin                                 | Not used Lin                                 | ear                             | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Not used                                          | Not used                        | Not used                        | Not used                        | Not used                        | Counter 2 Configuration Flags                  | Not used                        |
| 36     | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                                      | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                    | Ctr3MaxCount                    | Counter 3 Maximum Count                        | Ctr3MaxCount                    |
| 38  39 | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                                      | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                    | Ctr3MinCount                    | Counter 3 Minimum Count                        | Ctr3MinCount                    |
| 40  41 | Ctr3Preset                      |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                                   |                                 |                                 |                                 |                                 | Counter 3 Preset                               |                                 |
| 42     | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                                    | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Ctr3Hysteresis                  | Counter 3 Hysteresis                           | Ctr3Hysteresis                  |
| 43     | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                                        | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                      | Ctr3Scalar                      | Counter 3 Scalar                               | Ctr3Scalar                      |
| 44     | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime                          | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Ctr3CyclicRateUpdateTime        | Counter 3 Cyclic Rate Update Time              | Ctr3CyclicRateUpdateTime        |
| 45     | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                                   | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Not used Lin ear Not used                                 | Counter 3 Configuration Flags                  | Not used Lin ear Not used                                 |
| 46     | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit                           | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range0To11[0].HighLimit         | Range 0 High Limit                             | Range0To11[0].HighLimit         |
| 47 48  |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                                   |                                 |                                 |                                 |                                 | Range 0 Low Limit                              |                                 |
| 49     | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out                   | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out | Range0To11[0].LowLimit  Out Out                | Range0To11[0].LowLimit  Out Out |
| 50     | Out 15                          | Out 14                          | Out 13                          | 12 Out 11                       |                                 | Out 10                          | Out 09                          | 8                               | Out 7                           | Out 6                                             | Out 5 Out 4 Out                 | 3                               | Out 2 Out 1                     | Out 0                           | Range 0 Output Control                         |                                 |
| 51     | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Inv                             | Not used Type                   | Not used Type                                     | Not used Type                   |                                 |                                 |                                 | Not used ToThisCtr Range 0 Configuration Flags |                                 |
| 52     | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit                           | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range0To11[1].HighLimit         | Range 1 High Limit                             | Range0To11[1].HighLimit         |
| 54     | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit                            | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range0To11[1].LowLimit          | Range 1 Low Limit                              | Range0To11[1].LowLimit          |
| 55 56  | Out 15 14                       | Out                             | Out 13                          | Out 12                          | Out 11                          | Out 10                          | Out 09                          | Out 8                           | Out 7                           | Out 6                                             | Out 5 Out 4 Out                 | 3                               | Out 2 Out 1                     | Out 0                           | Range 1 Output Control                         |                                 |
| 57     | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Inv                             | Not used Type                   | Not used Type                                     | Not used Type                   |                                 |                                 |                                 | Not used ToThisCtr Range 1 Configuration Flags |                                 |
| 58  59 | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit                           | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range0To11[2].HighLimit         | Range 2 High Limit                             | Range0To11[2].HighLimit         |
| 60     |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                                   |                                 |                                 |                                 |                                 |                                                |                                 |
| 61     | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit                            | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range0To11[2].LowLimit          | Range 2 Low Limit                              | Range0To11[2].LowLimit          |
| 62     | Out 15 14                       | Out                             | Out 13                          | Out 12                          | Out 11                          | Out 10                          | Out 09                          | Out 8                           | Out 7                           | Out 6                                             | Out 5 Out 4 Out                 | 3                               | Out 2 Out 1                     | Out 0                           | Range 2 Output Control                         |                                 |
| 63     | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Not used                        | Inv                             | Not used Type                   | Not used Type                                     | Not used Type                   |                                 |                                 |                                 | Not used ToThisCtr Range 2 Configuration Flags |                                 |
| 64     | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit                           | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range0To11[3].HighLimit         | Range 3 High Limit                             | Range0To11[3].HighLimit         |
| 65     |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                 |                                                   |                                 |                                 |                                 |                                 |                                                |                                 |

Table 12 - Configuration Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC (Continued)

| Word   | Bit                     | Bit                     | Bit                     | Bit                     | Bit                     | Bit                     | Bit                     | Bit                     | Bit                     | Bit                     | Bit                                             | Bit                     | Bit                     | Bit                     | Bit                                            | Bit                     | Bit   |
|--------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------------------------------|-------------------------|-------------------------|-------------------------|------------------------------------------------|-------------------------|-------|
| Word   |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 |                         |                         |                         | Function                                       |                         |       |
| 66     | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit                          | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range0To11[3].LowLimit  | Range 3 Low Limit                              | Range0To11[3].LowLimit  |       |
| 67     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |
| 68     | Out 15                  | Out 14                  | Out 13                  | Out 12                  | Out 11                  | Out 10 09               | Out Out 8               | 7                       | Out                     | Out 6                   | Out 5 Out 4 Out                                 | 3                       | Out 2 Out 1 Out 0       |                         | Range 3 Output Control                         |                         |       |
| 69     | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Inv                     | Not used Type           | Not used Type           | Not used Type                                   |                         |                         |                         | Not used ToThisCtr Range 3 Configuration Flags |                         |       |
| 70     | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit                         | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range0To11[4].HighLimit | Range 4 High Limit                             | Range0To11[4].HighLimit |       |
| 71     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |
| 72     | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit                          | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range0To11[4].LowLimit  | Range 4 Low Limit                              | Range0To11[4].LowLimit  |       |
| 73     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |
| 74     | Out 15                  | Out 14                  | Out 13                  | Out 12                  | Out 11 10               | Out Out 09              | Out 8                   | 7                       | Out                     | Out 6                   | Out 5 Out 4 Out                                 | 3                       | Out 2 Out 1             | Out 0                   | Range 4 Output Control                         |                         |       |
| 75     | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Inv                     | Not used Type           | Not used Type           | Not used Type                                   |                         |                         |                         | Not used ToThisCtr Range 4 Configuration Flags |                         |       |
| 76     | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit                         | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range0To11[5].HighLimit | Range 5 High Limit                             | Range0To11[5].HighLimit |       |
| 77     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |
| 78     | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit                          | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range0To11[5].LowLimit  | Range 5 Low Limit                              | Range0To11[5].LowLimit  |       |
| 79     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |
| 80     | Out 15                  | Out 14                  | Out 13                  | Out 12                  | Out 11 10               | Out Out 09              | Out 8                   | 7                       | Out                     | Out 6                   | Out 5 Out 4 Out                                 | 3                       | Out 2 Out 1             | Out 0                   | Range 5 Output Control                         |                         |       |
| 81     | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Inv                     | Not used Type           | Not used Type           | Not used Type                                   |                         |                         |                         | Not used ToThisCtr Range 5 Configuration Flags |                         |       |
| 82     | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit                         | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range0To11[6].HighLimit | Range 6 High Limit                             | Range0To11[6].HighLimit |       |
| 84     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |
|        | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit                          | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range0To11[6].LowLimit  | Range 6 Low Limit                              | Range0To11[6].LowLimit  |       |
| 85     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |
| 86     | Out 15                  | Out 14                  | Out 13                  | Out 12                  | Out 11                  | Out 10                  | Out 09                  | Out 8                   | Out 7                   | Out 6                   | Out 5 Out 4 Out                                 | 3                       | Out 2 Out 1             | Out 0                   | Range 6 Output Control                         |                         |       |
| 87     | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Inv                     | Not used Type           | Not used Type           | Not used Type                                   |                         |                         |                         | Not used ToThisCtr Range 6 Configuration Flags |                         |       |
| 88     | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit                         | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range0To11[7].HighLimit | Range 7 High Limit                             | Range0To11[7].HighLimit |       |
| 89     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |
| 90     | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit                          | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range0To11[7].LowLimit  | Range 7 Low Limit                              | Range0To11[7].LowLimit  |       |
| 91     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |
| 92     | Out 15                  | Out 14                  | Out 13                  | Out 12                  | Out 11                  | Out 10 09               | Out Out 8               | 7                       | Out                     | Out 6                   | Out 5 Out 4 Out                                 | 3                       | Out 2 Out 1             | Out 0                   | Range 7 Output Control                         |                         |       |
| 93     | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Not used                | Inv  Not used Type      | Inv  Not used Type      | Inv  Not used Type      | Inv  Not used Type                              |                         |                         |                         | Not used ToThisCtr Range 7 Configuration Flags |                         |       |
| 94     | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit                         | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range0To11[8].HighLimit | Range 8 High Limit                             | Range0To11[8].HighLimit |       |
| 95     |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                                                 |                         |                         |                         |                                                |                         |       |

Table 12 - Configuration Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC (Continued)

| Bit                         |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             |                                                 |                             |                             |                             | Function                                        |                             |
|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-----------------------------|-------------------------------------------------|-----------------------------|-----------------------------|-----------------------------|-------------------------------------------------|-----------------------------|
| Word                        |                             |                             |                             |                             |                             |                             |                             |                             |                             |                             | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 |                             |                             |                             | Function                                        |                             |
| 96                          | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit                          | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range0To11[8].LowLimit      | Range 8 Low Limit                               | Range0To11[8].LowLimit      |
| 97                          | 97                          | 97                          | 97                          | 97                          | 97                          | 97                          | 97                          | 97                          | 97                          | 97                          | 97                                              | 97                          | 97                          | 97                          | 97                                              | 97                          |
| 98                          | Out 15                      | Out 14                      | Out 13                      | Out 12                      | Out 11                      | Out 10                      | Out 09 Out 8                | 7                           | Out                         | Out 6                       | Out 5 Out 4 Out                                 | 3                           | Out 2 Out 1                 | Out 0                       | Range 8 Output Control                          |                             |
| 99  Not used                | 99  Not used                | 99  Not used                | 99  Not used                | 99  Not used                | 99  Not used                | 99  Not used                | 99  Not used                | Inv                         | Not used Type               | Not used Type               | Not used Type                                   |                             |                             |                             | Not used ToThisCtr Range 8 Configuration Flags  |                             |
| Range0To11[9].HighLimit     | Range0To11[9].HighLimit     | Range0To11[9].HighLimit     | Range0To11[9].HighLimit     | Range0To11[9].HighLimit     | Range0To11[9].HighLimit     | Range0To11[9].HighLimit     | Range0To11[9].HighLimit     | Range0To11[9].HighLimit     |                             |                             |                                                 |                             |                             |                             | Range 9 High Limit                              |                             |
| 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit                     | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | 102  Range0To11[9].LowLimit | Range 9 Low Limit                               | 102  Range0To11[9].LowLimit |
| 103                         | 103                         | 103                         | 103                         | 103                         | 103                         | 103                         | 103                         | 103                         | 103                         | 103                         | 103                                             | 103                         | 103                         | 103                         | 103                                             | 103                         |
| 104  Out 15                 |                             | Out 14                      | Out 13                      | Out 12                      | Out 11                      | Out 10                      | Out 09 Out 8                |                             | Out 7                       | Out 6                       | Out 5 Out 4 Out                                 | 3                           | Out 2 Out 1                 | Out 0                       | Range 9 Output Control                          |                             |
| 105  Not used               | 105  Not used               | 105  Not used               | 105  Not used               | 105  Not used               | 105  Not used               | 105  Not used               | 105  Not used               | Inv                         | Not used Type               | Not used Type               | Not used Type                                   |                             |                             |                             | Not used ToThisCtr Range 9 Configuration Flags  |                             |
| Range0To11[10].HighLimit    | Range0To11[10].HighLimit    | Range0To11[10].HighLimit    | Range0To11[10].HighLimit    | Range0To11[10].HighLimit    | Range0To11[10].HighLimit    | Range0To11[10].HighLimit    | Range0To11[10].HighLimit    | Range0To11[10].HighLimit    |                             |                             |                                                 |                             |                             |                             | Range 10 High Limit                             |                             |
| Range0To11[10].LowLimit     | Range0To11[10].LowLimit     | Range0To11[10].LowLimit     | Range0To11[10].LowLimit     | Range0To11[10].LowLimit     | Range0To11[10].LowLimit     | Range0To11[10].LowLimit     | Range0To11[10].LowLimit     | Range0To11[10].LowLimit     |                             |                             |                                                 |                             |                             |                             | Range 10 Low Limit                              |                             |
| 109                         | 109                         | 109                         | 109                         | 109                         | 109                         | 109                         | 109                         | 109                         | 109                         | 109                         | 109                                             | 109                         | 109                         | 109                         | 109                                             | 109                         |
| 110                         | Out 15                      | Out 14                      | Out 13                      | Out 12                      | Out 11                      | Out 10                      | Out 09 Out 8                |                             | Out 7                       | Out 6                       | Out 5 Out 4 Out                                 | 3                           | Out 2 Out 1                 | Out 0                       | Range 10 Output Control                         |                             |
| 111  Not used               | 111  Not used               | 111  Not used               | 111  Not used               | 111  Not used               | 111  Not used               | 111  Not used               | 111  Not used               | Inv                         | Not used Type               | Not used Type               | Not used Type                                   |                             |                             |                             | Not used ToThisCtr Range 10 Configuration Flags |                             |
| Range0To11[11].HighLimit    | Range0To11[11].HighLimit    | Range0To11[11].HighLimit    | Range0To11[11].HighLimit    | Range0To11[11].HighLimit    | Range0To11[11].HighLimit    | Range0To11[11].HighLimit    | Range0To11[11].HighLimit    |                             |                             |                             |                                                 |                             |                             |                             | Range 11 High Limit                             |                             |
| Range0To11[11].LowLimit     | Range0To11[11].LowLimit     | Range0To11[11].LowLimit     | Range0To11[11].LowLimit     | Range0To11[11].LowLimit     | Range0To11[11].LowLimit     | Range0To11[11].LowLimit     | Range0To11[11].LowLimit     | Range0To11[11].LowLimit     |                             |                             |                                                 |                             |                             |                             | Range 11 Low Limit                              |                             |
| 115                         | 115                         | 115                         | 115                         | 115                         | 115                         | 115                         | 115                         | 115                         | 115                         | 115                         | 115                                             | 115                         | 115                         | 115                         | 115                                             | 115                         |
| 116                         | Out 15                      | Out 14                      | Out 13                      | Out 12                      | Out 11                      | Out 10                      | Out 09 8                    | Out                         | Out 7                       | Out 6                       | Out 5 Out 4 Out                                 | 3                           | Out 2 Out 1                 | Out 0                       | Range 11 Output Control                         |                             |
| 117  Not used               | 117  Not used               | 117  Not used               | 117  Not used               | 117  Not used               | 117  Not used               | 117  Not used               | 117  Not used               | Inv  Not used Type          | Inv  Not used Type          | Inv  Not used Type          | Inv  Not used Type                              |                             |                             |                             | Not used ToThisCtr Range 11 Configuration Flags |                             |

## Table 13 - Configuration Array - L23E Packaged Controller Embedded HSC

| Word   | Bit       | Bit      | Bit       | Bit      | Bit                 | Bit                 | Bit          | Bit          | Bit          | Bit          | Bit          | Bit                                             | Bit      | Function                                                  | Bit   | Bit   |
|--------|-----------|----------|-----------|----------|---------------------|---------------------|--------------|--------------|--------------|--------------|--------------|-------------------------------------------------|----------|-----------------------------------------------------------|-------|-------|
| Word   |           |          |           |          |                     |                     |              |              |              |              |              | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 |          | Function                                                  |       |       |
| 0      | Not used  | Not used | Not used  | Not used | NumberOf Counters   | NumberOf Counters   | Not used PFE | Not used PFE | Not used PFE | Not used Ctr | Not used Ctr | Rst                                             | OCL O    | General Configuration Bits                                |       |       |
| 1      | Filter_Z1 | Not used | Filter_B1 | Not used | Filter_A1 Filter_Z0 | Filter_A1 Filter_Z0 |              | Not used     | Filter_B0    | Filter_B0    | Not used     |                                                 |          | Filter_A0 Filter Selection                                |       |       |
| 2      | Not used  | Not used | Not used  | Not used | Not used            | Out 3 PSR           | Out 2 PSR    | Out1 PSR     | Out0 PSR     | Out3 PSO     | Out2 PSO     | Out1 PSO                                        | Out0 PSO | Program State for Output and Program State Run for Output |       |       |
| 3      | Not used  | Not used | Not used  | Not used | Not used            | Not used            | Not used     | Not used     | Not used     | Out3 PVO     | Out2 PVO     | Out1 PVO                                        | Out0 PVO | Program Value for Output                                  |       |       |

Table 13 - Configuration Array - L23E Packaged Controller Embedded HSC (Continued)

| Word   | Bit          |              |              |              |              | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |              |              |              |                            |                            |                            | Function                                              |              |              |              |
|--------|--------------|--------------|--------------|--------------|--------------|---------------------------------------------------|--------------|--------------|--------------|----------------------------|----------------------------|----------------------------|-------------------------------------------------------|--------------|--------------|--------------|
| 4      | Not used     | Not used     | Not used     | Not used     | Out 3 FSR    | Out 2 FSR                                         | Out1 FSR     | Out0 FSR     | Out3 FSO     | Out2 FSO                   | Out1 FSO                   | Out0 FSO                   | Fault State for Output and Fault State Run for Output |              |              |              |
| 5      | Not used     | Not used     | Not used     | Not used     | Not used     | Not used                                          | Not used     | Not used     | Out3 FVO     | Out2 FVO                   | Out1 FVO                   | Out0 FVO                   | Fault Value for Output                                |              |              |              |
| 6      | Ctr0MaxCount | Ctr0MaxCount | Ctr0MaxCount | Ctr0MaxCount | Ctr0MaxCount | Ctr0MaxCount                                      | Ctr0MaxCount | Ctr0MaxCount | Ctr0MaxCount | Ctr0MaxCount               | Ctr0MaxCount               | Ctr0MaxCount               | Counter 0 Maximum Count                               | Ctr0MaxCount | Ctr0MaxCount | Ctr0MaxCount |
| 8      | Ctr0MinCount | Ctr0MinCount | Ctr0MinCount | Ctr0MinCount | Ctr0MinCount | Ctr0MinCount                                      | Ctr0MinCount | Ctr0MinCount | Ctr0MinCount | Ctr0MinCount               | Ctr0MinCount               | Ctr0MinCount               | Counter 0 Minimum Count                               | Ctr0MinCount | Ctr0MinCount | Ctr0MinCount |
| 10     | Ctr0Preset   | Ctr0Preset   | Ctr0Preset   | Ctr0Preset   | Ctr0Preset   | Ctr0Preset                                        | Ctr0Preset   | Ctr0Preset   | Ctr0Preset   | Ctr0Preset                 | Ctr0Preset                 | Ctr0Preset                 | Counter 0 Preset                                      | Ctr0Preset   | Ctr0Preset   | Ctr0Preset   |
| 12     | Not used     |              |              |              |              |                                                   |              |              |              |                            |                            |                            | Not used                                              |              |              |              |
| 13     | Not used     |              |              |              |              |                                                   |              |              |              |                            |                            |                            | Not used                                              |              |              |              |
| 14     | Not used     |              |              |              |              |                                                   |              |              |              |                            |                            |                            | Not used                                              |              |              |              |
| 15     | Not used Lin              | ear          | Not used     | Storage mode | Not used     | Not used                                          | Not used     | Not used     | Not used     | Operational mode Counter 0 | Operational mode Counter 0 | Operational mode Counter 0 | Configuration Flags                                   |              |              |              |
| 16     | Ctr1MaxCount | Ctr1MaxCount | Ctr1MaxCount | Ctr1MaxCount | Ctr1MaxCount | Ctr1MaxCount                                      | Ctr1MaxCount | Ctr1MaxCount | Ctr1MaxCount | Ctr1MaxCount               | Ctr1MaxCount               | Ctr1MaxCount               | Counter 1 Maximum Count                               | Ctr1MaxCount | Ctr1MaxCount | Ctr1MaxCount |
| 18  19 | Ctr1MinCount | Ctr1MinCount | Ctr1MinCount | Ctr1MinCount | Ctr1MinCount | Ctr1MinCount                                      | Ctr1MinCount | Ctr1MinCount | Ctr1MinCount | Ctr1MinCount               | Ctr1MinCount               | Ctr1MinCount               | Counter 1 Minimum Count                               | Ctr1MinCount | Ctr1MinCount | Ctr1MinCount |
| 20     | Ctr1Preset   | Ctr1Preset   | Ctr1Preset   | Ctr1Preset   | Ctr1Preset   | Ctr1Preset                                        | Ctr1Preset   | Ctr1Preset   | Ctr1Preset   | Ctr1Preset                 | Ctr1Preset                 | Ctr1Preset                 | Counter 1 Preset                                      | Ctr1Preset   | Ctr1Preset   | Ctr1Preset   |
| 22     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used                                          | Not used     | Not used     | Not used     | Not used                   | Not used                   | Not used                   | Not used                                              | Not used     | Not used     | Not used     |
| 23     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used                                          | Not used     | Not used     | Not used     | Not used                   | Not used                   | Not used                   | Not used                                              | Not used     | Not used     | Not used     |
| 24     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used                                          | Not used     | Not used     | Not used     | Not used                   | Not used                   | Not used                   | Not used                                              | Not used     | Not used     | Not used     |
| 25     | Not used Lin ear              | Not used Lin ear              | Not used     | Storage mode | Not used     | Not used                                          | Not used     | Not used     | Not used     | Operational mode Counter 1 | Operational mode Counter 1 | Operational mode Counter 1 | Configuration Flags                                   |              |              |              |
| 26     | Ctr2MaxCount | Ctr2MaxCount | Ctr2MaxCount | Ctr2MaxCount | Ctr2MaxCount | Ctr2MaxCount                                      | Ctr2MaxCount | Ctr2MaxCount | Ctr2MaxCount | Ctr2MaxCount               | Ctr2MaxCount               | Ctr2MaxCount               | Counter 2 Maximum Count                               | Ctr2MaxCount | Ctr2MaxCount | Ctr2MaxCount |
| 28     | Ctr2MinCount | Ctr2MinCount | Ctr2MinCount | Ctr2MinCount | Ctr2MinCount | Ctr2MinCount                                      | Ctr2MinCount | Ctr2MinCount | Ctr2MinCount | Ctr2MinCount               | Ctr2MinCount               | Ctr2MinCount               | Counter 2 Minimum Count                               | Ctr2MinCount | Ctr2MinCount | Ctr2MinCount |
| 30     | Ctr2Preset   | Ctr2Preset   | Ctr2Preset   | Ctr2Preset   | Ctr2Preset   | Ctr2Preset                                        | Ctr2Preset   | Ctr2Preset   | Ctr2Preset   | Ctr2Preset                 | Ctr2Preset                 | Ctr2Preset                 | Counter 2 Preset                                      | Ctr2Preset   | Ctr2Preset   | Ctr2Preset   |
| 32     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used                                          | Not used     | Not used     | Not used     | Not used                   | Not used                   | Not used                   | Not used                                              | Not used     | Not used     | Not used     |
| 33     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used                                          | Not used     | Not used     | Not used     | Not used                   | Not used                   | Not used                   | Not used                                              | Not used     | Not used     | Not used     |
| 34     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used                                          | Not used     | Not used     | Not used     | Not used                   | Not used                   | Not used                   | Not used                                              | Not used     | Not used     | Not used     |
| 35     | Not used Lin ear Not used              | Not used Lin ear Not used              | Not used Lin ear Not used              | Not used Lin ear Not used              | Not used Lin ear Not used              | Not used Lin ear Not used                                                   | Not used Lin ear Not used              | Not used Lin ear Not used              | Not used Lin ear Not used              | Not used Lin ear Not used                            | Not used Lin ear Not used                            | Not used Lin ear Not used                            | Counter 2 Configuration Flags                         | Not used Lin ear Not used              | Not used Lin ear Not used              | Not used Lin ear Not used              |

Table 13 - Configuration Array - L23E Packaged Controller Embedded HSC (Continued)

| Word   | Bit          | Bit          | Bit          | Bit                                             | Function                      | Bit          | Bit          | Bit          | Bit          | Bit          | Bit          | Bit          | Bit          | Bit          | Bit          |
|--------|--------------|--------------|--------------|-------------------------------------------------|-------------------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|
| Word   |              |              |              | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 | Function                      |              |              |              |              |              |              |              |              |              |              |
| 36     | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount                                    | Counter 3 Maximum Count       | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount | Ctr3MaxCount |
| 37     |              |              |              |                                                 | Counter 3 Maximum Count       |              |              |              |              |              |              |              |              |              |              |
| 38     | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount                                    | Counter 3 Minimum Count       | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount | Ctr3MinCount |
| 39     |              |              |              |                                                 | Counter 3 Minimum Count       |              |              |              |              |              |              |              |              |              |              |
| 40     | Ctr3Preset   | Ctr3Preset   | Ctr3Preset   | Ctr3Preset                                      | Counter 3 Preset              | Ctr3Preset   | Ctr3Preset   | Ctr3Preset   | Ctr3Preset   | Ctr3Preset   | Ctr3Preset   | Ctr3Preset   | Ctr3Preset   | Ctr3Preset   | Ctr3Preset   |
| 41     |              |              |              |                                                 | Counter 3 Preset              |              |              |              |              |              |              |              |              |              |              |
| 42     | Not used     | Not used     | Not used     | Not used                                        | Not used                      | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     |
| 43     | Not used     | Not used     | Not used     | Not used                                        | Not used                      | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     |
| 44     | Not used     | Not used     | Not used     | Not used                                        | Not used                      | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     |
| 45     | Not used Lin              | ear          | Not used     | Not used                                        | Counter 3 Configuration Flags | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     | Not used     |              |              |

## General Configuration Bits

These configuration bits apply to the 1769-HSC/B module and the CMX 5370 L2 packaged controller embedded HSC.

|    |                                  | Configuration Array Word 0 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                    |       |
|----|----------------------------------|------------------------------------------------------------------------------|--------------------|-------|
| General Configuration Bits Individual Counter (1)  dduaCou Reset Disable(1)    | Number of counters  Not used PFE | Number of counters  Not used PFE                                             | Not used Ctr Reset | OCL O |

## OCLO - Overcurrent Latch Off (OverCurrentLatchOff)

When set, this bit causes the module to make any overcurrent activity latch the corresponding output off, simulating a physical fuse. When OCLO = 0, it automatically resets. The rising edge of RBF resets the output.

## IMPORTANT

Do not set this bit while a counter or range is enabled (Ctr0En, Ctr1En, Ctr2En, Ctr3En, or RangeEn set to 1). Attempting to do so will result in a BadModConfigUpdate error.

See page 120 for a list of prohibited settings.

Counter 0 in this example equates to individual counter reset selection bit 12.

## Counter Reset (CtrReset)

Bits 12…15 in the configuration array correspond to the counter reset selection bits for counters 0…3, respectively. The Counter Reset Enable in the Add-On profile lets you select which counter to be enabled or disabled. An enabled checkbox indicates a zero (0) in the respective counter reset selection bits in RSLogix 5000 software.

## IMPORTANT

The individual counter reset functionality applies only to the 1769-HSC/B module used with CompactLogix controllers and the CMX 5370 L2 packaged controller embedded HSC. You cannot use the individual counter reset functionality with MicroLogix controllers.

If you do not want a counter to reset by default, you must uncheck the box in the Add-On profile for the respective counter reset selection bit. A '1' will display in the configuration array to denote that this bit is disabled from resetting a count. The individual counter reset functionality for the 1769-HSC/B module is reverse logic, with a 0 = enabled and a 1 = disabled, for RSLogix 5000 software.

Figure 19 - Configuration for Individual Counter Reset Enable

<!-- image -->

As shown in Figure 19, the Counter Reset Enable box defaults with a check mark to indicate the respective counter is enabled in the Add-On Profile. Therefore, the individual counter reset functionality is enabled for the selected counter of the 1769-HSC/B module. The corresponding controller tag in RSLogix 5000 software displays a zero (0) for enabled.

Counter 0 in this example equates to individual counter reset selection bit 12.

Figure 20 - Configuration for Individual Counter Reset Disable

<!-- image -->

As shown in Figure 20, the Counter Reset Enable box has been unchecked to indicate the individual counter reset functionality is disabled for the selected counter of the 1769-HSC/B module. The corresponding controller tag in RSLogix 5000 software shows a one (1) for disabled.

The CtrReset bit, when set, causes the following to occur for both the 1769-HSC/A and 1769-HSC/B modules when the system transitions to Run or the Inhibit Module bit transitions to 0:

- System checks counter reset selection bits 12…15 to determine which counter needs to be reset.(1)
- Only those counters selected for reset are reset to zero.
- The output array is reset to default values until the ModConfig bit is set (1). The default value for the output array is all zeros.
- The input array counter status flags (Overflow, Underflow, RisingEdgeZ, RateValid, PresetWarning) are reset.
- The input array counter values (Current Count(2), StoredCount, CurrentRate and PulseInterval) are also reset to zero.
- Counts are lost and outputs are turned off.

## IMPORTANT

For most predictable results, clear the output image of the controller before performing a counter reset (CtrReset) to the 1769-HSC module.

This is because CtrReset does not change the controller's output image. CtrReset sets the 1769-HSC module's output array to all zeroes. If any bit is set to 1 in the controller's output image when sent to the module, it will be seen as a state transition and be acted upon.

(1) This applies only to the 1769-HSC/B module and the CMX 5370 L2 packaged controller embedded HSC.

(2) If zero is outside the MinCount and MaxCount limits set in the configuration array, then the Preset value is loaded into CurrentCount instead of zero. This also causes the PresetWarning bit to be set, which, in turn, sets the GenError bit.

## PFE - Program to Fault Enable (ProgToFaultEn)

This bit indicates what should happen when the bus controller indicates a change from one condition (Program mode) to another (Fault mode). If this bit is set (1), the safe state operation of all four real outputs changes to that identified by the Fault State and Fault Value words. If this bit is reset (0), the module continues with the operation identified by the Program State and Program Value words.

## Number of Counters (NumberOfCounters)

This 2-bit value indicates whether the module uses 1 counter, 2 counters, 3 counters, or 4 counters. The default value is 1 (2 counters).

|   Bit 01  Bit 00  Counters |
|----------------------------|
|                        001 |
|                        012 |
|                        103 |
|                        114 |

## IMPORTANT

Do not set this value while a counter or range is enabled (Ctr0En, Ctr1En, Ctr2En, Ctr3En, or RangeEn set to 1). Attempting to do so will result in a BadModConfigUpdate error.

See page 120 for a list of prohibited settings.

## Filter Selection

| Configuration Array Word 1 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |          |          |          |                   |          |          |          |          |          |
|------------------------------------------------------------------------------|----------|----------|----------|-------------------|----------|----------|----------|----------|----------|
| Filter Selection Filter_Z1                                                   | Not used | FilterB1 | Not used | FilterA1 FilterZ0 | Not used | FilterB0 | Not used | FilterA0 | FilterA0 |

## This value indicates the nominal filter frequency as shown in the table.

| Filters and Corresponding Bits   |                                                                     | FilterA0 Bit 1 - FilterA0_1   | Bit 0 - FilterA0_0   |
|----------------------------------|---------------------------------------------------------------------|-------------------------------|----------------------|
| Filters and Corresponding Bits   | FilterB0                                                            | Bit 4 - FilterB0_1            | Bit 3 - FilterB0_0   |
| Filters and Corresponding Bits   | FilterZ0                                                            | Bit 7 - FilterZ0_1            | Bit 6 - FilterZ0_0   |
| Filters and Corresponding Bits   | FilterA1                                                            | Bit 9 - FilterA1_1            | Bit 8 - FilterA1_0   |
| Filters and Corresponding Bits   | FilterB1                                                            | Bit 12 - FilterB1_1           | Bit 11 - FilterB1_0  |
| Filters and Corresponding Bits   | FilterZ1                                                            | Bit 15 - FilterZ1_1           | Bit 14 - FilterZ1_0  |
| Nominal Frequency Settings       | None                                                                | 0                             | 0                    |
| Nominal Frequency Settings       | 0.01 ms minimum pulse width (0.0185 ms for the packaged controller) |                               | 0 1                  |
| Nominal Frequency Settings       | 0.5 ms minimum pulse width (0.715 ms for the packaged controller)   |                               | 1 0                  |
| Nominal Frequency Settings       | 5 ms minimum pulse width (7.1 ms for the packaged controller)       |                               | 1 1                  |

## IMPORTANT

Do not set these bits while certain counters or ranges are enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.

## Program Mode and Program State Run

| Configuration Array Word 2 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |          |          |          |          |          |         |         |         |         |
|------------------------------------------------------------------------------|----------|----------|----------|----------|----------|---------|---------|---------|---------|
| Output Program Mode and Output Program State Run                             | Not used | Out3 PSR | Out2 PSR | Out1 PSR | Out0 PSR | Out3 PM | Out2 PM | Out1 PM | Out0 PM |

Program Mode (Out0ProgramMode through Out3ProgramMode)

The program mode bits configure the output for Hold Last State (HLS) or User-defined Safe State (UDSS) during Program State.

- 1 = Hold Last State
- 0 = User-defined Safe State

## IMPORTANT

Program Mode and Program State Run apply only to certain controllers. Refer to your controller's documentation for more information.

The packaged controllers' embedded HSC does not support this feature.

Program State Run (Out0ProgramStateRun through Out3ProgramStateRun)

Program State Run lets you specify, on a bit basis, that the output should continue to be controlled by the module as if it were in the Run state. That is, events on the module or changes in the output image will affect the physical outputs without regard to the Program\_HLS or UDSS state indicated. When this bit is set, the corresponding Program Mode and Program Value bits are ignored.

<!-- image -->

ATTENTION: Selecting this option lets outputs change state while ladder logic is not running. You must take care to make sure that this does not pose a risk of injury or equipment damage when selecting this option.

## IMPORTANT

The prescan initiated by some controllers could have an effect on the outputs. To overcome any changes in physical output states caused by this, retentive output instructions (for example, latch or unlatch) should be used when bit manipulations are done on the Output image of this module in ladder logic.

This applies to a wide range of bits when Program State Run is selected, because presetting a counter, enabling a range, changing a mask, and changing configuration array settings can cause ranges and outputs to change state.

## Output Program Value (Out0ProgramValue through Out3ProgramValue)

| Configuration Array Word 3 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |          |         |         |         |         |          |          |          |          |          |          |
|------------------------------------------------------------------------------|----------|---------|---------|---------|---------|----------|----------|----------|----------|----------|----------|
| Output Program Value                                                         | Not used | Out3 PV | Out2 PV | Out1 PV | Out0 PV | Not used | Not used | Not used | Not used | Not used | Not used |

These bits are the values that will be applied to each of the real outputs when User-defined Safe State (UDSS) is set as described and the module is in Program state.

## Output Fault Mode and Output Fault State Run

| Configuration Array Word 4 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |          |          |          |          |          |         |         |         |         |
|------------------------------------------------------------------------------|----------|----------|----------|----------|----------|---------|---------|---------|---------|
| Output Fault Mode and Output Fault State Run                                 | Not used | Out3 FSR | Out2 FSR | Out1 FSR | Out0 FSR | Out3 FM | Out2 FM | Out1 FM | Out0 FM |

Output Fault Mode (Out0FaultMode through Out3FaultMode)

These bits configure the output for Hold Last State or User-defined Safe State during a Fault state.

- 1 = Hold Last State
- 0 = User-defined Safe State

Output Fault State Run (Out0FaultStateRun through Out3FaultStateRun)

Similar to Program State Run, Fault State Run lets you specify, on a bit basis, that the output should continue to be controlled by the module as if it were Run state. That is, events on the module or changes in the output image will affect the physical outputs without regard to the Fault\_HLS or UDSS state indicated. When this bit is set, the corresponding Fault mode and fault value bits are ignored.

<!-- image -->

ATTENTION: Selecting this option lets outputs change state while ladder logic is not running. You must take care to make sure that this does not pose a risk of injury or equipment damage when selecting this option.

## IMPORTANT

The prescan initiated by some controllers could have an effect on the outputs. To overcome any changes in physical output states caused by this, retentive output instructions (for example, latch or unlatch) should be used when bit manipulations are done on the output image of this module in ladder logic.

This applies to a wide range of bits when Fault State Run is selected, because presetting a counter, enabling a range, changing a mask, and changing Configuration Array settings can cause ranges and outputs to change state.

## Output Fault Value (Out0FaultValue through Out3FaultValue)

| Configuration Array Word 5 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   | Configuration Array Word 5 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |          |         |         |         |         |          |          |          |          |          |          |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------|---------|---------|---------|---------|----------|----------|----------|----------|----------|----------|
|                                                                              | 5 Output Fault Value                                                         | Not used | Out3 FV | Out2 FV | Out1 FV | Out0 FV | Not used | Not used | Not used | Not used | Not used | Not used |

These bits are the values that will be applied to each of the real outputs when User-defined Safe State is set as described and the module is in Fault state.

TIP

Outputs are also affected by PFT above.

## Counter Maximum Count (CtrnMaxCount)

| Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                            |              |
|-----------------------------------------------------------------------------|----------------------------|--------------|
|                                                                             | 6 Counter 0 Maximum Count  | Ctr0MaxCount |
| 7                                                                           |                            |              |
|                                                                             | 16 Counter 1 Maximum Count | Ctr1MaxCount |
| 17                                                                          |                            |              |
|                                                                             | 26 Counter 2 Maximum Count | Ctr2MaxCount |
| 27                                                                          |                            |              |
|                                                                             | 36 Counter 3 Maximum Count | Ctr3MaxCount |
| 37                                                                          |                            |              |

This is the maximum count value allowed for counter (n). The count value cannot exceed this value. Allowable values are CtrnMinCount 1…2,147,483,647 (decimal).

The default value is 2,147,483,647 decimal for counters 0 and 1. The default value is 0 for counters 2 and 3.

## IMPORTANT

Do not change this value while the counter is enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.

## Counter Minimum Count (CtrnMinCount)

| Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   | Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
|                                                                             | 8 Counter 0 Minimum Count Ctr0MinCount                                      |
| 9                                                                           | 8 Counter 0 Minimum Count Ctr0MinCount                                      |
|                                                                             | 18 Counter 1 Minimum Count Ctr1MinCount                                     |
| 19                                                                          | 18 Counter 1 Minimum Count Ctr1MinCount                                     |
|                                                                             | 28 Counter 2 Minimum Count Ctr2MinCount                                     |
| 29                                                                          | 28 Counter 2 Minimum Count Ctr2MinCount                                     |
|                                                                             | 38 Counter 3 Minimum Count Ctr3MinCount                                     |
| 39                                                                          | 38 Counter 3 Minimum Count Ctr3MinCount                                     |

This is the minimum count value allowed for counter (n). The count value cannot fall below this value. This value must be less than CtrnMaxCount or a configuration error occurs. Allowable values are from -2,147,483,648 to CtrnMaxCount - 1.

The default value is -2,147,483,648 decimal for counters 0 and 1. The default value is 0 for counters 2 and 3.

## IMPORTANT

Do not change this value while the counter is enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.

## Counter Preset (CtrnPreset)

| Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   | Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------|
|                                                                             | 10 Counter 0 Preset Ctr0Preset                                              |
| 11                                                                          | 10 Counter 0 Preset Ctr0Preset                                              |
|                                                                             | 20 Counter 1 Preset Ctr1Preset                                              |
| 21                                                                          | 20 Counter 1 Preset Ctr1Preset                                              |
|                                                                             | 30 Counter 2 Preset Ctr2Preset                                              |
| 31                                                                          | 30 Counter 2 Preset Ctr2Preset                                              |
|                                                                             | 40 Counter 3 Preset Ctr3Preset                                              |
| 41                                                                          | 40 Counter 3 Preset Ctr3Preset                                              |

This value can be used to change the current count value of countern on certain gate (Zn) events and when CtrnSoftPreset is used.

CtrnPreset must be greater than or equal to CtrnMinCount and less than CtrnMaxCount. The default value is zero.

## Counter Hysteresis (CtrnHysteresis)

IMPORTANT

The Counter Hysteresis information does not apply to the L23E packaged controller because rate measurement is not supported.

|                                        | Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|----------------------------------------|-----------------------------------------------------------------------------|
| 12 Counter 0 Hysteresis Ctr0Hysteresis |                                                                             |
| 22 Counter 1 Hysteresis Ctr1Hysteresis |                                                                             |
| 32 Counter 2 Hysteresis Ctr2Hysteresis |                                                                             |
| 42 Counter 3 Hysteresis Ctr3Hysteresis |                                                                             |

The hysteresis value is the number of counts that should be disregarded in the calculation of the cyclic rate. If the count value changes by less than the hysteresis value, the rate is reported as zero, regardless of the actual rate at which the pulses are counted.

## IMPORTANT

Do not change this value while the counter is enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.

## Counter Scalar (CtrnScalar)

## IMPORTANT

The Counter Scalar information does not apply to the L23E packaged controller because rate measurement is not supported.

|                                | Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|--------------------------------|-----------------------------------------------------------------------------|
| 13 Counter 0 Scalar Ctr0Scalar |                                                                             |
| 23 Counter 1 Scalar Ctr1Scalar |                                                                             |
| 33 Counter 2 Scalar Ctr2Scalar |                                                                             |
| 43 Counter 3 Scalar Ctr3Scalar |                                                                             |

This value is used to scale the Rate value. The Rate value is divided by the Scalar value. The default value is 1 for counters 0 and 1. The default value is 0 for counters 2 and 3.

CtrnScalar can be used to determine RPM. To configure the Ctr[n].CurrentRate value to show an RPM value, set CtrnScalar to (counts per revolution)/60.

See page 34 for more information.

## IMPORTANT

For any counter being used, do not set Scalar to a value less than one or a configuration error will occur.

## IMPORTANT

Do not change this value while the counter is enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.

## Cyclic Rate Update Time (CtrnCyclicRateUpdateTime)

The Counter Scalar information does not apply to the L23E packaged

IMPORTANT controller because rate measurement is not supported.

| Configuration Array Words                                     | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|---------------------------------------------------------------|---------------------------------------------------|
| 14 Counter 0 Cyclic Rate Update Time Ctr0CyclicRateUpdateTime |                                                   |
| 24 Counter 1 Cyclic Rate Update Time Ctr1CyclicRateUpdateTime |                                                   |
| 34 Counter 2 Cyclic Rate Update Time Ctr2CyclicRateUpdateTime |                                                   |
| 44 Counter 3 Cyclic Rate Update Time Ctr3CyclicRateUpdateTime |                                                   |

This value is used to set the cyclic rate update time for the CurrentRate calculation. The value indicates the time in milliseconds from 1…32767. An invalid number causes a configuration error. The default value is 10 for counters 0 and 1. The default value is 0 for counters 2 and 3.

## IMPORTANT

Do not change this value while the counter is enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.

See Cyclic Rate Calculation Method (current rate) on page 32 for more information on cyclic rate.

## Configuration Flags

|                                  |                 |          |              |          | Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                  |                  |          |          |          |          |          |
|----------------------------------|-----------------|----------|--------------|----------|-----------------------------------------------------------------------------|------------------|------------------|----------|----------|----------|----------|----------|
| 15 Counter 0 Configuration Flags | Not used Linear | Not used | Storage mode | Not used | Not used                                                                    | Operational mode | Operational mode | Not used |          |          |          |          |
| 25 Counter 1 Configuration Flags | Not used Linear | Not used | Storage mode | Not used | Not used                                                                    | Operational mode | Operational mode | Not used |          |          |          |          |
| 35 Counter 2 Configuration Flags | Not used Linear | Not used | Not used     | Not used | Not used                                                                    | Not used         | Not used         | Not used | Not used | Not used | Not used | Not used |
| 45 Counter 3 Configuration Flags | Not used Linear | Not used | Not used     | Not used | Not used                                                                    | Not used         | Not used         | Not used | Not used | Not used | Not used | Not used |

Operational Mode (CtrnConfig.OperationalMode\_0 through CtrnConfig.OperationalMode\_2)

These bits apply to Counters 0 and 1 only.

This value determines how the A0 or A1 and B0 or B1 inputs are decoded when assigned to counter 0 or counter 1.

| Set bit   |                                                                                        |    | For function             |
|-----------|----------------------------------------------------------------------------------------|----|--------------------------|
|           | CtrnConfig.OperationalMode_2 CtrnConfig.OperationalMode_1 CtrnConfig.OperationalMode_0 |    |                          |
| 0         | 0                                                                                      | 0  | Pulse internal direction |
| 0         | 0                                                                                      | 1  | Pulse external direction |
| 1         | 0                                                                                      | 0  | Quadrature encoder X1    |
| 1         | 0                                                                                      | 1  | Quadrature encoder X2    |
| 1         | 1                                                                                      | 0  | Quadrature encoder X4    |
| 0         | 1                                                                                      | 0  | Up/Down Pulses           |
| 0         | 1                                                                                      | 1  | reserved                 |
| 1         | 1                                                                                      | 1  | reserved                 |

TIP

The Ctr1Config.OperationalMode bits are reserved if the Number of Counters equals 1. Attempting to set reserved bits will result in a configuration error.

| IMPORTANT   | Do not change this value while the counter is enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Storage Mode (CtrnConfig.StorageMode\_0 through CtrnConfig.StorageMode\_2)

These three bits apply to Counters 0 and 1 only. They define how the module interprets the Z input, as shown below. Each bit works independently. If bit 0 and bit 2 are set simultaneously, a Z event causes the Current Count Value to be stored and then preset.

| Set bit   | Set bit                                                                                                                                                                                       | For function                                                                                                                                                                                  |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           |                                                                                                                                                                                               | CtrnConfig.StorageMode_0 Stores the Current Count Value on the rising edge of Z to Ctr[n].StoredCount in the input file.                                                                      |
|           |                                                                                                                                                                                               | CtrnConfig.StorageMode_1 Holds the counter at its Current Count Value while Z = 1.                                                                                                            |
|           |                                                                                                                                                                                               | CtrnConfig.StorageMode_2 Presets the Current Count Value on the rising edge of Z.                                                                                                             |
| IMPORTANT | Z = internal Z. Internal Z is the version of the Z input pin as modified by the output array control bits Z Invert and Z Inhibit.                                                             | Z = internal Z. Internal Z is the version of the Z input pin as modified by the output array control bits Z Invert and Z Inhibit.                                                             |
| TIP       | The Ctr1Config.Storage Mode bits are reserved if NumberofCounters_1 and NumberofCounters_0 are set to 00 (one counter). Attempting to set reserved bits will result in a configuration error. | The Ctr1Config.Storage Mode bits are reserved if NumberofCounters_1 and NumberofCounters_0 are set to 00 (one counter). Attempting to set reserved bits will result in a configuration error. |
| IMPORTANT | Do not change this value while the counter is enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.                         | Do not change this value while the counter is enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.                         |

Linear (Ctr0Config.Linear through Ctr3Config.Linear)

This bit indicates how the counter operates upon reaching a CtrnMinCount or CtrnMaxCount.

- 0 = Ring Counter
- 1 = Linear Counter

See page 28 for a description of ring and linear counter operation.

| IMPORTANT   | Do not change this value while the counter is enabled. Attempting to do so will result in a BadModConfigUpdate error. See page 120 for a list of prohibited settings.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Range High Limit (Range0To11[n].HighLimit) and Range Low Limit (Range0To11[n].LowLimit)

IMPORTANT

The Range High Limit and Range Low Limit words do not apply to the L23E packaged controller.

|                                                          | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |
|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     | 46 and 47 Range 0 High Limit Range0To11[0].HighLimit     |
| 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       | 48 and 49 Range 0 Low Limit Range0To11[0].LowLimit       |
| 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     | 52 and 53 Range 1 High Limit Range0To11[1].HighLimit     |
| 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       | 54 and 55 Range 1 Low Limit Range0To11[1].LowLimit       |
| 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      | 58and 59 Range 2 High Limit Range0To11[2].HighLimit      |
| 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       | 60 and 61 Range 2 Low Limit Range0To11[2].LowLimit       |
| 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     | 64 and 65 Range 3 High Limit Range0To11[3].HighLimit     |
| 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       | 66 and 67 Range 3 Low Limit Range0To11[3].LowLimit       |
| 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     | 70 and 71 Range 4 High Limit Range0To11[4].HighLimit     |
| 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       | 72 and 73 Range 4 Low Limit Range0To11[4].LowLimit       |
| 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     | 76 and 77 Range 5 High Limit Range0To11[5].HighLimit     |
| 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       | 78 and 79 Range 5 Low Limit Range0To11[5].LowLimit       |
| 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     | 82 and 83 Range 6 High Limit Range0To11[6].HighLimit     |
| 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       | 84 and 85 Range 6 Low Limit Range0To11[6].LowLimit       |
| 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     | 88 and 89 Range 7 High Limit Range0To11[7].HighLimit     |
| 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       | 90 and 91 Range 7 Low Limit Range0To11[7].LowLimit       |
| 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     | 94 and 95 Range 8 High Limit Range0To11[8].HighLimit     |
| 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       | 96 and 97 Range 8 Low Limit Range0To11[8].LowLimit       |
| 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   | 100 and 101 Range 9 High Limit Range0To11[9].HighLimit   |
| 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     | 102 and 103 Range 9 Low Limit Range0To11[9].LowLimit     |
| 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit | 106 and 107 Range 10 High Limit Range0To11[10].HighLimit |
| 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   | 108 and 109 Range 10 Low Limit Range0To11[10].LowLimit   |
| 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit | 112 and 113 Range 11 High Limit Range0To11[11].HighLimit |

These values, which represent a count value or rate value, depending upon the programed Type, are used for range comparison. When the rate value is equal to Range0To11[n].HighLimit or Range0To11[n].LowLimit, Rangen changes state, becoming either active or inactive, depending upon the setting of the Range0To11[n].Invert bit.

## Object Value (Current Count or Current Rate)

TIP Range0To11[n].HighLimit must be greater than Range0To11[n].LowLimit or a configuration error results.

<!-- image -->

## Range Output Control (Range0To11[n].OutputControl)

IMPORTANT The Range Output Control words do not apply to the L23E packaged controller.

|                                   |        |        |        |        | Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |       |       |       |       |       |       |       |       |       |       |
|-----------------------------------|--------|--------|--------|--------|-----------------------------------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 50 Range 0 Output Control Out 15  | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| 56 Range 1 Output Control Out 15  | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| 62 Range 2 Output Control Out 15  | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| Range 3 Output Control Out 15     | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| 74 Range 4 Output Control Out 15  | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| 80 Range 5 Output Control Out 15  | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| 86 Range 6 Output Control Out 15  | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| Range 7 Output Control Out 15     | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| 98 Range 8 Output Control Out 15  | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| 104 Range 9 Output Control Out 15 | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| Out 15                            | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |
| Out 15                            | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                                                      | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |

These 16-bit words indicate which outputs should be enabled when a range is active. When range n is enabled, this word is combined with the other range output masks as described in Output Off Mask (OutputOffMask.0 through OutputOffMask.15) on page 91 and on page 89 .

## Range Configuration Flags

IMPORTANT

The Range Configuration Flag information does not apply to the L23E packaged controller.

|                                  |          |     |                |                |                    | Configuration Array Words 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                    |
|----------------------------------|----------|-----|----------------|----------------|--------------------|-----------------------------------------------------------------------------|--------------------|
| 51 Range 0 Configuration Flags   | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 57 Range 1 Configuration Flags   | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 63 Range 2 Configuration Flags   | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 69 Range 3 Configuration Flags   | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 75 Range 4 Configuration Flags   | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 81 Range 5 Configuration Flags   | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 87 Range 6 Configuration Flags   | Not used | Inv | Not used Typ e | Not used Typ e | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 93 Range 7 Configuration Flags   | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 99 Range 8 Configuration Flags   | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 105 Range 9 Configuration Flags  | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 111 Range 10 Configuration Flags | Not used | Inv | Not used Typ   | e              | Not used ToThisCtr | Not used ToThisCtr                                                          | Not used           |
| 117 Range 11 Configuration Flags | Not used | Inv | Not used Typ   | e              | Not used Typ       | Not used ToThisCtr                                                          | Not used ToThisCtr |

## ToThisCtr (Range0To11[n].ToThisCounter)

This 2-bit value indicates which counter is used in the range comparison for range n, as shown in the table.

|   Bit 01  Bit 00  Counter |
|---------------------------|
|                       000 |
|                       011 |
|                       102 |
|                       113 |

| IMPORTANT   | If this value is greater than NumberOfCounters, a configuration error occurs.   |
|-------------|---------------------------------------------------------------------------------|

## Type (Range0To11[n].Type)

This bit indicates which type of value to use for the range comparison in range n . This value and Range0To11[n].ToThisCounter determine the current value that is used in range comparison as the rate or count value.

|   Range0To11[n].Type | Range Type   |
|----------------------|--------------|
|                    0 | Count Value  |
|                    1 | Rate Value   |

## Inv (Range0To11[n].Invert)

This bit indicates whether the range n should be active inside or outside the Range0To11[n].Low Limit and Range0To11[n].HighLimit window.

- 0 = The range n is active when the rate or count value is at or between Range0To11[n].Low Limit and Range0To11[n].HighLimit. When the range is active, the RangeActive.n bit is set. When the range is active and enabled, the outputs indicated in the Range Output Control word are activated .
- 1 = The range n is active when the rate or count value is lower than or equal to Range0To11[n].LowLimit or higher than or equal to Range0To11[n].HighLimit. When the range is active, the RangeActive.n bit is set. When the range is active and enabled, the outputs indicated in the Range Output Control word are applied.
- TIP Ranges can be active in overflow, underflow, and rollover situations.

## Output Array

The output array, which consists of 34 words, lets you access the module's realtime output data to control the module. The default value is all zeros.

## IMPORTANT

## IMPORTANT

The output array contains dynamic configuration data. The settings in the output array must be compatible with the settings in the configuration array.

For example, do not attempt to set Counter Control Bits for a given counter in the output array unless NumberOfCounters in the configuration array indicates that the counter is declared to be used.

All Not used bits (shaded in the Output Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC table, below) must be set to 0 or the InvalidOutput bit in the input array will be set. When the InvalidOutput bit is set, the entire output array is rejected until an output array that does not have this error is sent.

## Table 14 - Output Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC

| Word Bit   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | Function                                                           |                                                   |
|------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|--------------------------------------------------------------------|---------------------------------------------------|
| Word Bit   |                                                   | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | Function                                                           |                                                   |
| 0          | Out 15                                            | Out 14                                            | Out 13                                            | Out 12                                            | Out 11                                            | Out 10                                            | Out 9                                             | Out 8                                             | Out 7                                             | Out 6                                             | Out 5                                             | Out 4                                             | Out 3                                             | Out 0                                             | Out 2 Out 1 Output On Mask                                         |                                                   |
| 1          | Out 15                                            | Out 14                                            | Out 13                                            | Out 12                                            | Out 11                                            | Out 10                                            | Out 9                                             | Out 8                                             | Out 7                                             | Out 6                                             | Out 5                                             | Out 4                                             | Out 3                                             | Out 0                                             | Out 2 Out 1 Output Off Mask                                        |                                                   |
| 2          |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | R15 R14 R13 R12 R11 R10 R9 R8 R7 R6 R5 R4 R3 R2 R1 R0 Range Enable |                                                   |
| 3          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                                           | Not used                                          |
| 4          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | RBF                                               | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Reset Blown Fuse                                                   | Not used                                          |
| 5          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | RP W                                              | RRE Z                                             |                                                   | Z Inh Z Inv D                                     | Inh                                               | D Inv                                             |                                                   |                                                   | RU RO SP En Counter 0 Control Bits                                 |                                                   |
| 6          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | RP W                                              | RRE Z                                             |                                                   | Z Inh Z Inv D                                     | Inh                                               | D Inv                                             |                                                   |                                                   | RU RO SP En Counter 1 Control Bits                                 |                                                   |
| 7          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | RP W                                              | Not used                                          | Not used                                          | Not used                                          | Not used                                          | D Inv                                             |                                                   |                                                   | RU RO SP En Counter 2 Control Bits                                 |                                                   |
| 8          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | RP W                                              | Not used                                          | Not used                                          | Not used                                          | Not used                                          | D Inv                                             |                                                   |                                                   | RU RO SP En Counter 3 Control Bits                                 |                                                   |
| 9          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                                           | Not used                                          |
| 10  11     | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Range12To15[0].HiLimOrDirWr Range High Limit or   | Direct Write Value                                                 | Range12To15[0].HiLimOrDirWr Range High Limit or   |
| 12         | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit                           | Range Low Limit                                                    | Range12To15[0].LowLimit                           |
| 13         | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control | Range12To15[0].OutputControl Range Output Control                  | Range12To15[0].OutputControl Range Output Control |
| 15         | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Not used                                          |                                                   | Inv                                               | Inv                                               | Not used LD                                       | W                                                 | Type                                              |                                                   |                                                   | Not used ToThisCtr Range Configuration Flags                       |                                                   |
| 16         | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Range12To15[1].HiLimOrDirWr Range High Limit or   | Direct Write Value                                                 | Range12To15[1].HiLimOrDirWr Range High Limit or   |
| 18         | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit                           | Range Low Limit                                                    | Range12To15[1].LowLimit                           |
| 19         |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | Range Low Limit                                                    |                                                   |
|            |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | Range Low Limit                                                    |                                                   |

Table 14 - Output Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC (Continued)

| Word Bit   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | Function                                          |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
|------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Word Bit   |                                                   | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                                                   |                                                   |                                                   |                                                   | Function                                          |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 20         | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control | Range12To15[1].OutputControl Range Output Control |
| 21         | Not used                                          | Not used                                          | Inv                                               | Not used LD                                       | W                                                 | Type                                              | Not used ToThisCtr Range Configuration Flags      |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 22         | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Direct Write Value                                | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   | Range12To15[2].HiLimOrDirWr Range High Limit or   |
| 23         |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | Direct Write Value                                |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 24         | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range Low Limit                                   | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit                           |
| 25         |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | Range Low Limit                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 26         | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control | Range12To15[2].OutputControl Range Output Control |
| 27         | Not used                                          | Not used                                          | Inv                                               | Not used LD                                       | W                                                 | Type                                              | Not used ToThisCtr Range Configuration Flags      |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 28         | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Direct Write Value                                | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   | Range12To15[3].HiLimOrDirWr Range High Limit or   |
| 29         |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | Direct Write Value                                |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 30         | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range Low Limit                                   | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit                           |
| 31         |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   | Range Low Limit                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 32         | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control | Range12To15[3].OutputControl Range Output Control |
| 33         | Not used                                          | Not used                                          | Inv                                               | Not used LD                                       | W                                                 | Type                                              | Not used ToThisCtr Range Configuration Flags      |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |

Table 15 - Output Array - L23E Packaged Controller Enbedded HSC

| Word Bit             |                      |                      |                      |                      |                      |                                                 |                      |                      |                      |                      |                      |                      |                      | Function                                                            |                      |                      |
|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|-------------------------------------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|---------------------------------------------------------------------|----------------------|----------------------|
| Word Bit             |                      |                      |                      |                      |                      | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 |                      |                      |                      |                      |                      |                      |                      | Function                                                            |                      |                      |
| 0                    | Out 15               | Out 14 Out 12        | Out 13               | Out 11               | Out 9                | Out 10 Out 8                                    |                      | Out 7                | Out 6                | Out 5                | Out 3 Out 2          | Out 1                | Out 0                | Out 4 Output On Mask                                                |                      |                      |
| 1                    | Out 15               | Out 14 Out 12        | Out 13               | Out 11               | Out 9                | Out 10                                          | Out 8                | Out 7                | Out 6                | Out 5                | Out Out 2            | Out 1                | Out 0                | Out 4 3 Output Off Mask                                             |                      |                      |
| 2                    |                      | R3 R2 R1 R0          |                      | Not used             | Not used             | Not used                                        | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Range Enable                                                        | Not used             |                      |
| 3                    | Not used             | Not used             | Not used             | Not used             | Not used             | Not used                                        | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used                                                            | Not used             | Not used             |
| 4  Not used          | 4  Not used          | 4  Not used          | 4  Not used          | 4  Not used          | 4  Not used          | 4  Not used                                     | 4  Not used          | RBF  Not used        | RBF  Not used        | RBF  Not used        | RBF  Not used        | RBF  Not used        | RBF  Not used        | Reset Blown Fuse                                                    | RBF  Not used        |                      |
| 5  Not used          | 5  Not used          | 5  Not used          | 5  Not used          | 5  Not used          | 5  Not used          | 5  Not used                                     |                      |                      |                      |                      |                      |                      |                      | RPW RREZ Z Inh Z Inv D Inh D Inv RU RO SP En Counter 0 Control Bits |                      |                      |
| 6  Not used          | 6  Not used          | 6  Not used          | 6  Not used          | 6  Not used          | 6  Not used          | 6  Not used                                     |                      |                      |                      |                      |                      |                      |                      | RPW RREZ Z Inh Z Inv D Inh D Inv RU RO SP En Counter 1 Control Bits |                      |                      |
| 7  Not used  RPW     | 7  Not used  RPW     | 7  Not used  RPW     | 7  Not used  RPW     | 7  Not used  RPW     | 7  Not used  RPW     | Not used                                        | Not used             | Not used             | Not used             | Not used             |                      |                      |                      | D Inv RU RO SP En Counter 2 Control Bits                            |                      |                      |
| 8  Not used  RPW     | 8  Not used  RPW     | 8  Not used  RPW     | 8  Not used  RPW     | 8  Not used  RPW     | 8  Not used  RPW     | Not used                                        | Not used             | Not used             | Not used             | Not used             |                      |                      |                      | D Inv RU RO SP En Counter 3 Control Bits                            |                      |                      |
| 9  Not used          | 9  Not used          | 9  Not used          | 9  Not used          | 9  Not used          | 9  Not used          | 9  Not used                                     | 9  Not used          | 9  Not used          | 9  Not used          | 9  Not used          | 9  Not used          | 9  Not used          | 9  Not used          | Not used                                                            | 9  Not used          | 9  Not used          |
| RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0                            | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 | Range High Limit or Direct Write Value 0                            | RangeHighLimit_DWV_0 | RangeHighLimit_DWV_0 |
| 11                   | 11                   | 11                   | 11                   | 11                   | 11                   | 11                                              | 11                   | 11                   | 11                   | 11                   | 11                   | 11                   | 11                   | 11                                                                  | 11                   | 11                   |
| 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0                             | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  | Range Low Limit 0                                                   | 12  RangeLowLimit_0  | 12  RangeLowLimit_0  |
| 13                   | 13                   | 13                   | 13                   | 13                   | 13                   | 13                                              | 13                   | 13                   | 13                   | 13                   | 13                   | 13                   | 13                   | 13                                                                  | 13                   | 13                   |

Table 15 - Output Array - L23E Packaged Controller Enbedded HSC (Continued)

| Word Bit                 |                          |                          |                          |                          |                          |                          |                          |                                                 |                          |                          |                          |                          |                          |                          |                          |                          | Function                                      |
|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|-------------------------------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|--------------------------|-----------------------------------------------|
| Word Bit                 |                          |                          |                          |                          |                          |                          |                          | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 |                          |                          |                          |                          |                          |                          |                          |                          | Function                                      |
| 14                       | Out 15                   | Out 14                   | Out 13                   | Out 12                   | Out 11                   | Out 10                   | Out 9                    | Out 8                                           | Out 7                    | Out 6                    | Out 5                    | Out 4                    | Out 3                    | Out 2                    | Out 1                    | Out 0                    | Range Output Mask 0                           |
| 15                       | Not used                 | Not used                 | Not used                 | Not used                 | Not used                 | Not used                 | Not used                 | RInv                                            | Not used LDW             | Not used LDW             |                          |                          |                          |                          |                          |                          | Not used RCntrNum Range Configuration Flags 0 |
| 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1                        | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | 16  RangeHighLimit_DWV_1 | Range High Limit or Direct Write Value 1      |
| 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1                             | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | 18  RangeLowLimit_1      | Range Low Limit 1                             |
| 20                       | Out 15                   | Out 14                   | Out 13                   | Out 12                   | Out 11                   | Out 10                   | Out 9                    | Out 8                                           | Out 7                    | Out 6                    | Out 5                    | Out 4                    | Out 3                    | Out 2                    | Out 1                    | Out 0                    | Range Output Mask 1                           |
| 21  Not used             | 21  Not used             | 21  Not used             | 21  Not used             | 21  Not used             | 21  Not used             | 21  Not used             | 21  Not used             | RInv                                            | Not used LDW             | Not used LDW             |                          |                          |                          |                          |                          |                          | Not used RCntrNum Range Configuration Flags 1 |
| 22  RangeHighLimit_DWV_2 | 22  RangeHighLimit_DWV_2 | 22  RangeHighLimit_DWV_2 | 22  RangeHighLimit_DWV_2 | 22  RangeHighLimit_DWV_2 | 22  RangeHighLimit_DWV_2 | 22  RangeHighLimit_DWV_2 | 22  RangeHighLimit_DWV_2 | 22  RangeHighLimit_DWV_2                        |                          |                          |                          |                          |                          |                          |                          |                          | Range High Limit or Direct Write Value 2      |
| 24  RangeLowLimit_2      | 24  RangeLowLimit_2      | 24  RangeLowLimit_2      | 24  RangeLowLimit_2      | 24  RangeLowLimit_2      | 24  RangeLowLimit_2      | 24  RangeLowLimit_2      | 24  RangeLowLimit_2      | 24  RangeLowLimit_2                             | 24  RangeLowLimit_2      | 24  RangeLowLimit_2      |                          |                          |                          |                          |                          |                          | Range Low Limit 2                             |
| 25                       | 25                       | 25                       | 25                       | 25                       | 25                       | 25                       | 25                       | 25                                              | 25                       | 25                       | 25                       | 25                       | 25                       | 25                       | 25                       | 25                       |                                               |
| 26  Out 15               |                          | Out 14                   | Out 13                   | Out 12                   | Out 11                   | Out 10                   | Out 9                    | Out 8                                           | Out 7                    | Out 6                    | Out 5                    | Out 4                    | Out 3                    | Out 2                    | Out 1                    | Out 0                    | Range Output Mask 2                           |
| 27  Not used             | 27  Not used             | 27  Not used             | 27  Not used             | 27  Not used             | 27  Not used             | 27  Not used             | 27  Not used             | RInv                                            | Not used LDW             | Not used LDW             |                          |                          |                          |                          |                          |                          | Not used RCntrNum Range Configuration Flags 2 |
| 28  RangeHighLimit_DWV_3 | 28  RangeHighLimit_DWV_3 | 28  RangeHighLimit_DWV_3 | 28  RangeHighLimit_DWV_3 | 28  RangeHighLimit_DWV_3 | 28  RangeHighLimit_DWV_3 | 28  RangeHighLimit_DWV_3 | 28  RangeHighLimit_DWV_3 | 28  RangeHighLimit_DWV_3                        | 28  RangeHighLimit_DWV_3 | 28  RangeHighLimit_DWV_3 |                          |                          |                          |                          |                          |                          | Range High Limit or Direct Write Value 3      |
| 30  RangeLowLimit_3      | 30  RangeLowLimit_3      | 30  RangeLowLimit_3      | 30  RangeLowLimit_3      | 30  RangeLowLimit_3      | 30  RangeLowLimit_3      | 30  RangeLowLimit_3      | 30  RangeLowLimit_3      | 30  RangeLowLimit_3                             | 30  RangeLowLimit_3      | 30  RangeLowLimit_3      |                          |                          |                          |                          |                          |                          | Range Low Limit 3                             |
| 31                       | 31                       | 31                       | 31                       | 31                       | 31                       | 31                       | 31                       | 31                                              | 31                       | 31                       | 31                       | 31                       | 31                       | 31                       | 31                       | 31                       |                                               |
| 32                       | Out 15                   | Out 14                   | Out 13                   | Out 12                   | Out 11                   | Out 10                   | Out 9                    | Out 8                                           | Out 7                    | Out 6                    | Out 5                    | Out 4                    | Out 3                    | Out 2                    | Out 1                    | Out 0                    | Range Output Mask 3                           |
| 33                       | Not used                 | Not used                 | Not used                 | Not used                 | Not used                 | Not used                 | Not used                 | RInv                                            | Not used LDW             | Not used LDW             |                          |                          |                          |                          |                          |                          | Not used RCntrNum Range Configuration Flags 3 |

## Output on Mask (OutputOnMask.0 through OutputOnMask.15)

|                       |        |        |        |        |        |       |       |       |       |       | Output Array Word 0 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |       |       |       |       |
|-----------------------|--------|--------|--------|--------|--------|-------|-------|-------|-------|-------|-----------------------------------------------------------------------|-------|-------|-------|-------|
| Output On Mask Out 15 | Out 14 | Out 13 | Out 12 | Out 11 | Out 10 | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4                                                                 | Out 3 | Out 2 | Out 1 | Out 0 |

This word lets you turn on any output, real or virtual, when the corresponding bit is set. This mask is logically ORed with the range masks but logically ANDed with the Output Off Mask Word described on page 91 .

Using the Output On Mask, all of the module's outputs can be turned on directly by the user control program, like discrete outputs. A bit which is set in the mask turns on the corresponding real or virtual output.

See Output Control on page 36 and Output Control Example on page 43 for more information about output determination.

TIP

The corresponding Output Off Mask bit must be set to enable this bit.

## Output Off Mask (OutputOffMask.0 through OutputOffMask.15)

| Output Array Word 1   |        |        |        |        |        | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |       |       |       |       |       |       |       |       |       |       |
|-----------------------|--------|--------|--------|--------|--------|---------------------------------------------------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Output Off Mask       | Out 15 | Out 14 | Out 13 | Out 12 | Out 11 | Out 10                                            | Out 9 | Out 8 | Out 7 | Out 6 | Out 5 | Out 4 | Out 3 | Out 2 | Out 1 | Out 0 |

This word turns OFF any output, real or virtual, when the corresponding bit is reset. This mask has veto power over all the Range masks and the Output On Mask described above. It is logically AND'ed with the results of those masks.

See Output Control on page 36 and Output Control Example on page 43 for more information about output determination.

TIP

This mask can be overridden when a safe state is indicated.

## Range Enable (RangeEn.0 through RangeEn.15)

| Output Array Word 2   |             | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00       |
|-----------------------|-------------|-------------------------------------------------------|
| Range Enable          |             | R15 R14 R13 R12 R11 R10 R9 R8 R7 R6 R5 R4 R3 R2 R1 R0 |
| Output Array Word 2   |             | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00       |
| Range Enable          | R3 R2 R1 R0 |                                                       |

When the bit corresponding to the range number is set,

Range[n].OutputControl is applied whenever the range is active.

## RBF - Reset Blown Fuse (ResetBlownFuse)

| Output Array Word 4   |          | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |     |          |
|-----------------------|----------|---------------------------------------------------|-----|----------|
| Reset Blown Fuse      | Not used |                                                   | RBF | Not used |

When the OvercurrentLatchOff bit is set and an overcurrent condition has occurred, the real output remains off until this bit is cycled from 0 to 1(rising edge).

## Control Bits

| Output Array Words 5 to 8 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |          |          |                                              |                   |          |          |
|-----------------------------------------------------------------------------|----------|----------|----------------------------------------------|-------------------|----------|----------|
| Counter 0 Control Bits (Word 5)                                             | Not used | Not used | RPW RREZ Z Inh Z Inv D Inh D Inv RU RO SP En | Not used          | Not used |          |
| Counter 1 Control Bits (Word 6)                                             | Not used | Not used | RPW RREZ Z Inh Z Inv D Inh D Inv RU RO SP En | Not used          | Not used |          |
| Counter 2 Control Bits (Word 7)                                             | Not used | RPW      | Not used                                     | D Inv RU RO SP En | Not used | Not used |
| Counter 3 Control Bits (Word 8)                                             | Not used | RPW      | Not used                                     | D Inv RU RO SP En | Not used | Not used |

The control bits for counter (n) are described below.

TIP

The order of precedence for the Preset and Direct Write actions is as follows:

1. Preset
2. Direct Write

## IMPORTANT

Setting any of the control bits under certain conditions of the NumberOfCounters value will result in the input error flag, Ctr[n].InvalidCounter. For more information, see IC - Invalid Counter (Ctr[1].InvalidCounter to Ctr[3].Invalid Counter) table on page 107 .

## En - Enable Counter (CtrnEn)

This bit, when set (1), enables the inputs to be counted. When reset (0), this bit inhibits any activity of the A or B inputs from affecting the count, pulse interval, and rate values.

## SP - Soft Preset (CtrnSoftPreset)

A 0 to 1 transition of this bit causes counter (n) to be preset, changing the count to the value in CtrnPreset.

## RCO - Reset Counter Overflow (CtrnResetCounterOverflow)

A 0 to 1 transition of this bit causes the corresponding Ctr[n]Overflow bit to be reset.

## RCU - Reset Counter Underflow (CtrnResetCounterUnderflow)

A 0 to 1 transition of this bit causes the corresponding Ctr[n]Underflow bit to be reset.

## D Inv - Direction Invert (CtrnDirectionInvert)

This bit, when set, inverts the direction of the counter (n) as follows:

- If the CtrnDirectionInhibit bit is set when this bit is 0, the resulting direction is up, increasing counts.
- If the CtrnDirectionInhibit bit is set when this bit is 1, the resulting direction is down, decreasing counts.

## D Inh - Direction Inhibit (CtrnDirectionInhibit)

This bit, when set, inhibits the direction of the input signal from being used by the module.

## Z Inv - Z Invert (CtrnZInvert)

When set, this bit inverts the Zn value. The Zn value is also affected by the CtrnZInhibit bit. If the CtrnZInhibit is set, the module uses CtrnZInvert for all internal Z activities, preset, hold and store. Input state Zn is not affected by this bit.

## Z Inh - Z Inhibit (CtrnZInhibit)

When set, this bit inhibits the Zn state from being used by the module. However, even if the counter is inhibited, it still will count the pulses at input. For example, if the counter is inhibited with count of 10 and there are 10 more pulses after which it was un-inhibited, then the current count instead of starting with 11 will be 21 for the next pulse.

RREZ - Reset Rising Edge Z (CtrnResetRisingEdgeZ)

A 0 to 1 transition causes the Ctr[n].RisingEdgeZ bit to be reset.

RPW - Reset Counter Preset Warning (CtrnResetCtrPresetWarning)

A 0 to 1 transition causes the Ctr[n]PresetWarning bit to be reset.

## Range High Limit or Direct Write Value (Range12To15[n].HiLimOrDirWr)

IMPORTANT

For the L23E packaged controllers embedded HSC, the ranges referred to in this section are numbered 0…3 instead of 12…15. The ranges in this section apply to only the 1769-HSC module and the CMX 5370 L2 packaged controllers embedded HSC.

| Output Array Words                                                           | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|------------------------------------------------------------------------------|---------------------------------------------------|
| 10 and 11 Range 12 High Limit Direct Write Value Range12To15[0].HiLimOrDirWr |                                                   |
| 16 and 17 Range 13 High Limit Direct Write Value Range12To15[1].HiLimOrDirWr |                                                   |
| 22 and 23 Range 14 High Limit Direct Write Value Range12To15[2].HiLimOrDirWr |                                                   |
| 28 and 29 Range 15 High Limit Direct Write Value Range12To15[3].HiLimOrDirWr |                                                   |

This value can be used in one of two ways, depending on the setting of the Load Direct Write (Range12To15[n].LoadDirectWrite) bit.

When Load Direct Write = 0

When Range12To15[n].LoadDirectWrite = 0, then Range12To15[n].HiLimOrDirWr is used in the range comparison (range represents a count value or a rate value according to the programmed range type, Range12To15[n].Type).

When the range value is equal to Range12To15[n].HiLimOrDirWr, Rangen will change state. The range will become active or inactive depending on the Range12To15[n].Invert bit.

<!-- image -->

TIP

Range12To15[n].HiLimOrDirWr must be higher than the Range12To15[n].LowLimit or the InvalidRangeLimitn error flag in the input array will be set.

TIP

Range12To15[n].HiLimOrDirWr can be higher than the maximum rate or count value. For example, when the object value is a rate, Range12To15[n].HiLimOrDirWr can be programmed in excess of 1,000,000 with no configuration error.

When Load Direct Write = 1

When Range12To15[n].LoadDirectWrite = 1, then Range12To15[n].HiLimOrDirWr is used to change the Ctr[n].CurrentCount to Range12To15[n].HiLimOrDirWr.

When the Range12To15[n].LoadDirectWrite bit transitions from 0 to 1, then Range12To15[n].HiLimOrDirWr is loaded into Ctr[n].CurrentCount (where n is the counter indicated in Range12To15[n].ToThisCounter).

TIP

When CtrnSoftPreset and a Range12To15[n].LoadDirectWrite to counter n are indicated at the same time, only the CtrnSoftPreset will occur. When more than one range indicates a Range12To15[n].LoadDirectWrite to a single counter, only the one from the lowest designated range will take effect.

## Range Low Limit (Range12To15[n].LowLimit)

IMPORTANT

For the L23E packaged controllers embedded HSC, the ranges referred to in this section are numbered 0…3 instead of 12…15. The ranges in this section apply to only the 1769-HSC module and the CMX 5370 L2 packaged controllers embedded HSC.

| Output Array Words           |                         | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |                         |
|------------------------------|-------------------------|---------------------------------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
| 12 and 13 Range 12 Low Limit | Range12To15[0].LowLimit | Range12To15[0].LowLimit                           | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit | Range12To15[0].LowLimit |
| 18 and 19 Range 13 Low Limit | Range12To15[1].LowLimit | Range12To15[1].LowLimit                           | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit | Range12To15[1].LowLimit |
| 24 and 25 Range 14 Low Limit | Range12To15[2].LowLimit | Range12To15[2].LowLimit                           | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit | Range12To15[2].LowLimit |
| 30 and 31 Range 15 Low Limit | Range12To15[3].LowLimit | Range12To15[3].LowLimit                           | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit | Range12To15[3].LowLimit |

This value is used in the range comparison. It is the complement of the Range12To15[n].HiLimOrDirWr value in setting the compare window.

When the rate or count value is equal to Range12To15[n].LowLimit, the range will change state – opposite of the action at Range12To15[n].HiLimOrDirWr. The range will become active or inactive depending on the Range12To15[n].Invert bit.

| TIP   | Range12To15[n].LowLimit must be lower than the Range12To15[n].HiLimOrDirWr or the InvalidRangeLimitn error flag in the input array will be set.   |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| TIP   | Like Range12To15[n].HiLimOrDirWr Range12To15[n].LowLimit can extend beyond the minimum rate or count value.                                       |
| TIP   | When Range12To15[n].LoadDirectWrite is set, Range12To15[n].LowLimit is ignored.                                                                   |

## Range Output Control (Range12To15[n].OutputControl)

## IMPORTANT

For the L23E packaged controllers embedded HSC, the ranges referred to in this section are numbered 0…3 instead of 12…15. The ranges in this section apply to only the 1769-HSC module and the CMX 5370 L2 packaged controllers embedded HSC.

|                                                         | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00         |                                                         |                                                         |                                                         |                                                         |                                                         |                                                         |                                                         |                                                         |                                                         |                                                         |                                                         |                                                         |                                                         |
|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|
| 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl | 14 Range 12 Output Control Range12To15[0].OutputControl |
| 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl | 20 Range 13 Output Control Range12To15[1].OutputControl |
| 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl | 26 Range 14 Output Control Range12To15[2].OutputControl |
| 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl | 32 Range 15 Output Control Range12To15[3].OutputControl |

This 16-bit word indicates which outputs should be on (corresponding bit set in this word) when a range is active. When Rangen is enabled and active, Range12To15[n].OutputControl will be logically OR'ed with other Range12To15[n].OutputControl masks and the OutputOnMask.n and so forth., as described on page 89 .

When Range12To15[n].LoadDirectWrite is set, Range12To15[n].OutputControl is ignored.

## Range Configuration Flags (12To15)

## IMPORTANT

For the L23E packaged controllers embedded HSC, the ranges referred to in this section are numbered 0…3 instead of 12…15. The ranges in this section apply to only the 1769-HSC module and the CMX 5370 L2 packaged controllers embedded HSC.

| Output Array Words              |          | 15 14 13 12 11 10 09 08 07 06 05 04   |     |                   | (1)                |                    | 03 02 01 00        |
|---------------------------------|----------|---------------------------------------|-----|-------------------|--------------------|--------------------|--------------------|
| 15 Range 12 Configuration Flags | Not used | Not used                              | Inv | Not used LDW Type | Not used ToThisCtr | Not used ToThisCtr |                    |
| 21 Range 13 Configuration Flags | Not used | Not used                              | Inv | Not used LDW Type | Not used ToThisCtr | Not used ToThisCtr |                    |
| 27 Range 14 Configuration Flags | Not used | Not used                              | Inv | Not used LDW Type | Not used LDW Type  | Not used ToThisCtr | Not used ToThisCtr |
| 33 Range 15 Configuration Flags | Not used | Not used                              | Inv | Not used LDW Type | Not used LDW Type  | Not used ToThisCtr | Not used ToThisCtr |

(1) Bit 04 is not used for the packaged controller.

ToThisCtr - Range Counter Number (Range12To15[n].ToThisCounter)

This 2-bit value indicates which counter will be used in the range comparison or Range12To15[n].LoadDirectWrite. The counter is indicated in the table below.

|   Bit 01  Bit 00  Counter |
|---------------------------|
|                       000 |
|                       011 |
|                       102 |
|                       113 |

If Range12To15[n].ToThisCounter is set to a number larger than NumberOfCounters in the configuration array, then the InvalidCtrAssignToRangen error bit in the input array will be set.

Type - RangeType (Range12To15[n].Type)

| IMPORTANT   | For the L23E packaged controllers embedded HSC, the range type is fixed at 0, which sets the range type to count value. The ranges in this section apply to only the 1769-HSC module and the CMX 5370 L2 packaged controllers embedded HSC.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

This bit value indicates which type of value to use for the range comparison in Range. That is, the Range12To15[n].ToThisCounter, from above, and this Range12To15[n].Type value determine the rate or count value, the current value which is compared to, for the range comparison. The type of value is indicated as follows:

- 0 = Count Value
- 1 = Rate Value

When Range12To15[n].LoadDirectWrite is set Range12To15[n]. Type is ignored.

LDW - Load Direct Write (Range12To15[n].LoadDirectWrite)

A 0 to 1 transition of this bit causes counter (n)'s current count value to change to the value of Range12To15[n].HiLimOrDirWr.

| IMPORTANT   | The write occurs according to the internal timings of the module and the system. For the most predictable results, the counter should be disabled or stopped while performing this action.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | If both CtrnSoftPreset and Range12To15[n].HiLimOrDirWr transition to 1 during the same Output Array update, only the CtrnSoftPreset occurs. Range12To15[n].HiLimOrDirWr is ignored.          |

## Input Array

Inv - Range Invert (Range12To15[n].Invert)

Indicates the active portion of Rangen. When Range12To15[n].Invert = 0, the outputs are activated when the range value is at or between the Range12To15[n].LowLimit and Range12To15[n].HiLimOrDirWr. When Range12To15[n].Invert = 1, the outputs are activated when the range is at or outside the range limits.

<!-- image -->

The input array, which consists of 35 words, allows read-only access to the module's input data via word and bit access. The input array is described below. The functions are described in more detail in the sections following the table.

| IMPORTANT   | During the non-run states (program and fault), the module continues to update the input array (continues counting). Depending on the bus master, you may not see this.                                                 |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TIP         | Status bits for a particular counter reflect the configuration settings for that counter. To receive valid status, the counter must be enabled and the module must have stored a valid configuration for that counter. |

## Table 16 - Input Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC

| Word Bit   |                                                   |                                                               |                                                   |                                                   |                                                   |                                                   | Function                                          |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
|------------|---------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Word Bit   |                                                   | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00               |                                                   |                                                   |                                                   |                                                   | Function                                          |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 0          | Not used                                          | Not used                                                      | Not used                                          | Not used                                          | Not used                                          | Not used                                          | Z1 B1 A1 Z0 B0 A0 Input State                     | Not used                                          | Not used                                          |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 1          | Readback.0 through Readback.15                    | Readback.0 through Readback.15                                | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback                                          | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    | Readback.0 through Readback.15                    |
| 2          | InvalidRangeLimit1 2 through InvalidRangeLimit1 5 | InvalidCtrAssignToRange1 2 through InvalidCtrAssignToRange1 5 | Gen Error                                         | Invalid Output                                    | Mod Config                                        | Not used Out0Overcurrent through Out3Overcurrent  | Status Flags                                      | Not used Out0Overcurrent through Out3Overcurrent  | Not used Out0Overcurrent through Out3Overcurrent  |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 3          | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active             | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active | RangeActive.0 through RangeActive.15 Range Active |
| 4          | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                                           | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Counter 0 Current Count                           | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               | Ctr[0].CurrentCount                               |
| 5          |                                                   |                                                               |                                                   |                                                   |                                                   |                                                   | Counter 0 Current Count                           |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| 6          | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                            | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Counter 0 Stored Count                            | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                | Ctr[0].StoredCount                                |
| 7          |                                                   |                                                               |                                                   |                                                   |                                                   |                                                   | Counter 0 Stored Count                            |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |

Table 16 - Input Array - 1769-HSC Module and CMX 5370 L2 Packaged Controller Embedded HSC (Continued)

| Word Bit               |                      |                                                 |                      |                      | Function                             |                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |
|------------------------|----------------------|-------------------------------------------------|----------------------|----------------------|--------------------------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|----------------------|
|                        |                      | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 |                      |                      |                                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |
| 8                      | Ctr[0].CurrentRate   | Ctr[0].CurrentRate                              | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   | Counter 0 Current Rate               | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   | Ctr[0].CurrentRate   |
| 9                      |                      |                                                 |                      |                      |                                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |
| 10                     | Ctr[0].PulseInterval | Ctr[0].PulseInterval                            | Ctr[0].PulseInterval | Ctr[0].PulseInterval | Counter 0 Pulse Interval             | Ctr[0].PulseInterval | Ctr[0].PulseInterval | Ctr[0].PulseInterval | Ctr[0].PulseInterval | Ctr[0].PulseInterval | Ctr[0].PulseInterval | Ctr[0].PulseInterval | Ctr[0].PulseInterval | Ctr[0].PulseInterval | Ctr[0].PulseInterval |
| 11                     |                      |                                                 |                      |                      |                                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |
| 12                     | Not used             | C0PW RV                                         | Not used ID W        | Not used             | REZ CUdf COvf Counter 0 Status Flags | Not used             | Not used             | Not used             |                      |                      |                      |                      |                      |                      |                      |
| 13                     | Not used             | Not used                                        | Not used             | Not used             | Not used                             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             |
| 14                     | Ctr[1].CurrentCount  | Ctr[1].CurrentCount                             | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  | Counter 1 Current Count              | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  | Ctr[1].CurrentCount  |
| 16                     |                      |                                                 |                      |                      | Counter 1 Stored Count               |                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |
|                        | Ctr[1].StoredCount   | Ctr[1].StoredCount                              | Ctr[1].StoredCount   | Ctr[1].StoredCount   | Ctr[1].StoredCount                   | Ctr[1].StoredCount   | Ctr[1].StoredCount   | Ctr[1].StoredCount   | Ctr[1].StoredCount   | Ctr[1].StoredCount   | Ctr[1].StoredCount   | Ctr[1].StoredCount   | Ctr[1].StoredCount   | Ctr[1].StoredCount   | Ctr[1].StoredCount   |
| 18  19                 | Ctr[1].CurrentRate   | Ctr[1].CurrentRate                              | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   | Counter 1 Current Rate               | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   | Ctr[1].CurrentRate   |
| 20                     |                      |                                                 |                      |                      | Counter 1 Pulse Interval             |                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |
| 22                     | Ctr[1].PulseInterval | Ctr[1].PulseInterval                            | Ctr[1].PulseInterval | Ctr[1].PulseInterval | Ctr[1].PulseInterval                 | Ctr[1].PulseInterval | Ctr[1].PulseInterval | Ctr[1].PulseInterval | Ctr[1].PulseInterval | Ctr[1].PulseInterval | Ctr[1].PulseInterval | Ctr[1].PulseInterval | Ctr[1].PulseInterval | Ctr[1].PulseInterval | Ctr[1].PulseInterval |
|                        | Not used             | C1PW RV IC ID                                   | W                    | Not used             | REZ CUdf COvf Counter 1 Status Flags | Not used             | Not used             | Not used             |                      |                      |                      |                      |                      |                      |                      |
| 23                     | Not used             | Not used                                        | Not used             | Not used             | Not used                             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             |
| 24                     | Ctr[2].CurrentCount  | Ctr[2].CurrentCount                             | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  | Counter 2 Current Count              | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  | Ctr[2].CurrentCount  |
| 26  Ctr[2].CurrentRate |                      |                                                 |                      |                      | Rate                                 |                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |
| 27                     |                      |                                                 |                      |                      | Counter 2 Current                    |                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |
| 28                     | Not used             | C2PW RV IC ID                                   | W                    | Not use d            | CUdf COvf Counter 2 Status Flags     | Not used             | Not used             | Not used             |                      |                      |                      |                      |                      |                      |                      |
| 29                     | Not used             | Not used                                        | Not used             | Not used             | Not used                             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             | Not used             |
| 30                     | Ctr[3].CurrentCount  | Ctr[3].CurrentCount                             | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  | Counter 3 Current Count              | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  | Ctr[3].CurrentCount  |
| 32                     |                      |                                                 |                      |                      | Counter 3 Current                    |                      |                      |                      |                      |                      |                      |                      |                      |                      |                      |
|                        | Ctr[3].CurrentRate   | Ctr[3].CurrentRate                              | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   | Rate                                 | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   | Ctr[3].CurrentRate   |
| 34                     | Not used             | C3PW RV IC ID                                   | W                    | Not use d            | CUdf COvf Counter 3 Status Flags     | Not used             | Not used             | Not used             |                      |                      |                      |                      |                      |                      |                      |

## Table 17 - Input Array - L23E Packaged Controller Enbedded HSC

| Word Bit   |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                               |                         |                         |                         |                         | Function                         |                        |
|------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|-------------------------------|-------------------------|-------------------------|-------------------------|-------------------------|----------------------------------|------------------------|
| Word Bit   | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 Not used | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 Not used | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 Not used | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 Not used | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 Not used | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 Not used | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 Not used | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 Not used | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 Not used | Z1 B1 A1 Z0 B0 A0 Input State |                         |                         |                         |                         | Function                         |                        |
| 0  1       | Out 15                                                   | Out 14 Out 12                                            | Out 13                                                   | Out 11                                                   | Out 10                                                   | Out 9                                                    | Out 8                                                    | Out 7                                                    | Out 5                                                    | Out 4                         | Out 3                   | Out 2                   | Out 1                   | Out 0                   | DataEcho                         |                        |
| 2          | BadRangeLimit 3                                         | BadRangeLimit 3                                         | BadRangeLimit 3                                         | 0 BadRangeCtrNum3  0 ERR UBS MCfg                       | 0 BadRangeCtrNum3  0 ERR UBS MCfg                       | 0 BadRangeCtrNum3  0 ERR UBS MCfg                       | 0 BadRangeCtrNum3  0 ERR UBS MCfg                       | 0 BadRangeCtrNum3  0 ERR UBS MCfg                       |                                                          |                               | OverCurFdbck Output03 0 | OverCurFdbck Output03 0 | OverCurFdbck Output03 0 | OverCurFdbck Output03 0 | Status Flags                     |                        |
| 3          |                                                          | R3 R2 R1 R0                                              |                                                          | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                      |                         |                         |                         |                         | Range Active                     |                        |
| 4          | PresentCount_0                                           | PresentCount_0                                           | PresentCount_0                                           | PresentCount_0                                           | PresentCount_0                                           | PresentCount_0                                           | PresentCount_0                                           | PresentCount_0                                           | PresentCount_0                                           | PresentCount_0                | PresentCount_0          | PresentCount_0          | PresentCount_0          | PresentCount_0          | PresentCount_0                   | PresentCount_0         |
| 6          | StoredValue_0                                            | StoredValue_0                                            | StoredValue_0                                            | StoredValue_0                                            | StoredValue_0                                            | StoredValue_0                                            | StoredValue_0                                            | StoredValue_0                                            | StoredValue_0                                            | StoredValue_0                 | StoredValue_0           | StoredValue_0           | StoredValue_0           | StoredValue_0           | StoredValue_0                    | StoredValue_0          |
| 7 8        | Not used                                                 |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                               |                         |                         |                         |                         | Not used                         |                        |
| 10  11     | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                      | Not used                | Not used                | Not used                | Not used                | Not used                         | Not used               |
| 13         | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                      | Not used                | Not used                | Not used                | Not used                | Not used                         | Not used               |
| 14         |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                               |                         |                         |                         |                         |                                  |                        |
|            | PresentCount_1                                           | PresentCount_1                                           | PresentCount_1                                           | PresentCount_1                                           | PresentCount_1                                           | PresentCount_1                                           | PresentCount_1                                           | PresentCount_1                                           | PresentCount_1                                           | PresentCount_1                | PresentCount_1          | PresentCount_1          | PresentCount_1          | PresentCount_1          | PresentCount_1                   | PresentCount_1         |
| 16         | StoredValue_1                                            | StoredValue_1                                            | StoredValue_1                                            | StoredValue_1                                            | StoredValue_1                                            | StoredValue_1                                            | StoredValue_1                                            | StoredValue_1                                            | StoredValue_1                                            | StoredValue_1                 | StoredValue_1           | StoredValue_1           | StoredValue_1           | StoredValue_1           | StoredValue_1                    | StoredValue_1          |
| 17 18      | Not used                                                 |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                               |                         |                         |                         |                         | Not used                         |                        |
| 19 20      | Not used                                                 |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                               |                         |                         |                         |                         | Not used                         |                        |
| 23         | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                      | Not used                | Not used                | Not used                | Not used                | Not used                         | Not used               |
|            |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                               |                         |                         |                         |                         | Not used                         |                        |
| 24  25     | PresentCount_2                                           | PresentCount_2                                           | PresentCount_2                                           | PresentCount_2                                           | PresentCount_2                                           | PresentCount_2                                           | PresentCount_2                                           | PresentCount_2                                           | PresentCount_2                                           | PresentCount_2                | PresentCount_2          | PresentCount_2          | PresentCount_2          | PresentCount_2          | PresentCount_2                   | PresentCount_2         |
| 26         | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                                                 | Not used                      | Not used                | Not used                | Not used                | Not used                | Not used                         | Not used               |
| 27 28      |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                               |                         |                         |                         |                         |                                  |                        |
|            | Not used                                                 |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                               |                         |                         |                         |                         | CUdf COvf Counter 2 Status Flags |                        |
| 29         | C2PW RV IC BD Not used                                   | C2PW RV IC BD Not used                                   | C2PW RV IC BD Not used                                   | C2PW RV IC BD Not used                                   | C2PW RV IC BD Not used                                   | C2PW RV IC BD Not used                                   | C2PW RV IC BD Not used                                   | C2PW RV IC BD Not used                                   | C2PW RV IC BD Not used                                   | C2PW RV IC BD Not used        | C2PW RV IC BD Not used  | C2PW RV IC BD Not used  | C2PW RV IC BD Not used  | C2PW RV IC BD Not used  | Not used                         | C2PW RV IC BD Not used |
|            | W                                                        | W                                                        | W                                                        | W                                                        | W                                                        | W                                                        | W                                                        | W                                                        | W                                                        | W                             | W                       | W                       | W                       | W                       | W                                | W                      |
| 30         | PresentCount_3                                           | PresentCount_3                                           | PresentCount_3                                           | PresentCount_3                                           | PresentCount_3                                           | PresentCount_3                                           | PresentCount_3                                           | PresentCount_3                                           | PresentCount_3                                           | PresentCount_3                | PresentCount_3          | PresentCount_3          | PresentCount_3          | PresentCount_3          | PresentCount_3                   | PresentCount_3         |
| 31         |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                                                          |                               |                         |                         |                         |                         | PresentCount_3                   |                        |

Table 17 - Input Array - L23E Packaged Controller Enbedded HSC (Continued)

| Word Bit   |          |               |                                                 | Function                         |          |          |          |          |          |          |          |          |          |          |          |          |
|------------|----------|---------------|-------------------------------------------------|----------------------------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| Word Bit   |          |               | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00 | Function                         |          |          |          |          |          |          |          |          |          |          |          |          |
| 32         | Not used | Not used      | Not used                                        | Not used                         | Not used | Not used | Not used | Not used | Not used | Not used | Not used | Not used | Not used | Not used | Not used | Not used |
| 33         |          |               |                                                 |                                  |          |          |          |          |          |          |          |          |          |          |          |          |
| 34         | Not used | C3PW RV IC ID | W                                               | CUdf COvf Counter 3 Status Flags | Not used | Not used | Not used | Not used |          |          |          |          |          |          |          |          |

## Input State (InputStateA0 through InputStateZ1)

| Input Array Word 0 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |          |                   |          |          |          |          |          |          |          |          |
|----------------------------------------------------------------------|----------|-------------------|----------|----------|----------|----------|----------|----------|----------|----------|
| Input State                                                          | Not used | Z1 B1 A1 Z0 B0 A0 | Not used | Not used | Not used | Not used | Not used | Not used | Not used | Not used |

This word indicates the state of the real (physical) inputs after filtering.

- 1 = On
- 0 = Off

## Readback (Readback.0 through Readback.15)

|                                         | Input Array Word 1 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |                                         |
|-----------------------------------------|----------------------------------------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|
| Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15                              | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 | Readback Readback.0 through Readback.15 |

This input word reflects the counter's module-directed status of all 16 outputs, real and virtual.

- 1 = On
- 0 = Off

## Status Flags

## IMPORTANT

For the L23E packaged controllers embedded HSC, the ranges referred to in this section are numbered 0…3 instead of 12…15. The ranges in this section apply to only the 1769-HSC module and the CMX 5370 L2 packaged controllers embedded HSC.

|                                                              |                                                             |           |                |            |          |                                         | Input Array Word 2 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                                         |                                         |
|--------------------------------------------------------------|-------------------------------------------------------------|-----------|----------------|------------|----------|-----------------------------------------|----------------------------------------------------------------------|-----------------------------------------|-----------------------------------------|
| Status Flags InvalidRangeLimit12 through InvalidRangeLimit15 | InvalidCtrAssignToRange12 through InvalidCtrAssignToRange15 | Gen Error | Invalid Output | Mod Config | Not used | Out0Overcurrent through Out3Overcurrent | Out0Overcurrent through Out3Overcurrent                              | Out0Overcurrent through Out3Overcurrent | Out0Overcurrent through Out3Overcurrent |

## Output Overcurrent (Out0Overcurrent to Out3OverCurrent)

The output overcurrent bits are set (1) when the module is in an overcurrent condition. These bits also show whether the output is latched off, because the output remains in the off state and these bits remain on until the ResetBlownFuse bit is used.

## Module Configured (ModConfig)

Word 2, bit 5 is set by the module after it has accepted all of the configuration data. When set (1), this bit confirms that the module received and accepted valid configuration data. When reset (0), this bit indicates that the module still is checking for errors or contains errors and the old configuration is still being used.

TIP The module takes up to two seconds to validate configuration data.

## Invalid Output (InvalidOutput)

- 1 = an unused bit in the output array is set
- 0 = no unused bits in the output array are set

When this error occurs, the entire output array is rejected until an output array that does not have this error is sent.

## Error (GenError)

When this bit is set (1), it indicates one or more of the following errors for the input array:

- OutnOvercurrent
- InvalidRangeLimitn
- InvalidCtrAssignToRangen
- InvalidOutput
- Ctr[n].Overflow
- Ctr[n].Underflow
- Ctr[n].InvalidDirectWrite
- Ctr[n].InvalidCounter
- Ctr[n].PresetWarning

where n indicates the counter number.

To determine which error has set the GenError bit, identify which bit is set. This could be done by using a subroutine to examine these bits in the input array.

TIP Ctr[n].RateValid does not set the GenError bit.

Invalid Counter Assigned to Range (InvalidCtrAssignToRange12 through InvalidCtrAssignToRange15)

InvalidCtrAssignToRange12 is set when the indicated range in the output array refers to a non-existent counter.

- It is set (1) when Range12To15[n].ToThisCounter &gt; NumberOfCounters.
- It is cleared (0) when Range12To15[n].ToThisCounter  NumberOfCounters .

When this error occurs, the entire output array is rejected until a valid configuration is detected.

Invalid Range Limit (InvalidRangeLimit12 through InvalidRangeLimit15)

This bit is set when the range limits are invalid according to the limitations indicated in Range12To15[n].HiLimOrDirWr and Range12To15[n].LowLimit in the output array.

- 1 = Range limits are invalid.
- 0 = no error

When this error occurs, the entire output array is rejected until a valid configuration is detected.

## Range Active (RangeActive.0 through RangeActive.15)

|                                                   | Input Array Word 3 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
|---------------------------------------------------|----------------------------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15                    | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 | Range Active RangeActive.0 through RangeActive.15 |
|                                                   | Input Array Word 3 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |
| Range Active RA3 RA2 RA1 RA0                      |                                                                      |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |                                                   |

This word reflects the status of all of the ranges. When a count or rate meets the criteria programmed for a given range, the range is active.

- 1 = active
- 0 = inactive/false

TIP When the range is enabled and active, the output mask for that range is applied.

## Current Count (Ctr[n].CurrentCount)

| Input Array Words   | Input Array Words                              | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|---------------------|------------------------------------------------|---------------------------------------------------|
|                     | 4 Counter 0 Current Count Ctr[0].CurrentCount  |                                                   |
| 5                   | 4 Counter 0 Current Count Ctr[0].CurrentCount  |                                                   |
|                     | 14 Counter 1 Current Count Ctr[1].CurrentCount |                                                   |
| 15                  | 14 Counter 1 Current Count Ctr[1].CurrentCount |                                                   |
|                     | 24 Counter 2 Current Count Ctr[2].CurrentCount |                                                   |
| 25                  | 24 Counter 2 Current Count Ctr[2].CurrentCount |                                                   |
|                     | 30 Counter 3 Current Count Ctr[3].CurrentCount |                                                   |
| 31                  | 30 Counter 3 Current Count Ctr[3].CurrentCount |                                                   |

This is the 32-bit count value from the counter.

## Stored Count (Ctr[n].StoredCount)

| Input Array Words   | Input Array Words                            | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|---------------------|----------------------------------------------|---------------------------------------------------|
|                     | 6 Counter 0 Stored Count Ctr[0].StoredCount  |                                                   |
| 7                   | 6 Counter 0 Stored Count Ctr[0].StoredCount  |                                                   |
|                     | 16 Counter 1 Stored Count Ctr[1].StoredCount |                                                   |
| 17                  | 16 Counter 1 Stored Count Ctr[1].StoredCount |                                                   |

This is the last stored 32-bit value from counter (n). The count value is stored depending on the CtrnConfig.StorageMode and Zn inputs.

When a storage event occurs, the Ctr[n].RisingEdgeZ bit is set, indicating that the value is new. If more than one Zn occurs before the Ctr[n].RisingEdgeZ bit is reset (using the CtrnResetRisingEdgeZ bit), the Ctr[n].StoredCount word will contain only the last Ctr[n].StoredCount value. There is no indication that the data has been overwritten.

## Current Rate (Ctr[0].CurrentRate to Ctr[3].CurrentRate)

IMPORTANT

For the L23E packaged controllers embedded HSC, the current rate words do not apply; they are always returned as 0 in the input array. The rate words in this section apply to the 1769-HSC module and the CMX 5370 L2 packaged controllers embedded HSC.

| Input Array Words   | Input Array Words                            | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|---------------------|----------------------------------------------|---------------------------------------------------|
|                     | 8 Counter 0 Current Rate Ctr[0].CurrentRate  |                                                   |
| 9                   | 8 Counter 0 Current Rate Ctr[0].CurrentRate  |                                                   |
|                     | 18 Counter 1 Current Rate Ctr[1].CurrentRate |                                                   |
| 19                  | 18 Counter 1 Current Rate Ctr[1].CurrentRate |                                                   |
|                     | 26 Counter 2 Current Rate Ctr[2].CurrentRate |                                                   |
| 27                  | 26 Counter 2 Current Rate Ctr[2].CurrentRate |                                                   |
|                     | 32 Counter 3 Current Rate Ctr[3].CurrentRate |                                                   |
| 33                  | 32 Counter 3 Current Rate Ctr[3].CurrentRate |                                                   |

This 32-bit value is the current rate value, scaled by CtrnScalar, from the counter. This uses the Cyclic Rate Calculation Method. See page 32 for more information.

Rate-based ranges use this value for comparisons, even when the Ctr[n].RateValid bit is zero.

IMPORTANT This value is current only when the Ctr[n].RateValid bit is set (1).

## Pulse Interval (Ctr[0].PulseInterval and Ctr[1].PulseInterval)

IMPORTANT

For the L23E packaged controllers embedded HSC, the pulse interval words do not apply; they are always returned as 0 in the input array. The pulse interval words in this section apply to the 1769-HSC module and the CMX 5370 L2 packaged controllers embedded HSC.

| Input Array Words   | Input Array Words                                | 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00   |
|---------------------|--------------------------------------------------|---------------------------------------------------|
|                     | 10 Counter 0 Pulse Interval Ctr[0].PulseInterval |                                                   |
| 11                  | 10 Counter 0 Pulse Interval Ctr[0].PulseInterval |                                                   |
|                     | 20 Counter 1 Pulse Interval Ctr[1].PulseInterval |                                                   |
| 21                  | 20 Counter 1 Pulse Interval Ctr[1].PulseInterval |                                                   |

This is the time, in microseconds, between the last two pulses for the counter. The pulses indicated here are those transitions on which the count value can change. For example, in quadrature X1 mode, these are the successive rising edges of A only.

If more than two pulses have occurred since the value was last read, the value indicates only the time between the last two pulses that have been processed.

## Status Flags

| Input Array Words         |          | 15 14 13 12 11 10 09 08 07 06 05   | (1)            |          |          | 04 03 02 01 00               |          |          |
|---------------------------|----------|------------------------------------|----------------|----------|----------|------------------------------|----------|----------|
| 12 Counter 0 Status Flags | Not used | Not used                           | C0PW RV        | Not used | Not used | IDW REZ CUdf COvf            | Not used | Not used |
| 22 Counter 1 Status Flags | Not used | Not used                           | Not used       | Not used | Not used | C1PW RV IC IDW REZ CUdf COvf | Not used | Not used |
| 28 Counter 2 Status Flags | Not used | Not used                           | C2PW RV IC IDW | Not used | Not used | CUdf COvf                    | Not used | Not used |
| 34 Counter 3 Status Flags | Not used | Not used                           | C3PW RV IC IDW | Not used | Not used | CUdf COvf                    | Not used | Not used |

(1) Bit 05 is not used for the packaged controller.

The status bits for the counter (n) are described below.

COvf - Count Overflow (Ctr[0].Overflow to Ctr[3].Overflow)

For linear counters, this bit is set when the counter is, or has been, in an overflow condition. For ring counters, this bit is set when the counter has rolled over. COvf is reset when the CtrnResetCountOverflow bit transitions from 0 to 1.

See Counter Types on page 28 for more information about linear and ring counters.

CUdf - Count Underflow (Ctr[0].Underflow to Ctr[3].Underflow)

For linear counters, this bit is set when the counter is, or has been, in an underflow condition. For ring counters, this bit is set when the counter has rolled under. CUdf is reset when the CtrnResetCountUnderflow bit transitions from 0 to 1.

See Counter Types on page 28 for more information about linear and ring counters.

REZ - Rising Edge Z (Ctr[0].RisingEdgeZ to Ctr[1].RisingEdgeZ)

This bit is set (1) when Zn, as modified by the CtrnZInvert and CtrnZInhibit bits, has a rising edge. It is reset (0) by a 0 to 1 transition of the CtrnResetRisingEdgeZ bit in the output array. N is equal to 0 or 1 depending upon which input is used, Z0 or Z1.

IDW - Invalid Direct Write (Ctr[0].InvalidDirectWrite to Ctr[3].InvalidDirectWrite)

| IMPORTANT   | For the L23E packaged controllers Embedded HSC, the ranges referred to in this section are numbered 0…3 instead of 12…15. The ranges in this section apply to only the 1769-HSC module and the CMX 5370 L2 packaged controllers Embedded HSC.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

This bit is set when the Range12To15[n].HiLimOrDirWr is invalid. (For example, if CtrnMaxCount &lt; Range12To15[n].HiLimOrDirWr or Range12To15[n].HiLimOrDirWr &lt; CtrnMinCount.)

When this error occurs, the entire output array is rejected until a valid configuration is detected.

## IC - Invalid Counter (Ctr[1].InvalidCounter to Ctr[3].Invalid Counter)

When set (1) this bit indicates that an invalid control bit is set for the counter. Depending on the value of NumberOfCounters, the following errors will occur:

- If NumberOfCounters &lt; 1, then setting one of the control bits for Counter 1 will result in input error flag Ctr[1].InvalidCounter.
- If NumberOfCounters &lt;  2, then setting one of the control bits for Counter 2 will result in input error flag Ctr[2].InvalidCounter.
- If NumberOfCounters &lt;  3, then setting one of the control bits for Counter 3 will result in input error flag Ctr[3].InvalidCounter.

When this error occurs, the entire output array is rejected until an output array that does not have this error is sent.

The control bits are shown on page 92 .

## RV - Rate Valid (Ctr[0].RateValid to Ctr[3].RateValid)

## IMPORTANT

For the L23E packaged controllers Embedded HSC, the RV value does not apply; they are not used and are always set to 0. The RV values in this section apply to the 1769-HSC module and the CMX 5370 L2 packaged controllers Embedded HSC.

This bit is set (1) when the rate value indicated in Ctr[n].CurrentRate is current. When this bit is reset (0), Ctr[n].CurrentRate is frozen at the last known good value.

This bit is reset when the Ctr[n].Overflow or Ctr[n].Underflow bits have been set during the last CtrnCyclicRateUpdateTime period.

See page 34 for more Rate Valid reset conditions.

CnPW - Counter Preset Warning (Ctr[0]. ]. PresetWarning to Ctr[3]. ]. PresetWarning)

This bit is set when Ctr[n].CurrentCount has been forced by the module to the CtrnPreset value. This will happen when a configuration array is accepted, which sets the following:

- CtrnMinCount &gt; Ctr[n].CurrentCount or
- CtrnMaxCount &lt; Ctr[n].CurrentCount.

This bit is reset by a 0 to 1 transition of the CtrnResetCtrPresetWarning bit in the output array.

TIP You must manually reset CnPW, COvf, CUdf and REZ (but not IDW, RV or IC) to enable them to be set again.

## Safety Considerations

## Diagnostics and Troubleshooting

This chapter describes how to troubleshoot the module.

| Topic                                      |   Page |
|--------------------------------------------|--------|
| Safety Considerations                      |    109 |
| Module Operation versus Counter Operation  |    111 |
| Counter Defaults                           |    111 |
| Module Diagnostics                         |    112 |
| Non-critical versus Critical Module Errors |    113 |
| Module Error Definition                    |    114 |
| Error Codes                                |    116 |

Safety considerations are an important element of proper troubleshooting procedures. Actively thinking about the safety of yourself and others, as well as the condition of your equipment, is of primary importance.

The following sections describe several safety concerns you should be aware of when troubleshooting your control system.

<!-- image -->

ATTENTION: Never reach into a machine to actuate a switch because unexpected motion can occur and cause injury.

Remove all electrical power at the main power disconnect switches before checking electrical connections or inputs/outputs causing machine motion.

## Status Indicators

When any status indicator on the module is illuminated, it indicates that power is applied to the module.

<!-- image -->

## Stand Clear of the Machine

When troubleshooting any system problem, have all personnel remain clear of the machine. The problem could be intermittent, and sudden unexpected machine motion could occur. Have someone ready to operate an emergency stop switch in case it becomes necessary to shut off power to the machine.

## Program Alteration

There are several possible causes of alteration to the user program, including extreme environmental conditions, Electromagnetic Interference (EMI), improper grounding, improper wiring connections, and unauthorized tampering. If you suspect a program has been altered, check it against a previously saved program on an EEPROM or UVPROM memory module.

## Safety Circuits

Circuits installed on the machine for safety reasons, like over-travel limit switches, stop push buttons, and interlocks, should always be hard-wired to the master control relay. These devices must be wired in series so that when any one device opens, the master control relay is de-energized, thereby removing power to the machine. Never alter these circuits to defeat their function. Serious injury or machine damage could result.

## Module Operation versus Counter Operation

## Counter Defaults

The module performs operations at two levels:

- Module level
- Counter level

Module-level operations include functions, such as powerup, configuration, and communication with a bus master, such as a MicroLogix 1500 controller.

Counter-level operations include counter-related functions, such as data conversion and overflow or underflow detection.

Internal diagnostics are performed at both levels of operation. When detected, module error conditions are immediately indicated by the module status indicator. Both module hardware and configuration error conditions are reported to the controller. Counter overflow or underflow conditions are reported in the module's input data table. Module hardware errors are typically reported in the controller's I/O status file. Refer to your controller manual for details.

When the module powers up, all output array and configuration array values are set to their default values. See page 66 in Chapter 4 or Appendix D on page 149 for default values. All input array values are cleared. None of the module data is retained through a power cycle.

In effect, this means that power cycling clears the module with these results:

- Stored counts are lost.
- Faults and flags are cleared.
- Outputs are off.

The bus master will attempt to write program data to the output array and configuration array.

## Module Diagnostics

<!-- image -->

45272

The 176-HSC module offers power-up, configuration, and post configuration diagnostics.

## Power-up Diagnostics

At module powerup, a series of internal diagnostic tests are performed. These diagnostic tests must be successfully completed or the OK status indicator remains off and a module error results and is reported to the controller.

Table 18 - Diagnostic Indicators

| Indicator Color                              | Indicates                                                                                                                                                                                                                                                      |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 OUT                                        | Amber ON/OFF logic status of output 0                                                                                                                                                                                                                          |
| Amber ON/OFF logic status of output 1        | 1 OUT                                                                                                                                                                                                                                                          |
| 2 OUT  Amber ON/OFF logic status of output 2 |                                                                                                                                                                                                                                                                |
|                                              | Amber ON/OFF logic status of output 3                                                                                                                                                                                                                          |
| FUSE  Red                                    | Overcurrent                                                                                                                                                                                                                                                    |
| OK  Off                                      | No power is applied.                                                                                                                                                                                                                                           |
|                                              | Red (briefly) Performing self-test.                                                                                                                                                                                                                            |
|                                              | Solid Green OK, normal operating condition.                                                                                                                                                                                                                    |
|                                              | Flashing Green OK, module in Program or Fault mode.                                                                                                                                                                                                            |
| Solid Red or Amber                           | Hardware error. Cycle power to the module. If problem persists, replace the module.                                                                                                                                                                            |
|                                              | Flashing Red Recoverable fault. Reconfigure, reset, or perform error recovery. See Non-critical versus Critical Module Errors on page 113. The OK status indicator flashes red for all of the error codes in the Configuration Error Codes table on page 117 . |
| A0                                           | Amber ON/OFF status of input A0                                                                                                                                                                                                                                |
| A1                                           | Amber ON/OFF status of input A1                                                                                                                                                                                                                                |
| B0                                           | Amber ON/OFF status of input B0                                                                                                                                                                                                                                |
| B1                                           | Amber ON/OFF status of input B1                                                                                                                                                                                                                                |
| Z0                                           | Amber ON/OFF status of input Z0                                                                                                                                                                                                                                |
| Z1                                           | Amber ON/OFF status of input Z1                                                                                                                                                                                                                                |

ALL ON

Possible causes for all status indicators to be on include the following:

- Bus Error has occurred: Controller hard fault. Cycle power.
- During upgrade of controller: Normal. Do not cycle power during the upgrade.
- All status indicators will flash on briefly during power-up. This is normal.

## Non-critical versus Critical Module Errors

## Configuration Diagnostics

When a configuration is sent, the module performs a diagnostic check to see that the configuration is valid. This results in either a valid ModConfig bit or module configuration error. See the Configuration Error Codes table on page 117 for configuration error codes.

## Post Configuration Diagnostics

If the ModConfig bit in the input array is set, then the module has accepted the configuration. Now, on every scan, each channel status flag in the input array is examined. The output array is checked on each scan for compatibility with the configuration array.

The 1769-HSC module has non-critical and critical errors.

## Non-critical Errors

Non-critical module errors are typically recoverable. Non-critical error conditions are indicated by the extended error code. See the Configuration Error Codes table on page 117 for more information.

TIP

The OK status indicator will be in a flashing red state for all of the error codes in the Configuration Error Codes table on page 117 .

## Critical Errors

Critical module errors are conditions that prevent normal or recoverable operation of the system. When these types of errors occur, the system typically leaves the Run or Program mode and enters the fault mode of operation until the error can be dealt with. Critical module errors are indicated in the General Common Hardware Error Codes table on page 116 .

## Module Error Definition

Table 19 - Module Error Definition

| ‘Don’t Care’ Bits   | ‘Don’t Care’ Bits   | Module Error                          | Extended Error Information   | Extended Error Information   | Extended Error Information   | Extended Error Information   | Extended Error Information   | Extended Error Information   | Extended Error Information   | Extended Error Information   | Extended Error Information   |
|---------------------|---------------------|---------------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|------------------------------|
|                     |                     | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0 |                              |                              |                              |                              |                              |                              |                              |                              |                              |
|                     | 0000000000000000    |                                       |                              |                              |                              |                              |                              |                              |                              |                              |                              |
| Hex Digit 4         | Hex Digit 4         | Hex Digit 3                           | Hex Digit 3                  | Hex Digit 1                  | Hex Digit 1                  | Hex Digit 1                  | Hex Digit 1                  |                              |                              |                              |                              |

## Module Error Field

The purpose of the module error field is to classify module errors into three distinct groups, as described in Table 20. The type of error determines what kind of information exists in the extended error information field. These types of module errors are typically reported in the controller's I/O status file. Refer to your controller manual for details.

Table 20 - Module Error Types

| Module Error Field Value Bits 11 through 09 (Binary)   | Error Type  Description                                                                                                                                                                                                       |
|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                        | No Errors 000 No error is present. The extended error field holds no additional information.                                                                                                                                  |
|                                                        | Hardware Errors 001 General and specific hardware error codes are specified in the extended error information field.                                                                                                          |
|                                                        | Configuration Errors 010 Module-specific error codes are indicated in the extended error field. These error codes correspond to options that you can change directly. For example, the input range or input filter selection. |

## Extended Error Information Field

Check the extended error information field when a non-zero value is present in the module error field. Depending upon the value in the module error field, the extended error information field can contain error codes that are module-specific or common to all 1769 modules.

TIP

If no errors are present in the module error field, the extended error information field will be set to zero.

## Hardware Errors

General or module-specific hardware errors are indicated by module error code 1. See the General Common Hardware Error Codes table on page 116 for more information.

Module errors are expressed in two fields as four-digit Hex format, with the most significant digit as 'don't care' and irrelevant. The two fields are 'Module Error' and 'Extended Error Information'. The structure of the module error data is shown in Table 19 .

## Configuration Errors

If you set the fields in the configuration file to invalid or unsupported values, the module ignores the invalid configuration, generates a non-critical error, and keeps operating with the previous configuration.

The Configuration Error Codes table on page 117 lists the possible module-specific configuration error codes defined for the module. Correct the error by providing proper configuration data to the module.

Table 21 describes configuration errors in more general terms.

Table 21 - Error Conditions by Type of Configuration

| Programming Words Error Conditions                       |                                                                                                                                                         |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| General Configuration Bits, Filters and Safe State Words | •  Unused or Reserved bit were set. •  A counter or counters were running when the general configuration bits or filter and safe state words were sent. |
| Counter Configuration                                    | •  Unused or Reserved bit were set. •  Operational Mode is invalid for the counter. (NumberOfCounters may be incorrect.) •  Operational Mode is invalid for the counter. (mode selection may be incorrect). •  The selected counter was running when the configuration was sent. •  CtrnMaxCount  CtrnMinCount () •  CtrnHysteresis < 0 (1) C (1) •  Cyseess  CtrnScalar < 1(1) •  CtrnCyclicRateUpdateTime < 1 (1) •  The preset value is outside its valid range. (CtrnPreset not equal to or between CtrnMinCount or CtrnMaxCount) •  Counter was running when the minimum/maximum count value was changed.                                                                                                                                                         |
| Range Configuration                                      | •  Unused or Reserved bit were set.  •  Range0to11[n].HighLimit  Range0to11[n].LowLimit (1) •  Range0To11[n].ToThisCounter refers to a non-declared counter (1) (Range0To11[n].ToThisCounter > NumberOfCounters) ed  (1)                                                                                                                                                         |

(1) Does not apply to the packaged controller.

## Error Codes

The tables in this section explain the extended error codes for general common hardware errors, configuration errors, and runtime errors.

Table 22 - General Common Hardware Error Codes

| Error Type Hex                | Description Status of the                                                             |
|-------------------------------|---------------------------------------------------------------------------------------|
| Error Type Hex                | No Error X000 000 0 0000 0000 OK, normal operating condition. Solid or flashing green |
| General Common Hardware Error | X200 001 0 0000 0000 General hardware error; no additional information Solid red      |
| General Common Hardware Error | X201 001 0 0000 0001 Power-up reset state Briefly red                                 |
| General Common Hardware Error | X202 001 0 0000 0010 Bus master incompatibility Solid red                             |
| General Common Hardware Error | X203 001 0 0000 0011 General hardware error Solid red                                 |
| General Common Hardware Error | X210 001 0 0000 1010 General microprocessor error Solid red                           |
| General Common Hardware Error | X211 001 0 0000 1011 Microprocessor internal register error Solid red                 |
| General Common Hardware Error | X212 001 0 0000 1100 Microprocessor special function register error Solid red         |
| General Common Hardware Error | X213 001 0 0000 1101 Microprocessor internal memory error Solid red                   |
| General Common Hardware Error | X214 001 0 0000 1110 Microprocessor timer error Solid red                             |
| General Common Hardware Error | X215 001 0 0000 1111 Microprocessor interrupt error Solid red                         |
| General Common Hardware Error | X216 001 0 0001 0000 Microprocessor watchdog error Solid red                          |
| General Common Hardware Error | X220 001 0 0001 1000 Firmware corrupt Solid red                                       |
| General Common Hardware Error | X221 001 0 0001 1001 Firmware checksum error in non-volatile RAM Solid red            |
| General Common Hardware Error | X222 001 0 0001 1010 Firmware checksum error in RAM Solid red                         |
| General Common Hardware Error | X230 001 0 0001 1110 External RAM test error Solid red                                |
| General Common Hardware Error | X231 001 0 0001 1111 External RAM cell test error Solid red                           |
| General Common Hardware Error | X240 001 0 0010 0100 Gate array loading failed Solid red                              |
| General Common Hardware Error | X250 001 0 0011 0010 External watchdog error Solid red                                |

Table 23 - Configuration Error Codes

| Module Error Code Extended Error Information Code   | Hex Equivalent (1)  Error Description                                                                                                                                                                                            |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Binary Binary                                       |                                                                                                                                                                                                                                  |
|                                                     | X400 010 0 0000 0000 General Configuration Error No additional information                                                                                                                                                       |
|                                                     | X401 010 0 0000 0001 UnusedConfigBitSet One or more of the unused module configuration bits are set.                                                                                                                             |
|                                                     | X402 010 0 0000 0010 BadModConfigUpdate Occurs when you attempt to change a forbidden module configuration parameter while a counter or range is still enabled. See Table 24 on page 120 for a list of the forbidden parameters. |
|                                                     | X411 010 0 0001 0001 BadCounterNum_1 Nonzero configuration values were entered for Counter 1, when Counter 1 was not available.                                                                                                  |
|                                                     | X412 010 0 0001 0010 BadCounterNum_2 Nonzero configuration values were entered for Counter 2, when Counter 2 was not available.                                                                                                  |
|                                                     | X413 010 0 0001 0011 BadCounterNum_3 Nonzero configuration values were entered for Counter 3, when Counter 3 was not available.                                                                                                  |
|                                                     | X420 010 0 0010 0000 BadCounterMode_0 Operation Mode_0 is set to an invalid value. For example, value is reserved (011 or 111) or nonzero when NumberofCounters = 11.                                                            |
|                                                     | X421 010 0 0010 0001 BadCounterMode_1 Operation Mode_1 is set to an invalid value. For example, value is reserved (011 or 111) or nonzero when NumberofCounters = 10 or 11.                                                      |
|                                                     | X430 010 0 0011 0000 BadMin_0 Programmed Ctr0MinCount is greater than the Ctr0MaxCount.                                                                                                                                          |
|                                                     | X431 010 0 0011 0001 BadMin_1 Programmed Ctr1MinCount is greater than the Ctr1MinCount.                                                                                                                                          |
|                                                     | X432 010 0 0011 0010 BadMin_2 Programmed Ctr2MinCount is greater than the Ctr2MaxCount.                                                                                                                                          |
|                                                     | X433 010 0 0011 0011 BadMin_3 Programmed Ctr3MinCount is greater than the Ctr3MaxCount.                                                                                                                                          |
|                                                     | X440 010 0 0100 0000 BadPreset_0 The programmed Ctr0Preset is greater than the Ctr0MaxCount or less than the Ctr0MinCount.                                                                                                       |
|                                                     | X441 010 0 0100 0001 BadPreset_1 The programmed Ctr1Preset is greater than the Ctr1MaxCount or less than the Ctr1MinCount.                                                                                                       |
|                                                     | X442 010 0 0100 0010 BadPreset_2 The programmed Ctr2Preset is greater than the Ctr2MaxCount or less than the Ctr2MinCount.                                                                                                       |
|                                                     | X443 010 0 0100 0011 BadPreset_3 The programmed Ctr3Preset is greater than the Ctr3MaxCount or less than the Ctr3MinCount.                                                                                                       |
|                                                     | X450 010 0 0101 0000 BadHysteresis_0 The Ctr0Hysteresis value is invalid, that is, less than zero.                                                                                                                               |
|                                                     | X451 010 0 0101 0001 BadHysteresis_1 The Ctr1Hysteresis value is invalid, that is, less than zero.                                                                                                                               |
|                                                     | X452 010 0 0101 0010 BadHysteresis_2 The Ctr2Hysteresis value is invalid, that is, less than zero.                                                                                                                               |
|                                                     | X453 010 0 0101 0011 BadHysteresis_3 The Ctr3Hysteresis value is invalid, that is, less than zero.                                                                                                                               |
|                                                     | X460 010 0 0110 0000 BadScalar_0 The Ctr0Scalar value is invalid, that is, less than one.                                                                                                                                        |
|                                                     | X461 010 0 0110 0001 BadScalar_1 The Ctr1Scalar value is invalid, that is, less than one when NumberofCounters = 01, 10 or 11.                                                                                                   |

TIP

The OK status indicator flashes red for all error codes in the Configuration Error Codes table.

IMPORTANT

Only error codes X400…X443 apply to the packaged controller.

Table 23 - Configuration Error Codes (Continued)

| Module Error Code Extended Error Information Code   | Hex Equivalent (1)  Error Description                                                                                                                                                                                |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Binary Binary                                       | Hex Equivalent (1)  Error Description                                                                                                                                                                                |
|                                                     | X462 010 0 0110 0010 BadScalar_2 The Ctr2Scalar value is invalid, that is, less than one when NumberofCounters = 10 or 11.                                                                                           |
|                                                     | X463 010 0 0110 0011 BadScalar_3 The Ctr3Scalar value is invalid, that is, less than one when NumberofCounters = 11.                                                                                                 |
|                                                     | X470 010 0 0111 0000 BadScale_0 The Ctr0CyclicRateUpdateTime is invalid, that is, less than one.                                                                                                                     |
|                                                     | X471 010 0 0111 0001 BadScale_1 The Ctr1CyclicRateUpdateTime is invalid, that is, less than one when NumberofCounters = 01, 10 or 11.                                                                                |
|                                                     | X472 010 0 0111 0010 BadScale_2 The Ctr2CyclicRateUpdateTime is invalid, that is, less than one when NumberofCounters = 10 or 11.                                                                                    |
|                                                     | X473 010 0 0111 0011 BadScale_3 The Ctr3CyclicRateUpdateTime is invalid, that is, less than one when NumberofCounters = 11.                                                                                          |
|                                                     | X480 010 0 1000 0000 BadRangeLimit_0 The Range0To11[0].LowLimit is greater than or equal to the Range0To11[0].HighLimit.                                                                                             |
|                                                     | X481 010 0 1000 0001 BadRangeLimit_1 The Range0To11[1].LowLimit is greater than or equal to the Range0To11[1].HighLimit.                                                                                             |
|                                                     | X482 010 0 1000 0010 BadRangeLimit_2 The Range0To11[2].LowLimit is greater than or equal to the Range0To11[2].HighLimit.                                                                                             |
|                                                     | X483 010 0 1000 0011 BadRangeLimit_3 The Range0To11[3].LowLimit is greater than or equal to the Range0To11[3].HighLimit.                                                                                             |
|                                                     | X484 010 0 1000 0100 BadRangeLimit_4 The Range0To11[4].LowLimit is greater than or equal to the Range0To11[4].HighLimit.                                                                                             |
|                                                     | X485 010 0 1000 0101 BadRangeLimit_5 The Range0To11[5].LowLimit is greater than or equal to the Range0To11[5].HighLimit.                                                                                             |
|                                                     | X486 010 0 1000 0110 BadRangeLimit_6 The Range0To11[6].LowLimit is greater than or equal to the Range0To11[6].HighLimit.                                                                                             |
|                                                     | X487 010 0 1000 0111 BadRangeLimit_7 The Range0To11[7].LowLimit is greater than or equal to the Range0To11[7].HighLimit.                                                                                             |
|                                                     | X488 010 0 1000 1000 BadRangeLimit_8 The Range0To11[8].LowLimit is greater than or equal to the Range0To11[8].HighLimit.                                                                                             |
|                                                     | X489 010 0 1000 1001 BadRangeLimit_9 The Range0To11[9].LowLimit is greater than or equal to the Range0To11[9].HighLimit.                                                                                             |
|                                                     | X48A 010 0 1000 1010 BadRangeLimit_10 The Range0To11[10].LowLimit is greater than or equal to the Range0To11[10].HighLimit.                                                                                          |
|                                                     | X48B 010 0 1000 1011 BadRangeLimit_11 The Range0To11[11].LowLimit is greater than or equal to the Range0To11[11].HighLimit.                                                                                          |
|                                                     | X490 010 0 1001 0000 BadCtrAssignToRange_0 This error occurs if you try to set Range0To11[0].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected). |
|                                                     | X491 010 0 1001 0001 BadCtrAssignToRange_1 This error occurs if you try to set Range0To11[1].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected). |
|                                                     | X492 010 0 1001 0010 BadCtrAssignToRange_2 This error occurs if you try to set Range0To11[2].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected). |

Table 23 - Configuration Error Codes (Continued)

| Module Error Code Extended Error Information Code   | Hex Equivalent (1)  Error Description                                                                                                                                                                                  |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Binary Binary                                       | Hex Equivalent (1)  Error Description                                                                                                                                                                                  |
|                                                     | X493 010 0 1001 0011 BadCtrAssignToRange_3 This error occurs if you try to set Range0To11[3].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected).   |
|                                                     | X494 010 0 1001 0100 BadCtrAssignToRange_4 This error occurs if you try to set Range0To11[4].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected).   |
|                                                     | X495 010 0 1001 0101 BadCtrAssignToRange_5 This error occurs if you try to set Range0To11[5].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected).   |
|                                                     | X496 010 0 1001 0110 BadCtrAssignToRange_6 This error occurs if you try to set Range0To11[6].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected).   |
|                                                     | X497 010 0 1001 0111 BadCtrAssignToRange_7 This error occurs if you try to set Range0To11[7].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected).   |
|                                                     | X498 010 0 1001 1000 BadCtrAssignToRange_8 This error occurs if you try to set Range0To11[8].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected).   |
|                                                     | X499 010 0 1001 1001 BadCtrAssignToRange_9 This error occurs if you try to set Range0To11[9].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected).   |
|                                                     | X49A 010 0 1001 1010 BadCtrAssignToRange_10 This error occurs if you try to set Range0To11[10].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected). |
|                                                     | X49B 010 0 1001 1011 BadCtrAssignToRange_11 This error occurs if you try to set Range0To11[11].ToThisCounter to an invalid value (that is, to a counter that is not available due to the number of counters selected). |

The BadModConfigUpdate error conditions are shown in the following table. They occur when you attempt to change a forbidden module configuration parameter while a counter or range is still enabled. To recover from this situation, do the following:

- Correct the configuration problem.
- Reconfigure the module.

TIP

Refer to your controller's documentation for available reconfiguration methods.

IMPORTANT

Do not change the module settings in Table 24 while counter or range is enabled.

Table 24 - 'BadModConfigUpdate' Error Prohibited Configuration Settings

| Configuration Parameters                |                          | Array Position Prohibited from changing when indicated bits (X) are set   | Array Position Prohibited from changing when indicated bits (X) are set   | Array Position Prohibited from changing when indicated bits (X) are set   | Array Position Prohibited from changing when indicated bits (X) are set   | Array Position Prohibited from changing when indicated bits (X) are set   |
|-----------------------------------------|--------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Configuration Parameters                |                          |                                                                           |                                                                           |                                                                           | Word Bit Ctr0EN Ctr1EN Ctr2EN Ctr3EN RangeEN                              |                                                                           |
| OverCurrentLatchOff                     |                          |                                                                           | 0 0 X X X X X                                                             |                                                                           |                                                                           |                                                                           |
| ProgToFaultEn                           | 0 4                      |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |
| NumberOfCounters                        | 0 8 and 9 X X X X X      |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |
| Filter_A0                               | 1 0 and 1 X              |                                                                           |                                                                           | X                                                                         |                                                                           |                                                                           |
| Filter_B0                               | 1 3 and 4 X              |                                                                           |                                                                           | X                                                                         |                                                                           |                                                                           |
| Filter_Z0                               | 1 6 and 7 X              |                                                                           |                                                                           | X                                                                         |                                                                           |                                                                           |
| Filter_A1                               | 1 8 and 9                |                                                                           | X X                                                                       |                                                                           |                                                                           |                                                                           |
| Filter_B1                               | 1 11 and 12              |                                                                           | X X                                                                       |                                                                           |                                                                           |                                                                           |
| Filter_Z1                               | 1 14 and 15              |                                                                           | X X                                                                       |                                                                           |                                                                           |                                                                           |
| OutnProgramMode                         | 2 0 to 3                 |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |
| OutnProgramStateRun                     | 2 4 to 7                 |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |
| OutnProgramValue                        | 3 0 to 3                 |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |
| Outn0FaultMode                          | 4 0 to 3                 |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |
| OutnFaultStateRun                       | 4 4 to 7                 |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |
| OutnFaultValue                          | 5 0 to 3                 |                                                                           |                                                                           |                                                                           |                                                                           |                                                                           |
| Ctr0MaxCount Ctr0MinCount Ctr0Preset(1) | 6 and 7 8 and 9 -- -- -- | X X                                                                       |                                                                           |                                                                           |                                                                           |                                                                           |
|                                         | 10 and 11                | (1)                                                                       |                                                                           |                                                                           |                                                                           |                                                                           |
| Ctr0Hysteresis (2)                      | 12 --                    | X                                                                         |                                                                           |                                                                           |                                                                           |                                                                           |
| Ctr0Scalar(2)                           | 13 --                    | X                                                                         |                                                                           |                                                                           |                                                                           |                                                                           |
| Ctr0CyclicRateUpdateTime (2)            | 14 --                    | X                                                                         |                                                                           |                                                                           |                                                                           |                                                                           |
| Ctyr0Config.OperationMode               | 15 0 to 3                | X                                                                         |                                                                           |                                                                           |                                                                           |                                                                           |
| Ctr0Config.StorageMode                  | 15 8 to 10               | X                                                                         |                                                                           |                                                                           |                                                                           |                                                                           |
| Ctr0Config.Linear                       | 15 12                    | X                                                                         |                                                                           |                                                                           |                                                                           |                                                                           |

Table 24 - 'BadModConfigUpdate' Error Prohibited Configuration Settings (Continued)

| Configuration Parameters     |           |         | Array Position Prohibited from changing when indicated bits (X) are set   | Array Position Prohibited from changing when indicated bits (X) are set   | Array Position Prohibited from changing when indicated bits (X) are set   | Array Position Prohibited from changing when indicated bits (X) are set   | Array Position Prohibited from changing when indicated bits (X) are set   |
|------------------------------|-----------|---------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|
|                              |           |         |                                                                           |                                                                           |                                                                           |                                                                           | Word Bit Ctr0EN Ctr1EN Ctr2EN Ctr3EN RangeEN                              |
| Ctr1MaxCount                 | 16 and 17 | --      |                                                                           | X                                                                         |                                                                           |                                                                           |                                                                           |
| Ctr1MinCount                 | 18 and 19 | --      |                                                                           | X                                                                         |                                                                           |                                                                           |                                                                           |
| Ctr1Preset(1)                | 20 and 21 | --      |                                                                           | (1)                                                                       |                                                                           |                                                                           |                                                                           |
| Ctr1Hysteresis (2)           | 22        | --      |                                                                           | X                                                                         |                                                                           |                                                                           |                                                                           |
| Ctr1Scalar(2)                | 23        | --      |                                                                           | X                                                                         |                                                                           |                                                                           |                                                                           |
| Ctr1CyclicRateUpdateTime (2) | 24        | --      |                                                                           | X                                                                         |                                                                           |                                                                           |                                                                           |
| Ctr1Config.OperationalMode   | 25        | 0 to 3  |                                                                           | X                                                                         |                                                                           |                                                                           |                                                                           |
| Ctr1Config.StorageMode       | 25        | 8 to 10 |                                                                           | X                                                                         |                                                                           |                                                                           |                                                                           |
| Ctr1Config.Linear            | 25        | 12      |                                                                           | X                                                                         |                                                                           |                                                                           |                                                                           |
| Ctr2MaxCount                 | 26 and 27 | --      |                                                                           |                                                                           | X                                                                         |                                                                           |                                                                           |
| Ctr2MinCount                 | 28 and 29 | --      |                                                                           |                                                                           | X                                                                         |                                                                           |                                                                           |
| Ctr2Preset(1)                | 30 and 31 | --      |                                                                           |                                                                           | (1)                                                                       |                                                                           |                                                                           |
| Ctr2Hysteresis (2)           | 32        | --      |                                                                           |                                                                           | X                                                                         |                                                                           |                                                                           |
| Ctr2Scalar(2)                | 33        | --      |                                                                           |                                                                           | X                                                                         |                                                                           |                                                                           |
| Ctr2CyclicRateUpdateTime (2) | 34        | --      |                                                                           |                                                                           | X                                                                         |                                                                           |                                                                           |
| Ctr2Config.Linear            | 35        | 12      |                                                                           |                                                                           | X                                                                         |                                                                           |                                                                           |
| Ctr3MaxCount                 | 36 and 37 | --      |                                                                           |                                                                           |                                                                           | X                                                                         |                                                                           |
| Ctr3MinCount                 | 38 and 39 | --      |                                                                           |                                                                           |                                                                           | X                                                                         |                                                                           |
| Ctr3Preset(1)                | 40 and 41 | --      |                                                                           |                                                                           |                                                                           | (1)                                                                       |                                                                           |
| Ctr3Hysteresis (2)           | 42        | --      |                                                                           |                                                                           |                                                                           | X                                                                         |                                                                           |
| Ctr3Scalar(2)                | 43        | --      |                                                                           |                                                                           |                                                                           | X                                                                         |                                                                           |
| Ctr3CyclicRateUpdateTime (2) | 44        | --      |                                                                           |                                                                           |                                                                           | X                                                                         |                                                                           |
| Ctr3Config.Linear            | 45        | 12      |                                                                           |                                                                           |                                                                           | X                                                                         |                                                                           |
|                              |           |         | Ranges 46 to 117 -- Can be changed wile counters and ranges are enabled   | Ranges 46 to 117 -- Can be changed wile counters and ranges are enabled   | Ranges 46 to 117 -- Can be changed wile counters and ranges are enabled   | Ranges 46 to 117 -- Can be changed wile counters and ranges are enabled   | Ranges 46 to 117 -- Can be changed wile counters and ranges are enabled   |

(1) CtrnPreset can be changed while CtrnEn = 1.

(2) Does not apply to the L23E packaged controllers embedded HSC.

## Notes:

## Specifications

| IMPORTANT   | For specifications for the packaged controllers, refer to the CompactLogix Packaged Controller Installation Instructions, publication 1769-IN082 .   |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------|

Table 25 - Technical Specifications - 1769-HSC

| Attribute                               | 1769-HSC                                                                                                                                |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Dimensions (H x W x D), approx.         | 118 x 35 x 87 mm (4.65 x 1.38 x 3.43 in.) Height including mounting tabs is 138 mm (5.43 in.)                                           |
| Shipping weight (with carton), .        | 309 g (0.681 lb)                                                                                                                        |
| Bus current draw, max                   | 425 mA at 5V DC 0 mA at 24V DC                                                                                                          |
| Heat dissipation                        | 6.21 W The Watts per point, plus the minimum Watts, with all points energized                                                           |
| Isolation voltage                       | 75V (continuous), reinforced Insulation type, channel-to-system and channel-to-channel Type tested at 1200V AC for 2 s                  |
| All supply power and/or current ratings | Input: 30V DC 40 °C (104 °F ) Output: 1 A per channel, 4 A per module, 30V DC 40 °C (104 °F )                                           |
| Power supply distance rating            | Module cannot be more than four modules away from a system power supply                                                                 |
| Recommended cable                       | Individually shielded, twisted-pair cable (for the type recommended by the encoder or sensor manufacturer)                              |
| Wire size                               | 0.32…2.1 mm 2  (22…14 AWG) solid copper wire or 0.32…1.3 mm 2  (22…16 AWG) stranded copper wire rated at 90 °C (194 °F ) insulation max |
|                                         | Wiring category 2 - on signal ports (1)                                                                                                 |
| Vendor ID code                          | 1                                                                                                                                       |
| Product type code                       | 109                                                                                                                                     |
| Product code                            | 19                                                                                                                                      |
| Enclosure type rating                   | None (open-style)                                                                                                                       |
| North American temp code                | T3C                                                                                                                                     |

<!-- image -->

Table 26 - Input Specifications - 1769-HSC

| Attribute                      | 1769-HSC                               |
|--------------------------------|----------------------------------------|
| No. of inputs                  | 2 quadrature (ABZ) differential inputs |
| Input voltage range            | 2.6…30V DC (1)                         |
| On-state voltage, max          | 30V DC (1)                             |
| On-state voltage, min          | 2.6 V DC                               |
| On-state current, min          | 6.8 mA                                 |
| Off-state voltage, max         | 1.0V DC                                |
| Off-state current, max         | 1.5 mA                                 |
| Off-state leakage current, max | 1.5 mA                                 |
| Input current, max             | 15 mA                                  |
| Input current, min             | 6.8 mA                                 |
| Input impedance, nom           | 1950                                  |
| Pulse width, min               | 250 nsec                               |
| Pulse separation, min          | 131 nsec                               |
| Input frequency, max           | 1 MHz                                  |

Table 27 - Output Specifications - 1769-HSC

| Attribute                      | 1769-HSC                             |
|--------------------------------|--------------------------------------|
| No. of outputs                 | 16 total, 4 physical and 12 virtual  |
| Output voltage range           | 5…30V DC (1)                         |
| On-state voltage, max          | User power - 0.1V DC                 |
| On-state current, max          | 1 A per point (2) 4 A per module (3) |
| On-state current, min          | 1 mA                                 |
| On-state voltage drop, max     | 0.5V DC                              |
| Off-state leakage current, max | 5 µA                                 |
| Input current, min             | 6.8 mA                               |
| Turn-on time, max              | 400 µs (4)                           |
| Turn-off time, max             | 200 µs                               |
| Reverse polarity protection    | 30V DC                               |

Table 28 - Environmental Specifications - 1769-HSC

| Attribute                                                                                                                                                                                                  | 1769-HSC                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Nb, Operating Thermal Shock)                                             | 0…60 °C (32…140 °F)                                                                                                                                                  |
| Temperature, surrounding air, max For UL certified open equipment                                                                                                                                          | 40 °C (104 °F)                                                                                                                                                       |
| Temperature, nonoperating IEC 60068-2-1 (Test Ab, Unpackahed Nonoperating Cold), IEC 60068-2-2 (TestBb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock) | -40…85 °C (-40…185 °F)                                                                                                                                               |
| Relative humidity IEC 60068-2-3e0 (Test Db, Unpackaged Damp Heat)                                                                                                                                          | 5...95% noncondensing                                                                                                                                                |
| Vibration, operating IEC 60068-2-6 (Test Fc, Operating)                                                                                                                                                    | 5 g @ 10…500 Hz, peak-to-peak                                                                                                                                        |
| Vibration, relay operation                                                                                                                                                                                 | 2 g @ 10…500 Hz (1)                                                                                                                                                  |
| Shock, operating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                                | 30 g, 11 ms panel mounted 20 g, 11 ms DIN rail mounted                                                                                                               |
| Shock, nonoperating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                             | 40 g, panel mounted 30 g, DIN rail mounted                                                                                                                           |
| Emissions CISPR 11                                                                                                                                                                                         | Group 1, Class A                                                                                                                                                     |
| ESD immunity IEC 61000-4-2                                                                                                                                                                                 | 6 kV contact discharges 8 kV air discharges                                                                                                                          |
| Radiated RF immunity IEC 6100-4-3                                                                                                                                                                          | 10V/m with 1 kHz sine-wave 80% AM from 80…2000 MHz 10V/m with 200 Hz 50% Pulse 100% AM at 900 and 1890 MHz 10V/m with 1 kHz sine-wave 80% AM from 2000…2700 MHz      |
| EFT/B immunity IEC 61000-4-4                                                                                                                                                                               | ±2 kV at 5 kHz on power ports ±2 kV at 5 kHz on signal ports                                                                                                         |
| Surge transient immunity IEC 61000-4-5                                                                                                                                                                     | ±1 kV line-line (DM) and ±2 kV line-earth (CM) on power ports ±1 kV line-line (DM) and ±2 kV line-earth (CM) on signal ports ±1 kV line-earth (CM) on shielded ports |
| Conducted RF immunity IEC 61000-4-6                                                                                                                                                                        | 10V rms with 1 kHz sine-wave 80% AM from 150 kHz…80 MHz                                                                                                              |

## Table 29 - Certifications - 1769-HSC(1)

| Certification(2)   | 1769-HSC                                                                                                                                                                                                             |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                    | c-UL-us UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584                                                                                                                      |
|                    | c-UL-us UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E321922                                                                                      |
|                    | CE European Union 2004/108/EC EMC Directive, compliant with the following: •  EN 61000-6-2; Industrial Immunity •  EN 61000-6-4; Industrial Emissions •  EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) |
| C-Tick             | Australian Radiocommunications Act, compliant with AS/NZS CISPR 11; Industrial Emissions                                                                                                                             |

## Throughput and Timing

| Operation     | Description                                                                                                                                                  | Timing                                                |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
|               | Input file update time The delay between the time the module receives a pulse and when the Compact bus count value is updated.                               | 500 µs, max                                           |
|               | Output turn-on time The time it takes for the real output to reach 90% output voltage after commanded by the module, not including processor scan time.      | 400 µs, max                                           |
|               | Output turn-off time The time it takes for the real output to reach 10% output voltage after commanded by the module, not including the processor scan time. | 200 µs, max                                           |
| Rate accuracy | The accuracy of the reported rate as compared to actual input rate in the equation: reported rate/actual input rate.                                         | Depends on frequency. See Rate Accuracy on page 127 . |

## Rate Accuracy

The following graph shows rate error at various frequencies. The following trends can assist you in reading the graph:

- Of the lines that rise at low frequencies, the left-most is a 10-second update time (CtrnCyclicRateUpdateTime = 10000).
- The right-most of these lines is a 1-millisecond update time (CtrnCyclicRateUpdateTime = 1).
- The line that rises at high frequencies illustrates Ctr[n].PulseInterval.

Figure 21 - Rate Errors Comparison

<!-- image -->

## Temperature Derating

Refer to the following figures for 1769-HSC temperature derating.

Figure 22 - Maximum Input Voltage - 24V DC Operation

Voltage Derating Based on Temperature

<!-- image -->

45204

| Temperature          | Derated Voltage (1)   |
|----------------------|-----------------------|
| 0…40 °C (-32…104 °F) | 30V DC                |
| 55 °C (131 °F)       | 26.4V DC              |
| 60 °C (140 °F)       | 5V DC                 |

For input voltages greater than 24V DC, usea½W resistor with value: 125 x (Vin - 5V).

Figure 23 - Maximum Output Voltage - 24V DC Operation

Voltage Derating Based on Temperature

<!-- image -->

| Temperature           | Derated Voltage   |
|-----------------------|-------------------|
| 0…40 °C (-32…104 °F)  | 30V DC            |
| 55…60 °C (131…140 °F) | 26.4V DC          |

Figure 24 - Maximum Output Current per Point - 5V DC Operation

Current Derating Based on Temperature

Figure 25 - Maximum Output Current per Module - 5V DC Operation

<!-- image -->

| Temperature          | Derated Current   |
|----------------------|-------------------|
| 0…40 °C (-32…104 °F) | 1 A               |
| 60 °C (140 °F)       | 0.5 A             |

Current Derating Based on Temperature

<!-- image -->

| Temperature          | Derated Current   |
|----------------------|-------------------|
| 0…40 °C (-32…104 °F) | 4 A               |
| 60 °C (140 °F)       | 2.0 A             |

Figure 26 - Maximum Output Current per Point - 24V DC Operation

Current Derating Based on Temperature

Figure 27 - Maximum Output Current per Module - 24V DC Operation

<!-- image -->

| Temperature          | Derated Current   |
|----------------------|-------------------|
| 0…40 °C (-32…104 °F) | 1 A               |
| 55 °C (131 °F)       | 0.5 A             |
| 60 °C (140 °F)       | 0.25 A            |

Current Derating Based on Temperature

<!-- image -->

| Temperature          | Derated Current   |
|----------------------|-------------------|
| 0…40 °C (-32…104 °F) | 4 A               |
| 55 °C (131 °F)       | 2 A               |
| 60 °C (140 °F)       | 1 A               |

## Dimensions

See page 51 in Chapter 3 for these dimensions:

- Compact I/O module with CompactLogix controller and power supply
- Compact I/O module with MicroLogix 1500 base unit and processor

## System Diagram

<!-- image -->

## Program a 1769-HSC Module, CompactLogix Controller, and 845F Incremental Encoder with RSLogix 5000 Software

The application example demonstrates how to wire an 845F optical incremental encoder to a 1769-HSC module and ultimately monitor the Current Count value in the CompactLogix controller. We also will control two onboard outputs with two ranges.

<!-- image -->

|   Slot | Module       |
|--------|--------------|
|      0 | 1769-L32E    |
|      1 | 1769-IQ6XOW4 |
|      2 | 1769-OV16    |
|      3 | 1769-IF4     |
|      4 | 1769-HSC     |

## 845F Encoder Wiring to the 1769-HSC Module

## Scope

| 845F Encoder Wire     | Color 1769-HSC Terminal   |
|-----------------------|---------------------------|
| Blue/black wire pair  | Blue A0+                  |
|                       | Black A0-                 |
| White/black wire pair | White B0+                 |
|                       | Black B0-                 |
| Green/black wire pair | Green Z0+                 |
|                       | Black Z0-                 |
| Red/black wire pair   | Red 24V DC power supply   |
|                       | Black 24V DC common       |

These steps are used in this example.

1. Add the 1769-HSC module into a CompactLogix system by using RSLogix 5000 software.
2. Configure the 1769-HSC module by entering configuration information into Configuration and Output tags created in RSLogix 5000 software for the 1769-HSC module.
3. Monitor the Current Count value from the 1769-HSC module in the Input Tag created for the module.
4. Verify that module outputs 0 and 1 turn on when the Current Counts value is within the specified ranges.

## Add a 1769-HSC Module to a CompactLogix System

The example in this section uses a 1769-L32E controller to add a 1769-HSC Module into the CompactLogix System by using RSLogix 5000 software.

1. Start the RSLogix 5000 programming software.
2. The Quick Start window appears.
2. Click New Project.
3. Choose your controller and revision number.
4. Enter a unique controller name.
5. Click OK.

<!-- image -->

The RSLogix 5000 project window appears.

<!-- image -->

6. Right-click CompactBus Local and select New Module.

<!-- image -->

The Select Module dialog box appears.

7. Select the left-most I/O module in your 1769 CompactLogix chassis and click OK.

<!-- image -->

The New Module dialog box appears.

8. In the Name box, type a name and click OK.

The module is added to the I/O Configuration.

<!-- image -->

9. Repeat steps 6 through 8 until all of your local I/O modules are added in order from left to right.

<!-- image -->

In this example, the 1769-IF4 and 1769-HSC /B modules must be configured. For information on configuring the 1769-IF4 module, refer to the Compact I/O Analog Modules User Manual, publication 1769-UM002 .

## Configure the 1769-HSC Module

When the 1769-HSC module is added to the CompactLogix project, input, output, and configuration tags are automatically created in the Controller Tags area.

1. In the Controller Organizer, double-click the 1769-HSC module.

The Module Properties dialog box appears.

2. Click the Input Configuration tab.
3. The Number of Counters defaults to 2.

<!-- image -->

IMPORTANT The contents of counter 1 must be cleared to save any changes if the number of counters is changed to 1.

4. Click the Reset Counter box to select the designated number of counters for the reset counter functionality.

You select the actual counter on the Counter Configuration dialog box.

5. Click the Counter Configuration tab.

6. Use this information to complete the Counter Configuration tab.

| Option  Value                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maximum Count  1,200,000                                                                                                                                                                                                                                                      |
| Minimum Count  0                                                                                                                                                                                                                                                              |
| Preset 0                                                                                                                                                                                                                                                                      |
| Hysteresis 0                                                                                                                                                                                                                                                                  |
| Scalar 1                                                                                                                                                                                                                                                                      |
| Update Time 1                                                                                                                                                                                                                                                                 |
| Operation Mode Choose an operation mode from the pull-down menu, such as Pulse Internal Direction.                                                                                                                                                                            |
| Counter Reset Enable This box displays for 1769-HSC/B modules only . The checkbox defaults with a check mark if the selection bit is enabled for this counter on the Add-On profile. Clear the checkbox to disable this counter from resetting. See page 73 for more details. |
| Storage Mode Nothing selected                                                                                                                                                                                                                                                 |
| Counter Mode Ring Counter                                                                                                                                                                                                                                                     |

Your Counter Configuration tab should look like the example.

<!-- image -->

7. Click Apply.
8. Click the Output Configuration tab.

9. Use this information to complete the Output Configuration tab.

<!-- image -->

| Option             | Value                                                      | Value       |
|--------------------|------------------------------------------------------------|-------------|
|                    | Range 0                                                    | Range 1     |
| Type               | Count Value                                                | Count Value |
| Counter            | 0                                                          | 0           |
| High Limit 600,000 |                                                            | 1,200,000   |
| Low Limit 500,000  |                                                            | 1,000,000   |
|                    | Output Control 2#0000_0000_0000_0001 2#0000_0000_0000_0010 |             |

Your Output Configuration tab should look like the example.

10. Click Apply.

<!-- image -->

11. In the Controller Organizer, double-click Controller Tags.
12. At the bottom of the window, click Monitor Tags.

The tags for I/O modules appear in the following format, where 's' is the slot number of the module.

| Tag       | Description        |
|-----------|--------------------|
| Local:s:I | Input Image        |
| Local:s:O | Output Image       |
| Local:s:C | Configuration Data |

13. Click '+' to expand the output tags (Local:4:0).
14. Use this information to configure these output tags.
- (1) Changing this bit to a 1 changes the CtrOEn tag to 1 when you press Tab.

| Tag            | Value                    |
|----------------|--------------------------|
| OutputOnMask   | 2#0000_0000_0000_0000    |
| OutputOffMask  | 2#0000_0000_0000_0011    |
| RangeEn        | 2#0000_0000_0000_0011    |
| ResetBlownFuse | 0                        |
| Ctr0           | 2#0000_0000_0000_0001(1) |

Your output tags should look like the example.

<!-- image -->

## Monitor the Current Count and Verify Output Operation

In this section, you use the 1769-HSC module's input tags (Local:4:I) to view what is running.

1. Save the program and download it to your controller.
2. Put the controller into Run mode.
3. Spin the shaft on your 845F encoder.

The Ctr0CurrentCount tag displays the current count data for Counter0 of the 1769-HSC module. For this example, this count is the number of pulses received from the encoder times four (because the operating mode is Encoder X4).

| Name                         | 色 Value           | Style   | DataType   |
|------------------------------|--------------------|---------|------------|
| +-Local:4:1.RangeActive      | 2#0000000000000000 | Binary  | INT        |
| +-Local:4:1.Ctr0CurrentCount |                    | Decimal | DINT       |
| +-Local:4:1.Ctr0StoredCount  | 0                  | Decimal | DINT       |
| +-Local:4:l.Ctr0CurrentRate  | 0                  | Decimal | DINT       |

4. Continue to spin the encoder shaft until the Ctr0CurrentCount value is within the limits set for Range 0 (500,000–600,000).

The lowest bit of the RangeActive tag turns on.

| Name                         | 色                 |         | Style   | Data Type   |
|------------------------------|--------------------|---------|---------|-------------|
| ±-Local:4:1.RangeActive      | 2#0000000000000001 |         | Binary  | INT         |
| ±-Local:4:l.CtrOCurrentCount |                    | 0000529 | Decimal | DINT        |
| ±-Local:4:1.Ctr0StoredCount  |                    | =       | Decimal | DINT        |
| +-l ncal4·lChrnCurrentRate   |                    |         | Merimal | DINT        |

InputStates A0, B0, and Z0 toggle on and off reflecting the state of the encoder signals on those inputs as the encoder shaft is moved.

5. Continue to spin the encoder shaft until the Ctr0CurrentCount value is within the limits set for Range 1 (1,000,000–1,200,000) turns bit 1 of the RangeActive tag on.

Your 1769-HSC module and encoder are programmed.

<!-- image -->

| Name                   | Value ←             | Style   | Data Type   |
|------------------------|---------------------|---------|-------------|
| -Local:4:C             | (...}               |         | AB:1769_HS0 |
| -Local:4:1             | (...}               |         | AB:1769_HSC |
| -Local:4:1.Fault       | 2#000000000000000.. | Binary  | DINT        |
| -Local:4:l.lnputState  | 2#00000000          | Binary  | SINT        |
| Local:4:l.lnputStateA0 | 1                   | Decimal | BOOL        |
| Local:4:1.lnputStateB0 | 1                   | Decimal | BOOL        |
| Local:4:1.lnputStateZ0 | 1                   | Decimal | BOOL        |
| Local:4:1.lnputStateA1 | 0                   | Decimal | BOOL        |
| Local:4:1.InputStateB1 | 0                   | Decimal | BOOL        |
| Local:4:1.InputStateZ1 | 0                   | Decimal | BOOL        |
| +-1ncal4-1Readhack     | 2#0000000000000000  | Rinaru  | INT         |

## System Diagram

<!-- image -->

## Program a 1769-HSC Module, MicroLogix 1500 Controller, and 845F Incremental Encoder with RSLogix 500 Software

This application example demonstrates how to wire an 845F optical incremental encoder to a 1769-HSC module and ultimately monitor the Current Count value in the MicroLogix 1500 controller. We also will control two onboard outputs with two ranges.

## IMPORTANT

The individual counter reset functionality in the 1769-HSC/B module applies only to CompactLogix controllers. You cannot use the individual counter reset functionality with MicroLogix controllers.

<!-- image -->

## 845F Encoder Wiring to the 1769-HSC Module

## Scope

| 845F Encoder Wire     | Color 1769-HSC Terminal   |
|-----------------------|---------------------------|
| Blue/Black Wire Pair  | Blue A0+                  |
|                       | Black A0-                 |
| White/Black Wire Pair | White B0+                 |
|                       | Black B0-                 |
| Green/Black Wire Pair | Green Z0+                 |
|                       | Black Z0-                 |
| Red/Black Wire Pair   | Red 24V DC Power Supply   |
|                       | Black 24V DC Common       |

These steps are used in this example.

1. Add the 1769-HSC module into a MicroLogix 1500 system by using RSLogix 500 software.
2. Configure the 1769-HSC module by entering configuration information into I/O Configuration created in RSLogix 500 software for the 1769-HSC module.
3. Monitor the Current Count value from the 1769-HSC module.
4. Verify that module outputs 0 and 1 turn on when the Current Count value is within the specified ranges.

## Add a 1769-HSC Module to a MicroLogix 1500 System

The example in this section uses a MicroLogix 1500 controller to add a 1769-HSC module into the MicroLogix 1500 system by using RSLogix 500 software.

1. Start the RSLogix 500 software.
2. Click New.

The Select Processor Type dialog box appears.

<!-- image -->

3. Select the correct controller type (Bul.1764 MicroLogix 1500 LRP Series C, for this example).
4. Type a Processor Name and click OK.

The project window appears.

<!-- image -->

5. To add I/O modules to your project, click I/O Configuration.

The I/O Configuration dialog box appears.

<!-- image -->

This dialog box displays all 1769 I/O modules supported by your MicroLogix 1500 controller.

6. To add the 1769-HSC module to your MicroLogix 1500 system, double-click the module or drop and drag the module to the correct slot (in this example, slot 1).

<!-- image -->

To continue with configuring the 1769-HSC module, do not close this dialog box.

## Configure Your 1769-HSC Module

You configure the 1769-HSC module in an offline project and then download to the MicroLogix 1500 controller.

1. To open the 1769-HSC-module configuration file, click Adv Config.
2. To display the counter configuration information with the default values, click the Counters Tab.
3. Use this information to complete the configuration for the Counters tab.

<!-- image -->

| Option                          | Value                                                                                                      |
|---------------------------------|------------------------------------------------------------------------------------------------------------|
| # of Counters                   | 2 (default) Counter 1 contents must be cleared to store changes if the number of counters is changed to 1. |
| Operational Mode                | (Quadrature) Encoder X 4                                                                                   |
| Max Count                       | 1,200,000                                                                                                  |
| Min Count                       | 0                                                                                                          |
| Preset                          | 1                                                                                                          |
| Update Time                     | 1                                                                                                          |
| Count Behavior on Configuration | Retained                                                                                                   |
| Hysteresis:                     | 0                                                                                                          |
| RPM Scale Factor                | 1                                                                                                          |
| Storage Mode                    | All unchecked                                                                                              |
| Acc behavior Over/Under Flow    | Ring Counter                                                                                               |
| Filters (A, B, Z )              | None                                                                                                       |

Your Counter tab should look like the example below.

<!-- image -->

4. Click the Ranges tab to display the counter range configuration window with default values.
5. Use this information to complete the configuration for the Ranges tab.
6. Click OK.

<!-- image -->

| Value                                            | Value   |
|--------------------------------------------------|---------|
| Range #0 Range #1                                |         |
| Counter Used Counter #0 Counter #0               |         |
| Range Type Count Value Count Value               |         |
| High Limit 600,000 1,200,000                     |         |
| Low Limit 500,000 1,000,000                      |         |
| Range Active Within the Limits Within the Limits |         |
| Output Mask 0001 0002                            |         |

7. In the Project Menu, under Data Files, click Output.

<!-- image -->

The 34 words of the output image open. Addresses for these 34 words are Output Word [0] through Output Word [33]. In this example, only the first six words are modified. Output Word [6] through Output Word [33] are for Counters 1–3 and Ranges 12–15, which we are not using in this example.

8. Use this information to configure the first six Output words.

| Output Data File Decimal Value Description   |                                                                                             |
|----------------------------------------------|---------------------------------------------------------------------------------------------|
| Output Word [0] 0 Not used                   |                                                                                             |
|                                              | Output Word [1] 3 Enables Outputs 0 and 1 to be controlled by the 1769-HSC module's ranges. |
|                                              | Output Word [2] 3 Enable Ranges 0 and 1                                                     |
|                                              | Output Word [3] 0 Not using Interrupts                                                      |
|                                              | Output Word [4] 0 Not using Interrupts                                                      |
|                                              | Output Word [5] 1 Enable Counter 0                                                          |

## Monitor the Current Count and Verify Output Operation

No program logic is needed for this example. Use these steps to monitor the count and verify the output operation.

1. Save the program and download it to your controller.
2. Put the controller into Run mode.
3. Spin the shaft on your 845F encoder.

Input words 4 and 5, Current Count, display the current count data for Counter #0 of the 1769-HSC module. In this example, this count is the number of pulses received from the encoder times four (Quadrature Encoder X4 is the operating mode).

4. Continue to spin the encoder shaft until the current count value is within the limits set for Range 0 (500,000–600,000).

Output 0 turns On only when the current count value is equal to or within the Range 0 limits. Output 1 turns On only when the Current Count value is equal to or within the Range 1 limits (1,000,000–1,200,000). These two outputs are Off for all other values of the Current Count for Counter 0.

You can also use a CPW instruction to monitor 32-bit values via ladder logic.

## Programming Quick Reference

This appendix section for the 1769-HSC Module contains at-a-glance lists of the following:

- Configuration array
- Output array
- Input array

## IMPORTANT

The information in this appendix does not apply to the packaged controllers.

The default value for the configuration array is all zeros, except where noted.

Table 30 - Configuration Array for the 1769-HSC Module

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

Description

0 Individual Counter Reset Disable(1)

NumberOfCtrs

PFE

CtrRst OCLO GeneralConfigBits

® OvercurrentLatchOff

CtrReset

ProgToFaultEn

ogoau
NumberOfCounters\_0(2)

NumberOfCounters\_1

1 Filter\_Z1

Filter\_B1

Filter\_A1 Filter\_Z0

Filter\_B0

Filter\_A0 FilterA0\_0, FilterA0\_1 -- ...Z1\_1

2

Out3

PSR

Out2

PSR

Out1

PSR

Out0

PSR

Out3

PM

Out2

PM

Out1

PM

Out0

PM

Out0ProgramStateRun --Out3... and

Out0ProgramMode -- Out3...

3

Out3

PV

Out2

PV

Out1

PV

Out0

PV

Out0ProgramValue --- Out3...

4

Out3

FSR

Out2

FSR

Out1

FSR

Out0

FSR

Out3

FM

Out2

FM

Out1

FM

Out0

FM

Out0FaultStateRun --Out3FaultStateRun and

Out0FaultMode -- Out3FaultMode

5

Out3

FV

Out2

FV

Out1

FV

Out0

FV

Out0FaultValue -- Out3FaultValue

6

7

Ctr0MaxCount(3)

Ctr0MaxCount

8

9

Ctr0MinCount(4)

Ctr0MinCount

10

11

Ctr0Preset

Ctr0Preset

12 Ctr0Hysteresis

Ctr0Hysteresis

13 Ctr0Scalar(5)

Ctr0Scalar

14 Ctr0CyclicRateUpdateTime

(6)

Ctr0CyclicRateUpdateTime

15

Linear

Storage Mode

Operational Mode Ctr0ConfigFlags

® Ctr0Config.OperationalMode\_0

Ctr0Config.OperationalMode\_1

Ctr0Config.OperationalMode\_2

Ctr0Config.StorageMode\_0

Ctr0Config.StorageMode\_1

Ctr0Config.StorageMode\_2

Ctr0Config.Linear

16

17

Ctr1MaxCount(3)

Ctr1MaxCount

18

19

Ctr1MinCount(4)

Ctr1MinCount

20

21

Ctr1Preset

Ctr1Preset

22 Ctr1Hysteresis

Ctr1Hysteresis

23 Ctr1Scalar(5)

Ctr1Scalar

24 Ctr1CyclicRateUpdateTime

(6)

Ctr1CyclicRateUpdateTime

25

Linear

Storage Mode

Operational Mode Ctr1ConfigFlags

® Ctr1Config.OperationalMode\_0

Ctr1Config.OperationalMode\_1

Ctr1Config.OperationalMode\_2

Ctr1Config.StorageMode\_0

Ctr1Config.StorageMode\_1

Ctr1Config.StorageMode\_2

Ctr1Config.Linear

26

27

Ctr2MaxCount(3)

Ctr2MaxCount

28

29

Ctr2MinCount(4)

Ctr2MinCount

30

31

Ctr2Preset

Ctr2Preset

32 Ctr2Hysteresis

Ctr2Hysteresis

33 Ctr2Scalar(5)

Ctr2Scalar

34 Ctr2CyclicRateUpdateTime

(6)

Ctr2CyclicRateUpdateTime

35

Linear

Ctr2ConfigFlags

® Ctr2Config.Linear

36

37

Ctr3MaxCount(3)

Ctr3MaxCount

<!-- image -->

<!-- image -->

## Table 30 - Configuration Array for the 1769-HSC Module

<!-- image -->

| 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Ctr3MinCount(4)                                                                                                                                                                                               | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                | Ctr3MinCount                                                                                                                                                                                                                                                                |
| Ctr3Preset                                                                                                                                                                                                    | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  | Ctr3Preset                                                                                                                                                                                                                                                                  |
| 42 Ctr3Hysteresis                                                                                                                                                                                             | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              | Ctr3Hysteresis                                                                                                                                                                                                                                                              |
| 43 Ctr3Scalar(5)                                                                                                                                                                                              | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  | Ctr3Scalar                                                                                                                                                                                                                                                                  |
| 44 Ctr3CyclicRateUpdateTime (6)                                                                                                                                                                               | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    | Ctr3ConfigFlags  Range0to11[0].HighLimit                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                               | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      |
| Range0to11[0].LowLimit                                                                                                                                                                                        | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      | Range0to11[0].LowLimit                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 50 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[0].OutputControl Inv  Type  ToThisCtr Range0to11[0].ConfigFlags ® Range0To11[0].ToThisCounter_0 | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        | Range0To11[0].ToThisCounter_1 Range0To11[0].Type Range0To11[0].Invert Range0to11[1].HighLimit Range0to11[1].LowLimit                                                                                                                                                        |
| 56 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[1].OutputControl                                                                                | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    | ToThisCtr Range0to11[1].ConfigFlags ® Range0To11[1].ToThisCounter_0 Range0To11[1].ToThisCounter_1 Range0To11[1].Type Range0To11[1].Invert Range0to11[2].HighLimit Range0to11[2].LowLimit                                                                                    |
| Inv  Type  Range0to11[2].HighLimit  Range0to11[2].LowLimit                                                                                                                                                    | Inv  Type  Range0to11[2].HighLimit  Range0to11[2].LowLimit                                                                                                                                                                                                                  | Inv  Type  Range0to11[2].HighLimit  Range0to11[2].LowLimit                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 62 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[2].OutputControl                                                                                | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    | ToThisCtr Range0to11[2].ConfigFlags ® Range0To11[2].ToThisCounter_0 Range0To11[2].ToThisCounter_1 Range0To11[2].Type Range0To11[2].Invert Range0to11[3].HighLimit Range0to11[3].LowLimit                                                                                    |
|                                                                                                                                                                                                               | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit | 68 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[3].OutputControl ToThisCtr Range0to11[3].ConfigFlags ® Range0To11[3].ToThisCounter_0 Range0To11[3].ToThisCounter_1 Range0To11[3].Type Range0to11[4].HighLimit |
|                                                                                                                                                                                                               | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 | Range0To11[3].Invert Range0to11[4].LowLimit                                                                                                                                                                                                                                 |
| Range0to11[4].LowLimit                                                                                                                                                                                        | Range0to11[4].LowLimit                                                                                                                                                                                                                                                      | Range0to11[4].LowLimit                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 74 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[4].OutputControl Inv  Type                                                                      | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           | ToThisCtr Range0to11[4].ConfigFlags ® Range0To11[4].ToThisCounter_0 Range0To11[4].ToThisCounter_1 Range0To11[4].Type Range0To11[4].Invert Range0to11[5].HighLimit                                                                                                           |
|                                                                                                                                                                                                               | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      | Range0to11[5].LowLimit                                                                                                                                                                                                                                                      |
| Range0to11[5].HighLimit                                                                                                                                                                                       | Range0to11[5].HighLimit                                                                                                                                                                                                                                                     | Range0to11[5].HighLimit                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| Range0to11[5].LowLimit  Inv  Type                                                                                                                                                                             | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         | ToThisCtr Range0to11[5].ConfigFlags ® Range0To11[5].ToThisCounter_0 Range0To11[5].Type Range0To11[5].Invert Range0to11[6].HighLimit                                                                                                                                         |
| Range0to11[6].HighLimit                                                                                                                                                                                       | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      |
| Range0to11[6].LowLimit                                                                                                                                                                                        | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      | Range0to11[6].LowLimit                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| Inv                                                                                                                                                                                                           | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[6].ConfigFlags ® Range0To11[6].ToThisCounter_0 Range0to11[7].HighLimit                                                                                                                                                                                 |
| Range0to11[7].LowLimit                                                                                                                                                                                        | Range0to11[7].LowLimit                                                                                                                                                                                                                                                      | Range0to11[7].LowLimit                                                                                                                                                                                                                                                      | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            | Range0To11[6].ToThisCounter_1 Range0To11[6].Type                                                                                                                                                                                                                            |
|                                                                                                                                                                                                               | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 | Range0To11[6].Invert Range0to11[7].LowLimit                                                                                                                                                                                                                                 |
| Inv  Type                                                                                                                                                                                                     | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 | ToThisCtr Range0to11[7].ConfigFlags ® Range0To11[7].ToThisCounter_0 Range0to11[8].HighLimit                                                                                                                                                                                 |
|                                                                                                                                                                                                               | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      |
| Range0to11[8].LowLimit                                                                                                                                                                                        | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      | Range0to11[8].LowLimit                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                               | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     | Range0to11[9].HighLimit                                                                                                                                                                                                                                                     |
| Range0to11[9].LowLimit                                                                                                                                                                                        | Range0to11[9].LowLimit                                                                                                                                                                                                                                                      | Range0to11[9].LowLimit                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 103                                                                                                                                                                                                           | 103                                                                                                                                                                                                                                                                         | 103                                                                                                                                                                                                                                                                         | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 | ToThisCtr Range0to11[8].ConfigFlags ® Range0To11[8].ToThisCounter_0 Range0To11[8].Type Range0To11[8].Invert                                                                                                                                                                 |
| Type  Range0to11[7].HighLimit  Range0to11[8].HighLimit  Inv  Type  Range0to11[9].HighLimit                                                                                                                    | Type  Range0to11[7].HighLimit  Range0to11[8].HighLimit  Inv  Type  Range0to11[9].HighLimit                                                                                                                                                                                  | Type  Range0to11[7].HighLimit  Range0to11[8].HighLimit  Inv  Type  Range0to11[9].HighLimit                                                                                                                                                                                  |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 86 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[6].OutputControl                                                                                | 86 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[6].OutputControl                                                                                                                                              | 86 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[6].OutputControl                                                                                                                                              |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 80 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[5].OutputControl                                                                                | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[5].ToThisCounter_1                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                               | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     | Range0To11[7].Type Range0To11[7].Invert                                                                                                                                                                                                                                     |
| 92 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[7].OutputControl                                                                                | 92 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[7].OutputControl                                                                                                                                              | Range0To11[7].ToThisCounter_1                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 93  94 95                                                                                                                                                                                                     | 93  94 95                                                                                                                                                                                                                                                                   | 93  94 95                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 96 97                                                                                                                                                                                                         | 96 97                                                                                                                                                                                                                                                                       | 96 97                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                               |                                                                                                                                                                                                                                                                             | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               | Range0To11[8].ToThisCounter_1                                                                                                                                                                                                                                               |
| 98 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[8].OutputControl                                                                                | 98 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[8].OutputControl                                                                                                                                              | 98 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[8].OutputControl                                                                                                                                              |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 101 102                                                                                                                                                                                                       | 101 102                                                                                                                                                                                                                                                                     | 101 102                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 99                                                                                                                                                                                                            | 99                                                                                                                                                                                                                                                                          | 99                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 100                                                                                                                                                                                                           | 100                                                                                                                                                                                                                                                                         | 100                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                               | Range0to11[9].LowLimit                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |
| 104 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[9].OutputControl                                                                               | 104 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[9].OutputControl                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                                                             |

Table 30 - Configuration Array for the 1769-HSC Module

105

Inv

Type

ToThisCtr Range0to11[9].ConfigFlags ® Range0To11[9].ToThisCounter\_0

Range0To11[9].ToThisCounter\_1

Range0To11[9].Type

Range0To11[9].Invert

106

107

Range0to11[10].HighLimit

Range0to11[10].HighLimit

108

109

Range0to11[10].LowLimit

Range0to11[10].LowLimit

110 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[10].OutputControl

111

Inv

Type

ToThisCtr Range0to11[10].ConfigFlags ® Range0To11[10].ToThisCounter\_0

Range0To11[10].ToThisCounter\_1

Range0To11[10].Type

Range0To11[10].Invert

112

113

Range0to11[11].HighLimit

Range0to11[11].HighLimit

114

115

Range0to11[11].LowLimit

Range0to11[11].LowLimit

116 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range0to11[11].OutputControl

117

Inv

Type

ToThisCtr Range0to11[11].ConfigFlags ® Range0To11[11].ToThisCounter\_0

Range0To11[11].ToThisCounter\_1

Range0To11[11].Type

Range0To11[11].Invert

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

Description

<!-- image -->

The default value for the input array is all zeroes.

## Table 31 - Input Array for the 1769-HSC Module

15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0

Description

0

Z1 B1 A1 Z0 B0 A0 InputStateA0 -- InputStateZ1

1 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Readback.0 -- Readback.15

2 InvalidRangeLimit12…15 InvalidCtrAssignToRange12…15 GenErr InvOut MCfg

Out0Overcurrent -- Out3… Status Flags



InvalidRangeLimit12 ... 15

InvalidCtrAssignToRange12 ... 15

GenError

InvalidOutput

ModConfig

Out0Overcurrent0 ... 3

3 R15 R14 R13 R12 R11 R10 R09 R08 R07 R06 R05 R04 R03 R02 R01 R00

RangeActive.0 --

RangeActive.15

4

5

Ctr[0].CurrentCount Ctr[0].CurrentCount

6

7

Ctr[0].StoredCount Ctr[0].StoredCount

8

9

Ctr[0].CurrentRate Ctr[0].CurrentRate

10

11

Ctr[0].PulseInterval Ctr[0].PulseInterval

12

C0PW RV

IDW REZ CUdf COvf Ctr[0].StatusFlags



Ctr[0].Overflow

Ctr[0].Underflow

Ctr[0].RisingEdgeZ

Ctr[0].InvalidDirectWrite

----------------

Ctr[0].RateValid

Ctr[0].PresetWarning

13

Reserved

14

15

Ctr[1].CurrentCount Ctr[1].CurrentCount

16

17

Ctr[1].StoredCount Ctr[1].StoredCount

18

19

Ctr[1].CurrentRate Ctr[1].CurrentRate

20

21

Ctr[1].PulseInterval Ctr[1].PulseInterval

22

C1PW RV IC IDW REZ CUdf COvf Ctr[1].StatusFlags



Ctr[1].Overflow

- [ ] Ctr[1].Underflow

- [ ] Ctr[1].RisingEdgeZ

- [ ] Ctr[1].InvalidDirectWrite

- [ ] Ctr[1].InvalidCounter

- [ ] Ctr[1].RateValid

- [ ] Ctr[1].PresetWarning

23

Reserved

24

25

Ctr[2].CurrentCount Ctr[2].CurrentCount

26

27

Ctr[2].CurrentRate Ctr[2].CurrentRate

28

C2PW RV IC IDW

- CUdf COvf Ctr[2].StatusFlags Reserved



Ctr[2].Overflow

Ctr[2].Underflow

----------------

- [ ] Ctr[2].InvalidDirectWrite

- [ ] Ctr[2].InvalidCounter

- [ ] Ctr[2].RateValid

- [ ] Ctr[2].PresetWarning

29

30

31

Ctr[3].CurrentCount Ctr[3].CurrentCount

32

33

Ctr[3].CurrentRate Ctr[3].CurrentRate

34

C3PW RV IC IDW

CUdf COvf Ctr[3].StatusFlags



- [ ] Ctr[3].Overflow

Ctr[3].Underflow

----------------

- [ ] Ctr[3].InvalidDirectWrite

- [ ] Ctr[3].InvalidCounter

- [ ] Ctr[3].RateValid

Ctr[3].PresetWarning

The default value for the output array is all zeroes.

Table 32 - Output Array for the 1769-HSC Module

<!-- image -->

|       | 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 0                   |                                                         |                                                         |                                                                                                                                           | Description                                                                                                                               |                                                         |
|-------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
|       |                                                         |                                                         |                                                         | 0 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 OutputOnMask.0 -- OutputOnMask.15       |                                                                                                                                           |                                                         |
|       |                                                         |                                                         |                                                         | 1 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 OutputOffMask.0 -- OutputOffMask.15     |                                                                                                                                           |                                                         |
|       |                                                         |                                                         |                                                         | 2 R15 R14 R13 R12 R11 R10 R09 R08 R07 R06 R05 R04 R03 R02 R01 R00 RangeEn.0 -- RangeEn.15                                                 |                                                                                                                                           |                                                         |
| 3     |                                                         |                                                         |                                                         | Reserved                                                                                                                                  |                                                                                                                                           |                                                         |
| 4     | RBF                                                     |                                                         |                                                         | ResetBlownFuse                                                                                                                            |                                                                                                                                           |                                                         |
| 5     |                                                         |                                                         |                                                         | RPW RREZ Z Inh Z Inv D Inh D Inv RCU RCO SP En Ctr0ControlBits                                                                            |   Ctr0En                                                                                                                                 |                                                         |
| 6     |                                                         |                                                         |                                                         | RPW RREZ Z Inh Z Inv D Inh D Inv RCU RCO SP En Ctr1ControlBits                                                                            | Ctr0SoftPreset Ctr0ResetCountOverflow Ctr0ResetCountUnderflow                                                                             |                                                         |
| 7  8  | RPW                                                     |                                                         |                                                         | D Inv RCU RCO SP En Ctr2ControlBits                                                                                                       | Ctr0DirectionInvert                                                                                                                       |                                                         |
| 9  10 | RPW                                                     |                                                         |                                                         | D Inv RCU RCO SP En Ctr3ControlBits                                                                                                       | Ctr0DirectionInhibit Ctr0ZInvert                                                                                                          |                                                         |
| 11    |                                                         |                                                         |                                                         | Reserved                                                                                                                                  | Ctr0ZInhibit                                                                                                                              |                                                         |
|       | Range12To15[0].HiLimOrDirWr Range12To15[0].HiLimOrDirWr | Range12To15[0].HiLimOrDirWr Range12To15[0].HiLimOrDirWr | Range12To15[0].HiLimOrDirWr Range12To15[0].HiLimOrDirWr | Range12To15[0].HiLimOrDirWr Range12To15[0].HiLimOrDirWr                                                                                   | Range12To15[0].HiLimOrDirWr Range12To15[0].HiLimOrDirWr                                                                                   |                                                         |
| 12 13 | Range12To15[0].LowLimit Range12To15[0].LowLimit         | Range12To15[0].LowLimit Range12To15[0].LowLimit         | Range12To15[0].LowLimit Range12To15[0].LowLimit         | Range12To15[0].LowLimit Range12To15[0].LowLimit                                                                                           | Range12To15[0].LowLimit Range12To15[0].LowLimit                                                                                           |                                                         |
|       |                                                         |                                                         |                                                         | 14 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range12To15[0].OutputControl.0 ... .15 |                                                                                                                                           |                                                         |
| 15    |                                                         | Inv                                                     | LDW Type                                                | ToThisCtr Range12To15[0].Config Flags                                                                                                     |   Range12To15[0].ToThisCounter_0 Range12To15[0].ToThisCounter_1                                                                          |                                                         |
| 16 17 | Range12To15[1].HiLimOrDirWr Range12To15[1].HiLimOrDirWr | Range12To15[1].HiLimOrDirWr Range12To15[1].HiLimOrDirWr | Range12To15[1].HiLimOrDirWr Range12To15[1].HiLimOrDirWr | Range12To15[1].HiLimOrDirWr Range12To15[1].HiLimOrDirWr                                                                                   | Range12To15[1].HiLimOrDirWr Range12To15[1].HiLimOrDirWr                                                                                   |                                                         |
| 18 19 | Range12To15[1].LowLimit Range12To15[1].LowLimit         | Range12To15[1].LowLimit Range12To15[1].LowLimit         | Range12To15[1].LowLimit Range12To15[1].LowLimit         | Range12To15[1].LowLimit Range12To15[1].LowLimit                                                                                           | Range12To15[1].LowLimit Range12To15[1].LowLimit                                                                                           |                                                         |
|       |                                                         |                                                         |                                                         | 20 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range12To15[1].OutputControl.0 ... .15 |                                                                                                                                           |                                                         |
| 21    |                                                         | Inv                                                     | LDW Type                                                | ToThisCtr Range12To15[1].Config Flags                                                                                                     |   Range12To15[1].ToThisCounter_0                                                                                                         |                                                         |
| 22 23 | Range12To15[2].HiLimOrDirWr Range12To15[2].HiLimOrDirWr | Range12To15[2].HiLimOrDirWr Range12To15[2].HiLimOrDirWr | Range12To15[2].HiLimOrDirWr Range12To15[2].HiLimOrDirWr | Range12To15[2].HiLimOrDirWr Range12To15[2].HiLimOrDirWr                                                                                   | Range12To15[2].HiLimOrDirWr Range12To15[2].HiLimOrDirWr                                                                                   |                                                         |
| 24 25 | Range12To15[2].LowLimit Range12To15[2].LowLimit         | Range12To15[2].LowLimit Range12To15[2].LowLimit         | Range12To15[2].LowLimit Range12To15[2].LowLimit         | Range12To15[2].LowLimit Range12To15[2].LowLimit                                                                                           | Range12To15[2].LowLimit Range12To15[2].LowLimit                                                                                           |                                                         |
|       |                                                         |                                                         |                                                         | 26 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range12To15[2].OutputControl.0 ... .15 |                                                                                                                                           |                                                         |
| 27    |                                                         | Inv                                                     | LDW Type                                                | ToThisCtr Range12To15[2].Config Flags                                                                                                     |   Range12To15[2].ToThisCounter_0 Range12To15[2].ToThisCounter_1                                                                          |                                                         |
| 28 29 | Range12To15[3].HiLimOrDirWr Range12To15[3].HiLimOrDirWr | Range12To15[3].HiLimOrDirWr Range12To15[3].HiLimOrDirWr | Range12To15[3].HiLimOrDirWr Range12To15[3].HiLimOrDirWr | Range12To15[3].HiLimOrDirWr Range12To15[3].HiLimOrDirWr                                                                                   | Range12To15[3].HiLimOrDirWr Range12To15[3].HiLimOrDirWr                                                                                   | Range12To15[3].HiLimOrDirWr Range12To15[3].HiLimOrDirWr |
| 30 31 | Range12To15[3].LowLimit Range12To15[3].LowLimit         | Range12To15[3].LowLimit Range12To15[3].LowLimit         | Range12To15[3].LowLimit Range12To15[3].LowLimit         | Range12To15[3].LowLimit Range12To15[3].LowLimit                                                                                           | Range12To15[3].LowLimit Range12To15[3].LowLimit                                                                                           | Range12To15[3].LowLimit Range12To15[3].LowLimit         |
|       |                                                         |                                                         |                                                         | 32 Out15 Out14 Out13 Out12 Out11 Out10 Out09 Out08 Out07 Out06 Out05 Out04 Out03 Out02 Out01 Out00 Range12To15[3].OutputControl.0 ... .15 |                                                                                                                                           |                                                         |
| 33    |                                                         | Inv                                                     | LDW Type                                                | ToThisCtr Range12To15[3].Config Flags                                                                                                     |   Range12To15[3].ToThisCounter_0 Range12To15[3].ToThisCounter_1 Range12To15[3].Type Range12To15[3].LoadDirectWrite Range12To15[3].Invert |                                                         |

## Notes:

## 1769-UM006D-EN-P, May 2011

## 1769-UM006C-EN-P, November 2010

## History of Changes

This appendix summarizes the revisions to this manual. Reference this appendix if you need information to determine what changes have been made across multiple revisions. This can be especially useful if you are deciding to upgrade your hardware or software based on information added with previous revisions of this manual.

- Changed the hysteresis detection and configuration section to indicate that the Ctr[n].CurrentRate is reported as zero if the change in counts over the update time cycle is equal to or less than the minimum number of programmed counts.
- Added that the individual counter reset function for the 1769-HSC/B module applies to only CompactLogix controllers and not MicroLogix controllers.
- Changed hex equivalent values for general common hardware errors.
- Changed the input file update time to 500 ìs, max.

Updated the counter reset in the configuration array for bits 12…15. The individual counter reset functionality for the 1769-HSC series B module is reverse logic with a 0 = enabled and a 1 = disabled for RSLogix 5000 software. The firmware change applies to only the 1769-HSC series B module.

## Notes:

The following terms and abbreviations are used throughout this manual. For definitions of terms not listed here, refer to the Allen-Bradley Industrial Automation Glossary, publication AG-7.1 .

accumulated value (ACC) The number of elapsed time intervals or counted events.

actuator 1) A device that converts an electrical signal into mechanical motion. 2) In a general sense, any machine/process load device (for example, transducer) of a controller output circuit. See output device (page 162).

address 1) A character string that uniquely identifies a memory location. 2) A character string that uniquely identifies the physical location of an input or output circuit.

algorithm A set of procedures used for solving a problem in a finite number of steps.

- American wire gauge (AWG) A standard system used for designating the size of electrical conductors. Gauge

numbers have an inverse relationship to size; larger numbers have a smaller crosssectional area. However, a single-strand conductor has a larger cross-sectional area than a multi-strand conductor of the same gauge so that they have the same current-carrying specification.

analog circuit 1) A circuit in which the signal can vary continuously between specified limits. 2) A circuit that provides a continuous function. 3) Contrasted with digital circuit (page 159).

asynchronous 1) Lacking a regular time relationship; not related through repeating time patterns. 2) Contrasted with synchronous (page 163).

AWG See American wire gauge (page 157).

backplane A printed-circuit board, at the back of a chassis, that provides electrical interconnection between the modules inserted into the chassis.

- balanced circuit 1) A circuit whose two sides are electrically alike and symmetrical to a common reference point, usually ground. 2) Contrasted with unbalanced circuit (page 163).

bandwidth The range of frequencies over which a system is designed to operate. The bandwidth is expressed in Hertz between the highest and lowest frequencies.

- baseband link 1) A communication link with only one channel, encoded by on/off switching. Examples: DH and DH+ links. 2) Contrasted with carrier-band link (page 158) and broadband link (page 158).
- bidirectional I/O module An I/O module whose communication with the scanner or processor is bidirectional and therefore uses both input and output image areas.

broadband link

1) A communication link that can have multiple channels. Each channel signal modulates its own carrier frequency. Example: LAN/1 link. 2) Contrasted with carrier-band link (page 158) and baseband link (page 157).

bus A single path or multiple parallel paths for power or data signals that several devices can be connected at the same time. A bus can have several sources of supply and/or several sources of demand.

carrier-band link

1) A communication link with a single channel whose signal modulates a carrier frequency. Example: Data Highway II link. 2) Contrasted with broadband link (page 158) and baseband link (page 157).

cascade connection A series connection of amplifier stages or links in which the output of one stage feeds the input of the next.

cascading timers/counters A programming technique of using multiple timers and/or counters to extend the range of the timer or counter beyond the maximum values that can be accumulated in a single instruction.

channel A path for a signal. Several channels can share a common link.

chassis A hardware assembly that houses devices such as I/O modules, adapter modules, processor modules, and power supplies.

communication format

Format that defines the type of information transferred between an I/O module and its owner controller. This format also defines the tags created for each I/O module.

compatible match An electronic keying protection mode that requires the physical module and the module configured in the software to match according to vendor, catalog number, and major revision. In this case, the minor revision of the module must be greater than or equal to that of the configured slot.

configuration The arrangement and interconnection of hardware components within a system, and the hardware (switch and jumper) and software selections that determine the operating characteristics of the system.

connection The communication mechanism from the controller to another module in the control system.

controller A unit, such as a programmable controller or relay panel, that controls machine or process elements.

- coordinated system time (CST) Timer value which is kept synchronized for all modules within a single

ControlBus chassis. The CST is a 64-bit number with s resolution.

data 1) A general term for any type of information. 2) In a more restricted sense, data refers to the end-use information in the particular context; thereby excluding the protocol information used to get the end-use information.

data table The part of processor memory that contains I/O values and files where data is monitored, manipulated, and changed for control purposes.

database The entire body of data that has to do with one or more related subjects. Typically, it consists of a collection of data files.

differential 1) Pertaining to a method of signal transmission through two wires. The transmission always has opposite states. The signal data is the polarity difference between the wires; when one is high, the other is low. Neither wire is grounded. The circuit can be either a balanced circuit, a floating circuit, or a circuit with a high-impedance path to ground from either end. Usually used in reference to encoders, analog I/O circuits, and communication circuits. 2) Contrasted with single-ended (page 163).

digital circuit 1) A switching circuit that has only two states: on and off. 2) A circuit that provides a step function. 3) Contrasted with analog circuit (page 157).

direct connection An I/O connection where the controller establishes an individual connection with I/O modules.

direct I/O module 1) An I/O module for which each input or output that has an individual connection that corresponds directly to a data table bit or word that stores the value of the signal at that I/O circuit (digital or analog). This lets the ladder logic have direct access to the I/O values. 2) Contrasted with intelligent I/O module (page 161).

disable keying Option that turns off all electronic keying to the module. Requires no attributes of the physical module and the module configured in the software to match.

download The process of transferring the contents of a project on the workstation into the controller.

duration 1) The time during which something exists or lasts. For example, the length of time that a signal is high can be described as the duration of a pulse. 2) Compare interval (page 161) and period (page 162).

electronic keying A system feature which makes sure that the physical module attributes are consistent with what was configured in the software.

encoder Any feedback element that converts linear or rotary position (absolute or incremental) into a digital signal.

- Linear encoder—is a feedback element that directly converts linear position (absolute or incremental) into a digital signal.
- Rotary encoder—is a feedback element that converts rotary position (absolute or incremental) into a digital signal. Often, the directly measured rotary position is used to determine a linear position through gearing.

encoder bandwidth An expression for maximum encoder speed in Hz. Can also refer to the maximum rate at which the control loop can accept encoder signals. The actual bandwidth of the encoder and the capability of the controller to process encoder signals can not be the same.

exact match An electronic keying protection mode that requires the physical module and the module configured in the software to match identically, according to vendor, catalog number, major revision and minor revision.

factory wiring 1) Wiring completed before the product was shipped from the factory in which it was built. 2) Contrasted with field wiring (page 160).

field side Interface between user field-wiring and I/O module.

field wiring 1) Wiring connected by the user after the user receives the product. 2) Contrasted with factory wiring (page 160).

hysteresis 1) The effect of residual magnetism whereby the magnetization of a ferrous substance lags the magnetizing force because of molecular friction. 2) The property of magnetic material that causes the magnetic induction for a given magnetizing force to depend upon the previous conditions of magnetization. 3) A form of nonlinearity in which the response of a circuit to a particular set of input conditions depends not only on the instantaneous values of those conditions, but also on the immediate past of the input and output signals.

inhibit A ControlLogix process that lets you configure an I/O module but prevent it from communicating with the owner controller. In this case, the controller does not establish a connection.

input See sensor (page 163).

- intelligent I/O module 1) An I/O module that provides some on-board processing of input values to control some output values without going through the data table for control by the ladder logic. An intelligent I/O module can have digital I/O circuits, analog I/O circuits, or both. 2) Contrasted with direct I/O module (page 159).
- interval 1) The length of time between events or states. For example, the length of time between when a signal is high can be described as the interval between pulses. 2) Compare duration (page 159) and period (page 162).
- I/O module 1) In a programmable controller system, a module (interchangeable plug-in item within a larger assembly) that interfaces directly through I/O circuits to the sensors and actuators of the machine/process.
- isolated I/O module A module that has each input or output electrically isolated from every other input or output on that module.
- jumper A short conductor with which you can connect two points.
- k Kilo. A prefix used with units of measurement to designate a multiple of 1000.
- keying Devices that let only selected pairs of mating connectors be plugged into each other.
- listen-only connection An I/O connection that lets a controller monitor I/O module data without owning the module.
- local I/O 1) I/O connected to a processor across a backplane or a parallel link, thus limiting its distance from the processor. 2) Contrasted with remote I/O (page 162).
- major revision A module revision that is updated any time there is a functional change to the module resulting in an interface change with software.
- minor revision A module revision that is updated any time there is a change to the module that does not affect its function or software user interface.
- module slot A location for installing a module. In typical modular construction, modules plug into a backplane; each module slides into a slot that lines it up with its backplane connector.
- multicast Data transmissions which reach a specific group of one or more destinations.
- network update time (NUT) The smallest repetitive time interval in which the data can be sent on a ControlNet network. The NUT can be configured over the range from 2 ms…100 ms by using the RSNetWorx software.

node The connection point at which media access is provided.

| output device 1) For a computer, a CRT terminal or printer. 2) For a programmable controller, see actuator  (page 157).                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| owner-controller The controller that creates and stores the primary configuration and communication connection to a module.                                                                                                                                                                                                                                                |
| period 1) The length of time for a cyclical operation to complete one full cycle. For example, the length of time from one point in a cyclical wave form to the same point in the next cycle of the wave form. 2) Compare duration (page 159) and interval (page 161).                                                                                                     |
| power supply A device that converts available power to a form that a system can use—usually converts AC power to DC power.                                                                                                                                                                                                                                                 |
| producer/consumer model Intelligent data exchange system devices in which the HSC module produces data without having been polled first. Devices that need the data (consumers) recognize the data they need and consume it. Therefore, data only needs to be sent out on the network in a single message no matter how large the number of nodes to which it needs to go. |
| program mode In this mode, the controller program is not executing. Inputs are actively producing data. Outputs are not actively controlled and go to their configured Program mode state.                                                                                                                                                                                 |
| proximity switch/sensor A switch/sensor that is actuated when an actuating device is moved near it, without physical contact.                                                                                                                                                                                                                                              |
| pulse A momentary sharp change in voltage, current, or light from its quiescent condition.                                                                                                                                                                                                                                                                                 |
| quadrature Separation in phase by 90°. Used on single channels of feedback devices, such as encoders and resolvers, to detect the direction of motion.                                                                                                                                                                                                                     |
| remote connection  An I/O connection where the controller establishes an individual connection with I/O modules in a remote chassis.                                                                                                                                                                                                                                       |
| remote I/O  1) I/O connected to a processor across a serial link. With a serial link, remote I/O can be located long distances from the processor. 2) Contrasted with local I/O (page 161).                                                                                                                                                                                |

- removal and insertion under power (RIUP) ControlLogix feature that lets a user install or remove a module or RTB while power is applied.
- requested packet interval (RPI) A configured parameter that defines when the module will multicast data.
- run mode In this mode, the controller program is executing. Inputs are actively producing data. Outputs are actively controlled.
- sensor A digital or analog transducer (a device such as a limit switch, push button switch, pressure sensor, or temperature sensor) that generates an electrical signal through an input circuit to a controller.
- single-ended 1) Unbalanced, as when one side is grounded. See unbalanced circuit (page 163) 2) Contrasted with differential (page 159).
- synchronous 1) In step or in phase, as applied to two or more circuits, devices, or machines. 2) Contrasted with asynchronous (page 157).
- tag A named area of the controller's memory where data is stored like a variable. For example, an I/O definition file can contain a tag (definition) for each I/O—with each I/O definition containing a unique tag name by which the I/O can be addressed.
- unbalanced circuit 1) A circuit whose two sides are electrically dissimilar, as when one side is grounded. 2) Contrasted with balanced circuit (page 157).

## Notes:

## A

## additional resources 9

## array

configuration defaults 149

input defaults 152

output defaults 153

## C

cable 54

channel diagnostics 113

## CompactLogix controller

application example 131

compatibility 11

## configuration

array 66 , 149

defaults 149

error 115

errors 66

flags 67 , 68 , 71 , 82

## control bits 92

## count

overflow 106

underflow 106

value 28 -29

## counter

basic description 12

configuration summary 18

control bits 88 -89

preset warning 108

reset 66 , 72

type linear counter 28

ring counter 29

## current

count 98 , 104

draw 123

rate 105

## cyclic rate update time 67 , 81

## D

## defaults

configuration array 66 , 149

counter 15 , 111

counter maximum count 78 , 151

counter minimum count 79 , 151

counter preset 79

counter reset 73 , 74

counter scalar 80

,

151

cyclic rate update time 81 , 151

default safe state 43

input array 152

number of counters 75 , 151

output array 88 , 153

## DeviceNet adapter

compatibility 15 , 65

dimensions 128

## DIN rail mounting 52

direct write 30

value 94

## direction

inhibit 21 , 93

invert 21 , 93

## E

electrical noise 47

enable counter 92

## error

BadCounterMode 117

BadCounterNum 117

BadCtrAssignToRange 118

BadHysteresis 117

BadMin 117

BadModConfigUpdate 117 , 120

BadPreset 117

BadRangeLimit 118

BadScalar 117

BadScale 118

codes 116

configuration 66 , 115

critical 113

cyclic rate error 35

definitions 114

extended error information field 114

general configuration error 117

general error bit 98 , 102

hardware 114

invalid counter 107

invalid counter assigned to range 97 , 103

invalid direct write 107

invalid output 102

invalid range 95

invalid range limit 103

module error field 114

non-critical 113

per pulse error 35

UnusedConfigBitSet 117

## extended

error code 116

error information field 114

## F

fault state run 42

Filter Selection 70 , 75

filter selection 66

finger-safe terminal block 55

## G

gate/preset functions 18

gating 30

## general

configuration bits 66 , 70 error bit 102

## H

## hardware

error 114

features 13

heat considerations 47

hold last state 40

hysteresis 33

, 67 , 80

## I

individual counter reset 66 , 72

## input

array 98 array defaults 152 basic description 12 block diagram 16 differential encoder wiring 59 discrete device wiring 61 isolation 54

reducing noise 55

single-ended encoder wiring 60

state 98 , 100 , 101

terminal block wiring 58

## input configurations 21

## input operational mode 21

pulse external direction 22

internal direction 23

up and down pulses 24

X1 quadrature encoder 25

X2 quadrature encoder 26

X4 quadrature encoder 26

## installation

grounding 54

heat and noise considerations 47

## invalid

counter 107

counter assigned to range 103

direct write 107

output 102

range limit 103

## L

linear counter 28 , 83

load direct write 97

## M

masks 36

maximum count 67 , 71 , 78

## MicroLogix 1500

application example 141

compatibility 11

, 149

minimum count 67 , 71 , 79

module configured 102

module error field 114

mounting 50

## N

number of counters 18 , 75

O

## operating

block diagrams 16

description 15

operational mode 82

## output

array 88

array defaults 153

basic description 12

block diagram 17

control 36

control example 43

fault mode 67 , 77

fault state run 67 , 77

fault value 67 , 78

isolation 62

off mask 36 , 88 , 89 , 91

on mask 36 , 88 , 89

overcurrent autoreset operation 62

program mode 66 , 70

program state run 66

program value 66 , 77

required power supply 62

terminal block wiring 58

thermal protection 62

transient pulse warning 63

wiring diagram 64

## overcurrent 40

feedback 102

OverCurrentLatchOff bit 62 , 72

overflow 28 , 29 , 34

linear counter 28

## P

panel mounting 50

power-up diagnostics 112

preset 67 , 71 , 79

preset/reset 31

## program

alteration 110

mode 76

state run 41 , 76

to fault enable 43 , 75

## pulse

external direction 22

internal direction 23

interval 99 , 105

## R

## range

active 98 , 100 , 103

configuration flags 86 , 88-90 , 96

control 37

enable 88 -89 , 91

high limit 68 , 84 , 94

direct write value 88 -90

invert 87 , 98

low limit 68 , 84 , 88-90 , 95

output control 68 , 85 , 88-90 , 96

type 87 , 97

rate 32

accuracy 36 , 127

method 35

range 32

valid 34 , 107

readback 44 , 98 , 101

real outputs 36

removing terminal block 55

replacing a module 53

reset 31 , 73

blown fuse 88 , 89 , 92

counter overflow 92

counter preset warning 93

counter underflow 93

individual counter 66 , 72

rising edge Z 93

reset/preset 31

ring counter 29 , 83

rising edge Z 106

Rockwell Software application example 132

RSLogix 5000 software example 142

## S

safe state control 40

safety circuits 110

scalar 34 , 67 , 80

soft preset 92

spacing 50

specifications 123

status bits 98

, 100 , 101 , 106

flags 98 indicators overview 14

power-up diagnostics 112

safety considerations 109

troubleshooting status 14 , 112

## storage

mode 83

stored count 104

## T

temperature derating 128

terminal door label 58

screw torque 56

terminal block removing 55

wiring 55

throughput and timing 126

timing 126

ToThisCounter 86

troubleshooting safety considerations 109

## U

underflow 28 , 29 , 34

linear counter 28

up and down pulses 24

user-defined safe state 40

## V

virtual outputs 36

## W

wire size 56

wiring 45

module 56

routing considerations 47

terminal block 55

## X

X1 quadrature encoder 25

X2 quadrature encoder 26

X4 quadrature encoder 26

## Z

## Z

inhibit 93 input functions 30 gating 30 preset/reset 30 setting output array 106 invert 93

## Rockwell Automation Support

Rockwell Automation provides technical information on the Web to assist you in using its products. At http://www.rockwellautomation . co m/support/, you can find technical manuals, a knowledge base of FAQs, technical and application notes, sample code and links to software service packs, and a MySupport feature that you can customize to make the best use of these tools.

For an additional level of technical phone support for installation, configuration, and troubleshooting, we offer TechConnect support programs. For more information, contact your local distributor or Rockwell Automation representative, or visit http://www.rockwellautomation . co m/support/ .

## Installation Assistance

If you experience a problem within the first 24 hours of installation, review the information that is contained in this manual. You can contact Customer Support for initial help in getting your product up and running.

| United States or Canada 1.440.646.3434   |                                                                                                                                                          |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States or Canada          | Use the Worldwide Locator at http://www.rockwellautomation.com/support/americas/phone_en.html, or contact your local Rockwell Automation representative. |

## New Product Satisfaction Return

Rockwell Automation tests all of its products to ensure that they are fully operational when shipped from the manufacturing facility. However, if your product is not functioning and needs to be returned, follow these procedures.

| United States Contact your distributor. You must provide a Customer Support case number (call the phone number above to obtain one) to your distributor to complete the return process.   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States Please contact your local Rockwell Automation representative for the return procedure.                                                                              |

## Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete this form, publication RA-DU002, available at http://www.rockwellautomation . co m/literature/ .

Rockwell Otomasyon Ticaret A.Ş., Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400