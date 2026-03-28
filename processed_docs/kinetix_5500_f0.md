<!-- image -->

<!-- image -->

## Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Multi-axis Servo Drives

Catalog Numbers 2094-SE02F-M00-S1, 2094-EN02D-M01-S1

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

Original Instructions

<!-- image -->

## Important User Information

Solid-state equipment has operational characteristics differing from those of electromechanical equipment. Safety Guidelines for the Application, Installation and Maintenance of Solid State Controls (publication SGI-1.1 available from your local Rockwell Automation sales office or online at http://www.rockwellautomation.com/literature/) describes some important differences between solid-state equipment and hard-wired electromechanical devices. Because of this difference, and also because of the wide variety of uses for solid-state equipment, all persons responsible for applying this equipment must satisfy themselves that each intended application of this equipment is acceptable.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss.

<!-- image -->

<!-- image -->

<!-- image -->

## IMPORTANT

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

Identifies information that is critical for successful application and understanding of the product.

Allen-Bradley, Guardmaster, Kinetix, Logix5000, MP-Series, PowerFlex, RSLogix, Rockwell Software, Rockwell Automation, Studio 5000, and TechConnect are trademarks of Rockwell Automation, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

## New and Updated Information

This manual contains new and updated information.

This table contains the changes made to this revision.

| Topic                                                                                                                                                                          | Page      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| Studio 5000™ Logix Designer application is the rebranding of RSLogix™ 5000 software. References to RSLogix 5000 software have been replaced by the Logix Designer application. | 12        |
| Updated descriptive text in Safety Certification and Important Safety Considerations for consistency with the text used in other Kinetix® servo drive safety documentation.    | 13 and 14 |
| Added European Union Directives to chapter 1.                                                                                                                                  | 16        |
| Corrected the IOD-0 pin description and signal name.                                                                                                                           | 27        |
| Added IMPORTANT text and Response Time Settings table                                                                                                                          | 47        |
| Added descriptive text and example formulas to enhance the understanding of Safe Stop 1 and 2. 56…59                                                                           |           |
| Deceleration Rate removed from Safe Stop Parameter tables throughout this publication. –                                                                                       |           |
| Corrected wiring to IOD-27 and IOD-28 in Figure 28. 90                                                                                                                         |           |
| Added IMPORTANT text to Editing the Configuration. 118                                                                                                                         |           |
| Added IMPORTANT text to Example Application. 121                                                                                                                               |           |
| Replaced the Safe Stop tab screen capture.                                                                                                                                     | 129       |
| Added bullet statement to FEEDBACK 1 in the Safe State Faults table.                                                                                                           | 135       |

## Notes:

Preface

## Table of Contents

|                            | About This Publication. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11                |                                                                                                      |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
|                            | Audience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11   |                                                                                                      |
|                            | Conventions. . . . . . . . . . . . . . .                                                                                      | . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 11                      |
|                            | Terminology. . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                 | . . . . . . . . . . . . . . . . . . . . 11                                                           |
|                            | Studio 5000 Environment . . . . . . .                                                                                         | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 12                                |
|                            | Additional Resources . . . .                                                                                                  | . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . 12                |
|                            | Chapter 1                                                                                                                     |                                                                                                      |
| Safety Concept             | Safety Certification. . . .  . . . . . . . . . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . . . . . . . . 13                                                           |
|                            | Important Safety Considerations                                                                                               | . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 14                                      |
|                            | Safety Category 4 Performance Definition. . . . . . . . . . . . . . . . . . . . . . 14                                        |                                                                                                      |
|                            | Stop Category Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15                          |                                                                                                      |
|                            | Performance Level and Safety Integrity Level (SIL) CL3 . . . . . . . . . 15                                                   |                                                                                                      |
|                            | European Union Directives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16                    |                                                                                                      |
|                            | CE Conformity . . . . . . .                                                                                                   | . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 16                    |
|                            | EMC Directive. . . . . . . . . . . .                                                                                          | . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 16                            |
|                            | Low Voltage Directive . . .                                                                                                   | . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 16                        |
|                            | Functional Proof Tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16               |                                                                                                      |
|                            | PFD and PFH Definitions . . . . . .                                                                                           | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 17                              |
|                            | PFD and PFH Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17               |                                                                                                      |
|                            | Safe State . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17 |                                                                                                      |
|                            | Safety Reaction Time. . . .                                                                                                   | . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . 18                |
|                            | Considerations for Safety Ratings. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18                       |                                                                                                      |
|                            | Considerations for Single-encoder Applications. . . . . . . . . . . . . . . . . 18                                            |                                                                                                      |
|                            | Understanding Commutation . . . . .  . . . . . . . . . . . . . . .                                                            | . . . . . . . . . . . . . 19                                                                         |
|                            | Chapter 2                                                                                                                     |                                                                                                      |
| About the Kinetix 6200 and | Safety Functions . . . . . . . . . . .                                                                                        | . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 21                      |
| Kinetix 6500 Safe Speed    | Operation Modes . . . . . . . . . .                                                                                           | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 22                              |
| Monitoring Features        | Disabled Mode . . . . . . . . . . . .                                                                                         | . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 22                            |
|                            | Lock Monitoring . . . . . . . . . . .                                                                                         | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 23                              |
|                            | Safe Maximum Speed, Safe Maximum Acceleration, and                                                                            | Safe Direction Monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 |
|                            | Hardware Features . . . . . . . . . .                                                                                         | . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 24                        |
|                            | Chapter 3                                                                                                                     |                                                                                                      |
| Installation and Wiring    | General Safety Information . . . . .                                                                                          | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 25                              |
|                            | Power Supply Requirements . . . . .                                                                                           | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 26                                |
|                            | Wiring the Safety Connections. . .                                                                                            | . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 26                                |
|                            | Terminal Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27                 |                                                                                                      |
|                            | Compatible Encoders .  . . . . . . . . . . . . . . . . . . . . . . .                                                          | . . . . . . . . . . . . . . . . . . . . 28                                                           |

Chapter 4

| Speed Monitoring I/O Signals   | Inputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29   |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
|                                | Safe Stop Input (SS_In) . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . 32                        |
|                                | Safe Limited Speed Input (SLS_In) . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32                                      |
|                                | Door Monitor Input (DM_In) . .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 32                                   |
|                                | Enabling Switch Monitor Input (ESM_In) . . . . . . . . . . . . . . . . . . . . . 33                                               |
|                                | Lock Monitor Input (LM_In) . . .  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . 33                                 |
|                                | Reset Input (Reset_In) . . . . . . .  . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . 34                       |
|                                | Outputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35      |
|                                | Safe Stop Output (SS_Out) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35                                |
|                                | Safe Limited Speed Output (SLS_Out). . . . . . . . . . . . . . . . . . . . . . . . . 36                                           |
|                                | Door Control Output (DC_Out)  . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . 38                                       |
|                                | Chapter 5                                                                                                                         |
| General Device and Feedback    | Cascaded Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41                     |
| Monitoring Configuration       | Operation Mode . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 42             |
|                                | Reset Type . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 42     |
|                                | Overspeed Response Time . .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 43                      |
|                                | Speed Resolution Accuracy for Rotary Systems . . . . . . . . . . . . . . . . . . 43                                               |
|                                | Speed Resolution Accuracy for Linear Systems . . . . . . . . . . . . . . . . . . 45                                               |
|                                | General Parameter List. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48                  |
|                                | Feedback Monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49                  |
|                                | Feedback Polarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49                    |
|                                | Single Encoder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                   |
|                                | Dual Encoders. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50                   |
|                                | Feedback Voltage Monitoring Range . . . . . . . . . . . . . . . . . . . . . . . . . . . 53                                        |
|                                | Feedback Fault . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53                   |
|                                | Feedback Parameter List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54                    |
|                                | Chapter 6                                                                                                                         |
| Safe Stop and Safe Stop with   | Safe Stop Mode . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 55           |
| Door Monitoring Modes          | Stop Categories. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56                   |
|                                | Standstill Speed and Position Tolerance . . . . . . . . . . . . . . . . . . . . . . . . 61                                        |
|                                | Deceleration Monitoring .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 62                          |
|                                | Safe Stop Reset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63                  |
|                                | Door Control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64                   |
|                                | Lock Monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66                      |
|                                | Safe Stop Parameter List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66                   |
|                                | Safe Stop Wiring Example. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68                      |
|                                | Safe Stop with Door Monitoring Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68                                    |
|                                | Lock Monitoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68                      |
|                                | SS Reset. . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 69          |
|                                | Safe Stop with Door Monitoring Parameter List . . . . . . . . . . . . . . . . . . . . 69                                          |
|                                | Safe Stop with Door Monitoring Wiring Example. . . . . . . . . . . . . . . . . . . 69                                             |

Chapter 7

| Safe Limited Speed (SLS) Modes      | Safe Limited Speed (SLS) Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71                                                                            |                                            |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
|                                     | Safe Limited Speed Reset. . . . .  . . . . . . . . . . . . . . . . . .                                                                                                            | . . . . . . . . . . . . . . . 73           |
|                                     | Safe Limited Speed Parameter List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74                                                                            |                                            |
|                                     | Safe Limited Speed Wiring Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75                                                                                |                                            |
|                                     | Safe Limited Speed with Door Monitoring Mode . . . . . . . . . . . . . . . . . . . 75                                                                                             |                                            |
|                                     | Safe Limited Speed Reset. . . . .  . . . . . . . . . . . . . . . . . .                                                                                                            | . . . . . . . . . . . . . . . 76           |
|                                     | SLS with Door Monitoring Parameter List . . . . . . . . . . . . . . . . . . . . . . . . . 77                                                                                      |                                            |
|                                     | SLS with Door Monitoring Wiring Example . . . . . . . . . . . . . . . . . . . . . . . 77                                                                                          |                                            |
|                                     | Safe Limited Speed with Enabling Switch Monitoring Mode. . . . . . . . . 78                                                                                                       |                                            |
|                                     | Safe Stop Reset (SS Reset) and Safe Limited Speed Reset (SLS Reset) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78        |                                            |
|                                     | SLS with Enabling Switch Monitoring Parameter List. . . . . . . . . . . . . . . 79                                                                                                |                                            |
|                                     | SLS with Enabling Switch Monitoring Wiring Example . . . . . . . . . . . . . 79                                                                                                   |                                            |
|                                     | Safe Limited Speed with Door Monitoring and Enabling Switch                                                                                                                       |                                            |
|                                     | Monitoring Mode. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80                                                                 |                                            |
|                                     | Behavior During SLS Monitoring.  . . . . . . . . . . . . . . . .                                                                                                                  | . . . . . . . . . . . . . 81               |
|                                     | Behavior While SLS Monitoring is Inactive. . . . . . . . . . . . . . . . . . . . . 81                                                                                             |                                            |
|                                     | Behavior During SLS Monitoring Delay. . . . . . . . . . . . . . . . . . . . . . . . 81                                                                                            |                                            |
|                                     | Safe Stop Reset (SS Reset) and Safe Limited Speed Reset (SLS Reset) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82        |                                            |
|                                     | SLS with Door Monitoring and Enabling Switch Monitoring Parameter List . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 82 |                                            |
|                                     | SLS with Door Monitoring and Enabling Switch Monitoring Wiring Example . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . 83     |                                            |
|                                     | Safe Limited Speed Status Only Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84                                                                                  |                                            |
|                                     | Speed Hysteresis . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                                                                                       | . . . . . . . . . . . . . . . . 85         |
|                                     | SLS Status Only Parameter List .  . . . . . . . . . . . . . . . . . .                                                                                                             | . . . . . . . . . . . . . . . . 85         |
|                                     | SLS Status Only Wiring Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86                                                                              |                                            |
|                                     | Chapter 8                                                                                                                                                                         |                                            |
| Slave Modes for Multi-axis Cascaded | Cascaded Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89                                                                      |                                            |
| Systems                             | Slave, Safe Stop Mode . .  . . . . . . . . . . . . . . . . . . . . . .                                                                                                            | . . . . . . . . . . . . . . . . . . . . 91 |
|                                     | Slave, Safe Stop Parameter List . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91                                                                        |                                            |
|                                     | Slave, Safe Stop Wiring Examples.  . . . . . . . . . . . . . . . . . .                                                                                                            | . . . . . . . . . . . . . . . 93           |
|                                     | Slave, Safe Limited Speed Mode .  . . . . . . . . . . . . . . . . . .                                                                                                             | . . . . . . . . . . . . . . . . 96         |
|                                     | Slave, Safe Limited Speed Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96                                                                               |                                            |
|                                     | Slave, Safe Limited Speed Wiring Examples . . . . . . . . . . . . . . . . . . . . . . . . 97                                                                                      |                                            |
|                                     | Slave, Safe Limited Speed Status Only Mode . . . . . . . . . . . . . . . . . . . . . . . 99                                                                                       |                                            |
|                                     | Slave, Safe Limited Speed Status Only Parameter List . . . . . . . . . . . . . . . 99                                                                                             |                                            |
|                                     | Slave, Safe Limited Speed Status Only Wiring Examples. . . . . . . . . . . . 100 Multi-axis Connections. . . . . . . .  . . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . 101        |

Chapter 9

| Safe Maximum Speed and Direction                                           | Safe Maximum Speed (SMS) Monitoring. . . . . . . . . . . . . . . . . . . . . . . . . . 103               |                                                    |
|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| Monitoring                                                                 | Safe Maximum Acceleration (SMA) Monitoring . . . . . . . . . . . . . . . . . . . 106                     |                                                    |
|                                                                            | Safe Direction Monitoring (SDM).  . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . 108                  |
|                                                                            | Max Speed, Max Accel, and Direction Monitoring Parameter List . . . 110                                  |                                                    |
|                                                                            | Chapter 10                                                                                               |                                                    |
| Safety Configuration and Verification Safety Configuration . . . . . . . . | . . . . . . . . . . . . . . . . . . .                                                                    | . . . . . . . . . . . . . . . . . 111              |
|                                                                            | Configuration Signature ID . . .  . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . 111                  |
|                                                                            | Safety-lock . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . . 112            |
|                                                                            | Set and Change a Password . . . . . . . . . . . .                                                        | . . . . . . . . . . . .  . . . . . . . . . . . 112 |
|                                                                            | Resetting the Password . . . . . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 113                |
|                                                                            | Resetting the Configuration . . .  . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . 113                  |
|                                                                            | Basics of Application Development and Testing . . . . . . . . . . . . . . . . . . . 114                  |                                                    |
|                                                                            | Commissioning the System. .  . . . . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . . . . 114            |
|                                                                            | Specifying the Safety Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . 115            |                                                    |
|                                                                            | Configure the Safe Speed Monitoring Drive . . . . . . . . . . . . . . . . . . . 116                      |                                                    |
|                                                                            | Project Verification Test  . . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . . . 116            |
|                                                                            | Confirm the Project . . . . . . . .  . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . 117                |
|                                                                            | Safety Validation . . . .  . . . . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . . . . 117          |
| Drive . . . . . . . . . . . . . . . . .                                    | Verifying the Signature and Lock in the Safe Speed Monitor . . . . . . . . . . . . . . . . . . . .       | . . . . . . . . . . . . . . . . . . 118            |
|                                                                            | Editing the Configuration. . . . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 118                |
|                                                                            | Chapter 11                                                                                               |                                                    |
| Safety Configuration Example                                               | Example Application . . . .  . . . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . . 121          |
|                                                                            | Use the Initial Safety Main Tab Commands . . . . . . . . . . . . . . . . . . . 123                       |                                                    |
|                                                                            | Configure the Safety Tab Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . 126              |                                                    |
|                                                                            | Feedback Tab Settings . .  . . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . . . 127            |
|                                                                            | Configure the Input Tab Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . 128               |                                                    |
|                                                                            | Configure the Safe Stop Tab Parameters . . . . . . . . . . . . . . . . . . . . . . . 129                 |                                                    |
|                                                                            | Configure Safe Limited Speed Tab Parameters . . . . . . . . . . . . . . . . . 130                        |                                                    |
|                                                                            | Configure Safe Max Speed Tab Parameters . . . . . . . . . . . . . . . . . . . . 131                      |                                                    |
|                                                                            | Chapter 12                                                                                               |                                                    |
| Troubleshooting the Safe Speed                                             | Status Indicators . . . . .  . . . . . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . . . . . 133      |
| Monitoring Drive                                                           | Nonrecoverable Faults . .  . . . . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . . . . . 133        |
|                                                                            | Fault Recovery . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . . . . . 133        |
|                                                                            | Input and Output Faults . . . . . .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 134              |
|                                                                            | Fault Codes and Descriptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134 |                                                    |
|                                                                            | Fault Reactions. . . . .  . . . . . . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . . . . . . . 137    |
|                                                                            | Safe State Faults . . . . .  . . . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . . 137          |
|                                                                            | Stop Category Faults and Fault While Stopping Faults. . . . . . . . . . 137                              |                                                    |
|                                                                            | Status Attributes . .  . . . . . . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . . . . . 138    |
|                                                                            | Guard Status Attributes . . . . .  . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . 138                |

|                | I/O Diagnostic Status Attributes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140                          |                                         |
|----------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
|                | Configuration Fault Codes . . . . .  . . . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . 141       |
|                | Configuration Fault Example. . .  . . . . . . . . . . . . . . . .                                                       | . . . . . . . . . . . . . . 142         |
|                | Appendix A                                                                                                              |                                         |
| Specifications | General Specifications  . . . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . 143      |                                         |
|                | Certifications . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . . . . 144 |
|                | Encoder Specifications. . .  . . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . 144       |                                         |
|                | Appendix B                                                                                                              |                                         |
| Parameter Data | Parameter Groups. . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . 145     |                                         |
|                | Parameters and Settings in a Linear List . . . . . . . . . . . . . . . . . . . . . . . . . . . 146                      |                                         |
|                | Safety Attributes . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 150 |                                         |
|                | Index                                                                                                                   |                                         |

## Notes:

| About This Publication   | This manual explains how the Kinetix 6200 and Kinetix 6500 drives can be used in Safety Integrity Level (SIL) CL3, Performance Level [PLe], or Category (CAT) 4 applications. It describes the safety requirements, including PFD and PFH values and application verification information, and provides information on configuring and troubleshooting the Kinetix 6200 and Kinetix 6500 drives with safe speed monitoring.   |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Audience                 | Use this manual if you are responsible for designing, configuring, or troubleshooting safety applications that use the Kinetix 6200 and Kinetix 6500 drives with safe speed monitoring. You must have a basic understanding of electrical circuitry and familiarity with Kinetix 6200 and Kinetix 6500 drives. You must also be trained and experienced in the creation, operation, and maintenance of safety systems.        |
| Conventions              | In this manual, configuration parameters are in brackets. For example, [Overspeed Response Time].                                                                                                                                                                                                                                                                                                                             |
| Terminology              | This table defines common safety terms used in this manual.                                                                                                                                                                                                                                                                                                                                                                   |

| Abbreviation Full Term   |                                                | Definition                                                                                                                                                                                                               |
|--------------------------|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1oo2                     | One out of Two                                 | Refers to the behavioral design of a dual-channel safety system.                                                                                                                                                         |
| CAT                      | Category                                       | –                                                                                                                                                                                                                        |
| EN                       | European Norm                                  | European Standards (EN specifications) developed by the European Committee for Standardization for the European Union.                                                                                                   |
| ESPE                     | Electro-sensitive Protective Equipment         | An assembly of devices and/or components working together for protective tripping or presence sensing purposes and comprising as a minimum: •  Sensing devices •  Controlling/monitoring devices •  Output signal-switching devices (OSSD)                                                                                                                                                                                                                          |
| IEC                      | International Electrotechnical Commission      | Non-profit, non-governmental international standards organization that prepares and publishes international standards for all electrical, electronic, and related technologies, collectively known as electrotechnology. |
| IGBT                     | Insulated Gate Bi-polar Transistors            | Typical power switch used to control main current.                                                                                                                                                                       |
| ISO                      | International Organization for Standardization | Voluntary organization whose members are recognized authorities on standards, each one representing a different country.                                                                                                 |
| OSSD                     | Output Signal Switching Device                 | The component of the electro-sensitive protective equipment (ESPE) connected to the control system of a machine responds by going to the OFF-state when the sensing device is actuated during normal operation.          |
| PFD                      | Probability of Failure on Demand               | The average probability of a system to fail to perform its design function on demand.                                                                                                                                    |
| PFH                      | Probability of Failure per Hour                | The probability of a system to have a dangerous failure occur per hour.                                                                                                                                                  |
| PL                       | Performance Level                              | EN ISO 13849-1 safety rating                                                                                                                                                                                             |
| S1                       |                                                | 2094-SE02F-M00-S1 and 2094-EN02D-M01-S1 Catalog numbers for Kinetix 6200 and Kinetix 6500 drives with Safe Speed Monitoring functionality.                                                                               |
| SFF                      | Safe Failure Fraction                          | The sum of safe failures plus the sum of dangerous detected failures divided by the sum of all failures                                                                                                                  |
| SIL                      | Safety Integrity Level                         | A measure of a products ability to lower the risk that a dangerous failure could occur.                                                                                                                                  |

## Studio 5000 Environment

## Additional Resources

The Studio 5000 Engineering and Design Environment combines engineering and design elements into a common environment. The first element in the Studio 5000 environment is the Logix Designer application. The Logix Designer application is the rebranding of RSLogix 5000 software and will continue to be the product to program Logix5000™ controllers for discrete, process, batch, motion, safety, and drive-based solutions.

<!-- image -->

The Studio 5000 environment is the foundation for the future of Rockwell Automation® engineering design tools and capabilities. It is the one place for design engineers to develop all the elements of their control system.

These documents contain additional information concerning related Rockwell Automation products.

| Resource                                                                                                        | Description                                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix 6200 and Kinetix 6500 Modular Multi-axis Servo Drive User Manual, publication 2094-UM002                | Provides information on installing, configuring, starting up, troubleshooting, and applications for your Kinetix 6200 or Kinetix 6500 servo drive system.                                     |
| Kinetix Safe-off Feature Safety Reference Manual, publication GMC-RM002                                         | Provides information on wiring and troubleshooting your Kinetix 5500 servo drives with the safe-off feature.                                                                                  |
| System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001                           | Provides information, examples, and techniques designed to minimize system failures caused by electrical noise.                                                                               |
| EMC Noise Management DVD, publication GMC-SP004                                                                 | Provides information, examples, and techniques designed to minimize system failures caused by electrical noise.                                                                               |
| Kinetix Motion Control Selection Guide, publication GMC-SG001                                                   | Overview of Kinetix servo drives, motors, actuators, and motion accessories designed to help make initial decisions for the motion control products best suited for your system requirements. |
| Safety Guidelines for the Application, Installation and Maintenance of Solid State Control, publication SGI-1.1 | Describes important differences between solid state control and hardwired electromechanical devices.                                                                                          |

You can view or download publications at http://www.rockwellautomation.com/literature. To order paper copies of technical documentation, contact your local Rockwell Automation distributor or sales representative.

## Safety Certification

## Safety Concept

This chapter describes the safety performance level concept and how the Kinetix 6200 and Kinetix 6500 drives can meet the requirements of Performance Level e (PLe) and safety category 4 (CAT 4) per EN ISO 13849-1 and SIL CL3 per IEC EN 61508, EN 61800-5-2, and EN 62061.

| Topic                             |   Page |
|-----------------------------------|--------|
| Safety Certification              |     13 |
| Functional Proof Tests            |     16 |
| PFD and PFH Definitions           |     17 |
| Safe State                        |     17 |
| Safety Reaction Time              |     18 |
| Considerations for Safety Ratings |     18 |

The TÜV Rheinland group has approved the Kinetix 6200 and Kinetix 6500 servo drives for use in safety-related applications up to ISO 13849-1 Performance Level e (PLe) and category 4, SIL CL3 per IEC EN 61508, EN 61800-5-2 and EN 62061 where removing the motion producing power is considered to be the safe state. All of the examples related to I/O included in this manual are based on achieving de-energization as the safe state for typical Machine Safety and Emergency Shutdown (ESD) systems.

<!-- image -->

## Important Safety Considerations

The system user is responsible for the following:

- Validation of any sensors or actuators connected to the system
- Completing a system-level risk assessment
- Certification of the machine to the desired EN ISO 13849-1 performance level or EN 62061 SIL level
- Project management and proof testing
- Programming the application software and the drive configurations in accordance with the information in this manual
- Access control to the system, including password handling
- Analyzing all configuration settings and choosing the proper setting to achieve the required safety rating

## IMPORTANT

When applying functional safety, restrict access to qualified, authorized personnel who are trained and experienced.

<!-- image -->

ATTENTION: When designing your system, consider how personnel exit the machine if the door locks while they are in the machine. Additional safeguarding devices can be required for your specific application.

## Safety Category 4 Performance Definition

To achieve Safety Category 4 according to EN ISO 13849-1:2006, the safetyrelated parts have to be designed such that:

- the safety-related parts of machine control systems and/or their protective equipment, as well as their components, shall be designed, constructed, selected, assembled, and combined in accordance with relevant standards so that they can withstand expected conditions.
- basic safety principles shall be applied.
- a single fault in any of its parts does not lead to a loss of safety function.
- a single fault is detected at or before the next demand of the safety function, or, if this detection is not possible, then an accumulation of faults shall not lead to a loss of the safety function.
- the average diagnostic coverage of the safety-related parts of the control system shall be high, including the accumulation of faults.
- the mean time to dangerous failure of each of the redundant channels shall be high.
- measures against common cause failure shall be applied.

## Stop Category Definitions

The selection of a stop category for each stop function must be determined by a risk assessment.

- Stop Category 0 is achieved with immediate removal of power to the actuator, resulting in an uncontrolled coast to stop. Safe Torque Off accomplishes a Stop Category 0 stop.
- Stop Category 1 is achieved with power available to the machine actuators to achieve the stop. Power is removed from the actuators when the stop is achieved.
- Stop Category 2 is a controlled stop with power available to the machine actuators. The stop is followed by a holding position under power.

Refer to Safe Stop Mode on page 55 for more information.

| IMPORTANT   | When designing the machine application, timing and distance must be considered for a coast to stop (Stop Category 0 or Safe Torque Off). For more information regarding stop categories, refer to EN 60204-1.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TIP         | You can determine the drive/motor Stop Delay characteristics by using Motion Analyzer software, version 4.7 or later.                                                                                           |

## Performance Level and Safety Integrity Level (SIL) CL3

For safety-related control systems, Performance Level (PL), according to EN ISO 13849-1, and SIL levels, according to EN 61508 and EN 62061, include a rating of the system's ability to perform its safety functions. All of the safety-related components of the control system must be included in both a risk assessment and the determination of the achieved levels.

Refer to the EN ISO 13849-1, EN 61508, and EN 62061 standards for complete information on requirements for PL and SIL determination.

Refer to Chapter 10 for more information on the requirements for configuration and verification of a safety-related system containing the Kinetix 6200 and Kinetix 6500 drives.

## European Union Directives

## Functional Proof Tests

If this product is installed within the European Union or EEC regions and has the CE mark, the following regulations apply.

## CE Conformity

Conformity with the Low Voltage Directive and Electromagnetic Compatibility (EMC) Directive is demonstrated by using harmonized European Norm (EN) standards published in the Official Journal of the European Communities. The safe torque-off circuit complies with the EN standards when installed according instructions found in this manual.

## EMC Directive

This unit is tested to meet Council Directive 2004/108/EC Electromagnetic Compatibility (EMC) by using these standards, in whole or in part:

- EN 61800-3 - Adjustable Speed Electrical Power Drive Systems, Part 3 - EMC Product Standard including specific test methods
- EN 61326-2-1 EMC - Immunity requirements for safety-related systems

The product described in this manual is intended for use in an industrial environment.

CE Declarations of Conformity are available online at go to http://www.rockwellautomation.com/rockwellautomation/certification/ overview.page and in EC Declaration of Conformity on page 178 .

## Low Voltage Directive

These units are tested to meet Council Directive 2006/95/EC Low Voltage Directive. The EN 60204-1 Safety of Machinery-Electrical Equipment of Machines, Part 1-Specification for General Requirements standard applies in whole or in part. Additionally, the standard EN 50178 Electronic Equipment for use in Power Installations apply in whole or in part.

Refer to the Kinetix Servo Drives Specifications Technical Data, publication GMC-TD003, for environmental and mechanical specifications.

The functional safety standards require that functional proof tests be performed on the equipment used in the system. Proof tests are performed at user-defined intervals and are dependent upon PFD and PFH values.

## IMPORTANT

Your specific application determines the time frame for the proof test interval.

## PFD and PFH Definitions

## PFD and PFH Data

## Safe State

Safety-related systems can be classified as operating in either a Low Demand mode, or in a High Demand/Continuous mode.

- Low Demand mode: where the frequency of demands for operation made on a safety-related system is no greater than one per year or no greater than twice the proof-test frequency.
- High Demand/Continuous mode: where the frequency of demands for operation made on a safety-related system is greater than once per year or greater than twice the proof test interval.

The SIL value for a low demand safety-related system is directly related to orderof-magnitude ranges of its average probability of failure to satisfactorily perform its safety function on demand or, simply, average probability of failure on demand (PFD). The SIL value for a High Demand/Continuous mode safety-related system is directly related to the probability of a dangerous failure occurring per hour (PFH).

These PFD and PFH calculations are based on the equations from IEC 61508 and show worst-case values.

This table provides test data for a 20-year proof test interval and demonstrates the worst-case effect of various configuration changes on the data.

Table 1 - PFD and PFH for 20-year Proof Test Interval

| Attribute Single Encoder   | Dual Encoder   |
|----------------------------|----------------|
| PFH [1e-9] 5.88            | 2.37           |
| PFD [1e-4] 10.3            | 4.15           |
| SFF %  99.4%               | 99.5%          |

The Safe State encompasses all operation that occurs outside of the other monitoring and stopping behavior defined as part of the drive. In addition, configuration takes place in the Safe State. While the drive is in the Safe State, all safety control outputs, except the Door Control (DC\_Out) output, are in their safe state (de-energized). The Door Control (DC\_Out) output is in either the locked state or in the de-energized state depending upon the condition that resulted in the safe state.

When you cycle power, the drive enters the Safe State for self-testing. If the selftests pass and there is a valid configuration, the drive remains in the Safe State until a successful request for safe speed monitoring occurs.

If a Safe State fault is detected, the drive goes to the Safe State. This includes faults related to integrity of hardware or firmware.

For more information on faults, refer to Chapter 12 .

## Safety Reaction Time

## Considerations for Safety Ratings

The safety reaction time is the amount of time from a safety-related event as input to the system until the system is in the Safe State.

The safety reaction time from an input signal condition that triggers a safe stop, to the initiation of the configured Stop Type, is 20 ms (maximum).

The safety reaction time from an overspeed event that triggers a safe stop, to the actual initiation of the configured Stop Type, is equal to the value of the [Overspeed Response Time] parameter.

For more information on overspeed response time, see Overspeed Response Time on page 43 .

The achievable safety rating of an application that uses safe speed monitoring is dependent upon many factors, including the encoder setup, drive options, and the type of motor.

When using two independent encoders to monitor motion and when installed in a manner to avoid any common cause dangerous failure, the Kinetix 6200 and Kinetix 6500 drives can be used in applications up to and including SIL CL3, PLe, and CAT 4.

For applications that rely on commutation to generate torque and motion, a safety rating up to and including SIL CL3, PLe, and CAT 4 can be achieved.

## IMPORTANT

Some of the diagnostics performed on the encoder signals require motion to detect faults. You must make sure that motion occurs at least once every six months.

## Considerations for Single-encoder Applications

When configured correctly, the Kinetix 6200 and Kinetix 6500 drive performs these diagnostics on the encoder:

- Sin 2 + Cos 2 diagnostic
- Detection of open or short-circuit
- Encoder supply voltage monitoring
- Detection of illegal quadrature transitions of the sine and cosine signals

A safety rating up to and including SIL CL3, PLe, and CAT 4 can be achieved in a single-encoder application with these requirements:

- The motor is a permanent magnet (PM) brushless AC motor.
- The motor controller must be configured as a closed-loop application with field-oriented control by using the single-encoder for commutation.
- The motor-to-encoder coupling is designed to exclude shaft slippage as a dangerous failure mechanism.
- The encoder is of the Sin/Cos type and is suitable for the desired safety rating of the application.

An encoder that is suitable for SIL CL3 applications must follow one of these two conventions:

- – Use independent Sine/Cosine signals and be incapable of producing simulated signals when under an error condition.
- – Use simple or discreet circuitry with no complex or programmable internal devices.
- Encoder voltage monitoring in Kinetix 6200 and Kinetix 6500 drives can be enabled, depending on the feedback configuration.
- The system design of the motor/encoder-to-load coupling excludes shaft slippage and breakage as a dangerous failure mechanism.

## Understanding Commutation

Permanent magnet (PM), brushless AC motors are a class of synchronous motor that depends on electronic brushless commutation for their operation. In PM brushless motors, an electromagnetic field is created by the permanent magnets on the rotor. A rotating magnetic field is created by a number of electromagnets commutated electronically with IGBT's at the right speed, order, and times. Movement of the electromagnetic field is achieved by switching the currents in the coils of the stator winding. This process is called commutation. Interaction of the two electromagnetic fields produces magnetic force or torque.

## Notes:

## Safety Functions

<!-- image -->

## About the Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Features

This chapter describes the safe speed monitoring features of the Kinetix 6200 and Kinetix 6500 drives.

| Topic             |   Page |
|-------------------|--------|
| Safety Functions  |     21 |
| Hardware Features |     24 |

The Kinetix 6200 and Kinetix 6500 safe speed-monitoring servo drives feature five inputs, two sets of safety outputs, and one bipolar safety output. Each of the inputs and outputs support a specific safety function.

- Safe Stop (SS)
- Safe Limited Speed Monitoring (SLS)
- Door Monitoring (DM)
- Enabling Switch Monitoring (ESM)
- Lock Monitoring (LM)
- Door Control (DC)

An additional reset input provides for reset and monitoring of the safety circuit.

The drive can be used in single-axis or multi-axis applications, and can be configured as a master or slave based on its location in the system.

## Operation Modes

You can configure the drive to operate in one of 11 user-selectable operation modes, based on combinations of the safety functions listed on the previous page.

| Operation Mode                                                                                                                                                                                                                                                                                                                                        |   Page |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Disabled – In this mode, all safety functions are disabled.                                                                                                                                                                                                                                                                                           |     22 |
| Safe Stop – The drive activates the configured Stop Category upon deactivation of the Safe Stop input or the occurrence of a Stop Category fault.                                                                                                                                                                                                     |     55 |
| Safe Stop with Door Monitoring – In addition to monitoring for Safe Stop, the drive monitors the status of the door.                                                                                                                                                                                                                                  |     68 |
| Safe Limited Speed – In addition to monitoring for Safe Stop, the drive monitors the feedback velocity and compares it to a configurable Safe Speed Limit. If the velocity exceeds the limit, the drive initiates the configured Stop Category.                                                                                                       |     71 |
| Safe Limited Speed with Door Monitoring – In addition to monitoring for Safe Stop and Safe Limited Speed, the drive monitors the status of the door.                                                                                                                                                                                                  |     75 |
| Safe Limited Speed with Enabling Switch Control – In addition to monitoring for Safe Stop and Safe Limited Speed, the drive monitors the status of the Enabling Switch input.                                                                                                                                                                         |     78 |
| Safe Limited Speed with Door Monitor and Enabling Switch – In addition to monitoring for Safe Stop and Safe Limited Speed, the drive monitors the status of the door and the Enabling Switch input.                                                                                                                                                   |     79 |
| Safe Limited Speed (status only) – In addition to monitoring for Safe Stop, the drive monitors the feedback velocity and compares it to a configurable Safe Speed Limit. If the velocity exceeds the limit, the system status is made available as a safe output intended for a safety programmable logic controller. No stopping action takes place. |     84 |
| Slave, Safe Stop – The drive performs the same functions as Safe Stop. However, it regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output.                                                                          |     91 |
| Slave, Safe Limited Speed – The drive performs the same functions as Safe Limited Speed mode. However, it regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output.                                                   |     96 |
| Slave, Safe Limited Speed (status only) – The drive performs the same functions as Safe Limited Speed Status Only mode. However, it regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output.                         |     99 |

## Disabled Mode

In Disabled mode, all safety functions are disabled. Input, output, or speed monitoring diagnostics do not take place and all outputs are in their safe state. Motion power is enabled for drive commissioning in this mode.

| IMPORTANT   | The drive monitors motion for Safe Stop in every mode except Disabled.   |
|-------------|--------------------------------------------------------------------------|

## Lock Monitoring

Lock monitoring helps prevent access to the hazard during motion. In many applications, it is not sufficient for the machine to initiate a stop command once the door has been opened, because a high inertia machine can take a long time to stop. Preventing access to the hazard until a safe speed has been detected can be the safest condition. The lock monitoring feature is used to verify the operation of the door locking mechanism.

Lock monitoring can be enabled on single units or on the first unit in a multi-axis system. If the Lock Monitor input (LM\_In) indicates that the door is unlocked when the Door Control output (DC\_Out) is in the locked state, or if the Lock Monitor input indicates locked when the Door Monitor input (DM\_In) transitions from closed to open, the configured Stop Category is initiated.

## Safe Maximum Speed, Safe Maximum Acceleration, and Safe Direction Monitoring

Three additional safety functions, Safe Maximum Speed (SMS), Safe Maximum Acceleration (SMA) and Safe Direction Monitoring (SDM), operate independent of the other modes, relying on the Safe Stop function. When you configure the drive for Safe Maximum Speed, the feedback velocity is monitored and compared against a user-configurable limit. If the measured velocity is greater than or equal to the limit, the configured Stop Category is executed.

When Safe Acceleration Monitoring is enabled, the option monitors the acceleration rate and compares it to a configured Safe Maximum Acceleration Limit. If acceleration is detected as greater than or equal to the Safe Maximum Acceleration Limit, an Acceleration fault occurs. If an Acceleration fault is detected while the option is actively monitoring motion, the configured Stop Category is initiated.

Safe Direction Monitoring is also activated via option configuration. The option monitors the feedback direction and executes the configured Stop Category when motion in the illegal direction is detected.

Refer to Chapter 9 for detailed information on these functions.

## Hardware Features

The drive features five dual-channel inputs, two sets of sourcing safety outputs, and one bipolar safety output. You can configure dual-channel inputs to accept a following-contact configuration with two normally closed contacts, or one normally closed and one normally open contact. They can also be configured for single channel operation.

IMPORTANT

Single-channel operation does not meet SIL CL3, PLe, Cat 4 safety integrity.

These inputs also support output signal switching devices (OSSD). Each output has integral pulse-test checking circuitry.

The 2090-K6CK-D44M (44-pin) low-profile connector kit is designed specifically for use with the Kinetix 6200 and Kinetix 6500 modular drives. Safety connections are made by using this connector kit.

Figure 1 - 44-pin Low-profile Connector Kit

<!-- image -->

Refer to Wiring the Safety Connections on page 26 for the connector pinouts.

## General Safety Information

## Installation and Wiring

This chapter provides details on connecting devices and wiring the 2090-K6CKD44M Low-profile connector kit.

| Topic                         |   Page |
|-------------------------------|--------|
| General Safety Information    |     25 |
| Power Supply Requirements     |     26 |
| Wiring the Safety Connections |     26 |
| Terminal Connections          |     27 |
| Compatible Encoders           |     28 |

<!-- image -->

ATTENTION: The drive is intended to be part of the safety-related control system of a machine. Before installation, a risk assessment must be performed to determine whether the specifications of this safety option are suitable for all foreseeable operational and environmental characteristics for the system being installed.

Observe all electrical safety regulations stipulated by the appropriate technical authorities.

<!-- image -->

ATTENTION: Make sure that the electrical power supplied to the drive is switched off before making connections.

Refer to the Kinetix 6200 and Kinetix 6500 Modular Multi-axis Servo Drive User Manual, publication 2094-UM002, for more information.

<!-- image -->

## Power Supply Requirements

## Wiring the Safety Connections

The external power supply must conform to the Directive 2006/95/EC Low Voltage, by applying the requirements of EN61131-2 Programmable Controllers, Part 2 - Equipment Requirements and Tests and one of the following:

- EN60950 - SELV (Safety Extra Low Voltage)
- EN60204 - PELV (Protective Extra Low Voltage)
- IEC 60536 Safety Class III (SELV or PELV)
- UL 508 Limited Voltage Circuit
- 21.6…28.8V DC must be supplied by a power supply that complies with IEC/EN60204 and IEC/EN 61558-1.

For planning information, refer to the guidelines in Industrial Automation Wiring and Grounding Guidelines, Allen-Bradley publication 1770-4.1 .

Safety connections are made by using the 2090-K6CK-D44M low-profile connector kit.

Figure 2 - Making Safety Connections

<!-- image -->

Refer to the Kinetix 6200 and Kinetix 6500 Modular Multi-axis Servo Drive User Manual, publication 2094-UM002, for safety, auxiliary feedback, and I/O signal descriptions and wiring examples when using the 2090-K6CK-D44M connector kit.

## Terminal Connections

Prepare wires for termination on the IOD connector with a 5 mm (0.2 in.) strip length. Tighten all terminal screws firmly and recheck them after all connections have been made. Recommended terminal screw torque is 0.4 N·m (3.5 lb·in).

Refer to page 143 for the I/O signal electrical specifications.

Table 2 - IOD Connector Pinouts

15 24V Common 24VCOM 37 (S72) Enabling Sw. Mon. Input 0 ESM\_IN\_CH0

16 Reserved – 38 (S82) Enabling Sw. Mon. Input 1 ESM\_IN\_CH1

| IOD Pin (1)   | Description                                          | Signal           |
|---------------|------------------------------------------------------|------------------|
| 0             | Chassis Ground                                       | Shield           |
| 1             | Sine Differential Input + A Differential Input +     | AUX_SIN+ AUX_A+  |
| 2             | Sine Differential Input - A Differential Input -     | AUX_SIN AUX_A-                  |
| 3             | Cosine Differential Input + B Differential Input +   | AUX_COS+ AUX_B+  |
| 4             | Cosine Differential Input - B Differential Input -   | AUX_COS AUX_B-                  |
| 5             | Data Differential Input + Index Differential Input + | AUX_DATA+ AUX_I+ |
| 6             | Data Differential Input - Index Differential Input - | AUX_DATA AUX_I-                  |
| 7             | Clock Output +                                       | AUX_CLK+         |
| 8             | Clock Output -                                       | AUX_CLK-         |
| 9             | Encoder 5V Power Output EPWR_5V                      |                  |
|               | 10 Encoder Common                                    | ECOM             |
|               | 11 Encoder 9V Power Output EPWR_9V                   |                  |
|               | 12 Reserved                                          | –                |
|               | 13 Reserved                                          | –                |
|               | 14 24V Power Out                                     | 24VPWR (2)       |
|               | 17 (A1) Safety 24V Power Input SPWR                  |                  |
|               | 18 (A2) Safety 24V Common                            | SCOM             |
|               | 19 (S12) Safe Stop Input 0                           | SS_IN_CH0        |
|               | 20 (S22) Safe Stop Input 1                           | SS_IN_CH1        |
|               | 21 (34) Safe Stop Output 0                           | SS_OUT_CH0       |
|               | 22 (44) Safe Stop Output 1                           | SS_OUT_CH1       |

| IOD Pin (1)  Description                        | Signal      |
|-------------------------------------------------|-------------|
| 23 (S52) Safe Limited Speed Input 0 SLS_IN_CH0  |             |
| 24 (S62) Safe Limited Speed Input 1 SLS_IN_CH1  |             |
| 25 Reset Reference                              | RESET_REF   |
| 26 (S34) Reset Input                            | RESET_IN    |
| 27 (S11) Pulse Test Output 0                    | TEST_OUT_0  |
| 28 (S21) Pulse Test Output 1                    | TEST_OUT_1  |
| 29 (68) Safe Limited Speed Output 0 SLS_OUT_CH0 |             |
| 30 (78) Safe Limited Speed Output 1 SLS_OUT_CH1 |             |
| 31 (S32) Door Monitor Input 0                   | DM_IN_CH0   |
| 32 (S42) Door Monitor Input 1                   | DM_IN_CH1   |
| 33 (X32) Lock Monitor Input 0                   | LM_IN_CH0   |
| 34 (X42) Lock Monitor Input 1                   | LM_IN_CH1   |
| 35 (51) Door Control Channel Output- DC_OUT_CH0 |             |
| 36 (52) Door Control Channel Output+ DC_OUT_CH1 |             |
| 39 24V Power Out                                | 24VPWR  (3) |
| 40 24V Common                                   | 24VCOM      |
| 41 Digital Input 1                              | INPUT1      |
| 42 Digital Input 2                              | INPUT2      |
| 43 Digital Input 3                              | INPUT3      |
| 44 Digital Input 4                              | INPUT4      |

## Compatible Encoders

These feedback devices are supported.

|                          | Cat. No. and Description Additional Resources                                                     |                                                                                                                                                               |
|--------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sin/Cos Encoders (1)     | 842HR-xJxxx15FWYx                                                                                 | Refer to the Bulletin 842HR Sin/Cosine Encoders product profile, publication 842HR-PP001, for more information on these encoders.                             |
| Incremental Encoders (2) | 845T-xx12xxx-x and 845T-xx13xxx-x 845T-xx42xxx and 845T-xx43xxx-x 845T-xx52xxx and 845T-xx53xxx-x | Refer to the Sensors Reference Catalog, publication C116, for catalog number, dimensions, and specifications for Bulletin 845T and 845H Incremental Encoders. |
| Incremental Encoders (2) | 845H-SJxxx4xxYxx                                                                                  | Refer to the Sensors Reference Catalog, publication C116, for catalog number, dimensions, and specifications for Bulletin 845T and 845H Incremental Encoders. |
| Rotary Motors            | 1326AB-Bxxxx-M2L/S2L                                                                              | Refer to the Kinetix Motion Control Selection Guide, publication GMC-SG001 for more information on these motors.                                              |
| Rotary Motors            | MP-Series™ motors with embedded Sin/Cos or incremental encoders                                   | Refer to the Kinetix Motion Control Selection Guide, publication GMC-SG001 for more information on these motors.                                              |
| Rotary Motors            | Any motor with SRS-60 Stegmann encoder                                                            | Refer to the product documentation for your specific motor to determine the                                                                                   |
| Rotary Motors            | encoder type. Any motor with SRM-60 Stegmann encoder                                              | Refer to the product documentation for your specific motor to determine the                                                                                   |

## Inputs

## Speed Monitoring I/O Signals

This chapter describes the safe-speed monitoring input and output signals of the Kinetix 6200 and Kinetix 6500 drives.

| Topic   |   Page |
|---------|--------|
| Inputs  |     29 |
| Outputs |     35 |

The Kinetix 6200 and Kinetix 6500 drives have five inputs capable of safetycertified dual-channel support. Each dual-channel input supports a specific safety function of the drive: Safe Stop, Safe Limited Speed, Door Monitoring, Enabling Switch Monitoring, and Lock Monitoring.

All five inputs are electrically identical and rely on the same pair of pulse test outputs, Test\_Out\_0 and Test\_Out\_1, when not using the OSSD configuration.

The inputs can be configured for one of the following settings:

- Not used
- Dual-channel equivalent
- Dual-channel equivalent 3 s
- Dual-channel complementary
- Dual-channel complementary 3 s
- Dual-channel SS equivalent 3 s
- Single channel

## IMPORTANT

Single-channel configuration is not SIL CL3, PLe, Cat 4.

When configured for dual-channel operation, the consistency between the two channels is evaluated. For dual-channel equivalent configurations, the active state for both channel 0 and channel 1 is ON. For dual-channel complementary configurations, the active state for channel 0 is ON and the active state for channel 1 is OFF. Any time both channels are not active, the input pair is evaluated as OFF.

<!-- image -->

When both channels are active, if one channel's input terminal transitions from active to inactive and back to active, while the other channel's input terminal remains active, both channels must go inactive at the same time before the evaluated status can return to ON. This condition is called 'cycle inputs required'.

Figure 3 - Cycle Inputs Required

<!-- image -->

If inputs are configured with the following dual channel settings, an Input fault occurs if the inputs are discrepant for longer than 3 seconds or if a 'cycle inputs required' condition exists lor longer than 3 seconds.

- Dual-channel equivalent 3 s
- Dual-channel complementary 3 s
- Dual-channel SS equivalent 3 s

If inputs are configured with one of the following dual channel settings, which have no limit on the length of time that inputs can be discrepant, an Input fault does not occur for any discrepant condition or for any 'cycle inputs required' condition.

- Dual-channel equivalent
- Dual-channel complementary

For all input settings except Dual-channel SS equivalent 3 s, if one or two channels are connected to a 24V DC source other than terminals IOD-27 and IOD-28, a fault occurs.

I/O faults are Stop Category faults that initiate the configured Stop Category. I/O faults are latched until the drive is successfully reset.

For more information on I/O faults, refer to Troubleshooting the Safe Speed Monitoring Drive on page 133 .

When using a dual-channel complementary device, the normally-open input must be connected to the second input, as shown in the illustration. For example, if the door is open when the input is ON, the normally-open contact must be the second input (Input 1).

Figure 4 - Safety Input Wiring Examples

Drive Drive

<!-- image -->

<!-- image -->

## IMPORTANT

Cross wiring of Test Outputs to Inputs is not allowed. For example, do not connect TEST\_OUT\_0 to Input 1 or TEST\_OUT\_1 to Input 0.

Table 3 - IOD Connector Input Terminals

| Safe Stop (SS_In)   | Safe Limited Speed (SLS_In)   | Function  Door Monitoring (DM_In)                      | Enabling Switch Monitoring (ESM_In)   | Lock Monitoring (LM_In)   |
|---------------------|-------------------------------|--------------------------------------------------------|---------------------------------------|---------------------------|
|                     |                               | Input 0 = Channel 0 IOD-19 IOD-23 IOD-31 IOD-37 IOD-33 |                                       |                           |
|                     |                               | Input 1 = Channel 1 IOD-20 IOD-24 IOD-32 IOD-38 IOD-34 |                                       |                           |

Short-circuits of the input loop to ground or 24V are detected. For dual-channel inputs, cross loops are also detected.

## Safe Stop Input (SS\_In)

The SS\_In input is intended for connection to an E-Stop device.

The SS\_In input must be active to initiate Safe Stop monitoring. If the SS\_In input is being monitored, a transition from ON to OFF (closed to open) is used to request the configured Stop Category.

In a cascaded configuration, the SS\_In inputs of the middle and last drives are connected to the Safe Stop (SS\_Out) output of an upstream drive.

## Safe Limited Speed Input (SLS\_In)

The SLS\_In input is used to connect to a switch whose OFF state requests Safe Limited Speed monitoring.

If Safe Limited Speed monitoring is configured, the SLS\_In input is monitored from the time of a successful Safe Stop Reset or Safe Limited Speed Reset, until the time that the configured Stop Category is initiated or the Safe State is entered.

If the SLS\_In input is being monitored, the OFF state is used to request the Safe Limited Speed monitoring functionality of the drive.

In a cascaded configuration, the SLS\_In inputs of the middle and last drives are connected to the Safe Limited Speed (SLS\_Out) output of an upstream drive.

## Door Monitor Input (DM\_In)

This input monitors the status of the door to indicate if it is open or closed. The DM\_In input can be connected to a non-guardlocking switch if the door does not need to be locked. The door status is monitored by the first unit in multi-axis systems.

The DM\_In input is intended for connection to a guardlocking switch when the drive is configured as a master device with door monitoring. When the drive is configured as a slave in a cascaded system, its DM\_In input is connected to the Door Control output (DC\_Out) of the upstream drive.

Refer to Door Control Output (DC\_Out) on page 38 for more information.

## Enabling Switch Monitor Input (ESM\_In)

The ESM\_In input is intended to be connected to an enabling switch. The drive uses the ESM\_In input only as a safety enable, not for control. The ESM\_In inputs function and monitoring is performed by the first unit in multi-axis systems.

The ESM\_In input ON state is used to enable motion under mode-specific conditions in the Safety Limited Speed with Enabling Switch and Safe Limited Speed with Door Monitoring and Enabling Switch Monitoring modes.

Refer to Safe Limited Speed with Door Monitoring Mode on page 75 and Safe Limited Speed with Enabling Switch Monitoring Mode on page 78 for the conditions that must be true to start monitoring the ESM\_In input.

If the ESM\_In input is OFF while it is being monitored, an ESM Monitoring fault occurs and the drive initiates the configured Stop Category.

Refer to Chapter 12 for information on faults and how to recover from them.

## Lock Monitor Input (LM\_In)

The LM\_In input verifies that the guardlocking solenoid switch is locked. It is intended to confirm the door control function.

The LM\_In input is monitored by the first unit in multi-axis systems.

## Reset Input (Reset\_In)

The Reset input is for reset and monitoring of the safety circuit. The reset input can be configured for automatic, manual, or manual monitored reset types.

Wire the reset input terminal (IOD-26) to the 24V DC input terminal, (IOD-25), depending on the configured reset type, as shown.

Figure 5 - Reset Input Configurations

<!-- image -->

IMPORTANT

If you configure the drive for automatic reset, wiring of the reset input terminal (IOD-26) is not required.

## Outputs

The drive has three safety control outputs. The outputs have various output current capabilities, depending on function.

See the specifications in Appendix A to verify your power requirements.

## Safe Stop Output (SS\_Out)

The safe state for this signal is OFF.

These outputs are typically used in multi-axis applications. In multi-axis applications, you can use these outputs to daisy-chain the master drive to a slave.

For SS\_Out to SS\_In cascaded signals, the interface is a dual-channel sourcing solid-state safety output connected to a dual-channel safety input configured as OSSD. The outputs are pulse-tested.

Figure 6 - SS\_Out to SS\_In Connections for Multi-axis Applications

<!-- image -->

For more information on multi-axis configurations, see Cascaded Configurations starting on page 89 .

Alternately, the first SS\_Out output can be used to signal a programmable logic controller (PLC) that a Safe Stop has been requested.

If the SS\_In is ON (closed) and a successful Safe Stop Reset is performed, the SS\_Out output is turned ON. If Lock Monitoring is not enabled or the door control logic state is Unlock, the SS\_Out signal turns ON immediately when the SS\_In turns ON. If Lock Monitoring is enabled, and the door control logic state is Lock, the SS\_Out signal is not turned ON until the door has been locked by using the DC\_Out signal and the LM\_In input has been verified as ON.

If the Stop Category is initiated or if a Safe Stop is initiated due to a fault, the SS\_Out output is turned OFF.

If an error is detected on either channel of the dual-channel output, a fault occurs. I/O faults are Stop Category faults that initiate the configured Stop Category. The fault is latched until the drive is successfully reset.

For more information on faults, refer to Chapter 12 .

## Safe Limited Speed Output (SLS\_Out)

The safe state for this signal in all cases is OFF.

The SLS\_Out output functionality is determined by the configured Operation mode. If the SLS\_In is ON and a successful Safe Stop or Safe Limited Speed reset is performed, the SLS\_Out turns ON in all Safe Limited Speed modes except Safe Limited Speed Status Only.

For the Safe Limited Speed modes (SLS), the SLS\_Out is used to interconnect speed monitoring drives in multi-axis applications. For SLS\_Out to SLS\_In cascaded signals, the interface is a dual-channel sourcing solid state safety output connected to a dual-channel safety input configured as OSSD.

For a single unit system or the last unit in a cascaded system, the SLS\_Out is intended to be connected to an input of a safety programmable logic controller (PLC). The same PLC could also control the Safe Stop function with a safe PLC output connected to the Safe Stop input (SS\_In).

For the first or middle units in a cascaded system, the SLS\_Out is intended to be connected to the Safe Limited Speed input (SLS\_In) of the next drive in the cascaded system. This lets one SLS switch enable Safe Limited Speed on all axes at the same time.

Figure 7 - SLS\_Out to SLS\_In Connections for Multi-axis Applications

<!-- image -->

For more information on multi-axis configurations, see Cascaded Configurations starting on page 89 .

For Safe Limited Speed Status Only modes, the SLS\_Out output is used as an indication that the Safe Limited Speed monitoring is active and the monitored speed is less than the configured Safe Speed Limit. If the speed is greater than or equal to the Safe Speed Limit, the SLS\_Out is turned OFF. When Safe Limited Speed monitoring is not active or the drive is in a SLS Monitoring Delay, the SLS\_Out output is OFF. The SLS\_Out output is turned OFF when a Safe Stop has been initiated, a fault has occurred, or the drive is in the safe state.

See Safe Limited Speed Status Only Mode on p page 84 for more information.

If an error is detected on either channel of the dual-channel output, a fault occurs. I/O faults are Stop Category faults that initiate the configured Stop Category. The fault is latched until the drive is successfully reset.

For more information on faults, refer to Chapter 12 .

## Door Control Output (DC\_Out)

You can use this output for door control in single-axis and multi-axis systems. This output attempts to maintain last state when a fault occurs.

The DC\_Out output is updated based on door control logic status, the [Door Control Output] parameter setting, and any Safe State faults that can be detected.

This output is Unlocked only when motion is verified to be at Standstill Speed or Safe Limited Speed.

Figure 8 - Door Control and Lock Monitoring

<!-- image -->

TIP

Check your interlock switch for internal jumpers before installation.

If an error is detected on either channel of the dual-channel output, a fault occurs. I/O faults are Stop Category faults that initiate the configured Stop Category. The fault is latched until the drive is successfully reset.

For more information on faults, refer to Chapter 12 .

The DC\_Out output can be used as a bipolar output in Power to Release or Power to Lock configurations, or it can be configured as Cascading (2Ch Sourcing).

When the Door Control output is configured as cascading (2Ch Sourcing), the dual-channel bipolar output acts as two sourcing outputs capable of driving the OSSD Door Monitor input (DM\_In) of the next speed monitoring drive in the cascaded chain. The DC\_out output can also be used as a source for general purpose inputs. In this configuration, the current is limited to 20 mA.

Figure 9 - Door Control Cascading Outputs

<!-- image -->

Only the wiring configurations shown below are supported for the Door Control output.

Figure 10 - Door Control Output Wiring

<!-- image -->

- (1) When wired as a source for a safety input, current is limited to 20 mA per output.
- (2) For example, SmartGuard 600 controller, Guard I/O module.

Short-circuits of the output loop to ground or 24V are detected. For cascaded outputs, cross loops are also detected.

## Notes:

## Cascaded Configuration

<!-- image -->

## General Device and Feedback Monitoring Configuration

This chapter describes the general and feedback configuration settings that must be configured to operate the safe speed monitoring features.

| Topic                   |   Page |
|-------------------------|--------|
| Cascaded Configuration  |     41 |
| Operation Mode          |     42 |
| Reset Type              |     42 |
| Overspeed Response Time |     43 |
| General Parameter List  |     48 |
| Feedback Monitoring     |     49 |
| Feedback Parameter List |     54 |

The drive can be used in single-axis or multi-axis applications. The [System Configuration] parameter indicates the drive's location in the system: Single Unit (Single), Cascaded First Unit (Multi First), Cascaded Middle Unit (Multi Mid), or Cascaded Last Unit (Multi Last). Single unit and cascaded first options are system masters.

Refer to Chapter 8 for more information on cascaded configurations.

## Operation Mode

## Reset Type

You can configure the drive to operate in one of 11 user-selectable Operation modes, based on combinations of the safety functions the drive supports. The modes, except for Disabled, are described in detail in subsequent chapters of this manual.

Table 4 - Safety Function Combinations

| For these modes                                                       | See       |
|-----------------------------------------------------------------------|-----------|
| Master, Safe Stop                                                     | Chapter 6 |
| Master, Safe Stop - Door Monitor                                      | Chapter 6 |
| Master, Safe Stop - Safe Limited Speed                                | Chapter 7 |
| Master, Safe Stop - Safe Limited Speed - Door Monitor                 | Chapter 7 |
| Master, Safe Stop - Safe Limited Speed - Enable Switch                | Chapter 7 |
| Master, Safe Stop - Safe Limited Speed - Door Monitor - Enable Switch | Chapter 7 |
| Master, Safe Stop - Safe Limited Speed Status Only                    | Chapter 7 |
| Slave, Safe Stop                                                      | Chapter 8 |
| Slave, Safe Limited Speed                                             | Chapter 8 |
| Slave, Safe Limited Speed Status Only                                 | Chapter 8 |

You can configure the [Reset Type] parameter as automatic, manual, or manual monitored. The default is manual monitored. The configured Reset Type applies to both Safe Stop and Safe Limited Speed Resets.

TIP The Reset input does not require wiring for automatic reset configurations.

See Safe Stop Reset on page 63 and page 69, and Safe Limited Speed Reset on page 73 , page 76, and page 78 for details on how the [Reset Type] parameter affects Safe Stop and Safe Limited Speed operation.

<!-- image -->

ATTENTION: For all types of reset (automatic, manual, or manual monitored), if a reset of the Safe Stop or Safe Limited Speed functions can result in machine operation, the other speed monitoring functions must be configured to detect and prevent dangerous motion.

<!-- image -->

ATTENTION: The Safe Stop Reset does not provide safety-related restart according to EN 60204-1. Restart must be performed by external measures if automatic restart could result in a hazardous situation. You are responsible for determining whether automatic restart could pose a hazard.

## Overspeed Response Time

The [Overspeed Response Time] parameter setting determines the maximum reaction time from an overspeed event to the initiation of the configured [Stop Category]. The safety reaction time from an overspeed event that triggers a Stop Category, to the actual initiation of that Stop Category, is equal to the value of the [Overspeed Response Time] parameter. The configurable options are 42, 48, 60, 84, 132, 228, and 420 ms.

The [Overspeed Response Time] parameter setting also determines the speed resolution that can be achieved. The Overspeed Response Time and the encoder resolution affect the speed resolution accuracy as shown in the tables on the following pages.

## Speed Resolution Accuracy for Rotary Systems

Table 5 - Encoder Resolution 16 lines/rev

| Overspeed Response Time Setting   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)                                     | Speed (RPM)                  |
|-----------------------------------|---------------|---------------|---------------|---------------|-------------------------------------------------|------------------------------|
| Overspeed Response Time Setting   |               |               |               |               |                                                 | 1 10 100 1000 10,000 100,000 |
| 42                                |               |               |               |               | 156.253 156.283 156.583 159.583 189.583 489.583 |                              |
| 48                                | 78.127        | 78.142        | 78.292        | 79.792        | 94.792                                          | 244.792                      |
| 60                                | 39.063        | 39.071        | 39.146        | 39.896        | 47.396                                          | 122.396                      |
| 84                                | 19.532        | 19.535        | 19.573        | 19.948        | 23.698                                          | 61.198                       |
| 132                               | 9.766         | 9.768         | 9.786         | 9.974         | 11.849                                          | 30.599                       |
| 228                               | 4.883         | 4.884         | 4.893         | 4.987         | 5.924                                           | 15.299                       |
| 420                               | 2.441         | 2.442         | 2.447         | 2.493         | 2.962                                           | 7.650                        |

Table 6 - Encoder Resolution 128 lines/rev

| Overspeed Response Time Setting   |   Speed (RPM) |   Speed (RPM) |   Speed (RPM) |   Speed (RPM) | Speed (RPM)   | Speed (RPM)   |
|-----------------------------------|---------------|---------------|---------------|---------------|---------------|---------------|
| Overspeed Response Time Setting   |         1     |        10     |       100     |      1000     |               | 10,000 93,750 |
| 42                                |        19.535 |        19.565 |        19.865 |        22.865 | 52.865        | 332.031       |
| 48                                |         9.767 |         9.782 |         9.932 |        11.432 | 26.432        | 166.016       |
| 60                                |         4.884 |         4.891 |         4.966 |         5.716 | 13.216        | 83.008        |
| 84                                |         2.442 |         2.446 |         2.483 |         2.858 | 6.608         | 41.504        |
| 132                               |         1.221 |         1.223 |         1.242 |         1.429 | 3.304         | 20.752        |
| 228                               |         0.61  |         0.611 |         0.621 |         0.715 | 1.652         | 10.376        |
| 420                               |         0.305 |         0.306 |         0.31  |         0.357 | 0.826         | 5.188         |

## Table 7 - Encoder Resolution 1000 lines/rev

| Overspeed Response Time Setting   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)                 | Speed (RPM)   |
|-----------------------------------|---------------|---------------|---------------|---------------|-----------------------------|---------------|
| Overspeed Response Time Setting   |               |               |               |               | 1 10 100 1000 10,000 12,000 |               |
| 42                                | 2.503         | 2.533         | 2.833         | 5.833         | 35.833                      | 42.500        |
| 48                                | 1.252         | 1.267         | 1.417         | 2.917         | 17.917                      | 21.250        |
| 60                                | 0.626         | 0.633         | 0.708         | 1.458         | 8.958                       | 10.625        |
| 84                                | 0.313         | 0.317         | 0.354         | 0.729         | 4.479                       | 5.313         |
| 132                               | 0.156         | 0.158         | 0.177         | 0.365         | 2.240                       | 2.656         |
| 228                               | 0.078         | 0.079         | 0.089         | 0.182         | 1.120                       | 1.328         |
| 420                               | 0.039         | 0.040         | 0.044         | 0.091         | 0.560                       | 0.664         |

## Table 8 - Encoder Resolution 1024 lines/rev

| Overspeed Response Time Setting   |   Speed (RPM) |   Speed (RPM) |   Speed (RPM) |   Speed (RPM) | Speed (RPM)   | Speed (RPM)      |
|-----------------------------------|---------------|---------------|---------------|---------------|---------------|------------------|
| Overspeed Response Time Setting   |         1     |        10     |       100     |      1000     |               | 10,000 11,718.75 |
| 42                                |         2.445 |         2.475 |         2.775 |         5.775 | 35.775        | 41.504           |
| 48                                |         1.222 |         1.237 |         1.387 |         2.887 | 17.887        | 20.752           |
| 60                                |         0.611 |         0.619 |         0.694 |         1.444 | 8.944         | 10.376           |
| 84                                |         0.306 |         0.309 |         0.347 |         0.722 | 4.472         | 5.188            |
| 132                               |         0.153 |         0.155 |         0.173 |         0.361 | 2.236         | 2.594            |
| 228                               |         0.076 |         0.077 |         0.087 |         0.18  | 1.118         | 1.297            |
| 420                               |         0.038 |         0.039 |         0.043 |         0.09  | 0.559         | 0.648            |

Table 9 - Encoder Resolution 3000 lines/rev

| Overspeed Response Time Setting   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)        | Speed (RPM)   |
|-----------------------------------|---------------|---------------|---------------|--------------------|---------------|
| Overspeed Response Time Setting   |               |               |               | 1 10 100 1000 4000 |               |
| 42                                | 0.837         | 0.867         | 1.167         | 4.167              | 14.167        |
| 48                                | 0.418         | 0.433         | 0.583         | 2.083              | 7.083         |
| 60                                | 0.209         | 0.217         | 0.292         | 1.042              | 3.542         |
| 84                                | 0.105         | 0.108         | 0.146         | 0.521              | 1.771         |
| 132                               | 0.052         | 0.054         | 0.073         | 0.260              | 0.885         |
| 228                               | 0.026         | 0.027         | 0.036         | 0.130              | 0.443         |
| 420                               | 0.013         | 0.014         | 0.018         | 0.065              | 0.221         |

Table 10 - Encoder Resolution 5000 lines/rev

| Overspeed Response Time Setting   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)   | Speed (RPM)        | Speed (RPM)   |
|-----------------------------------|---------------|---------------|---------------|--------------------|---------------|
| Overspeed Response Time Setting   |               |               |               | 1 10 100 1000 2400 |               |
| 42                                | 0.503         | 0.533         | 0.833         | 3.833              | 8.500         |
| 48                                | 0.252         | 0.267         | 0.417         | 1.917              | 4.250         |
| 60                                | 0.126         | 0.133         | 0.208         | 0.958              | 2.125         |
| 84                                | 0.063         | 0.067         | 0.104         | 0.479              | 1.063         |
| 132                               | 0.031         | 0.033         | 0.052         | 0.240              | 0.531         |
| 228                               | 0.016         | 0.017         | 0.026         | 0.120              | 0.266         |
| 420                               | 0.008         | 0.008         | 0.013         | 0.060              | 0.133         |

## Speed Resolution Accuracy for Linear Systems

Table 11 - Encoder Resolution 500 lines/mm

| Overspeed Response Time Setting   |   Speed (mm/s) |   Speed (mm/s) |   Speed (mm/s) |   Speed (mm/s) |   Speed (mm/s) |   Speed (mm/s) |
|-----------------------------------|----------------|----------------|----------------|----------------|----------------|----------------|
| Overspeed Response Time Setting   |          0.01  |          0.1   |          1     |         10     |        100     |        400     |
| 42                                |          0.083 |          0.084 |          0.087 |          0.117 |          0.417 |          1.417 |
| 48                                |          0.042 |          0.042 |          0.043 |          0.058 |          0.208 |          0.708 |
| 60                                |          0.021 |          0.021 |          0.022 |          0.029 |          0.104 |          0.354 |
| 84                                |          0.01  |          0.01  |          0.011 |          0.015 |          0.052 |          0.177 |
| 132                               |          0.005 |          0.005 |          0.005 |          0.007 |          0.026 |          0.089 |
| 228                               |          0.003 |          0.003 |          0.003 |          0.004 |          0.013 |          0.044 |
| 420                               |          0.001 |          0.001 |          0.001 |          0.002 |          0.007 |          0.022 |

Table 12 - Encoder Resolution 1000 lines/mm

| Overspeed Response Time Setting   | Speed (mm/s)   | Speed (mm/s)   | Speed (mm/s)   | Speed (mm/s)   | Speed (mm/s)          | Speed (mm/s)   |
|-----------------------------------|----------------|----------------|----------------|----------------|-----------------------|----------------|
| Overspeed Response Time Setting   |                |                |                |                | 0.01 0.1 1 10 100 200 |                |
| 42                                | 0.042          | 0.042          | 0.045          | 0.075          | 0.375                 | 0.708          |
| 48                                | 0.021          | 0.021          | 0.023          | 0.038          | 0.188                 | 0.354          |
| 60                                | 0.010          | 0.011          | 0.011          | 0.019          | 0.094                 | 0.177          |
| 84                                | 0.005          | 0.005          | 0.006          | 0.009          | 0.047                 | 0.089          |
| 132                               | 0.003          | 0.003          | 0.003          | 0.005          | 0.023                 | 0.044          |
| 228                               | 0.001          | 0.001          | 0.001          | 0.002          | 0.012                 | 0.022          |
| 420                               | 0.001          | 0.001          | 0.001          | 0.001          | 0.006                 | 0.011          |

Table 13 - Encoder Resolution 5000 lines/mm

| Overspeed Response Time Setting   | Speed (mm/s)                                 | Speed (mm/s)   | Speed (mm/s)   | Speed (mm/s)   | Speed (mm/s)   |
|-----------------------------------|----------------------------------------------|----------------|----------------|----------------|----------------|
| Overspeed Response Time Setting   | 0.01 0.1 1 10 40                             |                |                |                |                |
| 42                                | 0.008367 0.008667 0.011667 0.041667 0.141667 |                |                |                |                |
| 48                                | 0.004183 0.004333 0.005833 0.020833 0.070833 |                |                |                |                |
| 60                                | 0.002092 0.002167 0.002917 0.010417 0.035417 |                |                |                |                |
| 84                                | 0.001046 0.001083 0.001458 0.005208 0.017708 |                |                |                |                |
| 132                               | 0.000523 0.000542 0.000729 0.002604 0.008854 |                |                |                |                |
| 228                               | 0.000261 0.000271 0.000365 0.001302 0.004427 |                |                |                |                |
| 420                               | 0.000131 0.000135 0.000182 0.000651 0.002214 |                |                |                |                |

Table 14 - Encoder Resolution 20,000 lines/mm

| Overspeed Response Time Setting   | Speed (mm/s)   | Speed (mm/s)                        | Speed (mm/s)   | Speed (mm/s)   |
|-----------------------------------|----------------|-------------------------------------|----------------|----------------|
| Overspeed Response Time Setting   | 0.01           | 0.1  1  10                          |                |                |
| 42                                |                | 0.002117 0.002417 0.005417 0.035417 |                |                |
| 48                                |                | 0.001058 0.011208 0.002708 0.017708 |                |                |
| 60                                |                | 0.000529 0.000604 0.001354 0.008854 |                |                |
| 84                                |                | 0.000265 0.000302 0.000677 0.004427 |                |                |
| 132                               |                | 0.000132 0.000151 0.000339 0.002214 |                |                |
| 228                               |                | 0.000066 0.000076 0.000169 0.001107 |                |                |
| 420                               |                | 0.000033 0.000038 0.000085 0.000553 |                |                |

For example, an encoder resolution of 128 and Overspeed Response Time of 42 ms results in a speed resolution accuracy of ±19.865 RPM if your Safe Maximum Speed is configured for 100.0 RPM. An SMS Speed fault can occur when encoder 1 is at 80.135 RPM. However, the SMS Speed fault cannot occur until encoder 1 reaches 119.865 RPM.

Figure 11 - Need Figure Title Here

<!-- image -->

If your encoder resolution is not listed in the tables, use these equations.

For rotary systems, the conversion from [Overspeed Response Time] to Speed Resolution in revolutions per minute is:

Speed Resolution =

(RPM)

15000

(Overspeed Response Time - 36) x Feedback Resolution

(Overspeed Response Time - 36)

For linear systems, the conversion from [Overspeed Response Time] to mm/s is:

250

(Overspeed Response Time - 36) x Feedback Resolution

Speed Resolution =

(mm/s)

IMPORTANT

Speed (RPM) x 0.02

(Overspeed Response Time - 36)

To avoid nuisance FEEDBACK 1 faults, do not configure Overspeed Response Time in the shaded area of Table 15 .

Table 15 - Allowable Overspeed Response/Encoder Resolution Setting

| Encoder Resolution Lines/Rev   | Overspeed Response Time (ms)                     | Overspeed Response Time (ms)                   | Overspeed Response Time (ms)   | Overspeed Response Time (ms)   | Overspeed Response Time (ms)   | Overspeed Response Time (ms)   | Overspeed Response Time (ms)   |
|--------------------------------|--------------------------------------------------|------------------------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------------------------|
| Encoder Resolution Lines/Rev   |                                                  | 42 48 60 84 132 228 420                        |                                |                                |                                |                                |                                |
| 16                             | 156.250  78.125                                  | 39.063  19.531 9.766 4.883 2.441               |                                |                                |                                |                                |                                |
| 32                             | 78.125  39.063                                   | 19.531 9.766 4.883 2.441 1.221                 |                                |                                |                                |                                |                                |
| 64                             | 39.063                                           | 19.531 9.766 4.883 2.441 1.221 0.610           |                                |                                |                                |                                |                                |
| 128                            | 19.531 9.766 4.883 2.441 1.221 0.610 0.305       |                                                |                                |                                |                                |                                |                                |
|                                |                                                  | 256 9.766 4.883 2.441 1.221 0.610 0.305 0.153  |                                |                                |                                |                                |                                |
|                                |                                                  | 512 4.883 2.441 1.221 0.610 0.305 0.153 0.076  |                                |                                |                                |                                |                                |
|                                |                                                  | 1024 2.441 1.221 0.610 0.305 0.153 0.076 0.038 |                                |                                |                                |                                |                                |
|                                |                                                  | 2048 1.221 0.610 0.305 0.153 0.076 0.038 0.019 |                                |                                |                                |                                |                                |
|                                |                                                  | 4096 0.610 0.305 0.153 0.076 0.038 0.019 0.010 |                                |                                |                                |                                |                                |
|                                |                                                  | 8192 0.305 0.153 0.076 0.038 0.019 0.010 0.005 |                                |                                |                                |                                |                                |
|                                | 16,384 0.153 0.076 0.038 0.019 0.010 0.005 0.002 |                                                |                                |                                |                                |                                |                                |
| 32,768                         |                                                  | 0.076 0.038 0.019 0.010 0.005 0.002 0.001      |                                |                                |                                |                                |                                |

<!-- formula-not-decoded -->

+

## General Parameter List

Set these parameters to configure general operation of the drive.

## Table 16 - General Parameters

| Tab                                | Parameter Name Description                                                                                                                           | Values (Safety Configuration Tool)                                                                                                                                                                                                            |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Change System Configuration | System Configuration Defines whether the drive is a single unit or if it occupies a first, middle, or last position in a multi-axis cascaded system. | Default: Single Unit                                                                                                                                                                                                                          |
| Safety Change System Configuration | System Configuration Defines whether the drive is a single unit or if it occupies a first, middle, or last position in a multi-axis cascaded system. | Options: Single Unit Cascaded First Unit Cascaded Middle Unit Cascaded Last Unit                                                                                                                                                              |
| Safety Change System Configuration | Operation Mode Defines the primary operating mode of the speed monitoring safety functions.                                                          | Default: SafeStop                                                                                                                                                                                                                             |
| Safety Change System Configuration | Operation Mode Defines the primary operating mode of the speed monitoring safety functions.                                                          | Options: Disabled SafeStop SafeStop-DoorMonitor SafeStop-SafeLimitedSpeed SafeStop-SafeLimitedSpeed-DoorMonitor SafeStop-SafeLimitedSpeed-EnableSwitch SafeStop-SafeLimitedSpeed-DoorMonitor-EnableSwitch SafeStop-SafeLimitedSpeedStatusOnly |
| Safety Change System Configuration | Reset Type Defines the type of reset used by the drive. Default: Manual Monitored                                                                    |                                                                                                                                                                                                                                               |
| Safety Change System Configuration | Reset Type Defines the type of reset used by the drive. Default: Manual Monitored                                                                    | Options: Automatic Manual Manual Monitored                                                                                                                                                                                                    |
| Safety Change System Configuration | Configuration for the feedback interface sampling rate. Default: 42 ms                                                                               |                                                                                                                                                                                                                                               |
| Safety Change System Configuration | Configuration for the feedback interface sampling rate. Default: 42 ms                                                                               | Options: 42 ms 48 ms 60 ms 84 ms 132 ms 228 ms 420 ms                                                                                                                                                                                         |

## Feedback Monitoring

The [Feedback Mode] parameter defines whether the feedback monitoring devices are configured as a single encoder or as dual encoders. When two encoders are used, the [Feedback Mode] parameter also defines the type of discrepancy checking that is performed between the two encoders.

## IMPORTANT

Feedback devices can be a Sin/Cos or incremental feedback device.

You choose the type of feedback device, either sine/cosine or incremental for encoder 1 by using the [Primary Feedback Type] parameter. You also choose the feedback type, resolution, and polarity of both encoders.

Configure the feedback type as rotary or linear by using the [Primary Feedback Units] parameter. Configure the resolution in lines per revolution or lines per millimeter by using the [Primary Feedback Cycles] parameter.

For dual encoder configurations, the resolution of the first encoder can be different than the resolution of the second encoder. After discrepancy testing has passed, the speed, relative position, and direction used by the drive are based on encoder 1.

## IMPORTANT

For dual-encoder configurations, the resolution of the first encoder can be different than the resolution of the second encoder, but it must be equal to or higher than the resolution of the second encoder.

## Feedback Polarity

Configure the direction of polarity to be the same as the encoder or reversed by using the [Primary Feedback Polarity] parameter. The drive defines the normal positive direction for encoders as A leading B. To use encoders where B leads A, you must choose Negative for the [Primary Feedback Polarity] parameter. Set the [Secondary Feedback Polarity] parameter so that the resulting speed direction is of the same polarity as encoder 1.

## Single Encoder

If the [Feedback Mode] parameter is set to Single Encoder, the single encoder input is processed redundantly and cross-checked in a 1oo2 architecture. The speed, direction, and stopped status are derived from the single encoder by the 1oo2 architecture.

TIP

If the [Feedback Mode] parameter is set to Single Encoder, the single encoder input corresponds to the Kinetix 6200 motor feedback (MF connector) connections.

Refer to Considerations for Safety Ratings, on page 18, for more information.

## Dual Encoders

If the [Feedback Mode] parameter is set to Dual Encoders, each encoder input is processed by a single channel and cross-checked in a 1oo2 architecture. Discrepancy checking is performed between the two encoders. After the discrepancy checks have passed, the speed, direction, and stopped status are derived from encoder 1.

TIP

If the [Feedback Mode] parameter is set to Dual Encoders, the encoder 1 input corresponds to the Kinetix 6200 motor feedback (MF) connector and the encoder 2 input corresponds to Kinetix 6200 auxiliary feedback (IOD) connector.

IMPORTANT

All monitoring functions are based on the speed of encoder 1. The encoder 2 signal is used for fault diagnostics.

Speed and direction checks are affected by these parameters:

- Dual Feedback Speed Ratio, [Velocity Ratio]
- Dual Feedback Position Tolerance, [Position Discrepancy Tolerance]
- Dual Feedback Speed Discrepancy Tolerance, [Velocity Discrepancy Tolerance]

## Dual Feedback Speed Ratio

The Dual Feedback Speed Ratio, [Velocity Ratio] parameter, is defined as the ratio of the expected speed of encoder 2 divided by the expected speed of encoder 1. This parameter configures the anticipated gearing between encoder 1 and encoder 2.

<!-- image -->

| Dual Feedback Speed Ratio   | Expected Speed of Encoder 2   |
|-----------------------------|-------------------------------|
| [Velocity Ratio] Parameter  | Expected Speed of Encoder 1   |

If [Feedback Mode] equals Single Encoder, the only legal value for [Velocity Ratio] parameter is 0.0.

If [Feedback Mode] is any Dual Encoder configuration, the range of legal values for [Velocity Ratio] is from 0.0001…10,000.0.

For example, if encoder 2's speed is expected to be 1000 revolutions per second while encoder 1's speed is expected to be 100 revolutions per second, then configure the [Velocity Ratio] as 10.0.

The units used to measure encoder speed are configurable as either rotary (rev) or linear (mm) units. Any combination of rotary and linear units for the two encoders is allowed.

## Dual Feedback Position Discrepancy Tolerance

The Dual Feedback Position Discrepancy Tolerance, [Position Discrepancy Tolerance] parameter, defines the cumulative position discrepancy that is tolerated between encoder 1 and encoder 2. The position discrepancy is defined as position change relative to encoder 1.

| IMPORTANT   | The relative position discrepancy difference is reset to zero at each Safe Stop Reset.   |
|-------------|------------------------------------------------------------------------------------------|

This discrepancy checking is performed only while the [Feedback Mode] parameter is equal to one of these values.

## [Feedback Mode] Parameter Settings

Dual encoder with speed and position discrepancy checking

Dual encoder with position discrepancy checking

## This table defines the legal values for each Feedback mode value.

| [Feedback Mode] Parameter Settings             | Dual Feedback Position Discrepancy Tolerance, [Position Discrepancy Tolerance] Legal Values                                                            |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| One encoder                                    | 0                                                                                                                                                      |
|                                                | Dual encoder with speed and position discrepancy 1…65,535 in degrees (rotary encoders) or mm (linear encoders) relative to the resolution of encoder 1 |
| Dual encoder with speed discrepancy checking 0 |                                                                                                                                                        |
|                                                | Dual encoder with position discrepancy checking 1…65,535 in degrees (rotary encoders) or mm (linear encoders) relative to the resolution of encoder 1  |

If an illegal value is detected, an Invalid Configuration fault occurs and the drive remains in the Safe State.

| IMPORTANT   | When setting discrepancy tolerances, consider that configuring a high gear ratio between encoder 1 and encoder 2 can lead to unexpected dual feedback position faults. This is because a very large encoder 1 movement translates into a very small encoder 2 movement.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Dual Feedback Speed Discrepancy Tolerance

The Dual Feedback Speed Discrepancy Tolerance [Velocity Discrepancy Tolerance] parameter, defines the discrepancy that is tolerated for a difference in speed between encoder 1 and encoder 2. This speed is relative to encoder 1. This discrepancy checking is performed only while the Feedback mode is equal to one of these values.

| [Feedback Mode] Parameter Settings                        |
|-----------------------------------------------------------|
| Dual encoder with speed and position discrepancy checking |
| Dual encoder with speed discrepancy checking              |

For rotary systems, the value is specified in revolutions per minute. For linear systems, the value is specified in mm per second.

| [Feedback Mode] Parameter Settings                        | Dual Feedback Speed Discrepancy Tolerance, [Velocity Discrepancy Tolerance] Values                             |
|-----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| One encoder                                               | 0                                                                                                              |
| Dual encoder with speed and position discrepancy checking | 0.1…6553.5 in rev/min (rotary encoders) or mm/s (linear encoders)                                              |
|                                                           | Dual encoder with speed discrepancy checking 0.1…6553.5 in rev/min (rotary encoders) or mm/s (linear encoders) |
| Dual encoder with position discrepancy checking 0         |                                                                                                                |

If an illegal value is detected, an Invalid Configuration fault occurs and the drive remains in the Safe State.

## Feedback Voltage Monitoring Range

Use the [5V Monitoring] and [9V Monitoring] parameters to set the feedback voltage monitoring range. The monitoring ranges help define the trip zone for encoder 1 and encoder 2, respectively.

Table 17 - Feedback Voltage Monitoring Range

|                                                              | 5/9V Monitoring Setting   |                | 5 9        |
|--------------------------------------------------------------|---------------------------|----------------|------------|
|                                                              | Range                     | 4.5…5.5V 7…12V |            |
|                                                              | Trip Zone                 | < 4.5V         | < 7V       |
| The encoder must be specified                                | Can Trip                  | 4.5…4.62V      | 7…7.4V     |
| to operate across this complete No Trip 4.62…5.38V 7.4…11.4V |                           |                |            |
| range or larger.                                             | Can Trip                  | 5.38…5.5V      | 11.4…12.0V |
|                                                              | Trip Zone                 | >5.5V          | > 12.0V    |

Your power supply must stay within the No Trip range.

## Feedback Fault

The allowable frequency of feedback input signals is limited. The drive monitors feedback signals whenever its configuration is valid and the Operation mode is not configured as Disabled.

Table 18 - Maximum Encoder Frequency

|             | Encoder Type Frequency, max   |
|-------------|-------------------------------|
| Sine/cosine | ≤ 100 kHz                     |
| Incremental | ≤ 200 kHz                     |

If the feedback signals indicate greater-than or equal-to the maximum value, a Feedback\_x fault (Safe State fault) occurs (x equals 1 or 2 depending upon the encoder that has the fault).

Diagnostics are performed on the encoder input signals. If the encoder diagnostic tests fail, a Feedback\_x fault (Safe State fault) occurs.

## Feedback Parameter List

To define the type of feedback used by the drive, set these parameters.

TIP

Secondary feedback parameter settings are not required when the [Feedback Mode] parameter setting is single encoder.

Table 19 - Feedback Parameters

| Tab                                    | Parameter Name Description     | Values                                                                                                                                                         | (Safety Configuration Tool)                                                                                                                   |
|----------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Feedback Change Feedback Configuration |                                | Feedback Mode Selects the number of feedback devices and the type of discrepancy checking.                                                                     | Default: Single Encoder                                                                                                                       |
| Feedback Change Feedback Configuration |                                | Feedback Mode Selects the number of feedback devices and the type of discrepancy checking.                                                                     | Options: Single Encoder Dual Encoders w/speed and position discrepancy Dual Encoders w/speed discrepancy Dual Encoders w/position discrepancy |
| Feedback Change Feedback Configuration |                                | 5V Monitoring Enable 5V monitoring.                                                                                                                            | Default: Voltage not monitored                                                                                                                |
| Feedback Change Feedback Configuration |                                | 5V Monitoring Enable 5V monitoring.                                                                                                                            | Options: Voltage not monitored Voltage monitored                                                                                              |
| Feedback Change Feedback Configuration |                                | 9V Monitoring Enable 9V monitoring.                                                                                                                            | Default: Voltage not monitored                                                                                                                |
| Feedback Change Feedback Configuration |                                | 9V Monitoring Enable 9V monitoring.                                                                                                                            | Options: Voltage not monitored Voltage monitored                                                                                              |
| Feedback Primary Feedback              | Type                           | Selects the type of feedback for encoder 1.                                                                                                                    | Default: Sin/Cos                                                                                                                              |
| Feedback Primary Feedback              | Type                           | Selects the type of feedback for encoder 1.                                                                                                                    | Options: Sin/Cos TTL (incremental)                                                                                                            |
| Feedback Primary Feedback              | Cycles                         | Defines counts (linear) or revolutions (rotary) for encoder 1.                                                                                                 | Default: 1024                                                                                                                                 |
| Feedback Primary Feedback              | Cycles                         | Defines counts (linear) or revolutions (rotary) for encoder 1.                                                                                                 | Range: 1…65,535 pulses/revolution or pulses/mm based on the [Primary Feedback Units] parameter                                                |
| Feedback Primary Feedback              | Units                          | Selects millimeters or revolutions for encoder 1. Default: Revolutions (per Rev)                                                                               |                                                                                                                                               |
| Feedback Primary Feedback              | Units                          | Selects millimeters or revolutions for encoder 1. Default: Revolutions (per Rev)                                                                               | Options: Revolutions (per Rev) Millimeters (per mm)                                                                                           |
| Feedback Primary Feedback              |                                | Feedback Polarity Defines the direction polarity for encoder 1. Default: Positive                                                                              |                                                                                                                                               |
| Feedback Primary Feedback              |                                | Feedback Polarity Defines the direction polarity for encoder 1. Default: Positive                                                                              | Options: Positive Negative                                                                                                                    |
| Feedback Secondary Feedback            | Cycles                         | Defines counts (linear) or revolutions (rotary) for encoder 2.                                                                                                 | Range: 1…65,535 pulses/revolution or pulses/mm based on the [Secondary Feedback Units] parameter                                              |
| Feedback Secondary Feedback            | Units                          | Selects millimeters or revolutions for encoder 2. Options: Revolutions (per Rev)                                                                               | Millimeters (per mm)                                                                                                                          |
| Feedback Secondary Feedback            |                                | Feedback Polarity Defines the direction polarity for encoder 2. Options: Positive                                                                              | Negative                                                                                                                                      |
| Feedback Dual Feedback                 |                                | Velocity Ratio Defines the ratio of the expected speed of encoder 2 divided by the expected speed of encoder 1. Not valid when Feedback Mode = Single Encoder. | Range: 0.0001…10,000.0 ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter              |
| Feedback Dual Feedback                 | Velocity Discrepancy Tolerance | Dual Feedback Speed Discrepancy Tolerance. Range: 0…6553.5 rpm or mm/s                                                                                         | ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                     |
| Feedback Dual Feedback                 | Position Discrepancy Tolerance | Acceptable difference in position between encoder 1 and encoder 2.                                                                                             | Range: 0…65,535 deg or mm ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter           |

## Safe Stop Mode

## Safe Stop and Safe Stop with Door Monitoring Modes

This chapter describes the Safe Stop modes of safety operation and provides a list of configuration parameters as well as wiring examples for each Safe Stop mode.

| Topic                                         |   Page |
|-----------------------------------------------|--------|
| Safe Stop Mode                                |     55 |
| Safe Stop Parameter List                      |     66 |
| Safe Stop Wiring Example                      |     68 |
| Safe Stop with Door Monitoring Mode           |     68 |
| Safe Stop with Door Monitoring Parameter List |     69 |
| Safe Stop with Door Monitoring Wiring Example |     69 |

When properly configured for Safe Stop, the drive monitors the Safe Stop input (SS\_In) and initiates the configured Stop Category upon deactivation of the input. The Stop Category is configurable as either Safe Torque Off with or without Standstill Checking, Safe Stop 1, or Safe Stop 2. The drive recognizes motion as stopped when encoder 1 feedback signals indicate the system has reached the configured Standstill Speed. Once Standstill Speed has been reached, the Door Control output (DC\_Out) is set to Unlock.

In addition to setting the Standstill Speed, you configure the Stop Delay [Maximum Stop Time], the period where deceleration occurs after a Safe Stop is initiated, and an optional Stop Monitoring Delay [Safe Stop Monitor Delay] that is a delay between the action that requests the Safe Stop and the initiation of the configured Stop Category. A [Safe Stop Monitor Delay] can be configured only for Safe Stop 1 or Safe Stop 2.

When properly configured for Safe Stop mode, the drive also monitors for faults and initiates the appropriate reaction. If the fault is a Safe State fault, the drive enters the Safe State. If the fault is a Stop Category fault, the drive initiates the configured Stop Category.

<!-- image -->

## Stop Categories

Use the [Stop Category] parameter to configure the type of stop that the system executes when a Safe Stop is initiated. A Safe Stop can be initiated by a transition of the SS\_In input from ON to OFF or by the occurrence of a Stop Category fault.

While the drive executes the configured Stop Category, it continues to monitor the system. If a Stop Category fault is detected, the drive sets the outputs to a faulted state, but allows for the door control logic to be set to Unlock if the feedback signals indicate Standstill Speed has been reached.

Safe torque-off, with or without standstill checking, opens the Guard Gate drive output (status = 0) when the Safe Stop is executed. This is commonly known as coast-to-stop.

## Safe Torque Off with Standstill Checking

This Stop Category lets you access the hazard area immediately after motion is detected as stopped rather than waiting until a specific time has elapsed.

When Safe Torque Off with Standstill Checking is initiated, motion power is removed immediately and the configured Stop Delay [Maximum Stop Time] begins. If the configured Standstill Speed is detected any time after the Safe Stop has been initiated and before the end of the configured Stop Delay, door control logic is set to Unlock.

If the Standstill Speed is not detected by the end of the configured Stop Delay, a Stop Speed fault occurs and the door control logic remains set to Lock until Standstill Speed is detected.

## IMPORTANT

After successful SS\_Reset, the Logix Designer application must issue an MSF instruction prior to restarting the machine.

Figure 12 - Timing Diagram for Safe Torque-off with Standstill Checking

<!-- image -->

(1) This signal is internal to the drive.

(2) DC\_Out output shown configured as Power to Release. See Door Control on page 64 for more information.

## Safe Stop 1 and 2

When Safe Stop 1 or 2 is initiated by a transition of the SS\_In input from ON to OFF, the drive does not initiate the configured Stop Delay [Maximum Stop Time] until after the optional Stop Monitoring Delay [Safe Stop Monitor Delay] expires, unless a Stop Category fault occurs during the Stop Monitoring Delay.

When Safe Stop 1 or 2 is initiated by a Stop Category fault, the Stop Delay [Maximum Stop Time] begins immediately, regardless of whether a Stop Monitoring Delay [Safe Stop Monitor Delay] is configured.

During a Safe Stop 1 and 2, the drive decelerates at a rate calculated by using the [Deceleration Reference Speed] and [Maximum Stop Time] parameters. When Safe Stop 1 or 2 is initiated, the drive decelerates at the calculated rate. Follow these calculations, depending on the conditions of your application.

Use these formulas if the actual speed of the drive is ≤ the Decel Reference Speed.

<!-- formula-not-decoded -->

## IMPORTANT

Deceleration Reference Speed must be the application's actual maximum motor speed. If the actual motor speed is greater than the Deceleration Reference Speed, then the Actual Stop Time equals the Maximum Stop Time.

Use this formula if the actual speed of the drive is ≥ the Decel Reference Speed.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## EXAMPLE

Deceleration monitoring takes place during the Stop Delay [Maximum Stop Time]. These three configurable parameters define the deceleration profile that is used:

- [Deceleration Reference Speed]
- [Deceleration Tolerance]
- Stop Delay, [Maximum Stop Time]

If Standstill Speed is detected any time after the Safe Stop has been initiated and before the Stop Delay [Maximum Stop Time] expires, door control logic is set to Unlock. If the Standstill Speed is not detected by the end of the configured Stop Delay [Maximum Stop Time], a Stop Speed fault occurs.

TIP

You can determine the drive/motor Stop Delay characteristics by using Motion Analyzer software, version 4.7 or later.

When Safe Stop 1 is executed, the Guard Gate drive output is on (status = 1) until standstill speed is reached or a fault occurs. This safe stop is commonly known as a controlled, monitor stop.

## IMPORTANT

Do not use Safe Stop 1 for vertical axis applications because the Guard Gate output is off (status = 0) when below standstill speed.

For Safe Stop 1, motion power is removed when Standstill Speed is reached.

## IMPORTANT

For Safe Stop 1, after a successful SS\_Reset, the Logix Designer application must issue an MSF instruction prior to restarting the machine.

Figure 13 - Timing Diagram for Safe Stop 1

<!-- image -->

(1) This signal is internal to the drive.

(2) DC\_Out output shown configured as Power to Release. See Door Control on page 64 for more information.

When Safe Stop 2 is executed, the Guard Gate drive output is on (status = 1) until after standstill speed is reached or a fault occurs. Use this safe stop for vertical load applications. The IGBT remains active, therefore follow the examples on page 57 to MAS before SS\_Reset.

For Safe Stop 2, motion power is not removed when Standstill Speed is reached.

## IMPORTANT

For Safe Stop 2, the Logix Designer application must monitor the state of the Axis.GuardStopRequestStatus tag. After the tag becomes active and stop monitoring expires, the program must issue an MAS instruction. Successful SS\_Reset is required prior to restarting the machine.

Figure 14 - Timing Diagram for Safe Stop 2

<!-- image -->

- (1) This signal is internal to the drive.
- (2) DC\_Out output shown configured as Power to Release. See Door Control on page 64 for more information.

## Safe Torque Off without Standstill Checking

When Safe Torque Off without Standstill Checking is initiated, motion power is removed immediately and the configured Stop Delay [Maximum Stop Time] begins. Door control logic is set to Unlock when the Stop Delay [Maximum Stop Time] expires, regardless of speed.

Figure 15 - Timing Diagram for Safe Torque Off without Standstill Checking

<!-- image -->

(1) This signal is internal to the drive.

(2) DC\_Out output shown configured as Power to Release. See Door Control on page 64 for more information.

TIP All Stop Types require an encoder to be connected.

## Standstill Speed and Position Tolerance

For Stop Categories that include Standstill Checking, you set the Standstill Speed and Standstill Position Tolerance.

| IMPORTANT   | The [Standstill Speed] and [Standstill Position Window] parameters are not used for Safe Torque Off without Standstill Checking configurations. Set these parameters to zero.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Standstill Speed is used to declare motion as stopped. The system is at standstill when the speed detected is less than or equal to the configured Standstill Speed. The [Standstill Speed] parameter defines the speed limit before the drive determines standstill has been reached and the door control logic is set to Unlock.

| IMPORTANT   | Standstill detection relies on the encoder 1 signal. The encoder 2 signal is used for fault diagnostics.   |
|-------------|------------------------------------------------------------------------------------------------------------|

The [Standstill Position Window] parameter defines the position limit in encoder 1 units that is tolerated after standstill has been reached. If the position changes by more than the amount specified by the Standstill Position Tolerance, after standstill has been reached and the door is unlocked, a Motion After Stopped fault occurs. This type of fault results in the drive entering the safe state.

The time required to verify that the Standstill Speed has been reached can be considerable when a very small Standstill Speed is configured and the encoder resolution of encoder 1 is very low.

- For rotary systems, the time (in seconds) exceeds 15 / [Standstill Speed (RPM) x Encoder 1 Resolution].
- For linear systems, the time (in seconds) exceeds 0.25 / [Standstill Speed (mm/s) x Encoder 1 Resolution].

## Deceleration Monitoring

Deceleration monitoring takes place during the configured Stop Delay [Maximum Stop Time], when the Stop Category is configured as Safe Stop 1 or Safe Stop 2. The deceleration start speed is captured at the beginning of the Stop Delay [Maximum Stop Time] and used to calculate the deceleration profile.

These parameters define the deceleration profile:

- Deceleration Reference Speed, [Deceleration Reference Speed]
- Deceleration Tolerance, [Deceleration Tolerance]
- Stop Delay, [Maximum Stop Time]

The Deceleration Reference Speed is relative to encoder 1. The [Deceleration Tolerance] parameter defines the percentage of the Deceleration Reference Speed that is tolerated above the calculated deceleration profile.

Figure 16 - Deceleration Monitoring

<!-- image -->

TIP

To account for system overshoot and drive delay, choose ∆v and set [Deceleration Reference Speed] to the highest normal operating speed to calculate the Deceleration Tolerance. Remember that [Deceleration Tolerance] parameter is a percentage.

When deceleration monitoring is being performed, the speed limit monitored during the Stop Delay [Maximum Stop Time] must be less than the Deceleration Monitoring Value or a Deceleration fault occurs. A Deceleration fault places outputs in the faulted state, but allows the door to be unlocked when the feedback signals indicate Standstill Speed has been reached.

## Safe Stop Reset

The Safe Stop Reset (SS Reset) is a reset from the Safe State or from a stopping condition to actively monitoring motion. The reset is successful if the SS\_In input is ON and no faults are present.

<!-- image -->

ATTENTION: For all types of reset (automatic, manual, or manual monitored), if a reset of the Safe Stop or Safe Limited Speed functions can result in machine operation, the other speed monitoring functions must be configured to detect and prevent dangerous motion.

<!-- image -->

ATTENTION: The Safe Stop Reset does not provide safety-related restart according to EN 60204-1. Restart must be performed by external measures if automatic restart could result in a hazardous situation. You are responsible for determining whether automatic restart could pose a hazard.

When an SS Reset is requested, all diagnostic tests that can be performed prior to outputs being energized are performed prior to a successful SS Reset. If a diagnostic test can be performed only when outputs are energized, the test is performed immediately following the SS Reset.

## IMPORTANT

An SS Reset is not attempted if the GuardStopInputCycleRequiredStatus attribute is set (1), indicating that an error, other than an invalid configuration fault or ESM\_In input fault, occurred. The GuardStopInputCycleRequiredStatus attribute is bit 25 of the [Guard Status] parameter.

## Automatic

If the SS Reset is configured as automatic, the drive always attempts a reset if it is in the Safe State or has initiated a Stop Category. The reset is attempted when the SS\_In input transitions from OFF to ON or if SS\_In is ON at powerup.

## Manual

If the SS Reset is configured as manual, the reset is attempted when the SS\_In input is ON and the Reset\_In input is ON.

## Manual Monitored

A manual monitored reset requires an OFF to ON to OFF transition of the Reset\_In input.

<!-- image -->

If at any time before the closing and opening of the Reset\_In input, the SS\_In input transitions from ON to OFF, the reset is aborted.

## Faults

If a fault occurs, other than an Invalid Configuration fault or an ESM Monitoring fault, the SS\_In input must turn OFF and ON again to reset the GuardStopInputCycleRequiredStatus bit before a successful SS Reset can occur.

## Door Control

The status of door control logic (Lock or Unlock) and the Door Monitor Input (DM\_In), along with the drive's location in the system [System Configuration] and Door Control Output Type [Door Control Output] determine whether the Door Control output (DC\_Out) is locked or unlocked during normal operation.

When the DC\_Out output has no faults, the drive is configured for Safe Stop, and the drive is monitoring motion, the door control logic state is Locked. It remains locked while a Safe Stop is being executed. For all Stop Categories except Safe Torque Off without Standstill Checking, door control logic is set to Unlock only when Standstill Speed has been reached. If the Stop Category is Safe Torque Off without Standstill Checking, door control logic is set to Unlock when the Stop Delay [Maximum Stop Time] has elapsed, regardless of speed.

## Configuration

You configure the type of door control for each Safe Speed Monitor Option module in the system.

| [Door Control Output] Settings   | [Door Control Output] Settings               | DC_Out Status and Lock State                                            |
|----------------------------------|----------------------------------------------|-------------------------------------------------------------------------|
|                                  | Single and Last Units First and Middle Units |                                                                         |
|                                  |                                              | Power to Release Not valid ON = Door is unlocked. OFF = Door is locked. |
|                                  |                                              | Power to Lock Not valid ON = Door is locked. OFF = Door is unlocked.    |
| Cascading (2 Ch Sourcing)        | Cascading (2 Ch Sourcing)                    | ON = Door is unlocked. OFF = Door is locked.                            |

A single or last drive in a cascaded system can be configured for any Door Output Type setting. For example, choose 2 Ch Sourcing to connect to a safety programmable controller input. The first or middle drive in a cascaded system must be configured as 2 Ch Sourcing.

<!-- image -->

ATTENTION: When the DC\_Out output is configured as Power to Lock, the safe state and faulted state is Unlocked. Make sure that this possibility does not create a hazard.

## Effect of Faults

These fault conditions affect the integrity of the DC\_Out output and force the DC\_Out output to its safe state (OFF) regardless of the status of door control logic:

- DC Out fault
- Invalid Configuration fault
- Internal Power Supply or MPU faults

<!-- image -->

ATTENTION: If a fault occurs after Standstill Speed has been reached, door control remains unlocked.

For fault conditions where the DC\_Out output can maintain its integrity, both door control logic and the DC\_Out output hold last state. If hold last state cannot be maintained, faults can turn the DC\_Out output OFF.

<!-- image -->

ATTENTION: If a fault occurs while the door is unlocked, it can remain unlocked. Make sure that this possibility does not create a hazard.

## Safe Stop Parameter List

Table 20 - Safe Stop Parameters

| Tab                                | Parameter Name Description                                                                  | Values (Safety Configuration Tool)   | Values (Safety Configuration Tool)                                                                                                                                               |
|------------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Change System Configuration | Operation Mode Defines the primary operating mode of the speed monitoring safety functions. |                                      | Setting: SafeStop                                                                                                                                                                |
| Input Change Input                 | Safe Stop Configuration for Safe Stop input (SS_In).                                        |                                      | Default: Dual Channel Equivalent                                                                                                                                                 |
| Configuration Type                 |                                                                                             |                                      | Options: Not Used Dual Channel Equivalent Dual Channel Equivalent 3 s Dual Channel Complementary Dual Channel Complementary 3 s Solid State Device Equivalent 3 s Single Channel |

## Lock Monitoring

If Lock Monitoring is enabled, the Lock Monitoring input (LM\_In) must be in the ON state any time the Door Control output (DC\_Out) is in the Lock state, except for the 5 seconds following the DC\_Out output's transition from the Unlocked state to the Locked state. If the LM\_In input is not ON during this time, a Lock Monitoring fault occurs. The LM\_In input must be OFF when the DM\_In input transitions from ON to OFF (the door opens).

A Lock Monitoring fault is a Stop Category fault that initiates the configured Stop Category.

To configure the drive for Safe Stop mode, set these parameters in addition to the General and Feedback parameters listed on page 48 and page 54 .

TIP

Not all Safe Stop configuration parameters require configuring for each Safe Stop category.

Table 20 - Safe Stop Parameters (continued)

| Tab                                      | Parameter Name Description   |                                                                                                                                                                                                                                                                                                                                                        | Values (Safety Configuration Tool)                                                                                                                                               |
|------------------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safe Stop Change Safe Stop Configuration |                              | Stop Category Safe operating stop type selection. This defines the type of Safe Stop that is performed if the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                | Default: Safe Torque-Off                                                                                                                                                         |
| Safe Stop Change Safe Stop Configuration |                              | Stop Category Safe operating stop type selection. This defines the type of Safe Stop that is performed if the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                | Options: Safe Torque-Off Safe Stop 1 Safe Stop 2                                                                                                                                 |
| Safe Stop Change Safe Stop Configuration |                              | Enable Standstill Checking. Automatically enabled for Safe Stop 1 and Safe Stop 2.                                                                                                                                                                                                                                                                     | Default: Standstill Checking Enabled                                                                                                                                             |
| Safe Stop Change Safe Stop Configuration |                              | Enable Standstill Checking. Automatically enabled for Safe Stop 1 and Safe Stop 2.                                                                                                                                                                                                                                                                     | Options: Standstill Checking Enabled Standstill Checking Not Enabled                                                                                                             |
| Safe Stop Change Safe Stop Configuration | Safe Stop Monitor Delay      | Defines the monitoring delay between the request and the Maximum Stop Time when the request for a Safe Stop 1 or a Safe Stop 2 is initiated by an SS_In input ON to OFF transition. If the Stop Category is Safe Torque-Off with or without Standstill Speed Checking, the Safe Stop Monitor Delay must be 0 or an Invalid Configuration fault occurs. | Default: 0                                                                                                                                                                       |
| Safe Stop Change Safe Stop Configuration | Safe Stop Monitor Delay      | Defines the monitoring delay between the request and the Maximum Stop Time when the request for a Safe Stop 1 or a Safe Stop 2 is initiated by an SS_In input ON to OFF transition. If the Stop Category is Safe Torque-Off with or without Standstill Speed Checking, the Safe Stop Monitor Delay must be 0 or an Invalid Configuration fault occurs. | Range: 0…6553.5 s                                                                                                                                                                |
| Safe Stop Change Safe Stop Configuration | Deceleration Reference Speed | Determines deceleration rate to monitor for Safe Stop 1 or Safe Stop 2.                                                                                                                                                                                                                                                                                | Default: 0                                                                                                                                                                       |
| Safe Stop Change Safe Stop Configuration | Deceleration Reference Speed | Determines deceleration rate to monitor for Safe Stop 1 or Safe Stop 2.                                                                                                                                                                                                                                                                                | Range: 0…65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                            |
| Safe Stop Change Safe Stop Configuration |                              | Maximum Stop Time Defines the maximum stop delay time that is used when the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                                                  | Default: 0                                                                                                                                                                       |
| Safe Stop Change Safe Stop Configuration |                              | Maximum Stop Time Defines the maximum stop delay time that is used when the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                                                  | Range: 0…6553.5 s                                                                                                                                                                |
| Safe Stop Change Safe Stop Configuration | Deceleration Tolerance       | This is the acceptable tolerance above the deceleration rate set by the [Deceleration Reference Speed] parameter.                                                                                                                                                                                                                                      | Default: 0                                                                                                                                                                       |
| Safe Stop Change Safe Stop Configuration | Deceleration Tolerance       | This is the acceptable tolerance above the deceleration rate set by the [Deceleration Reference Speed] parameter.                                                                                                                                                                                                                                      | Range: 0…100% of Deceleration Reference Speed                                                                                                                                    |
| Safe Stop Change Safe Stop Configuration |                              | Standstill Speed Defines the speed limit that is used to declare motion as stopped. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                                                                         | Default: 0.001                                                                                                                                                                   |
| Safe Stop Change Safe Stop Configuration |                              | Standstill Speed Defines the speed limit that is used to declare motion as stopped. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                                                                         | Range: 0.001…65.535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                        |
| Safe Stop Change Safe Stop Configuration | Standstill Position Window   | Defines the position limit window in encoder 1 degrees or mm that are tolerated after a safe stop condition has been detected. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                              | Default: 10                                                                                                                                                                      |
| Safe Stop Change Safe Stop Configuration | Standstill Position Window   | Defines the position limit window in encoder 1 degrees or mm that are tolerated after a safe stop condition has been detected. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                              | Range: 0…65,535 degrees (360° = 1 revolution) or mm ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                    |
| Safety Change System Configuration       |                              | Door Control Output Defines the lock and unlock state for door control output (DC_Out). Any Door Control Output option can be used for a single-axis system or for the last unit in a multi-axis system. The first and middle units of a multi-axis system must be configured as 2 Channel Sourcing.                                                   | Default: Power to Release                                                                                                                                                        |
| Safety Change System Configuration       |                              | Door Control Output Defines the lock and unlock state for door control output (DC_Out). Any Door Control Output option can be used for a single-axis system or for the last unit in a multi-axis system. The first and middle units of a multi-axis system must be configured as 2 Channel Sourcing.                                                   | Options: Power to Release Power to Lock 2 Channel Sourcing                                                                                                                       |
| Safety Change System Configuration       | Enable Lock Monitoring       | Lock Monitoring can be enabled only when the drive is a single unit or the first unit in a multi-axis system as set in [System Configuration].                                                                                                                                                                                                         | Default: Lock Monitoring Not Enabled                                                                                                                                             |
| Safety Change System Configuration       | Enable Lock Monitoring       | Lock Monitoring can be enabled only when the drive is a single unit or the first unit in a multi-axis system as set in [System Configuration].                                                                                                                                                                                                         | Options: Lock Monitoring Not Enabled Lock Monitoring Enabled                                                                                                                     |
| Input Change Input Configuration Type    |                              | Lock Monitor Configuration for the Lock Monitor input (LM_In). Default: Not Used                                                                                                                                                                                                                                                                       |                                                                                                                                                                                  |
| Input Change Input Configuration Type    |                              | Lock Monitor Configuration for the Lock Monitor input (LM_In). Default: Not Used                                                                                                                                                                                                                                                                       | Options: Not Used Dual Channel Equivalent Dual Channel Equivalent 3 s Dual Channel Complementary Dual Channel Complementary 3 s Solid State Device Equivalent 3 s Single Channel |

## Safe Stop Wiring Example

## Safe Stop with Door Monitoring Mode

This example illustrates safe stop wiring.

Figure 17 - Master, Safe Stop (First or Single Unit)

<!-- image -->

When properly configured for Safe Stop with Door Monitoring, the drive monitors the Safe Stop input (SS\_In) and initiates the configured Stop Category upon deactivation of the input as described in Safe Stop Mode on page 55 .

In addition, the drive verifies through monitoring the Door Monitor input (DM\_In) that the door interlock solenoid controlled by the Door Control output (DC\_Out) is in an expected state. The DM\_In input is ON when the door is closed and OFF when the door is open. If the door is monitored as opened during Safe Stop monitoring, a Door Monitoring fault occurs and the drive initiates the configured Stop Category.

You can monitor the door's status with or without using the Door Control (lock/ unlock) function. When door control logic is set to Lock, the drive puts the solenoid into the locked state when the machine is not at a safe speed or at Standstill Speed.

## Lock Monitoring

If an Operaton mode that includes Door Monitoring is selected and Lock Monitoring is enabled, the Lock Monitor input (LM\_In) signal must be OFF any time that the Door Monitor input (DM\_In) transitions from ON to OFF.

## IMPORTANT

If your application uses Lock Monitoring without Door Monitoring, you must use some means to make sure that the Lock Monitor is not stuck at Lock indication.

## Safe Stop with Door Monitoring Parameter List

## SS Reset

If the Door Monitor input (DM\_In) is OFF when a Safe Stop (SS) Reset is attempted in any state other than actively monitoring Safe Limited Speed, a Door Monitoring fault occurs and the drive initiates the configured Stop Category.

To configure the drive for Safe Stop with Door Monitoring, set the DM Input parameter in addition to the Safe Stop parameters listed on page 66 .

Table 21 - Safe Stop with Door Monitoring Parameters

|                                       | Tab Parameter Name Description                                                              | Values (Safety Configuration Tool)   | Values (Safety Configuration Tool)            |
|---------------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------|-----------------------------------------------|
| Safety Change System Configuration    | Operation Mode Defines the primary operating mode of the speed monitoring safety functions. |                                      | Setting: SafeStop-Door Monitor                |
| Input Change Input Configuration Type | Door Monitor Configuration for the Door Monitor input (DM_In). Default: Not Used            |                                      | (1) Options: Not Used Dual Channel Equivalent |

## Safe Stop with Door Monitoring Wiring Example

This example illustrates wiring for safe stop with door monitoring.

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              29 | SLS_OUT_CH0     |              29 |
|              30 | SLS_OUT_CH1     |              30 |
|              31 | DM_IN_CH0       |              31 |
|              32 | DM_IN_CH1       |              32 |
|              33 | LM_IN_CH0 (1)   |              33 |
|              34 | LM_IN_CH1       |              34 |
|              35 | DC_OUT_CH0      |              35 |
|              36 | DC_OUT_CH1      |              36 |
|              37 | ESM_IN_CH0      |              37 |
|              38 | ESM_IN_CH1      |              38 |

Figure 18 - Master, Safe Stop with Door Monitoring (First or Single Unit)

<!-- image -->

## Notes:

## Safe Limited Speed (SLS) Mode

## Safe Limited Speed (SLS) Modes

This chapter describes the Safe Limited Speed (SLS) modes of safety operation and provides a list of configuration parameters along with wiring examples for each mode.

| Topic                                                                       |   Page |
|-----------------------------------------------------------------------------|--------|
| Safe Limited Speed (SLS) Mode                                               |     71 |
| Safe Limited Speed Parameter List                                           |     74 |
| Safe Limited Speed Wiring Example                                           |     75 |
| Safe Limited Speed with Door Monitoring Mode                                |     75 |
| SLS with Door Monitoring Parameter List                                     |     77 |
| SLS with Door Monitoring Wiring Example                                     |     77 |
| Safe Limited Speed with Enabling Switch Monitoring Mode                     |     78 |
| SLS with Enabling Switch Monitoring Parameter List                          |     79 |
| SLS with Enabling Switch Monitoring Wiring Example                          |     79 |
| Safe Limited Speed with Door Monitoring and Enabling Switch Monitoring Mode |     80 |
| SLS with Door Monitoring and Enabling Switch Monitoring Parameter List      |     82 |
| SLS with Door Monitoring and Enabling Switch Monitoring Wiring Example      |     83 |
| Safe Limited Speed Status Only Mode                                         |     84 |
| SLS Status Only Parameter List                                              |     85 |
| SLS Status Only Wiring Examples                                             |     86 |

When properly configured for Safe Limited Speed, the drive performs Safe Limited Speed (SLS) monitoring functions in addition to the Safe Stop function described in Safe Stop Mode on page 55. When the Safe Limited Speed input (SLS\_In) is OFF, feedback velocity is monitored and compared against a configurable Safe Speed Limit.

<!-- image -->

If the feedback velocity is below the Safe Speed Limit during Safe Limited Speed monitoring, the Door Control output (DC\_Out) is unlocked after the [Safe Limited Speed Monitor Delay], if configured, has expired.

<!-- image -->

ATTENTION: Make sure that an unlocked door does not result in a hazardous situation.

If a Stop Category is initiated or a fault occurs while the drive is actively monitoring Safe Limited Speed, door control remains unlocked. The safe state of the SLS\_In input can result in the door being unlocked.

If the measured velocity exceeds the Safe Speed Limit, an SLS fault occurs and the configured [Stop Category] is initiated. An optional [Safe Limited Speed Monitor Delay] can be configured to delay the start of Safe Limited Speed monitoring.

Safe Limited Speed monitoring is requested by a transition of the Safe Limited Speed input (SLS\_In) from ON to OFF. When the SLS\_In input is ON, the drive does not monitor for Safe Limited Speed and the measured velocity can be above or below the Safe Speed Limit.

<!-- image -->

If the Reset Type is configured as Automatic, Safe Limited Speed monitoring is disabled when the SLS\_In input is turned ON and the machine operates at its normal run speed. Make sure that the SLS\_In input cannot transition to ON while someone is in the hazardous area.

If you configure a [Safe Limited Speed Monitor Delay], the delay begins when Safe Limited Speed monitoring is requested by the SLS\_In transition from ON to OFF. The drive begins monitoring for Safe Limited Speed when the delay times out. If system speed is greater than or equal to the configured Safe Speed Limit during Safe Limited Speed monitoring, an SLS fault occurs and the drive initiates the configured Stop Category.

Figure 19 - Timing Diagram for Safe Limited Speed (SLS)

<!-- image -->

## Safe Limited Speed Reset

A Safe Limited Speed (SLS) Reset is a transition out of actively monitoring safe limited speed. It can also occur during a [Safe Limited Speed Monitor Delay], if one is configured. When an SLS Reset occurs, the drive no longer monitors for safe limited speed and the door is locked. Speed is no longer restricted to the configured Safe Speed Limit.

The SLS Reset function monitors the SLS\_In input. If an SLS Reset is requested, the drive checks that no faults are present and verifies that the SLS\_In input is ON (closed circuit) before the reset is performed.

When the input is OFF, Safe Limited Speed monitoring takes place, after the [Safe Limited Speed Monitor Delay], if one is configured. An SLS Reset can be requested during active Safe Limited Speed monitoring or during a Safe Limited Speed Monitoring Delay. If a reset is requested during a Safe Limited Speed Monitoring Delay, the reset does not wait for the delay to time out.

## Automatic

Once the SLS\_In input is ON (closed), the drive lets the drive resume normal operating speed. No reset button is required to re-enter the normal run state.

## Manual

When the SLS\_In input transitions from OFF to ON and the Reset\_In input is ON, an SLS\_Reset is attempted.

If the SLS\_In transitions from OFF to ON and the Reset\_In input is OFF, the drive stays in its current state, whether it is actively monitoring Safe Limited Speed or is in a Safe Limited Speed Monitoring Delay, and waits for the Reset\_In input to transition to ON, before attempting the SLS\_Reset. If at any time, the SLS\_In input transitions back to OFF, the SLS\_Reset is aborted.

## Manual Monitored

When the SLS\_In input transitions from OFF to ON, the drive waits for an OFF to ON to OFF transition of the Reset\_In input before an SLS\_Reset is attempted. If at any time during this period, the SLS\_In input transitions back to OFF, the SLS\_Reset is aborted.

## Safe Limited Speed Parameter List

To configure the drive for Safe Limited Speed monitoring, set these parameters in addition to the Safe Stop parameters listed beginning on page 66 .

Table 22 - Safe Limited Speed Parameters

| Tab                                                        | Parameter Name Description                                                                                                                                                | Values (Safety Configuration Tool)                                                                                                    |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Safety Change System Configuration                         | Operation Mode Defines the primary operating mode of the speed monitoring safety functions.                                                                               | Setting: SafeStop-Safe Limited Speed                                                                                                  |
| Input Change Input Configuration Type                      | Safe Limited Speed Configuration for the Safe Limited Speed input (SLS_In).                                                                                               | Default: Not Used (1) Options: Not Used Dual Channel Equivalent                                                                       |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Defines the Safe Limited Speed Monitoring Delay between the SLS_In ON to OFF transition and the initiation of the Safe Limited Speed (SLS) monitoring. | Default: 0                                                                                                                            |
| Safe Limited Speed Change Safe Limited Speed Configuration | Monitor Delay                                                                                                                                                             | Range: 0…6553.5 s                                                                                                                     |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Speed Limit Defines the speed limit that is monitored in Safe Limited Speed (SLS) mode.                                                                              | Default: 0 (1)                                                                                                                        |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Speed Limit Defines the speed limit that is monitored in Safe Limited Speed (SLS) mode.                                                                              | Range: 0…65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter |

## Safe Limited Speed Wiring Example

This example illustrates wiring for safe limited speed.

Figure 20 - Master, Safe Limited Speed (First or Single Unit)

<!-- image -->

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              29 | SLS_OUT_CH0     |              29 |
|              30 | SLS_OUT_CH1     |              30 |
|              31 | DM_IN_CH0       |              31 |
|              32 | DM_IN_CH1       |              32 |
|              33 | LM_IN_CH0       |              33 |
|              34 | LM_IN_CH1       |              34 |
|              35 | DC_OUT_CH0      |              35 |
|              36 | DC_OUT_CH1      |              36 |
|              37 | ESM_IN_CH0      |              37 |
|              38 | ESM_IN_CH1      |              38 |

When properly configured for Safe Limited Speed with Door Monitoring, the drive performs Safe Limited Speed (SLS) monitoring functions as described in Safe Limited Speed (SLS) Mode on page 71 in addition to the Safe Stop functions as described in Safe Stop Mode on page 55 .

In addition, the drive verifies through monitoring the Door Monitor input (DM\_In) that the drive controlled by the Door Control output (DC\_Out) is in the expected state. If the door is monitored as opened when it should be closed, the drive initiates the configured Stop Category.

The Door Monitor input (DM\_In) is ON when the door is closed and OFF when the door is open. The DM\_In input must be ON (door closed) whenever Safe Limited Speed monitoring is inactive (SLS\_In is ON, meaning the circuit is closed). The DM\_In input must also be ON (door closed) during a Safe Limited Speed Monitor Delay. A Door Monitor fault is a Stop Category fault that initiates the configured Stop Category.

## Safe Limited Speed with Door Monitoring Mode

If Safe Limited Speed Monitoring is active (SLS\_In input is OFF) and the drive has verified a safe speed condition, the door can be unlocked and opened.

<!-- image -->

ATTENTION: Make sure that an open door does not result in a hazardous situation.

If a Stop Category is initiated or a fault occurs while the drive is actively monitoring Safe Limited Speed, door control remains unlocked. The safe state of the SLS\_In input can result in the door being unlocked.

You can monitor the door's status with or without the door control (lock/ unlock) function. When door control logic is set to lock, it prevents personnel from entering the hazardous area when the machine is not at a safe speed or at Standstill Speed.

## Safe Limited Speed Reset

When properly configured for Safe Limited Speed with Door Monitoring, the drive must be monitoring motion (SLS\_In input is OFF) if the door is open (DM\_In is OFF). Make sure the door is closed before requesting an SLS Reset.

A Safe Limited Speed Reset results in a Door Monitoring fault if the door is open (DM\_In is OFF) when the reset is requested by a transition of the SLS\_In input from OFF to ON. A Door Monitor fault is a Stop Category fault that initiates the configured Stop Category.

## SLS with Door Monitoring Parameter List

To configure the drive for Safe Limited Speed with Door Monitoring, set the DM Input parameter in addition to the Safe Stop parameters listed on page 66 and the Safe Limited Speed parameters listed on page 74 .

Table 23 - SLS with Door Monitoring Parameters

| Tab                                | Parameter Name Description                                                                  | Values (Safety Configuration Tool)   | Values (Safety Configuration Tool)                                                                                                                                               |
|------------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Change System Configuration | Operation Mode Defines the primary operating mode of the speed monitoring safety functions. |                                      | Setting: SafeStop-Safe Limited Speed with Door Monitoring                                                                                                                        |
| Input Change Input                 | Door Monitor Configuration for the Door Monitor input (DM_In). Default: Not Used            |                                      | (1)                                                                                                                                                                              |
| Configuration Type                 |                                                                                             |                                      | Options: Not Used Dual Channel Equivalent Dual Channel Equivalent 3 s Dual Channel Complementary Dual Channel Complementary 3 s Solid State Device Equivalent 3 s Single Channel |

## SLS with Door Monitoring Wiring Example

This example illustrates wiring for SLS with door monitoring.

Figure 21 - Master, Safe Limited Speed with Door Monitoring (First or Single Unit)

<!-- image -->

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              29 | SLS_OUT_CH0     |              29 |
|              30 | SLS_OUT_CH1     |              30 |
|              31 | DM_IN_CH0       |              31 |
|              32 | DM_IN_CH1       |              32 |
|              33 | LM_IN_CH0 (1)   |              33 |
|              34 | LM_IN_CH1       |              34 |
|              35 | DC_OUT_CH0      |              35 |
|              36 | DC_OUT_CH1      |              36 |
|              37 | ESM_IN_CH0      |              37 |
|              38 | ESM_IN_CH1      |              38 |

## Safe Limited Speed with Enabling Switch Monitoring Mode

When properly configured for Safe Limited Speed with Enabling Switch Monitoring, the drive performs Safe Limited Speed (SLS) monitoring functions as described in Safe Limited Speed (SLS) Mode on page 71 in addition to the Safe Stop functions as described in Safe Stop Mode on page 55 .

In addition, the drive monitors the Enabling Switch Monitor input (ESM\_In) after the Safe Limited Speed Monitoring Delay times out. Once the enabling switch is activated, the ESM\_In input must remain ON while Safe Limited Speed monitoring is active or an ESM Monitoring fault occurs. An ESM Monitoring fault is a Stop Category fault that initiates the configured Stop Category.

## IMPORTANT

When Safe Limited Speed Monitoring is inactive, the ESM\_In input is not monitored.

## Safe Stop Reset (SS Reset) and Safe Limited Speed Reset (SLS Reset)

If an ESM Monitoring Fault occurs due to the ESM\_In input turning OFF (enabling switch is released), the drive can be reset without cycling the SS\_In input. To perform an SLS Reset, first return the ESM\_In input to ON (grip the enabling switch in the middle position). Then, press and release the reset button. In this case, only the SS\_In input does not need to be cycled to reset the drive following a fault.

While Safe Limited Speed is being monitored after the [Safe Limited Speed Monitor Delay] times out, if the SLS\_In input is ON and an SLS Reset occurs, the ESM\_In is not monitored.

<!-- image -->

ATTENTION: Make sure that the SLS\_In input cannot transition to ON while someone is in the hazard area.

Use appropriate procedures when selecting safe limited speed to prevent other users from changing the mode while personnel are in the machine area.

If you attempt an SS Reset when the SLS\_In input is OFF and the ESM\_In input is OFF, an ESM Monitoring fault occurs. An ESM Monitoring fault is a Stop Category fault that initiates the configured Stop Category.

## SLS with Enabling Switch Monitoring Parameter List

To configure the drive for Safe Limited Speed with Enabling Switch Monitoring, set the [Enabling Switch Monitor] parameter in addition to the Safe Stop parameters listed on page 66 and the Safe Limited Speed parameters listed on page 74 .

Table 24 - SLS with Enabling Switch Monitoring Parameters

| Tab                                   | Parameter Name Description   |                                                                                             | Values (Safety Configuration Tool)   | Values (Safety Configuration Tool)                                |
|---------------------------------------|------------------------------|---------------------------------------------------------------------------------------------|--------------------------------------|-------------------------------------------------------------------|
| Safety Change System Configuration    |                              | Operation Mode Defines the primary operating mode of the speed monitoring safety functions. |                                      | Setting: SafeStop-Safe Limited Speed with Enabling Switch Control |
| Input Change Input Configuration Type | Enabling Switch Monitor      | Configuration for the Enabling Switch input (ESM_In). Default: Not Used                     |                                      | (1) Options: Not Used Dual Channel Equivalent                     |

## SLS with Enabling Switch Monitoring Wiring Example

This example illustrates wiring for SLS with enabling switch monitoring.

Figure 22 - Master, Safe Limited Speed with Enabling Switch Monitoring (First or Single Unit)

<!-- image -->

440J-N21TNPM Enabling Switch

(1) Lock monitoring connections are not required for Safe Limited Speed with Enabling Switch Monitoring mode operation.

## Safe Limited Speed with Door Monitoring and Enabling Switch Monitoring Mode

When properly configured for Safe Limited Speed with Door Monitoring and Enabling Switch Monitoring, the drive performs Safe Limited Speed (SLS) monitoring functions as described on page 71, in addition to the Safe Stop functions as described in Safe Stop Mode on page 55 .

The drive also monitors both the Enabling Switch Monitor input (ESM\_In) and the Door Monitor input (DM\_In). This mode lets you access the hazardous area when the machine is under a Safe Limited Speed condition. The following is a typical procedure for accessing the hazardous area by using this mode.

1. Set the SLS\_In input to OFF.

The Safe Speed Limit must not be exceeded after the [Safe Limited Speed Monitor Delay], if configured, times out.

2. After the Safe Limited Speed Monitoring Delay has timed out, hold the enabling switch in the middle position

Once a safe speed is detected and the enabling switch is in the middle position, the drive unlocks the door.

3. Continue to hold the enabling switch while you open the door, enter the hazard area, and perform the required maintenance.

Follow these steps to remove the safe speed condition and resume normal run operation.

1. Leave the hazard area while holding the enabling switch.
2. Hold the enabling switch until the door is closed and you have disabled the SLS\_In input by setting it to the ON or closed position.
3. Press the reset button, if manual reset is configured.
4. Release the enabling switch.

The machine resumes normal run operation.

<!-- image -->

ATTENTION: Make sure that the SLS\_In input cannot transition to ON while someone is in the hazard area.

Use appropriate procedures when selecting safe limited speed to prevent other users from changing the mode while personnel are in the machine area.

## Behavior During SLS Monitoring

When Safe Limited Speed monitoring is active, door control logic is set to Unlock if the ESM\_In input is ON and the speed is detected at below the Safe Speed Limit.

If the ESM\_In input is ON, the door can be opened (DM\_In transitions from ON to OFF). However, if the ESM\_In input transitions to OFF after the door has been opened, an ESM Monitoring fault occurs. An ESM Monitoring fault is a Stop Category fault that initiates the configured [Stop Category].

If the DM\_In input transitions from ON to OFF (door is opened), while the ESM\_In input is OFF, a Door Monitoring fault occurs. A Door Monitoring fault is a Stop Category fault that initiates the configured [Stop Category].

<!-- image -->

ATTENTION: While Safe Limited Speed Monitoring is active, the ESM\_In input is not monitored until the DM\_In input is detected as OFF.

Make sure that the ESM\_In input is not relied upon for safety until the DM\_In input has transitioned to OFF.

After the DM\_In input turns OFF, it could turn back ON again if the door is closed behind the operator but the ESM\_In input is still monitored.

## Behavior While SLS Monitoring is Inactive

If Safe Limited Speed monitoring is inactive, the DM\_In input must be ON (door closed) or a Door Monitoring fault occurs and the drive initiates the configured [Stop Category]. The ESM\_In input can be ON or OFF.

## Behavior During SLS Monitoring Delay

The status of the ESM\_In input does not affect the operation of the system during a [Safe Limited Speed Monitor Delay]. However, the DM\_In input must be ON (door closed) during the delay or a Door Monitoring fault occurs and the drive initiates the configured [Stop Category].

## SLS with Door Monitoring and Enabling Switch Monitoring Parameter List

## Safe Stop Reset (SS Reset) and Safe Limited Speed Reset (SLS Reset)

The door must be closed when an SS Reset or SLS Reset is requested. An SS Reset results in a Door Monitoring fault if the door is open when the reset is requested by a transition of the SS\_In input from OFF to ON. An SLS Reset also results in a Door Monitoring fault if the door is open when the reset is requested by a transition of the SLS\_In input from OFF to ON. A Door Monitor fault is a Stop Category fault that initiates the configured [Stop Category].

If an SS Reset is attempted while the SLS\_In input is OFF, an ESM Monitoring fault occurs. An ESM Monitoring fault is a Stop Category fault that initiates the configured [Stop Category].

To configure the drive for Safe Limited Speed with Door Monitoring and Enabling Switch Monitoring, set the [Door Monitor] and [Enable Switch Monitor] parameters in addition to the Safe Stop parameters listed on page 66 and the Safe Limited Speed parameters listed on page 74 .

Table 25 - SLS with Door Monitoring and Enabling Switch Monitoring Parameters

| Tab                                   | Parameter Name Description   |                                                                                             | Values (Safety Configuration Tool)                                                                                                                                               |
|---------------------------------------|------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Change System Configuration    |                              | Operation Mode Defines the primary operating mode of the speed monitoring safety functions. | Setting: SafeStop-Safe Limited Speed with Door Monitor and Enabling Switch                                                                                                       |
| Input Change Input Configuration Type |                              | Door Monitor Configuration for the Door Monitor input (DM_In). Default: Not Used            | (1)                                                                                                                                                                              |
| Input Change Input Configuration Type |                              | Door Monitor Configuration for the Door Monitor input (DM_In). Default: Not Used            | Options: Not Used Dual Channel Equivalent Dual Channel Equivalent 3 s Dual Channel Complementary Dual Channel Complementary 3 s Solid State Device Equivalent 3 s Single Channel |
| Input Change Input Configuration Type | Enabling Switch Monitor      | Configuration for the Enabling Switch input (ESM_In). Default: Not Used                     | (1)                                                                                                                                                                              |
| Input Change Input Configuration Type | Enabling Switch Monitor      | Configuration for the Enabling Switch input (ESM_In). Default: Not Used                     | Options: Not Used Dual Channel Equivalent Dual Channel Equivalent 3 s Dual Channel Complementary Dual Channel Complementary 3 s Solid State Device Equivalent 3 s Single Channel |

## SLS with Door Monitoring and Enabling Switch Monitoring Wiring Example

This example illustrates wiring for SLS with door monitoring and enabling switch monitoring.

Figure 23 - Master, Safe Limited Speed with Door Monitoring and Enabling Switch Monitoring (First or Single Unit)

<!-- image -->

## Safe Limited Speed Status Only Mode

When properly configured for Safe Limited Speed Status Only, the drive provides Safe Limited Speed status information in addition to the Safe Stop functions as described in Safe Stop Mode on page 55 .

When the Safe Limited Speed input (SLS\_In) is OFF, the feedback velocity is monitored and compared against a configurable Safe Speed Limit. If the measured velocity exceeds the limit, no stopping action takes place. Instead, the system status is made available as a safe output intended for a safety programmable logic controller (PLC).

You can program an optional [Safe Limited Speed Monitor Delay] to delay the start of Safe Limited Speed monitoring.

TIP

In Safe Limited Speed Status Only mode, Door Monitoring and Enabling Switch Monitoring are not available.

<!-- image -->

ATTENTION: When the drive is properly configured for Safe Limited Speed Status Only mode, it does not automatically initiate a Safe Stop in the event of an overspeed condition.

Safe Limited Speed monitoring is requested by a transition of the SLS\_In input from ON to OFF. If you configure a [Safe Limited Speed Monitor Delay], the delay begins when Safe Limited Speed monitoring is requested by the SLS\_In input transition from ON to OFF. The drive begins monitoring for Safe Limited Speed when the delay times out. The SLS\_Out output is ON if Safe Limited Speed monitoring is active and the speed is below the configured Safe Speed Limit, considering hysteresis.

Figure 24 - Timing Diagram for Safe Limited Speed Status Only

<!-- image -->

(1) Low Threshold = (Speed Hysteresis/100) x Safe Speed Limit

## SLS Status Only Parameter List

## Speed Hysteresis

The [Safe Limited Speed Hysteresis] parameter provides hysteresis for the SLS\_Out output when the drive is configured for SLS Status Only and Safe Limited Speed monitoring is active. The SLS\_Out output is turned ON if the speed is less than the Low Threshold [(Speed Hysteresis/100) x Safe Speed Limit]. The SLS\_Out output is turned OFF when the speed is greater than or equal to the configured [Safe Speed Limit].

The SLS\_Out output remains OFF if Safe Limited Speed monitoring begins when the detected speed is less than the configured Safe Speed Limit but greater than or equal to the Low Threshold [(Speed Hysteresis/100) x Safe Speed Limit].

The SLS\_Out output is held in its last state when the speed is less than the configured Safe Speed Limit and the speed is greater than or equal to the Low Threshold [(Speed Hysteresis/100) x Safe Speed Limit].

To configure the drive for Safe Limited Speed Status Only monitoring, set these parameters in addition to the Safe Stop parameters listed on page 66 .

Table 26 - SLS Status Only Parameters

| Tab                                                        | Parameter Name Description       |                                                                                                                                                        | Values (Safety Configuration Tool)                                                                                                                                               |
|------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Change System Configuration                         |                                  | Operation Mode Defines the primary operating mode of the speed monitoring safety functions.                                                            | Setting: SafeStop-Safe Limited Speed Status Only                                                                                                                                 |
| Input Change Input Configuration Type                      |                                  | Safe Limited Speed Configuration for the Safe Limited Speed input (SLS_In).                                                                            | Default: Not Used (1)                                                                                                                                                            |
| Input Change Input Configuration Type                      |                                  | Safe Limited Speed Configuration for the Safe Limited Speed input (SLS_In).                                                                            | Options: Not Used Dual Channel Equivalent Dual Channel Equivalent 3 s Dual Channel Complementary Dual Channel Complementary 3 s Solid State Device Equivalent 3 s Single Channel |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Monitor Delay | Defines the Safe Limited Speed Monitoring Delay between the SLS_In ON to OFF transition and the initiation of the Safe Limited Speed (SLS) monitoring. | Default: 0                                                                                                                                                                       |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Monitor Delay | Defines the Safe Limited Speed Monitoring Delay between the SLS_In ON to OFF transition and the initiation of the Safe Limited Speed (SLS) monitoring. | Range: 0…6553.5 s                                                                                                                                                                |
| Safe Limited Speed Change Safe Limited Speed Configuration |                                  | Safe Speed Limit Defines the speed limit that is monitored in Safe Limited Speed (SLS) mode.                                                           | Default: 0                                                                                                                                                                       |
| Safe Limited Speed Change Safe Limited Speed Configuration |                                  | Safe Speed Limit Defines the speed limit that is monitored in Safe Limited Speed (SLS) mode.                                                           | Range: 0…65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                            |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Hysteresis    | Provides hysteresis for SLS_Out output when Safe Limited Speed monitoring is active.                                                                   | Default: 0                                                                                                                                                                       |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Hysteresis    | Provides hysteresis for SLS_Out output when Safe Limited Speed monitoring is active.                                                                   | Range: 10…100% when [Operation Mode] = SafeStop-SafeLimitedSpeedStatusOnly                                                                                                       |

## SLS Status Only Wiring Examples

These examples illustrate wiring for SLS status only operation.

Figure 25 - Master, Safe Limited Speed Status Only (Single Unit)

<!-- image -->

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              28 | TEST_OUT_1      |              28 |

|   29 | SLS_OUT_CH0   |   29 |
|------|---------------|------|
|   30 | SLS_OUT_CH1   |   30 |
|   31 | DM_IN_CH0     |   31 |
|   32 | DM_IN_CH1     |   32 |
|   33 | LM_IN_CH0     |   33 |
|   34 | LM_IN_CH1     |   34 |
|   35 | DC_OUT_CH0    |   35 |
|   36 | DC_OUT_CH1    |   36 |
|   37 | ESM_IN_CH0    |   37 |
|   38 | ESM_IN_CH1    |   38 |

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              26 | RESET_IN        |              26 |
|              25 | RST_REF         |              25 |
|              24 | SLS_IN_CH1      |              24 |
|              23 | SLS_IN_CH0      |              23 |
|              22 | SS_OUT_CH1      |              22 |
|              21 | SS_OUT_CH0      |              21 |
|              20 | SS_IN_CH1       |              20 |
|              19 | SS_IN_CH0       |              19 |
|              18 | SCOM            |              18 |
|              17 | SPWR            |              17 |

Figure 26 - Master, Safe Limited Speed Status Only (First Unit)

<!-- image -->

This example assumes that a programmable safety controller is monitoring all drive functions and controlling the drive. The SS\_In and SLS\_In inputs are connected to the I/O module; however, standard safety component inputs could also be used.

These functions are not performed by the drive in this scenario:

- Guardlocking switch inputs
- Door locking
- Door status (open or closed)
- Enabling switch

Figure 27 - Safe Limited Speed Status Only with Programmable Controller Monitoring

<!-- image -->

## Cascaded Configurations

<!-- image -->

## Slave Modes for Multi-axis Cascaded Systems

This chapter describes the slave modes of safety operation and wiring examples of cascaded multi-axis configurations.

| Topic                                                 |   Page |
|-------------------------------------------------------|--------|
| Cascaded Configurations                               |     89 |
| Slave, Safe Stop Mode                                 |     91 |
| Slave, Safe Stop Parameter List                       |     91 |
| Slave, Safe Stop Wiring Examples                      |     93 |
| Slave, Safe Limited Speed Mode                        |     96 |
| Slave, Safe Limited Speed Parameters                  |     96 |
| Slave, Safe Limited Speed Wiring Examples             |     97 |
| Slave, Safe Limited Speed Status Only Mode            |     99 |
| Slave, Safe Limited Speed Status Only Parameter List  |     99 |
| Slave, Safe Limited Speed Status Only Wiring Examples |    100 |
| Multi-axis Connections                                |    101 |

Use the [System Configuration] parameter to define the drive's position in the system as Single Unit, Cascaded First Unit, Cascaded Middle Unit, or Cascaded Last Unit. Only the middle or last drive in a multi-axis system can be configured for slave modes.

For cascaded drives, connect the safety switches to the safety inputs (SS\_In, SLS\_In, DM\_In, ESM\_In, and LM\_In) of only the first (master) axis. Each feedback for Safe Stop functions are connected to their respective axis. The inputs are cascaded from one drive to the next by connecting the outputs from the previous drive to the inputs of the next drive.

Figure 28 - Cascaded Connections

<!-- image -->

(1) Automatic reset is selected for middle and last cascaded units if a single reset input to the master unit is used. A single reset by the first unit resets all following units in the cascaded system. If a fault occurs after the first axis in the cascaded chain, only the subsequent axes enter the safe state. Reset is accomplished either manual or manual monitored by applying IOD-25 RESET\_Ref to IOD-26 RESET\_In. To reset all axes, you must cycle the SS\_Input on the first axis.

(2) The Enabling Switch Monitor Input and Lock Monitor Input are connected to only the master axis.

(3) The Cascaded Last Unit DC output is conected to the door control solenoid to indicate that the door monitor output is terminated and encompasses the master, middle, and last units in the chain.

The inputs from the safety switches are monitored by the first (master) drive. A Safe Limited Speed Reset detected by the first drive is cascaded to the subsequent drives via the SLS\_Out to SLS\_In chain. Although all units can be configured for any reset type, we recommend using automatic reset in all slave units to follow the master units reset type.

Any fault or transition of the SS\_In input to OFF is detected by the first drive and initiates the configured [Stop Category] to all of the drives via the SS\_Out to SS\_In chain.

Any fault in a slave drive initiates the configured [Stop Category] only to that drive and to slave drives further down the chain.

| IMPORTANT   | Safe Stop monitoring is not initiated for non-faulted units earlier in the cascaded chain.                        |
|-------------|-------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | The safety reaction time for a cascaded system includes the sum of the reaction times of each drive in the chain. |

## Slave, Safe Stop Mode

## Slave, Safe Stop Parameter List

Table 27 - Slave, Safe Stop Parameters

| Tab                                   | Parameter Name Description                                                                                                                           | Values (Safety Configuration Tool)   | Values (Safety Configuration Tool)               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|--------------------------------------------------|
| Safety Change System Configuration    | System Configuration Defines whether the drive is a single unit or if it occupies a first, middle, or last position in a multi-axis cascaded system. |                                      | Options: Cascaded Middle Unit Cascaded Last Unit |
| Safety Change System Configuration    | Operation Mode Defines the primary operating mode of the speed monitoring safety functions.                                                          |                                      | Default: SafeStop                                |
| Input Change Input Configuration Type | Safe Stop Configuration for Safe Stop input (SS_In).                                                                                                 |                                      | Option: Solid State Device Equivalent 3 s        |

When properly configured for Slave, Safe Stop mode, the drive performs the same functions as Safe Stop except that the drive regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output. This makes sure that the Door Control output commands the door to unlock only if all units command the door to unlock.

To configure the drive for a Slave, Safe Stop mode, set these parameters. See Multi-axis Connections on page 101 for details on configuring slave drives.

Table 27 - Slave, Safe Stop Parameters (continued)

| Tab                                      | Parameter Name Description   |                                                                                                                                                                                                                                                                                                                                                        | Values (Safety Configuration Tool)                                                                                                                            |
|------------------------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safe Stop Change Safe Stop Configuration |                              | Stop Category Safe operating stop type selection. This defines the type of Safe Stop that is performed if the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                | Default: Safe Torque-Off                                                                                                                                      |
| Safe Stop Change Safe Stop Configuration |                              | Stop Category Safe operating stop type selection. This defines the type of Safe Stop that is performed if the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                | Options: Safe Torque-Off Safe Stop 1 Safe Stop 2                                                                                                              |
| Safe Stop Change Safe Stop Configuration |                              | Enable Standstill Checking Automatically enabled for Safe Stop 1 and Safe Stop 2.                                                                                                                                                                                                                                                                      | Default: Standstill Checking Enabled                                                                                                                          |
| Safe Stop Change Safe Stop Configuration |                              | Enable Standstill Checking Automatically enabled for Safe Stop 1 and Safe Stop 2.                                                                                                                                                                                                                                                                      | Options: Standstill Checking Enabled Standstill Checking Not Enabled                                                                                          |
| Safe Stop Change Safe Stop Configuration | Safe Stop Monitor Delay      | Defines the monitoring delay between the request and the Maximum Stop Time when the request for a Safe Stop 1 or a Safe Stop 2 is initiated by an SS_In input ON to OFF transition. If the Stop Category is Safe Torque-Off with or without Standstill Speed Checking, the Safe Stop Monitor Delay must be 0 or an Invalid Configuration fault occurs. | Default: 0                                                                                                                                                    |
| Safe Stop Change Safe Stop Configuration | Safe Stop Monitor Delay      | Defines the monitoring delay between the request and the Maximum Stop Time when the request for a Safe Stop 1 or a Safe Stop 2 is initiated by an SS_In input ON to OFF transition. If the Stop Category is Safe Torque-Off with or without Standstill Speed Checking, the Safe Stop Monitor Delay must be 0 or an Invalid Configuration fault occurs. | Range: 0…6553.5 s                                                                                                                                             |
| Safe Stop Change Safe Stop Configuration | Deceleration Reference Speed | Determines deceleration rate to monitor for Safe Stop 1 or Safe Stop 2.                                                                                                                                                                                                                                                                                | Default: 0                                                                                                                                                    |
| Safe Stop Change Safe Stop Configuration | Deceleration Reference Speed | Determines deceleration rate to monitor for Safe Stop 1 or Safe Stop 2.                                                                                                                                                                                                                                                                                | Range: 0…65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                         |
| Safe Stop Change Safe Stop Configuration |                              | Maximum Stop Time Defines the maximum stop delay time that is used when the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                                                  | Default: 0                                                                                                                                                    |
| Safe Stop Change Safe Stop Configuration |                              | Maximum Stop Time Defines the maximum stop delay time that is used when the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                                                  | Range: 0…6553.5 s                                                                                                                                             |
| Safe Stop Change Safe Stop Configuration | Deceleration Tolerance       | This is the acceptable tolerance above the deceleration rate set by the [Deceleration Reference Speed] parameter.                                                                                                                                                                                                                                      | Default: 0                                                                                                                                                    |
| Safe Stop Change Safe Stop Configuration | Deceleration Tolerance       | This is the acceptable tolerance above the deceleration rate set by the [Deceleration Reference Speed] parameter.                                                                                                                                                                                                                                      | Range: 0…100% of Deceleration Reference Speed                                                                                                                 |
| Safe Stop Change Safe Stop Configuration |                              | Standstill Speed Defines the speed limit that is used to declare motion as stopped. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                                                                         | Default: 0.001                                                                                                                                                |
| Safe Stop Change Safe Stop Configuration |                              | Standstill Speed Defines the speed limit that is used to declare motion as stopped. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                                                                         | Range: 0.001…65.535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                     |
| Safe Stop Change Safe Stop Configuration | Standstill Position Window   | Defines the position limit window in encoder 1 degrees or mm that is tolerated after a safe stop condition has been detected. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                               | Default: 10                                                                                                                                                   |
| Safe Stop Change Safe Stop Configuration | Standstill Position Window   | Defines the position limit window in encoder 1 degrees or mm that is tolerated after a safe stop condition has been detected. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                               | Range: 0…65,535 degrees (360° = 1 revolution) or mm ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter |
| Safety                                   |                              | Door Control Output Defines the lock and unlock state for door control output (DC_Out). Any Door Control Output option can be used for a single-axis system or for the last unit in a multi-axis system. The first and middle units of a multi-axis system must be configured as 2 Channel Sourcing.                                                   | Default: Power to Release                                                                                                                                     |
| Change System Configuration              |                              | Door Control Output Defines the lock and unlock state for door control output (DC_Out). Any Door Control Output option can be used for a single-axis system or for the last unit in a multi-axis system. The first and middle units of a multi-axis system must be configured as 2 Channel Sourcing.                                                   | Options: Power to Release Power to Lock 2 Channel Sourcing                                                                                                    |
| Input                                    |                              | Door Monitor Configuration for the Door Monitor input (DM_In). Option: Solid State Device Equivalent 3 s                                                                                                                                                                                                                                               |                                                                                                                                                               |
| Change Input Configuration Type          |                              | Door Monitor Configuration for the Door Monitor input (DM_In). Option: Solid State Device Equivalent 3 s                                                                                                                                                                                                                                               |                                                                                                                                                               |

## Slave, Safe Stop Wiring Examples

These examples show two different Slave, Safe Stop configurations.

The first example shows the drive configured as a cascaded middle unit via the [System Configuration] parameter. It has SS\_In and DM\_In input connections from the previous upstream drive, as well as SS\_Out and DC\_Out output connections to the next downstream drive. This unit is configured with automatic reset so it follows the function of the previous axis.

See Safe Stop with Door Monitoring Wiring Example on page 69 for an example of a first (master) unit.

Figure 29 - Slave, Safe Stop, Middle Unit

<!-- image -->

| Previous Upstream Axis IOD Connector Terminals   | Previous Upstream Axis IOD Connector Terminals   | Previous Upstream Axis IOD Connector Terminals   | Previous Upstream Axis IOD Connector Terminals   | Middle Axis IOD Connector Terminals   | Middle Axis IOD Connector Terminals   | Middle Axis IOD Connector Terminals   | Next Downstream Axis IOD Connector Terminals   | Next Downstream Axis IOD Connector Terminals   | Next Downstream Axis IOD Connector Terminals   |
|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|--------------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| IOD Connector                                    | IOD Connector                                    | IOD Connector                                    | IOD Connector                                    | IOD Connector                         | IOD Connector                         | IOD Connector                         | IOD Connector                                  | IOD Connector                                  | IOD Connector                                  |
|                                                  | 28                                               | TEST_OUT_1                                       | 28                                               |                                       | 28                                    | TEST_OUT_1 28                         | 28                                             | TEST_OUT_1                                     | 28                                             |
|                                                  | 27                                               | TEST_OUT_0                                       | 27                                               |                                       | 27                                    | TEST_OUT_0 27                         | 27                                             | TEST_OUT_0                                     | 27                                             |
|                                                  | 26                                               | RESET_IN                                         | 26                                               |                                       | 26                                    | RESET_IN 26                           | 26                                             | RESET_IN                                       | 26                                             |
|                                                  | 25                                               | RESET_REF                                        | 25                                               |                                       | 25                                    | RESET_REF 25                          | 25                                             | RESET_REF                                      | 25                                             |
|                                                  | 24                                               | SLS_IN_CH1                                       | 24                                               |                                       | 24                                    | 24 SLS_IN_CH1                         | 24                                             | SLS_IN_CH1                                     | 24                                             |
|                                                  | 23                                               | SLS_IN_CH0                                       | 23                                               |                                       | 23                                    | 23 SLS_IN_CH0                         | 23                                             | SLS_IN_CH0                                     | 23                                             |
|                                                  | 22                                               | SS_OUT_CH1                                       | 22                                               |                                       | 22                                    | 22 SS_OUT_CH1                         | 22                                             | SS_OUT_CH1                                     | 22                                             |
|                                                  | 21                                               | SS_OUT_CH0                                       | 21                                               |                                       | 21                                    | 21 SS_OUT_CH0                         | 21                                             | SS_OUT_CH0                                     | 21                                             |
|                                                  | 20                                               | SS_IN_CH1                                        | 20                                               |                                       | 20                                    | 20 SS_IN_CH1                          | 20                                             | SS_IN_CH1                                      | 20                                             |
|                                                  | 19                                               | SS_IN_CH0                                        | 19                                               |                                       | 19                                    | 19 SS_IN_CH0                          | 19                                             | SS_IN_CH0                                      | 19                                             |
| GND                                              | 18                                               | SCOM                                             | 18                                               |                                       | 18                                    | 18 SCOM                               | 18                                             | SCOM                                           | 18                                             |
| +24V DC                                          | 17                                               | SPWR                                             | 17                                               |                                       | 17                                    | 17 SPWR                               | 17                                             | SPWR                                           | 17                                             |
|                                                  | 29                                               | SLS_OUT_CH0                                      | 29                                               |                                       | 29                                    | SLS_OUT_CH0 29                        | 29                                             | SLS_OUT_CH0                                    | 29                                             |
|                                                  | 30                                               | SLS_OUT_CH1                                      | 30                                               |                                       | 30                                    | SLS_OUT_CH1 30                        | 30                                             | SLS_OUT_CH1                                    | 30                                             |
|                                                  | 31                                               | DM_IN_CH0                                        | 31                                               |                                       | 31                                    | DM_IN_CH0 31                          | 31                                             | DM_IN_CH0                                      | 31                                             |
|                                                  | 32                                               | DM_IN_CH1                                        | 32                                               |                                       | 32                                    | DM_IN_CH1 32                          | 32                                             | DM_IN_CH1                                      | 32                                             |
|                                                  | 33                                               | LM_IN_CH0                                        | 33                                               |                                       | 33                                    | LM_IN_CH0 33                          | 33                                             | LM_IN_CH0                                      | 33                                             |
|                                                  | 34                                               | LM_IN_CH1                                        | 34                                               |                                       | 34                                    | LM_IN_CH1 34                          | 34                                             | LM_IN_CH1                                      | 34                                             |
|                                                  | 35                                               | DC_OUT_CH0                                       | 35                                               |                                       | 35                                    | DC_OUT_CH0 35                         | 35                                             | DC_OUT_CH0                                     | 35                                             |
|                                                  | 36                                               | DC_OUT_CH1                                       | 36                                               |                                       | 36                                    | DC_OUT_CH1 36                         | 36                                             | DC_OUT_CH1                                     | 36                                             |
|                                                  | 37                                               | ESM_IN_CH0                                       | 37                                               |                                       | 37                                    | ESM_IN_CH0 37                         | 37                                             | ESM_IN_CH0                                     | 37                                             |
|                                                  | 38                                               | ESM_IN_CH1                                       | 38                                               |                                       | 38                                    | ESM_IN_CH1 38                         | 38                                             | ESM_IN_CH1                                     | 38                                             |

This example shows the last cascaded slave drive in the system. It has SS\_In and DM\_In inputs from the previous upstream drive, but its DC\_Out output is connected to a guardlocking interlock switch. This unit is configured with automatic reset so it follows the function of the previous axis.

Figure 30 - Slave, Safe Stop, Last Unit

<!-- image -->

This example shows three drives connected together in a cascaded system.

## IMPORTANT

All drive modules must share a common ground.

Figure 31 - First, Middle, and Last Drives in a Cascaded System with Door Control and Lock Monitoring

<!-- image -->

## Slave, Safe Limited Speed Mode

## Slave, Safe Limited Speed Parameters

When properly configured for Slave, Safe Limited Speed mode, the drive performs the same functions as Safe Limited Speed mode as described on page 71 .

However, the drive regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output. Door Monitoring, Enabling Switch Monitoring, and Lock Monitoring functions are not allowed in this mode.

For the door to unlock, all axes must be below safe limited speed.

TIP Only the middle and last drive in a multi-axis system can be configured for slave modes.

To configure the drive for Slave, Safe Limited Speed monitoring, set these parameters in addition to the Slave, Safe Stop parameters listed on page 91. See Multi-axis Connections on page 101 for details on configuring slave drives.

| Tab                                                        | Parameter Name Description                                                                                                                                                | Values (Safety Configuration Tool)                                                                                                    |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Safety Change System Configuration                         | System Configuration Defines whether the drive is a single unit or if it occupies a first, middle, or last position in a multi-axis cascaded system.                      | Options: Cascaded Middle Unit Cascaded Last Unit                                                                                      |
| Safety Change System Configuration                         | Operation Mode Defines the primary operating mode of the speed monitoring safety functions.                                                                               | Default: SafeStop-Safe Limited Speed                                                                                                  |
| Input Change Input Configuration Type                      | Safe Limited Speed Configuration for the Safe Limited Speed input (SLS_In).                                                                                               | Default: Solid State Device Equivalent 3 s                                                                                            |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Defines the Safe Limited Speed Monitoring Delay between the SLS_In ON to OFF transition and the initiation of the Safe Limited Speed (SLS) monitoring. | Default: 0                                                                                                                            |
| Safe Limited Speed Change Safe Limited Speed Configuration | Monitor Delay                                                                                                                                                             | Range: 0…6553.5 s                                                                                                                     |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Speed Limit Defines the speed limit that is monitored in Safe Limited Speed (SLS) mode.                                                                              | Default: 0 (1)                                                                                                                        |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Speed Limit Defines the speed limit that is monitored in Safe Limited Speed (SLS) mode.                                                                              | Range: 0…65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter |

## Slave, Safe Limited Speed Wiring Examples

These examples show two different Slave, Safe Limited Speed configurations.

The first example is configured as a cascaded middle unit via the [System Configuration] parameter. It has SS\_In, SLS\_In, and DM\_In input connections from the previous upstream drive, as well as SS\_Out, SLS\_Out, and DC\_Out output connections to the next downstream drive.

See SLS with Door Monitoring Wiring Example on page 77 for an example of a first (master) unit.

Figure 32 - Slave, Safe Limited Speed, Middle Unit

<!-- image -->

## Previous Upstream Axis IOD Connector Terminals

|   IOD Connector | IOD Connector   |   IOD Connector |
|-----------------|-----------------|-----------------|
|              28 | TEST_OUT_1      |              28 |
|              27 | TEST_OUT_0      |              27 |
|              26 | RESET_IN        |              26 |
|              25 | RESET_REF       |              25 |
|              24 | SLS_IN_CH1      |              24 |
|              23 | SLS_IN_CH0      |              23 |
|              22 | SS_OUT_CH1      |              22 |
|              21 | SS_OUT_CH0      |              21 |
|              20 | SS_IN_CH1       |              20 |
|              19 | SS_IN_CH0       |              19 |
|              18 | SCOM            |              18 |
|              17 | SPWR            |              17 |

|   29 | SLS_OUT_CH0   |   29 |
|------|---------------|------|
|   30 | SLS_OUT_CH1   |   30 |
|   31 | DM_IN_CH0     |   31 |
|   32 | DM_IN_CH1     |   32 |
|   33 | LM_IN_CH0     |   33 |
|   34 | LM_IN_CH1     |   34 |
|   35 | DC_OUT_CH0    |   35 |
|   36 | DC_OUT_CH1    |   36 |
|   37 | ESM_IN_CH0    |   37 |
|   38 | ESM_IN_CH1    |   38 |

Last Axis IOD Connector Terminals

<!-- image -->

This second example is configured as a cascaded last unit via the [System Configuration] parameter. It has SS\_In, SLS\_In, and DM\_In input connections from the previous upstream drive, but its DC\_Out output is connected to a guardlocking interlock switch.

Figure 33 - Slave, Safe Limited Speed, Last Unit

## Slave, Safe Limited Speed Status Only Mode

## Slave, Safe Limited Speed Status Only Parameter List

When properly configured for Slave, Safe Limited Speed Status Only mode, the Safe Speed Monitor Option module performs the same functions as Safe Limited Speed Status Only mode as described on page 84. However, the drive regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output.

The SLS\_Out output of the last drive in a cascaded chain goes high only when all axes are below the Safe Speed Limit. In Safe Limited Speed Status Only mode, each subsequent unit does not enable Safe Limited Speed until the previous unit has reached the Safe Speed Limit.

Door Monitoring and Enabling Switch Monitoring functions are not allowed in this mode.

TIP Only the middle and last drive in a multi-axis system can be configured for slave modes.

To configure the drive for Slave, Safe Limited Speed Status Only monitoring, set these parameters in addition to the Slave, Safe Stop parameters listed on page 91 and the Slave, Safe Limited Speed parameters listed on page 96. See Multi-axis Connections on page 101 for details on configuring slave drives.

Table 28 - Slave, Safe Limited Speed Status Only Parameters

| Tab                                                        | Parameter Name Description    |                                                                                                                                                      | Values (Safety Configuration Tool)                                         |
|------------------------------------------------------------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Safety Change System Configuration                         |                               | System Configuration Defines whether the drive is a single unit or if it occupies a first, middle, or last position in a multi-axis cascaded system. | Options: Cascaded Middle Unit Cascaded Last Unit                           |
| Safety Change System Configuration                         |                               | Operation Mode Defines the primary operating mode of the speed monitoring safety functions.                                                          | Option: SafeStop-Safe Limited Speed Status Only                            |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Hysteresis | Provides hysteresis for SLS_Out output when Safe Limited Speed monitoring is active.                                                                 | Default: 0                                                                 |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Hysteresis | Provides hysteresis for SLS_Out output when Safe Limited Speed monitoring is active.                                                                 | Range: 10…100% when [Operation Mode] = SafeStop-SafeLimitedSpeedStatusOnly |

## Slave, Safe Limited Speed Status Only Wiring Examples

These examples show two different Slave, Safe Limited Speed Status Only configurations.

The first example is configured as a cascaded middle unit via the [System Configuration] parameter. It has SS\_In, SLS\_In, and DM\_In input connections from the previous upstream drive, as well as SS\_Out, SLS\_Out, and DC\_Out output connections to the next downstream drive.

## IMPORTANT

The SLS\_Out signals change state immediately based on the speed relative to the Safe Speed Limit if the Safe Limited Speed Monitoring Delay is set to zero.

See SLS Status Only Wiring Examples starting on page 86 for an example of a first (master) unit.

Figure 34 - Slave, Safe Limited Speed Status Only, Middle Drive

## Previous Upstream Axis IOD Connector Terminals

## Next Downstream Axis IOD Connector Terminals

<!-- image -->

## Previous Upstream Axis IOD Connector Terminals

This second example is configured as a cascaded last unit via the [System Configuration] parameter. It has SS\_In, SLS\_In, and DM\_In input connections from the previous upstream drive, but its SS\_Out, SLS\_Out, and DC\_out outputs are connected to a Bulletin 1791DS module.

Figure 35 - Slave, Safe Limited Speed Status Only, Last Drive

## Last Axis IOD Connector Terminals

<!-- image -->

## Multi-axis Connections

When configuring a multi-axis system, you need to consider the location of each drive in the system. The type of cascaded connections that can be made are dependent upon the Operation mode configurations of the master and slave drives and their positions in the system.

Middle and last units in the cascaded chain can be configured for Automatic reset. A single reset by the first unit also resets all following units in the chain. If a fault occurs after the first axis in the cascaded chain, only the subsequent axis enters the safe state. To reset all axes, you must cycle the SS\_In input on the first axis.

For slave units in a multi-axis system, the SS\_In, SLS\_In, and DM\_In input signal types (if used) must be configured for output switching signal devices (OSSD) because the output from the previous unit is also configured for OSSD.

For middle or last units in multi-axis systems, the drive regards the Door Monitor input as a Door Control output from an upstream axis, and performs a logical AND with its internal Door Control signal to form the cascaded Door Control output.

For information on door control in the master unit, see Door Control on page 64 .

Figure 36 - Multi-axis Connections

| Typical Operation Mode Combinations                                    | Typical Operation Mode Combinations            | Cascaded Connections Allowed   | Cascaded Connections Allowed   | Cascaded Connections Allowed   |
|------------------------------------------------------------------------|------------------------------------------------|--------------------------------|--------------------------------|--------------------------------|
| Master Drive                                                           | First Slave Drive (1) (Second Drive in System) | SS_Out to SS_In                | SLS_Out to SLS_In              | DC_Out to (2) DM_In  (2)                                |
| Safe Stop                                                              | Slave - Safe Stop                              | Yes                            | –                              | Yes                            |
| Safe Stop with Door Monitoring                                         | Slave - Safe Stop                              | Yes                            | –                              | Yes                            |
| Safe Limited Speed                                                     | Slave - Safe Stop                              | Yes                            | –                              | Yes                            |
| Safe Limited Speed                                                     | Slave - Safe Limited Speed                     | Yes                            | Yes                            | Yes                            |
| Safe Limited Speed with Door Monitoring                                | Slave - Safe Stop                              | Yes                            | –                              | Yes                            |
| Safe Limited Speed with Door Monitoring                                | Slave - Safe Limited Speed                     | Yes                            | Yes                            | Yes                            |
| Safe Limited Speed with Enabling Switch Monitoring Slave - Safe Stop   |                                                | Yes                            | –                              | Yes                            |
| Safe Limited Speed with Enabling Switch Monitoring Slave - Safe Stop   | Slave - Safe Limited Speed                     | Yes                            | Yes                            | Yes                            |
| Safe Limited Speed with Door Monitoring and Enabling Switch Monitoring | Slave - Safe Stop                              | Yes                            | –                              | Yes                            |
| Safe Limited Speed with Door Monitoring and Enabling Switch Monitoring | Slave - Safe Limited Speed                     | Yes                            | Yes                            | Yes                            |
| Safe Limited Speed Status Only                                         | Slave - Safe Stop                              | Yes                            | –                              | Yes                            |
| Safe Limited Speed Status Only                                         | Slave - Safe Limited Speed Status Only         | Yes                            | Yes                            | –                              |

This table shows the supported Operation modes for slave drives (n+1) cascaded from slaves (n).

Figure 37 - Slave Drive Operation Modes

| Supported Operation Mode Combinations   | Supported Operation Mode Combinations   | Cascaded Connections Allowed   | Cascaded Connections Allowed   | Cascaded Connections Allowed   |
|-----------------------------------------|-----------------------------------------|--------------------------------|--------------------------------|--------------------------------|
| Slave Drive (n)                         | Slave Drive (n+1)                       | SS_Out to SS_In                | SLS_Out to SLS_In              | DC_Out to (1) DM_In  (1)                                |
| Slave - Safe Stop                       | Slave - Safe Stop                       | Yes                            | —                              | Yes                            |
| Slave - Safe Limited Speed              | Slave - Safe Stop                       | Yes                            | —                              | Yes                            |
| Slave - Safe Limited Speed              | Slave - Safe Limited Speed              | Yes                            | Yes                            | Yes                            |
| Slave - Safe Limited Speed Status Only  | Slave - Safe Stop                       | Yes                            | —                              | Yes                            |
| Slave - Safe Limited Speed Status Only  | Slave - Safe Limited Speed Status Only  | Yes                            | Yes                            | Yes                            |

## Safe Maximum Speed (SMS) Monitoring

<!-- image -->

## Safe Maximum Speed and Direction Monitoring

This chapter describes Safe Maximum Speed (SMS), Safe Maximum Acceleration (SMA), and Safe Direction (SDM) monitoring modes of safety operation and provides a list of configuration parameters.

| Topic                                                         |   Page |
|---------------------------------------------------------------|--------|
| Safe Maximum Speed (SMS) Monitoring                           |    103 |
| Safe Maximum Acceleration (SMA) Monitoring                    |    106 |
| Safe Direction Monitoring (SDM)                               |    108 |
| Max Speed, Max Accel, and Direction Monitoring Parameter List |    110 |

Configure Safe Maximum Speed monitoring by setting the [Enable Maximum Speed Monitoring] parameter to Enable. When configured, Safe Maximum Speed monitoring is active any time the drive configuration is valid and the Operation mode is not Disabled.

When you configure the drive for Safe Maximum Speed, the feedback velocity is monitored and compared against a user-configurable limit.

The [Safe Maximum Speed Limit] parameter is relative to encoder 1. If the monitored speed is greater than or equal to the configured [Safe Maximum Speed Limit] value, an SMS Speed fault (Stop Category fault) occurs.

Figure 38 - Safe Max Speed Timing Diagram

<!-- image -->

You define the Stop Category initiated by the drive in the event of an SMS Speed fault by using the [Safe Maximum Speed Monitoring Stop Behavior] parameter.

Table 29 - SMS Monitoring Stop Behavior

| [Safe Maximum Speed Monitoring Stop Behavior] Parameter   | Description                                                                                                                                 |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Use Safe Torque Off with Check for Standstill             | The drive initiates Safe Torque Off with Check for Standstill any time an SMS Speed fault is detected while the drive is monitoring motion. |
| Use Configured Stop Type                                  | The drive initiates the configured [Stop Category] parameter any time an SMS Speed fault is detected while the drive is monitoring motion.  |

If an SMS Speed fault is detected during a Stop Monitoring Delay, [Safe Stop Monitor Delay], the delay ends immediately and the configured Stop Delay [Maximum Stop Time] begins.

Figure 39 - SMS Speed Fault During Stop Monitoring Delay

<!-- image -->

If an SMS Speed fault is detected during the Stop Delay [Max Stop Time], and the [Safe Maximum Speed Monitoring Stop Behavior] parameter equals Use Configured Stop Type, and the feedback signals indicate less than maximum frequency (1) for your encoder type, the fault is reported, but no further action is taken. Deceleration monitoring performs the safety function during the Stop Delay [Maximum Stop Time]. That is, if an SMS Speed fault occurs during the Stop Delay [Maximum Stop Time], the fault is ignored and the stopping action continues.

Figure 40 - SMS Speed Fault When [Safe Maximum Speed Monitoring Stop Behavior] Set to 'Use Configured Stop Type'

<!-- image -->

(1) 100 kHz for Sin/Cos or 200 kHz for Incremental

If an SMS Speed fault is detected during the Stop Delay [Maximum Stop Time] and the [Safe Maximum Speed Monitoring Stop Behavior] parameter equals Use Safe Torque Off with Check for Standstill, the SMS Speed fault is reported and motion power is removed. The Stop Delay [Maximum Stop Time] continues with standstill checking enabled.

Figure 41 - SMS Speed Fault When [Safe Maximum Speed Monitoring Stop Behavior] Set to 'Use Safe Torque Off with Check for Standstill'

<!-- image -->

(1) This signal is internal to the drive.

For more information about faults, see Fault Reactions on page 137 .

## Safe Maximum Acceleration (SMA) Monitoring

Configure Safe Maximum Acceleration monitoring by setting the [Enable Maximum Acceleration Monitoring] parameter to Enable. When configured, Safe Maximum Acceleration Monitoring is active any time the drive configuration is valid and Operation mode is not set to Disabled.

The resolution accuracy of the acceleration monitoring in revolutions/second 2 is equal to the speed resolution in:

<!-- image -->

The resolution accuracy of the acceleration monitoring in mm/second 2 is equal to the speed resolution in:

(mm/s x 2)

[(Overspeed Response Time - 36)/1000] seconds

## IMPORTANT

Acceleration is measured within the Overspeed Response Time, [Overspeed Response Time] parameter.

When you configure the drive for Safe Maximum Acceleration, the drive monitors the acceleration rate and compares it to a configured Safe Maximum Acceleration Limit, [Safe Maximum Acceleration Limit]. If the acceleration is greater than or equal to the configured [Safe Maximum Acceleration Limit], an Acceleration fault (Stop Category fault) occurs.

Figure 42 - Safe Max Acceleration Timing Diagram

<!-- image -->

You define the Stop Category initiated by the drive in the event of an Acceleration fault by using the [Safe Maximum Acceleration Monitoring Stop Behavior] parameter.

Table 30 - SMA Monitoring Stop Behavior

| [Safe Maximum Acceleration Monitoring Stop Behavior] Parameter   | Description                                                                                                                                                                                  |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                  | Use Safe Torque Off with Check for Standstill The drive initiates Safe Torque Off with Check for Standstill any time an Acceleration fault is detected while the drive is monitoring motion. |
| Use Configured Stop Type                                         | The drive initiates the configured Stop Category any time an Acceleration fault is detected while the drive is monitoring motion.                                                            |

If an Acceleration fault is detected during a Stop Monitoring Delay [Safe Stop Monitor Delay] and the [Safe Maximum Acceleration Monitoring Stop Behavior] parameter is configured as Use Safe Torque Off with Check for Standstill, the Stop Monitoring Delay [Safe Stop Monitor Delay] ends immediately and Stop Delay [Maximum Stop Time] begins.

If an Acceleration fault is detected during the Stop Delay [Maximum Stop Time], and the [Safe Maximum Acceleration Monitoring Stop Behavior] parameter equals Use Configured Stop Type, and feedback signals indicate less than the maximum frequency (1) for your encoder type, then the fault occurs with no further action. Deceleration Monitoring performs the safety function during the Stop Delay [Maximum Stop Time]. That is, if an Acceleration fault occurs during the Stop Delay [Maximum Stop Time], the fault is ignored and the stopping action continues.

Figure 43 - Acceleration Fault When [Safe Maximum Acceleration Monitoring Stop Behavior] Set to 'Use Configured Stop Type'

<!-- image -->

If an Acceleration fault is detected during the Stop Delay [Maximum Stop Time] and the [Safe Maximum Acceleration Monitoring Stop Behavior] parameter equals Use Safe Torque Off with Check for Standstill, the Acceleration fault is reported and Motion Power is removed. The Stop Delay [Maximum Stop Time] continues with standstill checking enabled.

## Safe Direction Monitoring (SDM)

Figure 44 - Acceleration Fault When [Safe Maximum Acceleration Monitoring Stop Behavior] Set to 'Use Safe Torque Off with Check for Standstill'

<!-- image -->

- (1) This signal is internal to the drive.

For more information about faults, see Fault Reactions on page 137 .

When configured for Safe Direction Monitoring, the drive monitors the feedback direction and initiates the configured Stop Category when motion in the illegal direction is detected. You configure Safe Direction Monitoring by using the [Enable Safe Direction Monitoring] parameter. This parameter also determines the direction, positive or negative, that motion is allowed.

Table 31 - Enable Safe Direction Monitoring

| [Enable Safe Direction Monitoring] Parameter Description                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------|
| Disabled Safe Direction Monitoring is disabled.                                                                                                |
| Positive Always Safe Direction Monitoring is active any time the configuration is valid and not Disabled.                                      |
| Positive During SLS Safe Direction Monitoring is performed only when the drive is actively monitoring Safe Limited Speed.  Negative During SLS |

## IMPORTANT

Be sure to set the [Primary Feedback Polarity] and [Secondary Feedback Polarity] configuration parameters properly for a consistent direction between encoder 1 and encoder 2.

You can configure a position limit, in encoder units, tolerated in the wrong direction before a Direction fault occurs, by using the [ Jitter Tolerance] parameter.

Figure 45 - Positive Safe Direction Monitoring Timing Diagram

<!-- image -->

Figure 46 - Negative Safe Direction Monitoring Timing Diagram

<!-- image -->

If motion is detected in the incorrect direction while Safe Direction Monitoring is active, a Direction fault occurs. If a Direction fault is detected while the drive is monitoring motion, the configured [Stop Category] is initiated and direction monitoring is not performed during the safe stop. If a Direction fault is first detected after the initiation of the safe stop, then all outputs go to their faulted state.

For more information about faults, see Fault Reactions on page 137 .

## Max Speed, Max Accel, and Direction Monitoring Parameter List

Set these parameters to configure Safe Maximum Speed, Safe Maximum Acceleration, and Safe Direction Monitoring.

Table 32 - Max Speed, Max Accel, and Direction Monitoring Parameters

| Tab                                                           | Parameter Name Description                         |                                                                                                                                 | Values (Safety Configuration Tool)                                                                                                    |
|---------------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Feedback Primary Feedback                                     |                                                    | Feedback Polarity Defines the direction polarity for encoder 1. Default: Positive                                               |                                                                                                                                       |
| Feedback Primary Feedback                                     |                                                    | Feedback Polarity Defines the direction polarity for encoder 1. Default: Positive                                               | Options: Positive Negative                                                                                                            |
| Feedback Secondary Feedback                                   |                                                    | Feedback Polarity Defines the direction polarity for encoder 2. Options: Positive                                               | Negative                                                                                                                              |
| Safe Max Speed Change Safe Maximum Speed Configuration        | Safe Maximum Speed Configuration                   | Enable Maximum Speed Monitoring.                                                                                                | Default: Maximum Speed Monitoring Not Enabled                                                                                         |
| Safe Max Speed Change Safe Maximum Speed Configuration        | Safe Maximum Speed Configuration                   | Enable Maximum Speed Monitoring.                                                                                                | Options: Maximum Speed Monitoring Not Enabled Maximum Speed Monitoring Enabled                                                        |
| Safe Max Speed Change Safe Maximum Speed Configuration        | Safe Maximum Speed Limit                           | Defines the maximum speed limit that is tolerated if Safe Maximum Speed (SMS) monitoring is enabled.                            | Default: 0                                                                                                                            |
| Safe Max Speed Change Safe Maximum Speed Configuration        | Safe Maximum Speed Limit                           | Defines the maximum speed limit that is tolerated if Safe Maximum Speed (SMS) monitoring is enabled.                            | Range: 0…65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter |
| Safe Max Speed Change Safe Maximum Speed Configuration        | Safe Maximum Speed Monitoring Stop Behavior        | Defines the Stop Category that is initiated in the event of a SMS Speed fault.                                                  | Default: Use Safe Torque-Off with Check for Standstill                                                                                |
| Safe Max Speed Change Safe Maximum Speed Configuration        | Safe Maximum Speed Monitoring Stop Behavior        | Defines the Stop Category that is initiated in the event of a SMS Speed fault.                                                  | Options: Use Safe Torque-Off with Check for Standstill Use Configured Stop Type                                                       |
| Safe Max Accel Change Safe Maximum Acceleration Configuration | Safe Maximum Acceleration Configuration            | Enable Maximum Acceleration Monitoring. Default: Maximum Acceleration Monitoring Not Enabled                                    |                                                                                                                                       |
| Safe Max Accel Change Safe Maximum Acceleration Configuration | Safe Maximum Acceleration Configuration            | Enable Maximum Acceleration Monitoring. Default: Maximum Acceleration Monitoring Not Enabled                                    | Options: Maximum Acceleration Monitoring Not Enabled Maximum Acceleration Monitoring Enabled                                          |
| Safe Max Accel Change Safe Maximum Acceleration Configuration | Safe Maximum Acceleration Limit                    | Defines the Safe Maximum Acceleration (SMA) limit, relative to encoder 1, of the system is being monitored.                     | Default: 0                                                                                                                            |
| Safe Max Accel Change Safe Maximum Acceleration Configuration | Safe Maximum Acceleration Limit                    | Defines the Safe Maximum Acceleration (SMA) limit, relative to encoder 1, of the system is being monitored.                     | Range: 0…65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter |
| Safe Max Accel Change Safe Maximum Acceleration Configuration | Safe Maximum Acceleration Monitoring Stop Behavior | Defines the Stop Category that is initiated in the event of an SMA Acceleration fault.                                          | Default: Use Safe Torque-Off with Check for Standstill                                                                                |
| Safe Max Accel Change Safe Maximum Acceleration Configuration | Safe Maximum Acceleration Monitoring Stop Behavior | Defines the Stop Category that is initiated in the event of an SMA Acceleration fault.                                          | Options: Use Safe Torque-Off with Check for Standstill Use Configured Stop Type                                                       |
| Safe Direction Change Safe Direction Monitoring Configuration | Safe Direction Monitoring Configuration            | Enable Safe Direction Monitoring.                                                                                               | Default: Safe Direction Monitoring Not Enabled                                                                                        |
| Safe Direction Change Safe Direction Monitoring Configuration | Safe Direction Monitoring Configuration            | Enable Safe Direction Monitoring.                                                                                               | Options: Safe Direction Monitoring Not Enabled Safe Direction Monitoring Enabled                                                      |
| Safe Direction Change Safe Direction Monitoring Configuration |                                                    | Monitor Type Defines the monitor type if Safe Direction Monitoring is enabled.                                                  | Options: Always During Safe Limited Speed                                                                                             |
| Safe Direction Change Safe Direction Monitoring Configuration |                                                    | Safe Direction Defines the allowable direction if Safe Direction Monitoring is enabled.                                         | Default: Positive                                                                                                                     |
| Safe Direction Change Safe Direction Monitoring Configuration |                                                    | Safe Direction Defines the allowable direction if Safe Direction Monitoring is enabled.                                         | Options: Positive Negative                                                                                                            |
| Safe Direction Change Safe Direction Monitoring Configuration |                                                    | Jitter Tolerance The position limit in encoder units tolerated in the wrong direction when Safe Direction Monitoring is active. | Default: 10                                                                                                                           |
| Safe Direction Change Safe Direction Monitoring Configuration |                                                    | Jitter Tolerance The position limit in encoder units tolerated in the wrong direction when Safe Direction Monitoring is active. | Range: 0…65,535 deg or mm ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter   |

## Safety Configuration

## Safety Configuration and Verification

This chapter provides guidelines for configuring the safety functions.

| Topic                                         |   Page |
|-----------------------------------------------|--------|
| Safety Configuration                          |    111 |
| Basics of Application Development and Testing |    114 |
| Commissioning the System                      |    114 |
| Editing the Configuration                     |    118 |

Safety configuration is accomplished through a safety configuration tool and an ethernet connection between the drive and your personal computer. The drive has a private IP address, with the final octet determined by the drive SERCOS node address, for example http://192.168.1.1, the IAM power module node address is 001. Refer to the Kinetix 6200 Modular Multi-axis Servo Drive User Manual, publication 2094-UM002, for more information on setting the node address of your Kinetix 6200 modular servo drive.

The safety configuration tool provides a Safety Main page that displays the current status of the safety configuration and buttons to lock/unlock the configuration, save the configuration to a file, apply a specific configuration, and set an optional password. Use the Change Safety Password page to change the password.

When you configure a speed monitoring safety system, you must record and verify the configuration signature and set the safety-lock status of the system configuration. Though optional, you can configure a password to help protect the system configuration from unauthorized modifications.

## Configuration Signature ID

The configuration Signature ID is an identification number that uniquely identifies a specific configuration. Each time the system is configured or reconfigured, a new configuration signature is generated to identify that specific configuration.

You can view the configuration Signature ID by accessing the [Configuration Signature] parameter.

## Safety-lock

When you have verified the operation of the system and recorded the configuration Signature ID, you must lock the configuration to protect it from modification.

| IMPORTANT   | If you do not safety-lock the configuration, untested or unintentional changes can be made to the safety configuration that could result in unexpected system behavior.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

You can lock the configuration by clicking the Lock command in the Safety Main tab.

The safety lock status indicator on the control module illuminates solid yellow when the configuration is locked. The safety lock status indicator flashes yellow when the configuration is unlocked.

You can also check the safety-lock status of the system by viewing the Configuration Lock bit (bit 1) in the AxisServoDrive.GuardStatus tag. If the bit equals 1, the configuration is locked. If it equals 0, the configuration is unlocked.

| IMPORTANT   | The AxisServoDrive.GuardStatus tag must be set as a real time attribute.   |
|-------------|----------------------------------------------------------------------------|

## Set and Change a Password

You can protect the system configuration by using an optional password. If you set a password, edits to the configuration, as well as safety-locking and reset operations require the password to be entered. You can set a password from the Change Safety Password tab.

Follow these steps to set a new password.

1. Open the safety configuration tool and expand the Safety folder.

2. Click the Change Safety Password tab.
3. Enter the New Password and Confirm the New Password.

<!-- image -->

## IMPORTANT

If no password was set previously, you enter only the new password. Once set, you must enter this password to change the password or to use the Safety Main tab commands.

4. Click Change Password.

The safety configuration tool confirms that your password is set.

Follow these steps to change a password.

1. Click the Change Safety Password tab in the Safety folder.
2. Enter the Current Password and enter/confirm the New Password.
3. Click Change Password.

The safety configuration tool confirms that your password is changed.

## Resetting the Password

If you forget the password and need to reset it, you must perform a drive firmware upgrade.

## Resetting the Configuration

To reset the default configuration parameter values, you must perform a drive firmware upgrade.

## Basics of Application Development and Testing

## Commissioning the System

Configuration for the intended SIL CL3, PLe, or Cat 4 system must be carried out by the system integrator or an operator trained and experienced in safety applications. The developer must follow good design practices.

- Use functional specifications, including flow charts, timing diagrams and sequence charts.
- Perform a configuration review.
- Perform configuration validation.

This flowchart shows the steps required for commissioning a Speed Monitoring safety system. The items in bold are explained in the following sections.

Figure 47 - Commissioning a Safety System Flowchart

<!-- image -->

## Specifying the Safety Configuration

You must create a specification for the system configuration that addresses the safety requirements identified by a risk assessment of your application. Use the specification to verify that the configuration is selected correctly and that it fully addresses your application's functional and safety control requirements. The specification must be a detailed description that can include (if applicable):

- a sequence of operations.
- flow and timing diagrams.
- sequence charts.
- a configuration description of each parameter.
- documented descriptions of the steps with step conditions and actuators to be controlled.
- input and output definitions.
- I/O wiring diagrams and references.
- a theory of operation.
- a matrix or table of stepped conditions and the actuators to be controlled, including sequence and timing diagrams.
- a definition of marginal conditions, for example, operating modes.

The I/O portion of the specification must contain the analysis of field circuits, that is, the type of sensors and actuators.

- Sensors (Digital or Analog)
- – Signal in standard operation (dormant current principle for digital sensors, sensors OFF means no signal)
- – Determination of redundancies required for SIL levels
- – Discrepancy monitoring and visualization, including your diagnostic logic
- Actuators
- – Position and activation in standard operation (normally OFF)
- – Safe reaction/positioning when switching OFF or power failure.
- – Discrepancy monitoring and visualization, including your diagnostic logic.

## Configure the Safe Speed Monitoring Drive

The drive is configured in the Safe State. The drive must be unlocked to be configured. If a password exists, you must provide the password to unlock the drive.

Follow these steps to configure the drive.

1. If the drive safety configuration is locked, you can unlock the configuration by clicking Unlock in the Safety Main tab.

If an error occurs, you need to enter the password.

2. Edit parameters to meet your system configuration specification and risk assessment requirements.
3. When you are finished editing parameters, click Apply.

A Configuration Signature ID is generated and displayed in the Safety Main tab. The Configuration Signature ID is also displayed across the drive four-character display for 20 seconds after configuration is applied.

4. Enter the password, if required.
5. Click Lock, in the Safety Main tab, to lock the safety configuration.

Refer to Appendix B for a complete list of parameters and settings for the drive.

## Project Verification Test

To check that the drive's configuration adheres to the application specification, you must generate a suitable set of test cases covering the application. The set of test cases must be filed and retained as the test specification. You must include a set of tests to prove the validity of the safety configuration parameters.

You must perform a complete functional test of the entire system before the operational startup of a safety-related system.

## Confirm the Project

The goal of confirming the project is to make sure the parameter values you configure are retained in the drive. You must check each parameter to make sure it is set to the correct value according to your system configuration specification.

Follow these steps to confirm the project.

1. Open the safety configuration tool and expand the Safety folder.
2. Click Configuration Summary.

<!-- image -->

The Configuration Summary report opens.

<!-- image -->

Each parameter and the parameter values are displayed. This example is only a partial list.

3. Verify that the settings in the report match your system configuration specification.
2. – Click Save to create an html file to record the configuration.
3. – Click Print to create a paper record of the configuration.
4. Return to the Safety Main tab and click Refresh.

The current safety configuration is read from the drive.

5. Click Configuration Summary again and compare the values in your saved file or printed report to the current safety configuration from the drive.
6. Verify that the two Configuration Summary reports match.

## Safety Validation

An independent, third-party review of the safety system can be required before the system is approved for operation. An independent, third-party certification is required for IEC 61508 SIL CL3.

## Editing the Configuration

## Verifying the Signature and Lock in the Safe Speed Monitor Drive

To meet SIL CL3, PLe, or Cat 4 requirements, you must verify that the correct configuration is locked in the drive.

To verify the configuration Signature ID, reopen the Safety Main tab and view the contents of the [Configuration Signature] parameter and make sure that it matches the configuration Signature ID that displayed as part of the configuration process on page 116 .

To verify the lock status, you can view the [Safety Lock Status] parameter. You can also view the status of the Configuration Lock bit (bit 1) of the AxisServoDrive.GuardStatus tag. If the bit equals 1, the configuration is locked. If the bit equals 0, the configuration is unlocked.

Only authorized, specially-trained personnel can make edits to the configuration. Use all supervisory methods available, for example, software password protection.

When authorized, specially-trained personnel make edits, they assume the central safety responsibility while the changes are in progress. These personnel must also maintain safe application operation.

You must sufficiently document all edits, including:

- authorization.
- impact analysis.
- execution.
- test information.
- revision information.

## IMPORTANT

After replacing a 2094-xx02x-M0x-S1 safe-speed control module, the safety configuration (web page) can be from the previous control module of the same IP address. To correct this condition, go to Internet Explorer/Tools/ Internet Options and under Browsing history, click Delete to delete temporary files, cookies, and web form information.

This flowchart shows the steps necessary to edit the drive's configuration.

Figure 48 - Edit Commissioning the Safety System Flowchart

<!-- image -->

## Notes:

## Example Application

## Safety Configuration Example

This configuration example guides you through the basic steps required to program an application that uses some of the safety functions. The other chapters of this manual provide detailed information on the operation of each safety function.

| Topic                                       |   Page |
|---------------------------------------------|--------|
| Example Application                         |    121 |
| Use the Initial Safety Main Tab Commands    |    123 |
| Configure the Safety Tab Parameters         |    126 |
| Feedback Tab Settings                       |    127 |
| Configure the Input Tab Parameters          |    128 |
| Configure the Safe Stop Tab Parameters      |    129 |
| Configure Safe Limited Speed Tab Parameters |    130 |
| Configure Safe Max Speed Tab Parameters     |    131 |

This example application uses the following basic configuration in a single-axis system.

- Safe Stop (SS) enabled with an E-stop button.
- Safe Limited Speed (SLS) initiated with a 2NC contact switch.
- Control &amp; monitoring of door safety interlock switch (TLS 3 GD2) configured as Power to Release.
- A Reset button with 1 NO contact.
- One encoder connected with Sin/Cos output signal and resolution of 1024 cycles per revolution.
- A configured Safe Maximum Speed (SMS) limit.

## IMPORTANT

After replacing a 2094-xx02x-M0x-S1 safe-speed control module, the safety configuration (web page) can be from the previous control module of the same IP address. To correct this condition, go to Internet Explorer/Tools/ Internet Options and under Browsing history, click Delete to delete temporary files, cookies, and web form information.

Figure 49 - Safe Limited Speed with Door Monitoring Example

<!-- image -->

Each of the following sections describe the settings you need to enter for each parameter group. Configuration is accomplished by using the safety configuration tool.

Figure 50 - Safety Configuration Tool - Home Tab

<!-- image -->

## Use the Initial Safety Main Tab Commands

The Safety Main tab lets you lock or unlock the safety configuration, save the configuration to a file, apply a safety configuration, and enter a password. The default [Safety Lock Status] parameter setting is Unlock.

You can set a password from the Change Safety Password tab. You must enter the current password and then enter the new password. If you have forgotten the current password, you must perform a drive firmware upgrade.

## IMPORTANT

If no password was set previously, you enter only the new password. Once set, you must enter this password to change the password or to use the Safety Main tab commands.

Follow these steps to use the Apply, Refresh, Lock, and Unlock commands.

1. Open the safety configuration tool by entering the IP address of the drive. In this example, the IP address is http://192.168.1.1. The final octet is determined by the IAM module node address (001).
2. Expand the Safety folder to gain access to the Safety Main tab.
3. Click Safety Main.
4. The Safety Main tab dialog box opens.
4. Click Apply.

<!-- image -->

The Apply command is used to apply changes you've made to the safety configuration.

If the configuration is locked or protected by a password, the command fails.

<!-- image -->

## 5. Click Refresh.

The Refresh command is used to apply the current safety configuration.

## 6. Click Lock.

The [Safety Lock Status] parameter value changes to Locked and this message appears as confirmation.

If the configuration is already locked or protected by a password, the command fails.

## 7. Click Unlock.

The [Safety Lock Status] parameter value changes to Unlocked and this message appears.

If the configuration is already unlocked or protected by a password, the command fails.

<!-- image -->

Refresh command

Successful

<!-- image -->

Lock command Successful

<!-- image -->

Lockcommand Not

Successful

Unlock command Successful

<!-- image -->

Unlockcommand Not

Successful

Follow these steps to use the Save File and Apply File commands.

## 1. Click Save File.

Your current safety configuration is saved to a file. You can apply this configuration by using the Apply File command.

## 2. Click Browse.

Select your configuration file in the Choose File dialog box.

<!-- image -->

## 3. Click Open.

The path to your file appears in the File Management field.

4. Click Apply File.

Your saved configuration is applied.

If the configuration is locked or protected by a password, the command fails.

<!-- image -->

<!-- image -->

## Configure the Safety Tab Parameters

Follow these steps to configure the Safety tab parameters.

1. Expand the Safety folder to gain access to the Safety tab.
2. Under Safety Configuration, choose Safety.

The Safety tab dialog box opens.

<!-- image -->

3. From the System Configuration pull-down menu, choose Single Unit (default) as the parameter value.
4. From the Operation Mode pull-down menu, choose SafeStopSafeLimitedSpeed-DoorMonitor as the parameter value.

In this mode, the door is locked when the machine speed is above a configured Safe Speed limit. The door can be unlocked when the machine is at Standstill Speed or is at or below the Safe Speed Limit and the SLS\_In input is off.

5. From the Reset Type pull-down menu, choose Manual Monitored as the parameter value.

The Manual Monitored setting requires a closing and opening of the reset circuit for a reset.

6. From the Door Control Output pull-down menu, choose Power to Release as the parameter value.

This setting is chosen because power must be applied to the solenoid inside the TLS-3 GD2 interlock switch for the gate interlock to release.

7. Check the Enable Lock Monitoring box.
8. From the Overspeed Response Time pull-down menu, choose the parameter value.

Refer to Overspeed Response Time on page 43 for more information on setting this parameter.

## Feedback Tab Settings

Follow these steps to configure the Feedback tab parameters.

1. Expand the Safety folder to gain access to the Feedback tab.
2. Under Safety Configuration, choose Feedback.

The Feedback tab dialog box opens.

<!-- image -->

3. From the Feedback Mode pull-down menu, choose Single Encoder (default) as the parameter value for redundant processing and crosschecking of the single encoder input in a 1oo2 architecture.
4. Check the box to enable encoder power supply monitoring. Refer to Encoder Specifications on page 144 to determine the voltage used for your encoder type.
5. From the Primary Feedback Type pull-down menu, choose Sin/Cos as the parameter value.
6. Enter 1024 per Rev as the Primary Feedback Cycles parameter value.

In this example, 1024 cycles per revolution is the feedback type resolution. Yours could be different.

7. From the Primary Feedback Polarity pull-down menu, choose Positive (default) as the parameter value, indicating that the feedback device shaft rotates in the same direction as the motor shaft.

## Configure the Input Tab Parameters

Follow these steps to configure the Input tab parameters.

1. Expand the Safety folder to gain access to the Input tab.
2. Under Safety Configuration, choose Input.

The Input tab dialog box opens.

<!-- image -->

3. From the Safe Stop pull-down menu, choose Dual Channel Equivalent (default) as the parameter value.

In this example, the Safe Stop input (SS\_In) monitors an E-Stop switch with two normally-closed (2NC) contacts.

4. From the Door Monitor pull-down menu, choose Dual Channel Equivalent (default) as the parameter value.

In this example, the Door Monitor input (DM\_In) monitors the TLS-3 GD2 interlock switch with two normally-closed (2NC) contacts.

5. From the Lock Monitor] pull-down menu, choose Dual Channel Equivalent (default) as the parameter value.

In this example, the Lock Monitor input (LM\_In) monitors the TLS 3 GD2 interlock switch with two normally-closed (2NC) contacts.

6. From the Safe Limited Speed pull-down menu, choose Dual Channel Equivalent (default) as the parameter value.

In this example, the Lock Monitor input (LM\_In) monitors a switch with two normally-closed (2NC) contacts. If the NC contacts are open and speed exceeds the configured Safe Limited Speed, the drive initiates the configured Stop Category.

When the drive is actively monitoring Safe Limited Speed, and the monitored value is at or below the configured Safe Speed Limit, the interlock switch is released and the door can be open.

7. From the Enabling Switch Monitor pull-down menu, choose Not Used as the parameter value.

## Configure the Safe Stop Tab Parameters

Refer to Appendix B beginning on page 145 for default, minimum, and maximum values for these safety parameters.

TIP If a rotary feedback device is used, the units are revolutions per minute (RPM). If a linear feedback device is used, the units are in millimeters per second (mm/s).

Follow these steps to configure the Safe Stop tab parameters.

1. Expand the Safety folder to gain access to the Safe Stop tab.
2. Under Safety Configuration, choose Safe Stop. The Safe Stop tab opens.
3. From the Stop Category pull-down menu, choose Safe Torque-Off (default) and check the Standstill Checking box, as the parameter value.
4. Safe Torque-Off with Standstill Checking removes motion generated power from the motor immediately after an
5. E-Stop command and unlocks the door when Standstill Speed is detected.
4. Enter the desired [Maximum Stop Time] parameter value.
5. Enter the desired [Standstill Speed] parameter value.
6. Enter the desired [Standstill Position Window] parameter value.

<!-- image -->

## Configure Safe Limited Speed Tab Parameters

Refer to Appendix B beginning on page 145 for default, minimum, and maximum values for these safety parameters.

- TIP

If a rotary feedback device is used, the units are revolutions per minute (RPM). If a linear feedback device is used, the units are in millimeters per second (mm/s).

Follow these steps to configure the Safe Limited Speed tab parameters.

1. Expand the Safety folder to gain access to the Safe Limited Speed tab.
2. Under Safety Configuration, choose Safe Limited Speed. The Safe Limited Speed tab dialog box opens.
3. Enter the desired [Safe Limited Speed Monitor Delay] parameter value.
4. Enter the desired [Safe Limited Speed] parameter value.

<!-- image -->

## Configure Safe Max Speed Tab Parameters

Refer to Appendix B beginning on page 145 for default, minimum, and maximum values for these safety parameters.

- TIP

If a rotary feedback device is used, the units are revolutions per minute (RPM). If a linear feedback device is used, the units are in millimeters per second (mm/s).

Follow these steps to configure the Safe Max Speed tab parameters.

1. Expand the Safety folder to gain access to the Safe Max Speed tab.
2. Under Safety Configuration, choose Safe Max Speed.
3. The Safe Max Speed tab dialog box opens.
3. Check Enable Maximum Speed Monitoring.
4. Enter the desired [Safe Maximum Speed Limit] parameter value.
5. Click Apply.

<!-- image -->

If all your parameter settings are valid, the configuration is applied.

If one or more of your parameter settings are invalid, the command fails.

<!-- image -->

## Notes:

## Status Indicators

## Nonrecoverable Faults

## Fault Recovery

## Troubleshooting the Safe Speed Monitoring Drive

This chapter provides troubleshooting tables for diagnosing fault conditions associated with the safe speed monitoring safety functions.

| Topic                        |   Page |
|------------------------------|--------|
| Status Indicators            |    133 |
| Nonrecoverable Faults        |    133 |
| Fault Recovery               |    133 |
| Fault Codes and Descriptions |    134 |
| Fault Reactions              |    137 |
| Status Attributes            |    138 |

The safety lock status indicator on the control module illuminates solid yellow when the configuration is locked. The safety lock status indicator flashes yellow when the configuration is unlocked. If there is no safety configuration, the safety lock status indicator is off.

In addition to the recoverable faults described in this chapter, the drive also generates nonrecoverable faults when an anomaly with the drive hardware is detected. These faults are Safe State faults. If a Safe State fault occurs, all safety control outputs are set to their safe state.

To clear a nonrecoverable fault, cycle power. If the nonrecoverable fault persists, the drive must be replaced.

If the fault is no longer present, you can clear the fault condition with a successful SS Reset and a Motion Axis Fault Reset (MAFR) via the Logix Designer application, except in the case of an Invalid Configuration fault, MP Out fault, or Reset At Powerup fault. An Invalid Configuration fault is cleared by a successful reconfiguration. An MP Out fault or Reset At Powerup fault is cleared at power down or by a successful reconfiguration.

## Input and Output Faults

## Fault Codes and Descriptions

An input or output fault indication can be caused by several wiring fault conditions during commissioning or normal operation. If an input fault occurs, check for the following:

- One of the channels is shorted to a 24V DC source.
- One of the channels is shorted to a GND source.
- Two input channels have shorted together.
- One or both output channels have an overcurrent condition.

An input fault can also occur if one of the channels in a dual-channel system changed state after a 3-second discrepancy time interval, and if the inputs are configured with one of these settings:

- Dual-channel equivalent 3 s
- Dual-channel complementary 3 s
- Dual-channel SS equivalent 3 s

Faults fall into one of three categories: Stop Category fault, Fault While Stopping fault, and Safe State fault. Stop Category faults can be Motion faults, Monitor faults, or I/O faults.

The safety configuration tool can display a fault history queue that provides a record of the faults detected by the drive. The fault history queue stores the fault codes and timestamps for the last 10 faults that occurred.

These tables list the faults, fault codes, and display text for each fault. You can view these faults by accessing the [Fault Status] parameter.

Table 33 - Safe State Faults

| Code  Display Text  Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SAFE FLT 00... RESERVED  Reserved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SAFE FLT 01... INTERNAL HDWR nn (1)  A nonrecoverable microprocessor error has occurred.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SAFE FLT 02... INVALID CONFIG An Invalid Configuration fault occurs if a configuration parameter is set to an illegal value or combination of values. See the Configuration Fault Codes on page 141 .                                                                                                                                                                                                                                                                                                                                                                                                                     |
| SAFE FLT 03... MP OUT nn (1)  An MP Output fault occurs if an internal error is detected in the circuit that removes motion producing power from the drive terminals.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| SAFE FLT 04... RESET AT POWERUP A Reset Powerup fault occurs if the reset type is configured for Manual or Manual Monitored and the Reset_In input is detected as ON when power is cycled.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SAFE FLT 05... FEEDBACK 1  A Feedback 1 fault occurs if any of these conditions are detected at encoder 1:  •  An open wire is detected. •  A short-circuit is detected. •  A sine/cosine fault exists, that is the amplitude of the sine signal squared plus the amplitude of the cosine signal squared is not equal to a constant value. •  The feedback signals indicate a frequency greater than or equal to 100 kHz for a Sine/cosine encoder or 200 kHz for a incremental encoder. •  Illegal encoder signal transitions are detected. •  Incorrect Overspeed Response Time setting (refer to Table 15 on page 47). |
| SAFE FLT 06... FEEDBACK 2 A Feedback 2 fault occurs if any of these conditions are detected at encoder 2: •  Illegal encoder signal transitions are detected. •  The feedback signals indicate a frequency greater than or equal to 200 kHz.                                                                                                                                                                                                                                                                                                                                                                              |
| SAFE FLT 07... DUAL FB SPEED A Dual Feedback Speed fault occurs if an error is detected between the speed from the first encoder and the speed from the second encoder. Valid speed-comparison values are determined by the configured Feedback Speed Ratio and Feedback Speed Tolerance.                                                                                                                                                                                                                                                                                                                                 |
| SAFE FLT 08... DUAL FB POSITION A Dual Feedback Position fault occurs if a discrepancy is detected between the relative position change of encoder 1 and the relative position change of encoder 2 since the last SS Reset.                                                                                                                                                                                                                                                                                                                                                                                               |
| SAFE FLT 13... MOTION AFTER STOP If the drive is configured for a stop type that includes stopped speed checking, a Motion After Stop fault occurs if either of the following is detected after the system is stopped and the door has been unlocked: •  Speed greater than the configured Standstill Speed •  A position change greater than the configured Standstill Position limit                                                                                                                                                                                                                                    |
| SAFE FLT 27... ENCODER 1 VOLTAGE An Encoder 1 Voltage fault occurs if the encoder voltage at encoder 1 is detected as out of range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SAFE FLT 28... ENCODER 2 VOLTAGE An Encoder 2 Voltage fault occurs if the encoder voltage at encoder 2 is detected as out of range.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SAFE FLT 30... RESERVED Reserved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SAFE FLT 31... RESERVED Reserved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

Table 34 - Fault While Stopping Faults

| Code  Display Text        | Description                                                                                                                                                                                                                                                                                                                   |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           | SAFE FLT 11... DECELERATION A Deceleration fault occurs if the speed is detected at greater than the limit specified for the configured Stop Delay [Maximum Stop Time] when the configured Stop Category is Safe Stop 1 or 2.                                                                                                 |
| SAFE FLT 12... STOP SPEED | A Stop Speed fault occurs when the drive is configured for a Stop Category that includes Standstill Speed checking (Safe Stop 1 or 2, and Safe Torque Off with Standstill Speed Checking) and the detected speed is greater than the configured Standstill Speed at the end of the configured Stop Delay [Maximum Stop Time]. |

Table 35 - Stop Category Faults

| Code  Display Text                     | Description    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SAFE FLT 09... SS IN nn (1)            | I/O Faults (2) | An SS_In fault occurs if an error is detected in the SS_In dual-channel input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SAFE FLT 10... SS OUT nn (1)           | I/O Faults (2) | An SS_Out fault occurs if an error is detected in the SS_Out dual-channel output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                        | I/O Faults (2) | SAFE FLT 14... SLS IN An SLS_In fault occurs if an error is detected in the SLS_In dual-channel input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                        | I/O Faults (2) | SAFE FLT 15... SLS OUT An SLS_Out fault occurs if an error is detected in the SLS_Out dual-channel output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                        | I/O Faults (2) | SAFE FLT 20... DM IN A DM_In fault occurs if an error is detected in the DM_In dual-channel input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                        | I/O Faults (2) | SAFE FLT 22... DC OUT A DC_Out fault occurs if an error is detected in the DC_Out dual-channel output.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                        | I/O Faults (2) | SAFE FLT 23... LM IN An LM_In fault occurs if an error is detected in the LM_In dual-channel input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                        | I/O Faults (2) | SAFE FLT 25... ESM IN An ESM_In fault occurs if an error is detected in the ESM_In dual-channel input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SAFE FLT 16... SLS SPEED Motion        | Faults         | The monitored speed was detected at greater than or equal to the Safe Speed Limit during Safe Limited Speed monitoring.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                        | Faults         | SAFE FLT 17... SMS SPEED A Safe Maximum Speed fault indicates that Safe Maximum Speed (SMS) monitoring is enabled and the monitored speed was detected at greater than or equal to the configured Safe Max Speed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                        | Faults         | SAFE FLT 18... ACCELERATION An Acceleration fault indicates that the monitored speed was detected as greater than or equal to the configured Safe Accel Rate during safe acceleration monitoring.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SAFE FLT 19... DIRECTION               | Faults         | A Direction fault indicates that motion was detected in the restricted direction during safe direction monitoring (SDM).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SAFE FLT 21... DOOR MONITORING Monitor | Fault          | If the drive is configured for Safe Limited Speed (SLS), but SLS monitoring is not active, the DM_In input must be ON (door closed) or a Door Monitoring fault occurs. A Door Monitoring fault occurs if the door is open (DM_In input is OFF) when an SS Reset or SLS Reset is requested (SLS_In transitions to ON). If a configured SLS Monitoring Delay [Safe Limited Speed Monitor Delay] is in progress prior to Safe Limited Speed monitoring being active and the DM_In input is OFF (door open), a Door Monitoring fault occurs. If the drive is configured for door monitoring and enabling switch monitoring and is actively monitoring safe limited speed, a Door Monitoring fault occurs if the DM_In input transitions from ON to OFF (door is opened), while the ESM_In input is OFF.                              |
| SAFE FLT 26... ESM MONITORING          | Fault          | If the drive is configured for enabling switch monitoring and is actively monitoring safe limited speed, the ESM_In input must be ON or an ESM Monitoring fault occurs. If the drive is only configured for enabling switch monitor, and a configured SLS monitoring delay [Lim Spd Mon Delay] is in progress, the ESM_In input must be ON when the delay times out or an ESM Monitoring fault occurs. If the ESM_In input is ON while the drive is actively monitoring safe limited speed, the door can be opened (DM_In transitions from ON to OFF) if no Lock Monitoring fault exists. However, if the ESM_In input transitions to OFF after the door has been opened, an ESM Monitoring fault occurs. If you attempt an SS Reset while the SLS_In input is OFF and the ESM_In input is OFF, an ESM Monitoring fault  occurs. |
| SAFE FLT 24... LOCK MONITORING         | Fault          | If the drive is configured for lock monitoring, a Lock Monitoring fault occurs when:  •  the LM_In input is detected as OFF while the door control output is in the Lock state, except for the 5 seconds following the transition of the DC_Out output from Unlock to Lock. •  the LM_In input is detected as ON when the DM_In signal transitioned from ON to OFF.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Fault Reactions

When a fault occurs, the type of fault and the status of the system determine the resulting state of the system.

## Safe State Faults

If a Safe State fault occurs in any operational state including the Disabled state, the drive goes to the Safe State. In the Safe State, all safety outputs are in their safe states.

## Stop Category Faults and Fault While Stopping Faults

If a Stop Category fault or Fault While Stopping fault occurs while the drive is monitoring motion, the drive initiates the configured Stop Category.

The type of fault detected determines the drive's response when the fault occurs while the drive is executing the configured Stop Category.

| Type of Fault Detected                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Response                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fault While Stopping Faults: •  Deceleration fault •  Stop Speed fault These Stop Category Faults: •  SMS Speed fault when the [Safe Maximum Speed Monitoring Stop Behavior] is configured for Use Safe Torque Off with Check for Standstill •  Acceleration fault when the [Safe Maximum Acceleration Monitoring Stop                                                                                                                                                                                                                                                             | Outputs are placed in a faulted state, but door control logic can be set to Unlock if feedback signals indicate that Standstill Speed has been reached. The drive continues to monitor for faults. |
| Behavior] is configured for Use Safe Torque Off with Check for Standstill •  Direction fault, if the fault occurred while a safe stop was in progress.                                                                                                                                                                                                                                                                                                                                                                                                                             | Outputs are placed in a faulted state, but door control logic can be set to Unlock if feedback signals indicate that Standstill Speed has been reached. The drive continues to monitor for faults. |
| These Stop Category faults: •  SLS Speed fault •  Direction fault, if the fault was detected before the safe stop was initiated. In this case, the drive does not perform Direction Monitoring while executing the configured Stop Category. •  Door Monitoring fault •  ESM Monitoring fault •  Lock Monitoring fault •  SMS Speed fault when the [Safe Maximum Speed Monitoring Stop Behavior] is configured for Use Configured Stop Category •  Acceleration fault when the [Safe Maximum Acceleration Monitoring Stop Behavior] is configured for Use Configured Stop Category | The drive continues to execute the configured Stop Category and monitor for faults.                                                                                                                |

## Status Attributes

Table 36 - Guard Status Attributes

| Bit  Display Text Axis 1.    | Description                                                                                                                                                                                                                                                                                                                               |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                              | 0 GuardOKStatus This bit indicates when there are no faults. It is set (1), when all of the Fault Status bits 1…31 are 0 (no faults). The bit is 0 if any Fault Status bit from 1…31 indicates a fault (1).                                                                                                                               |
| 1 GuardConfig LockedStatus   | This bit shows the status of the [Safety Lock Status] parameter. A 1 indicates the configuration is locked; a 0 indicates the configuration is unlocked.                                                                                                                                                                                  |
| 2 GuardGateDrive OutputSatus | This bit shows the status of the drive’s Motion Power command to the drive. A 1 indicates Motion Power is enabled; a 0 indicates Motion Power is disabled.                                                                                                                                                                                |
| 3 GuardStopInput Status      | This bit displays the logical value, 1 or 0, evaluated for the dual-channel SS_In input.                                                                                                                                                                                                                                                  |
| 4 GuardStop RequestStatus    | This bit is set to 1 when a safe stop is initiated by either a transition of the SS_In input from ON to OFF or by a Stop Category fault. This bit is reset to 0 when a successful SS Reset occurs and when the Operation mode is set to Disabled (0).                                                                                     |
| 5 GuardStop InProgressStatus | This bit is set to 1 when a safe stop is initiated by the transition of the SS_In input from ON to OFF with no active fault conditions. It is not set to 1 when a Safe Stop is initiated by a Stop Category fault. While set to 1, this bit is reset (0) if Standstill Speed is reached or any fault condition is detected.               |
| 6 GuardStop DecelStatus      | This bit is set to 1 if the configured Stop Delay [Maximum Stop Time] is active for a Safe Stop 1 or Safe Stop 2 while the drive is executing the Safe Stop. This bit is not set during a Category 0 Safe Torque Off Safe Stop. This bit is reset (0) when Standstill Speed is detected, a Safe State fault occurs, or a SS Reset occurs. |
| 7 GuardStop StandstillStatus | This bit is set to 1 if a successful Safe Stop has been executed and the speed is less than or equal to the Standstill Speed. This bit is set to 0 by an SS Reset or the occurrence of a Stop Category fault. It is always 0 when the drive is configured for a Safe Torque Off without Standstill Speed Checking.                        |

If outputs are already in a faulted state due to a previous fault, and a subsequent Stop Category fault or Fault While Stopping fault occurs, outputs remain in a faulted state, door control logic can be set to Unlock if feedback signals indicate that Standstill Speed has been reached, and the drive continues to monitor for faults.

If a Stop Category fault or Fault While Stopping fault occurs after Standstill Speed has been reached and the drive has set door control logic to Unlock, the drive goes to the Safe State.

<!-- image -->

ATTENTION: If a fault occurs after Standstill Speed has been reached, door control logic remains unlocked.

A Safe State fault can set the Door Control output (DC\_Out) to OFF.

For diagnostic purposes, you can only view status attributes by accessing the AxisServoDrive.GuardStatus tag in the Logix Designer application.

## Guard Status Attributes

These attributes are stored in the AxisServoDrive.GuardStatus tag. Each bit corresponds to a different attribute.

## Table 36 - Guard Status Attributes (continued)

| Bit  Display Text Axis 1.                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 8 GuardStop OutputStatus                     | This bit is set to 1 if the dual-channel SS_Out output is being commanded to the ON state. This bit is the commanded value, not a readback value. This bit is set to 0 if the SS_Out output is being commanded to the OFF state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 9 GuardLimited SpeedInputStatus              | This bit reflects the logical value evaluated for the dual-channel SLS_In input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 10 GuardLimited SpeedRequestStatus           | This bit is set to 1, if the Safe Limited Speed operation has been requested while the drive is actively monitoring motion or a SLS Monitoring Delay is in progress.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 11 GuardLimitedSpeed MonitorInProgressStatus | This bit is set to 1 when Safe Limited Speed monitoring is active.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 12 GuardLimitedSpeed OutputStatus            | This bit is set to 1 if the dual-channel SLS_Out output is being commanded to the ON state. This bit is the commanded value, not a readback value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 13 GuardMaxSpeedMonitor InProgressStatus     | This bit is set to a 1, if Safe Maximum Speed monitoring is enabled and Safe Maximum Speed is being monitored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 14 GuardMaxAccelMonitor InProgressStatus     | This bit is set to 1, if Safe Maximum Acceleration monitoring is enabled and safe maximum acceleration is actively being monitored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 15 GuardDirectionMonitor InProgressStatus    | If Safe Direction monitoring is enabled and configured for Positive Always or Negative Always, the SDM_In_Progress bit is set to 1 any time the drive is configured for any Operation mode other than Disabled. If Safe Direction monitoring is enabled and configured for Positive During SLS or Negative During SLS, then this bit is set to 1 if the drive is actively monitoring for Safe Limited Speed. It is set to 0 in any other operating mode.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 16 GuardDoorControl LockStatus               | This bit is set to 1 if door control logic status is Lock. This bit is set to 0 if door control logic status is Unlock.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 17 GuardDoorControl OutputStatus             | This bit is set to 1 if the dual-channel DC_Out output is being commanded to the ON state. This is the commanded value, not the readback value. This bit is set to 0, if the dual-channel DC_Out output is being commanded to the OFF state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 18 GuardDoorMonitor InputStatus              | This bit is set to 1 if the logical value of the dual-channel DM_In input is evaluated as 1. This bit is set to 0 if the logical value of the dual-channel DM_In input is evaluated as 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 19 GuardDoorMonitor InProgressStatus         | The status of this bit is dependent on the drive’s speed monitoring configuration. The bit is 1 when:  •  the drive is configured for Safe Stop with Door Monitoring and is monitoring motion, or is executing a Safe Stop. •  the drive is configured for Safe Limited Speed with Door Monitoring and the drive is not actively monitoring for Safe Limited Speed, is in a SLS Monitoring Delay, or is executing a Safe Stop. •  the drive is configured for Safe Limited Speed with Door Monitoring and Enabling Switch Monitoring, and –  the drive is not actively monitoring for Safe Limited Speed, is in a SLS Monitoring Delay, or is executing a Safe Stop.  –  the drive is actively monitoring for Safe Limited Speed when the ESM_In input is OFF and the DM_In input is ON. This bit is always set to 0 when the drive is not configured for Door Monitoring. |
| 20 GuardLockMonitor InputStatus              | This bit is set to 1 if the logical value of the dual-channel LM_In input is evaluated as 1. This bit is set to 0 if the logical value of the dual-channel LM_In input is evaluated as 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 21 GuardEnablingSwitch InputStatus           | This bit is set to 1 if the logical value of the dual-channel ESM_In input is evaluated as 1. This bit is set to 0 if the logical value of the dual-channel ESM_In input is evaluated as 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 22 GuardEnablingSwitch InProgressStatus      | This bit is set to 1 if the Operation mode is configured for Enabling Switch Monitoring, Safe Limited Speed monitoring is active, and the SLS_In input is OFF. It is also set to 1 if the Operation mode is configured for Enabling Switch Monitoring and Door Monitoring and the DM_In input is OFF. This bit is set to 0 when the Operation mode is not configured for Enabling Switch Monitoring.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                              | 23 GuardResetInputStatus This status bit reflects the state of the Reset_In input. A 1 indicates the Reset_In input is ON; a 0 indicates the Reset_In input is OFF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 24 GuardReset RequiredStatus                 | This bit indicates when an SS Reset is required. The bit is set to 1 whenever the drive is successfully configured and is in the Safe State or when Standstill Speed has been reached.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 25 GuardStopInputCycle RequiredStatus        | This bit indicates when the SS_In input must be cycled prior to a SS Reset being performed. The bit is set to 1 if the SS_In input is ON and a fault is detected or the Wait Stop Request attribute equals 1. It is set to 0 if the SS_In input is detected as OFF.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 26 Reserved                                  | 26 Reserved                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## I/O Diagnostic Status Attributes

These attributes are accessible through the safety configuration tool under the Diagnostics folder, Monitor Signals tab.

Table 37 - Safety Input Signal Status

| Safety Inputs Value   |                       |
|-----------------------|-----------------------|
|                       | SS Input 0 False/True |
|                       | SS Input 1 False/True |
| SLS Input 0           | False/True            |
| SLS Input 1           | False/True            |
| DM Input 0            | False/True            |
| DM Input 1            | False/True            |
| LM Input 0            | False/True            |
| LM Input 1            | False/True            |
| ESM Input 0           | False/True            |
| ESM Input 1           | False/True            |
| Reset Input           | False/True            |

Table 38 - Safety Output Signal Status

| Safety Outputs Value   |            |
|------------------------|------------|
| SS Output 0            | False/True |
| SS Output 1            | False/True |
| SLS Output 0           | False/True |
| SLS Output 1           | False/True |
| DC Output 0            | False/True |
| DC Output 1            | False/True |

## Configuration Fault Codes

Use these fault codes to identify the reason for an Invalid Configuration fault.

| Fault Code Description                                                                                      |
|-------------------------------------------------------------------------------------------------------------|
| 0 No fault .                                                                                                |
| 2  [Operation Mode] value not legal based on [System Configuration] value.                                  |
| 5  [Control Output] value not legal based on [System Configuration] value.                                  |
| 7  [Safe Stop Monitor Delay] value not legal based on [Stop Category] value.                                |
| 9  [Deceleration Reference Speed] value not legal based on [Primary Feedback Cycles] value.                 |
| 11 [Standstill Speed] value not legal based on [System Configuration] value.                                |
| 13 [Safe Limited Speed Monitor Delay] value not legal based on [Operation Mode] value.                      |
| 14 [Safe Speed Limit] value not legal based on [Operation Mode] or [Primary Feedback Cycles] value.         |
| 15 [Safe Limited Speed Hysteresis] value not legal based on [Operation Mode] value.                         |
| 17 [Safe Maximum Speed Limit] value not legal based on [Primary Feedback Cycles] value.                     |
| 22 [Enable Safe Direction Monitoring] value not legal based on [Operation Mode] value.                      |
| 24 [Enable Lock Monitoring] value not legal based on [Operation Mode] value.                                |
| 28 [Secondary Feedback Resolution] value not legal based on [Feedback Mode] value.                          |
| 30 [Secondary Feedback Polarity] value not legal based on [Feedback Mode] value.                            |
| 33 [Velocity Ratio] value not legal based on [Feedback Mode] value.                                         |
| 34 [Position Discrepancy Tolerance] value not legal based on [Feedback Mode] value.                         |
| 35 [Velocity Discrepancy Tolerance] value not legal based on [Feedback Mode] value.                         |
| 38 [Safe Stop] value not legal based on [Operation Mode] value.                                             |
| 39 [Safe Limited Speed] value not legal based on [Operation Mode] value.                                    |
| 40 [Door Monitor] value not legal based on [System Configuration] and [Operation Mode] value.               |
| 41 [Enable Switch Monitor] value not legal based on [Operation Mode] value.                                 |
| 42 [Lock Monitor Input] value not legal based on [Operation Mode] value and [Enable Lock Monitoring] value. |
| 1001 Illegal [System Configuration] value.                                                                  |
| 1003 Illegal [Reset Type] value.                                                                            |
| 1004 Reserved.                                                                                              |
| 1006 Illegal [Safe Stop Category] value.                                                                    |
| 1010 Illegal [Stop Deceleration Tolerance] value.                                                           |
| 1025 Illegal [Feedback Mode] value.                                                                         |
| 1026 Illegal [Primary Feedback Type] value.                                                                 |
| 1027 Illegal [Primary Feedback Cycles] value.                                                               |
| 1031 Illegal [5V Monitoring] value.                                                                         |
| 1032 Illegal [9V Monitoring] value.                                                                         |
| 1036 Illegal [Over Speed Response Time] value.                                                              |
| 1088 Reserved.                                                                                              |

## Configuration Fault Example

Configuration faults are not displayed on the drive. However, you can use the Safety Configuration Tool to access the fault code. Press Apply to see if a configuration fault exists.

In this configuration fault example, an invalid Velocity Ratio setting caused Configuration Fault 33. Refer to the table on page 141 for a complete list of all configuration fault codes and descriptions.

Figure 51 - Feedback Tab - Configuration Fault 33

<!-- image -->

## General Specifications

## Specifications

This appendix provides product specifications for the safe speed monitoring safety functions.

| Topic                  |   Page |
|------------------------|--------|
| General Specifications |    143 |
| Certifications         |    144 |
| Encoder Specifications |    144 |

These specifications apply to the safe speed monitoring safety functions.

Table 39 - Safety Specifications

| Attribute                                         | Value                                                                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Standards                                         | IEC/EN60204-1, ISO12100, IEC 61508, IEC 61800-5-2                                                                                                |
| Safety category                                   | Cat. 4 and PLe per EN ISO 13849-1; SIL CL3 per IEC 61508 and EN 62061                                                                            |
| Power supply (user I/O)                           | 21.6…28.8V DC (24V nom), 0.9…1.2 x rated voltage  (1) PELV or SELV 1.35 A, max                                                                   |
| Power consumption 36 W                            |                                                                                                                                                  |
|                                                   | SLS outputs 24V DC, 20 mA, short-circuit protected  (2)                                                                                          |
| SS outputs                                        | 24V DC, 20 mA, short-circuit protected  (2)                                                                                                      |
| Door control outputs                              | 24V DC, short-circuit protected •  0.75 A, bipolar (Power to Release/Power to Lock) configuration •  20 mA, cascading (2Ch Source) configuration |
| Pulse outputs                                     | 24V DC, 30 mA, short-circuit protected                                                                                                           |
| Safety inputs SS_In, SLS_In, ESM_In, DM_In, LM_In | 5 mA per input, max                                                                                                                              |
| Input ON Voltage, min 16.5V                       |                                                                                                                                                  |
| Input OFF Voltage, max 5V                         |                                                                                                                                                  |
| Input OFF Current, max 2 mA                       |                                                                                                                                                  |
| Input-to-output response time 20 ms               |                                                                                                                                                  |
| Overspeed Response Time User-configurable         |                                                                                                                                                  |
| Reset_In Input                                    | 5 mA per input, max                                                                                                                              |
| Reset time, max  (3)                              | 400 ms per axis                                                                                                                                  |

<!-- image -->

## Certifications

## Encoder Specifications

Table 40 - Terminal Wiring Specifications

| Attribute          | Value                                               |
|--------------------|-----------------------------------------------------|
| Conductor size (1) | 0.25…0.75 mm 2 (24…18 AWG)                          |
| Strip length       | 5 mm (0.25 in.)                                     |
|                    | Terminal screw torque 0.22…0.25 N•m (1.9…2.2 lb•in) |

See the Product Certification link at http://www.ab.com for Declarations of Conformity, Certificates, and other certifications details.

| Agency Certification  (1)   | Value                                                                                                                                                                                                                                                                                                                  |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| c-UL-us (2)                 | UL Listed, certified for US and Canada.                                                                                                                                                                                                                                                                                |
| CE                          | European Union 2004/108/EC EMC Directive, compliant with: •  EN 61800-3; categories C2 and C3 •  EN 62061; EM Immunity                                                                                                                                                                                                 |
| C-Tick                      | Australian Radiocommunications Act, compliant with: EN 61800-3; categories C2 and C3                                                                                                                                                                                                                                   |
| Functional Safety           | Certified by TÜV for Functional Safety: up to SIL CL3, according to EN 61800-5-2, EN 61508, and EN 62061; up to Performance Level PLe and Category 4, according to EN ISO 13849-1; when used as described in this Kinetix 6200 and Kinetix 6500 Safe Speed Monitoring Safety Reference Manual, publication 2094-RM001. |

Use Belden 9728 cable with the following encoder specifications.

|                  | Type Parameter                         | Description                                      |
|------------------|----------------------------------------|--------------------------------------------------|
| Incremental      | Incremental encoder support            | 5 and 9V, differential A quad B                  |
| Incremental      | Differential input voltage (AM and BM) | 1.0…7.0V                                         |
| Incremental      | High threshold level, min              | 3.5V                                             |
| Incremental      | Generic Low threshold level, max       | 0.4V                                             |
| Incremental      | DC current draw (AM and BM)            | 60 mA, max                                       |
| Incremental      | Input signal frequency (AM and BM)     | 200 kHz, max                                     |
| Incremental      | Cable length, max                      | 30.5 m (100 ft) max cable length with 5V encoder |
| Generic Sin/Cos  | AM/BM input frequency                  | 100 kHz, max                                     |
| Generic Sin/Cos  | AM/BM differential input voltage (p-p) | 0.6…1.2V                                         |
| Stegmann Sin/Cos | AM/BM input frequency                  | 100 kHz, max                                     |
| Stegmann Sin/Cos | AM/BM differential input voltage (p-p) | 1V ±10%                                          |

## Parameter Groups

## Parameter Data

This appendix provides a description of the safety parameters and safety attributes.

Safety parameters are organized into a linear list under the Safety Main and Safety Configuration categories.

<!-- image -->

<!-- image -->

## Parameters and Settings in a Linear List

Table 41 - Configurable Parameters and Settings

| Tab                                 | Parameter Name Description   |                                                                                                                                                      | Values (Safety Configuration Tool)                                                                                                                                                                                                            |
|-------------------------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Main Commands                |                              | Password Safety configuration password is optional, but once set is required to use Safety Main tab commands.                                        | Range: N/A                                                                                                                                                                                                                                    |
| Safety Main Commands                |                              | Safety Lock Status Status indicator for the safety configuration lock/unlock status.                                                                 | Default: Unlocked                                                                                                                                                                                                                             |
| Safety Main Commands                |                              | Safety Lock Status Status indicator for the safety configuration lock/unlock status.                                                                 | Options: Unlocked Locked                                                                                                                                                                                                                      |
| Safety Main Configuration Signature | Configuration Signature ID   | Safety configuration identifier (read only). Signature ID is written when the Apply command is used successfully.                                    | Range: N/A                                                                                                                                                                                                                                    |
| Safety Change System Configuration  |                              | System Configuration Defines whether the drive is a single unit or if it occupies a first, middle, or last position in a multi-axis cascaded system. | Default: Single Unit                                                                                                                                                                                                                          |
| Safety Change System Configuration  |                              | System Configuration Defines whether the drive is a single unit or if it occupies a first, middle, or last position in a multi-axis cascaded system. | Options: Single Unit Cascaded First Unit Cascaded Middle Unit Cascaded Last Unit                                                                                                                                                              |
| Safety Change System Configuration  |                              | Operation Mode Defines the primary operating mode of the speed monitoring safety functions.                                                          | Default: SafeStop                                                                                                                                                                                                                             |
| Safety Change System Configuration  |                              | Operation Mode Defines the primary operating mode of the speed monitoring safety functions.                                                          | Options: Disabled SafeStop SafeStop-DoorMonitor SafeStop-SafeLimitedSpeed SafeStop-SafeLimitedSpeed-DoorMonitor SafeStop-SafeLimitedSpeed-EnableSwitch SafeStop-SafeLimitedSpeed-DoorMonitor-EnableSwitch SafeStop-SafeLimitedSpeedStatusOnly |
| Safety Change System Configuration  |                              | Reset Type Defines the type of reset used by the drive. Default: Manual Monitored                                                                    |                                                                                                                                                                                                                                               |
| Safety Change System Configuration  |                              | Reset Type Defines the type of reset used by the drive. Default: Manual Monitored                                                                    | Options: Automatic Manual Manual Monitored                                                                                                                                                                                                    |
| Safety Change System Configuration  |                              | Door Control Output Defines the lock and unlock state for door control output (DC_Out). Any Door Control Output option can be used for a             | Default: Power to Release                                                                                                                                                                                                                     |
| Safety Change System Configuration  |                              | single-axis system or for the last unit in a multi-axis system. The first and middle units of a multi-axis system                                    | Options: Power to Release Power to Lock 2 Channel Sourcing                                                                                                                                                                                    |
| Safety Change System Configuration  | Enable Lock Monitoring       | Lock Monitoring can be enabled only when the drive is a single unit or as the first unit in a multi-axis system as set in [System Configuration].    | Default: Lock Monitoring Not Enabled                                                                                                                                                                                                          |
| Safety Change System Configuration  | Enable Lock Monitoring       | Lock Monitoring can be enabled only when the drive is a single unit or as the first unit in a multi-axis system as set in [System Configuration].    | Options: Lock Monitoring Not Enabled Lock Monitoring Enabled                                                                                                                                                                                  |
| Safety Change System Configuration  | Overspeed Response Time      | Configuration for the feedback interface sampling rate. Default: 42 ms                                                                               |                                                                                                                                                                                                                                               |
| Safety Change System Configuration  | Overspeed Response Time      | Configuration for the feedback interface sampling rate. Default: 42 ms                                                                               | Options: 42 ms 48 ms 60 ms 84 ms 132 ms 228 ms 420 ms                                                                                                                                                                                         |

This table lists the configurable parameters and their valid settings. If any values other than those listed in the table are configured for any of the parameters, an Invalid Configuration fault occurs.

Table 41 - Configurable Parameters and Settings (continued)

| Tab                                    | Parameter Name Description                                                                                                                                     | Values (Safety Configuration Tool)                                                                                                                                               |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Feedback Change Feedback Configuration | Feedback Mode Selects the number of feedback devices and the type of discrepancy checking.                                                                     | Default: Single Encoder                                                                                                                                                          |
| Feedback Change Feedback Configuration | Feedback Mode Selects the number of feedback devices and the type of discrepancy checking.                                                                     | Options: Single Encoder Dual Encoders w/speed and position discrepancy Dual Encoders w/speed discrepancy Dual Encoders w/position discrepancy                                    |
| Feedback Change Feedback Configuration | 5V Monitoring Enable 5V monitoring. Default: Voltage not monitored                                                                                             |                                                                                                                                                                                  |
| Feedback Change Feedback Configuration | 5V Monitoring Enable 5V monitoring. Default: Voltage not monitored                                                                                             | Options: Voltage not monitored Voltage monitored                                                                                                                                 |
| Feedback Change Feedback Configuration |                                                                                                                                                                | 9V Monitoring Enable 9V monitoring. Default: Voltage not monitored                                                                                                               |
| Feedback Change Feedback Configuration |                                                                                                                                                                | Options: Voltage not monitored Voltage monitored                                                                                                                                 |
| Feedback Primary Feedback              | Type Selects the type of feedback for encoder 1. Default: Sin/Cos                                                                                              |                                                                                                                                                                                  |
| Feedback Primary Feedback              | Type Selects the type of feedback for encoder 1. Default: Sin/Cos                                                                                              | Options: Sin/Cos TTL (incremental)                                                                                                                                               |
| Feedback Primary Feedback              | Cycles Defines counts (linear) or revolutions (rotary) for encoder 1.                                                                                          | Default: 1024                                                                                                                                                                    |
| Feedback Primary Feedback              | Cycles Defines counts (linear) or revolutions (rotary) for encoder 1.                                                                                          | Range: 1 … 65,535 pulses/revolution or pulses/mm based on the [Primary Feedback Units] parameter                                                                                 |
| Feedback Primary Feedback              | Units Selects millimeters or revolutions for encoder 1. Default: Revolutions (per Rev)                                                                         |                                                                                                                                                                                  |
| Feedback Primary Feedback              | Units Selects millimeters or revolutions for encoder 1. Default: Revolutions (per Rev)                                                                         | Options: Revolutions (per Rev) Millimeters (per mm)                                                                                                                              |
| Feedback Primary Feedback              | Feedback Polarity Defines the direction polarity for encoder 1. Default: Positive                                                                              |                                                                                                                                                                                  |
| Feedback Primary Feedback              | Feedback Polarity Defines the direction polarity for encoder 1. Default: Positive                                                                              | Options: Positive Negative                                                                                                                                                       |
| Feedback Secondary  (1) Feedback       | Cycles Defines counts (linear) or revolutions (rotary) for encoder 2.                                                                                          | Range: 1 … 65,535 pulses/revolution or pulses/mm based on the [Secondary Feedback Units] parameter                                                                               |
| Feedback Secondary  (1) Feedback       | Units  Selects millimeters or revolutions for encoder 2. Options: Revolutions (per Rev)                                                                        | Millimeters (per mm)                                                                                                                                                             |
| Feedback Secondary  (1) Feedback       | Feedback Polarity Defines the direction polarity for encoder 2. Options: Positive                                                                              | Negative                                                                                                                                                                         |
| Feedback Dual Feedback                 | Velocity Ratio Defines the ratio of the expected speed of encoder 2 divided by the expected speed of encoder 1. Not valid when Feedback Mode = Single Encoder. | Range: 0.0001 … 10,000.0 ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                               |
| Feedback Dual Feedback                 | Velocity Discrepancy Tolerance Dual Feedback Speed Discrepancy Tolerance. Range: 0…6553.5 rpm or mm/s                                                          | ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                                                        |
| Feedback Dual Feedback                 | Position Discrepancy Tolerance Acceptable difference in position between encoder 1 and encoder 2.                                                              | Range: 0…65,535 deg or mm ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                              |
| Input Change Input Configuration Type  | Safe Stop Configuration for Safe Stop input (SS_In). Default: Dual Channel Equivalent                                                                          |                                                                                                                                                                                  |
| Input Change Input Configuration Type  | Safe Stop Configuration for Safe Stop input (SS_In). Default: Dual Channel Equivalent                                                                          | Options: Not Used Dual Channel Equivalent Dual Channel Equivalent 3 s Dual Channel Complementary Dual Channel Complementary 3 s Solid State Device Equivalent 3 s Single Channel |

Table 41 - Configurable Parameters and Settings (continued)

| Tab                                                        | Parameter Name Description       |                                                                                                                                                                                                                                                                                                                                                        | Values (Safety Configuration Tool)                                                                                                                              |
|------------------------------------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input Change Input Configuration Type                      |                                  | Door Monitor Configuration for the Door Monitor input (DM_In). Default: Not Used                                                                                                                                                                                                                                                                       |                                                                                                                                                                 |
| Input Change Input Configuration Type                      |                                  | Lock Monitor Configuration for the Lock Monitor input (LM_In). Options: Not Used                                                                                                                                                                                                                                                                       |                                                                                                                                                                 |
| Input Change Input Configuration Type                      |                                  | Safe Limited Speed Configuration for the Safe Limited Speed input (SLS_In).                                                                                                                                                                                                                                                                            | Dual Channel Equivalent Dual Channel Equivalent 3 s Dual Channel Complementary                                                                                  |
| Input Change Input Configuration Type                      | Enabling Switch Monitor          | Configuration for the Enabling Switch input (ESM_In).                                                                                                                                                                                                                                                                                                  | Dual Channel Complementary 3 s Solid State Device Equivalent 3 s Single Channel                                                                                 |
| Safe Stop Change Safe Stop Configuration                   |                                  | Stop Category Safe operating stop type selection. This defines the type of Safe Stop that is performed if the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                | Default: Safe Torque-Off                                                                                                                                        |
| Safe Stop Change Safe Stop Configuration                   |                                  | Stop Category Safe operating stop type selection. This defines the type of Safe Stop that is performed if the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                | Options: Safe Torque-Off Safe Stop 1 Safe Stop 2                                                                                                                |
| Safe Stop Change Safe Stop Configuration                   |                                  | Enable Standstill Checking. Automatically enabled for Safe Stop 1 and Safe Stop 2.                                                                                                                                                                                                                                                                     | Default: Standstill Checking Enabled                                                                                                                            |
| Safe Stop Change Safe Stop Configuration                   |                                  | Enable Standstill Checking. Automatically enabled for Safe Stop 1 and Safe Stop 2.                                                                                                                                                                                                                                                                     | Options: Standstill Checking Enabled Standstill Checking Not Enabled                                                                                            |
| Safe Stop Change Safe Stop Configuration                   | Safe Stop Monitor Delay          | Defines the monitoring delay between the request and the Maximum Stop Time when the request for a Safe Stop 1 or a Safe Stop 2 is initiated by an SS_In input ON to OFF transition. If the Stop Category is Safe Torque-Off with or without Standstill Speed Checking, the Safe Stop Monitor Delay must be 0 or an Invalid Configuration fault occurs. | Default: 0                                                                                                                                                      |
| Safe Stop Change Safe Stop Configuration                   | Safe Stop Monitor Delay          | Defines the monitoring delay between the request and the Maximum Stop Time when the request for a Safe Stop 1 or a Safe Stop 2 is initiated by an SS_In input ON to OFF transition. If the Stop Category is Safe Torque-Off with or without Standstill Speed Checking, the Safe Stop Monitor Delay must be 0 or an Invalid Configuration fault occurs. | Range: 0 … 6553.5 s                                                                                                                                             |
| Safe Stop Change Safe Stop Configuration                   | Deceleration Reference Speed     | Determines deceleration rate to monitor for Safe Stop 1 or Safe Stop 2.                                                                                                                                                                                                                                                                                | Default: 0                                                                                                                                                      |
| Safe Stop Change Safe Stop Configuration                   | Deceleration Reference Speed     | Determines deceleration rate to monitor for Safe Stop 1 or Safe Stop 2.                                                                                                                                                                                                                                                                                | Range: 0 … 65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                         |
| Safe Stop Change Safe Stop Configuration                   |                                  | Maximum Stop Time Defines the maximum stop delay time that is used when the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                                                  | Default: 0                                                                                                                                                      |
| Safe Stop Change Safe Stop Configuration                   |                                  | Maximum Stop Time Defines the maximum stop delay time that is used when the Safe Stop function is initiated by a stop type condition.                                                                                                                                                                                                                  | Range: 0 … 6553.5 s                                                                                                                                             |
| Safe Stop Change Safe Stop Configuration                   | Deceleration Tolerance           | This is the acceptable tolerance above the deceleration rate set by the [Deceleration Reference Speed] parameter.                                                                                                                                                                                                                                      | Default: 0                                                                                                                                                      |
| Safe Stop Change Safe Stop Configuration                   | Deceleration Tolerance           | This is the acceptable tolerance above the deceleration rate set by the [Deceleration Reference Speed] parameter.                                                                                                                                                                                                                                      | Range: 0 … 100% of Deceleration Reference Speed                                                                                                                 |
| Safe Stop Change Safe Stop Configuration                   |                                  | Standstill Speed Defines the speed limit that is used to declare motion as stopped. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                                                                         | Default: 0.001                                                                                                                                                  |
| Safe Stop Change Safe Stop Configuration                   |                                  | Standstill Speed Defines the speed limit that is used to declare motion as stopped. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                                                                         | Range: 0.001 … 65.535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                     |
| Safe Stop Change Safe Stop Configuration                   | Standstill Position Window       | Defines the position limit window in encoder 1 degrees or mm that is tolerated after a safe stop condition has been detected. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                               | Default: 10                                                                                                                                                     |
| Safe Stop Change Safe Stop Configuration                   | Standstill Position Window       | Defines the position limit window in encoder 1 degrees or mm that is tolerated after a safe stop condition has been detected. Not valid for Safe Torque-Off without Standstill Checking.                                                                                                                                                               | Range: 0 … 65,535 degrees (360° = 1 revolution) or mm ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Monitor Delay | Defines the Safe Limited Speed Monitoring Delay between the SLS_In ON to OFF transition and the initiation of the Safe Limited Speed (SLS) monitoring.                                                                                                                                                                                                 | Default: 0                                                                                                                                                      |
| Safe Limited Speed Change Safe Limited Speed Configuration | Safe Limited Speed Monitor Delay | Defines the Safe Limited Speed Monitoring Delay between the SLS_In ON to OFF transition and the initiation of the Safe Limited Speed (SLS) monitoring.                                                                                                                                                                                                 | Range: 0 … 6553.5 s                                                                                                                                             |
| Safe Limited Speed Change Safe Limited Speed Configuration |                                  | Safe Speed Limit Defines the speed limit that is monitored in Safe Limited Speed (SLS) mode.                                                                                                                                                                                                                                                           | Default: 0                                                                                                                                                      |
| Safe Limited Speed Change Safe Limited Speed Configuration |                                  | Safe Speed Limit Defines the speed limit that is monitored in Safe Limited Speed (SLS) mode.                                                                                                                                                                                                                                                           | Range: 0 … 65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                         |

Table 41 - Configurable Parameters and Settings (continued)

| Tab                                                                    | Parameter Name Description                         |                                                                                                                                 | Values (Safety Configuration Tool)                                                                                                                                                                                        |
|------------------------------------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safe Limited Speed Change Safe Limited Speed Configuration (continued) | Safe Limited Speed Hysteresis                      | Provides hysteresis for SLS_Out output when Safe Limited Speed monitoring is active.                                            | Default: 0                                                                                                                                                                                                                |
| Safe Limited Speed Change Safe Limited Speed Configuration (continued) | Safe Limited Speed Hysteresis                      | Provides hysteresis for SLS_Out output when Safe Limited Speed monitoring is active.                                            | Range: 0% when [Operation Mode] = SafeStop SafeStop-DoorMonitor SafeStop-SafeLimitedSpeed SafeStop-SafeLimitedSpeed-DoorMonitor SafeStop-SafeLimitedSpeed-EnableSwitch SafeStop-SafeLimitedSpeed-DoorMonitor-EnableSwitch |
| Safe Limited Speed Change Safe Limited Speed Configuration (continued) | Safe Limited Speed Hysteresis                      | Provides hysteresis for SLS_Out output when Safe Limited Speed monitoring is active.                                            | 10 … 100% when [Operation Mode] = SafeStop-SafeLimitedSpeedStatusOnly                                                                                                                                                     |
| Safe Max Speed Change Safe Maximum Speed Configuration                 | Safe Maximum Speed Configuration                   |                                                                                                                                 | Enable Maximum Speed Monitoring. Default: Maximum Speed Monitoring Not Enabled                                                                                                                                            |
| Safe Max Speed Change Safe Maximum Speed Configuration                 | Safe Maximum Speed Configuration                   |                                                                                                                                 | Options: Maximum Speed Monitoring Not Enabled Maximum Speed Monitoring Enabled                                                                                                                                            |
| Safe Max Speed Change Safe Maximum Speed Configuration                 | Safe Maximum Speed Limit                           | Defines the maximum speed limit that is tolerated if Safe Maximum Speed (SMS) monitoring is enabled.                            | Default: 0                                                                                                                                                                                                                |
| Safe Max Speed Change Safe Maximum Speed Configuration                 | Safe Maximum Speed Limit                           | Defines the maximum speed limit that is tolerated if Safe Maximum Speed (SMS) monitoring is enabled.                            | Range: 0 … 65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                                                                   |
| Safe Max Speed Change Safe Maximum Speed Configuration                 | Safe Maximum Speed Monitoring Stop Behavior        | Defines the Stop Category that is initiated in the event of a SMS Speed fault.                                                  | Default: Use Safe Torque-Off with Check for Standstill                                                                                                                                                                    |
| Safe Max Speed Change Safe Maximum Speed Configuration                 | Safe Maximum Speed Monitoring Stop Behavior        | Defines the Stop Category that is initiated in the event of a SMS Speed fault.                                                  | Options: Use Safe Torque-Off with Check for Standstill Use Configured Stop Type                                                                                                                                           |
| Safe Max Accel Change Safe Maximum Acceleration Configuration          | Safe Maximum Acceleration Configuration            | Enable Maximum Acceleration Monitoring. Default: Maximum Acceleration Monitoring Not Enabled                                    |                                                                                                                                                                                                                           |
| Safe Max Accel Change Safe Maximum Acceleration Configuration          | Safe Maximum Acceleration Configuration            | Enable Maximum Acceleration Monitoring. Default: Maximum Acceleration Monitoring Not Enabled                                    | Options: Maximum Acceleration Monitoring Not Enabled Maximum Acceleration Monitoring Enabled                                                                                                                              |
| Safe Max Accel Change Safe Maximum Acceleration Configuration          | Safe Maximum Acceleration Limit                    | Defines the Safe Maximum Acceleration (SMA) limit, relative to encoder 1, of the system is being monitored.                     | Default: 0                                                                                                                                                                                                                |
| Safe Max Accel Change Safe Maximum Acceleration Configuration          | Safe Maximum Acceleration Limit                    | Defines the Safe Maximum Acceleration (SMA) limit, relative to encoder 1, of the system is being monitored.                     | Range: 0 … 65,535 rpm or mm/s ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                                                                   |
| Safe Max Accel Change Safe Maximum Acceleration Configuration          | Safe Maximum Acceleration Monitoring Stop Behavior | Defines the Stop Category that is initiated in the event of an SMA Acceleration fault.                                          | Default: Use Safe Torque-Off with Check for Standstill                                                                                                                                                                    |
| Safe Max Accel Change Safe Maximum Acceleration Configuration          | Safe Maximum Acceleration Monitoring Stop Behavior | Defines the Stop Category that is initiated in the event of an SMA Acceleration fault.                                          | Options: Use Safe Torque-Off with Check for Standstill Use Configured Stop Type                                                                                                                                           |
| Safe Direction Change Safe Direction Monitoring Configuration          | Safe Direction Monitoring Configuration            | Enable Safe Direction Monitoring. Default: Safe Direction Monitoring Not Enabled                                                |                                                                                                                                                                                                                           |
| Safe Direction Change Safe Direction Monitoring Configuration          | Safe Direction Monitoring Configuration            | Enable Safe Direction Monitoring. Default: Safe Direction Monitoring Not Enabled                                                | Options: Safe Direction Monitoring Not Enabled Safe Direction Monitoring Enabled                                                                                                                                          |
| Safe Direction Change Safe Direction Monitoring Configuration          |                                                    | Monitor Type Defines the monitor type if Safe Direction Monitoring is enabled.                                                  | Options: Always During Safe Limited Speed                                                                                                                                                                                 |
| Safe Direction Change Safe Direction Monitoring Configuration          |                                                    | Safe Direction Defines the allowable direction if Safe Direction Monitoring is enabled.                                         | Default: Positive                                                                                                                                                                                                         |
| Safe Direction Change Safe Direction Monitoring Configuration          |                                                    | Safe Direction Defines the allowable direction if Safe Direction Monitoring is enabled.                                         | Options: Positive Negative                                                                                                                                                                                                |
| Safe Direction Change Safe Direction Monitoring Configuration          |                                                    | Jitter Tolerance The position limit in encoder units tolerated in the wrong direction when Safe Direction Monitoring is active. | Default: 10                                                                                                                                                                                                               |
| Safe Direction Change Safe Direction Monitoring Configuration          |                                                    | Jitter Tolerance The position limit in encoder units tolerated in the wrong direction when Safe Direction Monitoring is active. | Range: 0 … 65,535 deg or mm ratio based on revolutions or millimeters configuration defined by the [Primary Feedback Units] parameter                                                                                     |

## Safety Attributes

This table lists the safety attributes as found in the Logix Designer application.

Table 42 - Logix Designer Safety Attributes

| Parameter Name Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Values (Safety Configuration Tool)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Axis 1: Guard Faults Bit-encoded faults                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | GuardInternalFault GuardConfigurationFault GuardGateDriveFault GuardResetFault GuardFeedback1Fault GuardFeedback2Fault GuardFeedbackSpeedCompareFault GuardFeedbackPositionCompareFault GuardStopInputFault GuardStopOutputFault GuardStopDecelFault GuardStopStandstillFault GuardStopMotionFault GuardLimitedSpeedInputFault GuardLimitedSpeedOutputFault GuardLimitedSpeedMonitorFault GuardMaxSpeedMonitorFault GuardMaxAccelMonitorFault GuardDirectionMonitorFault GuardDoorMonitorInputFault GuardDoorMonitorFault GuardDoorControlOutputFault GuardLockMonitorInputFault GuardLockMonitorFault GuardEnablingSwitchMonitorInputFault |
| Axis 1: Guard Status GuardOKStatus GuardConfigLockedStatus GuardGateDriveOutputSatus GuardStopInputStatus GuardStopRequestStatus GuardStopInProgressStatus GuardStopDecelStatus GuardStopStandstillStatus GuardStopOutputStatus GuardLimitedSpeedInputStatus GuardLimitedSpeedRequestStatus GuardLimitedSpeedMonitorInProgressStatus GuardLimitedSpeedOutputStatus GuardMaxSpeedMonitorInProgressStatus GuardMaxAccelMonitorInProgressStatus GuardDirectionMonitorInProgressStatus GuardDoorControlLockStatus GuardDoorControlOutputStatus GuardDoorMonitorInputStatus GuardDoorMonitorInProgressStatus GuardLockMonitorInputStatus GuardEnablingSwitchInputStatus GuardEnablingSwitchInProgressStatus GuardResetInputStatus GuardResetRequiredStatus GuardStopInputCycleRequiredStatus Reserved | 0 = Fault; 1 = OK 0 = Unlock; 1 = Lock 0 = Off; 1 = On 0 = Off; 1 = On 0 = Inactive; 1 = Active 0 = Inactive; 1 = Active 0 = Inactive; 1 = Active 0 = Inactive; 1 = Active 0 = Off; 1 = On 0 = Off; 1 = On 0 = Inactive; 1 = Active 0 = Inactive; 1 = Active 0 = Off; 1 = On 0 = Inactive; 1 = Active 0 = Inactive; 1 = Active 0 = Inactive; 1 = Active 0 = Unlock; 1 = Lock 0 = Off; 1 = On 0 = Off; 1 = On 0 = Inactive; 1 = Active 0 = Off; 1 = On 0 = Off; 1 = On 0 = Inactive; 1 = Active 0 = Off; 1 = On 0 = Inactive; 1 = Active 0 = Inactive; 1 = Active                                                                            |

## Numerics

## 2 Channel Sourcing 65

## A

## access

hazardous area 80

additional resources 12

application example 121

automatic reset 42

SLS reset 73

SS reset 64

## C

## cascaded

configuration 41 , 89

connections 35 , 37 , 39

Cat 4 11 , 13

performance definition 14

CE

comply with CE 16

conformity 16

meet requirements 16

## certification

agencies 144

Cat 4 11 , 13

EN ISO 13849-1 13

PLe 11 , 13

SIL 3 13

SIL CL3 11

commissioning the system 114-118

commutation 19

## configuration

confirm 117

lock bit 112 118

signature, see Signature ID

signature. See Signature ID.

115

example 121 lock 112 , specification summary 117

configure parameters 116

## connector kit

catalog number 24

wiring 26

## D

## DC\_Out output 38

wiring 38 , 39

deceleration monitoring 58 , 62

disabled mode 22

discrepancy checking 51

encoders 50

DM\_In input 32

documentation additional resources 12

## door control 64-65

output fault conditions 65 38

wiring door monitoring fault 82

dual channel operation 29

dual encoder configurations 50 resolution 49

## dual feedback

position discrepancy tolerance 51 speed discrepancy tolerance 52 speed ratio 51

## E

edit the configuration 116 , 118

EMC directive 16

emergency shutdown systems 13

EN 60204-1 15

EN 61508 15

EN 61508-5-2 144

EN 61800-5-2

SIL 3 certification 13

EN 62061 15

EN ISO 13849-1 13 , 14 , 15 , 144

encoder compatible 28

resolution 43

specifications 144

ESM\_In input 33 , 78

## European Norm

definition 11

## F

## fault

history queue 134 recovery 133 while stopping faults

137

## fault codes

configuration faults 141

door monitoring 82

Fault While Stopping Faults 135

input 134

nonrecoverable 133

output 134

recovery 133

Safe State Faults 135

Stop Category Faults 136

## features 24

## feedback

device types 49

49-54

54

cycles 49 fault 53 monitoring parameters polarity 49 tab 127 type 49

units 49

voltage monitor range 53

## G

guard faults, bit-encoded 150

## H

## hold last state

SLS\_Out output 85

home tab 122

## I

## I/O Diagnostic Status attributes 140 IEC EN 61508

SIL 3 certification 13

## input

faults 134

tab 128

inputs 29

IP address 111

## L

LM\_In input 33

lock monitoring 23 , 66

wiring 38

Logix Designer application 12

low voltage directive 16

## M

## manual monitored reset 42

SLS reset 73

SS Reset 64

## manual reset 42

SLS reset 73

SS Reset 64

max stop time 55

## multi-axis

configurations 89-90

connections 101 , 102

wiring 35 , 37

## O

## operation

modes 22

output faults 134

outputs

35

OverSpd Response 43

## P

## parameter list

all parameters 146-149

complete list 146

feedback 54

general 48

Max Speed and Direction Monitoring 110

Safe Limited Speed 74

Safe Limited Speed Status Only 85

Safe Stop 66

Safe Stop With Door Monitoring 69

Slave, Safe Limited Speed 96

Slave, Safe Limited Speed Status Only 99

Slave, Safe Stop 91

SLS With Door Monitoring 77

SLS With Door Monitoring and Enabling

Switch Monitoring 82

SLS With Enabling Switch Monitoring 79

## parameters

configure 116

edit 116 , 118

groups 145

## password

change 112

new 112

reset 113

data 17

definition 11 , 17

data 17

definition 11 , 17

## pinouts 27

PL 15

definition 11

PLe 11 , 13 , 144

polarity 49

power supply 26

## power to

lock 65

release 65

## probability of failure

on demand 11

per hour 11

proof tests 16

pulse test outputs 29

## R

recover from fault 133

## reset

input wiring

Reset\_In input 34

password

113

See also SS reset, SLS reset, or reset type type 42

reset type 42

Reset\_In input 73

## PFD

## PFH

| risk assessment  25 ,  115                                             | safety configuration tool  111                                             |
|------------------------------------------------------------------------|----------------------------------------------------------------------------|
|                                                                        | feedback tab  127 home tab  122                                            |
| S                                                                      | input tab  128                                                             |
| safe accel limit                                                       | safe limited speed tab  130 131                                            |
| See safe maximum acceleration limit.                                   | safe max speed tab                                                         |
| safe direction monitoring  108                                         | safe stop tab  129                                                         |
| negative  109                                                          | safety main tab  123 126                                                   |
| overview  23                                                           | safety tab  safety lock indicator  133                                     |
| positive  109                                                          |                                                                            |
| safe limited speed                                                     | shutdown, EDS  13                                                          |
| mode  71                                                               | Signature ID  111 ,  116 ,  118 SIL                                        |
| monitoring delay  72 ,  73 ,  78 ,  80 ,  84                           |                                                                            |
| monitoring inactive  81                                                | 3  13                                                                      |
| reset                                                                  | CL3  11 ,  144                                                             |
| See SLS reset 84                                                       | certification, user responsibilities  14 single encoder configurations  50 |
| status only mode  tab  130                                             | single-channel operation  29                                               |
| with door monitoring and enabling switch                               | slave, safe limited speed                                                  |
| monitoring mode  80                                                    | mode  96                                                                   |
| with door monitoring mode  75 with enabling switch monitoring mode  78 | status only mode  99                                                       |
| safe max speed  103                                                    | slave, safe stop mode  91                                                  |
| tab  131                                                               | SLS reset  42 ,  73 ,  78                                                  |
| safe maximum acceleration                                              | automatic  72 ,  73                                                        |
| limit                                                                  | manual  73                                                                 |
| 106 monitoring  106-108                                                | manual monitored  73                                                       |
| safe maximum acceleration monitoring                                   | SLS with door monitoring and enabling switch monitoring mode  82           |
| overview  23                                                           | SLS with door monitoring mode  76 73                                       |
| safe maximum speed monitoring  103-105                                 | SLS_In input  32 ,                                                         |
| overview  23                                                           | SLS reset  73 ,  78 36                                                     |
| safe speed limit  71 ,  81 ,  85                                       | SLS_Out output                                                             |
| safe state                                                             | hold last state  85 software                                               |
| definition  17 faults  137                                             |                                                                            |
| safe stop                                                              | Studio 5000 Environment  12 specifications                                 |
| 1  57                                                                  | encoder  144 general  143 144                                              |
| 2  57                                                                  | ,  speed                                                                   |
| mode  55 reset                                                         |                                                                            |
| See SS reset                                                           | hysteresis  85                                                             |
| tab  129 56-60                                                         | resolution  43                                                             |
| types                                                                  | speed resolution accuracy 46                                               |
| with door monitoring mode  68                                          | example                                                                    |
| safe torque-off                                                        | linear  45                                                                 |
| with standstill checking  56 without standstill checking  60           | rotary  43 SS reset  42 ,  63-64                                           |
|                                                                        | SLS with door monitoring and enabling switch                               |
| safety                                                                 | monitoring mode  82                                                        |
| attributes  150                                                        | SS_In input  32 35                                                         |
| certification, TÜV Rheinland  13 functions overview  21                | SS_Out output                                                              |
| information  25                                                        | standstill position tolerance  61                                          |
| lock  112 lock indicator                                               | speed  61                                                                  |
| 112 main tab  123                                                      | status attributes  138                                                     |
| mode, slave combinations  102 26                                       | stop category definitions                                                  |
| power supply                                                           | faults  137                                                                |
| ratings  18                                                            | 15                                                                         |
| reaction time  18 ,  43                                                | stop delay                                                                 |
| tab  126                                                               |                                                                            |
|                                                                        | See max stop time stop monitoring delay                                    |
|                                                                        | 55                                                                         |
|                                                                        | Studio 5000 Environment  12                                                |

## T

## terminal screws

```
connections 27 strip length 27 torque 27 timing diagram safe limited speed 72 safe limited speed status only 84 safe stop 1 58 safe stop 2 59 safe torque-off with standstill checking 56 safe torque-off without standstill checking 60
```

## V

## validation

third-party 117

## verify

116

118

configuration lock status 118 Signature ID

## W

## wiring

connector kit 26

DC\_Out output 38 , 39

DM\_In input 38

LM\_In input 38

multi-axis connections 35 , 37

safety input examples 31

## wiring example

safe limited speed mode 75

safe limited speed status only mode 86 , 88

safe stop mode 68

safe stop with door monitoring mode 69

slave, safe limited speed 97-98

slave, safe limited speed status only mode 100-101

slave, safe stop mode 93-95

SLS with door monitoring and enabling switch monitoring mode

83

SLS with door monitoring mode 77

SLS with enabling switch monitoring mode 7 79

## Rockwell Automation Support

Rockwell Automation provides technical information on the Web to assist you in using its products. At http://www.rockwellautomation.com/support, you can find technical manuals, technical and application notes, sample code and links to software service packs, and a MySupport feature that you can customize to make the best use of these tools. You can also visit our Knowledgebase at http://www.rockwellautomation.com/knowledgebase for FAQs, technical information, support chat and forums, software updates, and to sign up for product notification updates.

For an additional level of technical phone support for installation, configuration, and troubleshooting, we offer TechConnectSM support programs. For more information, contact your local distributor or Rockwell Automation representative, or visit http://www.rockwellautomation.com/support/ .

## Installation Assistance

If you experience a problem within the first 24 hours of installation, review the information that is contained in this manual. You can contact Customer Support for initial help in getting your product up and running.

| United States or Canada 1.440.646.3434   |                                                                                                                                                                    |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Outside United States or Canada          | Use the Worldwide Locator at http://www.rockwellautomation.com/rockwellautomation/support/overview.page, or contact your local Rockwell Automation representative. |

## New Product Satisfaction Return

Rockwell Automation tests all of its products to help ensure that they are fully operational when shipped from the manufacturing facility. However, if your product is not functioning and needs to be returned, follow these procedures.

| United States   | Contact your distributor. You must provide a Customer Support case number (call the phone number above to obtain one) to your distributor to complete the return process.   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                 | Outside United States Please contact your local Rockwell Automation representative for the return procedure.                                                                |

## Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete this form, publication RA-DU002, available at http://www.rockwellautomation.com/literature/ .