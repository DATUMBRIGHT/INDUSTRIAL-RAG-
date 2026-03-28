<!-- image -->

## Kinetix 300 EtherNet/IP Indexing Servo Drives

Catalog Numbers 2097-V31PR0, 2097-V31PR2, 2097-V32PR0, 2097-V32PR2, 2097-V32PR4, 2097-V33PR1, 2097-V33PR3, 2097-V33PR5, 2097-V33PR6, 2097-V34PR3, 2097-V34PR5, 2097-V34PR6

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

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes .

Preface

|                                  | Summary of Changes . . . .  . . . . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . . 9    |
|----------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------|
|                                  | Conventions . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . 9      |
|                                  | Additional Resources . . . . . . .  . . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . . 10     |
|                                  | Chapter 1                                                                                             |                                          |
| Start                            | About the Kinetix 300 Drive System . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11         |                                          |
|                                  | Catalog Number Explanation . . .  . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . 13         |
|                                  | Agency Compliance . . . . . . . . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . 14       |
|                                  | CE Requirements. . . . . . . . .  . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . 14       |
|                                  | Chapter 2                                                                                             |                                          |
| Installing the Kinetix 300 Drive | System Design Guidelines.  . . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . . . 16   |
| System                           | System Mounting Requirements .  . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . 16             |
|                                  | Transformer Selection . . . . . .  . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . 17         |
|                                  | Circuit Breaker/Fuse Selection  . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . 17           |
|                                  | Enclosure Selection . . .  . . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . . . 19   |
|                                  | Power Dissipation Specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . 20            |                                          |
|                                  | Minimum Clearance Requirements . . . . . . . . . . . . . . . . . . . . . . . . . 21                   |                                          |
|                                  | Electrical Noise Reduction . . . .  . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . 22       |
|                                  | Bonding Drives. . . . . . . . . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 22       |
|                                  | Bonding Multiple Subpanels. . .  . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . 24           |
|                                  | Establishing the Noise Zones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25         |                                          |
|                                  | Cable Categories for Kinetix 300 Drive Components. . . . . . . . . 27                                 |                                          |
|                                  | Noise Reduction Guidelines for Drive Accessories. . . . . . . . . . . . 27                            |                                          |
|                                  | Mount Your Kinetix 300 Drive. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30      |                                          |
|                                  | Chapter 3                                                                                             |                                          |
| Kinetix 300 Drive Connector Data | Kinetix 300 Drive Connectors and Indicators . . . . . . . . . . . . . . . . . . . 32                  |                                          |
| and Feature Descriptions         | Safe Torque Off Connector Pinout . . . . . . . . . . . . . . . . . . . . . . . . . 33                 |                                          |
|                                  | I/O Connector Pinout . . . . . .  . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . 34         |
|                                  | Motor Feedback (MF) Connector Pinout . . . . . . . . . . . . . . . . . . . 35                         |                                          |
|                                  | Ethernet Communication Connector Pinout . . . . . . . . . . . . . . . . 35                            |                                          |
|                                  | AC Input Power Connector Pinout . . . . . . . . . . . . . . . . . . . . . . . . . 36                  |                                          |
|                                  | Back-up Power Connector Pinout . . . . . . . . . . . . . . . . . . . . . . . . . . 36                 |                                          |
|                                  | Shunt Resistor and DC Bus Connector Pinout. . . . . . . . . . . . . . . 36                            |                                          |
|                                  | Motor-Power Connector Pinout. . . . . . . . . . . . . . . . . . . . . . . . . . . . 36                |                                          |
|                                  | Control Signal Specifications. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 |                                          |
|                                  | Digital Inputs . . . . . .  . . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . . . 37 |
|                                  | Digital Outputs . . . . .  . . . . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . . . 42   |
|                                  | Analog Reference Input . . . . .  . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . 43         |
|                                  | Analog Output . . . . . . . . . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 44       |
|                                  | Master Gearing/Step and Direction Inputs . . . . . . . . . . . . . . . . . . 45                       |                                          |

|                                  | Ethernet Connections . .  . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . 47     |
|----------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------|
|                                  | 24V DC Back-up Power . . . . . .  . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . 47           |
|                                  | Motor Feedback Specifications .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . 48         |
|                                  | Motor Feedback Specifications  . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . 49           |
|                                  | Feedback Power Supply . . . . .  . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 53         |
|                                  | Chapter 4                                                                                       |                                          |
| Connecting the Kinetix 300 Drive | Basic Wiring Requirements . . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . 55         |
| System                           | Build Your Own Cables. . . . .  . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . 56         |
|                                  | Route Power and Signal Wiring. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56       |                                          |
|                                  | Determine the Input Power Configuration . . . . . . . . . . . . . . . . . . . . . . 56          |                                          |
|                                  | Three-phase Power Wired to Three-phase Drives . . . . . . . . . . . . 57                        |                                          |
|                                  | Single-phase Power Wired to Single-phase Drives . . . . . . . . . . . . 58                      |                                          |
|                                  | Voltage Doubler Operation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58    |                                          |
|                                  | Isolation Transformer in Grounded Power Configurations . . . 59                                 |                                          |
|                                  | Three-phase Power Wired to Single-phase Drives . . . . . . . . . . . . 59                       |                                          |
|                                  | Voiding of CE Compliance. . .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . 61           |
|                                  | Ground Your Kinetix 300 Drive System. . . . . . . . . . . . . . . . . . . . . . . . . 62        |                                          |
|                                  | Ground Your Drive to the System Subpanel . . . . . . . . . . . . . . . . . 62                   |                                          |
|                                  | Ground Multiple Subpanels . .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . 63           |
|                                  | Power Wiring Requirements . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . 63         |
|                                  | Wiring Guidelines. . . . .  . . . . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . . . 65 |
|                                  | Wiring the Kinetix 300 Drive Connectors. . . . . . . . . . . . . . . . . . . . . . . 66         |                                          |
|                                  | Wire the Safe Torque Off (STO) Connector . . . . . . . . . . . . . . . . 66                     |                                          |
|                                  | Wire the Back-up Power (BP) Connector . . . . . . . . . . . . . . . . . . . 66                  |                                          |
|                                  | Wire the Input Power (IPD) Connector. . . . . . . . . . . . . . . . . . . . . 67                |                                          |
|                                  | Wire the Motor Power (MP) Connector . . . . . . . . . . . . . . . . . . . . 68                  |                                          |
|                                  | Apply the Motor-Cable Shield Clamp . . . . . . . . . . . . . . . . . . . . . . . . . . 73       |                                          |
|                                  | Feedback and I/O Cable Connections . . . . . . . . . . . . . . . . . . . . . . . . . . 74       |                                          |
|                                  | Flying-lead Feedback Cable Pinouts . . . . . . . . . . . . . . . . . . . . . . . . . 75         |                                          |
|                                  | Wiring the Feedback and I/O Connectors . . . . . . . . . . . . . . . . . . . . . . 76           |                                          |
|                                  | Wire the I/O Connector . . . . .  . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . 76           |
|                                  | Wire the Low Profile Connector Kit . . . . . . . . . . . . . . . . . . . . . . . . 77           |                                          |
|                                  | Shunt Resistor Connections. . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . 78         |
|                                  | Ethernet Cable Connections   . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . . 79     |
|                                  | Chapter 5                                                                                       |                                          |
| MotionView Software              | Drive Organizer and Identification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82 |                                          |
| Configuration                    | Motor Category. . . . . . .  . . . . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . . . . 82 |
|                                  | Synchronous Motor Database .  . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . 83           |
|                                  | Linear Motor Database . . . . .  . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 84         |
|                                  | General Category. . . . . .  . . . . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . . . . 85 |
|                                  | Communication Categories .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 89     |
|                                  | Ethernet Communication .   . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 89       |
|                                  | EtherNet/IP (CIP) Communication . . . . . . . . . . . . . . . . . . . . . . . . 90              |                                          |
|                                  | Input/Output Categories .  . . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . . . 91   |

Configure and Start Up the

Kinetix 300 Drive

| Digital I/O. . . . . . . .  . . . . . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . . . . . 91   |
|----------------------------------------------------------------------------------------------|--------------------------------------------|
| Analog I/O . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . . . . . 92         |
| Limits Categories . . . . .  . . . . . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . . . . 93   |
| Velocity Limits . . . . . .  . . . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . . 93     |
| Position Limits . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . . . . . 94         |
| Dynamics Category. . . . .  . . . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . . . . 95   |
| Tools Category. . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                 | . . . . . . . . . . . . . . . . . 96       |
| Monitor Category . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . . . . . . 97       |
| Faults Category . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . . . . . . . . . . . 98     |
| Indexing Category. . . . . . . . . .  . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . . . . . . 99       |
| Index Type Parameter . . . . .  . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . 101          |
| Action Parameter. . . . . . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 106        |
| Start Index . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . . . . . . 107      |
| Abort Indexing . . . . . . . . . .  . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . . 107        |
| Reset Index . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . . . . . 107        |
| Explicit Messages for Indexing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108 |                                            |
| Homing Category . . . . . .  . . . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . . 111    |
| Homing Methods . . . . .  . . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . . 112      |
| Immediate Homing. . . . . . . .  . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . 113          |
| Absolute Homing . . . . .  . . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . . 113      |
| Home to Marker . . . . . . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 114        |
| Home Offset . . . . . . . . . . . .  . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . 114        |
| Homing Switch . . . . . . . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . 114        |
| Homing Firmware Algorithm .  . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . 115              |
| Homing Methods Timing Diagrams  . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . 116              |
| Homing Methods 7…14. .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 116        |
| Homing Method 23 . . .  . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . . 117      |
| Homing Method 25 . . .  . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . . 118      |
| Homing Method 27 . . .  . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . . 119      |
| Homing Method 29 . . .  . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . . 120      |
| Homing Method 33 . . .  . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . . 121      |
| Homing Method 34 . . .  . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . . 121      |
| Homing Method 35 . . .  . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . . 121      |
| Upgrade Firmware . . . . . . . . .  . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . 122        |
| Chapter 6                                                                                    |                                            |
| Keypad Input . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                  | . . . . . . . . . . . . . . . . . 124      |
| Status Indicators. . . .  . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . 125    |
| Configure the Kinetix 300 Drive EtherNet/IP Address. . . . . . . . . . 126                   |                                            |
| Ethernet Connection . .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 126      |
| Kinetix 300 Drive Ethernet Port Configuration . . . . . . . . . . . . . 126                  |                                            |
| Current IP Address Ethernet Setting . . . . . . . . . . . . . . . . . . . . . . . 127        |                                            |
| Configure the IP Address Manually (static address). . . . . . . . . . 127                    |                                            |
| Configure the IP Address Automatically (dynamic address) . . 129                             |                                            |
| Install the Kinetix 300 Add-on Profile . . . . . . . . . . . . . . . . . . . . . . . . . 130 |                                            |
| Configuring the Logix EtherNet/IP Module. . . . . . . . . . . . . . . . . . . . 131          |                                            |
| Configure the Logix Controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131   |                                            |

|                                   | Configure the Ethernet Port. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132      |                                             |
|-----------------------------------|---------------------------------------------------------------------------------------------------|---------------------------------------------|
|                                   | Configure the Ethernet Module . . . . . . . . . . . . . . . . . . . . . . . . . . . 133           |                                             |
|                                   | Configure the Kinetix 300 Drive . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . 134               |
|                                   | Download the Program . . . . .  . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . 136             |
|                                   | Apply Power to the Kinetix 300 Drive . . . . . . . . . . . . . . . . . . . . . . . . . 137        |                                             |
|                                   | Test and Tune the Axis . . . . . .  . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 138         |
|                                   | Test the Axis . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . 138         |
|                                   | Tune the Axis . . . . . . . . . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 139         |
|                                   | Select Drive Operating Mode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 142 |                                             |
|                                   | Master Gearing Mode Examples .  . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . 143             |
|                                   | Master Gearing Example 1 . . .  . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . 143             |
|                                   | Master Gearing Example 2 . . .  . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . 143             |
|                                   | Master Gearing Example 3 . . .  . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . 143             |
|                                   | Configure Master Gearing Mode . . . . . . . . . . . . . . . . . . . . . . . . . . 144             |                                             |
|                                   | Configure the Drive Parameters and System Variables . . . . . . . . . . . 145                     |                                             |
|                                   | Tools for Viewing Parameters .  . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . 145               |
|                                   | Tools for Changing Parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147         |                                             |
|                                   | Configure Drive Mode with Explicit Messaging. . . . . . . . . . . . . . . . . 148                 |                                             |
|                                   | Configure Drive for Linear Motors and Direct Drive Stages. . . . . . 150                          |                                             |
|                                   | Motor Temperature Sensor. . .  . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . 150             |
|                                   | Understanding Encoder Resolution Setting . . . . . . . . . . . . . . . . . 150                    |                                             |
|                                   | Change the Encoder Resolution for an Incremental Encoder . 151                                    |                                             |
|                                   | Chapter 7                                                                                         |                                             |
| Troubleshooting the Kinetix 300   | Safety Precautions . . . . .  . . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . . . 153   |
| Drive System                      | General Troubleshooting . . . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . 154           |
|                                   | Display Behavior . . . . .  . . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 154       |
|                                   | Error Codes . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . . . 155     |
|                                   | Clearing Faults. . . . . .  . . . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . . . . 158 |
|                                   | Use Digital Inputs to Clear Faults. . . . . . . . . . . . . . . . . . . . . . . . . . 158         |                                             |
|                                   | Use Drive Parameters to Clear Faults. . . . . . . . . . . . . . . . . . . . . . . 158             |                                             |
|                                   | Chapter 8                                                                                         |                                             |
| Kinetix 300 Drive Safe Torque Off | Certification . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . . 161     |
| Feature                           | Important Safety Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . 162           |                                             |
|                                   | Safety Category 3 Requirements  . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . 162               |
|                                   | Stop Category Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 162    |                                             |
|                                   | Performance Level and Safety Integrity Level (SIL) CL3 . . . . . 162                              |                                             |
|                                   | Description of Operation . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . 163         |
|                                   | Functional Proof Tests . . . . . .  . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 163         |
|                                   | Troubleshooting the Safe Torque Off Function . . . . . . . . . . . . . 164                        |                                             |
|                                   | PFD and PFH Definitions . . . . .  . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . 164           |
|                                   | PFD and PFH Data . . . . . . . . .  . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 164         |
|                                   | Safe Torque Off Connector Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 165    |                                             |
|                                   | STO Connector Pinouts . . . . .  . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . 165             |
|                                   | Wiring Your Safe Torque Off Circuit. . . . . . . . . . . . . . . . . . . . . . . . . . 166        |                                             |

|                                                                  | European Union Directives . .  . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . 166         |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-----------------------------------------|
|                                                                  | Safe Torque Off Wiring Requirements . . . . . . . . . . . . . . . . . . . . . 167                  |                                         |
|                                                                  | Kinetix 300 Drive Safe Torque Off Feature. . . . . . . . . . . . . . . . . . . . . 168             |                                         |
|                                                                  | Safe Torque Off Feature Bypass.   . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . 168           |
|                                                                  | Kinetix 300 Drive Safe Torque Off Wiring Diagrams . . . . . . . . . . . 169                        |                                         |
|                                                                  | Safe Torque Off Signal Specifications . . . . . . . . . . . . . . . . . . . . . . . . . . 170      |                                         |
|                                                                  | Safety Input and Output Schematics . . . . . . . . . . . . . . . . . . . . . . . . . . . 171       |                                         |
|                                                                  | Appendix A                                                                                         |                                         |
| Interconnect Diagrams                                            | Interconnect Diagram Notes . . .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . 174       |
|                                                                  | Power Wiring Examples . . . . .  . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . 175     |
|                                                                  | Shunt-Resistor Wiring Example  . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . 177           |
|                                                                  | Kinetix 300 Drive/Rotary Motor Wiring Examples . . . . . . . . . . . . . 178                       |                                         |
|                                                                  | Kinetix 300 Drive/Linear Motor Wiring Examples . . . . . . . . . . . . . 181                       |                                         |
|                                                                  | Kinetix 300 Drive/Actuator Wiring Examples . . . . . . . . . . . . . . . . . . 183                 |                                         |
|                                                                  | Kinetix 300 Drive to MicroLogix Controller Wiring Examples. . . 186                                |                                         |
|                                                                  | Kinetix 300 Drive Master Gearing Wiring Example . . . . . . . . . . . . . 187                      |                                         |
|                                                                  | Motor Brake Currents . . . . . . .  . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . 188     |
|                                                                  | System Block Diagrams . . . . . .  . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . 189     |
|                                                                  | Appendix B                                                                                         |                                         |
| Input and Output Assembly                                        | Input and Output Assembly. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 191 |                                         |
|                                                                  | Output Assembly Examples . . . .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . 197       |
|                                                                  | Incremental Position Point-to-Point Profile . . . . . . . . . . . . . . . . 198                    |                                         |
|                                                                  | Velocity Motion Profile . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . 198   |
|                                                                  | Appendix C                                                                                         |                                         |
| Kinetix 300 Drive ID Tag Numbers Tag Number Descriptions . . . . | . . . . . . . . . . . . . . . . .                                                                  | . . . . . . . . . . . . . . . 199       |
|                                                                  | Index Base Addressing . . . . . .  . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 212     |
|                                                                  | Appendix D                                                                                         |                                         |
| MicroLogix Explicit Messaging                                    | Explicit Messaging Data Types . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 213  |                                         |
|                                                                  | Explicit Messaging Data Type Examples. . . . . . . . . . . . . . . . . . . . . . . . 214           |                                         |
|                                                                  | DINT Data Type Examples . .  . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . 214         |
|                                                                  | REAL Data Type Examples . .  . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . 215         |
|                                                                  | String Data Type Examples. . .  . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . 216         |
|                                                                  | Appendix E                                                                                         |                                         |
| Overtravel Inputs                                                | Modes of Operation . . . . . . . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 219     |
|                                                                  | Overtravel Hardware Inputs . .  . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . 220       |
|                                                                  | Operation . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . . . 221 |
|                                                                  | Overtravel Fault Recovery. . . .  . . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . . . 222     |

Leakage Current Specifications

Appendix F

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Index

. . . . . . . . . . . . . . . . . . . . 223

. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

. . . . . . . . . . . . . . . . . . 227

## Summary of Changes

## Conventions

This manual provides detailed installation instructions for mounting, wiring, and troubleshooting your Kinetix® 300 drive; and system integration for your drive/motor combination with a Logix controller.

This manual is intended for engineers and technicians that are directly involved in the installation and wiring of the Kinetix 300 drive and programmers who are directly involved in operation, field maintenance, and integration of the Kinetix 300 drive.

If you do not have a basic understanding of the Kinetix 300 drive, contact your local Rockwell Automation sales representative for information on available training courses.

Rockwell Automation recognizes that some of the terms that are currently used in our industry and in this publication are not in alignment with the movement toward inclusive language in technology. We are proactively collaborating with industry peers to find alternatives to such terms and making changes to our products and content. Please excuse the use of such terms in our content while we implement these changes.

This publication contains the following new or updated information. This list includes substantive updates only and is not intended to reflect all changes.

|                                                                                                                                                             | Topic Page   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Added the Bulletin 140M to 140MT Motor Protection Circuit Breakers Migration Profile publication information to the Additional Resources table.             | 10           |
| Updated all 140M-C and 140M-D devices (which reached end of life) to the equivalent 140MT device in Table 6 - Fuse and Circuit Breaker (CB) Specifications. | 18           |
| Updated European Union Directives references in the Wiring Your Safe Torque Off Circuit section. 166                                                        |              |

These conventions are used throughout this manual:

- Bulleted lists such as this one provide information, not procedural steps.
- Numbered lists provide steps or hierarchical information.

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation. You can view or download publications at rok.auto/literature .

| Resource                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix Rotary Motion Specifications Technical Data, publication KNX-TD001                                          | Product specifications for Kinetix VPL, VPC, VPF, VPH, and VPS; Kinetix MPL, MPM, MPF, and MPS; Kinetix TLY and TL; Kinetix HPK; and Kinetix MMA rotary motors.                                                                                                                                                                                                                                          |
| Kinetix Linear Motion Specifications Technical Data, publication KNX-TD002                                          | Product specifications for Kinetix MPAS and MPMA linear stages, Kinetix MPAR and MPAI electric cylinders, and Kinetix LDC and LDL linear motors.                                                                                                                                                                                                                                                         |
| Kinetix Rotary and Linear Motion Cable Specifications Technical Data, publication KNX-TD004                         | Product specifications for Kinetix 2090 motor and interface cables.                                                                                                                                                                                                                                                                                                                                      |
| Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005 | Provides product specifications for Kinetix Integrated Motion over the EtherNet/IP network (Kinetix 6500 and Kinetix 350), Integrated Motion over Sercos interface (Kinetix 6200, Kinetix 6000, Kinetix 2000, and Kinetix 7000), and component (Kinetix 3) servo drive families.                                                                                                                         |
| Kinetix 300 Shunt Resistor Installation Instructions, publication 2097-IN002                                        | Information on how to install and wire the Kinetix 300 shunt resistors.                                                                                                                                                                                                                                                                                                                                  |
| Kinetix 300 AC Line Filter Installation Instructions, publication 2097-IN003                                        | Information on installing and wiring the Kinetix 300 AC line filter.                                                                                                                                                                                                                                                                                                                                     |
| Kinetix 300 I/O Terminal Expansion Block Installation Instructions, publication 2097-IN005                          | Information on how to install and wire the Kinetix 300 I/O terminal expansion block.                                                                                                                                                                                                                                                                                                                     |
| Kinetix 300 Memory Module Installation Instructions, publication 2097-IN007                                         | Information on how to install the Kinetix 300 memory module.                                                                                                                                                                                                                                                                                                                                             |
| Bulletin 140M to 140MT Motor Protection Circuit Breakers Migration Profile, publication MIGRAT-PP049                | Provides detailed migration solutions for obsolete 140M motor protection devices to 140MT motor protection devices.                                                                                                                                                                                                                                                                                      |
| Kinetix 300 Memory Module Programmer Quick Start, publication 2097-QS001                                            | Information on how to use the memory module programmer to duplicate the memory module.                                                                                                                                                                                                                                                                                                                   |
| Kinetix 300/350 Drive Systems Design Guide, publication KNX-RM004                                                   | Provides system design guide to determine and select the required (drive specific) drive module, power accessory, connector kit, motor cable, and interface cable catalog numbers for your drive and motor/actuator motion control system. Included are system performance specifications and torque/ speed curves (rotary motion) and force/velocity curves (linear motion) for your motion application |
| CompactLogix™ System User Manual, publication 1769-UM011                                                            | Information on how to plan, mount, wire, and troubleshoot your CompactLogix system.                                                                                                                                                                                                                                                                                                                      |
| ControlLogix® Controllers User Manual, publication 1756-UM001                                                       | Information on how to install, configure, program, and operate a ControlLogix system.                                                                                                                                                                                                                                                                                                                    |
| ControlFLASH™ Firmware Upgrade Kit User Manual, publication 1756-QS105                                              | For ControlFLASH information not specific to any drive family.                                                                                                                                                                                                                                                                                                                                           |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                         | Provides general guidelines for installing a Rockwell Automation® industrial system.                                                                                                                                                                                                                                                                                                                     |
| System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001                               | Provides information, examples, and techniques designed to minimize system failures caused by electrical noise.                                                                                                                                                                                                                                                                                          |
| Product Certifications website, rok.auto/certifications                                                             | For declarations of conformity (DoC) currently available from Rockwell Automation.                                                                                                                                                                                                                                                                                                                       |
| Rockwell Automation Industrial Automation Glossary, publication AG-7.1                                              | A glossary of industrial automation terms and abbreviations.                                                                                                                                                                                                                                                                                                                                             |

## About the Kinetix 300 Drive System

Table 1 - Kinetix 300 Drive System Overview

| Kinetix 300 System Component                       |                                                                                                                                                                                                                                                                                                                                                            | Cat. No. Description                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Kinetix 300 EtherNet/IP Indexing Servo Drive       | 2097-V3xPRx                                                                                                                                                                                                                                                                                                                                                | Kinetix 300 EtherNet/IP indexing drives with Safe Torque Off feature are available with 120/240V or 480V AC input power.                                                                                                                                                                                                                                   |
| AC Line Filters                                    | 2090 2097-Fx                                                                                                                                                                                                                                                                                                                                               | Kinetix 2090 and Bulletin 2097-Fx AC line filters are required to meet CE with Kinetix 300 drives without an integrated line filter. Bulletin 2097 filters are available in foot mount and side mount.                                                                                                                                                     |
| Shunt Module                                       | 2097-Rx                                                                                                                                                                                                                                                                                                                                                    | Bulletin 2097 shunt resistors connect to the drive and provide shunt capability in regenerative applications.                                                                                                                                                                                                                                              |
| Terminal block for I/O connector                   | 2097-TB1                                                                                                                                                                                                                                                                                                                                                   | 50-pin terminal block. Use with IOD connector for control interface connections.                                                                                                                                                                                                                                                                           |
| Memory Module Programmer                           | 2097-PGMR                                                                                                                                                                                                                                                                                                                                                  | The EPM programmer is used to duplicate the memory and configuration of the Kinetix 300 drives.                                                                                                                                                                                                                                                            |
| Memory Modules 12 Pack 2097-MEM                    |                                                                                                                                                                                                                                                                                                                                                            | These memory modules are removable and the drive to store parameters in them.                                                                                                                                                                                                                                                                              |
| Logix PAC® Controller Platforms                    | Bulletin 5069 Bulletin 1768 and 1769                                                                                                                                                                                                                                                                                                                       | EtherNet/IP networking with CompactLogix™ 5370 and CompactLogix 5380 controllers with embedded dual-port. 1769-L3x controllers with embedded single port. 1768-L4x controller and 1768-L4xS safety controller with 1768-ENBT EtherNet/IP communication module.                                                                                             |
| Logix PAC® Controller Platforms                    | 1756-EN2T, 1756-EN2TR, and 1756-EN3TR module                                                                                                                                                                                                                                                                                                               | EtherNet/IP network communication modules for use with ControlLogix® 5570 and ControlLogix 5580 controllers.                                                                                                                                                                                                                                               |
| Logix PLC Controller Platforms                     | MicroLogix™ 1100 and 1400 controllers provide communications ports, an isolated combination RS-232/485 communication port, an Ethernet port, and (MiroLogix 1400 only) a non-isolated RS-232 communication port. Micro850® controllers with embedded inputs/outputs can accommodate from two to five plug-in modules and up to four expansion I/O modules. | MicroLogix™ 1100 and 1400 controllers provide communications ports, an isolated combination RS-232/485 communication port, an Ethernet port, and (MiroLogix 1400 only) a non-isolated RS-232 communication port. Micro850® controllers with embedded inputs/outputs can accommodate from two to five plug-in modules and up to four expansion I/O modules. |
| Studio 5000® Environment or RSLogix 5000® Software | N/A                                                                                                                                                                                                                                                                                                                                                        | RSLogix 5000 software (version 20 or earlier) and the Studio 5000 Logix Designer® application (version 21 or later) are used to program, commission, and maintain the Logix family of controllers.                                                                                                                                                         |
|                                                    |                                                                                                                                                                                                                                                                                                                                                            | Rotary Servo Motors Kinetix MP, Kinetix TL Compatible rotary motors include the Kinetix MP (MPL, MPM, MPF, and MPS) and Kinetix TL servo motors.                                                                                                                                                                                                           |
| Linear Stages                                      | Kinetix MPAS                                                                                                                                                                                                                                                                                                                                               | Compatible stages include Kinetix MPAS integrated linear stages.                                                                                                                                                                                                                                                                                           |
| Linear Actuators Kinetix LDAT                      |                                                                                                                                                                                                                                                                                                                                                            | Compatible actuators include Kinetix LDAT integrated linear thrusters.                                                                                                                                                                                                                                                                                     |
| Linear Motors                                      |                                                                                                                                                                                                                                                                                                                                                            | Kinetix LDC and LDL Compatible linear motors include Kinetix LDC and LDL linear motors.                                                                                                                                                                                                                                                                    |

## Start

| Topic                              |   Page |
|------------------------------------|--------|
| About the Kinetix 300 Drive System |     11 |
| Catalog Number Explanation         |     13 |
| Agency Compliance                  |     14 |

The Kinetix® 300 EtherNet/IP™ indexing servo drive is designed to provide a solution for applications with output power requirements between 0.4…3.0 kW (2…12 A rms).

<!-- image -->

Table 1 - Kinetix 300 Drive System Overview (Continued)

| Kinetix 300 System Component   |                                 | Cat. No. Description                                                                                                                                                                                                                                                                                                      |
|--------------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                |                                 | Electric Cylinders Kinetix MP, Kinetix TL Compatible electric cylinders include Kinetix MP (MPAR and MPAI) and Kinetix TL (TLAR) Electric Cylinders.                                                                                                                                                                      |
| Cables                         | Motor/brake and feedback cables | Motor power/brake and feedback cables include SpeedTec and threaded DIN connectors at the motor. Power/ brake cables have flying leads on the drive end and straight connectors to servo motors. Feedback cables have flying leads that wire to connector kits on the drive end and straight connectors on the motor end. |
|                                |                                 | Communication cables 1585J-M8CBJM-x (shielded) Ethernet cable.                                                                                                                                                                                                                                                            |

Figure 1 - Typical Kinetix 300 Drive Installation

<!-- image -->

## Catalog Number Explanation

Kinetix 300 drive catalog numbers and descriptions are listed in these tables.

Table 2 - Kinetix 300 Drives (single-phase)

| Cat. No.    | Input Voltage   |   Continuous Output Current A (0-pk) | Features                                      |
|-------------|-----------------|--------------------------------------|-----------------------------------------------|
| 2097-V31PR0 | 120/240V, 1 Ø   |                                  2.8 | • 120V Doubler mode 120/240V, 1 Ø • Safe Torque Off 2097-V31PR2 5.7                                               |
|             | 120/240V, 1 Ø   |                                  5.7 | • 120V Doubler mode 120/240V, 1 Ø • Safe Torque Off 2097-V31PR2 5.7                                               |
| 2097-V32PR0 | 240V, 1 Ø       |                                  2.8 | • Integrated AC line filter • Safe Torque Off |
| 2097-V32PR2 | 240V, 1 Ø       |                                  5.7 | • Integrated AC line filter • Safe Torque Off |
| 2097-V32PR4 | 240V, 1 Ø       |                                 11.3 | • Integrated AC line filter • Safe Torque Off |

## Table 3 - Kinetix 300 Drives (single/three-phase)

| Cat. No.    | Input Voltage                 |   Continuous Output Current A (0-pk) | Features        |
|-------------|-------------------------------|--------------------------------------|-----------------|
| 2097-V33PR1 | 120V, 1 Ø 240V, 1 Ø 240V, 3 Ø |                                  2.8 | Safe Torque Off |
| 2097-V33PR3 | 120V, 1 Ø 240V, 1 Ø 240V, 3 Ø |                                  5.7 | Safe Torque Off |
| 2097-V33PR5 | 120V, 1 Ø 240V, 1 Ø 240V, 3 Ø |                                 11.3 | Safe Torque Off |
| 2097-V33PR6 | 120V, 1 Ø 240V, 1 Ø 240V, 3 Ø |                                 17   | Safe Torque Off |

## Table 4 - Kinetix 300 Drives (three-phase)

| Cat. No.    | Input Voltage   |   Continuous Output Current A (0-pk) | Features        |
|-------------|-----------------|--------------------------------------|-----------------|
| 2097-V34PR3 | 480V, 3 Ø       |                                  2.8 | Safe Torque Off |
| 2097-V34PR5 | 480V, 3 Ø       |                                  5.7 | Safe Torque Off |
| 2097-V34PR6 | 480V, 3 Ø       |                                  8.5 | Safe Torque Off |

## Table 5 - Kinetix 300 Drive Accessories

| Cat. No.   | Drive Components                          |
|------------|-------------------------------------------|
| 2097-Fx    | AC line filters                           |
|            | 2097-TB1 Terminal block for I/O connector |
| 2097-Rx    | Shunt resistors                           |
|            | 2097-PGMR Memory module programmer        |
|            | 2097-MEM Memory modules 12 pack           |

## Agency Compliance

If this product is installed within the European Union and has the CE marking, the following requirements apply.

<!-- image -->

ATTENTION: To meet CE requirements requires a grounded system, and the method to ground the AC line filter and drive must match. Failure to do to match systems ground makes the filter ineffective and can damage the filter. For ground examples, see Ground Your Kinetix 300 Drive System on page 62 .

For more information on electrical noise reduction, see the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

## CE Requirements

To meet CE requirements, these requirements apply:

- Install an AC line filter (Kinetix 2090 or Bulletin 2097) as close to the drive as possible.
- Use Kinetix 2090 motor-power cables or use connector kits and connect the cable shields to the subpanel with the clamp provided.
- Use Kinetix 2090 motor-feedback cables or use connector kits and properly connect the feedback cable shield. Drive-to-motor power and feedback cables must not exceed 20 m (65.6 ft).
- Install the Kinetix 300 system inside an enclosure. Run input power wiring in conduit (grounded to the enclosure) outside of the enclosure. Separate signal and power cables.
- Isolate input power wiring and motor power cables from control wiring and motor feedback cables. Use shielded cable for power wiring and provide a grounded 360° clamp termination.

See Appendix A on page 173 for interconnect diagrams, including input power wiring and drive/motor interconnect diagrams.

<!-- image -->

## Installing the Kinetix 300 Drive System

| Topic                        |   Page |
|------------------------------|--------|
| System Design Guidelines     |     16 |
| Electrical Noise Reduction   |     22 |
| Mount Your Kinetix 300 Drive |     30 |

<!-- image -->

ATTENTION: Plan the installation of your system so that you can cut, drill, tap, and weld with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry, which can result in damage to components.

## System Design Guidelines

Use the information in this section when you design your enclosure and plan to mount your system components on the panel.

For online product selection and system configuration tools, including AutoCAD (DXF) drawings of the product, see .

https://www.rockwellautomation.com/global/support/selection.page

## System Mounting Requirements

- To comply with UL and CE, the Kinetix® 300 system must be enclosed in a grounded conductive enclosure that offers protection as defined in standard EN 60529 (IEC 529) to IP4X. The enclosures must be not accessible to an operator or unskilled persons. A NEMA 4X enclosure exceeds these requirements providing protection to IP66.
- The panel that you install in the enclosure for mounting your system components must be on a flat, rigid, vertical surface that is not subjected to shock, vibration, moisture, oil mist, dust, or corrosive vapors.
- Size the drive enclosure so as not to exceed the maximum-ambient temperature rating. Consider heat dissipation specifications for all drive components.
- Isolate input power wire and motor power cables from control wires and motor feedback cables. Use shielded cable for power wires and provide a grounded 360° clamp termination.
- Use high-frequency (HF) techniques for bonding to connect the enclosure, machine frame, and motor housing, and to provide a lowimpedance return path for high-frequency (HF) energy and reduce electrical noise.
- Use Kinetix 2090 motor-feedback cables or use connector kits and properly connect the feedback cable shield. Drive-to-motor power and feedback cables must not exceed 20 m (65.6 ft).

## IMPORTANT

System performance was tested at these cable length specifications. These limitations are also a CE requirement.

See the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001, for a better understanding the concept of electrical noise reduction.

## Transformer Selection

The Kinetix 300 drive does not require an isolation transformer for threephase input power. However, a transformer can be required to match the voltage requirements of the controller to the available service.

To size a transformer for the main AC power inputs, see Circuit Breaker/Fuse Selection on page 17 and the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005 .

| IMPORTANT   | Use a form factor of 1.5 for single and three-phase power (where form factor is used to compensate for transformer, drive, and motor losses, and to account for utilization in the intermittent operating area of the torque speed curve). For example, size a transformer to the voltage requirements of catalog number 2097-V34PR6 = 3 kW continuous x 1.5 = 4.5 KVA transformer.   |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Circuit Breaker/Fuse Selection

The Kinetix 300 drives use internal solid-state motor short-circuit protection and, when connected to a suitable branch circuit protection, are rated for use on a circuit that can deliver up to 100,000 A (fuses) or 65,000 A (circuit breakers).

| IMPORTANT   | Do not use circuit protection devices on the output of an AC drive as an isolating disconnect switch or motor overload device. These devices are designed to operate on sine wave voltage and the drive's PWM waveform does not allow it to operate properly. As a result, damage to the device occurs.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Make sure that the selected components are properly coordinated and meet acceptable codes including any requirements for branch circuit protection. Evaluation of the short-circuit available current is critical and must be kept below the short-circuit current rating of the circuit breaker.

See the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005, for input current and inrush current specifications for your Kinetix 300 drive.

See Fuse and Circuit Breaker (CB) Specifications on page 18 for recommended circuit breakers and fuses.

Table 6 - Fuse and Circuit Breaker (CB) Specifications

| Drive Cat. No.   |                                     | UL Applications IEC (non-UL) Applications    | UL Applications IEC (non-UL) Applications                                                            | UL Applications IEC (non-UL) Applications   |
|------------------|-------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------|---------------------------------------------|
| Drive Cat. No.   | Drive Voltage  Phase                | Fuses (Bussmann)                             | Miniature CB (1)  Cat. No. Motor Protection CB (1) (2) Cat. No. DIN gG Fuses Amps, Max Miniature CB (1) Cat. No.                                                                                                      | Motor Protection CB (1) Cat. No.            |
| 2097-V31PR0      | 120V Single-phase (voltage doubler) |                                              | KTK-R-20 (20 A) 1489-A1C200 140MT-D9E-C20 20 1492-SP1D200 140MT-D9E-C20                              |                                             |
| 2097-V31PR0      |                                     |                                              | 120/240V Single-phase KTK-R-10 (10 A) 1489-A1C100 140MT-C3E-C10 10 1492-SP1D100 140MT-C3E-C10        |                                             |
| 2097-V31PR2      | 120V Single-phase (voltage doubler) |                                              | KTK-R-30 (30 A) 1489-A1C300 140M-F8E-C32 32 1492-SP1D300 140M-F8E-C32                                |                                             |
| 2097-V31PR2      |                                     |                                              | 120/240V Single-phase KTK-R-20 (20 A) 1489-A1C200 140MT-D9E-C20 20 1492-SP1D200 140MT-D9E-C20        |                                             |
| 2097-V32PR0      | 240V Single-phase                   |                                              | KTK-R-15 (15 A) 1489-A1C150 140MT-D9E-C16 16 1492-SP1D150 140MT-D9E-C16                              |                                             |
|                  | 240V Single-phase                   |                                              | 240V Single-phase2097-V32PR2 KTK-R-20 (20 A) 1489-A1C200 140MT-D9E-C20 20 1492-SP1D200 140MT-D9E-C20 |                                             |
|                  | 240V Single-phase                   |                                              | 2097-V32PR4 KTK-R-30 (30 A) 1489-A1C300 140M-F8E-C32 32 1492-SP1D320 140M-F8E-C32                    |                                             |
| 2097-V33PR1      |                                     |                                              | 120/240V Single-phase KTK-R-20 (20 A) 1489-A1C200 140MT-D9E-C20 20 1492-SP1D200 140MT-D9E-C20        |                                             |
| 2097-V33PR1      |                                     |                                              | 240V Three-phase KTK-R-15 (15 A) 1489-A3C150 140MT-D9E-C16 16 1492-SP3D150 140MT-D9E-C16             |                                             |
| 2097-V33PR3      |                                     |                                              | 120/240V Single-phase KTK-R-20 (20 A) 1489-A1C200 140MT-D9E-C20 20 1492-SP1D200 140MT-D9E-C20        |                                             |
| 2097-V33PR3      |                                     |                                              | 240V Three-phase KTK-R-15 (15 A) 1489-A3C150 140MT-D9E-C16 16 1492-SP3D150 140MT-D9E-C16             |                                             |
| 2097-V33PR5      |                                     |                                              | 120/240V Single-phase KTK-R-30 (30 A) 1489-A1C300 140M-F8E-C32 32 1492-SP1D300 140M-F8E-C32          |                                             |
| 2097-V33PR5      |                                     |                                              | 240V Three-phase KTK-R-20 (20 A) 1489-A3C200 140MT-D9E-C20 20 1492-SP3D200 140MT-D9E-C20             |                                             |
| 2097-V33PR6      | 120/240V Single-phase LPJ-40SP N/A  |                                              | 140M-F8E-C32 40 N/A                                                                                  | 140M-F8E-C32                                |
| 2097-V33PR6      |                                     | 240V Three-phase KTK-R-30 (30 A) 1489-A3C300 | 32 1492-SP3D300                                                                                      | 140M-F8E-C32                                |
| 2097-V34PR3      | 480V Three-phase                    |                                              | KTK-R-10 (10 A) 1489-A3C100 140MT-C3E-C10 10 1492-SP3D100 140MT-C3E-C10                              |                                             |
| 2097-V34PR5      | 480V Three-phase                    |                                              | KTK-R-10 (10 A) 1489-A3C100 140MT-C3E-C10 10 1492-SP3D100 140MT-C3E-C10                              |                                             |
| 2097-V34PR6      | 480V Three-phase                    |                                              | KTK-R-20 (20 A) 1489-A3C200 140MT-D9E-C20 20 1492-SP3D200 140MT-D9E-C20                              |                                             |

See https://ab.rockwellautomation.com/allenbradley/productdirectory.page for product literature with specific short-circuit ratings.

For 140M to 140MT device migration details, see Bulletin 140M to 140MT Motor Protection Circuit Breakers Migration Profile, publication MIGRAT-PP049 .

(2) For UL applications, Bulletin 140M and 140MT devices are applied as self-protected combination motor controllers.

## Enclosure Selection

This example is provided to assist you in size selection for an enclosure for your Bulletin 2097 drive system. You need heat dissipation data from all components that are planned for your enclosure to calculate the enclosure size. See Power Dissipation Specifications on page 20 for the Kinetix 300 drive power dissipation.

With no active method of heat dissipation (such as fans or air conditioning), either of the following approximate equations can be used.

| Metric                                                    | Standard English                                          |
|-----------------------------------------------------------|-----------------------------------------------------------|
| Where T is temperature difference between inside air and outside ambient (°C), Q is heat that is generated in 2 enclosure (Watts), and A is enclosure surface area (m 2 ). The exterior surface of all six sides of an enclosure is calculated as                                                           | Where T is temperature difference between inside air and outside ambient (°F), Q is heat that is generated in 2) enclosure (Watts), and A is enclosure surface area (ft 2) . The exterior surface of all six sides of an enclosure is calculated as                                                           |
| A = 2dw + 2dh + 2wh                                       | A = (2dw + 2dh + 2wh) /144                                |
| Where d (depth), w (width), and h (height) are in meters. | Where d (depth), w (width), and h (height) are in inches. |

If the maximum ambient rating of the Kinetix 300 drive system is 40 °C (104 °F) and if the maximum environmental temperature is 20 °C (68 °F), then T=20. In this example, the total heat dissipation is 416 W (sum of all components in enclosure). So, in the equation below, T=20 and Q=416.

<!-- formula-not-decoded -->

In this example, the enclosure must have an exterior surface of at least 4.53 m 2 . If any portion of the enclosure is not able to transfer heat, exclude that part in the calculation.

Because the minimum cabinet depth to house the Kinetix 300 system (selected for this example) is 332 mm (13 in.), choose a cabinet approximately 2000 x 700 x 332 mm (78.7 x 27.6 x 13.0 in.) HxWxD.

<!-- formula-not-decoded -->

Because this cabinet size is considerably larger than what is necessary to house the system components. The choice of a smaller cabinet than can be more efficient to cool. Contact your cabinet manufacturer for options available to cool your cabinet.

## Power Dissipation Specifications

Use this table to size an enclosure and calculate required ventilation for your Kinetix 300 drive system.

| Cat. No.    |   Power Dissipation, W |
|-------------|------------------------|
| 2097-V31PR0 |                     28 |
| 2097-V31PR2 |                     39 |
| 2097-V32PR0 |                     28 |
| 2097-V32PR2 |                     39 |
| 2097-V32PR4 |                     67 |
| 2097-V33PR1 |                     28 |
| 2097-V33PR3 |                     39 |
| 2097-V33PR5 |                     67 |
| 2097-V33PR6 |                    117 |
| 2097-V34PR3 |                     39 |
| 2097-V34PR5 |                     58 |
| 2097-V34PR6 |                     99 |

## Minimum Clearance Requirements

This section provides information to assist you in making the choice of the size of your cabinet and position of your Kinetix 300 system components.

IMPORTANT

Mount the module in an upright position as shown. Do not mount the drive module on its side.

Figure 2 illustrates minimum clearance requirements for proper airflow and installation:

- Extra clearance is required depending on the accessory items installed.
- An extra 9.7 mm (0.38 in.) clearance is required left of the drive if the I/ O expansion terminal block is used.
- An extra 26 mm (1.0 in.) clearance is required right of the drive when the heatsink is present.
- An extra 36 mm (1.42 in.) is required right of the drive when the sidemount line filter is present. An extra 50 mm (2.0 in.) is required behind the drive when the rear-mount line filter is present.
- An extra 5.0 mm (0.19 in.) clearance is required in front of the drive when the 2090-K2CK-D15M feedback connector kit is used.
- Extra clearance is required for the cables and wires that are connected to the top, front, and bottom of the drive.
- An extra 150 mm (6.0 in.) is required when the drive is mounted near noise sensitive equipment or clean wireways.

See the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005 for Kinetix 300 drive dimensions.

Figure 2 - Minimum Clearance Requirements

<!-- image -->

| Drive Cat. No. A       |
|------------------------|
| 2097-V31PR0 185 (7.29) |
| 2097-V31PR2 185 (7.29) |
| 2097-V32PR0 230 (9.04) |
| 2097-V32PR2 230 (9.04) |
| 2097-V32PR4 230 (9.04) |
| 2097-V33PR1 185 (7.29) |
| 2097-V33PR3 185 (7.29) |
| 2097-V33PR5 185 (7.29) |
| 2097-V33PR6 230 (9.04) |
| 2097-V34PR3 185 (7.29) |
| 2097-V34PR5 185 (7.29) |
| 2097-V34PR6 230 (9.04) |

## Electrical Noise Reduction

This section outlines best practices that minimize the possibility of noiserelated failures as they apply specifically to Kinetix 300 system installations. For more information on the concept of high-frequency (HF) bonding, the ground plane principle, and electrical noise reduction, see the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

## Bonding Drives

Bonding is the practice where you connect the metal chassis, assemblies, frames, shields, and enclosures to reduce the effects of electromagnetic interference (EMI).

Unless specified, most paints are not conductive and act as insulators. To achieve a good bond between drive and the subpanel, surfaces must be paintfree or plated. Bonding the metal surfaces creates a low-impedance return path for high-frequency energy.

## IMPORTANT

To improve the bond between the drive and subpanel, construct your subpanel out of zinc-plated (paint-free) steel.

Improper bonding of the metal surfaces blocks the direct return path and allows high-frequency energy to travel elsewhere in the cabinet. Excessive highfrequency energy can affect the operation of other microprocessor-controlled equipment.

These illustrations show recommended practices for bonding the painted panels, enclosures, and brackets.

Figure 3 - Recommended Bonding Practices for Painted Panels

<!-- image -->

## Bonding Multiple Subpanels

Bonding multiple subpanels creates a common low-impedance exit path for the high frequency energy inside the cabinet. Subpanels that are not bonded together do not necessarily share a common low-impedance path. This difference in impedance can affect networks and other devices that span multiple panels.

- Bond the top and bottom of each subpanel to the cabinet by using 25.4 mm (1.0 in.) by 6.35 mm (0.25 in.) wire braid. As a rule, the wider and shorter the braid is, the better the bond.
- Scrape the paint from around each fastener to maximize metal-to-metal contact.

Figure 4 - Multiple Subpanels and Cabinet Recommendations

<!-- image -->

## Establishing the Noise Zones

Observe these guidelines when individual input-power components are used in the Kinetix 300 system:

- The clean zone (C) exits left of the Kinetix 300 system and includes the I/O wiring, feedback cable, Ethernet cable, and DC filter (gray wireway).
- The dirty zone (D) exits right of the Kinetix 300 system (black wireway) and includes the circuit breakers, transformer, 24V DC power supply, contactors, AC line filter, motor power, and safety cables.
- The very dirty zone (VD) is limited to where the AC line (EMC) filter VAC output jumpers over to the drive. Shielded cable is required only if the very dirty cables enter a wireway.
- (1) If drive system I/O cable contains (dirty) relay wires, route cable in dirty wireway.
- (2) For tight spaces, use a grounded steel shield. For examples, see the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .
- (3) This is a clean 24V DC available for any device that requires it. The 24V enters the clean wireway and exits to the left.
- (4) This is a dirty 24V DC available for motor brakes and contactors. The 24V enters the dirty wireway and exits to the right.

Figure 5 - Noise Zones (Kinetix 2090 AC line filters)

<!-- image -->

Figure 6 - Noise Zones (Bulletin 2097 AC line filters)

<!-- image -->

- (1) If drive system I/O cable contains (dirty) relay wires, route cable in dirty wireway.
- (2) For tight spaces, use a grounded steel shield. For examples, see the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .
- (3) This is a clean 24V DC available for any device that requires it. The 24V enters the clean wireway and exits to the left.
- (4) This is a dirty 24V DC available for motor brakes and contactors. The 24V enters the dirty wireway and exits to the right.

## Cable Categories for Kinetix 300 Drive Components

Table 7 indicates the zoning requirements of cables that connect to the Kinetix 300 drive components.

Table 7 - Kinetix 300 Drive Components

| Wire/Cable                                                                                       | Connector   | Zone       | Zone   | Zone   | Method                     | Method         |
|--------------------------------------------------------------------------------------------------|-------------|------------|--------|--------|----------------------------|----------------|
|                                                                                                  |             | Very Dirty |        |        | Dirty Clean Ferrite Sleeve | Shielded Cable |
| L1, L2, L3 (unshielded cable)                                                                    | IPD X       |            |        |        |                            |                |
| U, V, W (motor power)                                                                            | MP          |            | X      |        |                            | X              |
| +, -, SH (shunt resistor)                                                                        | BC          |            | X      |        |                            |                |
| 24V DC                                                                                           | BP          |            |        | X      |                            |                |
| Control COM, 24V DC control, safety enable, and feedback signals for the Safe Torque Off feature | STO         |            | X      |        |                            |                |
| Motor feedback                                                                                   | MF          |            |        | X      |                            | X              |
| Registration and analog outputs                                                                  | IOD         |            |        | X      |                            | X              |
| Others                                                                                           |             |            | X      |        |                            |                |
| Ethernet                                                                                         | Port 1      |            |        | X      |                            | X              |

## Noise Reduction Guidelines for Drive Accessories

See this section when mounting an AC line filter or shunt resistor module for guidelines that are designed to reduce system failures caused by excessive electrical noise.

## AC Line Filters

Observe these guidelines when mounting your AC line filter:

- If you are using a Kinetix 2090 line filter, mount the filter on the same panel as the Kinetix 300 drive, and as close to the drive as possible.
- Good HF bonding to the panel is critical. For painted panels, see the examples on page 23 .
- Isolate input and output wiring as far as possible.

## Shunt Resistors

Observe these guidelines when mounting your shunt resistor outside the enclosure:

- Mount shunt resistor and wiring in the very dirty zone or in an external shielded enclosure.
- Mount resistors in a shielded and ventilated enclosure outside the cabinet.
- Keep unshielded wiring as short as possible. Keep shunt wiring as flat to the cabinet as possible.

Figure 7 - Shunt Resistor Outside the Enclosure

<!-- image -->

When mounting your shunt module inside the enclosure, follow these additional guidelines:

- Mount the shunt resistor anywhere in the dirty zone, but as close to the Kinetix 300 drive as possible.
- Shunt wires can be run with motor power cables.
- Keep unshielded wiring as short as possible. Keep shunt wiring as flat to the cabinet as possible.
- Separate shunt wires from other sensitive, low-voltage signal cables.
- (1) If drive system I/O cable contains (dirty) relay wires, route cable in dirty wireway.
- (2) When space does not permit 150 mm (6.0 in.) clearance, install a grounded steel shield between the drive and clean wireway. For examples, see the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

Figure 8 - Shunt Resistor Inside the Enclosure

<!-- image -->

## Motor Brake

The brake is mounted inside the motor and how you connect to the drive depends on the motor series.

See Kinetix 300 Drive/Rotary Motor Wiring Examples beginning on page 178 for the interconnect diagram of your drive/motor combination.

## Mount Your Kinetix 300 Drive

This procedure assumes that you have prepared your panel and understand how to bond your system. For installation instructions regarding other equipment and accessories, see the instructions that came with those products.

<!-- image -->

ATTENTION: This drive contains electrostatic discharge (ESD) sensitive parts and assemblies. You are required to follow static control precautions when you install, test, service, or repair this assembly. If you do not follow ESD control procedures, components can be damaged. If you are not familiar with static control procedures, see Allen-Bradley® publication 8000-4.5.2 , Guarding Against Electrostatic Damage or any other applicable ESD Protection Handbook.

Follow these steps to mount your Kinetix 300 drive.

1. Lay out the position for the Kinetix 300 drive and accessories in the enclosure.

See Establishing the Noise Zones on page 25 for panel layout recommendations. Mounting hole dimensions for the Kinetix 300 drive are shown in the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005 .

2. Attach the Kinetix 300 drive to the cabinet, first by using the upper mounting slots of the drive and then the lower.

The recommended mounting hardware is M4 (#6-32) steel machine screws torqued to 1.1 N·m (9.8 lb·in). Observe bonding techniques as described in Bonding Drives on page 22 .

## IMPORTANT

To improve the bond between the Kinetix 300 drive and subpanel, construct your subpanel out of zinc plated (paint-free) steel.

3. Tighten all mounting fasteners.

<!-- image -->

## Kinetix 300 Drive Connector Data and Feature Descriptions

| Topic                                       |   Page |
|---------------------------------------------|--------|
| Kinetix 300 Drive Connectors and Indicators |     32 |
| Control Signal Specifications               |     37 |
| Motor Feedback Specifications               |     48 |

## Kinetix 300 Drive Connectors and Indicators

Although the physical sizes of the Kinetix® 300 drives vary, the location of the connectors and indicators is identical.

<!-- image -->

Figure 9 - Kinetix 300 Drive Connector and Indicators

<!-- image -->

Kinetix 300 Drive, Front View (2097-V33PR5 drive is shown)

| Item Description                       |
|----------------------------------------|
| 1 Mains (IPD) connector                |
| 2 Status and diagnostic display        |
| 3 Memory module socket                 |
| 4 Ethernet communication port (Port 1) |
| 5 I/O (IOD) connector                  |
| 6 Motor feedback (MF) connector        |

<!-- image -->

| Item Description                           |
|--------------------------------------------|
| 7 Ground lug                               |
| 8 Shunt resistor and DC bus (BC) connector |
| 9 Back-up power (BP) connector             |
| 10 Display control push buttons (3)        |
| 11 Motor power (MP) connector              |
| 12 Safe Torque Off (STO) connector         |

Table 8 - Kinetix 300 Drive Connectors

| Designator Description             | Connector                            |
|------------------------------------|--------------------------------------|
| IPD AC input power                 | 3-position or 4-position plug/header |
| PORT1 Ethernet communication port  | RJ45 Ethernet                        |
| IOD I/O                            | SCSI 50-pin high-density connector   |
| MF Motor feedback                  | 15-pin high-density D-shell (male)   |
| CPD Back-up power                  | 2-pin quick-connect terminal block   |
| BC Shunt Resistor and DC Bus       | 7-pin quick-connect terminal block   |
| MP Motor power                     | 6-pin quick-connect terminal block   |
| STO Safe Torque Off (STO) terminal | 6-pin quick-connect terminal block   |

## Safe Torque Off Connector Pinout

The Kinetix 300 drive ships with the (6-pin) wiring-plug header that connects your safety circuit to the Kinetix 300 drive Safe Torque Off feature, follow instructions in Safe Torque Off Feature Bypass that begin on page 168 to wire the drive with motion-allowed jumpers.

Figure 10 - Safe Torque Off Connector

<!-- image -->

Table 9 - Kinetix 300 Drive Safe Torque Off Connector Pinout

| STO Pin Description                  | Signal          |
|--------------------------------------|-----------------|
| 1 +24V DC output from the drive      | +24V DC control |
| 2 +24V DC output common              | Control COM     |
| 3 Safety status                      | Safety Status   |
| 4 Safety input 1 (+24V DC to enable) | Safety Input 1  |
| 5 Safety common                      | Safety COM      |
| 6 Safety input 2 (+24V DC to enable) | Safety Input 2  |

## IMPORTANT

Use Pins STO-1 (+24V DC Control) and STO-2 (Control COM) only for the motion-allowed jumpers to defeat the Safe Torque Off function. When the Safe Torque Off function is in operation, the 24V supply must come from an external source.

## I/O Connector Pinout

| IOD Pin Description                           | Signal   |
|-----------------------------------------------|----------|
| 1 Master encoder A+/Step+ input               | MA+      |
| 2 Master encoder A-/Step- input               | MA-      |
| 3 Master encoder B+/Direction+ input MB+      |          |
| 4 Master encoder B-/Direction- input MB-      |          |
| 5 Reserved                                    | —        |
| 6 Reserved                                    | —        |
| 7 Buffered encoder output: channel A+ BA+     |          |
| 8 Buffered encoder output: channel A- BA-     |          |
| 9 Buffered encoder output: channel B+ BB+     |          |
| 10 Buffered encoder output: channel B-        | BB-      |
| 11 Buffered encoder output: channel Z+ BZ+    |          |
| 12 Buffered encoder output: channel Z- BZ-    |          |
| 13…21 Reserved                                | —        |
| 22 Analog common                              | ACOM     |
| 23 Analog output (max 10 mA)                  | AO       |
| 24 Positive (+) of analog signal input        | AIN1+    |
| 25 Negative (-) of analog signal input        | AIN1-    |
| 26 Digital input group ACOM terminal IN_A_COM |          |
| 27 Negative travel limit switch               | IN_A1    |
| 28 Positive travel limit switch               | IN_A2    |
| 29 Inhibit/enable input                       | IN_A3    |

IOD Pin Description

30 Digital input A4

31 Digital input group BCOM terminal

32 Digital input B1

33 Digital input B2

34 Digital input B3

35 Digital input B4

36 Digital input Group CCOM Terminal

37 Digital input C1

38 Digital input C2

39 Registration input sensor

40 Digital input C4

41 Ready output collector

42 Ready output emitter

43 Programmable output #1 collector

44 Programmable output #1 emitter

45 Programmable output #2 collector

46 Programmable output #2 emitter

47 Programmable output #3 collector

48 Programmable output #3 emitter

49 Programmable output #4 collector

50 Programmable output #4 emitter

Figure 11 - Pin Orientation for 50-pin SCSI I/O (IOD) Connector

<!-- image -->

Signal

IN\_A4

IN\_B\_COM

IN\_B1

IN\_B2

IN\_B3

IN\_B4

IN\_C\_COM

IN\_C1

IN\_C2

IN\_C3

IN\_C4

RDY+

RDY-

OUT1-C

OUT1-E

OUT2-C

OUT2-E

OUT3-C

OUT3-E

OUT4-C

OUT4-E

## Motor Feedback (MF) Connector Pinout

| MF Pin Description                                   | Signal       |
|------------------------------------------------------|--------------|
| 1 Sine differential input+ AM+ differential input+   | SIN+ AM+     |
| 2 Sine differential input AM- differential input                                                      | SIN AM              |
| 3 Cosine differential input+ BM+ differential input+ | COS+ BM+     |
| 4 Cosine differential input BM- differential input                                                      | COS BM              |
| 5 Data differential input + Index pulse+             | DATA+ IM+    |
| 6 Common                                             | ECOM         |
| 7 Encoder power (+9V)                                | EPWR_9V  (2) |
| 8 Single-ended 5V Hall effect commutation            | S3           |

<!-- image -->

ATTENTION: To avoid damage to components, determine which power supply your encoder requires and connect the encoder power to either the 5V or 9V supply, but not both.

## IMPORTANT

Drive-to-motor power and feedback cable length must not exceed 20 m (65.6 ft). System performance was tested at these specifications and also applies when meeting CE requirements.

Figure 12 - Pin Orientation for 15-pin Motor Feedback (MF) Connector

<!-- image -->

## Ethernet Communication Connector Pinout

— 8—

| Port 1 Pin Description                 | Signal   |
|----------------------------------------|----------|
| 1 Transmit Port (+) Data Terminal + TX |          |
| 2 Transmit Port (-) Data Terminal - TX |          |
| 3 Receive Port (+) Data Terminal + RX  |          |
| 4 —                                    |          |

| Port 1 Pin Description                | Signal   |
|---------------------------------------|----------|
| 5 —                                   | —        |
| 6 Receive Port (-) Data Terminal - RX |          |
| 7 —                                   | —        |
|                                       | —        |

Figure 13 - Pin Orientation for 8-pin Ethernet Communication Port

<!-- image -->

| MF Pin Description                             | Signal       |
|------------------------------------------------|--------------|
| 9 Reserved                                     | —            |
| 10 Data differential input - Index pulse                                                | DATA IM              |
| 11 Motor thermal switch (normally closed)  (1) | TS           |
| 12 Single-ended 5V Hall effect commutation S1  |              |
| 13 Single-ended 5V Hall effect commutation S2  |              |
| 14 Encoder power (+5V)                         | EPWR_5V  (2) |
| 15 Reserved                                    | —            |

## AC Input Power Connector Pinout

| IPD Designator   | Description (2097-V31PRx drives) Signal IPD   |    |
|------------------|-----------------------------------------------|----|
|                  | L2/N AC Power In (non-doubler operation) L2/N |    |
|                  | L1 AC Power In                                | L1 |
| N                | AC Power Neutral (120V doubler only) N        |    |
|                  | PE Protective Earth (ground)                  | PE |

| Description (2097-V32PRx drives) Signal   |    |
|-------------------------------------------|----|
| L2 AC Power In                            | L2 |
| L1 AC Power In                            | L1 |
| PE Protective Earth (ground)              | PE |

| IPD Designator Description (2097-V33PRx, and 2097-V34PRx  drives)   | Signal   |
|---------------------------------------------------------------------|----------|
| L3 AC Power In (three-phase models)                                 | L3       |
| L2 AC Power In                                                      | L2       |
| L1 AC Power In                                                      | L1       |
| PE Protective Earth (ground)                                        | PE       |

## Back-up Power Connector Pinout

| BP Designator Description   |                            | Signal   |
|-----------------------------|----------------------------|----------|
| +24V                        | Positive 24V DC            | +24V DC  |
| -24V                        | 24V DC power supply return | Return   |

## Shunt Resistor and DC Bus Connector Pinout

| BC Designator Description   |                                | Signal   |
|-----------------------------|--------------------------------|----------|
| +                           | Positive DC bus/Shunt resistor | +        |
|                             | + +                            |          |
| SH                          | Shunt Resistor                 | SH       |
| -                           | Negative DC bus                | -        |
|                             | - -                            |          |

## Motor-Power Connector Pinout

| MP Designator Description   |                           | Signal   |
|-----------------------------|---------------------------|----------|
| PE                          | Protective Earth (ground) | PE       |
| W                           | Motor power out           | W        |
| V                           | Motor power out           | V        |
| U                           | Motor power out           | U        |

## Control Signal Specifications

This section provides a description of the Kinetix 300 drive I/O (IOD), communication, shunt resistor, and DC bus (BC), and back-up power (BP) connectors.

## Digital Inputs

The Kinetix 300 drive has 12 digital inputs. They can be used for travel limit switches, proximity sensors, push buttons, and hand shake with other devices. Each input can be assigned an individual de-bounce time via MotionView software or Explicit Messaging.

The inputs are separated into three groups: A, B, and C. Each group has four inputs and share one common: ACOM, BCOM, and CCOM respectively.

Travel limit switches, the inhibit/enable input, and registration input have dedicated inputs as shown in Table 10. For more information on the overtravel inputs, see Appendix E on page 219 .

Table 10 - Digital Input Assignments

| Digital Input Function   |                                    |
|--------------------------|------------------------------------|
|                          | IN_A1 Negative travel-limit switch |
|                          | IN_A2 Positive travel-limit switch |
| IN_A3                    | Inhibit/enable input               |
| IN_A4                    | N/A                                |
| IN_B1                    | N/A                                |
| IN_B2                    | N/A                                |
| IN_B3                    | N/A                                |
| IN_B4                    | N/A                                |
| IN_C1                    | N/A                                |
| IN_C2                    | N/A                                |
| IN_C3                    | Registration input sensor          |
| IN_C4                    | N/A                                |

You can configure the inputs that are listed as N/A for any of these functions.

- Abort Homing
- Abort Index
- Start Homing
- Start Index
- Fault Reset
- Home Sensor
- Index Select

Some of the digital inputs exercise control over functions under the control of the Output Assembly. When a digital input is mapped to the same function as exists in the Output Assembly, the following timing diagrams apply.

Figure 14 - Enable Timing Diagram (enable switch function that is configured for Run)

<!-- image -->

## IMPORTANT

Do not use the EtherNet/IP™ network for control and for configuring the Enable switch function for Run.

Table 11 - Enable Truth Table (configured for Run)

| Drive Input                              | Value    | Value      |
|------------------------------------------|----------|------------|
| Enable Input                             | Off      | Move to On |
| Drive Enable bit in Output Assembly  (1) |          | – On       |
| Resulting Drive State                    | Disabled | Enabled    |

Figure 15 - Enable Timing Diagram (enable switch function that is configured for Inhibit)

<!-- image -->

Table 12 - Enable Truth Table (configured for Inhibit)

| Drive Input                                                  | Value   | Value                     | Value   |
|--------------------------------------------------------------|---------|---------------------------|---------|
| Enable Input                                                 | On      | On  Off                   |         |
| Drive Enable bit in Output Assembly Move to On Move to Off – |         |                           |         |
| Resulting Drive State                                        |         | Enabled Disabled Disabled |         |

Figure 16 - Homing Timing Diagram

<!-- image -->

Table 13 - Homing Truth Table

| Drive Input                                                        | Value   | Value                       | Value                       | Value   | Value   | Value   |
|--------------------------------------------------------------------|---------|-----------------------------|-----------------------------|---------|---------|---------|
| Start Homing Input — — Move to On — — —                            |         |                             |                             |         |         |         |
| Start Homing bit in Output Assembly                                |         | — — — Move to On — —        |                             |         |         |         |
| Abort Homing Input On — Off Off Move to On —                       |         |                             |                             |         |         |         |
| Abort Homing bit in Output Assembly                                |         |                             | — On Off Off — Move to On   |         |         |         |
| Previous Drive State Enabled Enabled Enabled Enabled Homing Homing |         |                             |                             |         |         |         |
| Resulting Drive State Will not Will not home                       | home    | Starts homing Starts homing | Aborts homing Aborts homing |         |         |         |

Figure 17 - Indexing Timing Diagram

<!-- image -->

TIP The drive must be enabled for homing and indexing mode.

Table 14 - Indexing Truth Table

| Drive Input                                                            | Value   | Value                           | Value                           | Value   | Value   | Value   |
|------------------------------------------------------------------------|---------|---------------------------------|---------------------------------|---------|---------|---------|
| Start Index Input — — Move to On — — —                                 |         |                                 |                                 |         |         |         |
| Start Motion bit in Output Assembly                                    |         | — — — Move to On — —            |                                 |         |         |         |
| Abort Index Input On — Off Off Move to On —                            |         |                                 |                                 |         |         |         |
| Abort Index bit in Output Assembly                                     |         |                                 | — On Off Off — Move to On       |         |         |         |
| Previous Drive State Enabled Enabled Enabled Enabled Indexing Indexing |         |                                 |                                 |         |         |         |
| Resulting Drive State Will not Will not index                          | index   | Starts indexing Starts indexing | Aborts indexing Aborts Indexing |         |         |         |

The digital inputs are optically isolated and sink up to 24V DC. Electrical details are shown in Table 15 on page 41. You can configure the inputs for PNP sourcing or NPN sinking.

Figure 18 - Sourcing of Digital Inputs

<!-- image -->

Figure 19 - Sinking of Digital Inputs

<!-- image -->

Table 15 - Digital Input Signal Specifications

| Parameter       | Value           |
|-----------------|-----------------|
| Scan time       | 500 µs          |
| Current, max    | 9 mA, typical   |
| Input impedance | 1.2 k, typical |
| Voltage range   | 5…24V DC        |

## Digital Outputs

There are five digital outputs, OUT1…OUT4 and RDY, available on the IOD connector. Outputs are optically isolated open collector/emitter and are fully isolated from the drive circuits. Each output, OUT1…OUT4, can be assigned to one of these functions:

- Not assigned
- Zero speed
- In-speed window
- Current limit
- Runtime fault
- Ready
- Brake (motor brake release)

The Ready Output has a fixed function that becomes active when the drive is enabled and the output power transistors become energized.

Table 16 - Digital Output Signal Specifications

| Parameter    | Value   |
|--------------|---------|
| Scan time    | 500 µs  |
| Current, max | 100 mA  |
| Voltage, max | 30V DC  |

Figure 20 - Digital Output Circuit

<!-- image -->

## Analog Reference Input

The analog reference input AIN1+ and AIN1- (IOD-24 and IOD-25) accepts up to a ±10V DC analog signal as shown in Table 17. The analog signal is converted to a digital value with 12-bit resolution (11 bit plus sign). The total reference voltage as seen by the drive is the voltage difference between AIN1+ and AIN1-. If used in Single-ended mode, one of the inputs must be connected to a voltage source while the other one must be connected to Analog Common (ACOM). If used in Differential mode, the voltage source is connected across AIN1+ and AIN1- and the driving circuit common, if available, is connected to the drive Analog Common (ACOM) terminal.

Table 17 - Analog Signal Input Specifications

| Parameter       | Value          |
|-----------------|----------------|
| Scan time       | 0.0625 ms      |
| Current, max    | Depend on load |
| Input impedance | 47 k, typical |
| Voltage range   | -10…10V DC     |

## Analog Output

The analog output (AO) on pin IOD-23 has a 10-bit resolution. The analog output is a single-ended signal and referenced to Analog Common (ACOM) that can be the following motor data:

- Not Assigned
- RMS Phase Current
- RMS Peak Current
- Motor Velocity
- Phase Current U
- Phase Current V
- Phase Current W
- Iq Current
- Id Current

## IMPORTANT

Output values can vary during powerup until the specified power supply voltage is reached.

MotionView software refers to Phase Current U, V, and W as R, S, and T respectively.

Figure 21 - Analog Output Circuit

<!-- image -->

Table 18 - Analog Output Specifications

| Parameter     | Value      |
|---------------|------------|
| Scan time     | 0.0625 ms  |
| Current, max  | 10 mA      |
| Voltage range | -10…10V DC |

For configuration/setup of the analog outputs, see Configure the Drive Parameters and System Variables beginning on page 145 .

## Master Gearing/Step and Direction Inputs

You can connect a master encoder with quadrature outputs to the Kinetix 300 drive and control position in the Master Gearing operating mode.

You can connect a step and direction signal pair to the Kinetix 300 drive and control position in the Step and Direction operating mode.

These inputs are optically isolated from the rest of the drive circuits and from each other. Both inputs can operate from any voltage source in the range of 5…24V DC and do not require extra series resistors for normal operation.

IMPORTANT Master gearing inputs must be incremental encoders with TTL outputs.

Figure 22 - Step and Direction Timing Diagram

<!-- image -->

Figure 23 - Master Encoder Timing Diagram

<!-- image -->

Table 19 - Input Type and Output Compatibility

| Attribute                          | Value    |
|------------------------------------|----------|
| Recommended voltage                | 5…24V DC |
| Input frequency, max               | 2 MHz    |
| Pulse width (negative or positive) | 500 ns   |
| Input impedance                    | 700     |

Figure 24 - Master Gearing/Step and Direction Input Circuit Diagram

<!-- image -->

Differential signal inputs are preferred when using master gearing/step and direction. When using differential signal inputs, sinking or sourcing outputs can be used. Single-ended inputs can be used but are not recommended. Sinking type outputs cannot be used if single-ended inputs are used. The function of the master gearing/step and direction inputs is software selectable. Use the MotionView software, General category, to choose the desirable function.

An external pulse-train signal (step) supplied by an external device, such as a PLC or stepper indexer, can control the speed and position of the servo motor. The frequency of the step signal controls the speed of the motor. The number of pulses that are supplied to the Kinetix 300 drive determines the position of the servo motor. Direction input controls direction of the motion.

## Buffered Encoder Outputs

There are many applications where it is desired to close the feedback loop to an external device. This feature is accessible through the buffered encoder output connections (IOD-7…IOD-12) for TTL differential line encoder types. A master drive that powers a motor with a SICK-Stegmann high-resolution encoder generates buffered-encoder outputs for master gearing to a slave drive. However, a Tamagawa high-resolution encoder does not.

## IMPORTANT

The buffered encoder outputs are not supported with Tamagawa highresolution motor feedback.

If a motor with encoder feedback is being used, the A+, A-, B+, B-, Z+, and Zsignals are passed directly through drive pins IOD-7…IOD-12 with no filtering, up to a speed of 2 MHz. The encoder pass through delay is approximately 100 ns.

## Ethernet Connections

An RJ45 Ethernet connector (port 1) is provided on the Kinetix 300 drive.

Table 20 - Ethernet Communication Specifications

| Attribute                                        | Value                                                  |
|--------------------------------------------------|--------------------------------------------------------|
| Communication                                    | 100BASE-TX, full-duplex                                |
| Cyclic update period                             | 2 ms, min                                              |
| Auto MDI/MDIX crossover detection/correction Yes |                                                        |
| Cable                                            | CAT5E or CAT6, unshielded, or shielded, 100 m (328 ft) |

## 24V DC Back-up Power

The Kinetix 300 drive can use an external power supply to power the logic and communication circuits. If an independent 24V (@ 1 A) power supply is connected to the BP connector, the logic and communication circuits remain active during a mains input-power loss.

Table 21 - 24V DC Back-up Power Specifications

| Attribute     | Value     |
|---------------|-----------|
| Input voltage | 20…26V DC |
| Current       | 500 mA    |
| Inrush, max   | 30 A      |

## Motor Feedback Specifications

The Kinetix 300 drive accepts motor feedback signals from the following types of encoders with these general specifications.

Table 22 - Motor Feedback General Specifications

| Attribute                     | Motor Feedback                                                               |
|-------------------------------|------------------------------------------------------------------------------|
| Feedback device support       | • SICK-Stegmann Hiperface • Generic TTL Incremental • Tamagawa 17 bit Serial |
| Power supply voltage (EPWR5V) | 5.13…5.67V                                                                   |
| Power supply current (EPWR5V) | 400 mA, max  (1)(2)                                                          |
| Power supply voltage (EPWR9V) | 8.3…9.9V                                                                     |
| Power supply current (EPWR9V) | 275 mA, max  (2)(3)                                                          |
| Thermostat                    | Single-ended, under 500 = no fault, over 10 k= fault                     |

TIP Auto configuration is possible by using the Kinetix 300 drive MotionView OnBoard software for Allen-Bradley® motors.

## Motor Feedback Specifications

The Kinetix 300 drives support multiple types of feedback devices by using the 15-pin (MF) motor feedback connector and by sharing connector pins in many cases.

Table 23 - Motor Feedback Signals by Device Type

| MF Pin SICK-Stegmann Hiperface Generic TTL Incremental Tamagawa 17 bit Serial   |                   |
|---------------------------------------------------------------------------------|-------------------|
| 1 SIN+ AM+ —                                                                    |                   |
| 2 SIN- AM- —                                                                    |                   |
| 3 COS+ BM+ —                                                                    |                   |
| 4 COS- BM- —                                                                    |                   |
|                                                                                 | 5 DATA+ IM+ DATA+ |
| 6 ECOM ECOM ECOM                                                                |                   |
| 7 EPWR9V — —                                                                    |                   |
| 8 — S3                                                                          | —                 |
| 9— —                                                                            | —                 |
| IM-                                                                             | 10 DATA-  DATA                   |
| TS                                                                              | 11 TS  —          |
| S1                                                                              | 12 —  —           |
| S2                                                                              | 13 —  —           |
| EPWR5V                                                                          | 14 —  EPWR5V      |
| —                                                                               | 15 —  —           |

Figure 25 is the motor-thermostat interface schematic. Although the thermostat signal is shown for all feedback types, some motors do not support this feature because it is not part of the feedback device.

Figure 25 - Motor Thermostat Interface

<!-- image -->

Table 24 - Motor Thermostat State Specifications

| State    | Resistance at TS   |
|----------|--------------------|
| No Fault | 500               |
| Fault    | 10 k              |

Table 25 - SICK-Stegmann Hiperface Specifications

| Attribute                                         | Value                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------|
| Protocol                                          | Hiperface                                                                       |
| Memory support                                    | Not programmed, or programmed with Allen-Bradley® motor data                    |
|                                                   | Hiperface data communication RS-485, 9600 communication, 8 data bits, no parity |
| Sine/Cosine interpolation 2048 counts/sine period |                                                                                 |
| Input frequency (AM/BM) 250 kHz, max              |                                                                                 |
| Input voltage (AM/BM)                             | 0.6...1.2V, p-p, which is measured at the drive inputs                          |
| Line loss detection (AM/BM) Average (sin          | 2 + cos 2 ) > constant                                                          |

Figure 26 - SICK-Stegmann Hiperface Interface, SIN and COS Signals

<!-- image -->

Figure 27 - SICK-Stegmann Hiperface Interface, DATA Signals

<!-- image -->

Table 26 - Generic TTL Incremental Specifications

| Attribute                                   | Value                                      |
|---------------------------------------------|--------------------------------------------|
| TTL incremental encoder support             | 5V, differential A quad B                  |
| Quadrature interpolation                    | 4 counts/square wave period                |
| Differential input voltage (AM, BM, and IM) | 1.0…7.0V                                   |
| DC current draw (AM, BM, and IM)            | 30 mA, max                                 |
| Input signal frequency (AM, BM, and IM)     | 5.0 MHz, max                               |
| Edge separation (AM and BM)                 | 42 ns min, between any two edges           |
| Line loss detection (AM and BM)             | Average (AM 2 + BM 2 ) > constant          |
| Hall inputs (S1, S2, and S3)                | Single-ended, TTL, open collector, or none |

Figure 28 - Generic TTL Incremental, AM and BM Signals

<!-- image -->

Figure 29 - Generic TTL Interface, IM Signals

<!-- image -->

Figure 30 - Generic TTL Interface, S1, S2, or S3 Signals

<!-- image -->

Table 27 - Tamagawa 17-bit Serial Specifications

| Attribute                  | Value                                                        |
|----------------------------|--------------------------------------------------------------|
| Tamagawa model support     | TS5669N124                                                   |
| Protocol                   | Tamagawa proprietary                                         |
| Memory support             | Programmed with Allen-Bradley motor data                     |
| Differential input voltage | 1.0…7.0V                                                     |
| Data communication         | 2.5 Mbps, 8 data bits, no parity                             |
| Battery                    | 3.6V, located external to drive in Low Profile connector kit |

See Figure 27 for the Tamagawa 17-bit serial interface schematic. It is identical to the SICK-Stegmann Hiperface (DATA) signals schematic.

## Feedback Power Supply

The Kinetix 300 drive generates +5V and +9V DC for motor feedback power. Short circuit protection and separate common mode filtering for each channel is included.

Table 28 - Motor Feedback Power Specifications

| Voltage                 | Voltage                 | Current mA   | Current mA   |
|-------------------------|-------------------------|--------------|--------------|
|                         | Min Nominal Max Min Max |              |              |
| +5V DC EPWR_5V 5.13 5.4 |                         | 5.67 0       | 400          |
| +9V DC EPWR_9V 8.3      | 9.1  9.9                | 0            | 275          |

Figure 31 - Pin Orientation for 15-pin Motor Feedback (MF) Connector

<!-- image -->

## Notes:

## Basic Wiring Requirements

<!-- image -->

## Connecting the Kinetix 300 Drive System

| Topic                                                |   Page |
|------------------------------------------------------|--------|
| Basic Wiring Requirements                            |     55 |
| Ground Your Kinetix 300 Drive System                 |     62 |
| Power Wiring Requirements                            |     63 |
| Wiring Guidelines                                    |     65 |
| Wiring the Kinetix 300 Drive Connectors              |     66 |
| Apply the Motor-Cable Shield Clamp                   |     73 |
| Feedback and I/O Cable Connections                   |     74 |
| Wiring the Feedback and I/O Connectors               |     76 |
| Kinetix 300 Drive (IOD connector and terminal block) |     76 |
| Shunt Resistor Connections                           |     78 |
| Ethernet Cable Connections                           |     79 |

This section contains basic information on how to wire the Kinetix® 300 drive.

<!-- image -->

ATTENTION: Plan the installation of your system so that you can cut, drill, tap, and weld with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry, which can result in damage to components.

<!-- image -->

SHOCK HAZARD: To avoid a hazard of electrical shock, mount and wiry the Bulletin 2097 drive before you apply power. Once power is applied, connector terminals can have voltage present even when not in use.

## IMPORTANT

This section contains common PWM servo system wire configurations, size, and practices that can be used in most applications. National Electrical Code, local electrical codes, special operating temperatures, duty cycles, or system configurations take precedence over the values and methods provided.

## Determine the Input Power Configuration

## Build Your Own Cables

## IMPORTANT

Factory-made cables are designed to minimize EMI and are recommended over hand-built cables to optimize system performance.

- Connect the cable shield to the connector shells on both ends of the cable with a complete 360° connection.
- Use twisted-pair cable whenever possible. Twist differential signals with each other and twist single-ended signals with the appropriate ground return.

See the Kinetix Motion Control Selection Guide, publication KNX-SG001 , for Low Profile connector kit, drive-end (mating) connector kit, and motorend connector kit catalog numbers.

## Route Power and Signal Wiring

When you route power and signal wiring on a machine or system, radiated noise from nearby relays, transformers, and other electronic drives can be induced into motor or encoder feedback signals, input/output communication, or other sensitive low voltage signals. Radiated noise can cause system faults and communication anomalies.

See Electrical Noise Reduction on page 22 for examples of routing high and low voltage cables in wireways. See the System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001, for more information.

This section contains examples of typical single-phase and three-phase facility input power that is wired to single-phase and three-phase Kinetix 300 drives.

The grounded power configuration lets you ground your single-phase or threephase power at a neutral point. Match your secondary to one of the examples and be certain to include the grounded neutral connection.

See Table 93 on page 224 on for more information on leakage current.

## Three-phase Power Wired to Three-phase Drives

These examples illustrate grounded three-phase power that is wired to threephase Kinetix 300 drives when phase-to-phase voltage is within drive specifications.

Figure 32 - Three-phase (400/480V) Power Configuration (Wye secondary)

<!-- image -->

<!-- image -->

ATTENTION: For the 480V Kinetix 300 drives to meet proper voltage creepage and clearance requirements, each phase voltage to ground must be less than or equal to 300V AC rms. This means that the power system must use center grounded wye secondary configuration for 400/480V AC mains.

See Table 93 on page 224 for leakage currents.

Figure 33 - Three-phase (240V) Power Configuration (Delta secondary)

<!-- image -->

- (1) Leakage current from the line filter, in this configuration, typically is higher than a balanced (center ground) configuration.
- (1) Leakage current from the line filter, in this configuration, typically is higher than a balanced (center ground) configuration.

Figure 34 - Three-phase (240V) Power Configuration (Delta secondary)

<!-- image -->

## Single-phase Power Wired to Single-phase Drives

These examples illustrate grounded single-phase power that is wired to singlephase Kinetix 300 drives when phase-to-phase voltage is within drive specifications.

## IMPORTANT

The 2097-V32PRx models have integrated AC line filters and do not require the AC line filter that is shown in this diagram.

Figure 35 - Single-phase Grounded Power Configurations

<!-- image -->

- (1) This configuration applies to voltage-doubler operation for 2097-V31PRx drives.

Reducing the transformer output reduces motor speed. Feeder and branch short-circuit protection is not illustrated.

## Voltage Doubler Operation

You can wire the 2097-V31PRx drives with 120V input power and achieve twice the output voltage at half the output current, while maintaining the same output power. To use the voltage-doubler circuit, connect the 120V singlephase input power to the IPD-L1 and IPD-N terminals.

For Kinetix 300 drive power specifications, see the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005. For Kinetix 300 drive-input wiring diagrams, see Power Wiring Examples on page 175 .

## Isolation Transformer in Grounded Power Configurations

When using an isolation transformer, attach a chassis ground wire to the neutral connection. This grounded neutral connection does the following:

- Helps prevent the system from floating and avoids any high voltages that can otherwise occur, for example due to static electricity
- Provides a solid earth path for fault conditions

<!-- image -->

ATTENTION: If the supply transformer is an auto transformer (not recommended), a chassis earth ground must not be added. A chassis earth ground must already be included elsewhere in the system and if you add another it would create a short.

## Three-phase Power Wired to Single-phase Drives

This example illustrates grounded three-phase power that is wired to singlephase Kinetix 300 drives when phase-to-phase voltage is within drive specifications.

Figure 36 - Single-phase Amplifiers on Three-phase Power (Wye)

<!-- image -->

- (1) Contactors (MI, M2, and M3) can be optional. For more information, see Understanding the Machinery Directive, publication SHB-900. AC line filter is optional, but is required for CE compliance.

Feeder short-circuit protection is not illustrated.

This example illustrates grounded three-phase power that is wired to singlephase Kinetix 300 drives when phase-to-phase voltage exceeds drive specifications.

A neutral must be connected when single-phase drives are attached to a threephase isolating transformer secondary. It is not necessary that all three-phases be loaded with drives, but each drive must have its power return via the neutral connection.

<!-- image -->

ATTENTION: Failure to connect the neutral can result in supply voltage swings at the individual drives. Voltage swings occur when the neutral point moves in a vectorial as a result of load variations that experienced by the individual drives. The supply voltage swing can cause undervoltage and overvoltage trips on the drives, and the drive can be damaged if the overvoltage limit is exceeded.

Figure 37 - Single-phase Amplifiers (one AC line filter per drive)

<!-- image -->

Feeder and branch short-circuit protection is not illustrated.

IMPORTANT An EMC line filter for each drive is the preferred configuration, and required for CE compliance.

If a three-phase line filter is used to feed multiple single-phase drives (not recommended), it is important that the filter is on a neutral connection as shown in Figure 37. The neutral connection applies if three-phase is brought directly into the filter and no isolating transformer is present.

## Voiding of CE Compliance

The three-phase and neutral in-line filter applications that are described in Figure 37 cannot be adequate from an EMC aspect for CE compliance. Therefore, EMC validity and CE Mark by Rockwell Automation is voided when three-phase and neutral in line filters are used.

<!-- image -->

ATTENTION: The three-phase isolation transformer and neutral in-line filter applications that are described in this document have not been tested for EMC by Rockwell Automation and products that are used in such installations are not considered CE Marked by Rockwell Automation.

If this three-phase isolation transformer and neutral in-line filter application is used, the responsibility for EMC validation and CE Mark of the system lies with the user.

If CE compliance is a customer requirement, single-phase line filters, tested by Rockwell Automation, and specified for the product must be used. See the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005, for catalog numbers.

## Ground Your Kinetix 300 Drive System

All equipment and components of a machine or process system must have a common earth ground point that is connected to their chassis. A grounded system provides a safety ground path for short circuit protection. Ground your modules and panels to minimize shock hazard to personnel and damage to equipment caused by short circuits, transient overvoltages, and accidental connection of energized conductors to the equipment chassis. For CE ground requirements, see CE Requirements on page 14 .

## IMPORTANT

To improve the bond between the Kinetix 300 drive and subpanel, construct your subpanel out of zinc-plated (paint-free) steel.

## Ground Your Drive to the System Subpanel

<!-- image -->

ATTENTION: The National Electrical Code contains ground requirements, conventions, and definitions. Follow all applicable local codes and regulations to ground your system safely. See the illustration Figure 38 for details on how to ground your Kinetix 300 drive. See Appendix A on page 173 for the power wiring diagram for your Kinetix 300 drive.

If the Kinetix 300 drive is mounted on a painted subpanel, ground the drive to a bonded cabinet ground bus by using a braided ground strap or 4.0 mm 2 (12 AWG) solid copper wire 100 mm (3.9 in.) long.

Figure 38 - Connect the Braided Ground Strap - Example

<!-- image -->

For drive dimensions, See the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005 .

## Power Wiring Requirements

Figure 39 - Chassis Ground Configuration (multiple Kinetix 300 drives on one panel)

<!-- image -->

## Ground Multiple Subpanels

To ground multiple subpanels, see Figure 40. HF bonding is not illustrated. For information, see Bonding Multiple Subpanels on page 24 .

Figure 40 - Subpanels Connected to a Single Ground Point

<!-- image -->

Wire must be copper with 75 °C (167 °F) minimum rating. Phasing of main AC power is arbitrary and earth ground connection is required for improve safety and proper operation.

See Power Wiring Examples on page 175 for interconnect diagrams.

## IMPORTANT

The National Electrical Code and local electrical codes take precedence over the values and methods provided.

Table 29 - Kinetix 300 Drive-Power Wiring Requirements

| Cat. No.                                                                                                                | Description                          | Terminals                                   |                                                     |                                |              | Recommended Wire Size mm 2 (AWG)   | Strip Length Torque Value N•m (lb•in)   |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------|---------------------------------------------|-----------------------------------------------------|--------------------------------|--------------|------------------------------------|-----------------------------------------|
|                                                                                                                         |                                      |                                             | Pins Signals                                        |                                |              |                                    | mm (in.)                                |
| 2097-V31PR0 2097-V32PR0 2097-V32PR2 2097-V33PR1 2097-V33PR3 2097-V34PR3 2097-V34PR5 2097-V34PR6                         | Mains input power (IPD connector)    |                                             | L3 L2 L1 PE (1)                                     | L2/N L1 N PE (2)               | L2 L1 PE (3) | 2.5 (14)                           | 7 (0.28) 0.5 (4.5)                      |
| 2097-V32PR4 2097-V33PR5                                                                                                 |                                      |                                             |                                                     |                                |              | 4.0 (12)                           | 7 (0.28) 0.5 (4.5)                      |
| 2097-V31PR2 2097-V33PR6                                                                                                 |                                      |                                             |                                                     |                                |              | 6.0 (10)                           | 7 (0.28)  0.56…0.79 (5.0…7.0)           |
| 2097-V31PR2 2097-V32PR0 2097-V32PR2 2097-V32PR4 2097-V33PR1 2097-V33PR3 2097-V33PR5 2097-V34PR3 2097-V34PR5             | Motor power (MP connector)           | PE W V U                                    |                                                     |                                |              | 2.5 (14)                           | 7 (0.28) 0.5 (4.5)                      |
| 2097-V33PR6                                                                                                             |                                      |                                             |                                                     |                                |              | 4.0 (12)                           | 7 (0.28) 0.5 (4.5)                      |
| 2097-V31PR0 2097-V31PR2 2097-V32PR0 2097-V32PR2 2097-V32PR4 2097-V33PR1 2097-V33PR3 2097-V33PR5 2097-V34PR3 2097-V34PR5 | Shunt /DC Bus (4) (BC connector)     |                                             | + + SH - -                                          |                                |              | 2.5 (14)                           | 7 (0.28) 0.5 (4.5)                      |
| 2097-V33PR6                                                                                                             |                                      |                                             |                                                     |                                |              | 4.0 (12)                           | 7 (0.28) 0.5 (4.5)                      |
| 2097-V3xPRx                                                                                                             | Control back-up power (BP connector) |                                             | +24V DC -24V DC                                     |                                |              |                                    | 6 (0.25) 0.5 (4.5)                      |
| 2097-V3xPRx                                                                                                             | Safe Torque Off (STO connector)      | STO-1 (5) STO-2 (5) STO-3 STO-4 STO-5 STO-6 | Control COM Safety Status Safety Input 1 Safety COM | +24V DC Control Safety Input 2 |              | 1.5 (16)                           |                                         |

## Wiring Guidelines

<!-- image -->

ATTENTION: To avoid personal injury and equipment damage, make sure that the system installation complies with specifications for wire types, conductor sizes, branch circuit protection, and disconnect devices. The National Electrical Code (NEC) and local codes outline provisions for safely installing electrical equipment.

To avoid personal injury and equipment damage, make sure that motor power connectors are used for connection purposes only. Do not use them to turn the unit on and off.

To avoid personal injury and equipment damage, make sure that shielded power cables are grounded to help prevent potentially high voltages on the shield.

Use these guidelines as a reference when wiring the connectors on your Kinetix 300 drive power modules.

## IMPORTANT

## IMPORTANT

For connector locations of the Kinetix 300 drives, see Kinetix 300 Drive Connectors and Indicators on page 32 .

When you tighten screws to secure the wires, see the tables beginning on page 63 for torque values.

When you remove insulation from wires, see the tables beginning on page 63 for strip lengths.

To improve system performance, run wires and cables in the wireways as established in Establishing the Noise Zones on page 25 .

Follow these steps when wiring the connectors on your Kinetix 300 drive modules.

1. Prepare the wires for attachment to each connector plug by removing insulation equal to the recommended strip length.

## IMPORTANT

Use caution not to nick, cut, or otherwise damage strands as you remove the insulation.

2. Route the cable/wires to your Kinetix 300 drive.
3. Insert wires into connector plugs.

See connector pinout tables in Chapter 3 or the interconnect diagrams in Appendix A .

4. Tighten the connector screws.
5. Gently pull on each wire to make sure that it does not come out of its terminal; reinsert and tighten any loose wires.
6. Insert the connector plug into the module connector.

## Wiring the Kinetix 300 Drive Connectors

This section provides examples and wiring tables to assist you in while you make connections to the Kinetix 300 drive.

## Wire the Safe Torque Off (STO) Connector

For the Safe Torque Off (STO) connector pinouts, feature descriptions, and wiring information, see Chapter 8 on page 161.

## Wire the Back-up Power (BP) Connector

<!-- image -->

Table 30 - Back-up Power (BP) Connector

| Drive Cat. No. Terminals   |                 | Recommended Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|----------------------------|-----------------|------------------------------------|-------------------------|----------------------------|
| 2097-V3xPRx                | +24V DC -24V DC | 1.5 (16)                           |                         | 6 (0.25) 0.5 (4.5)         |

## Wire the Input Power (IPD) Connector

<!-- image -->

Table 31 - Input Power (IPD) Connector

| Drive Cat. No.                                                                                  | Terminals       | Terminals        | Terminals    | Recommended Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-------------------------------------------------------------------------------------------------|-----------------|------------------|--------------|------------------------------------|-------------------------|----------------------------|
| 2097-V31PR0 2097-V32PR0 2097-V32PR2 2097-V33PR1 2097-V33PR3 2097-V34PR3 2097-V34PR5 2097-V34PR6 | L3 L2 L1 PE (1) | L2/N L1 N PE (2) | L2 L1 PE (3) | 2.5 (14)                           |                         | 7 (0.28) 0.5 (4.5)         |
| 2097-V32PR4 2097-V33PR5                                                                         | L3 L2 L1 PE (1) |                  |              | 4.0 (12)                           |                         | 7 (0.28) 0.5 (4.5)         |
| 2097-V31PR2 2097-V33PR6                                                                         | L3 L2 L1 PE (1) |                  |              | 6.0 (10)                           | 7 (0.28)                | 0.56…0.79 (5.0…7.0)        |

(1) Applies to 2097-V33PRx, and 2097-V34PRx drive modules.

- (2) Applies to 2097-V31PRx drive modules.

(3) Applies to 2097-V32PRx drive modules.

## Wire the Motor Power (MP) Connector

Connections to the motor power (MP) connector include rotary motors, and rotary motor driven actuators.

Figure 41 - Motor Power (MP) Connector

<!-- image -->

Table 32 - Motor Power (MP) Termination Specifications

| Drive Cat. No. Terminals                                                                                                            |                      | Recommended Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------|-------------------------|----------------------------|
| 2097-V31PR0 2097-V31PR2 2097-V32PR0 2097-V32PR2 2097-V32PR4 2097-V33PR1 2097-V33PR3 2097-V33PR5 2097-V34PR3 2097-V34PR5 2097-V34PR6 | PE W V U             | 2.5 (14)                           |                         | 7 (0.28) 0.5 (4.5)         |
|                                                                                                                                     | 2097-V33PR6 4.0 (12) |                                    |                         |                            |

## Cable Shield Terminations

Factory-supplied motor power cables for Kinetix MP and Kinetix TL motors and actuator are shielded. The braided cable shield must end near the drive during installation. Remove a small portion of the cable jacket to expose the shield braid and clamp the exposed shield to the panel.

<!-- image -->

ATTENTION: To avoid a hazard of electrical shock, help ensure that shielded power cables are grounded at a minimum of one point for safety.

## IMPORTANT

For Kinetix TL motors, also connect the 152 mm (6.0 in.) termination wire to the closest earth ground.

See Pigtail Terminations on page 69 for more information.

## Pigtail Terminations

Kinetix TL motors have a short pigtail cable that connects to the motor, but is not shielded. The preferred method for grounding the Kinetix TL power cable on the motor side is to expose a section of the cable shield and clamp it directly to the machine frame. The motor power cable also has a 150 mm (6.0 in.) shield termination wire with a ring lug that connects to the closest earth ground. Use this method and the cable clamp. The termination wire can be extended to the full length of the motor pigtail if necessary, but it is best to connect the supplied wire directly to ground without lengthening.

Figure 42 - Pigtail Terminations

<!-- image -->

Table 33 - Motor-Power Cable Compatibility

| Motor/Actuator             | Connector Type          | Motor/Actuator Cat. No.                                                                        | Motor Power Cables (with brake wires)                                   | Motor Power Cables (without brake wires)   |
|----------------------------|-------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|--------------------------------------------|
| Kinetix MPL rotary motors  | Circular (Threaded) DIN | MPL-A/B15xxx-4xAA and MPL-A/B2xxx-4xAA                                                         | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex)   | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
| Kinetix MPS rotary motors  | Circular (Threaded) DIN | MPS-A/Bxxxx                                                                                    | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex)   | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
| Kinetix MPAS rotary motors | Circular (Threaded) DIN | MPAS-A/Bxxxx                                                                                   | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex)   | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
| Kinetix MPAR rotary motors | Circular (Threaded) DIN | MPAR-A/B1xxx and MPAR-A/B2xxx (Series A)                                                       | 2090-XXNPMF-xxSxx (standard) or 2090-CPBM4DF-xxAFxx (continuous-flex)   | 2090-CPWM4DF-xxAFxx (continuous-flex)      |
| Kinetix MPL rotary motors  | Circular (Speedtec) DIN | MPL-A/B15xxx-7xAA, MPL-A/B2xxx-7xAA, MPL-A/B3xxx-7xAA, MPL-A/B4xxx-7xAA, and MPL-A/B45xxx-7xAA | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | 2090-CPWM7DF-xxAAxx (standard) or 2090-CPWM7DF xxAFxx (continuous-flex)                                            |
| Kinetix MPM rotary motors  | Circular (Speedtec) DIN | MPM-A/Bxxxx                                                                                    | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | —                                          |
| Kinetix MPF rotary motors  | Circular (Speedtec) DIN | MPF-A/Bxxxx                                                                                    | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | —                                          |
| Kinetix MPAR rotary motors | Circular (Speedtec) DIN | MPAR-A/B3xxx, MPAR-A/B1xxx and MPAR-A/B2xxx (series B)                                         | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | —                                          |
| Kinetix MPAI rotary motors | Circular (Speedtec) DIN | MPAI-A/B3xxxx                                                                                  | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | —                                          |
| KInetix LDC linear motors  | Circular (Speedtec) DIN | LDC-Cxxxx                                                                                      | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | —                                          |
| Kinetix LDL linear motors  | Circular (Speedtec) DIN | LDL-xxxxxxx                                                                                    | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | —                                          |
| Kinetix LDAT linear motors | Circular (Speedtec) DIN | LDAT-Sxxxxxxxx                                                                                 | 2090-CPBM7DF-xxAAxx (standard) or 2090-CPBM7DF-xxAFxx (continuous-flex) | —                                          |
| Kinetix TL rotary motors   | Circular Plastic        | TLY-Axxxx                                                                                      | 2090-CPBM6DF-16AAxx (standard)                                          | 2090-CPWM6DF-16AAxx (standard)             |
| Kinetix TL rotary motors   | Circular Plastic        | TLAR-Axxxx                                                                                     | 2090-CPBM6DF-16AAxx (standard)                                          | 2090-CPWM6DF-16AAxx (standard)             |

This diagram shows an example of three-phase power wires for motors/ actuators that have no brakes. Thermal switch wires are included in the feedback cable.

See Kinetix 300 Drive/Rotary Motor Wiring Examples beginning on page 178 for interconnect diagrams.

Figure 43 - Motor Power Terminations (three-phase wires only)

<!-- image -->

The cable shield clamp that is shown in Figure 43 is mounted to the subpanel. Ground and secure the motor power cable in your system following instructions on page 73 .

This diagram shows an example of wiring with three-phase power wires and brake wires. The brake wires have a shield braid (shown in Figure 44 as gray) that folds back under the cable clamp before the conductors are attached to the motor brake circuit. Thermal switch wires are included in the feedback cable.

See Kinetix 300 Drive/Rotary Motor Wiring Examples beginning on page 178 for interconnect diagrams.

<!-- image -->

Figure 44 - Motor Power Terminations (three-phase and brake wires)

|       | Item Description                             | Item Description                |
|-------|----------------------------------------------|---------------------------------|
| 1 (1) | 24V power supply                             | 5 I/O (IOD) connector (2)       |
| 2 (1) | Relay and diode assembly (3)                 | 6 2097-V3xPRx Kinetix 300 drive |
|       | 3 Minimize unshielded wires in brake circuit | 7 Motor power (MP) connector    |
|       | 4 Kinetix MP cable brake wires               | 8 Cable clamp  (4)              |

- (2) Configure one emitter and collector pair from the Digital Outputs, OUT-1… OUT-4, pins 43…50, as Brake+ and Brake - by using MotionView software. Wire the output as sourcing and set brake engage and disengage times for motor selected. Motor brake is active on enable. For Digital Output specifications, see page 42
- (3) Diode 1N4004 rated 1.0 A @ 400V DC. See Interconnect Diagram Notes beginning on page 174 .
- (4) Exposed shield under clamp and place within 50…75 mm (2…3 in.) of drive, see page 73 for details.

Cable shield and lead preparation is provided with most Allen-Bradley® cable assemblies. Follow these guidelines if your motor-power cable shield and wires require preparation.

Figure 45 - Cable Shield and Lead Preparation

<!-- image -->

See Shunt-Resistor Wiring Example beginning on page 177 for interconnect diagrams.

Table 34 - Motor Power (MP) Connector

| Kinetix MP or Kinetix TL Servo Motor   | Terminal   |
|----------------------------------------|------------|
| U / Brown                              | U          |
| V / Black                              | V          |
| W / Blue                               | W          |
| Green/Yellow                           |            |

Table 35 - Motor Power (MP) Termination Specifications

| Drive Cat. No. Terminals                                                                                                            |                      | Recommended Wire Size mm 2 (AWG)   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------------------|-------------------------|----------------------------|
| 2097-V31PR0 2097-V31PR2 2097-V32PR0 2097-V32PR2 2097-V32PR4 2097-V33PR1 2097-V33PR3 2097-V33PR5 2097-V34PR3 2097-V34PR5 2097-V34PR6 | PE W V U             | 2.5 (14)                           |                         | 7 (0.28) 0.5 (4.5)         |
|                                                                                                                                     | 2097-V33PR6 4.0 (12) |                                    |                         |                            |

## Apply the Motor-Cable Shield Clamp

This procedure assumes that you have completed wiring your motor power (MP) connector and are ready to apply the cable shield clamp.

Follow these steps to apply the motor-cable shield clamp.

1. Locate a suitable position to install cable shield clamp within 50…75 mm (2…3 in.) of the drive.
2. Lay out and drill holes for cable clamp.

<!-- image -->

<!-- image -->

ATTENTION: Plan the installation of your system so that you can cut, drill, tap, and weld with the system removed from the enclosure. Because the system is of the open type construction, be careful to keep any metal debris from falling into it. Metal debris or other foreign matter can become lodged in the circuitry, which can result in damage to components.

3. Locate the position on the motor power cable that comes under the clamp and remove about an inch of the cable jacket to expose the shield braid.
4. Position the exposed portion of the cable braid directly in line with the clamp.
5. Clamp the exposed shield to the panel by using the clamp and 2 #6-32 x 1 screws provided.
6. Repeat step 1 … step 5 for each Kinetix 300 drive you are installing.

## Feedback and I/O Cable Connections

Factory made cables with premolded connectors are designed to minimize EMI and are recommended over hand-built cables to improve system performance. However, other options are available for building your own feedback and I/O cables.

Table 36 - Options for Connecting Motor Feedback and I/O

| Connection Option  Cat. No.          | Cable                                                                                              | Using This Type of Cable                                                      |
|--------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| Premolded connectors N/A             | Motor feedback                                                                                     | See Table 37 for the premolded motor feedback cable available for your motor. |
| Low Profile connector 2090-K2CK-D15M | Motor feedback                                                                                     | See Table 37 for the flying-lead cable available for your motor.              |
|                                      | I/O Terminal Block 2097-TB1 I/O interface for Master Gearing mode User-supplied flying-lead cable. |                                                                               |

Table 37 - Motor Feedback Cables for Specific Motor/Feedback Combinations

| Motor Cat. No.                                                      | Connector Type          | Feedback Type                    | Feedback Cable                                      | Feedback Cable                                                                                                            | Pinout   |
|---------------------------------------------------------------------|-------------------------|----------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------|
|                                                                     |                         |                                  | Premolded                                           | Flying-lead                                                                                                               |          |
| MPL-A/B15xxx-Hx4xAA, MPL-A/B2xxx-Hx4xAA                             | Circular (threaded) DIN | Incremental encoder              | N/A                                                 | 2090-XXNFMF-Sxx (standard) 2090-CFBM4DF-CDAFxx (continuous-flex)                                                          |          |
| MPL-A/B15xxx-V/Ex4xAA, MPL-A/B2xxx-V/Ex4xAA                         | Circular (threaded) DIN |                                  | N/A                                                 | 2090-XXNFMF-Sxx (standard) 2090-CFBM4DF-CDAFxx (continuous-flex)                                                          |          |
| MPAR-A/B3xxxx MPAR-A/B1xxxx and MPAR-A/B2xxxx (series A)            | Circular (threaded) DIN |                                  | N/A                                                 | 2090-XXNFMF-Sxx (standard) 2090-CFBM4DF-CDAFxx (continuous-flex)                                                          |          |
| MPAI-A/Bxxxx                                                        | Circular (threaded) DIN | High-resolution encoder          | N/A                                                 | 2090-XXNFMF-Sxx (standard) 2090-CFBM4DF-CDAFxx (continuous-flex)                                                          |          |
| MPS-A/Bxxxx-M/S                                                     | Circular (threaded) DIN |                                  | N/A                                                 | 2090-XXNFMF-Sxx (standard) 2090-CFBM4DF-CDAFxx (continuous-flex)                                                          |          |
| MPAS-A/Bxxxx-V/A                                                    | Circular (threaded) DIN |                                  | N/A                                                 | 2090-XXNFMF-Sxx (standard) 2090-CFBM4DF-CDAFxx (continuous-flex)                                                          |          |
| MPL-A/B15xxx-V/Ex7xAA, MPL-A/B2xxx-V/Ex7xAA                         |                         | Incremental encoder xxx-Hx7xAA,  | N/A                                                 | (continuous-flex)                                                                                                         |          |
| MPL-A/B15xxx-Hx7xAA, MPL-A/B2xxx-Hx7xAA                             |                         | Incremental encoder xxx-Hx7xAA,  | N/A                                                 | (continuous-flex)                                                                                                         |          |
| MPL-A/B3  MPL-A/B4xxx-Hx7xAA, MPL-A/B45xxx-Hx7xAA LDAT-SxxxxxxxBx   |                         | Incremental encoder xxx-Hx7xAA,  | N/A                                                 | (continuous-flex)                                                                                                         | page 75  |
| MPL-A/B3xxx-M/Sx7xAA, MPL-A/B4xxx-M/Sx7xAA, MPL - A/B45xxx-M/Sx7xAA | Circular (Speedtec)     | DIN B High-resolution encoder xxxxx-M/S                                  | N/A                                                 | (continuous-flex)                                                                                                         |          |
| MPM-A/B x                                                           | DIN                     | DIN B High-resolution encoder xxxxx-M/S                                  | N/A                                                 | (continuous-flex)                                                                                                         |          |
| MPF-A/Bxxxx-M/S                                                     |                         | DIN B High-resolution encoder xxxxx-M/S                                  | N/A                                                 | (continuous-flex)                                                                                                         |          |
| MPAR-A/B1xxxx and MPAR-A/B2xxxx (series B)                          |                         | DIN B High-resolution encoder xxxxx-M/S                                  | N/A                                                 | (continuous-flex)                                                                                                         |          |
| LDAT-Sxxxxxx-xDx                                                    |                         | Absolute Linear Encoder Feedback | N/A                                                 | 2090-CFBM7DF-CEAAxx or 2090-CFBM7DD-CEAAxx (standard, non-flex) 2090-CFBM7DF-CEAFxx 2090-CFBM7DD-CEAFxx (continuous-flex) |          |
| TLY-Axxxx-B                                                         | Circular Plastic        | High-resolution encoder          | N/A                                                 | 2090-CFBM6DF-CBAAx Axx (standard)                                                                                         | page 75  |
| TLAR-Axxxxx                                                         | Circular Plastic        | High-resolution encoder          | N/A                                                 | 2090-CFBM6DF-CBAAx Axx (standard)                                                                                         | page 75  |
|                                                                     | Circular Plastic        |                                  | TLY-Axxxx-H Incremental encoder 2090-CFBM6DD-CCAAxx | 2090-CFBM6DF-CBAAx Axx (standard)                                                                                         | page 75  |

## Flying-lead Feedback Cable Pinouts

Table 38 - 2090-XXNFMF-Sxx or 2090-CFBMxDF-CDAFxx Feedback Cable

| Connector Pin   | High-resolution Feedback    | Incremental Feedback             | Drive MF Connector Pin   |
|-----------------|-----------------------------|----------------------------------|--------------------------|
| Connector Pin   |                             | 9V Encoder 5V Encoder 5V Encoder | Drive MF Connector Pin   |
|                 |                             | 1 Sin+ Sin+ AM+ 1                |                          |
|                 |                             | 2 Sin- Sin- AM- 2                |                          |
|                 | 3 Cos+ Cos+ BM+ 3           |                                  |                          |
|                 |                             | 4 Cos- Cos- BM- 4                |                          |
|                 | 5 Data+ Data+ IM+ 5         |                                  |                          |
|                 | 6 Data- Data- IM- 10        |                                  |                          |
|                 |                             | 9 Reserved EPWR_5V EPWR_5V 14    |                          |
| 10              | Reserved ECOM               | ECOM                             | 6                        |
| 11              | EPWR_9V Reserved Reserved 7 |                                  |                          |
| 12              | ECOM                        | Reserved Reserved 6              |                          |
| 13              | TS+                         | TS+  TS+                         | 11                       |
| 14              | TS-  TS-                    | TS-                              | –                        |
| 15              | Reserved Reserved S1        |                                  | 12                       |
| 16              | Reserved Reserved S2        |                                  | 13                       |
| 17              | Reserved Reserved S3        |                                  | 8                        |

Table 39 - 2090-CFBM6DF-CBAAxx Feedback Cable

| Connector Pin   |                          | High Resolution Incremental Feedback   | Drive MF Connector Pin   |
|-----------------|--------------------------|----------------------------------------|--------------------------|
| Connector Pin   | TLY-Axxxx-B  TLAR-Axxxxx | TLY-Axxxx-H                            |                          |
| 6               | BAT+                     | Reserved                               | BAT+                     |
| 9               | Reserved                 | AM+                                    | 1                        |
| 10              | Reserved                 | AM-                                    | 2                        |
| 11              | Reserved                 | BM+                                    | 3                        |
| 12              | Reserved                 | BM-                                    | 4                        |
| 13              | DATA+                    | IM+                                    | 5                        |
| 14              | DATA-                    | IM-                                    | 10                       |
| 15              | Reserved                 | S1                                     | 12                       |
| 17              | Reserved                 | S2                                     | 13                       |
| 19              | Reserved                 | S3                                     | 8                        |
| 22              | EPWR 5V                  | EPWR 5V                                | 14                       |
| 23              | ECOM and BAT-            | ECOM                                   | 6                        |
| 24              | Shield                   | Shield                                 | Connector housing        |

## Wiring the Feedback and I/O Connectors

These procedures assume that you have mounted your Kinetix 300 system, completed the power wiring, and are ready to connect motor feedback.

## Wire the I/O Connector

Connect your I/O wires to the IOD connector by using the 2097-TB1 I/O Terminal Expansion Block. See the Kinetix 300 I/O Terminal Expansion Block Installation Instructions, publication 2097-IN005 .

Figure 46 - Kinetix 300 Drive (IOD connector and terminal block)

<!-- image -->

## Wire the Low Profile Connector Kit

The 2090-K2CK-D15M Low Profile connector kit is suitable for ending flying-lead motor feedback cables. Use it with the Kinetix 300 drive and all motors with incremental or high-resolution feedback. It has a 15-pin, male, Dsub connector and is compatible with all Kinetix 2090 feedback cables.

TLY-Axxxx-B rotary motors and TLAR-Axxxxx electric cylinders also require the 2090-DA-BAT2 battery to back up the high-resolution encoder.

Figure 47 - Kinetix 300 Drive (MF connector)

<!-- image -->

## Figure 48 - Wiring (15-pin) Flying-lead Feedback Cable Connections 2090-K2CK-D15M Connector Kit

<!-- image -->

## Shunt Resistor Connections

Follow these guidelines when wiring your 2097-Rx shunt resistor.

IMPORTANT

When you tighten screws to secure the wires, see the tables beginning on page 63 for torque values.

## IMPORTANT

To improve system performance, run wires and cables in the wireways as established in Chapter 2 .

- See Shunt Resistors on page 28 for noise zone considerations.
- See Shunt-Resistor Wiring Example on page 177 .
- See the installation instructions that are provided with your Bulletin 2097 shunt resistor, publication 2097-IN002 .

Figure 49 - Shunt/DC Bus (BC) Connector

<!-- image -->

Table 40 - Shunt-Resistor Power Wiring Requirements

| Accessory   | Description    | Connects to Terminals   | Recommended Wire Size mm 2 (AWG)   | Torque Value N•m (lb•in)   |
|-------------|----------------|-------------------------|------------------------------------|----------------------------|
| 2097-Rx     | Shunt Resistor | + SH                    |                                    | 2.5 (14) 0.5 (4.5)         |

## Ethernet Cable Connections

This procedure assumes that you have your Logix EtherNet/IP™ module and Kinetix 300 drive that is mounted and ready to connect the network cables.

The EtherNet/IP network is connected by using the Port 1 connector. See page 32 to locate the Ethernet connector on your Kinetix 300 drive. See the figure below to locate the connector on your Logix communication module.

Shielded Ethernet cable is available in lengths up to 78 m (256 ft). However, the total length of Ethernet cable connecting drive-to-drive, drive-tocontroller, or drive-to-switch must not exceed 100 m (328 ft).

If the entire channel is constructed of stranded cable (no fixed cable), then use the following equation for calculating maximum length:

Maximum Length = (113-2N)/y, meters where N = the number of connections in the channel and y = the loss factor that is compared to fixed cable (typically 1.2…1.5).

Figure 50 - CompactLogix Ethernet Port Location

CompactLogix™ Controller Platform 1769-L23E-QB1B Shown

<!-- image -->

The Port 1 Ethernet connection is used for connecting to a web browser and configuring your Logix module.

Figure 51 - Ethernet Wiring Example - External Switch

<!-- image -->

## Notes:

<!-- image -->

## MotionView Software Configuration

| Topic                              |   Page |
|------------------------------------|--------|
| Drive Organizer and Identification |     82 |
| Motor Category                     |     82 |
| General Category                   |     85 |
| Communication Categories           |     89 |
| Input/Output Categories            |     91 |
| Limits Categories                  |     93 |
| Dynamics Category                  |     95 |
| Tools Category                     |     96 |
| Monitor Category                   |     97 |
| Faults Category                    |     98 |
| Indexing Category                  |     99 |
| Homing Category                    |    111 |
| Upgrade Firmware                   |    122 |

## Drive Organizer and Identification

On the left side of MotionView software is the Drive Organizer. The Drive Organizer displays the node address for the drives that are currently connected to the software and lists the categories for each drive under the drive node address. This section contains a description of the parameters that are displayed in each category that is listed in the Drive Organizer.

Drive Identification displays the drive IP address and status. The dialog box displays drive identification information such as catalog number and firmware revision. In this window, you can assign the Drive Name and the Group ID.

<!-- image -->

Table 41 - Drive Identification Category

<!-- image -->

| ID Parameter Name Description   |                                                                                                   | Value/Notes                                                                 |
|---------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| 1 Drive ID String               | Drive identification string                                                                       | B12 154 140 100 020 Device Firmware Hardware Deviation Vector Family Revision Revision Revision Processor Revision Vector Processor Revision                                                                             |
| 2 Drive Name                    | Drive symbolic name  Up to 20 user-defined characters                                             | Drive symbolic name  Up to 20 user-defined characters                       |
| 3 Serial Number                 | Drive serial number  Unique number that is assigned to drive at the factory                       | Drive serial number  Unique number that is assigned to drive at the factory |
| 57 Group ID                     | Network group ID. Allows the assignment of different drives into logical groups.                  | Range: 1…32767                                                              |
|                                 | N/A Motor Database Revision The motor database resides in the drive firmware. 006 in this example |                                                                             |

## Motor Category

Allen-Bradley® motors and actuators with intelligent feedback devices are automatically populated into the motor configuration. In this example, the MPL-A1510V-Hxx2 servo motor is attached to the drive.

<!-- image -->

## Synchronous Motor Database

For Allen-Bradley synchronous motors and actuators with incremental encoders, click Change Motor and choose the device from the Synchronous&gt;Motor Database. In this example, the MPL-A1510V-Hxx2 motor is configured.

<!-- image -->

Table 42 - Motor Category

| ID Parameter Name Description          |                                                             | Value/Notes                                          |
|----------------------------------------|-------------------------------------------------------------|------------------------------------------------------|
| 10 Motor ID                            | Motor serial number (for Rockwell Automation® motor)        | Motor serial number (for Rockwell Automation® motor) |
| 11 Motor Model                         | Motor catalog number (for Rockwell Automation motor)        | Motor catalog number (for Rockwell Automation motor) |
| 12 Motor Vendor                        | Rockwell Automation                                         | Rockwell Automation                                  |
| 14 Halls Order                         | Hallcode index                                              | Range: 0…5                                           |
| 18 Jm                                  | Motor moment of inertia                                     | Range: 0…0.1 Kg-m 2                                  |
| 19 Ke                                  | Motor voltage or back EMF constant Range: 1…500 V/K rpm     |                                                      |
| 20 Kt                                  | Motor torque or force constant                              | Range: 0.01…10 N•m/A                                 |
| 21 Lm                                  | Motor phase-to-phase inductance                             | Range: 0.1…500 mH                                    |
| 22 Rm                                  | Motor phase-to-phase resistance                             | Range: 0.01…500                                     |
|                                        | 23 Nominal Phase Current Motor max current (RMS)            | Range: 0.5…50 A                                      |
| 24 Maximum Velocity Motor max velocity |                                                             | Range: 500…20,000 rpm                                |
| 25 Number Of Poles                     | Motor number of poles                                       | Range: 2…200                                         |
| 26 PPR Before Quad                     | Encoder resolution                                          | Range: 256 to (65536 x12/Npoles) expressed in PPR    |
|                                        | 27 Nominal Drive Bus Voltage Nominal motor-terminal voltage | Range: 50…800V                                       |
| 646 Rt                                 | Thermal resistance                                          | Range: 0…10000000 C/W                                |
| 647 Ct                                 | Thermal capacitance                                         | Range: 0…10000000 W-s/C                              |

## Linear Motor Database

For Allen-Bradley motors and actuators with incremental encoders, click Change Motor and choose the device from the Linear&gt;Motor Database. In this example, the LCD-C030100-DHTxxA linear motor is configured.

<!-- image -->

Table 43 - Linear Motor Category

| ID Parameter Name Description                 |                                                             | Value/Notes                                    |
|-----------------------------------------------|-------------------------------------------------------------|------------------------------------------------|
| 10 Motor ID                                   | Motor serial number (for Allen-Bradley motor)               | Motor serial number (for Allen-Bradley motor)  |
| 11 Motor Model                                | Motor catalog number (for Allen-Bradley motor)              | Motor catalog number (for Allen-Bradley motor) |
| 12 Motor Vendor                               | Allen-Bradley                                               | Allen-Bradley                                  |
| 14 Halls Order                                | Hallcode index                                              | Range: 0…5                                     |
| 243 Motor Block Mass                          | Motor block mass                                            | Range: 0…100 kg                                |
| 244 Kf                                        | Linear motor force constant                                 | Range: 1…1000 N/A rms                          |
| 245 Ke                                        | Motor voltage or back EMF constant Range: 1…500V rms/m/s    |                                                |
| 21 Lm                                         | Motor phase-to-phase inductance                             | Range: 0.1…500 mH                              |
| 22 Rm                                         | Motor phase-to-phase resistance                             | Range: 0.01…500                               |
|                                               | 23 Nominal Phase Current Motor max current (RMS)            | Range: 0.5…50 A                                |
| 24 Maximum Velocity Motor max velocity        |                                                             | Range: 0…10 m/s                                |
| 240 Pole Pitch                                | Pole pitch                                                  | Range: 2…200 mm                                |
| 246 Resolution (x1)                           | Linear encoder resolution                                   | Range: 0.4…40 µm                               |
|                                               | 27 Nominal Drive Bus Voltage Nominal motor-terminal voltage | Range: 50…800V                                 |
| 650 Intermittent Current Intermittent current |                                                             | Range: 0…100 A                                 |
| 646 Rt                                        | Thermal resistance                                          | Range: 0…10000000 C/W                          |
| 647 Ct                                        | Thermal capacitance                                         | Range: 0…10000000 W-s/C                        |

## General Category

The General category provides access to the basic configuration of motion. The parameters that are displayed depend on the motor type that is chosen in the Motor Category.

Figure 52 - General Category for Synchronous Motors

<!-- image -->

Table 44 - General Category for Synchronous

| ID Parameter Name Description Value/Notes   |                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 30 (1)  Current Limit                       |                                                                                                                                                                                                                                                                                                         | Continuous RMS current for motor selected You can lower this value. It lets you trigger a motor current alarm. However, the drive cannot limit the actual current to the motor. The actual RMS current limit to the motor is not configurable.                                                                                                                              |
| 32 (1)                                      | 8 kHz Peak Current Limit Peak current limit for 8 kHz operation (based on motor that is selected)                                                                                                                                                                                                       | You can lower this peak value to limit current to motor. Do not set below the RMS Current for motor (tag #30).                                                                                                                                                                                                                                                              |
|                                             | 39 Motor Temperature Sensor Motor thermal-protection function                                                                                                                                                                                                                                           | 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                      |
| 75 (2)                                      | Enable Accel/Decel Limits Enable Accel/Decel function/limits for Velocity mode                                                                                                                                                                                                                          | 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                                                                      |
| 76 (2)  Accel Limit                         | Accel value for Velocity mode                                                                                                                                                                                                                                                                           | Range: 0.1…5,000,000 rpm/s                                                                                                                                                                                                                                                                                                                                                  |
| 77 (2)  Decel Limit                         | Decel value for Velocity mode                                                                                                                                                                                                                                                                           | Range: 0.1…5,000,000 rpm/s                                                                                                                                                                                                                                                                                                                                                  |
| 78 Fault Reset                              | Reset fault configuration                                                                                                                                                                                                                                                                               | Manual Only On Disable                                                                                                                                                                                                                                                                                                                                                      |
| 79 Master                                   | Master to system ratio (numerator)                                                                                                                                                                                                                                                                      | Master counts range: -32768…+32768                                                                                                                                                                                                                                                                                                                                          |
| 80 System                                   | Master to system ratio (denominator)                                                                                                                                                                                                                                                                    | System counts range: 1…32768                                                                                                                                                                                                                                                                                                                                                |
| 266 Drive Mode                              | Sets the mode of operation for the drive 0 = Autotune                                                                                                                                                                                                                                                   | 1 = EtherNet/IP™ External Reference 2 = Master Gearing 3= Step and Direction 4 = Analog Velocity Input 5 = Analog Current Input 6 = Indexing                                                                                                                                                                                                                                |
| 181 User Units                              | User units                                                                                                                                                                                                                                                                                              | Revolutions of motor per user unit                                                                                                                                                                                                                                                                                                                                          |
|                                             | 672 Current output clamp Value to clamp output current, which is measured in percentage of motor rated current                                                                                                                                                                                          | Range: 0…400%                                                                                                                                                                                                                                                                                                                                                               |
|                                             | 670 Enable rotary unwind Enable rotary unwind for rotary motors. When rotary unwind is used with a motor with an absolute encoder, the position is restored with in the unwind cycle. These modes are available as Index Types in indexing mode or as a Reference Source in EtherNet/IP operation mode. | 0 = Unchecked = Disable 1 = Checked = Enable Rotary Unwind is designed only for these modes: • Rotary Absolute • Rotary Incremental • Rotary Shortest Path • Rotary Positive • Rotary Negative Rotary unwind mode with Blended or Registered moves is not supported. Attempting to use these move options without having configured rotary unwind results in a drive fault. |
|                                             | 671 User units per unwind Number of revolutions in one user unit. Range: 0…1000000                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                                                                                                             |
|                                             | 8 Negative motion polarity Inverts the motion polarity                                                                                                                                                                                                                                                  | 0 = Unchecked =Normal 1 = Checked =Reverse Step and Direction and Gear-based modes and position-based moves, such as incremental, absolute, and velocity-based jogs obey the motion polarity. Current based operating modes do not obey the motion polarity. The drive must be disabled to change the motion polarity.                                                      |

Figure 53 - General Category for Linear Motors

<!-- image -->

Table 45 - General Category y for Linear Motors

| ID Parameter Name Description Value/Notes   |                                                                                                                |                                                                                                                                                                                                                                                                                                                        |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 30 (1)  Current Limit                       |                                                                                                                | Continuous RMS current for motor selected You can lower this value. It lets you trigger a motor current alarm. However, the drive cannot limit the actual current to the motor. The actual RMS current limit to the motor is not configurable.                                                                         |
| 32 (1)                                      | 8 kHz Peak Current Limit Peak current limit for 8 kHz operation (based on motor that is selected)              | You can lower this peak value to limit current to motor. Do not set below the RMS Current for motor (tag #30).                                                                                                                                                                                                         |
|                                             | 39 Motor Temperature Sensor Motor thermal-protection function                                                  | 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                 |
| 75 (2)                                      | Enable Accel/Decel Limits Enable Accel/Decel function/limits for Velocity mode                                 | 0 = Disable 1 = Enable                                                                                                                                                                                                                                                                                                 |
| 76 (2)  Accel Limit                         | Accel value for Velocity mode                                                                                  | Range: 0.1…5,000,000 m/s 2                                                                                                                                                                                                                                                                                             |
| 77 (2)  Decel Limit                         | Decel value for Velocity mode                                                                                  | Range: 0.1…5,000,000 m/s 2                                                                                                                                                                                                                                                                                             |
| 78 Fault Reset                              | Reset fault configuration                                                                                      | Manual Only On Disable                                                                                                                                                                                                                                                                                                 |
| 79 Master                                   | Master to system ratio (numerator)                                                                             | Master counts range: -32768…+32768                                                                                                                                                                                                                                                                                     |
| 80 System                                   | Master to system ratio (denominator)                                                                           | System counts range: 1…32768                                                                                                                                                                                                                                                                                           |
| 266 Drive Mode                              | Sets the mode of operation for the drive 0 = Autotune                                                          | 1 = EtherNet/IP External Reference 2 = Master Gearing 3= Step and Direction 4 = Analog Velocity Input 5 = Analog Current Input 6 = Indexing                                                                                                                                                                            |
|                                             | 672 Current Output Clamp Value to clamp output current, which is measured in percentage of motor rated current | Range: 0…400%                                                                                                                                                                                                                                                                                                          |
|                                             | 676 User Units Scaling Shows how many user units in one Measure unit Range: 1…1000000                          |                                                                                                                                                                                                                                                                                                                        |
| 678 Measure Units                           | Measure units                                                                                                  | 0 = µm 1 = m 2 = in.                                                                                                                                                                                                                                                                                                   |
|                                             | 8 Negative Motion Polarity Inverts the motion polarity                                                         | 0 = Unchecked =Normal 1 = Checked =Reverse Step and Direction and Gear-based modes and position-based moves, such as incremental, absolute, and velocity-based jogs obey the motion polarity. Current based operating modes do not obey the motion polarity. The drive must be disabled to change the motion polarity. |

## Communication Categories

The communication categories provide access to setting the IP address for your drive and object parameters that are used in the Input and Output Assembly EtherNet/IP datalinks.

## Ethernet Communication

The Ethernet category provides access to the IP address configuration. You can configure your drive to obtain the IP address automatically (by using DHCP) or set the values manually.

<!-- image -->

Table 46 - Ethernet Communication Category

| ID Parameter Name Description                  | Value/Notes                                       |
|------------------------------------------------|---------------------------------------------------|
| 67 IP address EtherNet/IP address              | IP address changes at next powerup. 32-bit value. |
| 68 Subnet Mask EtherNet/IP NetMask             | Mask changes at next powerup. 32-bit value.       |
| 69 Default Gateway Ethernet Gateway IP address | Address changes at next powerup. 32-bit value.    |
| 70 Obtain IP address using DHCP Use DHCP       | Checked = Use DHCP service Unchecked = Manual     |

## EtherNet/IP (CIP) Communication

The EtherNet/IP (CIP) category provides access to the modifiable drive object parameters that are used in the Input and Output Assembly EtherNet/IP datalinks.

<!-- image -->

The Enable parameters determine if the parameter is copied into or out of the assembly.

Table 47 - EtherNet/IP (CIP) Communication Category

|     | ID Parameter Name Description      | Value/Notes                                            |
|-----|------------------------------------|--------------------------------------------------------|
|     | 249 Enable - Input Assembly Links  | Datalink A for input assembly UserDefinedIntegerData0  |
| 250 | 249 Enable - Input Assembly Links  | Datalink B for input assembly UserDefinedIntegerData1  |
| 251 | 249 Enable - Input Assembly Links  | Datalink C for input assembly UserDefinedIntegerReal0  |
| 252 | 249 Enable - Input Assembly Links  | Datalink D for input assembly UserDefinedIntegerReal1  |
|     | 253 Enable - Output Assembly Links | Datalink A for output assembly UserDefinedIntegerData0 |
| 254 | 253 Enable - Output Assembly Links | Datalink B for output assembly UserDefinedIntegerData1 |
| 255 | 253 Enable - Output Assembly Links | Datalink C for output assembly UserDefinedIntegerReal0 |
| 256 | 253 Enable - Output Assembly Links | Datalink D for output assembly UserDefinedIntegerReal1 |

## Input/Output Categories

The Input/Output categories provide access to the configuration of the modifiable Digital I/O and Analog I/O parameters.

## Digital I/O

## IMPORTANT

Drive object parameters of type DINT can be used only in the RAM integer datalinks, parameters of type REAL can be used only in the RAM float datalinks.

<!-- image -->

Table 48 - Digital I/O Category

|           | ID Parameter Name Description   |                                                                                                                                                                                                                                     |
|-----------|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|           |                                 | 29 Enable Switch Function Configuration of the enable digital input A3. 0 = Inhibit only. Must be asserted before the drive can be enabled. 1 = Run. Enables drive when asserted.                                                   |
|           |                                 | 84 Hard Limit Switches Action Configuration of the action to take when the limit switches are asserted. 0 = Not used 1 = Disable and coast 2 = Ramped Decel and Disable                                                             |
| 189 … 192 | Input A1…A4 de-bounce time      | Debounce time (0…1000 ms) of the individual digital inputs.                                                                                                                                                                         |
| 193 … 196 | Input B1…B4 de-bounce time      | Debounce time (0…1000 ms) of the individual digital inputs.                                                                                                                                                                         |
| 197 … 200 | Input C1…C4 de-bounce time      | Debounce time (0…1000 ms) of the individual digital inputs.                                                                                                                                                                         |
|           |                                 | 201 Output 1 Function (OUT1) Configuration of the specific function for the individual digital outputs. 0 = Not Assigned 1 = Zero Speed 2 = In Speed Window 3 = Current Limit 4 = Runtime fault 5 = Ready 6 = Brake 7 = In position |
|           | 202 Output 2 Function (OUT2)    | 201 Output 1 Function (OUT1) Configuration of the specific function for the individual digital outputs. 0 = Not Assigned 1 = Zero Speed 2 = In Speed Window 3 = Current Limit 4 = Runtime fault 5 = Ready 6 = Brake 7 = In position |
|           | 203 Output 3 Function (OUT3)    | 201 Output 1 Function (OUT1) Configuration of the specific function for the individual digital outputs. 0 = Not Assigned 1 = Zero Speed 2 = In Speed Window 3 = Current Limit 4 = Runtime fault 5 = Ready 6 = Brake 7 = In position |
|           | 204 Output 4 Function (OUT4)    | 201 Output 1 Function (OUT1) Configuration of the specific function for the individual digital outputs. 0 = Not Assigned 1 = Zero Speed 2 = In Speed Window 3 = Current Limit 4 = Runtime fault 5 = Ready 6 = Brake 7 = In position |

| ID Parameter Name Description   |                                                                                                                                                                                                          |
|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                 | 624 Input A4 Function Configuration of the specific function for the individual digital inputs, pre-assigned inputs such as Enable and Registration are not configurable. 1 = Abort Index 2 = (Reserved) |
| 625 … 628 Input B1…B4 Function  | 3 = Start Index 4 = Define Home 5 = Abort Homing 6 = Start Homing 7 = Fault Reset                                                                                                                        |
| 629 Input C1 Function           | 8 = Index Select 0 9 = Index Select 1 10 = Index Select 2                                                                                                                                                |
| 630 Input C2 Function           | 11 = Index Select 3 12 = Index Select 4                                                                                                                                                                  |
| 631 Input C4 Function           |                                                                                                                                                                                                          |
|                                 | 651 Brake Engage Delay Time (ms) from when the drive is disabled to the time that motion is stopped and brake is engaged.                                                                                |
|                                 | 652 Brake Release Delay Time (ms) from when the drive is enabled to the time that motion is allowed to begin (brake is released).                                                                        |

## Analog I/O

<!-- image -->

Table 49 - Analog I/O Category

| ID Parameter Name Description     |                                                                                                       | Value/Notes                                                                                                                                                                          |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 35 Analog Input (current scale)   | Analog input #1 current reference scale Range: - X…X Amps/Volt                                        | X = drive peak output current/10                                                                                                                                                     |
| 36 Analog Input (velocity scale)  | Analog input #1 velocity reference scale Range: -10,000…10,000 rpm/Volt                               |                                                                                                                                                                                      |
|                                   | 85 Analog Output Analog output function                                                               | 0 = Not assigned 1 = Phase Current (RMS) 2 = Phase Current (Peak Value) 3 = Motor Velocity 4 = Phase Current U 5 = Phase Current V 6 = Phase Current W 7 = Iq current 8 = Id current |
| 86 Analog Output (velocity scale) | Analog output scale for velocity quantities Range: 0…10 mV/rpm                                        |                                                                                                                                                                                      |
| 87 Analog Output (current scale)  | Analog output scale for current related quantities                                                    | Range: 0…10 V/A                                                                                                                                                                      |
|                                   | 89 Analog Input deadband Analog input #1 deadband. Applied when used as current or velocity reference | Range: 0…100 mV                                                                                                                                                                      |
|                                   | 90 Analog Input Offset Analog input #1 offset. Applied when used as current/velocity reference        | Range: -10,000…+10,000 mV                                                                                                                                                            |

## Limits Categories

The Limits categories provide access to the configuration of the modifiable velocity and position limit parameters.

## Velocity Limits

<!-- image -->

Table 50 - Velocity Limits Category

| ID Parameter Name Description   |                                                                                                                                                                                                | Value/Notes              |
|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| 58 Zero Speed                   | Value in user units/s below which the drive sets the Zero Speed Digital Output (if configured) and the VelocityStandstillStatus bit in the EtherNet/IP Input Assembly.                         | Range: 0…100 rpm         |
|                                 | 59 Speed Window The range in user units/s around the At Speed for setting the In-Speed Window Digital Output (if configured) and the VelocityLockStatus bit in the EtherNet/IP Input Assembly. | Range: 10…10000 rpm      |
| 60 At Speed                     | Value in user units/s for the target velocity for which the drive sets the In-Speed Window Digital Output (if configured) and the VelocityLockStatus bit in the EtherNet/IP Input Assembly.    | Range: -10000…+10000 rpm |

## Position Limits

<!-- image -->

Table 51 - Position Limits Category

| ID Parameter Name Description                                                                                                                                                                                                                                        | Value/Notes                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| 62 Max Error Time The amount of time that the drive can be outside of the Position Error before the drive asserts an Excess Position Error Fault.                                                                                                                    | Range: 0.25…8000 ms                                        |
| 178 Abort Decel The deceleration rate that the drive uses to bring the motor to a stop when either the Abort Homing or Abort Index Digital Inputs is asserted (if configured) or either the AbortIndex or AbortHoming bit is set in the EtherNet/IP Output Assembly. | User units/s 2                                             |
| 179 Position Limit The tolerance around the commanded position inside of which the drive sets the PositionLockStatus bit in the EtherNet/IP Input Assembly.                                                                                                          | User units                                                 |
| 217 Position Error The tolerance around the commanded position outside of which the drive asserts an Excess Position Error Fault when the Max Error Time is exceeded.                                                                                                | Encoder counts                                             |
| 218 Soft Limits (1)  Off or On depending if software travel limits are used.                                                                                                                                                                                         | 0 = Off 1 = Disable and Coast 2 = Ramped Decel and Disable |
| 219 Positive Limit If Soft Limits are On, the position that when reached, the drive asserts a Software Overtravel fault.                                                                                                                                             | User units                                                 |
| 220 Negative Limit                                                                                                                                                                                                                                                   | User units                                                 |

## Dynamics Category

The Dynamics category provides access to the configuration of the modifiable dynamics parameters.

<!-- image -->

Click Autotuning to begin autotuning.

Table 52 - Dynamics Category

| ID Parameter Name Description                                                                                                                                                                | Value/Notes    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| 44 Velocity P-Gain The proportional and integral gain (respectively) of the velocity loops. Gains are based on counts as the fundamental units and they are not physical units.              | Range: 0…32767 |
| 45 Velocity I-Gain                                                                                                                                                                           | Range: 0…32767 |
| 46 Position P-Gain The proportional, integral, and derivative gain (respectively) of the position loops. Gains are based on counts as the fundamental units and they are not physical units. | Range: 0…32767 |
| 47 Position I-Gain                                                                                                                                                                           | Range: 0…16383 |
| 48 Position D-Gain                                                                                                                                                                           | Range: 0…32767 |
| 49 Position I-Limit A clamping limit on the position loop I-gain compensator to prevent excessive torque overshooting from an over accumulation of the I-Gain.                               | Range: 0…20000 |
| 51 Gain Scaling A 2x factor that is applied to the gains in the velocity loop useful for scaling the gains when using encoders with a high number of counts per revolution.                  | Range: -16…+4  |

See the Servo Loop diagram on page 96 for more information on these parameters.

<!-- image -->

## Tools Category

The tools category provides access to the oscilloscope and digitally monitor drive performance parameters.

<!-- image -->

## Monitor Category

Table 53 - Monitor Category

| ID Parameter Name Description                |                                                                                                                                      | Value/Notes                                                                                                                                                                                                   |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 7 Actual Velocity                            | Actual measured motor velocity                                                                                                       | UU/s                                                                                                                                                                                                          |
| 65 Inputs                                    | Digital inputs states                                                                                                                | A1 Input = Bit 0 A2 Input = Bit 1 A3 Input = Bit 2 A4 Input = Bit 3 B1 Input = Bit 4 B2 Input = Bit 5 B3 Input = Bit 6 B4 Input = Bit 7 C1 Input = Bit 8 C2 Input = Bit 9 C3 Input = Bit 10 C4 Input = Bit 11 |
| 66 Outputs                                   | Digital outputs states. Writing to these variables sets or resets digital outputs that have not been assigned to a special function. | Output 1 = Bit 0 Output 2 = Bit 1 Output 3 = Bit 2 Output 4 = Bit 3                                                                                                                                           |
| 71 Analog Input                              | Analog Input AIN1 value                                                                                                              | Volts                                                                                                                                                                                                         |
| 73 Bus Voltage                               | Measured Bus voltage                                                                                                                 | Volts                                                                                                                                                                                                         |
| 74 Heatsink Temperature Heatsink temperature |                                                                                                                                      | 0 = Temperatures < 40 °C (104 °F) Actual heatsink temperature = Temperatures > 40 °C (104 °F)                                                                                                                 |
| 182 ME Counter                               | Master Encoder (ME) input counter-value, reset by writing zero or other value to the parameter.                                      | Counts                                                                                                                                                                                                        |
| 183 Phase Current                            | Phase current                                                                                                                        | Amps                                                                                                                                                                                                          |
| 184 Target Position (EC) Target position     |                                                                                                                                      | Encoder pulses                                                                                                                                                                                                |

The monitor category provides access to pre-configured status information for the drive. This information is displayed in a floating window that updates in real time.

<!-- image -->

Table 53 - Monitor Category (Continued)

| ID Parameter Name Description                           |                 | Value/Notes    |
|---------------------------------------------------------|-----------------|----------------|
| 185 Actual Position (EC) Actual position Encoder pulses |                 |                |
| 186 Position Error (EC)                                 | Position error  | Encoder pulses |
| 207 Registration Position (EC) Registration position    |                 | Encoder counts |
| 208 Registration Position Registration position         |                 | User units     |
| 209 Target Position                                     | Target position | User units     |
| 210 Actual Position                                     | Actual position | User units     |
| 211 Position Error                                      | Position error  | Encoder counts |

## Faults Category

The Faults category provides access to the configuration of the modifiable fault parameters.

<!-- image -->

Table 54 - Faults Category

| ID Parameter Name Description    |                                                                              | Value/Notes                                                   |
|----------------------------------|------------------------------------------------------------------------------|---------------------------------------------------------------|
| 653 Last Fault Code Fault E-code |                                                                              | Same fault code that is displayed on the servo drive display. |
|                                  | N/A Device Time The time since powerup of the drive that the fault occurred. | N/A                                                           |
| N/A Load Faults                  | Recall the last 15 faults the drive reported.                                | N/A                                                           |
| N/A Clear Fault History (1)      | Clear the fault history of the drive.                                        | N/A                                                           |
|                                  | N/A Clear Faults Clear the current fault in the drive.                       | N/A                                                           |

## Indexing Category

The software for the onboard indexing operation is accessed via the MotionView software and is also configurable over the EtherNet/IP connection by using Explicit Messaging in RSLogix 5000® and RSLogix 500® software or the Studio 5000 Logix Designer® application.

In Indexing mode, the Kinetix® 300 drive begins execution of indexes after either a command is received over the EtherNet/IP connection or immediately upon assertion of the hardware enable signal.

<!-- image -->

Table 55 - Indexing Category

| ID Parameter Name Description                                                                                 | Value/Notes   |
|---------------------------------------------------------------------------------------------------------------|---------------|
| 267 AutoStart Index Enable Auto Start index function for Indexing mode when drive becomes enabled 0 = Disable | 1 = Enable    |
| 632 Start Index  Indexing starts from index that is specified                                                 | 0…31          |
| 637 Current Index Index currently executing. This tag is valid only in Indexing mode.                         | 0…31          |

An index controls drive operation when Drive mode is set to Indexing in the General category. The drive starts indexing at the index whose number (0 … 31) is reflected in the cumulative binary values of the Index Select 0, 1, 2, 3, and 4 that are selected in the Digital Inputs category.

The digital input Index Select binary values are as follows:

- Index Select 0 = 1 if active, 0 if not.
- Index Select 1 = 2 if active, 0 if not.
- Index Select 2 = 4 if active, 0 if not.
- Index Select 3 = 8 if active, 0 if not.
- Index Select 4 = 16 if active, 0 if not.

If an Index Select is not assigned to a digital input, the Index Select is considered inactive.

When the Kinetix 300 drive is in Indexing mode the drive performs the required index-based position move, for each index, according to the parameters shown in Table 56. The Kinetix 300 drive supports up to 32 indexes.

The drive validates the index table before execution. During validation, if the drive encounters an error such as index entries that contain invalid values, the drive issues a fault. The fault does not allow execution of the index table until the anomaly has been corrected.

<!-- image -->

Table 56 - Index 00…31

| ID (1)  Parameter Name Description   |                                                                                                                                                                                                                     | Value/Notes (2)                                                                                                                                                                                                          |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                      | 272 Index Type Absolute with and without registration, incremental with and without registration, or blended incremental.                                                                                           | 0 = Absolute 1 = Incremental 2 = Registration absolute 3 = Registration incremental 4 = Blended 5 = Rotary absolute 6 = Rotary incremental 7 = Rotary shortest path 8 = Rotary positive 9 = Rotary negative 10 = Current |
| 273 Move                             | Trapezoidal or S-curve.                                                                                                                                                                                             | 0 = Trapezoidal 1 = S-curve                                                                                                                                                                                              |
| 274 Distance                         | The incremental distance to move or target position, which is based on the Index Type. 1…268435.4560 User Units                                                                                                     |                                                                                                                                                                                                                          |
| 275 Register Distance                | The incremental distance to move or target position, which is based on the Index Type. 1…268435.4560 User Units                                                                                                     |                                                                                                                                                                                                                          |
|                                      | 276 Batch Count How many times to execute index before moving on to the next index.                                                                                                                                 | 1…2147483647                                                                                                                                                                                                             |
| 277 Dwell                            | The time to remain at position before moving on to the next index. It is not applied between batches. If Index Type is Current, then Dwell is amount of time current level is applied.                              | 0…65535 ms                                                                                                                                                                                                               |
| 278 Velocity                         | The target speed when moving towards the new position. If the acceleration rate is too low, the axis cannot actually reach the target velocity. If Index type is Current, then Velocity is % rated current applied. | 0.0000…10,000,000.0000 User Units/s                                                                                                                                                                                      |
| 279 Accel                            | The rate to accelerate towards the configured velocity.                                                                                                                                                             | 0.0000…10,000,000.0000 User Units/s                                                                                                                                                                                      |
| 280 Decel                            | The rate to decelerate towards zero-velocity from configured-velocity.                                                                                                                                              | 0.0000…10,000,000.0000 User Units/s                                                                                                                                                                                      |
|                                      | 281 Next Index The next index to execute after the current index completes.                                                                                                                                         | 0…31                                                                                                                                                                                                                     |
| 282 Action                           | What to do when current index is complete.                                                                                                                                                                          | 0 = Stop 1 = Wait for start 2 = Next index                                                                                                                                                                               |

## Index Type Parameter

You can set the Index Type parameter to any of the following:

- Absolute
- Incremental
- Registration Absolute
- Registration Incremental
- Blended
- Rotary Absolute
- Rotary Incremental
- Rotary Shortest Path
- Rotary Positive
- Rotary Negative
- Current

## Absolute

Moves from its starting position to the specified Position. The axis must be homed before the drive can execute an absolute index otherwise an E27 fault is asserted.

## Incremental

Moves from its starting position the specified Distance.

## Registration Distance

Registration Distance is the relative distance that the motor travels beyond the position when a registration digital input is detected. If the indexing configuration Type is set to Registration Absolute or Registration Incremental, also configure the Registration Distance parameter. In Registration Indexing mode, the drive moves the motor from its starting position the specified Distance, provided the registration sensor input is not detected. If the registration sensor input is detected, the move is adjusted such that the Registration Distance setting determines the end position.

Figure 55 - Registration Index Type

<!-- image -->

## Blended

If the indexing configuration Type is set to Blended, the acceleration and deceleration parameters are not programmable. Instead, the drive calculates the parameters based the on distance and the velocity between the two points of the move. The index table contains the position and velocities necessary to assemble the profile.

## IMPORTANT

The full profile is assembled by stitching together a sequence of positions and velocities rather than complete move operations.

Figure 56 - Example of Blended Indexing

<!-- image -->

## Rotary Absolute

With a Rotary Absolute based move, the direction of travel depends on the current position of the motor and is not necessarily the shortest path to the end position. For start positions less than the end position, within the unwind, the result is motion in the positive direction; while start positions greater than the end position, within the unwind, results in motion in the negative direction.

The command position can be greater than the unwind value. Negative position values are equivalent to their corresponding positive values and are useful when rotating the axis through 0. For example, -90° is the same as +270°. When the position is greater than or equal to the unwind value, the axis moves through multiple revolutions of the unwind before stopping at an absolute position. The actual position on each revolution through the unwind starts at zero regardless of the number of revolutions performed.

Rotary Absolute mode is only possible when Rotary Unwind mode is configured in the General category.

Figure 57 - Rotary Absolute Move

<!-- image -->

## Rotary Incremental

With a Rotary Incremental based move, the direction of travel depends on the polarity of the commanded position. Positive commands result in motion in the positive direction and negative commands result in motion in the negative direction.

The command position can be greater than the unwind value. When the position is greater than or equal to the unwind value, the axis moves through multiple revolutions of the unwind before stopping. The actual position on each revolution through the unwind starts at zero regardless of the number of revolutions performed.

If your system has an absolute encoder, home the axis before initiating an absolute move otherwise the drive will fault with an E27.

Rotary Incremental mode is only possible when Rotary Unwind mode is configured in the General category.

## Rotary Shortest Path

The Rotary Shortest Path move is a special type of Absolute move. The motor is moved to the commanded position within the unwind in whichever direction of travel is the shortest, moving through 0° if necessary. With Rotary Shortest Path, the motor does not do multiple revolutions of unwind before stopping at an absolute position.

Rotary Shortest Path mode is only possible when Rotary Unwind mode is configured in the General category.

<!-- image -->

## Rotary Positive

The Rotary Positive move is a special type of Absolute move where the motor is moved to the commanded position within the unwind in the positive direction of travel moving through 0° if necessary. With Rotary Positive, move the motor does not do multiple revolutions of unwind before stopping at an absolute position.

Rotary Positive mode is only possible when Rotary Unwind mode is configured in the General category.

## Figure 59 - Rotary Positive Absolute Move

Rotary Negative

<!-- image -->

The Rotary Negative move is a special type of Absolute move where the motor is moved to the commanded position within the unwind in the negative direction of travel moving through 0° if necessary. With Rotary Negative, the motor cannot be moved multiple revolutions of unwind before stopping at an absolute position.

Rotary Negative mode is only possible when Rotary Unwind mode is configured in the General category.

## Figure 60 - Rotary Negative Absolute Move

<!-- image -->

## Current

The Kinetix 300 drive has a special-indexing configuration type of Current that supplies a specified current for a fixed time as part of executing the index table. You are able to transition to this type of index without disabling the drive. When in this mode, the position and velocity loops do not engage. When transitioning from Current mode to Position or Velocity mode, the drive begins to track commands with the current position or velocity of the drive. The drive does not attempt to correct for the movement of the motor while in Current mode.

When using Current Mode distance, velocity, acceleration, deceleration, and batch count parameters are not programmable.

In this type of index, the drive applies the specified current for the Dwell parameter number of milliseconds. All thermal protections continue to be active if the specified current exceeds the continuous current rating of the drive or motor. Figure 61 shows an example of a current index.

Figure 61 - Current Indexing

<!-- image -->

## Action Parameter

You can set the Action parameter to Stop, Wait for Start, or Next Index.

Stop

This action stops and holds zero velocity while remaining enabled. Upon assertion of the Start Index digital input or the Start Motion bit in the EtherNet/IP Output Assembly, the drive begins executing the index in the Index system parameter.

Figure 62 - Example of Stop and Hold Index Action

<!-- image -->

## Wait for Start

This action waits for either the Start Motion bit to transition in the EtherNet/ IP Output Assembly or for the Start Index configured digital input to perform an active transition.

Figure 63 - Example of Wait for Start Index Action

<!-- image -->

## Next Index

This action immediately moves to the next index as defined by the Next Index parameter.

Figure 64 - Example of Next Index Action

<!-- image -->

## Start Index

During powerup the Kinetix 300 drive does one of the following:

- Automatically start the indexing program upon enabling of the drive.
- Waiting for a digital input transition before starting the index.
- Waiting for a software signal over EtherNet/IP network before starting the index.

When the drive is configured for AutoStart Index, the drive begins executing the configured index immediately after the drive enables.

If the drive is not configured for AutoStart Indexing, the drive does not begin executing the configured index until either the Start Motion bit transitions in the EtherNet/IP Output Assembly or the digital input that is configured for Start Index is transitioned to an active state.

The configuration for Start Index requires setting the following parameters either over EtherNet/IP Explicit Messaging or through the MotionView software interface.

Table 57 - Start Index Configuration

| ID Parameter Name Description                                                                     | Value/Notes              |
|---------------------------------------------------------------------------------------------------|--------------------------|
| N/A Drive Mode Set to [Indexing]                                                                  | N/A                      |
| 267 AutoStart Index Enable Auto Start index function for Indexing mode when drive becomes enabled | 0 = Disable 1 = Enable   |
| 632 Start Index Indexing starts from index that is specified 0…31                                 |                          |
| 29 EnableSwitchType Enable switch function                                                        | 0 = Inhibit only 1 = Run |

## Abort Indexing

An active state ends an indexing sequence by decelerating to a stop and holding zero velocity while remaining enabled. No further indexing is executed until commanded by you or the controller.

The configuration for Abort Index can be set in the Add-on Profile (AOP) or through MotionView software interface as a digital input.

## Reset Index

Reset Index sets the current index to the Start Index.

## Explicit Messages for Indexing

The Kinetix 300 drive provides an EtherNet/IP assembly for configuring all parameters that are associated with one index from within one Explicit Message. To make one Explicit Message, make a User-Defined type in the RSLogix 5000 or RSLogix 500 software program, or Studio 5000 Logix Designer application that follows the structure that is shown in Figure 65. Send the User-defined type in a Set Attribute Single Explicit Message to class 4, instance 115 and attribute 3.

Figure 65 - Message Assembly Example

<!-- image -->

Table 58 - Explicit Messaging for Indexing

| RSLogix 5000 or Logix Designer Field   | Description                                                                                                                                       |
|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Index Number                           | This DINT contains the index number that is being modified.                                                                                       |
| Index Type                             | This DINT contains the type of the index, absolute, incremental, registration, or blended incremental.                                            |
| Index Move Type                        | This DINT contains the move type of the index Trapezoidal or S-curve.                                                                             |
| Index Distance                         | This REAL contains the move distance of the index.                                                                                                |
| Index Batch Count                      | This DINT contains the number of times the index executes before moving to the next index.                                                        |
| Index Dwell                            | This DINT contains the number of milliseconds the axis remains at position before moving to the next index.                                       |
| Index Velocity                         | This REAL contains the velocity that the axis moves at while moving the specified distance.                                                       |
|                                        | Index Maximum Acceleration This REAL contains the maximum acceleration that the axis used in reaching the index velocity.                         |
|                                        | Index Maximum Deceleration This REAL contains the maximum deceleration that the axis uses in when approaching the target position.                |
| Index Next Index                       | This DINT contains the next index that the drive begins executing after completing this index.                                                    |
| Index Action                           | This DINT contains the action that the drive takes once this index is complete.                                                                   |
|                                        | Index Registration Distance This REAL contains the displacement from the registration position the axis moves to if a registration index is used. |

Table 59 - Index Configuration Assembly Instance

| Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                                          |                                          |                                          |                                          |                                          |                                          |                                          |
|--------------------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|------------------------------------------|
| 0…3 Index Number (DINT)                                | 0…3 Index Number (DINT)                  | 0…3 Index Number (DINT)                  | 0…3 Index Number (DINT)                  | 0…3 Index Number (DINT)                  | 0…3 Index Number (DINT)                  | 0…3 Index Number (DINT)                  | 0…3 Index Number (DINT)                  |
| 4…7 Index Type (DINT)                                  | 4…7 Index Type (DINT)                    | 4…7 Index Type (DINT)                    | 4…7 Index Type (DINT)                    | 4…7 Index Type (DINT)                    | 4…7 Index Type (DINT)                    | 4…7 Index Type (DINT)                    | 4…7 Index Type (DINT)                    |
| 8…11 Index Move Type (DINT)                            | 8…11 Index Move Type (DINT)              | 8…11 Index Move Type (DINT)              | 8…11 Index Move Type (DINT)              | 8…11 Index Move Type (DINT)              | 8…11 Index Move Type (DINT)              | 8…11 Index Move Type (DINT)              | 8…11 Index Move Type (DINT)              |
| 12…15 Index Distance (REAL)                            | 12…15 Index Distance (REAL)              | 12…15 Index Distance (REAL)              | 12…15 Index Distance (REAL)              | 12…15 Index Distance (REAL)              | 12…15 Index Distance (REAL)              | 12…15 Index Distance (REAL)              | 12…15 Index Distance (REAL)              |
| 16…19 Index Batch Count (DINT)                         | 16…19 Index Batch Count (DINT)           | 16…19 Index Batch Count (DINT)           | 16…19 Index Batch Count (DINT)           | 16…19 Index Batch Count (DINT)           | 16…19 Index Batch Count (DINT)           | 16…19 Index Batch Count (DINT)           | 16…19 Index Batch Count (DINT)           |
| 20…23 Index Dwell (DINT)                               | 20…23 Index Dwell (DINT)                 | 20…23 Index Dwell (DINT)                 | 20…23 Index Dwell (DINT)                 | 20…23 Index Dwell (DINT)                 | 20…23 Index Dwell (DINT)                 | 20…23 Index Dwell (DINT)                 | 20…23 Index Dwell (DINT)                 |
| 24…27 Index Velocity (REAL)                            | 24…27 Index Velocity (REAL)              | 24…27 Index Velocity (REAL)              | 24…27 Index Velocity (REAL)              | 24…27 Index Velocity (REAL)              | 24…27 Index Velocity (REAL)              | 24…27 Index Velocity (REAL)              | 24…27 Index Velocity (REAL)              |
| 28…31 Index Maximum Acceleration (REAL)                | 28…31 Index Maximum Acceleration (REAL)  | 28…31 Index Maximum Acceleration (REAL)  | 28…31 Index Maximum Acceleration (REAL)  | 28…31 Index Maximum Acceleration (REAL)  | 28…31 Index Maximum Acceleration (REAL)  | 28…31 Index Maximum Acceleration (REAL)  | 28…31 Index Maximum Acceleration (REAL)  |
| 32…35 Index Maximum Deceleration (REAL)                | 32…35 Index Maximum Deceleration (REAL)  | 32…35 Index Maximum Deceleration (REAL)  | 32…35 Index Maximum Deceleration (REAL)  | 32…35 Index Maximum Deceleration (REAL)  | 32…35 Index Maximum Deceleration (REAL)  | 32…35 Index Maximum Deceleration (REAL)  | 32…35 Index Maximum Deceleration (REAL)  |
| 36…39 Index Next Index (DINT)                          | 36…39 Index Next Index (DINT)            | 36…39 Index Next Index (DINT)            | 36…39 Index Next Index (DINT)            | 36…39 Index Next Index (DINT)            | 36…39 Index Next Index (DINT)            | 36…39 Index Next Index (DINT)            | 36…39 Index Next Index (DINT)            |
| 40…43 Index Action (DINT)                              | 40…43 Index Action (DINT)                | 40…43 Index Action (DINT)                | 40…43 Index Action (DINT)                | 40…43 Index Action (DINT)                | 40…43 Index Action (DINT)                | 40…43 Index Action (DINT)                | 40…43 Index Action (DINT)                |
| 44…47 Index Registration Distance (REAL)               | 44…47 Index Registration Distance (REAL) | 44…47 Index Registration Distance (REAL) | 44…47 Index Registration Distance (REAL) | 44…47 Index Registration Distance (REAL) | 44…47 Index Registration Distance (REAL) | 44…47 Index Registration Distance (REAL) | 44…47 Index Registration Distance (REAL) |

In this Index Configuration Assembly example, the parameter Index Number with a range of 0…3 bytes is expanded to show the low, low middle, high middle, and high bytes. These values are typical for each parameter in Table 59 .

Table 60 - Index Configuration Assembly Example

| Byte Parameter Value              |
|-----------------------------------|
| 0 Index Number - Low byte         |
| 1 Index Number - Low middle byte  |
| 2 Index Number - High middle byte |
| 3 Index Number - High byte        |

Table 61 - ID Tag Numbers for Indexes 00…15

| Parameter Name 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15                    |                                                                      |                                                                 |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------|
| Index Type 272 283 294 305 316 327 338 349 360 371 382 293 404 415 426 437        |                                                                      |                                                                 |
|                                                                                   | Move 273 284 295 306 317 328 339 350 361 372 383 294 405 416 427 438 |                                                                 |
| Distance 274 285 296 307 318 329 340 351 362 373 384 295 406 417 428 439          |                                                                      |                                                                 |
| Register Distance 275 286 297 308 319 330 341 352 363 374 385 296 407 418 429 440 |                                                                      |                                                                 |
| Batch Count 276 287 298 309 320 331 342 353 364 375 386 297 408 419 430 441       |                                                                      |                                                                 |
| Dwell                                                                             |                                                                      | 277 288 299 310 321 332 343 354 365 376 387 298 409 420 431 442 |
| Velocity                                                                          | 278 289 300 311 322 333 344 355 366 377 388 299 410 421 432 443      |                                                                 |
| Accel                                                                             | 279 290 301 312 323 334 345 356 367 378 389 400 411 422 433 444      |                                                                 |
| Decel                                                                             | 280 291 302 313 324 335 346 357 368 379 390 401 412 423 434 445      |                                                                 |
| Next Index 281 292 303 314 325 336 347 358 369 380 391 402 413 424 435 446        |                                                                      |                                                                 |
| Action                                                                            |                                                                      | 282 293 304 315 326 337 348 359 370 381 392 403 414 425 436 447 |

Table 62 - ID Tag Numbers for Indexes 16…31

| Parameter Name 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31                    |                                                                       |                                                                 |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------|
| Index Type 448 459 470 481 492 503 514 525 536 547 558 569 580 591 602 613        |                                                                       |                                                                 |
|                                                                                   | Move 449 460 471 482 493 504 515 526 537 548 559 570 581 592 603 614  |                                                                 |
| Distance 450 461 472 483 494 505 516 527 538 549 560 571 582 593 604 615          |                                                                       |                                                                 |
| Register Distance 451 462 473 484 495 506 517 528 539 550 561 572 583 594 605 616 |                                                                       |                                                                 |
| Batch Count 452 463 474 485 496 507 518 529 540 551 562 573 584 595 606 617       |                                                                       |                                                                 |
|                                                                                   | Dwell 453 464 475 486 497 508 519 530 541 552 563 574 585 596 607 618 |                                                                 |
| Velocity                                                                          | 454 465 476 487 498 509 520 531 542 553 564 575 586 597 608 619       |                                                                 |
| Accel                                                                             | 455 466 477 488 499 510 521 532 543 554 565 576 587 598 609 620       |                                                                 |
| Decel                                                                             | 456 467 478 489 500 511 522 533 544 555 566 577 588 599 610 621       |                                                                 |
| Next Index 457 468 479 490 501 512 523 534 545 556 567 578 589 600 611 622        |                                                                       |                                                                 |
| Action                                                                            |                                                                       | 458 469 480 491 502 513 524 535 546 557 568 579 590 601 612 623 |

## Homing Category

The Kinetix 300 drives have a predefined (firmware-based) homing functionality. The supported homing methods include limit switches at the ends of travel, a dedicated home switch, an index pulse, or zero reference from the motor feedback device, or a combination of all.

<!-- image -->

The configuration for Homing requires setting these parameters either over EtherNet/IP Explicit Messaging or through the embedded software interface.

Table 63 - Homing Category

| ID Parameter Name Description                                                                                                                                                               | Value/Notes                                                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 227 Home Accel/Decel Homing acceleration/deceleration rate                                                                                                                                  | Range 0…10,000,000 UU per second  2 .                                         |
| 228 Home Offset The new position of the motor after the homing sequence is complete. All subsequent absolute moves are taken relative to this new zero position.                            | Range: -32767…+32767 user units.                                              |
| 230 Home Velocity Fast For homing methods that use one velocity setting, this tag is used as the velocity.                                                                                  | Range: -10,000…10,000 UU/sec.                                                 |
| 231 Home Velocity Slow For homing methods that use two velocity settings (fast and slow), this tag is used as the slow velocity. Typically, this tag is used to creep to a homing position. | Range: -10,000…10,000 UU/sec.                                                 |
| 232 Home Method Defines the type of homing to be performed. See Table 64 on page 113 .                                                                                                      | N/A                                                                           |
| 234 Home Switch The digital input that is used as a home switch for the appropriate homing method.                                                                                          | Do not assign to A1, A2, A3, or C3 as these inputs have predefined functions. |

## Homing Methods

To use homing methods involving Motor Index Pulse (zero pulse), the index pulse of the motor must be connected to the drive input. When the drive has been homed, it asserts the Homed bit in the EtherNet/IP Output Assembly.

The drive indicates whether the homing completed successfully or not. Once homing has been initiated, the Homing Active status bit in the EtherNet/IP Input Assembly is set. If the Homing Active status bit is no longer set and the Homed status bit is also not set, then an error has occurred in the homing and the drive is not homed.

If the drive has not been homed or the stored absolute position information from an absolute home is no longer valid, any absolute position moves generate a fault. Incremental position moves do not generate a fault.

Absolute homing is the only method that is retained after power cycles. With any other homing method, the Homed bit is not set following a power cycle until the homing has been repeated.

The absolute position information within the drive (if absolute homed) is cleared and the Homed bit cleared if any of these events occur:

- A change of motor encoder is detected.
- A change of motion polarity is made.
- The absolute position information within the motor nonvolatile memory does not match the absolute position information within the drive nonvolatile memory (if absolute homed).
- A feedback-related fault has occurred.
- At power-up drive is reporting a battery error.

If your drive is set to Indexing mode and you are not using a controller, a home switch is required to automatically home your incremental encoder at powerup.

| IMPORTANT   | All homing methods write to the nonvolatile memory in the drive, which is limited to 1 million write cycles. The drive must not be homed more often than 1 million times.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table 64 - Homing Methods Summary

| Home Method (1) (2) Direction                          | Homing Type Home Sensor Polarity   |
|--------------------------|------------------------------------|
| 7 Switch-Marker Forward  | Bi-directional Active/Rising       |
| 8 Switch-Marker Forward  | Uni-directional Active/Rising      |
| 9 Switch-Marker Forward  | Bi-directional Active/Falling      |
| 10 Switch-Marker Forward | Uni-directional Active/Falling     |
| 11 Switch-Marker Reverse | Bi-directional Active/Rising       |
| 12 Switch-Marker Reverse | Uni-directional Active/Rising      |
| 13 Switch-Marker Reverse | Bi-directional Active/Falling      |
| 14 Switch-Marker Reverse | Uni-directional Active/Falling     |
| 23 Switch-Fast Forward   | Home to sensor Active/Rising       |
| 25 Switch-Slow Forward   | Home to sensor Active/Falling      |
| 27 Switch-Slow Reverse   | Home to sensor Active/Falling      |
| 29 Switch-Fast Reverse   | Home to sensor Active/Rising       |
| 33 Marker  Reverse       | Home to marker N/A                 |
| 34 Marker  Forward       | Home to marker N/A                 |
| 35 Immediate  N/A        | N/A  N/A                           |

## Immediate Homing

The immediate home operation on the drive defines the current position of the motor to be the home and the position set to the [HomeOffset] parameter. The drive must be in Indexing mode or EtherNet/IP Positioning mode and the drive must be enabled.

## Absolute Homing

The absolute homing on the drive behaves similarly to the Immediate Homing operation. The homing does not induce shaft motion on the motor. The current position of the motor is the home position and the position is set to the [HomeOffset] parameter.

The difference between the absolute position in the encoder and the [HomeOffset] parameter is stored in nonvolatile memory so that all absolute motion is relative to the current position. After a power cycle, the drive continues to operate as though it was homed.

For absolute homing on motors with absolute encoders, execute an Immediate Home.

## Home to Marker

On incremental encoders, the drive uses the marker pulse that generated by the encoder as the marker for active homing.

On absolute encoders without a marker pulse, the drive synthesizes (internal to the drive firmware only) a marker pulse that is a consistent position once per mechanical rotation of the motor. The drive uses the generated marker pulse as the marker for active homing of an absolute encoder.

## Home Offset

The home offset parameter is the difference between the zero-position for the application and the machine home-position (found during homing). Once homing is completed, the zero-position is offset from the home-position by adding the home-offset to the home position. All subsequent absolute moves are taken relative to this new zero position.

## Homing Switch

The homing switch tag enables you to select the drive input that is used for the Home Switch connection. The Homing Switch Input Assignment range is 0…11. Inputs A1…A4 are assigned 0…3 respectively; inputs B1…B4 are assigned 4…7 respectively; and inputs C1…C4 are assigned 8…11 respectively. Do not assign to A1, A2, A3, or C3 as these inputs have predefined functions.

## Homing Firmware Algorithm

Figure 66 - Homing Algorithm Flowchart

<!-- image -->

## Homing Methods Timing Diagrams

For a summary of the homing methods, see Table 64 on page 113 .

## Homing Methods 7…14

Homing methods 7…14 use a home switch that is active over only a portion of the travel. In effect, the switch has a momentary action as the axis position sweeps past the switch. Using methods 7…10, the initial direction of movement is forward and by using methods 11…14, the initial direction of movement is reverse. Except if the home switch is active at the start of motion, in this case, the initial direction of motion is dependent on the edge being sought. The home position is at the index pulse on either side of the rising or falling edges of the home switch, as shown in the following two diagrams. If the initial direction of movement leads away from the home switch, the drive must reverse on encountering the relevant limit switch. All of these methods use the fast acceleration parameter.

Figure 67 - Homing Methods 7…10 (forward initial move)

<!-- image -->

Figure 68 - Homing Methods 11…14 (reverse initial move)

<!-- image -->

## Homing Method 23

Using this method, the initial direction of movement is forward (if the homing switch is inactive). The home position is the leading edge of the homing switch.

The axis accelerates to fast-homing velocity in the forward direction and motion continues until the homing switch is activated (rising edge) shown at position A. The axis decelerates to zero velocity.

If the homing switch is already active when the homing routine commences, then this initial move is not executed.

The axis accelerates to fast-homing velocity in the reverse direction and motion continues until the falling-edge of the homing switch is detected (position B), where the axis decelerates to 0 velocity. The axis accelerates to slow-homing velocity in the forward direction and motion continues until the rising-edge of the homing switch is detected (position C), where the axis decelerates to 0 velocity. The axis accelerates to slow-homing velocity in the reverse direction and motion continues until the falling-edge of the homing switch is detected (position 23). Position 23 is the home position (excluding offset).

TIP If the axis is on the wrong side of the homing switch when homing is started, the axis moves forward until it contacts the positive limit switch. Upon activating the positive limit switch the axis changes direction (reverse), following the procedure that is detailed in Homing Method 23 , but ignoring the initial move in the forward direction.

Figure 69 - Homing Method 23

<!-- image -->

## Homing Method 25

Using this method, the initial direction of movement is forward. The home position is the falling-edge of the homing switch.

The axis accelerates to fast-homing velocity in the forward direction and motion continues until the homing switch is deactivated (falling edge) shown at position A. The axis decelerates to zero velocity.

The axis accelerates to slow-homing velocity in the leftward direction. Motion continues until the rising-edge of the homing switch is detected (position B), where the axis decelerates to 0 velocity. The axis accelerates to slow-homing velocity in the rightward direction. Motion continues until the falling-edge of the homing switch is detected (position 25). Position 25 is the home position (excluding offset).

TIP If the axis is on the wrong side of the homing switch when homing is started, the axis moves forward until it contacts the positive limit switch (A2). Upon activating the positive limit switch, the axis changes direction (reverse) and continue motion until it sees the rising edge of the homing switch. The axis stops and follows the procedure as detailed Homing Method 25 .

Figure 70 - Homing Method 25

<!-- image -->

## Homing Method 27

Using this method, the initial direction of movement is reverse. The home position is the falling-edge of the homing switch.

The axis accelerates to fast-homing velocity in the reverse direction and motion continues until homing switch is deactivated (falling edge) shown at position A. The axis decelerates to zero velocity.

The axis accelerates to slow-homing velocity in the forward direction. Motion continues until the rising-edge of the homing switch is detected (position B), where the axis decelerates to 0 velocity.

The axis accelerates to slow-homing velocity in the reverse direction. Motion continues until the falling-edge of the homing switch is detected (position 27). Position 27 is the home position (excluding offset).

TIP If the axis is on the wrong side of the homing switch when homing is started, then the axis moves reverse until it contacts the negative limit switch (A1). Upon activating the negative limit switch, the axis changes direction (forward) and continues motion until it sees the rising-edge of the homing switch. The axis stops and follows the procedure as detailed Homing Method 27 .

Figure 71 - Homing Method 27

<!-- image -->

## Homing Method 29

Using this method, the initial direction of movement is reverse (if the homing switch is inactive). The home position is the leading edge of the homing switch.

The axis accelerates to fast-homing velocity in the leftward direction and continues until the homing switch is activated (rising edge) shown at position A. The axis decelerates to zero velocity. If the homing switch is already active when the homing routine commences, then this initial move is not executed.

The axis accelerates to fast-homing velocity in the forward direction. Motion continues until the falling-edge of the homing switch is detected (position B), where the axis decelerates to 0 velocity.

The axis accelerates to slow-homing velocity in the reverse direction. Motion continues until the rising-edge of the homing switch is detected (position C), where the axis decelerates to 0 velocity.

The axis accelerates to slow-homing velocity in the rightward direction. Motion continues until the falling-edge of the homing switch is detected (position 29). Position 29 is the home position (excluding offset).

TIP If the axis is on the wrong side of the homing switch when homing is started, the axis moves reverse until it contacts the negative limit switch (A1). Upon activating the negative limit switch, the axis changes direction (forward) following the procedure as detailed in Homing Method 29, but ignoring the initial move in the reverse direction.

Figure 72 - Homing Method 29

<!-- image -->

## Homing Method 33

Using this method, the initial direction of movement is reverse. The home position is the first index pulse past the shaft starting position. The axis accelerates to fast-homing velocity in the reverse direction and continues until the rising-edge of the first index pulse (position 33) is detected.

Figure 73 - Homing Method 33

<!-- image -->

## Homing Method 34

Using this method, the initial direction of movement is forward. The home position is the first index pulse past the shaft starting position. The axis accelerates to fast-homing velocity in the forward direction and continues until the rising-edge of the first index pulse (position 34) is detected.

Figure 74 - Homing Method 34

<!-- image -->

## Homing Method 35

Using this method, the current position is assumed to be the home position. There is no motion of the motor shaft during this procedure. Any offset specified is added to the stored home position.

## Upgrade Firmware

Follow these steps to upgrade the firmware in your Kinetix 300 drive.

1. Obtain the latest firmware from rok.auto/pcdc .
2. Run the MotionView software.
3. Click Upgrade.

This dialog box appears.

<!-- image -->

4. Comply with dialog box requests and click yes.

This dialog box appears.

<!-- image -->

5. Enter the IP address of the Kinetix 300 drive that you intend to upgrade.
6. Navigate to the .lar file that you downloaded in step 1.
7. Click Upgrade Firmware.

Do not turn off power to the computer or the drive.

8. When the upgrade is finished, restart the drive.

Access the upgraded MotionView software by entering the drives IP address in a web browser.

<!-- image -->

## Configure and Start Up the Kinetix 300 Drive

| Topic                                                     |   Page |
|-----------------------------------------------------------|--------|
| Keypad Input                                              |    124 |
| Configure the Kinetix 300 Drive EtherNet/IP Address       |    126 |
| Configuring the Logix EtherNet/IP Module                  |    131 |
| Apply Power to the Kinetix 300 Drive                      |    137 |
| Test and Tune the Axis                                    |    138 |
| Select Drive Operating Mode                               |    142 |
| Master Gearing Mode Examples                              |    143 |
| Configure the Drive Parameters and System Variables       |    145 |
| Configure Drive Mode with Explicit Messaging              |    148 |
| Configure Drive for Linear Motors and Direct Drive Stages |    150 |

## Keypad Input

<!-- image -->

The Kinetix® 300 drive is equipped with a diagnostic status indicator and three push buttons that are used to select displayed information and to edit a limited set of parameter values. You can scroll the parameters by using . To view a value, press . To return to Scroll mode press again.

<!-- image -->

<!-- image -->

When you press on editable parameters, the yellow status indicator (C) blinks, the blinking indicates that the parameter value can be changed. Use

<!-- image -->

to change the value. To store the new setting and return to Scroll mode press .

<!-- image -->

Table 65 - Status Display Information

| Status Indicator Description   |                                                                                                                  |
|--------------------------------|------------------------------------------------------------------------------------------------------------------|
| StAt                           | Current drive status - run = drive running, diS = drive disabled, EXX = Drive fault, where XX is the fault code. |
| Hx.xx                          | Hardware revision. For example, H2.00.                                                                           |
| Fx.xx                          | Firmware version. For example, F2.06.                                                                            |
| FLtS                           | Stored fault history. You can scroll through stored faults E0XX…E7XX, where XX is the fault code.                |
| Ht                             | Heatsink temperature. Heatsink temperature is shown ºC if greater than 40 ºC. Otherwise ‘LO (low) is displayed.  |
| EnC                            | Encoder activity. Primary encoder counts are displayed for encoder diagnostics.                                  |
| buS                            | Displays drive DC bus voltage.                                                                                   |
| Curr                           | Displays motor phase current (RMS). Shows current value if drive is enabled, otherwise shows DiS.                |
| boot                           | 0 = autostart disabled, 1 = autostart enabled.                                                                   |
| dHCP                           | Ethernet DHCP Configuration: 0=dHCP is disabled; 1=dHCP is enabled.                                              |
| IP_1                           | First octet of the IP address.                                                                                   |
| IP_2                           | Second octet of the IP address.                                                                                  |
| IP_3                           | Third octet of the IP address.                                                                                   |
| IP_4                           | Fourth octet of the IP address (changeable).                                                                     |

<!-- image -->

## Status Indicators

The Kinetix 300 drive has five status indicators around the periphery of the front panel display as shown in Figure 75. These status indicators that are used to monitor the system status, activity, and troubleshoot faults.

Figure 75 - Front Panel Display

<!-- image -->

Figure 76 - Status Indicators

| Status Indicator   | Function Description                                                               |
|--------------------|------------------------------------------------------------------------------------|
| A Enable           | Orange status indicator means that the drive is enabled (running).                 |
| B Regen            | Yellow status indicator means the drive is in Regeneration mode.                   |
|                    | C Data entry Yellow status indicator flashes when changing.                        |
|                    | D Drive fault Red status indicator illuminates upon a drive fault.                 |
|                    | E Comm activity Green status indicator flashes to indicate communication activity. |

## Configure the Kinetix 300 Drive EtherNet/IP Address

This section offers guidance on how to configure your Ethernet connection to the Kinetix 300 drive.

TIP To run MotionView OnBoard on a Mac OS, run the personal-computer emulation tool first.

## Ethernet Connection

Configuration, programming, and diagnostics of the Kinetix 300 drive are performed over the standard 10/100 Mbps Ethernet communication port by using the MotionView OnBoard software that is contained within the drive itself.

To access the MotionView OnBoard software, the Kinetix 300 drive and your personal computer must be configured to operate on the same Ethernet network. The IP addresses of the Kinetix 300 drive, the personal computer, or both drive and personal computer can require configuring to enable Ethernet communication between the two devices.

| IMPORTANT   | Any changes that are made to Ethernet communication settings on the Kinetix 300 drive do not take effect until the drive is powered off and powered on again. The drive continues to use the previous settings until power is cycled.                                                              |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TIP         | For personal computers with an Ethernet port that is used for a specific purpose, such as email or web browsing, it can more convenient for you to add an Ethernet port. Install a USB/Ethernet dongle or a PCMCIA Ethernet card to gain an extra port for communication to the Kinetix 300 drive. |

## Kinetix 300 Drive Ethernet Port Configuration

The IP address of the Kinetix 300 drive is composed of four sub-octets separated by three dots to conform to the Class C Subnet structure. Valid configurations for sub-octets are between 001…254. The default IP address for any Kinetix 300 drive is 192.168.124.200.

There are two methods to change the current IP address. An address can be assigned to the drive automatically (dynamic IP address) when the drive is connected to a DHCP (Dynamic Host Configuration Protocol) enabled server, or you can assign the drive IP address manually (static IP address). Both methods to configure the drives IP address are shown here.

## Current IP Address Ethernet Setting

The current Ethernet setting and IP address of the Kinetix 300 drive can be obtained from the drive display and keypad. Press on the display and use

<!-- image -->

to access parameters IP\_1, IP\_2, IP\_3 and IP\_4. Each of these parameters contains one sub-octet of the full IP address, for example in the case of the drive default (factory set) address parameters:

- IP\_1 = 192
- IP\_2 = 168
- IP\_3 = 124
- IP\_4 = 200

By accessing these four parameters, the full IP address on the drive can be obtained.

If parameters IP\_1, IP\_2, IP\_3 and IP\_4 all contain '----' rather than a numerical values it means that the drive has DHCP enabled and the DHCP server is yet to assign the drive its dynamic IP address. When DHCP server assigns an IP address, the drive displays the assigned address in the IP\_x parameters. See Configure the IP Address Automatically (dynamic address) on page 129 .

## Configure the IP Address Manually (static address)

When connecting directly from the Kinetix 300 drive to the personal computer without a server or when connecting to a private network, where all devices have static IP addresses, assign the IP address of the Kinetix 300 manually.

To assign the address manually, disable the DHCP mode by using the drive keypad and following these steps.

1. Press .
2. Use to access parameter DHCP.
3. Verify DHCP parameter is set to a value of 0.

<!-- image -->

<!-- image -->

<!-- image -->

If the DHCP parameter is set to 1, use and to change the value to 0.

4. Cycle power to the drive.

The change takes effect.

When DHCP is disabled and the drive power is cycled, The IP address reverts to the previous static IP address.

<!-- image -->

If you are connecting multiple drives to the personal computer, create a unique IP address for each drive by using the keypad on each drive. Change the IP\_4 parameter. IP\_4 is the only octet that can be changed via the keypad. IP\_1, IP2, and IP\_3 are read-only accessed this way. The drive power must be cycled for changes to take effect.

To configure the Kinetix 300 drive for a specific subnet or change its full IP address, use the MotionView configuration tool.

1. Run a Java enabled web browser.
2. Enter the current IP address of the drive into the browser.
3. MotionView OnBoard dialog box opens.
3. Click Run.
4. Click Connect.
5. Enter the IP address of the drive.
6. Click Connect.
7. From the Drive Organizer, select Communications &gt; Ethernet.

The IP address, subnet mask, and default gateway address can be edited in this screen. If the text turns red when entered, the values or format that is used are invalid and they are not applied.

<!-- image -->

8. Check Obtain IP Address by using DHCP, to enable DHCP.

To disable DHCP, Clear Obtain IP Address by using DHCP.

9. To make changes to take effect, cycle power.

The first time that you change an Ethernet parameter, the following dialog box opens. Click OK and cycle power for changes to take effect.

<!-- image -->

## Configure the IP Address Automatically (dynamic address)

When connecting a Kinetix 300 drive to a network domain with a DHCP enabled server, the IP address of the Kinetix 300 drive is assigned automatically. To automatically assign the address, the drive must have its DHCP mode enabled. Follow these steps by using the drive keypad and display.

1. Press .
2. Use to access parameter DHCP.
3. Check this parameter is set to 1.
4. If the DHCP parameter is set to 0, use and to change the parameter setting to 1.
5. Cycle the drive power to effect the change.

<!-- image -->

When the Kinetix 300 drive is waiting for an IP address to be assigned by the server it displays '----' in each of the four octet parameters (IP\_1, IP\_2, IP\_3, and IP\_4). Once the address is assigned, it appears in IP\_x parameters. If the parameters continues to display '----', then it is likely that a connection between the drive and server has not been established, or the server is not DHCP enabled.

DHCP can be enabled through the MotionView software. If you choose to configure the drive by using a manual (static) IP address, you can switch over to an automatic (dynamic) address once configuration is complete. See Current IP Address Ethernet Setting on page 127 for information on enabling DHCP from within the MotionView software.

TIP A useful feature of the MotionView software and communication interface to the Kinetix 300 drive is the ability to assign the drive a name (text string). This name can then be used to discover the drives IP address and is useful when the drive has its IP address automatically assigned by the server.

## Install the Kinetix 300 Add-on Profile

To select Kinetix 300 drives in RSLogix 5000® software, version 17, the Kinetix 300 Add-On Profile (AOP) is required. The AOP is available from the Product Compatibility Download Center (PCDC) website: http://compatibility.rockwellautomation.com/Pages/home.aspx. If you are using RSLogix 5000 software, version 18 or later, or the Studio 5000 Logix Designer® application you do not need the AOP.

Follow these steps to download the Kinetix 300 drives Add-On Profile.

1. Go to the Product Compatibility Download Center and enter Kinetix 300 in the Search PCDC window.
2. Click AOP for 2097 Kinetix 300 Drives v2.01.02.
3. Click Download.
4. Scroll down to Add On Profiles and check Select Files.
5. Scroll down and check AOP for 2097 Kinetix 300 Drives v2.01.02.
6. Click Downloads.
7. Continue with the AOP download.

<!-- image -->

<!-- image -->

<!-- image -->

## Configuring the Logix EtherNet/IP Module

This procedure assumes that you have wired your Kinetix 300 drive.

IMPORTANT

For the Kinetix 300 drive to communicate with the Ethernet network module you must be using RSLogix 5000 software (version 17 or later) or the Studio 5000 Logix Designer application.

For help using RSLogix 5000 software or the Studio 5000 Logix Designer application to configure the ControlLogix®, CompactLogix™, or SoftLogix™ EtherNet/IP™ modules, See Additional Resources on page 10 .

## Configure the Logix Controller

Follow these steps to configure the Logix controller.

1. Apply power to your Logix chassis that contains the Ethernet interface module/PCI card and open your RSLogix 5000 software or the Logix Designer application.
2. From the File menu, choose New.

The New Controller dialog box opens.

<!-- image -->

3. Configure the new controller.
- a. From the Type pull-down menu, choose your controller type. In this example, the CompactLogix L23E-QB1 controller is chosen.
- b. Enter your RSLogix 5000 software or the Logix Designer application version.
- c. From the Chassis Type pull-down menu, choose your chassis. This step applies only for ControlLogix controllers.
- d. Enter the slot where your module resides (leftmost slot = 0). This step applies only for ControlLogix controllers.
- e. Name the file.
4. Click OK.
5. From the Edit menu, choose Controller Properties.

The Controller Properties dialog box opens.

<!-- image -->

6. Click the Date and Time tab.
7. Check the box Make this controller the Coordinated System Time master.

IMPORTANT

You can assign only one ControlLogix controller as the Coordinated System Time master.

8. Click OK.

## Configure the Ethernet Port

This section applies when the CompactLogix controller, catalog number 1769L23E-QB1, is used.

Follow these steps to configure the Ethernet port.

1. Right-click the embedded 1769-L23E-QB1 Ethernet port and choose Properties.

<!-- image -->

The Module Properties dialog box opens.

<!-- image -->

2. Enter the IP address of the Ethernet port.

In this example, the IP address 192.168.124.2. is the controller Ethernet address, not the drive Ethernet address.

3. Click OK.

## Configure the Ethernet Module

This section applies when the ControlLogix controller, catalog number 1756ENET/B, is used.

Follow these steps to configure the Ethernet module.

1. Right-click I/O Configuration in the Controller Organizer and choose New Module.

<!-- image -->

The Select Module dialog box opens.

<!-- image -->

2. Expand the Communications category and select 1756-Exx/x appropriate for your actual hardware configuration.

In this example, the 1756-ENET/B module is chosen.

3. Click OK.

The New Module dialog box opens.

<!-- image -->

4. Configure the new module.
- a. Name the module.
- b. Enter the IP address of the Ethernet module.
4. In this example, the IP address 192.168.124.2. is the controller Ethernet address, not the drive Ethernet address.
- c. Enter the slot where your module resides (leftmost slot = 0).
5. Click OK.

## Configure the Kinetix 300 Drive

Follow these steps to configure the Kinetix 300 drive.

1. Right-click the embedded 1769-L23E Ethernet port and choose New Module.

<!-- image -->

The Select Module dialog box opens.

<!-- image -->

2. Expand the Drives category and select your Bulletin 2097 drive as appropriate for your actual hardware configuration.

In this example, the 2097-V33PR3 drive is selected.

3. Click OK.

The New Module dialog box opens.

<!-- image -->

4. Configure the new module.
- a. Name the module.
- b. Set the drive Ethernet address.

Set the Ethernet address in the software to match the Ethernet address scrolls on the drive. See Current IP Address Ethernet Setting on page 127 .

5. Click the Connection tab.
6. Configure the Requested Packet Interval (RPI) for your application. The default setting is 20 ms. Yours could be different.
7. Click Ok.

<!-- image -->

## Download the Program

After you complete the Logix configuration, you must download your program to the Logix processor.

## Apply Power to the Kinetix 300 Drive

This procedure assumes that you have wired and configured your Kinetix 300 drive system and your EtherNet/IP interface module.

<!-- image -->

To avoid hazard of electrical shock, mount and wire the Bulletin 2097 drive before you apply power. Once power is applied, connector terminals can have voltage present even when not in use.

Follow these steps to apply power to the Kinetix 300 drive system.

1. Disconnect the load to the motor.

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, disconnect the load to the motor. Make sure each motor is free of all linkages when initially you apply power to the system.

2. Determine the source of the drive logic power.
3. Apply mains input power to the Kinetix 300 drive IPD connector.
4. Observe the four character status indicator.
5. Determine the source of logic power.
6. Verify that Hardware Enable Input signal IOD connector pin 29 is at 0V.

| If Your Logic Power       | Then                                                                                     |
|---------------------------|------------------------------------------------------------------------------------------|
|                           | Is from (24V DC) back-up power Apply (24V DC) back-up power to the drive (BP connector). |
| Is from Mains input power | Apply mains input power to the drive (IPD connector).                                    |

<!-- image -->

| If the status indicator is   | Then                  |
|------------------------------|-----------------------|
| diS                          | Go to step 5          |
| Blank                        | Return to main step 2 |

| If Your Logic Power   | Then                                                                                |
|-----------------------|-------------------------------------------------------------------------------------|
|                       | Is from (24V DC) back-up power Apply mains input power to the drive (IPD connector) |
| Mains input power     | Go to step 6                                                                        |

7. Observe the status indicator on the front of the Kinetix 300 drive.

| Status Indicator Condition   | Status  Do This                                                  |
|------------------------------|------------------------------------------------------------------|
| Drive Fault  Off             | Normal condition Observe the Comm Activity, status indicator E.  |
| Steady red                   | Drive has a fault Go to Status Indicators on page 125.           |
| Comm Activity Flashes        | Communication is ready Go to Test and Tune the Axis on page 138. |
| Off                          | No communication Go to Status Indicators on page 125.            |

## Test and Tune the Axis

This procedure assumes that you have configured your Kinetix 300 drive, your Logix Ethernet module, and applied power to the system.

IMPORTANT

Before you test and tune your axis, verify that the Kinetix 300 drive status indicators are operating as described in step 7 on page 138 .

## Test the Axis

This procedure applies only to motors with incremental encoders. When using motors with absolute encoders skip, to Tune the Axis. Follow these steps to test the axis.

1. Verify the load was removed from each axis.
2. Run the MotionView OnBoard software.
3. Select the Motor category.
4. Click Check Phasing.
5. Apply Enable Input signal (IOD-29) for the axis you are testing.

<!-- image -->

<!-- image -->

ATTENTION: To avoid personal injury or damage to equipment, apply Enable Input (IOD-29) only to the axis you are testing.

6. Click Start Autophasing.

7. Determine if your test completed successfully.

| If                                                                                                | Then                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Your test has completed successfully and dialog box opened that states motor is phased correctly. | 1. Click Ok. 2. Remove Enable Input signal. 3. Go to Tune the Axis on page 139 .                                                                                                                |
| Your test did not complete successfully.                                                          | 1. Click Ok. 2. Verify that the Enable Input signal is applied to the axis you are testing. 3. Verify the motor feedback is wired as required. 4. Return to main step 6 and run the test again. |

## Tune the Axis

Follow these steps to tune the axes.

1. Verify the load is removed from the axis you want to tune.

<!-- image -->

ATTENTION: To reduce the possibility of unpredictable motor response tune your motor with the load removed first, then reattach the load and perform the tuning procedure again to provide an accurate operational response.

2. Run the MotionView OnBoard software.
3. Select General.
4. From the Drive Mode pull-down menu, choose Auto Tune.
5. Select Dynamics.

The current velocity and position gains, position limit, and scaling are displayed.

6. If you are using a linear incremental encoder with a resolution greater than 1 μm, do the following. Otherwise continue with the next step.
- a. Set FeedBack Filter to Yes.
- b. Set the time constant to 1 ms.
4. TIP To reduce the audible noise when a Kinetix LDAT linear thruster with an absolute encoder option is under servo control, we recommend that you use a low-pass filter with the cut-off frequency set to 150 Hz. You can configure the filter in the Dynamics category.
7. Click Autotuning.

The Autotuning dialog box opens.

<!-- image -->

8. Check desired Tuning boxes (Velocity/Position or both).
9. Enter the Travel Limit.

The Travel Limit is the maximum distance in User Units that the motor shaft or actuator can safely travel during the tuning procedure

10. Apply Enable Input signal for the axis you are tuning.
11. To enable the axis, set the DriveEn bit in RSLogix 5000 software or the Logix Designer application for the axis being tuned.
12. Click Start.

The Tune gains dialog box opens.

13. Click Yes.
14. Determine if your test completed successfully.

<!-- image -->

15. Check that the Position Error is in the range of 25…40 mm for safest operation
16. Select General.
17. From the Drive Mode pull-down menu, choose the mode that you desire.

TIP If motion performance is not what you expected after tuning the drive, several filters are available to improve performance. These filters are configured from the Dynamics view of the MotionView software and their placement within the servo loops are shown in the figure on page 96 .

## Select Drive Operating Mode

This procedure assumes that you have configured your Kinetix 300 drive, your Logix Ethernet module, and applied power to the drive.

The drive operating mode determines the command source for the drive. You can configure the drive from MotionView software or by Explicit Messaging, instance 266, to the drive object.

Follow these steps to select the drive operating mode by using MotionView software.

1. Verify the load was removed from each axis.
2. Run the MotionView software.
3. From the Drive Organizer, select General.
4. From the Drive Mode pull-down menu, choose your drive mode.

<!-- image -->

Table 66 - Available Drive Modes

| Mode                             | Drive Object Value   |
|----------------------------------|----------------------|
| Auto Tune                        | 0                    |
| EtherNet/IP External Reference 1 |                      |
| Master Gearing                   | 2                    |
| Step and Direction               | 3                    |
| Analog Velocity Input            | 4                    |
| Analog Current Input             | 5                    |
| Indexing                         | 6                    |

## Master Gearing Mode Examples

When using a Bulletin MPL encoder for master gearing, the Kinetix 300 planner treats the 128 and 1024 pulse encoders as having 262,144 interpolated counts per revolution for the calculation of the gearing ratios.

User units in the MotionView software, General category, is not used in Master Gearing mode, therefore any transmission ratio besides 1:1 must be configured in the master-to-system units.

## Master Gearing Example 1

A Bulletin MPL multi-turn motor is connected to the slave drive and outputs 128 pulses per revolution (ppr). A master encoder outputs 128 ppr TTL to the master gearing inputs on the Kinetix 300 slave drive. A 1:1 master encoder to motor revolution is required.

The drive interpolated counts are 262,144 counts/rev and the master encoder is 128 x 4 (512) counts/rev. The [Master] parameter is 1 and the [System] parameter is 262,144/512 or 512.

## Master Gearing Example 2

A Bulletin MPL multi-turn motor is connected to the slave drive and outputs 1024 ppr. A master encoder outputs 2048 ppr TTL to the master gearing inputs on the Kinetix 300 slave drive. A 1:1 master encoder to motor revolution is required.

The drive interpolated counts are 262,144 counts/rev and the master encoder is 2048 x 4 (8192) counts/rev. The [Master] parameter is 1 and the [System] parameter is 262,144/8192 or 32.

## Master Gearing Example 3

The same configuration as used in example 2 exists, however, the slave motor that generates the 1024 ppr is connected to a 5:1 gear box. Therefore, one revolution of the gear box requires five motor revolutions.

The drive interpolated counts are 262,144 counts/rev x 5 motor rev/1 output gear box revolution. The master encoder is 2048 x 4 (8192) counts/rev. The [Master] parameter is 1 and the [System] parameter is 262,144 x 5/8192 or 160.

## Configure Master Gearing Mode

This procedure assumes that you have configured your Kinetix 300 drive for Master Gearing mode, configured your Logix Ethernet module, and applied power to the system.

Follow these steps to configure the master gearing ratio.

1. Run the MotionView software.
2. From the Drive Organizer, click General.

## IMPORTANT

The buffered output is supported only for use with incremental encoder motor feedback. SICK-Stegmann or Tamagawa highresolution motor feedback must not be used on the master drive because they cannot generate buffered encoder output pulses. Conversely, the master gearing input supports only incremental encoder inputs.

3. Determine the ratio of buffered encoder output counts to the number of system motor counts.

See the examples on page 143 .

4. Enter the values into the Master and System ratio fields.

Use a negative value in the Master field to reverse the relative direction of the drive relative to the master.

<!-- image -->

## Configure the Drive Parameters and System Variables

This section provides information for you to access and change parameters not accessible through RSLogix 5000 software or the Studio 5000 Logix Designer application.

## Tools for Viewing Parameters

Follow these steps to view parameters.

1. From MotionView software, click Tools.
2. Click Parameter&gt;IO View.

<!-- image -->

<!-- image -->

3. Click Add to add a parameter to the viewer.
4. Select a parameter from within the tree structure.

<!-- image -->

5. Click Add.

<!-- image -->

## Tools for Changing Parameters

Some parameters are accessible through RSLogix 5000 software or the Studio 5000 Logix Designer application. The alternative is to use Explicit Messaging from the Ethernet module.

Follow these steps to change parameters by using Explicit Messaging.

1. Create a Set Attribute Single MSG instruction in the ladder logic program.
2. Use a Class value of 374 (Hex).
3. Use the ID of the parameter as listed in Appendix C as the Instance.
4. Use the Attribute value to reflect the format of the value and the nonvolatile status of the value.

<!-- image -->

| Attribute Format   |                             | Memory Stored In   |
|--------------------|-----------------------------|--------------------|
|                    | 0 32 - bit integer Volatile |                    |
| 1                  | 32-bit integer              | Nonvolatile        |
| 2                  | 32-bit floating point       | Volatile           |
| 3                  | 32-bit floating point       | Nonvolatile        |
| 4                  | String                      | Volatile           |
| 5                  | String                      | Nonvolatile        |

## Configure Drive Mode with Explicit Messaging

These Kinetix 300 drive modes can be set via explicit messaging:

- Master Gearing
- Step and Direction
- Analog Velocity
- Analog Current
- Indexing

Set the drive mode by entering the parameters from the appropriate table via EtherNet/IP Explicit Messaging or through the MotionView software. For Indexing mode, see page 99.

Table 67 - Master Gearing

| ID Parameter Name Description                                        | Value                                           |
|----------------------------------------------------------------------|-------------------------------------------------|
| 266 Drive Mode  Set to Master Gearing                                | 2                                               |
| 79 M2SRatioMaster Master to system ratio (master counts)             | Range: -32768…+32768                            |
| 80 M2SRatioSystem Master to system ratio denominator (system counts) | Range: 1…32768                                  |
| 29 EnableSwitchType Enable switch function                           | 0 = Inhibit only 1 = Enable as soon as asserted |

IMPORTANT Do not set parameter 80 to 0 or unexpected motion will occur.

## Table 68 - Step and Direction

| ID Parameter Name Description                                      | Value                                           |
|--------------------------------------------------------------------|-------------------------------------------------|
| 266 Drive Mode  Set to Step and Direction                          | 3                                               |
| 79 M2SRatioMaster Master to system ratio numerator (master counts) | Range: -32768…+32768                            |
| 29 EnableSwitchType Enable switch function                         | 0 = Inhibit only 1 = Enable as soon as asserted |

## Table 69 - Analog Velocity

| ID Parameter Name Description                                                                | Value                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 266 Drive Mode  Set to Analog Velocity                                                       | 4                                                                                                                                                                                    |
| 36 VelocityScale  Analog input velocity reference scale: Velocity = Vinput x VelocityScale   | Range: -10000…10000 rpm/V                                                                                                                                                            |
| 76 AccelLimit  Accel value for Velocity mode                                                 | Range: 0.1…5,000,000 UU/s                                                                                                                                                            |
| 77 DecelLimit  Decel value for Velocity mode                                                 | Range: 0.1…5,000,000 UU/s                                                                                                                                                            |
| 75 EnableVelAccDec Enable Accel/Decel function for Velocity mode 0 = Disable                 | 1 = Enable                                                                                                                                                                           |
| 89 AnalogInput1Deadband Analog input dead-band. Applied when used as a velocity reference.   | Range: 0…100 mV                                                                                                                                                                      |
| 90 AnalogInput1Offset Analog input offset. Applied when used as current/ velocity reference. | Range: -10.000…10.000                                                                                                                                                                |
| 85 AnalogOutFunction Analog output function                                                  | 0 = Not assigned 1 = Phase current (rms) 2 = Phase current (peak value) 3 = Motor velocity 4 = Phase current R 5 = Phase current S 6 = Phase current T 7 = Iq current 8 = Id current |
| 86 AnalogOutVelocityScale Analog output scale for velocity quantities Range: 0…10 mV/rpm     |                                                                                                                                                                                      |
| 29 EnableSwitchType Enable switch function                                                   | 0 = Inhibit only 1 = Enable as soon as asserted                                                                                                                                      |

## Table 70 - Analog Current

| ID Parameter Name Description                                                                | Value                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 266 Drive Mode  Set to Analog Current                                                        | 5                                                                                                                                                                                    |
| 35 CurrentScale  Current scale                                                               | Range: - X…+X Amps/Volt X = drive peak output current/10                                                                                                                             |
| 89 AnalogInput1Deadband Analog input dead-band. Applied when used as a velocity reference.   | Range: 0…100 mV                                                                                                                                                                      |
| 90 AnalogInput1Offset Analog input offset. Applied when used as current/ velocity reference. | Range: -10,000…10,000                                                                                                                                                                |
| 85 AnalogOutFunction Analog output function                                                  | 0 = Not assigned 1 = Phase current (rms) 2 = Phase current (peak value) 3 = Motor velocity 4 = Phase current R 5 = Phase current S 6 = Phase current T 7 = Iq current 8 = Id current |
| 87 AnalogOutCurrentScale Analog output scale for current related quantities. Range: 0…10V/A  |                                                                                                                                                                                      |
| 29 EnableSwitchType Enable switch function                                                   | 0 = Inhibit only 1 = Enable as soon as asserted                                                                                                                                      |

## Configure Drive for Linear Motors and Direct Drive Stages

Use this section to configure your Kinetix 300 drive for use with linear motor and linear stages.

## Motor Temperature Sensor

For Kinetix LDAT linear thrusters, Kinetix LDL, and Kinetix LDC linear motors and Kinetix MPAS linear stages, do the following.

1. Run MotionView software.
2. Click General Category.
3. Set Motor Temperature Sensor to Enable.

## Understanding Encoder Resolution Setting

Figure 77 shows the relationship of Resolution (x1) and Resolution (x4).

Figure 77 - Relationship between Resolution (1x) and Resolution (4x)

<!-- image -->

Here is a simple example.

EXAMPLE If Resolution (x1) = 4 µm, then Resolution (x4) = 1 µm

## Change the Encoder Resolution for an Incremental Encoder

The encoder resolution defaults to 5 μm per encoder count. If you must change the resolution, do the following.

1. Run the MotionView software.
2. From the Drive Organizer, click Motor.
3. Click Change Motor.
4. Click Custom Motor.
5. Click Create Custom.
6. Create a Vendor Name.

## EXAMPLE AB Custom

7. Create a Motor Model.

## EXAMPLE LDC-c030100DHT1u

8. Enter either the Resolution (x1) or the Resolution (x4) value.
9. Click Save File.
10. Enter &lt;filename&gt;.cmt.xml.
11. Click Update Drive.

This important message appears.

<!-- image -->

12. Answer yes or no according to your motor needs.

This important message appears.

<!-- image -->

IMPORTANT

We recommended that you do auto-phasing when you wire and commission new motors.

If you choose auto phasing, the following appears.

<!-- image -->

13. Follow the instructions in the dialog box.

If your system is wired by using one of the interconnect diagrams in Appendix A, then you get the following results.

Table 71 - Feedback Parameters

| Parameter Value      |           |
|----------------------|-----------|
| Resolution (x1)      | 20 µm     |
| Resolution (x4)      | 5 µm      |
| Halls order          | 3         |
| Inverted             | Checked   |
| B lead A for forward | Unchecked |

## Safety Precautions

<!-- image -->

## Troubleshooting the Kinetix 300 Drive System

| Topic                   |   Page |
|-------------------------|--------|
| Safety Precautions      |    153 |
| General Troubleshooting |    154 |
| Clearing Faults         |    158 |

Observe the following safety precautions when troubleshooting your Kinetix® 300 drive.

<!-- image -->

<!-- image -->

ATTENTION: DC bus capacitors can retain hazardous voltages after input power has been removed. Before working on the drive, measure the DC bus voltage to verify it has reached a safe level or wait the full time interval that is listed on the drive warning label. Failure to observe this precaution could result in severe bodily injury or loss of life.

Do not attempt to defeat or override the drive fault circuits. You must determine the cause of a fault and correct it before you attempt to operate the system. If you do not correct a drive or system malfunction, it could result in personal injury and/or damage to the equipment as a result of uncontrolled machine system operation.

Test equipment (such as an oscilloscope or chart recorder) must be properly grounded. Failure to include an earth ground connection could result in a potentially fatal voltage on the oscilloscope chassis.

SHOCK HAZARD: Capacitors retain charge for approximately 300 s after power is removed. Disconnect incoming power and wait at least 5 minutes before touching the drive. Failure to observe this precaution could result in severe bodily injury or loss of life.

RISQUE DE CHOC: Les condensateurs restent sous charge pendant environ 300 secondes après une coupure de courant. Couper l'alimentation et patienter pendant au moins 5 minutes avant de toucher l'entraînement. Le non-respect de cette précaution peut entraîner des blessures corporelles graves ou la mort.

## General Troubleshooting

<!-- image -->

WARNING: The opening of a branch circuit protective device can be an indication that a fault has been interrupted. To reduce the risk of fire or electric shock, parts that carry current and other components of the controller must be examined and replaced if damaged.

AVERTISSEMENT: Le déclenchement du dispositif de protection du circuit de dérivation peut être dû à une coupure qui résulte d'un courant de défaut. Pour limiter le risque d'incendie ou de choc électrique, examiner les pièces porteuses de courant et les autres éléments du contrôleur et les remplacer s'ils sont endommagés. En cas de grillage de l'élément traverse par le courant dans un relais de surcharge, le relais tout entier doit être remplacé.

See Error Codes on page 155 to identify anomalies, potential causes, and appropriate actions to resolve the anomalies. If anomalies persist after attempting to troubleshoot the system, contact your Allen-Bradley® representative for further assistance. To determine if your Kinetix 300 drive has an error, see Table 72 on page 155 .

## Display Behavior

By default, if there is no activity on the input keypad for 30 seconds, the Kinetix® 300 drive continuously scrolls the drives' IP address.

Upon powerup, the display shows its status: diS (disabled) or run (enabled), then after 30 seconds, the drive alternately scrolls the drives' IP address along with its status.

If the Kinetix 300 drive is faulted, the drive displays the fault code (nonscrolling). Then after 30 seconds, the drive alternately scrolls the drives' IP address along with its fault code.

Table 72 - Error Codes

| Error Code Anomaly                                                             | Possible Cause                                                                                                                                                                                                                           | Action/Solution                                                                                                                                                                          |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| –  Status indicator not displaying any messages. No AC power or back-up power. |                                                                                                                                                                                                                                          | Verify AC power or back-up power is applied to the Kinetix 300 drive.                                                                                                                    |
| –  Status indicator not displaying any messages. No AC power or back-up power. | Internal power supply malfunction.                                                                                                                                                                                                       | Call your Allen-Bradley representative.                                                                                                                                                  |
| –  Motor jumps when first enabled.                                             | Motor wiring error.                                                                                                                                                                                                                      | Check motor wiring.                                                                                                                                                                      |
| –  Motor jumps when first enabled.                                             | Incorrect motor chosen.                                                                                                                                                                                                                  | Verify that the proper motor is selected.                                                                                                                                                |
| E04 Motor overtemperature.                                                     | Motor thermostat trips due to: • High motor ambient temperature. • Excessive current.                                                                                                                                                    | • Operate within (not above) the continuous torque rating for the ambient temperature 40 °C (104 °F) maximum). • Lower ambient temperature, increase motor cooling.                      |
| E04 Motor overtemperature.                                                     | Motor wiring error.                                                                                                                                                                                                                      | Check motor wiring.                                                                                                                                                                      |
| E04 Motor overtemperature.                                                     | Incorrect motor selection.                                                                                                                                                                                                               | Verify that the proper motor has been selected.                                                                                                                                          |
| E06 Hardware overtravel.                                                       | Dedicated overtravel input is inactive.                                                                                                                                                                                                  | • Check wiring. • Verify motion profile.                                                                                                                                                 |
| E07 Feedback lost.                                                             | The feedback wiring is open, shorted, or missing. • Check motor encoder wiring.                                                                                                                                                          | • Make sure that the motor is recognized from drive's Web-based configuration motor screen.                                                                                              |
| E09 Bus undervoltage.                                                          | Low AC line/AC power input.                                                                                                                                                                                                              | • Verify voltage level of the incoming AC power. • Check AC power source for glitches or line drop. • Install an uninterruptible power supply (UPS) on your AC input.                    |
| E10 Bus overvoltage.                                                           | Excessive regeneration of power. When the motor is driven by an external mechanical power source, it may regenerate too much peak energy through the Kinetix 300 drives power supply. The system faults to save itself from an overload. | • Change the deceleration or motion profile. • Use a larger system (motor and Kinetix 300 drive). • Use a resistive shunt. • If a shunt is connected, verify that the wiring is correct. |
| E10 Bus overvoltage.                                                           | Excessive AC input voltage.                                                                                                                                                                                                              | Verify that input is within specifications.                                                                                                                                              |
| E11 Illegal Hall state.                                                        | Incorrect phasing.                                                                                                                                                                                                                       | Check the Hall phasing.                                                                                                                                                                  |
| E11 Illegal Hall state.                                                        | Bad connections.                                                                                                                                                                                                                         | • Verify the Hall wiring. • Verify 5V power supply to the encoder.                                                                                                                       |
| E12 Home search failed.                                                        | Home sensor and/or marker is outside the overtravel limits.                                                                                                                                                                              | • Check wiring. • Reposition the overtravel limits or sensor.                                                                                                                            |
| E14 Ethernet I/O connection lost.                                              | Ethernet I/O Connection lost.                                                                                                                                                                                                            | Check wiring and Ethernet cables and routing. Check controller program to be sure that I/O is scanned at correct RPI rate.                                                               |
| E16 Software overtravel.                                                       | Programmed overtravel limit has been exceeded. • Verify motion profile.                                                                                                                                                                  | • Verify that overtravel settings are appropriate.                                                                                                                                       |
| E18 Overspeed fault.                                                           | Motor speed has exceeded 125% of maximum rated speed.                                                                                                                                                                                    | • Check cables for noise. • Check tuning.                                                                                                                                                |
| E19 Excess position error.                                                     | Position error limit was exceeded.                                                                                                                                                                                                       | • Increase following error limit or time. • Check position loop tuning.                                                                                                                  |

## Error Codes

The following list is designed to help you resolve anomalies.

When a fault is detected, the status indicator displays an E and a two-digit error code until the anomaly is cleared.

## Table 72 - Error Codes (Continued)

| Error Code Anomaly                                                                                         | Possible Cause                                                                                              | Action/Solution                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E23 Drive Thermal Protection                                                                               | The internal filter algorithm protecting the drive from overheating has tripped.                            | • Reduce acceleration rates. • Reduce duty cycle (ON/OFF) of commanded motion. • Increase time permitted for motion. • Use larger Kinetix 300 drive and motor. • Check tuning.                                                                                                   |
| E26 Index parameter out of range.                                                                          | Parameters that are specified in the index table are beyond system capabilities.                            | Verify index parameters, such as position and velocity.                                                                                                                                                                                                                          |
| E27 Absolute move fault                                                                                    | Initiated move without being homed.                                                                         | When using an absolute encoder home the axis before attempting an absolute move.                                                                                                                                                                                                 |
| E30 Encoder communication fault.                                                                           | Communication was not established with an intelligent encoder.                                              | • Verify motor selection. • Verify that the motor supports automatic identification. • Verify motor encoder wiring.                                                                                                                                                              |
| E31 Encoder data.                                                                                          | Encoder data is corrupted.                                                                                  | Replace the motor/encoder.                                                                                                                                                                                                                                                       |
| E39 Safe Torque Off while enabled.                                                                         | The safety circuit was opened while drive was enabled or while attempting to enable.                        | Check safety circuit.                                                                                                                                                                                                                                                            |
| E43 Drive enable input.                                                                                    | An attempt was made to enable the axis through software while the Drive Enable hardware input was inactive. | Verify that Drive Enable hardware input is active whenever the drive is enabled through software.                                                                                                                                                                                |
| E43 Drive enable input.                                                                                    | The Drive Enable input that is transitioned from active to inactive while the axis was enabled.             | Verify that Drive Enable hardware input is active whenever the drive is enabled through software.                                                                                                                                                                                |
| E44 Controller changed to PROG mode.                                                                       | Program downloaded or turned key on logix controller to program position.                                   | Place controller back in RUN mode, clear faults.                                                                                                                                                                                                                                 |
| E67 Operating system failed.                                                                               | Hardware or configuration failure.                                                                          | • Cycle power. • Check configuration settings to be sure that drive tags setting are valid. • Check your program to ensure that there are not explicit messages to internal drive variables that have been noted as unpublished or reserved.                                     |
| E70 Memory module error.                                                                                   | Bad memory module                                                                                           | Replace memory module                                                                                                                                                                                                                                                            |
| E72 Drive temperature too high. The heatsink temperature sensor has detected an overtemperature condition. | Improper airflow/environmental temperature exceeds specifications or an application anomaly.                | Check for clogged vents or defective fan. Make sure that cooling is not restricted by insufficient space around the unit. Check ambient temperature in enclosure. Reduce acceleration rates. Reduce duty cycle (ON/OFF) of commanded motion. Increase time permitted for motion. |
| E74 Drive has exceeded peak current limit. Drive cannot regulate current properly.                         | Motor cables shorted.                                                                                       | Verify continuity of motor power cables and connector.                                                                                                                                                                                                                           |
| E74 Drive has exceeded peak current limit. Drive cannot regulate current properly.                         | Motor winding shorted internally.                                                                           | Disconnect motor power cables form the motor. If the motor is difficult to turn by hand, it must be replaced.                                                                                                                                                                    |
| E74 Drive has exceeded peak current limit. Drive cannot regulate current properly.                         | The machine duty cycle requires an RMS current exceeding the continuous rating of the controller.           | Change the command profile to reduce speed or increase time.                                                                                                                                                                                                                     |
| E74 Drive has exceeded peak current limit. Drive cannot regulate current properly.                         | Operation above continuous power rating and/or product environmental rating.                                | Verify ambient temperature is not too high. Operate within the continuous power rating. Reduces acceleration rates.                                                                                                                                                              |
| E74 Drive has exceeded peak current limit. Drive cannot regulate current properly.                         | The Kinetix 300 drive has a short circuit overcurrent, or failed component.                                 | Remove all power and motor connections and preform a continuity check form the DC bus to the U, V, and W motor outputs. If a continuity exists, check for wire fibers between terminal or send drive in for repair.                                                              |

## Table 72 - Error Codes (Continued)

| Error Code Anomaly                                                                                | Possible Cause                                                                                                                                                                              | Action/Solution                                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E76 Blank memory module.                                                                          | A Blank MEM module has been inserted into the drive.                                                                                                                                        | Push and hold the drive's enter key (bottom most red button) on the drive's front display until the drive shows "bUSY". This makes the drive format the blank memory module for usage with the drive.                     |
| E91 User watchdog has timed out.                                                                  | Ladder program error.                                                                                                                                                                       | • Not writing to WatchDogKick Tag frequently enough to help prevent timeout. • Watchdog timeout period set to too low a value. Increase timeout period or change controller application to kick watchdog more frequently. |
| E92 Bad battery.                                                                                  | • Tamagawa absolute feedback battery voltage low or missing. • A battery error is set at drive powerup when main power to the encoder is not present or the battery voltage is below 2.75V. | Replace battery.                                                                                                                                                                                                          |
| E93 Motion set-up parameters calculate an acceleration value above or below the drive capability. |                                                                                                                                                                                             | Check indexing profiles or motion set-up profiles. Increase or decrease acceleration profile. Increase or decrease permitted time for motion.                                                                             |
| E94 Motor or motor feedback cable.                                                                |                                                                                                                                                                                             | Motor or feedback device malfunction. • Check motor power/feedback wiring. • Replace motor or encoder.                                                                                                                    |
| E94 Motor or motor feedback cable.                                                                | Recommenced grounding, per installation instructions, has not been followed.                                                                                                                | • Verify grounding. • Route feedback cables away from noise sources. • See System Design for Control of Electric Noise Reference Manual, publication GMC-RM001 .                                                          |
| E95 Wrong Indexing Mode                                                                           | Index Type or ReferenceSource not supported in configured Linear/Rotary Unwind mode.                                                                                                        | • Change the Index Type or ReferenceSource to values that are supported by selecting Linear or Rotary Unwind mode                                                                                                         |

## Clearing Faults

This section provides methods for clear faults in the Kinetix 300 drive. You can clear drive faults by using digital inputs or drive parameters.

## Use Digital Inputs to Clear Faults

You can use MotionView software to clear faults by configuring a digital input as Fault Reset. To clear faults by using this input, you must make the input active until the fault clears and then deactivate it.

## Use Drive Parameters to Clear Faults

You can use the Kinetix 300 drive parameter to reset faults by using Explicit Messaging or UserDefinedDataLink.

## Explicit Messaging

Send Explicit Messages from within the RSLogix 5000® software or the Studio 5000 Logix Designer® application to Class 374 (hex) Instance 53, Attribute 0 to set it to a 1 and then back to a 0 when the fault is cleared.

<!-- image -->

## UserDefinedDataLink

Drive parameters that are used in the Explicit Messaging section can be mapped into the integer UserDefinedDataLink by using MotionView software. Then the parameter can be toggled by using the UserDefinedIntegerData0 or UserDefinedIntegerData1 tags within RSLogix 5000 software or the Logix Designer application.

Figure 78 - UserDefinedDataLink Example Using Parameter 53

<!-- image -->

## Drive Enable

The drive clears runtime faults if the drive enable command from RSLogix 5000 software or the Logix Designer application is cycled and the fault reset in the MotionView software is configured for On Disable. For the drive to be enabled, the DriveEn bit in the Output Assembly must be set to 1. By changing that from 1 back to 0, the fault clears as the drive disables.

## Notes:

## Certification

<!-- image -->

## Kinetix 300 Drive Safe Torque Off Feature

This appendix introduces you to how the Safe Torque Off feature meets the requirements for ISO 13849-1 Performance Level d (PLd) safety category 3.

| Topic                                             |   Page |
|---------------------------------------------------|--------|
| Certification                                     |    161 |
| Description of Operation                          |    163 |
| Functional Proof Tests                            |    163 |
| PFD and PFH Definitions                           |    164 |
| PFD and PFH Data                                  |    164 |
| Safe Torque Off Connector Data                    |    165 |
| Wiring Your Safe Torque Off Circuit               |    166 |
| Kinetix 300 Drive Safe Torque Off Feature         |    168 |
| Kinetix 300 Drive Safe Torque Off Wiring Diagrams |    169 |
| Safe Torque Off Signal Specifications             |    170 |

The Safe Torque Off circuit is type-approved and certified for use in safety applications up to and Performance Level d (PLd) safety category 3.

The TÜV Rheinland group has approved the Kinetix® 300 drives for use in safety-related Performance Level d (PLd) safety category 3, in which the deenergized state is considered to be the safe state. All safe state for typical machine safety systems.

## Important Safety Considerations

You are responsible for the following:

- Validation of any sensors or actuators that are connected to the drive system
- Completing a machine-level risk assessment
- Certification of the machine to the desired EN ISO 13849-1 Performance Level
- Project management and proof testing
- Programming the application software and the device configurations in accordance with the information in this safety reference manual and the drive product manual

## Safety Category 3 Requirements

Safety-related parts are designed with these attributes:

- A fault in any of these parts does not lead to the loss of the safety function
- A fault is detected whenever reasonably practicable
- Accumulation of undetected faults can lead to the loss of the safety function, which results in an uncontrolled coast-to-stop

## Stop Category Definition

Stop category 0 is achieved with immediate removal of power to the actuator.

| IMPORTANT   | If there is a drive or control failure, the most likely stop category is category 0. When designing the machine application, timing and distance should be considered for a coast-to-stop. For more information regarding stop categories, see EN 60204-1.   |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Performance Level and Safety Integrity Level (SIL) CL3

For safety-related control systems, Performance Level (PL), according to EN ISO 13849-1, and SIL levels, according to EN 61508 and EN 62061, include a rating of the systems ability to perform its safety functions. All safetyrelated components of the control system must be included in both a risk assessment and the determination of the achieved levels.

See the EN ISO 13849-1, EN 61508, and EN 62061 standards for complete information on requirements for PL and SIL determination.

## Description of Operation

## Functional Proof Tests

The Safe Torque Off feature provides a method, with sufficiently low probability of a dangerous failure on demand, to force the power-transistor control signals to a disabled state. When disabled, or any time power is removed from theallall of the drives output-power transistors are released from the ON state, effectively removing motive power generated by the drive. This results in a condition where the motor is in a coasting condition (stop category 0). Disabling the power transistor output does not provide mechanical isolation of the electrical output, which may be required for some applications.

Under normal drive operation, the Safe Torque Off switches are energized. If either of the safety enable inputs are de-energized, the gate control circuit is disabled. To meet EN ISO 13849-1 (PLd) both safety channels must be used and monitored.

<!-- image -->

ATTENTION: Permanent magnet motors may, in the event of two simultaneous faults in the IGBT circuit, result in a rotation of up to 180 electrical degrees.

The functional safety standards require that functional proof tests be performed on the equipment that is used in the system. Proof tests are performed at user-defined intervals, not to exceed one year, and are dependent upon PFD and PFH values.

## IMPORTANT

Your specific application determines the time frame for the proof test interval, but it must not exceed one year due to the use of switches internal to the drive, as required by EN ISO 13849-1.

To proof test the Safe Torque Off function, you must interrupt power to the inputs of the Safe Torque Off function at pins STO-4 and STO-6 and verify that the drive is in the disabled state.

Table 73 - Proof Test Truth Table

| Safety Function State Safety Input 1 (STO-4)                  | Safety Input 2 (STO-6) Safety Status Output (STO-3) Drive Status Indication(1)   |
|---------------------------------------------------------------|----------------------------------------------------------------------------------|
| Normal operation Energized Energized Energized Run            |                                                                                  |
| Safe Torque Off mismatch Energized De-energized Energized E39 |                                                                                  |
|                                                               | De-energized Energized Energized E39                                             |
| Safe Torque Off function engaged                              | De-energized De-energized De-energized E39                                       |

Normal operation of the Safe Torque Off function, if monitored and verified, constitutes the proof test. A Safe Torque Off mismatch results in error code E39.

## PFD and PFH Definitions

## PFD and PFH Data

## Troubleshooting the Safe Torque Off Function

| Error Code   | Fault Message RSLogix (HIM)             |                                                                 |                                                                                                                                                                      | Anomaly Potential Cause Possible Resolution                                                                                                                     |
|--------------|-----------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E39          | DriveHardFault (Safe Torque Off HW Flt) | Safe Torque Off function mismatch. Drive will not allow motion. | • Loose wiring at Safe Torque Off (STO) connector. • Cable/header not seated properly in Safe Torque Off (STO) connector. • Safe Torque Off circuit missing +24V DC. | • Verify wire terminations, cable/header connections, and +24V. • Reset error and run proof test. • If error persists, return the drive to Rockwell Automation. |

<!-- image -->

ATTENTION: The Safe Torque Off fault (E39) is detected upon demand of the Safe Torque Off function. After troubleshooting, a proof test must be performed to verify correct operation.

Safety-related systems can be classified as operating in either a Low Demand mode, or in a High Demand/Continuous mode:

- Low Demand mode: where the frequency of demands for operation made on a safety-related system is no greater than one per year or no greater than twice the proof test frequency.
- High Demand/Continuous mode: where the frequency of demands for operation made on a safety-related system is greater than once per year or greater than twice the proof test interval.

The SIL value for a low demand safety-related system is directly related to order-of-magnitude ranges of its average probability of failure to satisfactorily perform its safety function on demand or, simply, average probability of a dangerous failure on demand (PFD). The SIL value for a High Demand/ Continuous mode safety-related system is directly related to the probability of a dangerous failure occurring per hour (PFH).

These PFD and PFH calculations are based on the equations from EN 61508 and show worst-case values.

This table provides data for a 20-year proof test interval and demonstrates the worst-case effect of various configuration changes on the data.

Table 74 - PFD and PFH for 20-year Proof Test Interval

| Attribute   |   Value |
|-------------|---------|
| PFH [1e-9]  |     5.9 |
| PFD [1e-3]  |     1   |

## Safe Torque Off Connector Data

This section provides Safe Torque Off (STO) connector and header information for the Kinetix 300 drive Safe Torque Off.

## STO Connector Pinouts

Headers extend the STO connector signals for use in wiring or to defeat (not use) the Safe Torque Off function.

Figure 79 - Safe Torque Off (STO) Connector

<!-- image -->

| STO Pin Description                  | Signal          |
|--------------------------------------|-----------------|
| 1 +24V DC output from the drive      | +24V DC control |
| 2 +24V DC output common              | Control COM     |
| 3 Safety status                      | Safety Status   |
| 4 Safety input 1 (+24V DC to enable) | Safety Input 1  |
| 5 Safety common                      | Safety COM      |
| 6 Safety input 2 (+24V DC to enable) | Safety Input 2  |

## Wiring Your Safe Torque Off Circuit

This section provides guidelines for wiring your Kinetix 300 Safe Torque Off drive connections.

## European Union Directives

If this product is installed within the European Union or EEC regions and has the CE mark, the following regulations apply.

For more information on the concept of electrical noise reduction, see System Design for Control of Electrical Noise Reference Manual, publication GMC-RM001 .

## EMC Directive

This unit is tested to meet Council Directive 2014/30/EU Electromagnetic Compatibility (EMC) by using these standards, in whole or in part:

- EN 61800-3 - Adjustable Speed Electrical Power Drive Systems, Part 3 - EMC Product Standard including specific test methods
- EN 61000-6-4 EMC - Emission Standard, Part 2 - Industrial Environment
- EN 61000-6-2 EMC - Immunity Standard, Part 2 - Industrial Environment

The product that is described in this manual is intended for use in an industrial environment.

## CE Conformity

Conformity with the Low Voltage Directive and Electromagnetic Compatibility (EMC) Directive is demonstrated by using harmonized European Norm (EN) standards published in the Official Journal of the European Communities. The safe torque-off circuit complies with the EN standards when installed according instructions found in this manual.

CE Declarations of Conformity are available online at: rok.auto/certifications .

## Low Voltage Directive

These units are tested to meet Council Directive 2014/35/EU Low Voltage Directive. The EN 60204-1 Safety of Machinery-Electrical Equipment of Machines, Part 1-Specification for General Requirements standard applies in whole or in part.

## Safe Torque Off Wiring Requirements

These are the Safe Torque Off (STO) wiring requirements. Wire should be copper with 75 °C (167 °F) minimum rating.

IMPORTANT

The National Electrical Code and local electrical codes take precedence over the values and methods provided.

## IMPORTANT

Stranded wires must terminate with ferrules to help prevent short circuits, per table D7 of EN 13849.

Figure 80 - Safe Torque Off (STO) Terminal Plug

<!-- image -->

Table 75 - Safe Torque Off (STO) Terminal Plug Wiring

| Safe Torque Off (STO) Connector     | Safe Torque Off (STO) Connector                                                    | Recommended Wire Size                 | Recommended Wire Size   | Strip Length mm (in.)   | Torque Value N•m (lb•in)   |
|-------------------------------------|------------------------------------------------------------------------------------|---------------------------------------|-------------------------|-------------------------|----------------------------|
| Pin                                 | Signal                                                                             | Stranded Wire with Ferrule mm 2 (AWG) | Solid Wire mm 2  (AWG)  |                         |                            |
| STO-1 STO-2 STO-3 STO-4 STO-5 STO-6 | +24V DC Control Control COM Safety Status Safety Input 1 Safety COM Safety Input 2 | 0.75 (18)                             | 1.5 (16)                | 6 (0.25)                | 0.2 (1.8)                  |

## IMPORTANT

## IMPORTANT

Pins STO-1 (+24V DC Control) and STO-2 (Control COM) are used only by the motion-allowed jumpers to defeat the Safe Torque Off function. When the Safe Torque Off function is in operation, the 24V supply must come from an external source.

To be sure of system performance, run wires and cables in the wireways as established in the user manual for your drive.

## Kinetix 300 Drive Safe Torque Off Feature

The Safe Torque Off circuit, when used with suitable safety components, provides protection according to EN ISO 13849-1 (PLd). The Safe Torque Off option is just one safety control system. All components in the system must be chosen and applied correctly to achieve the desired level of operator safeguarding.

The Safe Torque Off circuit is designed to safely remove power from the gate firing circuits of the drives output power devices (IGBTs). This helps prevent them from switching in the pattern necessary to generate AC power to the motor.

You can use the Safe Torque Off circuit in combination with other safety devices to meet the stop and protection-against-restart requirements of EN ISO 13849-1.

<!-- image -->

ATTENTION: This option is suitable for performing mechanical work on the drive system or affected area of a machine only. It does not provide electrical safety.

<!-- image -->

SHOCK HAZARD: In Safe Torque Off mode, hazardous voltages may still be present at the motor. To avoid an electric shock hazard, disconnect power to the motor and verify that the voltage is zero before performing any work on the motor.

## Safe Torque Off Feature Bypass

The drive is supplied from the factory with the Safe Torque Off circuit enabled. The drive is not operational until +24V is present at terminals STO-4 and STO-6. When safety connections are not required, the drive can be operated with the safety circuit disabled.

Use jumper wires, as shown, to defeat the Safe Torque Off function.

Figure 81 - STO Motion-allowed Jumpers

<!-- image -->

## IMPORTANT

Pins STO-1 (+24V DC Control) and STO-2 (Control COM) are used only by the motion-allowed jumpers to defeat the Safe Torque Off function. When the Safe Torque Off function is in operation, the 24V supply must come from an external source.

## Kinetix 300 Drive Safe Torque Off Wiring Diagrams

This section provides typical wiring diagrams for the Kinetix 300 drive Safe Torque Off feature with other Allen-Bradley safety products.

For additional information regarding Allen-Bradley® safety products, including safety relays, light curtain, and gate interlock applications, see the Safety Products website https://www.rockwellautomation.com/en-us/products/ hardware/allen-bradley/safety-products.html .

The drive is shown in a single-axis relay configuration for both category 0 and category 1 stops per EN-60204-1 Safety of Machinery Directive. These are examples, however, and user applications can differ based on the required overall machine Performance Level requirements.

## IMPORTANT

The Kinetix 300 drive has been qualified and rated as a component to meet EN ISO 13849-1 Performance Level d (PLd), safety-level category 3. Dual inputs and drive monitoring of the Safe Torque Off circuit, STO-4 and ST0-6, are done to help prevent drive enable should either or both of these inputs not function.

It is suggested to evaluate the entire machine Performance Level required with a risk assessment and circuit analysis. Contact your local distributor or Rockwell Automation Sales for more information.

Figure 82 - Single-axis Relay Configuration (Stop Category 0) with Automatic Reset

<!-- image -->

Pins 1 and 2 are not used when using Safety Inputs. Pin 3 is a sinking output.

## Safe Torque Off Signal Specifications

Figure 83 - Single-axis Relay Configuration (Stop Category 1) with Automatic Reset

<!-- image -->

Pins 1 and 2 are not used when using Safety Inputs. Pin 3 is a sinking output.

- (1) The digital input, which is configured for Abort Index in MotionView software, must be active-high when the safety function is requested, so an interposing relay may be required to invert the signal. Digital input common (IN\_x\_COM) must be used in this signal activation/de-activation transition.

You can also bring this input into a PLC where you can use an AOP (add on profile) or assembly object to activate the recommended digital input (abort index).

This table provides specifications for the Safe Torque Off signals that are used in the Kinetix 300 servo drives.

| Attribute                          | Value                                                    |
|------------------------------------|----------------------------------------------------------|
| Safety inputs  (1)                 | Insulated, compatible with single-ended output (+24V DC) |
| Safety inputs  (1)                 | Enable voltage range: 20…24V DC                          |
| Safety inputs  (1)                 | Disable voltage range: 0…1.0V DC                         |
| Input impedance 6.8 k             |                                                          |
| Safety status                      | Isolated Open Collector (Emitter is grounded.)           |
| Output load capability             | 100 mA                                                   |
| Digital outputs max voltage 30V DC |                                                          |

## Safety Input and Output Schematics

The following are generic safety input and output schematics for the Kinetix 300 drive.

Figure 84 - Safety Input

<!-- image -->

Figure 85 - Safety Status Output - Sinking Type

<!-- image -->

## Notes:

## Interconnect Diagrams

| Topic                                                      |   Page |
|------------------------------------------------------------|--------|
| Interconnect Diagram Notes                                 |    174 |
| Power Wiring Examples                                      |    175 |
| Kinetix 300 Drive/Rotary Motor Wiring Examples             |    178 |
| Kinetix 300 Drive/Actuator Wiring Examples                 |    183 |
| Kinetix 300 Drive/Linear Motor Wiring Examples             |    181 |
| Kinetix 300 Drive to MicroLogix Controller Wiring Examples |    186 |
| Kinetix 300 Drive Master Gearing Wiring Example            |    187 |
| Motor Brake Currents                                       |    188 |
| System Block Diagrams                                      |    189 |

<!-- image -->

## Interconnect Diagram Notes

This appendix provides wiring examples to assist you in wiring the Kinetix® 300 system. The notes in this table apply to the wiring examples on the pages that follow.

| Note Information                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1 For power wiring specifications, see Power Wiring Requirements on page 63 .                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 2 For input fuse and circuit breaker sizes, see Circuit Breaker/Fuse Selection on page 17 .                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 3 Place the AC (EMC) line filters as close to the drive as possible and do not route very dirty wires in the wireway. If routing in a wireway is unavoidable, use shielded cable with shields that are grounded to the drive chassis and filter case. For AC line filter specifications, see the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005. This filter does not apply to 2097-V32PRx drives because they have integrated AC line filters. |
| 4 Terminal block is required to make connections. Configure one pair from the Digital OUT-1… OUT-4, pins 43…50, as Brake in MotionView software. For Digital Output specifications, see Digital Outputs on page 42 .                                                                                                                                                                                                                                                                                                 |
| 5 Contactor coil (M1) needs integrated surge suppressors for AC coil operation. See the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005 .                                                                                                                                                                                                                                                                                                        |
| 6 See the Motor Brake Currents table on page 188 to size the interposing relay for your application.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 7 Drive Enable input must be opened when main power is removed, or a drive fault occurs. A delay of at least 1.0 second must be observed before attempting to enable the drive after main power is restored.                                                                                                                                                                                                                                                                                                         |
| 8 Cable shield clamp must be used to meet CE requirements. No external connection to ground is required.                                                                                                                                                                                                                                                                                                                                                                                                             |
| 9 For motor cable specifications, see the Kinetix Motion Control Selection Guide, publication KNX-SG001 .                                                                                                                                                                                                                                                                                                                                                                                                            |
| 10 Motor power cables (2090-XXNPMF-xxSxx and 2090-CPBM6DF-16AAxx) have a drain wire that must be folded back under the cable shield clamp.                                                                                                                                                                                                                                                                                                                                                                           |
| 11 MPL-Axxx and MPL-B15xxx-H…MPL-B45xxx-H, MPM-Axxx, MPF-Axxx, MPS-Axxx, LDAT-Sxxxxxx-xBx, MPAR-Axxx, MPAI-Axxx, MPAS-Axxx, and MPAS-Bxxx (direct drive) encoders use the +5V DC supply.                                                                                                                                                                                                                                                                                                                             |
| 12 MPL-B15xxx-S/M…MPL-B45xxx-S/M, MPM-Bxxx, MPF-Bxxx, MPS-Bxxx, LDAT-Sxxxxxx-xDx, MPAR-Bxxx, MPAI-Bxxx, and MPAS-Bxxx (ballscrew) encoders use the +9V DC supply.                                                                                                                                                                                                                                                                                                                                                    |
| 13 Brake connector pins are labeled plus (+) and minus (-) or F and G respectively. Power connector pins are labeled U, V, W, and GND or A, B, C, and D respectively.                                                                                                                                                                                                                                                                                                                                                |
| 14 Kinetix LDAT linear thrusters do not have a brake option, so only the 2090-CPWM7DF-xxAAxx or 2090-CPWM7DF-xxAFxx motor power cables apply.                                                                                                                                                                                                                                                                                                                                                                        |

## Power Wiring Examples

You must supply input power components. The single-phase and three-phase line filters are wired downstream of fusing and the M1 contactor.

In this example, the 2097-V31PRx drives are wired to use the voltage doubling circuit. The 120V input voltage provides 240V output to motors. The 2097-V33PRx drives are wired for single-phase 120V operation.

Figure 86 - Kinetix 300 Drive (120V Single-phase Input Power)

<!-- image -->

In this example, single-phase 240V AC is applied to 2097-V31PRx and 2097-V32PRx drives.

## IMPORTANT

The 2097-V32PRx models have integrated AC line filters and do not require the AC line filter that is shown in this diagram.

Figure 87 - Kinetix 300 Drives (240V Single-phase Input Power)

<!-- image -->

In this example, three-phase 240V AC is applied to 2097-V33PRx drives and 480V AC is applied to 2097-V34PRx drives.

Figure 88 - Kinetix 300 Drive (240/480V Three-phase Input Power)

<!-- image -->

## IMPORTANT

For the 480V Kinetix 300 drives to meet EN ISO 13849-1 (PLd) spacing requirements, each phase voltage to ground must be less than or equal to 300V AC rms. To meet the requirement, the power system must use center grounded wye secondary configuration for 400/480V AC mains.

## Shunt-Resistor Wiring Example

See the the Kinetix 3, 300, 350, 2000, 6000, 6200, 6500, 7000 Servo Drives Specifications Technical Data, publication KNX-TD005, for the Bulletin 2097-Rx shunt resistors available for the Kinetix 300 drives. See the Kinetix 300 Shunt Resistor Installation Instructions, publication 2097-IN002, for more installation information.

Figure 89 - Shunt-Resistor Wiring Example

<!-- image -->

## Kinetix 300 Drive/Rotary Motor Wiring Examples

These wiring diagrams apply to Kinetix 300 drives with compatible rotary motors.

## IMPORTANT

The Kinetix MP motor wiring examples on this page apply to motors equipped with circular DIN (threaded) connectors.

Figure 90 - Kinetix MP (MPL-A/B and MPS-A/B) Motors

<!-- image -->

## IMPORTANT

The Kinetix MP motor wiring examples on this page apply to motors equipped with circular DIN (SpeedTec) connectors.

Figure 91 - Kinetix MP (MPL-A/B, MPM-A/B, MPF-A/B, and MPS-A/B) Motors

<!-- image -->

Figure 92 - Kinetix 300 Drive with Kinetix TL (TLY-A) Motors

<!-- image -->

## Kinetix 300 Drive/Linear Motor Wiring Examples

These wiring diagrams apply to Kinetix 300 drives with compatible linear motors.

Figure 93 - Kinetix 300 Drive with Kinetix LDC and Kinetix LDL Linear Motors

<!-- image -->

## Grounding Technique for Feedback Cable Shield

<!-- image -->

TTL Encoder

<!-- image -->

## Kinetix 300 Drive/Actuator Wiring Examples

These wiring diagrams apply to Kinetix 300 drives with compatible linear actuators.

Figure 94 - Kinetix 300 Drive with Kinetix MP (MPAS) Linear Stages and Kinetix LDAT Linear Thrusters

<!-- image -->

24V DC

24V DC COM

User Supplied

24V DC

<!-- image -->

Figure 95 - Kinetix 300 Drive with Kinetix MP (MPAR and MPAI) Electric Cylinders

<!-- image -->

Table 76 - Kinetix MP Electric Cylinder Power and Feedback Cables

| Kinetix MP Electric Cylinder Cat. No.        | Frame   | Power Cable Cat. No.                                                 | Feedback Cable Cat. No.                                              |
|----------------------------------------------|---------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| MPAR-A/B1xxx (series A) 32 2090-XXNPMF-16Sxx |         | (standard) 2090-CPxM4DF-16AFxx (continuous-flex)                     | 2090-XXNFMF-Sxx (standard) 2090-CFBM4DF-CDAFxx (continuous-flex)     |
| MPAR-A/B2xxx (series A) 40                   |         | (standard) 2090-CPxM4DF-16AFxx (continuous-flex)                     | 2090-XXNFMF-Sxx (standard) 2090-CFBM4DF-CDAFxx (continuous-flex)     |
| MPAR-A/B1xxx (series B) 32                   |         | 2090-CPxM7DF-16AAxx (standard) 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAR-A/B2xxx (series B) 40                   |         | 2090-CPxM7DF-16AAxx (standard) 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAR-A/B3xxx                                 | 63      | 2090-CPxM7DF-16AAxx (standard) 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/B2xxxx                                | 64      | 2090-CPxM7DF-16AAxx (standard) 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/B3xxxx                                | 83      | 2090-CPxM7DF-16AAxx (standard) 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A/B4xxxx                                | 110     | 2090-CPxM7DF-16AAxx (standard) 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-B5xxxx                                  | 144     | 2090-CPxM7DF-16AAxx (standard) 2090-CPxM7DF-16AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) 2090-CFBM7DF-CEAFxx (continuous-flex) |
| MPAI-A5xxxx                                  | 144     | 2090-CPxM7DF-14AAxx (standard) 2090-CPxM7DF-14AFxx (continuous-flex) | 2090-CFBM7DF-CEAAxx (standard) 2090-CFBM7DF-CEAFxx (continuous-flex) |

Figure 96 - Kinetix 300 Drive with Kinetix TL (TLAR) Electric Cylinders

<!-- image -->

## Kinetix 300 Drive to MicroLogix Controller Wiring Examples

The Kinetix 300 drive accepts unipolar or bipolar inputs.

Figure 97 - Analog Velocity (or Current) Control Mode

<!-- image -->

Use twisted pair shielded cables for analog signals. Route analog signals in clean wireways away from motor power cables.

Figure 98 - Step and Direction

<!-- image -->

## Kinetix 300 Drive Master Gearing Wiring Example

A master drive that powers a motor with a SICK-Stegmann high-resolution encoder generates buffered-encoder outputs for master gearing to a slave drive. However, a Tamagawa high-resolution encoder does not.

Figure 99 - Kinetix 300 Master Gearing Example

<!-- image -->

IMPORTANT

The buffered encoder outputs are not supported with Tamagawa highresolution motor feedback.

## Motor Brake Currents

Use these coil current values to size the interposing relay required for your application. See the interconnect diagram for your Kinetix 300 drive/motor beginning on page 178 for typical motor brake circuitry.

Table 77 - Motor Brake Coil Currents

| Compatible Brake Motors/Actuators  (1)                         | Coil Current   |
|----------------------------------------------------------------|----------------|
| MPL-x1510, MPL-x1520, MPL-x1530                                | 0.43…0.53 A    |
| MPL-x210, MPL-x220, MPL-x230                                   | 0.46…0.56 A    |
| MPL/MPF-x310, MPL/MPF-x320, MPL/MPF-x330                       | 0.45…0.55 A    |
| MPM-x115                                                       | 0.45…0.55 A    |
| MPS-x330                                                       | 0.45…0.55 A    |
| MPL-x420, MPL-x430, MPL-x4520, MPL-x4530, MPL-x4540, MPL-B4560 | 0.576…0.704 A  |
| MPM-x130                                                       | 0.576…0.704 A  |
| MPF-x430, MPF-x4530, MPF-x4540                                 | 0.576…0.704 A  |
| MPS-x4540                                                      | 0.576…0.704 A  |
| TLY-A110T, TLY-A120T, and TLY-A130T                            | 0.18…0.22 A    |
| TLY-A220T and TLY-A230T                                        | 0.333…0.407 A  |
| TLY-A2530P, TLY-A2540P, and TLY-A310M                          | 0.351…0.429 A  |

(1) Use of the variable x indicates that this specification applies to 230V and 460V motors.

## System Block Diagrams

This power block diagram applies to 2097-V32PRx, 2097-V33PRx, and 2097V34PRx servo drives.

Figure 100 - Power Block Diagram

<!-- image -->

shunt module is external to the Kinetix 300 drive.

Rx

(1) The 2097-Rx

This power block diagram applies to 2097-V31PRx servo drives. The voltagedoubler circuitry lets the drives with 120V input power get full performance from 240V motors.

Figure 101 - Voltage Doubler Block Diagram

<!-- image -->

shunt module is external to the Kinetix 300 drive.

Rx

(1) The 2097-Rx

## Input and Output Assembly

## Input and Output Assembly

| Topic                     |   Page |
|---------------------------|--------|
| Input and Output Assembly |    191 |
| Output Assembly Examples  |    197 |

The terms input and output refer to the point of view of the scanner device. Output data is produced by the scanner and consumed by the adapter. Input data is produced by the adapter and consumed by the scanner. The Kinetix® 300 drive is an adapter device and the controller, by using RSLogix 5000® software or the Studio 5000 Logix Designer® application, is a scanner device.

The drive contains EtherNet/IP™ Assembly Object Instances that pertain to these RSLogix 5000 software or the Logix Designer application connection parameters:

- Input (actual values such as actual velocity, actual position)
- Output (enable and reference value going to the drive)
- Index Configuration (see Indexing Category on page 99)

Assembly instances are accessible by using Class 3 explicit messages and the Class 1 I/O messaging.

<!-- image -->

Table 79 - Input Assembly

| RSLogix 5000 or Logix Designer Tags   | Description                                                                                                                                                                                                                                                         |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                       | Fault A nonzero value in this field means that the connection to the drive is not operational and no other fields in the Input Assembly should be used.                                                                                                             |
|                                       | DriveEn A nonzero value in this field means that the drive is enabled and the servo loops are closed.                                                                                                                                                               |
|                                       | PhysicalAxisFault A nonzero value in this field means that the drive has faulted.                                                                                                                                                                                   |
|                                       | PositionLockStatus A nonzero value in this field means that the drive is within the position tolerance window of the commanded position.                                                                                                                            |
|                                       | CurrentLimitStatus A nonzero value in this field means that the drive has reached the current limit. A nonzero value in this field does not mean that the drive is limiting current if the current limit was set to a lower value than the drive or motor supports. |
|                                       | RegistrationEventStatus A nonzero value in this field means that the drive has captured a registration event and position.                                                                                                                                          |
| IndexingStatus                        | A nonzero value in this field means that the drive is operating out of the indexing table within the drive.                                                                                                                                                         |
| MotionComplete                        | A nonzero value in this field means that the drive has completed a position-based move. This bit does not apply when in Indexing Current mode.                                                                                                                      |
|                                       | PositiveOvertravelInput A nonzero value in this field means that the positive overtravel input to the drive has been asserted.                                                                                                                                      |
|                                       | NegativeOvertravelInput A nonzero value in this field means that the negative overtravel input to the drive has been asserted.                                                                                                                                      |
| HomingStatus                          | A nonzero value in this field means that the drive is homing as configured by the Homing section of the MotionView software.                                                                                                                                        |
| AxisHomedStatus                       | A nonzero value in this field means that the drive has been successfully homed.                                                                                                                                                                                     |

You can modify Kinetix 300 drive parameters by using Explicit Messaging.

Table 78 - Drive Object Attributes

| Attribute   | Value                             | Comment                 |
|-------------|-----------------------------------|-------------------------|
|             | Service type Get Attribute Single | Service code 0x0E (hex) |
|             | Set Attribute Single              | Service code 0x10 (hex) |
| Class       | 374                               | Hex                     |
| Instance    | ID tag from Appendix C            | –                       |
|             |                                   | Attribute 0 DINT, RAM   |
|             |                                   | 1 DINT, MEM             |
|             |                                   | 2 REAL ,  RAM           |
|             |                                   | 3 REAL ,  MEM           |
|             |                                   | 4 String ,  RAM         |
|             |                                   | 5 String ,  MEM         |

When a Kinetix 300 drive parameter is changed by using explicit messaging, the Set Attribute Single message instruction is directed at this class, the instance is the identifier of the actual parameter and the attribute depends upon the type of data being written.

| IMPORTANT   | If power is removed from the drive, data that is stored in RAM is lost. Data that is stored in the memory module remains through power cycles.                                                |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPORTANT   | Memory module writes are limited to 1,000,000 per device. Make sure that all writes that are targeted at the memory module are necessary and not done as part of a background or cyclic task. |

Table 79 - Input Assembly (Continued)

| RSLogix 5000 or Logix Designer Tags   | Description                                                                                                                                             |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                       | VelocityStandstillStatus A nonzero value in this field means that the drive is within the configured tolerance for being at zero velocity.              |
| VelocityLockStatus                    | A nonzero value in this field means that the drive is within the configured tolerance around the commanded velocity.                                    |
| PowerStructureEn                      | A nonzero value in this field means that the drive power structure is enabled and providing current to the motor.                                       |
| DigitalInputA1Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputA2Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputA3Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputA4Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputB1Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputB2Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputB3Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputB4Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputC1Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputC2Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputC3Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| DigitalInputC4Status                  | A nonzero value in this field means that this digital input on the drive is asserted.                                                                   |
| ActiveIndex                           | This field indicates the currently executing index from within the indexing table in the drive.                                                         |
| ActualVelocity                        | This field indicates the current velocity of the motor that is controlled by the drive.                                                                 |
| ActualPosition                        | This field indicates the current position of the motor that is controlled by the drive.                                                                 |
| PositionCommand                       | This field indicates the position that the drive is moving the motor towards.                                                                           |
| PositionError                         | This field indicates the error between the current command position and the actual position.                                                            |
| MotorCurrent                          | This field indicates the average RMS current being applied to the motor.                                                                                |
| RegistrationPosition                  | This field indicates the position that the motor was at when the registration input was asserted.                                                       |
|                                       | UserDefinedIntegerData0 This field is a copy of the current value of whatever parameter it was configured to be in the MotionView software (Data Link). |
|                                       | UserDefinedIntegerData1 This field is a copy of the current value of whatever parameter it was configured to be in the MotionView software (Data Link). |
|                                       | UserDefinedIntegerReal0 This field is a copy of the current value of whatever parameter it was configured to be in the MotionView software (Data Link). |
|                                       | UserDefinedIntegerReal1 This field is a copy of the current value of whatever parameter it was configured to be in the MotionView software (Data Link). |

Table 80 - Input Assembly Instance (Assembly 113)

| Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                                      |                                      |                                      |                                      |                                      |                                          |                                      |
|--------------------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|------------------------------------------|--------------------------------------|
|                                                        | 0 Reserved Registration EventStatus  | Current LimitStatus                  |                                      | Reserved Reserved Position           | LockStatus                           | Physical AxisFault                       | DriveEn                              |
| 1…3 Reserved                                           | 1…3 Reserved                         | 1…3 Reserved                         | 1…3 Reserved                         | 1…3 Reserved                         | 1…3 Reserved                         | 1…3 Reserved                             | 1…3 Reserved                         |
|                                                        | 4 Reserved Axis Homed Status         | Homing Status Negative               | Overtravel Input                     | Positive Overtravel Input            |                                      | Reserved Motion Complete Indexing Status |                                      |
| 5…7 Reserved                                           | 5…7 Reserved                         | 5…7 Reserved                         | 5…7 Reserved                         | 5…7 Reserved                         | 5…7 Reserved                         | 5…7 Reserved                             | 5…7 Reserved                         |
| 8 Reserved Power Structure                             | 8 Reserved Power Structure           | 8 Reserved Power Structure           | 8 Reserved Power Structure           | 8 Reserved Power Structure           | En                                   | Velocity LockStatus                      | Velocity Standstill Status           |
| 9…11 Reserved                                          | 9…11 Reserved                        | 9…11 Reserved                        | 9…11 Reserved                        | 9…11 Reserved                        | 9…11 Reserved                        | 9…11 Reserved                            | 9…11 Reserved                        |
| 12 Digital Input B4Status                              | Digital Input B3Status               | Digital Input B2Status               | Digital Input B1Status               | Digital Input A4Status               | Digital Input A3Status               | Digital Input A2Status                   | Digital Input A1Status               |
| 13…15 Reserved                                         | 13…15 Reserved                       | 13…15 Reserved                       | 13…15 Reserved                       | 13…15 Reserved                       | 13…15 Reserved                       | 13…15 Reserved                           | 13…15 Reserved                       |
| 16 Reserved                                            | 16 Reserved                          | 16 Reserved                          | 16 Reserved                          | Digital Input C4Status               | Digital Input C3Status               | Digital Input C2Status                   | Digital Input C1Status               |
| 17…19 Reserved                                         | 17…19 Reserved                       | 17…19 Reserved                       | 17…19 Reserved                       | 17…19 Reserved                       | 17…19 Reserved                       | 17…19 Reserved                           | 17…19 Reserved                       |
| 20…23 ActiveIndex (DINT)                               | 20…23 ActiveIndex (DINT)             | 20…23 ActiveIndex (DINT)             | 20…23 ActiveIndex (DINT)             | 20…23 ActiveIndex (DINT)             | 20…23 ActiveIndex (DINT)             | 20…23 ActiveIndex (DINT)                 | 20…23 ActiveIndex (DINT)             |
| 24…27 ActualVelocity (REAL)                            | 24…27 ActualVelocity (REAL)          | 24…27 ActualVelocity (REAL)          | 24…27 ActualVelocity (REAL)          | 24…27 ActualVelocity (REAL)          | 24…27 ActualVelocity (REAL)          | 24…27 ActualVelocity (REAL)              | 24…27 ActualVelocity (REAL)          |
| 28…31 ActualPosition (REAL)                            | 28…31 ActualPosition (REAL)          | 28…31 ActualPosition (REAL)          | 28…31 ActualPosition (REAL)          | 28…31 ActualPosition (REAL)          | 28…31 ActualPosition (REAL)          | 28…31 ActualPosition (REAL)              | 28…31 ActualPosition (REAL)          |
| 32…35 PositionCommand (REAL)                           | 32…35 PositionCommand (REAL)         | 32…35 PositionCommand (REAL)         | 32…35 PositionCommand (REAL)         | 32…35 PositionCommand (REAL)         | 32…35 PositionCommand (REAL)         | 32…35 PositionCommand (REAL)             | 32…35 PositionCommand (REAL)         |
| 36…39 PositionError (REAL)                             | 36…39 PositionError (REAL)           | 36…39 PositionError (REAL)           | 36…39 PositionError (REAL)           | 36…39 PositionError (REAL)           | 36…39 PositionError (REAL)           | 36…39 PositionError (REAL)               | 36…39 PositionError (REAL)           |
| 40…43 MotorCurrent (REAL)                              | 40…43 MotorCurrent (REAL)            | 40…43 MotorCurrent (REAL)            | 40…43 MotorCurrent (REAL)            | 40…43 MotorCurrent (REAL)            | 40…43 MotorCurrent (REAL)            | 40…43 MotorCurrent (REAL)                | 40…43 MotorCurrent (REAL)            |
| 44…47 RegistrationPosition (REAL)                      | 44…47 RegistrationPosition (REAL)    | 44…47 RegistrationPosition (REAL)    | 44…47 RegistrationPosition (REAL)    | 44…47 RegistrationPosition (REAL)    | 44…47 RegistrationPosition (REAL)    | 44…47 RegistrationPosition (REAL)        | 44…47 RegistrationPosition (REAL)    |
| 48…51 UserDefinedIntegerData0 (DINT)                   | 48…51 UserDefinedIntegerData0 (DINT) | 48…51 UserDefinedIntegerData0 (DINT) | 48…51 UserDefinedIntegerData0 (DINT) | 48…51 UserDefinedIntegerData0 (DINT) | 48…51 UserDefinedIntegerData0 (DINT) | 48…51 UserDefinedIntegerData0 (DINT)     | 48…51 UserDefinedIntegerData0 (DINT) |
| 52…55 UserDefinedIntegerData1 (DINT)                   | 52…55 UserDefinedIntegerData1 (DINT) | 52…55 UserDefinedIntegerData1 (DINT) | 52…55 UserDefinedIntegerData1 (DINT) | 52…55 UserDefinedIntegerData1 (DINT) | 52…55 UserDefinedIntegerData1 (DINT) | 52…55 UserDefinedIntegerData1 (DINT)     | 52…55 UserDefinedIntegerData1 (DINT) |
| 56…59 UserDefinedIntegerReal0 (REAL)                   | 56…59 UserDefinedIntegerReal0 (REAL) | 56…59 UserDefinedIntegerReal0 (REAL) | 56…59 UserDefinedIntegerReal0 (REAL) | 56…59 UserDefinedIntegerReal0 (REAL) | 56…59 UserDefinedIntegerReal0 (REAL) | 56…59 UserDefinedIntegerReal0 (REAL)     | 56…59 UserDefinedIntegerReal0 (REAL) |
| 60…64 UserDefinedIntegerReal1 (REAL)                   | 60…64 UserDefinedIntegerReal1 (REAL) | 60…64 UserDefinedIntegerReal1 (REAL) | 60…64 UserDefinedIntegerReal1 (REAL) | 60…64 UserDefinedIntegerReal1 (REAL) | 60…64 UserDefinedIntegerReal1 (REAL) | 60…64 UserDefinedIntegerReal1 (REAL)     | 60…64 UserDefinedIntegerReal1 (REAL) |

In this Input Assembly example, the parameter ActiveIndex with a range of 24…27 bytes is expanded to show the low byte, low middle byte, high middle byte, and high byte. These values are typical for each parameter in Table 80 .

Table 81 - Input Assembly Example

| Byte Parameter Value              |
|-----------------------------------|
| 20 ActiveIndex - Low byte         |
| 21 ActiveIndex - Low middle byte  |
| 22 ActiveIndex - High middle byte |
| 23 ActiveIndex - High byte        |

Table 82 - Output Assembly

| RSLogix 5000 or Logix Designer Tags   | Description                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AbortIndex                            | Upon transition from 0 to 1 of this field, the drive aborts the current index or position based move the drive is executing and decel to zero velocity.                                                                                                                                                                      |
| StartMotion                           | Upon transition from 0 to 1 of this field, the drive begins moving towards the position in the CommandPosition field (listed in this table), assuming the drive is enabled.                                                                                                                                                  |
| DefineHome                            | Upon transition from 0 to 1 of this field, the drive defines the current position of the motor to be home.                                                                                                                                                                                                                   |
| AbortHoming                           | Upon transition from 0 to 1 of this field, the drive aborts (decel to zero velocity) the homing operation.                                                                                                                                                                                                                   |
| StartHoming                           | Upon transition from 0 to 1 of this field, the drive begins homing as configured by the Homing section of the MotionView software assuming the drive is enabled.                                                                                                                                                             |
| DriveEn                               | Upon transition from 0 to 1 of this field, the drive enables, it turns on power structure, closes servo loops, tracks commands.                                                                                                                                                                                              |
| StartingIndex                         | This field defines the first index that the drive should execute if the drive is operating in Indexing mode.                                                                                                                                                                                                                 |
| ReferenceSource                       | This field defines the type of control being exerted over EtherNet/IP network (0 = current, 1 = velocity, 2 = incremental position, 3 = absolute position, 4 = incremental registration, 5 = absolute registration, 6=Rotary Absolute, 7=Rotary Incremental, 8=Rotary Shortest Path, 9=Rotary Positive, 10=Rotary Negative). |
| AccelerationLimit                     | This field defines the maximum acceleration that the drive uses in accelerating towards the commanded position .                                                                                                                                                                                                             |
| DecelerationLimit                     | This field defines the maximum deceleration that the drive uses in accelerating towards the commanded position .                                                                                                                                                                                                             |
|                                       | CommandCurrentOrVelocity This field defines the commanded current (Amps RMS) or Velocity (User Units/s) if the ReferenceSource is 0 or 1 respectively and the drive is enabled.                                                                                                                                              |
| VelocityLimit                         | This field defines the maximum velocity that the drive uses in the profile towards the commanded position.                                                                                                                                                                                                                   |
| CommandPosition                       | This field defines the next position command that the drive should move the motor towards, takes effect only upon 0 to 1 transition of StartMotion field (that is listed in this table).                                                                                                                                     |
| RegistrationOffset                    | This field defines the offset from the registration event that the drive should move to during an incremental or absolute registration-based move.                                                                                                                                                                           |
|                                       | UserDefinedIntegerData0 The value in this field is written to whatever parameter it was configured to be in the MotionView software (Data Link).                                                                                                                                                                             |
|                                       | UserDefinedIntegerData1 The value in this field is written to whatever parameter it was configured to be in the MotionView software (Data Link).                                                                                                                                                                             |
|                                       | UserDefinedIntegerReal0 The value in this field is written to whatever parameter it was configured to be in the MotionView software (Data Link).                                                                                                                                                                             |
|                                       | UserDefinedIntegerReal1 The value in this field is written to whatever parameter it was configured to be in the MotionView software (Data Link).                                                                                                                                                                             |

Table 83 - Output Assembly Instance (Assembly 114)

| Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                                                                                             |                                       |                                       |                                       |                                       |                                       |                                       |
|--------------------------------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
|                                                        | 0 Drive En Reserved Start Homing Abort Homing Define Home Start Motion Reserved Abort Index |                                       |                                       |                                       |                                       |                                       |                                       |
| 1 Reserved                                             | 1 Reserved                                                                                  | 1 Reserved                            | 1 Reserved                            | 1 Reserved                            | 1 Reserved                            | 1 Reserved                            | 1 Reserved                            |
| 2 Reserved                                             | 2 Reserved                                                                                  | 2 Reserved                            | 2 Reserved                            | 2 Reserved                            | 2 Reserved                            | 2 Reserved                            | 2 Reserved                            |
| 3 Reserved                                             | 3 Reserved                                                                                  | 3 Reserved                            | 3 Reserved                            | 3 Reserved                            | 3 Reserved                            | 3 Reserved                            | 3 Reserved                            |
| 4…7 StartingIndex (DINT)                               | 4…7 StartingIndex (DINT)                                                                    | 4…7 StartingIndex (DINT)              | 4…7 StartingIndex (DINT)              | 4…7 StartingIndex (DINT)              | 4…7 StartingIndex (DINT)              | 4…7 StartingIndex (DINT)              | 4…7 StartingIndex (DINT)              |
| 8…11 ReferenceSource (DINT)                            | 8…11 ReferenceSource (DINT)                                                                 | 8…11 ReferenceSource (DINT)           | 8…11 ReferenceSource (DINT)           | 8…11 ReferenceSource (DINT)           | 8…11 ReferenceSource (DINT)           | 8…11 ReferenceSource (DINT)           | 8…11 ReferenceSource (DINT)           |
| 12…15 AccelerationLimit (REAL)                         | 12…15 AccelerationLimit (REAL)                                                              | 12…15 AccelerationLimit (REAL)        | 12…15 AccelerationLimit (REAL)        | 12…15 AccelerationLimit (REAL)        | 12…15 AccelerationLimit (REAL)        | 12…15 AccelerationLimit (REAL)        | 12…15 AccelerationLimit (REAL)        |
| 16…19 DecelerationLimit (REAL)                         | 16…19 DecelerationLimit (REAL)                                                              | 16…19 DecelerationLimit (REAL)        | 16…19 DecelerationLimit (REAL)        | 16…19 DecelerationLimit (REAL)        | 16…19 DecelerationLimit (REAL)        | 16…19 DecelerationLimit (REAL)        | 16…19 DecelerationLimit (REAL)        |
| 20…23 CommandCurrentOrVelocity (REAL)                  | 20…23 CommandCurrentOrVelocity (REAL)                                                       | 20…23 CommandCurrentOrVelocity (REAL) | 20…23 CommandCurrentOrVelocity (REAL) | 20…23 CommandCurrentOrVelocity (REAL) | 20…23 CommandCurrentOrVelocity (REAL) | 20…23 CommandCurrentOrVelocity (REAL) | 20…23 CommandCurrentOrVelocity (REAL) |
| 24…27 VelocityLimit (REAL)                             | 24…27 VelocityLimit (REAL)                                                                  | 24…27 VelocityLimit (REAL)            | 24…27 VelocityLimit (REAL)            | 24…27 VelocityLimit (REAL)            | 24…27 VelocityLimit (REAL)            | 24…27 VelocityLimit (REAL)            | 24…27 VelocityLimit (REAL)            |
| 28…31 CommandPosition (REAL)                           | 28…31 CommandPosition (REAL)                                                                | 28…31 CommandPosition (REAL)          | 28…31 CommandPosition (REAL)          | 28…31 CommandPosition (REAL)          | 28…31 CommandPosition (REAL)          | 28…31 CommandPosition (REAL)          | 28…31 CommandPosition (REAL)          |
| 32…35 RegistrationOffset (REAL)                        | 32…35 RegistrationOffset (REAL)                                                             | 32…35 RegistrationOffset (REAL)       | 32…35 RegistrationOffset (REAL)       | 32…35 RegistrationOffset (REAL)       | 32…35 RegistrationOffset (REAL)       | 32…35 RegistrationOffset (REAL)       | 32…35 RegistrationOffset (REAL)       |
| 36…39 UserDefinedIntegerData0 (DINT)                   | 36…39 UserDefinedIntegerData0 (DINT)                                                        | 36…39 UserDefinedIntegerData0 (DINT)  | 36…39 UserDefinedIntegerData0 (DINT)  | 36…39 UserDefinedIntegerData0 (DINT)  | 36…39 UserDefinedIntegerData0 (DINT)  | 36…39 UserDefinedIntegerData0 (DINT)  | 36…39 UserDefinedIntegerData0 (DINT)  |
| 40…43 UserDefinedIntegerData1 (DINT)                   | 40…43 UserDefinedIntegerData1 (DINT)                                                        | 40…43 UserDefinedIntegerData1 (DINT)  | 40…43 UserDefinedIntegerData1 (DINT)  | 40…43 UserDefinedIntegerData1 (DINT)  | 40…43 UserDefinedIntegerData1 (DINT)  | 40…43 UserDefinedIntegerData1 (DINT)  | 40…43 UserDefinedIntegerData1 (DINT)  |
| 44…47 UserDefinedIntegerReal0 (REAL)                   | 44…47 UserDefinedIntegerReal0 (REAL)                                                        | 44…47 UserDefinedIntegerReal0 (REAL)  | 44…47 UserDefinedIntegerReal0 (REAL)  | 44…47 UserDefinedIntegerReal0 (REAL)  | 44…47 UserDefinedIntegerReal0 (REAL)  | 44…47 UserDefinedIntegerReal0 (REAL)  | 44…47 UserDefinedIntegerReal0 (REAL)  |
| 48…51 UserDefinedIntegerReal1 (REAL)                   | 48…51 UserDefinedIntegerReal1 (REAL)                                                        | 48…51 UserDefinedIntegerReal1 (REAL)  | 48…51 UserDefinedIntegerReal1 (REAL)  | 48…51 UserDefinedIntegerReal1 (REAL)  | 48…51 UserDefinedIntegerReal1 (REAL)  | 48…51 UserDefinedIntegerReal1 (REAL)  | 48…51 UserDefinedIntegerReal1 (REAL)  |

In this Output Assembly example, the parameter StartingIndex with a range of 4…7 bytes is expanded to show the low byte, low middle byte, high middle byte, and high byte. These values are typical for each parameter in Table 83 .

Table 84 - Output Assembly Example

| Byte Parameter Value               |
|------------------------------------|
| 4 StartingIndex - Low byte         |
| 5 StartingIndex - Low middle byte  |
| 6 StartingIndex - High middle byte |
| 7 StartingIndex - High byte        |

The Attribute Values in this example only apply to Class 374 and not to Class 4 (Assembly Objects).

## Output Assembly Examples

This section provides examples of various motion profiles by showing which tags in the Output Assembly to manipulate.

You can manage the values in the Output Assembly by manipulating them in ladder code or by editing the tag directly in the tag structure.

IMPORTANT The Kinetix 300 drive must be in EtherNet/IP External Reference mode.

Figure 102 is an example of moving a value into the .ReferenceSource of the Output Assembly.

Figure 102 - Set Value of Output Assembly Tag

<!-- image -->

Figure 103 is an example of latching-on the .StartMotion bit of the Output Assembly.

Figure 103 - Turn-on the Output Assembly Tag

<!-- image -->

Figure 104 is an example of turning on the .StartMotion bit of the Output Assembly by editing the tag directly.

Figure 104 - Changing a Value in the Output Assembly Tag Structure

<!-- image -->

## Incremental Position Point-to-Point Profile

To execute an incremental position move, set the tag values shown in Table 85 .

Table 85 - Output Assembly Tags

| RSLogix 5000 or Logix Designer Tags   | Value                                                               |
|---------------------------------------|---------------------------------------------------------------------|
| ReferenceSource                       | Set the value to 2.                                                 |
| CommandPosition                       | Configure the motion profile by setting tags to the desired values. |
| VelocityLimit                         |                                                                     |
| AccelerationLimit                     |                                                                     |
| DecelerationLimit                     |                                                                     |
| DriveEn                               | Enable the drive by turning the tag “On.”                           |
| StartMotion                           | Start profile by turning the tag “On.”                              |

## Velocity Motion Profile

To execute a velocity move, set the tag values shown in Table 86 .

Table 86 - Output Assembly Tags

|        | ID Tag RSLogix 5000 or Logix Designer Tags           | Value                                                                                                                                                                                                                                           |
|--------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        |                                                      | N/A ReferenceSource Set the value to 1.                                                                                                                                                                                                         |
|        | N/A CommandCurrentOrVelocity Set the velocity value. |                                                                                                                                                                                                                                                 |
| 75 (1) | Enable Accel/Decel function/limits for Velocity mode | • Use internal defaults for Accel/Decel (ID 75 set to 0 = Disable). • Set Accel/Decel values by writing to ID 76 and 77 by using explicit messaging (See Appendix D on page 213). Tag 75 must be set to 1 = Enabled, for the values to be used. |
| 76 (1) | Accel value for Velocity mode                        | • Use internal defaults for Accel/Decel (ID 75 set to 0 = Disable). • Set Accel/Decel values by writing to ID 76 and 77 by using explicit messaging (See Appendix D on page 213). Tag 75 must be set to 1 = Enabled, for the values to be used. |
| 77 (1) | Decel value for Velocity mode                        | • Use internal defaults for Accel/Decel (ID 75 set to 0 = Disable). • Set Accel/Decel values by writing to ID 76 and 77 by using explicit messaging (See Appendix D on page 213). Tag 75 must be set to 1 = Enabled, for the values to be used. |
|        |                                                      | N/A DriveEn Enable the drive by turning the tag “On.”                                                                                                                                                                                           |

## Tag Number Descriptions

<!-- image -->

## Kinetix 300 Drive ID Tag Numbers

| Topic                   |   Page |
|-------------------------|--------|
| Tag Number Descriptions |    199 |
| Index Base Addressing   |    212 |

To change these parameters by using an Explicit Message, you configure the message to target class 374. The instance corresponds to the ID tag number in Table 87. The attribute is defined by the Drive Object Attributes table on page 192 .

| IMPORTANT   | Memory module writes are limited to 1,000,000 per device. Make sure that all writes that are targeted at the memory module are necessary and not done as part of a background or cyclic task.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Table 87 - Kinetix® 300 Drive Tag Numbers

<!-- image -->

|                                | Faults                                 |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
|--------------------------------|----------------------------------------|----------------------------------|-------------------------------------------------|-----------------------------------------|-------------------------------------|-------------------------------------------------|---------------------------------------------------------------|--------------------------|---------------------------------------|--------------------------------------------------|---------------------------------------------------------------------------------------------|-----------------------------------------------|-----------------------------------|------------------------------|---------------------------------|----------------------------------------------------|----------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Monitor                        |                                        |                                  |                                                 | X                                       |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| Homing                         |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| Indexing                       |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| Dynamics                       |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| Position Limits                |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| Velocity Limits                |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| Analog I/O                     |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                | X                                        |                                                                                                                                                                                                         |                                                                                                                   |
| Digital I/O                    |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| EtherNet/IP™ (CIP)             |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| General -Linear                |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| General -Synchronous           |                                        |                                  |                                                 |                                         | X X                                 |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          | X X                                                                                                                                                                                                     | X X                                                                                                               |
| Motor-Linear                   |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| Motor-Synchronous              |                                        |                                  |                                                 |                                         |                                     | X X                                             | X X X X                                                       | X X                      | X                                     | X                                                | X X X                                                                                       | X X                                           | X X                               | X X                          | X                               | X                                                  | X X            |                                          |                                                                                                                                                                                                         |                                                                                                                   |
| Top Level                      | X                                      | X                                | X                                               |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |
|                                | See  Table on page 82                  | Up to 20 user-defined characters | Unique numb er assigned to drive at the factory | in UU/sec                               | Ra nge: 0 = Positive, 1 = Negative  | Motor serial numb er (for Allen-Bradley® motor) | Motor catalog number (for Allen-Bradley motor)  Allen-Bradley | Range: 0…5               | Range: 0…0.1 Kg-m 2                   | Range: 1…500 V/K rpm                             | Range: 0.01…10 N•m/A  Range: 0.1…500 mH                                                     | Range: 0.01…500                              | Range: 0.5…50 A                   | Range: 500…20,000 rpm        | Range: 2…200                    | Range: 256 to (65536 x 12/Npoles) expressed in PPR | Range: 50…800V | 0 = Inhibit only 1 = Run                 | User may lower this value. This lets you trigger a motor currentalarm. However, the drive will not limit the actual current to themotor. The actual RMS current limit to the motor is not configurable. | User may lower this peak value to  limit current to motor. Do not set  below the RMS Current for motor (tag #30). |
|                                |                                        | 2 String R/W Drive symbolic name |                                                 |                                         |                                     | 10 String R Motor ID                            |                                                               |                          |                                       | 19 DINT R Motor voltage or back EMF constant, Ke | 20 DINT R Motor torque or force constant, Kt  21 DINT R Motor phase-to-phase inductance, Lm |                                               |                                   |                              |                                 |                                                    |                | 29 DINT R/W Enable switch function       | 30 REAL R/W Continuous RMS current for motor selected                                                                                                                                                   | Peak current limit for 8 kHz operation (based on motor                                                            |
| Access Description Value/Notes | 1 String R Drive identification string |                                  | 3 String R Drive serial number                  | 7 REAL R Actual measured motor velocity | 8 DINT R/W Negative Motion Polarity |                                                 | 11 String R Motor model  12 String R Motor vendor             | 14 DINT R Hallcode index | 18 DINT R Motor moment of inertia, Jm |                                                  |                                                                                             | 22 DINT R Motor phase-to-phase resistance, Rm | 23 DINT R Motor max current (RMS) | 24 DINT R Motor max velocity | 25 DINT R Motor number of poles | 26 REAL R Encoder resolution                       |                | 27 DINT R Nominal Motor terminal voltage |                                                                                                                                                                                                         | selected)                                                                                                         |
| Data Type                      |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         | 32 REAL R/W                                                                                                       |
| ID                             |                                        |                                  |                                                 |                                         |                                     |                                                 |                                                               |                          |                                       |                                                  |                                                                                             |                                               |                                   |                              |                                 |                                                    |                |                                          |                                                                                                                                                                                                         |                                                                                                                   |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

| Faults                         |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
|--------------------------------|-------------------------------------------------------------------------|------------------------------------------------------|------------------------------------------------|---------------------------------------------|-----------------------------------------|---------------------------------------------|-----------------------------------------|---------------------------------------------|-----------------------------------------------|---------------------------------------|-------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Monitor                        |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| Homing                         |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| Indexing                       |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| Dynamics                       |                                                                         |                                                      |                                                | X                                           | X                                       | X                                           | X                                       | X                                           | X                                             | X                                     |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| Position Limits                |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              | X                             | X                                                                                                                                |
| Velocity Limits                |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    | X                                                                                                                                                                 | X                                                                                                                                                                           | X                                                                                                                                                                                            |                               |                                                                                                                                  |
| Analog I/O                     | X                                                                       | X                                                    |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| Digital I/O                    |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| EtherNet/IP™ (CIP)             |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| EtherNet                       |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| General -Linear                |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| General -Synchronous           |                                                                         |                                                      | X X                                            |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| Motor-Linear                   |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| Motor-Synchronous              |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
| Top Level                      |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               | X                                                                                  |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |
|                                | Range:  Range: Range: - X…+X Amps/Volt X = drive peak output current/10 | Range: -10,000…+10,000 rpm/Volt                      | 0 = Disabled 1 = Enabled                       | Range: 0…32767                              | Range: 0…32767                          | Range: 0…32767                              | Range: 0…16383                          | Range: 0…32767                              | Range: 0…20000                                | Range: -16…+4                         | 0 = No action 1 = Reset drive | Range: 1…32767                                                                     | Range: 0…100 rpm                                                                                                                                                  | Range: 10…10000 rpm                                                                                                                                                         | Range: -10000…+10000 rpm                                                                                                                                                                     | Range: 1…32767 encoder counts | Range: 0.25…8000 ms                                                                                                              |
| Access Description Value/Notes | 35 REAL R/W Analog input #1 current reference scale                     | 36 REAL R/W Analog input #1 velocity reference scale | 39 DINT R/W Motor thermal protection function: |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               | Network group ID. Allows th e assignment of different  drives into logical groups. | Absolute value in user units/s below which the drivewill set the Zero Speed Digital Output (if configured)and the VelocityStandstillStatus bit in the EtherNet/IP | The range in user units/s around the At Speed forsetting the In-Speed Window Digital Output (ifconfigured) and the VelocityLockStatus bit in theEtherNet/IP Input Assembly. | Value in user units/s for the target velocity for whichthe drive will set the In-Speed Window Digital Output(if configured) and the VelocityLockStatus bit in theEtherNet/IP Input Assembly. |                               | The amount of time that the  drive can be outside of the Position Error before the drive asserts an Excess Position Error Fault. |
|                                |                                                                         |                                                      |                                                | 44 DINT R/W Velocity loop proportional gain | 45 DINT R/W Velocity loop integral gain | 46 DINT R/W Position loop proportional gain | 47 DINT R/W Position loop integral gain | 48 DINT R/W Position loop differential gain | 49 DINT R/W Position loop integral gain limit | 51 DINT R/W Gains scaling coefficient | 53 DINT R/W Drive reset       |                                                                                    | Input Assembly.                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              | 61 DINT R/W Position error    |                                                                                                                                  |
| Data Type                      |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               | 57 DINT R/W                                                                        | 58 REAL R/W                                                                                                                                                       | 59 REAL R/W                                                                                                                                                                 | 60 REAL R/W                                                                                                                                                                                  |                               | 62 REAL R/W                                                                                                                      |
| ID                             |                                                                         |                                                      |                                                |                                             |                                         |                                             |                                         |                                             |                                               |                                       |                               |                                                                                    |                                                                                                                                                                   |                                                                                                                                                                             |                                                                                                                                                                                              |                               |                                                                                                                                  |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

|                                | Faults                                                                                                                                                                                                   |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|----------------------------------------------|----------------------------------------------------------------------------------|----------------------|-----------------------------------|--------------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------|------------------------------------------------|--------------------------------------------------|
| Monitor                        | X                                                                                                                                                                                                        | X                                                                                                                                 |                                                   |                                              |                                                                                  |                      | X                                 | X                              | X                                                                                              |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Homing                         |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Indexing                       |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Dynamics                       |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Position Limits                |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Velocity Limits                |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Analog I/O                     |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Digital I/O                    |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| EtherNet/IP™ (CIP)             |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| EtherNet                       |                                                                                                                                                                                                          |                                                                                                                                   | X                                                 | X                                            | X                                                                                | X                    |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| General -Linear                |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                | X X                                                              |                                           |                                           |                                                                                                 |                                                |                                                  |
| General -Synchronous           |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  | X X                                       | X X                                       | X X                                                                                             | X X                                            | X X                                              |
| Motor-Linear                   |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Motor-Synchronous              |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Top Level                      |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
|                                | A1 Input = Bit 0 A2 Input = Bit 1 A3 Input = Bit 2 A4 Input = Bit 3 B1 Input = Bit 4 B2 Input = Bit 5 B3 Input = Bit 6B4 Input = Bit 7C1 Input = Bit 8C2 Input = Bit 9C3 Input = Bit 10C4 Input = Bit 11 | Output 1 = Bit 0Output 2 = Bit 1Output 3 = Bit 2Output 4 = Bit 3                                                                  | IP address changes at next powerup. 32 bit value. | Mask change s at next powerup. 32 bit value. | Address changes at next powerup. 32 bit value.  0 = Manual  1 = Use DHCP service |                      |                                   | Volts                          | 0 = Temperatures < 40 °C (104 °F)  Actual heat sink temperature = Temperatures >40 °C (104 °F) | 0 = Disabled 1 = Enabled                                         | Range: 0.1…5000000 rpm/s                  | Range: 0.1…5000000 rpm/s                  | 0 = On activation of Enable/Inhibit input (A3) 1 = On deactivation of Enable/Inhibit input (A3) | Master counts range: -32768…+32768             | System counts range: 1…32768                     |
| Access Description Value/Notes |                                                                                                                                                                                                          | Digital outputs states. Writing to these variables sets/resets digital outputs that have not been assigned to a special function. | 67 DINT R/W Ethernet IP address                   | 68 DINT R/W Ethernet IP NetMask              |                                                                                  | 70 DINT R/W Use DHCP | 71 REAL R Analog Input AIN1 value |                                |                                                                                                | 75 DINT R/W Enable Accel/Decel function/limits for Velocity mode | 76 REAL R/W Accel value for Velocity mode | 77 REAL R/W Decel value for Velocity mode | 78 DINT R/W Reset fault configuration                                                           | 79 DINT R/W Master to system ratio (numerator) | 80 DINT R/W Master to system ratio (denominator) |
|                                | 65 DINT R Digital inputs states                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              | 69 DINT R/W Ethernet Gateway IP address                                          |                      |                                   | 73 REAL R Measured Bus voltage | 74 REAL R Heatsink temperature                                                                 |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| Data Type                      |                                                                                                                                                                                                          | 66 DINT R/W                                                                                                                       |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |
| ID                             |                                                                                                                                                                                                          |                                                                                                                                   |                                                   |                                              |                                                                                  |                      |                                   |                                |                                                                                                |                                                                  |                                           |                                           |                                                                                                 |                                                |                                                  |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

| Faults                         |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
|--------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------|------------------------------|------------------------------|---------------------------|
| Monitor                        |                                                                                    |                                                                                                                                                                               |                                                                            | X                                                                                                                                                                                                                  |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            | X                                                                                   | X                        | X                            | X                            | X                         |
| Homing                         |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| Indexing                       |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| Dynamics                       |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| Position Limits                |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           | X                                                                                                                                                                                                                                                                                 | X                                                                                                                                                        |                                                            |                                                                                     |                          |                              |                              |                           |
| Velocity Limits                |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| Analog I/O                     |                                                                                    | X                                                                                                                                                                             | X                                                                          | X                                                                                                                                                                                                                  | X                                                                              | X                                                                         |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| Digital I/O                    | X                                                                                  |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| EtherNet/IP™ (CIP)             |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| EtherNet                       |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| General -Linear                |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| General -Synchronous           |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          | X                                                          |                                                                                     |                          |                              |                              |                           |
| Motor-Linear                   |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| Motor-Synchronous              |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
| Top Level                      |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |
|                                | 0 = Not used  1 = Disable and coast 2 = Ramped Decel and Disable                   | 0 = Not assigned1 = Phase Current (RMS)2 = Phase Current (Peak Value)3 = Motor Velocity4 = Phase Current U5 = Phase Current V6 = Phase Current W 7 = Iq current8 = Id current |                                                                            | Range: 0…10V                                                                                                                                                                                                       | Range: 0…100 mV                                                                | Range: -10,000…+10,000 mV                                                 | User units per seconds 2                                                                                                                                                                                                                                                          | User units                                                                                                                                               | 181 REAL R/W User units Revolutions of motor per user unit | Counts                                                                              | Amps                     | Encoder pulses               | Encoder pulses               | Encoder pulses            |
| Access Description Value/Notes | Configuration of the action-to-take when the hardware limit switches are asserted. | 85 DINT R/W Analog output function                                                                                                                                            | 86 REAL R/W Analog output scale for velocity quantities Range: 0…10 mV/rpm | 87 REAL R/W Analog output scale for current related quantities Range: 0…10 V/A  Analog output value. Allows control of analog output through this tag value. Used if tag #85 is set to 0.  if tag #85 is set to 0. | Analog input #1 dead-band. Applied when used as current or velocity reference. | Analog input #1 offset. Applied when used as current/  velocity reference | The deceleration rate that the drive will use to bringthe motor to a stop when either the Abort Homing orAbort Index Digital Inputs is asserted (if configured) oreither the AbortIndex or AbortHoming bit is set in the ortHoming bit is set in the EtherNet/IP Output Assembly. | The tolerance in user units around the commandedposition inside of which the drive will set thePositionLockStatus bit in the EtherNet/IP Input Assembly. |                                                            | Encoder input counter value, reset by writing zero or other value to the parameter. | 183 REAL R Phase current | 184 DINT R/W Target position | 185 DINT R/W Actual position | 186 DINT R Position error |
| Data Type                      | 84 DINT R/W                                                                        |                                                                                                                                                                               |                                                                            | 88 REAL W                                                                                                                                                                                                          | 89 REAL R/W                                                                    | 90 REAL R/W                                                               | 178 REAL R/W                                                                                                                                                                                                                                                                      | 179 DINT R/W                                                                                                                                             |                                                            | 182 DINT R/W                                                                        |                          |                              |                              |                           |
| ID                             |                                                                                    |                                                                                                                                                                               |                                                                            |                                                                                                                                                                                                                    |                                                                                |                                                                           |                                                                                                                                                                                                                                                                                   |                                                                                                                                                          |                                                            |                                                                                     |                          |                              |                              |                           |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

<!-- image -->

| Indexing Homing Monitor Faults                                  |                                                            |                                      |                                      |                                      |                                      |                                                                            |                                      |                                                        |                                      |                                      |                                            |                                                                                        |                                                                                        |                                                                                      |
|-----------------------------------------------------------------|------------------------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|----------------------------------------------------------------------------|--------------------------------------|--------------------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Digital I/O Analog I/O Velocity Limits Position Limits Dynamics |                                                            | X                                    | X                                    | X                                    | X                                    | X X                                                                        | X                                    |                                                        |                                      |                                      | X                                          |                                                                                        |                                                                                        | X                                                                                    |
|                                                                 | Motor-Linear General -Synchronous General -Linear EtherNet |                                      | Range: 0…1000 ms                     | Range: 0…1000 ms                     | Range: 0…1000 ms                     | Range: 0…1000 ms  Range: 0…1000 ms                                         | Range: 0…1000 ms                     |                                                        |                                      |                                      |                                            |                                                                                        |                                                                                        |                                                                                      |
| EtherNet/IP™ (CIP)                                              | Range: 0…1000 ms                                           | X  Range: 0…1000 ms                  |                                      | 192 DINT R/W Input A4 de-bounce time | 193 DINT R/W Input B1 de-bounce time | 194 DINT R/W Input B2 de-bounce time  195 DINT R/W Input B3 de-bounce time |                                      | 197 DINT R/W Input C1 de-bounce time  Range: 0…1000 ms | X Range: 0…1000 ms  X                | X                                    | Range: 0…1000                              | 0 = Not Assigned1 = Zero Speed2 = In Speed Window3 = Current Limit4 = Run time fault X | 0 = Not Assigned1 = Zero Speed2 = In Speed Window3 = Current Limit4 = Run time fault X | 0 = Not Assigned1 = Zero Speed2 = In Speed Window3 = Current Limit4 = Run time fault |
| Access Description Value/Notes                                  | 189 DINT R/W Input A1 de-bounce time                       |                                      | 191 DINT R/W Input A3 de-bounce time |                                      |                                      |                                                                            | 196 DINT R/W Input B4 de-bounce time |                                                        | 198 DINT R/W Input C2 de-bounce time | 199 DINT R/W Input C3 de-bounce time | Range: 0…1000 ms                           |                                                                                        | 202 DINT R/W Programmable Output Function: OUT2                                        | 203 DINT R/W Programmable Output Function: OUT3                                      |
|                                                                 | Top Level Motor-Synchronous                                |                                      |                                      |                                      |                                      |                                                                            |                                      |                                                        |                                      |                                      |                                            |                                                                                        |                                                                                        |                                                                                      |
|                                                                 |                                                            | 190 DINT R/W Input A2 de-bounce time |                                      |                                      |                                      |                                                                            |                                      |                                                        |                                      |                                      | 200 DINT R/W Input C4 de-bounce time in mS | 201 DINT R/W Programmable Output Function: OUT1                                        |                                                                                        |                                                                                      |
| Data Type                                                       |                                                            |                                      |                                      |                                      |                                      |                                                                            |                                      |                                                        |                                      |                                      |                                            |                                                                                        |                                                                                        |                                                                                      |
| ID                                                              |                                                            |                                      |                                      |                                      |                                      |                                                                            |                                      |                                                        |                                      |                                      |                                            |                                                                                        |                                                                                        |                                                                                      |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

<!-- image -->

| Faults                         |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|------------------------------------------|----------------------------------|------------------------------|----|------------------------------|---------------------------|------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| Monitor                        |                                                                                                                        |                                            |                                          | X                                | X                            | X  | X                            | X                         |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| Homing                         |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       | X                                                  | X                                                                                                                                              |                                                |
| Indexing                       |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| Dynamics                       |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| Position Limits                |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           | X X                                                  | X                                                              | X                                                                                                        | X                     |                                                    |                                                                                                                                                |                                                |
| Velocity Limits                |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| Analog I/O                     |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| Digital I/O                    | X                                                                                                                      |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| EtherNet/IP™ (CIP)             |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| EtherNet                       |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| General -Linear                |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| General -Synchronous           |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| Motor-Linear                   |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| Motor-Synchronous              |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| Top Level                      |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
| Access Description Value/Notes |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |
|                                | 0 = Not Assigned1 = Zero Speed2 = In Speed Window3 = Current Limit4 = Run time fault 5 = Ready6 = Brake7 = In position | Bit 0 = Hall 1Bit 1 = Hall 2Bit 2 = Hall 3 | Encoder counts Encoder counts            | User units                       | User units                   |    | User units                   | Encoder counts            | Encoder counts (positive)  Encoder counts (negative) | 0 = Off  1 = Disable and Coast 2 = Ramped Decel and Disable    | User units (positive)                                                                                    | User units (negative) | Range 0…10,000,000 UU per second  2 .              | Range: -32767…+32767 user units.                                                                                                               | Range: +/- 2,147,418,112 encoder counts.       |
|                                | 204 DINT R/W Programmable Output Function: OUT4                                                                        | 205 DINT R Current hall code               | 206 DINT R Primary encoder current value | 208 REAL R Registration position | 209 REAL R/W Target position |    | 210 REAL R/W Actual position | 211 REAL R Position error | 216 DINT R/W The tolerance around the commanded position outside of which the drive will assert a Excess Position ErrorFault when the Max Error Time is exceeded. 217 DINT R/W                                                      | Off or On depending if software travel limits should be  used. | If Soft Limits are On, the position that when reached,the drive will assert a Software Overtravel fault. |                       | 227 REAL R/W Homing acceleration/deceleration rate | The new position of the motor after the homingsequence is complete. All subsequent absolute movesare taken relative to this new zero position. | 229 DINT R/W Homing mode: Home Position Offset |
| Data Type                      |                                                                                                                        |                                            | 207 DINT R Registration position         |                                  |                              |    |                              |                           | 217 DINT R/W                                         | 218 DINT R/W                                                   | 219 REAL R/W                                                                                             | 220 REAL R/W          |                                                    | 228 REAL R/W                                                                                                                                   |                                                |
| ID                             |                                                                                                                        |                                            |                                          |                                  |                              |    |                              |                           |                                                      |                                                                |                                                                                                          |                       |                                                    |                                                                                                                                                |                                                |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

<!-- image -->

|                                | X X                                                                                                                                           | X                                                           |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-------------------------------|----------------------------------------------|-------------------------------------------|----------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|----------------------------------------------|--------------------------------------------------------|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Position Limits                |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
| Velocity Limits                |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
| Digital I/O                    |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
|                                |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        | X                                 | X                                 |                                   | X                                            | X X                                                    | X                                           |                                                                                                                                                                                                                        |            |
| EtherNet/IP™ (CIP)             |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   | X                                 | X                                            |                                                        |                                             | X                                                                                                                                                                                                                      |            |
| General -Linear                |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
| General -Synchronous           |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
| Motor-Linear                   |                                                                                                                                               |                                                             |                                                                                |                                                                                       | X                             | X                                            | X                                         | X                                      |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
| Top Level                      |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        | UserDefi nedIntegerData0          | UserDefinedIntegerData1           | UserDefinedIntegerReal0           |                                              | UserDefinedIntegerReal0                                | UserDefinedIntegerReal1                     | 240 REAL R/W Pole pitch Range: 2…200 mm X TCP segment                                                                                                                                                                  |            |
|                                | Range: -10,000…+10,000 UU/sec.                                                                                                                | See  Homing Category  on page 111 .                         | Do not assign to A1, A2, A3, or C3 as these inputs have predefined  functions. |                                                                                       | Range: 0…10 m/s               | Range: 1…1000 N/A rms                        |                                           | Range: 0.4…40 µm                       |                                   |                                   |                                   | UserDefinedIntegerData0                      |                                                        |                                             | Bit 7 indicates battery level has fallen to 3.1V DC or less. Bit 6 indicates battery level has fallen to 2.5V DC or less and absolute data may not be valid. Maximum delay time before sending an acknowledgement to a |            |
|                                |                                                                                                                                               |                                                             |                                                                                |                                                                                       | Range: 0…100 kg               |                                              | EMF constant, Ke Range: 1…500V rms/m/s    |                                        |                                   |                                   |                                   | UserDefinedIntegerReal1                      | UserDefinedIntegerData1                                |                                             |                                                                                                                                                                                                                        |            |
| Access Description Value/Notes | For homing methods that use one velocity setting, this  used as the slow velocity. Typically, this tag is used to creep to a homing position. | Defines the type of homing to be performed. See  page 113 . |                                                                                | The digital input that should be used as a home switch for appropriate homing method. |                               |                                              | 245 REAL R/W Linear motor voltage or back | 246 REAL R/W Linear encoder resolution | assembly                          | assembly                          | assembly                          | 253 DINT R/W Datalink A for output  assembly | assembly  255 DINT R/W Datalink C for output  assembly |                                             |                                                                                                                                                                                                                        |            |
|                                | tag is used as the velocity.  For homing methods that use two velocity settings(fast and slow), this tag is used as the slow velocity         | Table 64 on                                                 |                                                                                |                                                                                       | 243 REAL R/W Motor block mass | 244 REAL R/W Linear motor force constant, Kf |                                           |                                        |                                   |                                   | 251 DINT R/W Datalink C for input |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
|                                |                                                                                                                                               |                                                             |                                                                                |                                                                                       | 242 REAL R/W Linear speed     |                                              |                                           |                                        | 249 DINT R/W Datalink A for input | 250 DINT R/W Datalink B for input |                                   |                                              |                                                        | 256 DINT R/W Datalink D for output assembly | 264 DINT R/W TCP reply delay value                                                                                                                                                                                     |            |
|                                |                                                                                                                                               |                                                             |                                                                                | 234 DINT R/W                                                                          |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
| Data Type                      | 231 REAL R/W                                                                                                                                  | 232 DINT R/W                                                |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
| ID                             |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
|                                | 230 REAL R/W                                                                                                                                  |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        |            |
|                                |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   | 252 DINT R/W Datalink D for input assembly   | 254 DINT R/W Datalink B for output                     |                                             |                                                                                                                                                                                                                        |            |
|                                |                                                                                                                                               |                                                             |                                                                                |                                                                                       |                               |                                              |                                           |                                        |                                   |                                   |                                   |                                              |                                                        |                                             |                                                                                                                                                                                                                        | 247 DINT R |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

|                                | Faults                                                                                                                                     |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Monitor                        |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Homing                         |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Indexing                       |                                                                                                                                            | X                                                                             |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Dynamics                       |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Position Limits                |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Velocity Limits                |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Analog I/O                     |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Digital I/O                    |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          | X                                                                                                                                                                                                                      |
| EtherNet/IP™ (CIP)             |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| EtherNet                       |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| General -Linear                |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| General -Synchronous           | X X                                                                                                                                        |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Motor-Linear                   |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Motor-Synchronous              |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
| Top Level                      |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |
|                                | 0 = Auto Tune 1 = EtherNet/IP External Reference2 = Master Gearing3 = Step and Direction4 = Analog Velocity5 = Analog Current 6 = Indexing | 0 = Disable 1 = Enable                                                        | 0 to 1 transition = Executes indexing 1 to 0 transition = No effect on index effect on indexing | Cycle this tag value between 0 and 1 before the time-out period isreached to prevent a watchdog time-out and fault.                                                         | A value of 1 enables the watchdog mechanism.                                                                  | Range: 10 …1000 ms                                                                                                                                                       | 0 = Not Assigned1 = Abort Index2 = (Reserved)3 = Start Index4 = Define Home5 = Abort Homing6 = Start Homing7 = Fault Reset8 = Index Select 09= Index Select 110 = Index Select 211 = Index Select 312 = Index Select 4 |
| Access Description Value/Notes | 266 DINT R/W Sets the mode of operation for the drive                                                                                      | Enable Auto Start index function for Indexing mode when drive becomes enabled | Upon transition from 0 to  1 the drive will begin  executing index.                             | Value in this tag must change  before time-out time is reached, otherwise the faul t action is initiated. Function can be used with EtherNet/IP explicit messaging control. | Enables the communication watchdog function.Function can be used with EtherNet/IP explicit messaging control. | Time-out value. Function to be used with EtherNet/IPexplicit messaging control. This tag sets the window of time before the time-out  occurs and the fault is generated. | 624 DINT R/W Programmable input assignment for input A4                                                                                                                                                                |
| ID                             |                                                                                                                                            |                                                                               |                                                                                                 |                                                                                                                                                                             | 270 DINT R/W                                                                                                  | 271 DINT R/W                                                                                                                                                             |                                                                                                                                                                                                                        |
| Data Type                      |                                                                                                                                            | 267 DINT R/W                                                                  | 268 DINT R/W                                                                                    | 269 DINT W                                                                                                                                                                  |                                                                                                               |                                                                                                                                                                          |                                                                                                                                                                                                                        |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

<!-- image -->

| MotionView Page Used               | Faults               |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
|------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MotionView Page Used               | Monitor              |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Homing               |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Indexing             |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Dynamics             |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Position Limits      |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Velocity Limits      |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Analog I/O           |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Digital I/O          | X                                                                                                                                                                                                                      | X                                                                                                                                                                                                                      | X                                                                                                                                                                                                                      |
| MotionView Page Used               | EtherNet/IP™ (CIP)   |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | EtherNet             |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | General -Linear      |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | General -Synchronous |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Motor-Linear         |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Motor-Synchronous    |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| MotionView Page Used               | Top Level            |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
|                                    |                      | 0 = Not Assigned1 = Abort Index2 = (Reserved)3 = Start Index4 = Define Home5 = Abort Homing6 = Start Homing7 = Fault Reset8 = Index Select 09= Index Select 110 = Index Select 211 = Index Select 312 = Index Select 4 | 0 = Not Assigned1 = Abort Index2 = (Reserved)3 = Start Index4 = Define Home5 = Abort Homing6 = Start Homing7 = Fault Reset8 = Index Select 09= Index Select 110 = Index Select 211 = Index Select 312 = Index Select 4 | 0 = Not Assigned1 = Abort Index2 = (Reserved)3 = Start Index4 = Define Home5 = Abort Homing6 = Start Homing7 = Fault Reset8 = Index Select 09= Index Select 110 = Index Select 211 = Index Select 312 = Index Select 4 |
| ID  Access Description Value/Notes |                      | 625 DINT R/W Programmable input assignment for input B1                                                                                                                                                                | 626 DINT R/W Programmable input assignment for input B2                                                                                                                                                                | 627 DINT R/W Programmable input assignment for input B3                                                                                                                                                                |
| Data Type                          |                      |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

|                                           | Faults                                                                                                                                                                                                                 |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Monitor                                   |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Homing                                    |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Indexing                                  |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Dynamics                                  |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Position Limits                           |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Velocity Limits                           |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Analog I/O                                |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Digital I/O                               | X                                                                                                                                                                                                                      | X                                                                                                                                                                                                                      | X                                                                                                                                                                                                                      |
| EtherNet/IP™ (CIP)                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| EtherNet                                  |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| General -Linear                           |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| General -Synchronous                      |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Motor-Linear                              |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Motor-Synchronous                         |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
| Top Level                                 |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |
|                                           | 0 = Not Assigned1 = Abort Index2 = (Reserved)3 = Start Index4 = Define Home5 = Abort Homing6 = Start Homing7 = Fault Reset8 = Index Select 09= Index Select 110 = Index Select 211 = Index Select 312 = Index Select 4 | 0 = Not Assigned1 = Abort Index2 = (Reserved)3 = Start Index4 = Define Home5 = Abort Homing6 = Start Homing7 = Fault Reset8 = Index Select 09= Index Select 110 = Index Select 211 = Index Select 312 = Index Select 4 | 0 = Not Assigned1 = Abort Index2 = (Reserved)3 = Start Index4 = Define Home5 = Abort Homing6 = Start Homing7 = Fault Reset8 = Index Select 09= Index Select 110 = Index Select 211 = Index Select 312 = Index Select 4 |
| Data Type  Access Description Value/Notes | 628 DINT R/W Programmable input assignment for input B4                                                                                                                                                                | 629 DINT R/W Programmable input assignment for input C1                                                                                                                                                                | 630 DINT R/W Programmable input assignment for input C2                                                                                                                                                                |
| ID                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |                                                                                                                                                                                                                        |

Table 87 - Kinetix® 300 Drive Tag Numbers (Continued)

<!-- image -->

|                                | Faults                                                                                                                                                                                                                 |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      | X                                                            |                                                                                                                                                                                              |                                                                                                        |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------|-------------------------------------|--------------------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Monitor                        |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Homing                         |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Indexing                       |                                                                                                                                                                                                                        | X                                                    |                                                             |                                                             | X                                                                    |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Dynamics                       |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Position Limits                |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Velocity Limits                |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Analog I/O                     |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Digital I/O                    | X                                                                                                                                                                                                                      |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   | X                                                                                                                                                                               | X                                                                                                                                                                                    |                                                              |                                                                                                                                                                                              | X                                                                                                      |
| EtherNet/IP™ (CIP)             |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| EtherNet                       |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| General -Linear                |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| General -Synchronous           |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Motor-Linear                   |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
|                                |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      | X                                 |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Motor-Synchronous              |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      | X X                                 | X X                                  |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
| Top Level                      |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |
|                                | 0 = Not Assigned1 = Abort Index2 = (Reserved)3 = Start Index4 = Define Home5 = Abort Homing6 = Start Homing7 = Fault Reset8 = Index Select 09= Index Select 110 = Index Select 211 = Index Select 312 = Index Select 4 |                                                      | Uses the AbortDecel parameter (#178) to go to zero velocity | Uses the AbortDecel parameter (#178) to go to zero velocity | 0…31                                                                 | Range: 0…10000000 C/W               | Range: 0…10000000 W-s/C              | Range: 0…100 A                    | Motor brake engage delay, ms                                                                                                                                                    | Motor brake release delay, ms                                                                                                                                                        | Same fault code that is displayed on the servo drive display | Writing a non-zero value to this fi eld resets encoder detected faults on Kinetix TL (Bulletin TLY) moto rs without having to perform a power cycle once the failure condition is corrected. | 0 = Normally open input (active high) 1 = Normally closed input (active low)                           |
| Access Description Value/Notes | 631 DINT R/W Programmable input assignment for input C4                                                                                                                                                                | 632 DINT W Indexing starts from index specified 0…31 |                                                             | 634 DINT R Aborts homing in progress                        | Index currently executing. This tag is valid only in  Indexing mode. | 646 REAL R/W Thermal resistance, Rt | 647 REAL R/W Thermal capacitance, Ct |                                   | For the digital output that has been assigned to thebrake function, this is the delay from when the drive is disabled to the time that  motion is stopped and brake is engaged. | For the digital output that has been assigned to thebrake function, this is the delay from when the drive isenabled to the time that motion is allowed to begin (brake is released). |                                                              | 654 DINT WO Reset ABS encoder error method                                                                                                                                                   | Overtravel Input Polarity  (1) . Controls the active level of  the exception on the overtravel inputs. |
|                                |                                                                                                                                                                                                                        |                                                      | 633 DINT R Aborts index in progress                         |                                                             |                                                                      |                                     |                                      | 650 REAL R/W Intermittent current |                                                                                                                                                                                 |                                                                                                                                                                                      | 653 DINT RO Fault E-code                                     |                                                                                                                                                                                              |                                                                                                        |
| Data Type                      |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             | 637 DINT R                                                           |                                     |                                      |                                   | 651 DINT R/W                                                                                                                                                                    | 652 DINT R/W                                                                                                                                                                         |                                                              |                                                                                                                                                                                              | 668 DINT W                                                                                             |
| ID                             |                                                                                                                                                                                                                        |                                                      |                                                             |                                                             |                                                                      |                                     |                                      |                                   |                                                                                                                                                                                 |                                                                                                                                                                                      |                                                              |                                                                                                                                                                                              |                                                                                                        |

| MotionView Page Used           | Faults                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                          | und by                     |                           |                     |                    |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|---------------------------|---------------------|--------------------|
| Monitor                        |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| Homing                         |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| Indexing                       |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| Dynamics                       |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| Position Limits                |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| Velocity Limits                |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| Analog I/O                     |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| Digital I/O                    | when this firmware is used on hardware revision 1B. The hardware revision can be fo                                                                                                                                                                                      |                                                                                                                                                                                                          |                            |                           |                     |                    |
| EtherNet/IP™ (CIP)             |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| EtherNet                       |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| General -Linear                |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| General -Synchronous           |                                                                                                                                                                                                                                                                          | X                                                                                                                                                                                                        | X                          | X                         |                     |                    |
| Motor-Linear                   |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           | X                   | X                  |
| Motor-Synchronous              |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
| Top Level                      | inputs as normally open or normally closed                                                                                                                                                                                                                               |                                                                                                                                                                                                          |                            |                           |                     |                    |
| Access Description Value/Notes | When the registration digital in put becomes asserted, the motor position is captured, copied into th e Registered Position field in the Input Assembly, and the Registration Captured bit in the InputAssembly transitions from 0 to 1. d software has been enhanced to | Rotary Unwind is designed only for these modes: ion with Blended or Registered moves is not supported.Attempting to use these move optionswithout having configured rotary unwind will result in a drive |                            |                           |                     | 0 = µm1 = m2 = in. |
|                                | allow the configuration of the                                                                                                                                                                                                                                           | 0 = Disable1 = Enable Rotary AbsoluteRotary IncrementalRotary Shortest PathRotary PositiveRotary Negative Rotary unwind mode in conjunct fault.                                                          | Range: 0…1000000           | Range: 0…400%             | Range: 1…1000000    |                    |
|                                | Registration Arming  (1)  A 0-to-1 transition of this parameter arms the registration capture if the drive isnot currently in a registration based move. 667 DINT W Registration Arming (1) A 0-to-1 tra parameter arms the registration canot currently in a registration based  670 DINT R/W Enable rotary unwind. 671 REAL R/W User units per unwind. 672 REAL R/W Current output clamp.  676 REAL R/W User units scaling. 678 DINT R/W Measure units. (1) The hardware overtravel configuration in the MotionView OnBoard soft reading the last four digits of the Type field on the carton label. Table 87 - Kinetix® 300 Drive Tag Numbers (Continued) ID Data Type Access Description                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           |                     |                    |
|                                | (1) The hardware overtravel configuration in the MotionView OnBoar                                                                                                                                                                                                       | 670 DINT R/W Enable rotary unwind.                                                                                                                                                                       | R/W User units per unwind. | R/W Current output clamp. | User units scaling. | Measure units.     |
|                                |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            |                           | R/W                 |                    |
| Data Type                      | 667 DINT W                                                                                                                                                                                                                                                               |                                                                                                                                                                                                          | 671 REAL                   |                           | REAL                | DINT R/W           |
| ID                             |                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                          |                            | 672 REAL                  | 676                 | 678                |

## Index Base Addressing

There are 11 tags per index and 32 indexes total.

Table 88 - Index Base Address

Index x = Base Address (B) Index x = Base Address (B)

Index 0 = 272 Index 16 = 448

Index 1 = 283 Index 17 = 459

Index 2 = 294 Index 18 = 470

Index 3 = 305 Index 19 = 481

Index 4 = 316 Index 20 = 492

Index 5 = 327 Index 21 = 503

Index 6 = 338 Index 22 = 514

Index 7 = 349 Index 23 = 525

Index 8 = 360 Index 24 = 536

Index 9 = 371 Index 25 = 547

Index 10 = 382 Index 26 = 558

Index 11 = 393 Index 27 = 569

Index 12 = 404 Index 28 = 580

Index 13 = 415 Index 29 = 591

Index 14 = 426 Index 30 = 602

Index 15 = 437 Index 31 = 613

Table 89 - Indexing Tag Numbers

| ID Data Type   |                                                                                                                 | Access Description Value/Notes                                                              |
|----------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
|                | B+0 DINT R/W Index move type of absolute, incremental, registration or blended incremental for index 0…31.      | 0 = Absolute 1 = Incremental 2 = Registered Absolute 3 = Registered Incremental 4 = Blended |
|                | B+1 DINT R/W Trapezoidal or S-curve move for index 0…31.                                                        | 0 = Trapezoidal 1 = S-Curve                                                                 |
|                | B+2 DINT R/W Maximum distance to move for index 0…31.                                                           | Distance (how far to move)                                                                  |
|                | B+3 DINT R/W Relative distance to move after registration event for registration types for index 0…31.          | Move distance after registration                                                            |
|                | B+4 DINT R/W Batch count. Number of times to repeat index before executing for index 0…31. Range: 0…1000 counts |                                                                                             |
|                | B+5 DINT R/W Dwell time to remain at current position before executing for index 0…31 Range: 0…10,000 ms        |                                                                                             |
|                | B+6 DINT R/W Maximum velocity in UU while in motion for index 0…31                                              | Velocity (speed when moving towards new position)                                           |
|                | B+7 DINT R/W Maximum acceleration in UU while in motion for index 0…31                                          | Acceleration (how quickly towards configured velocity)                                      |
|                | B+8 DINT R/W Maximum deceleration in UU while in motion for index 0…31                                          | Deceleration (how quickly towards zero velocity from configured velocity)                   |
|                | B+9 DINT R/W Next index to execute if action so indicates for index 0…31                                        | Next Index (next index to execute if any)                                                   |
|                | B+10 DINT R/W Action to execute upon completing motion for index 0…31                                           | 0 - Stop 1 = Wait for Start 2 = Next Index                                                  |

## Explicit Messaging Data Types

## MicroLogix Explicit Messaging

You can use MicroLogix™ CIP Generic (MSG) instructions, also known as explicit messages, to read and write to the drive ID tags over the EtherNet/IP™ network. This capability is present in the MicroLogix 1100 series B and MicroLogix 1400 controllers. You can write to read/write (R/W) ID tags, however, read (R) ID tags are read-only. For the complete list of Kinetix® 300 ID tags, see Appendix C on page 199 .

| Topic                                 |   Page |
|---------------------------------------|--------|
| Explicit Messaging Data Types         |    213 |
| Explicit Messaging Data Type Examples |    214 |

ID tags are designated as either DINT, REAL, or string data types. The MicroLogix controller uses long file elements, such as L12:0 for DINT data types, floating point file elements, such as F13:0, for Real data types, and string file elements, such as ST14:0 for string data types.

The attribute value is used to designate the data format as DINT, REAL, string, and the memory location as volatile or nonvolatile.

Table 90 - Data Type Attributes

| Attribute Format Memory Stored In   |
|-------------------------------------|
| 0 DINT Volatile                     |
| 1 DINT Nonvolatile                  |
| 2 REAL Volatile                     |
| 3 REAL Nonvolatile                  |
| 4 String Volatile                   |
| 5 String Nonvolatile                |

Explicit messaging lets DINT data types to be read into and written from long file elements directly and Real data types to be read into and written from floating point file elements directly. String data types must be read into integer file elements, such as N11:0, by the MSG instruction and then copied into a string file element. Similarly strings must be copied into integer file elements first before being written by the MSG instruction.

<!-- image -->

## Explicit Messaging Data Type Examples

## IMPORTANT

For each CIP Generic message (MSG) instruction, you must use both a unique message file element, for example MG9:0 and a unique extended routing information file element, for example RIX10:0. The routing information file element stores not only the path to the destination Kinetix 300 drive IP address, but also the specific Class/Instance/Attribute settings.

This section provides examples for DINT, REAL, and String data types.

## DINT Data Type Examples

In this example, the instance decimal is ID tag 73 (bus voltage).

Figure 105 - Reading DINT from Volatile Memory

<!-- image -->

In this example, the instance decimal is ID tag 232 (homing method).

Figure 106 - Writing DINT into Nonvolatile Memory

<!-- image -->

## REAL Data Type Examples

In this example, the instance decimal is ID tag 183 (phase current).

Figure 107 - Reading REAL from Volatile Memory

<!-- image -->

In this example, the instance decimal is ID tag 58 (zero speed window).

Figure 108 - Writing REAL into Nonvolatile Memory

<!-- image -->

## String Data Type Examples

In this example, the instance decimal is ID tag 3 (drive serial number).

Figure 109 - Reading String from Volatile Memory

<!-- image -->

<!-- image -->

In this example, the instance decimal is ID tag 2 (drive symbolic name).

Figure 110 - Writing String into Nonvolatile Memory

<!-- image -->

<!-- image -->

## Notes:

## Modes of Operation

## Overtravel Inputs

The Kinetix® 300 drive has built-in hardware overtravel inputs. These digital inputs are positive and negative relative to the direction of movement on your axis. The overtravel limits are switches wired to the drive's inputs and mounted at the physical extremes (positive/negative) of your axis to indicate a nomovement condition for your axis.

| Topic                      |   Page |
|----------------------------|--------|
| Modes of Operation         |    219 |
| Overtravel Hardware Inputs |    220 |
| Operation                  |    221 |
| Overtravel Fault Recovery  |    222 |

The operation of the Kinetix 300 drives overtravel limits is only applicable in Positioning mode. You can also use non-positioning modes, but they must work with an external controller or PLC.

Table 91 - Overtravel Input Modes of Operation

<!-- image -->

| Positioning Modes                                                                                                                         | Non-positioning Modes                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Indexing mode                                                                                                                             | EtherNet/IP™ External Reference mode 0 = Current (torque) Reference 1 = Velocity Reference |
| EtherNet/IP External Reference mode 2 = Incremental Position 3 = Absolute Position 4 = Incremental Registration 5 = Absolute Registration | Analog Velocity Input mode                                                                 |
| Jog Profiler mode                                                                                                                         | Analog Current Input mode                                                                  |

<!-- image -->

Figure 111 - Modes of Operation in MotionView Software

<!-- image -->

## Overtravel Hardware Inputs

Overtravel inputs are dedicated inputs and cannot be used for anything else.

Table 92 - Overtravel Pin Assignments

| IOD Pin Description              | Signal   |
|----------------------------------|----------|
| IOD-28 Positive overtravel input | IN_A2    |
| IOD-27 Negative overtravel input | IN_A1    |

The overtravel inputs are edge triggered and once the overtravel limit is exceeded, the drive will perform the configured shutdown. Overtravel checking is configured via MotionView software under DriveIP &gt;IO &gt; Digital IO &gt; Hard Limit Switches Action.

Overtravel inputs can be programed for normally open or normally closed operation. Use EtherNet/IP Explicit Messaging tag ID 668 to modify this parameter.

Figure 112 - Overtravel Configuration in MotionView Software

<!-- image -->

The default action is Not Assigned. These actions are configured via the pulldown menu:

- Disable and Coast - immediately disables the drive upon detecting an overtravel condition. Disable and Coast is the only stopping action available when overtravel is tripped in Analog Velocity Mode.
- Decel and Disable - uses the Abort Decel rate to stop the servo and then disable the drive. Decel and Disable is not available for Analog Velocity Mode.

## Operation

If the drive is in a position operating mode, the overtravel limits are functional and will generate an error when the overtravel is reached. The drive will not allow axis movement in the direction of the overtravel limit until after the overtravel fault is reset. Only movement in the opposite direction is allowed.

If the drive is in a non-positioning mode of operation, the overtravel limits are functional and will generate an error when the overtravel is reached. However, it is up to the controller (via programming) to manage recovery and axis position after an overtravel fault. The drive will not limit axis movement once the fault has been cleared.

## IMPORTANT

If an overtravel fault is reset and the drive is enabled while the axis is on or beyond the overtravel limit, a runaway condition could occur when using the overtravel limits in a non-positioning mode.

An overtravel fault registers when the drive is enabled and motion causes the axis to pass the overtravel switch. Once the overtravel is triggered, the drive performs the configured Hard Limit Switches Action and drive is disabled.

An example of this is if the drive was in EtherNet/IP drive mode, had an overtravel fault, and the overtravel fault is reset. If a value still exists in the CommandCurrentOrVelocity parameter of the drive Add-on Profile, and that value is in the incorrect direction, the axis continues to move in that direction regardless of overtravel condition.

Figure 113 - MotionView Monitor Category

<!-- image -->

## Overtravel Fault Recovery

Follow these steps to recover from an overtravel fault condition while in a Positioning mode.

1. Reset the drive to clear the overtravel fault, either through MotionView software or via logic.

Typically, the overtravel input is still active after the reset, because the axis is still on the limit switch.

2. Enable the servo.
3. Move the axis off the limit switch.

The drive allows a position-based move in the direction opposite the limit switch. For example, if the axis is on a positive limit switch, it can move in a negative direction or if the axis is on a negative limit switch, it can move in a positive direction.

Once the axis is moved off the limit switch, the input goes low and the motion routine can begin again.

Follow these steps to recover from an overtravel fault condition while in a nonpositioning mode.

1. Change the motion command reference (velocity or current) to a value opposite the axis overtravel is on (set to a negative value if on the positive limit and vice versa if on the negative limit).

IMPORTANT

The drive will not limit motion in the direction of the overtravel when in a non-positioning mode, provided the overtravel input is still active and the initial overtravel fault has been reset.

2. Reset the drive to clear the overtravel fault, either through MotionView software or via logic.

Typically, the overtravel input is still active after the reset, because the axis is still on the limit switch.

3. Enable the servo.

## IMPORTANT

With a nonzero command reference, motion begins immediately upon Enable when in a current or velocity mode of operation.

4. Verify that the user program code permits continued axis motion and manages the motion routine.

## Leakage Current Specifications

This appendix contains leakage current specifications to be expected for center-grounded wye and corner-grounded delta input power configurations for Kinetix® 300 drives when installed with or without a mains AC line filter.

<!-- image -->

Table 93 - Leakage Current Specifications

| Mains Input - High Line (Nominal +10%) Fault Leakage (Calculated)  Single-phase  Three-phase   | Corner Ground  Delta  No External  Filter   |                                          |                       |                       |                  |                                     |                                     | k— — —             | —                  |                       | —                     |                       | 31 mA pk           | k— — —             | —                  |                    | 31 mA pk           |                    | —                  | 2 mA pk —          | 30 mA pk           | —                  |                    |
|------------------------------------------------------------------------------------------------|---------------------------------------------|------------------------------------------|-----------------------|-----------------------|------------------|-------------------------------------|-------------------------------------|--------------------|--------------------|-----------------------|-----------------------|-----------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|--------------------|
| Mains Input - High Line (Nominal +10%) Fault Leakage (Calculated)  Single-phase  Three-phase   |                                             | Filter                                   |                       |                       |                  | k— — —                              | k— — —                              | —                  |                    | k— — —                | 1 mA pk —             |                       | —                  |                    | 1 mA pk —          | —                  |                    |                    | —                  | k— — —             |                    |                    | 13 mA pk —         |
| Mains Input - High Line (Nominal +10%) Fault Leakage (Calculated)  Single-phase  Three-phase   | Center Ground WYE                           | No External Filter With External         | k— — —                | k— — —                | k— — —           |                                     |                                     |                    |                    | 2 mA pk —             | —                     | —                     |                    | 3 mA pk —          | —                  | —                  | k— — —             | 3 mA pk —          | —                  | —                  |                    | 3 mA pk —          | —                  |
| Mains Input - High Line (Nominal +10%) Fault Leakage (Calculated)  Single-phase  Three-phase   |                                             |                                          | 7  m A  p             | 8  m A  p             | 7  m A  p        | 8  m A  p                           | 2 9  m A  p                         | 2 8  m A  p        | 29 mA pk —         | 2 0  m A  p —         | —                     |                       | 1 9  m A  p        | —                  | —                  |                    | 1 9  m A  p        | —                  | —                  | 2 0  m A  p        | —                  |                    | —                  |
|                                                                                                | Corner Ground  Delta                        | No External  Filter                      |                       |                       |                  |                                     |                                     | —                  |                    | —                     |                       | 29 mA pk —            |                    |                    | —                  | 28 mA pk —         |                    | —                  |                    | 28 mA pk —         |                    | —                  |                    |
|                                                                                                |                                             | No External Filter With External  Filter |                       |                       | k— — —           | k— — —                              | k— — —                              |                    | —                  | k— — —                | 1 mA pk —             |                       | k— — —             |                    | 1 mA pk —          |                    | k— — —             |                    | 2 mA pk —          |                    |                    |                    | 12 mA pk —         |
|                                                                                                | Center Ground WYE                           |                                          | k— — —                | k— — —                |                  |                                     | k— — —                              |                    |                    | 2 mA pk —             |                       | ———                   |                    | 2 mA pk —          |                    | ———                |                    | 2 mA pk —          |                    | ———  k— — —        |                    | 3 mA pk —          |                    |
|                                                                                                |                                             |                                          | 7  m A  p             | 7  m A  p             | 6  m A  p 7  m A | p 2 7  m A  p                       | 2 6  m A  p                         |                    | 26 mA pk —         | 1 8  m A  p           | — —                   |                       | 1 8  m A  p        |                    | — —                |                    | 1 7  m A  p        |                    | — —                | 1 9  m A  p        |                    |                    | — —                |
|                                                                                                | Number of Phases                            |                                          | 1                     |                       |                  |                                     |                                     |                    | 1                  | 3 —                   | 3 —                   | 3 —                   | 1  3 —             | 1  3 —             | 1  3 —             | 1  3 —             | 1  3 —             | 1  3 —             | 1  3 —             |                    | 3 —                | 3 —                | 3 —                |
|                                                                                                | Continuous Output Current  (rms)            |                                          |                       |                       |                  |                                     | 4 A                                 | 8 A                |                    |                       |                       |                       | 4 A                |                    |                    |                    | 8 A                |                    |                    | 12 A 1             | 12 A 1             | 12 A 1             | 12 A 1             |
|                                                                                                | Voltage (rms)                               | 120V 2 A                                 | 240V                  | 120V 4 A              | 240V             | 240V 2 A                            |                                     |                    | 240V 2 A           | 240V 2 A              | 240V 2 A              | 240V 2 A              | 240V 2 A           | 240V 2 A           | 240V 2 A           | 240V 2 A           | 240V 2 A           | 240V 2 A           | 240V 2 A           | 240V 2 A           | 240V 2 A           | 240V 2 A           | 240V 2 A           |
|                                                                                                | Cat. No. Drive Description AC Input         | single-phase, doubler                    | single-phase, doubler | single-phase, doubler |                  | single-phase, withintegrated filter | single-phase, withintegrated filter | single/three-phase | single/three-phase | single/three-phase    | single/three-phase    | single/three-phase    | single/three-phase | single/three-phase | single/three-phase | single/three-phase | single/three-phase | single/three-phase | single/three-phase | single/three-phase | single/three-phase | single/three-phase | single/three-phase |
|                                                                                                |                                             |                                          | 2097-V31PR0 120/240V, | 2097-V31PR2           |                  | 2097-V32PR0 208/240V,               | 2097-V32PR2                         | 2097-V32PR4        |                    | 2097-V33PR1 208/240V, | 2097-V33PR1 208/240V, | 2097-V33PR1 208/240V, | 2097-V33PR3        | 2097-V33PR3        | 2097-V33PR3        | 2097-V33PR5        | 2097-V33PR5        | 2097-V33PR5        | 2097-V33PR5        | 2097-V33PR6        | 2097-V33PR6        | 2097-V33PR6        | 2097-V33PR6        |

Table 93 - Leakage Current Specifications (Continued)

| Mains Input - High Line (Nominal +10%) Fault Leakage (Calculated)   | Corner Ground Delta                    | No External Filter                  | —            |                       | —           |           | —           |           |
|---|----------------------------------------|-------------------------------------|--------------|-----------------------|-------------|-----------|-------------|-----------|
| Mains Input - High Line (Nominal +10%) Fault Leakage (Calculated)   | Three-phase Center Ground WYE          | Filter                              |              | 5 mA pk —             |             | 4 mA pk — |             | 5 mA pk — |
| Mains Input - High Line (Nominal +10%) Fault Leakage (Calculated)   | Three-phase Center Ground WYE          | No External Filter With External    | 17 mA pk —   | —                     | 17 mA pk —  | —         | 18 mA pk —  | —         |
| Mains Input - High Line (Nominal +10%) Fault Leakage (Calculated)   | Single-phase                           | No External Filter With External    | —            | —                     | —           | —         | —           | —         |
| Mains Input - Nominal Line Typical Leakage (Calculated)   | Center Ground WYE  Corner Ground Delta | No External Filter                  | —            |                       | —           |           | —           |           |
| Mains Input - Nominal Line Typical Leakage (Calculated)   | Three-phase                            | Filter                              |              | 5 mA pk —             |             | 3 mA pk — |             | 4 mA pk — |
| Mains Input - Nominal Line Typical Leakage (Calculated)   | Three-phase                            | No External Filter With External    | 16 mA pk —   |                       | 15 mA pk —  |           | 16 mA pk —  |           |
| Mains Input - Nominal Line Typical Leakage (Calculated)   | Single-phase                           | No External Filter With External    |              | — —                   | —           | — —       | —           | — —       |
| Mains Input - Nominal Line Typical Leakage (Calculated)   |                                        | Number ofPhases                     |              | 480V 2 A 3 —          |             |           |             |           |
| Mains Input - Nominal Line Typical Leakage (Calculated)   |                                        | ContinuousOutput Current            | (rms)        |                       | 4 A         |           | 6 A         |           |
| Mains Input - Nominal Line Typical Leakage (Calculated)   |                                        |                                     | Voltage(rms) |                       |             |           |             |           |
| Mains Input - Nominal Line Typical Leakage (Calculated)   |                                        | Cat. No. Drive Description AC Input |              | three-phase           |             |           |             |           |
| Mains Input - Nominal Line Typical Leakage (Calculated)   |                                        |                                     |              | 2097-V34PR3 400/480V, | 2097-V34PR5 |           | 2097-V34PR6 |           |

## Notes:

| Numerics                                            | category 3                                                   | category 3                                                   |
|-----------------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| 120/240V single-phase input power  176              | requirements  162 stop category definitions  162             | requirements  162 stop category definitions  162             |
| 120V single-phase input power  175                  | CE                                                           | CE                                                           |
| 1766-L32BXB  186                                    | compliance  14 ,  61                                         | compliance  14 ,  61                                         |
| 1766-L32BXBA  186                                   | comply with  166                                             | comply with  166                                             |
| 2097 master gearing example  187                    | conformity  166                                              | conformity  166                                              |
| 2097 with Kinetix LDAT linear thruster  183         | invalidate compliance  61 166                                | invalidate compliance  61 166                                |
| 240/480V three-phase input power  177               | meet requirements                                            | meet requirements                                            |
|                                                     | certification TÜV Rheinland  161                             | certification TÜV Rheinland  161                             |
| A                                                   | user responsibilities  162 circuit breaker                   | user responsibilities  162 circuit breaker                   |
| about this publication  9                           | selection  17                                                | selection  17                                                |
| AC input power                                      | circuit breaker specifications                               | circuit breaker specifications                               |
| pinouts  36                                         | Kinetix 300  18                                              | Kinetix 300  18                                              |
| actuators                                           | clamp  73                                                    | clamp  73                                                    |
| interconnect diagram                                | clean zone  25                                               | clean zone  25                                               |
| Kinetix MPAI  184                                   | clear faults  158                                            | clear faults  158                                            |
| Kinetix MPAR  184                                   | clearance requirements                                       | clearance requirements                                       |
| Kinetix MPAS  183 Kinetix TLAR  185                 | communication category  89                                   | communication category  89                                   |
| 10                                                  |                                                              |                                                              |
| additional resources                                | configuration                                                | configuration                                                |
| add-on profiles  130                                | add-on profiles                                              | add-on profiles                                              |
| analog current  142 ,  148                          | controller properties  131                                   | controller properties  131                                   |
| analog I/O category  92                             | date and time tab  132                                       | date and time tab  132                                       |
| analog output  44                                   | drive  134                                                   | drive  134                                                   |
| analog reference  43                                | drive mode                                                   | drive mode                                                   |
| analog velocity  142 ,  148 ,  186 apply power  137 | explicit messaging  148 drive parameter tools                | explicit messaging  148 drive parameter tools                |
| auto tune  142                                      | changing  147                                                | changing  147                                                |
|                                                     | viewing                                                      | viewing                                                      |
|                                                     | 145 drive parameters                                         | 145 drive parameters                                         |
| B                                                   | 145 drive properties  135 Ethernet module                    | 145 drive properties  135 Ethernet module                    |
| back-up power  47 pinouts  36                       | ControlLogix  133 module properties  134                     | ControlLogix  133 module properties  134                     |
| block diagrams                                      | Ethernet port CompactLogix  132                              | Ethernet port CompactLogix  132                              |
| power block diagram  189                            |                                                              |                                                              |
| voltage-doubler block diagram  190                  | module properties  133 EtherNet/IP  126                      | module properties  133 EtherNet/IP  126                      |
| bonding  23                                         | DHCP  129                                                    | DHCP  129                                                    |
| EMI (ElectroMagnetic Interference)                  |                                                              |                                                              |
| 22 high frequency energy  24 24                     | dynamic address  static address  127 EtherNet/IP module  131 | dynamic address  static address  127 EtherNet/IP module  131 |
| subpanels  188                                      |                                                              |                                                              |
| brake currents                                      | keypad input  124                                            | keypad input  124                                            |
| buffered encoder outputs  46                        | master gearing  144 select drive mode                        | master gearing  144 select drive mode                        |
| build your own cables  56                           | 142 status indicators  125                                   | 142 status indicators  125                                   |
|                                                     | test the axis  138 tune the axis  139                        | test the axis  138 tune the axis  139                        |
|                                                     | configuration system variables  145 connect                  | configuration system variables  145 connect                  |
| cables                                              |                                                              |                                                              |
| build your own cables                               | Ethernet  79                                                 | Ethernet  79                                                 |
| Ethernet cable length  79 length, CE  16            | external shunt resistor  feedback  74 I/O  74                | external shunt resistor  feedback  74 I/O  74                |
| motor feedback  motor power  69                     |                                                              |                                                              |
| shield clamp  73                                    | motor shield clamp                                           | motor shield clamp                                           |
| 13                                                  | designators  32                                              | designators  32                                              |
|                                                     | connector                                                    | connector                                                    |
| catalog numbers                                     |                                                              |                                                              |
|                                                     | C                                                            | C                                                            |
|                                                     | 129                                                          | 129                                                          |
|                                                     | 56                                                           | 56                                                           |
|                                                     | 74                                                           | 74                                                           |
|                                                     | locations  32 ,  165                                         | locations  32 ,  165                                         |
|                                                     | 73                                                           | 73                                                           |

coordinated system time master 132

current mode 186

## D

date and time tab 132

digital I/O category y 91

digital inputs 37

digital outputs 42

dirty zone 25

download program 136

drive object attributes 192

organizer, drive ID 82

properties 135

wiring BP connector 66

wiring IPD connector 67

wiring MP connector 68

wiring requirements 64

wiring STO connector 66

drive mode selection 142

drive parameter tools changing 147

viewing 145

dynamics category 95

servo loop diagram 96

## E

directive 166

motor ground termination 68 motor ground termination at motor

## EMI (ElectroMagnetic Interference)

bonding 22

EN 61508 162

EN 62061 162

EN ISO 13849-1 CAT 3

requirements 162

stop category definitions 162

## enclosure

requirements 16

sizing 19

error codes 155

## Ethernet 47

cable length 79

cables

RJ45 connector 79

category 89

pinouts 35

wiring 79

## Ethernet module

ControlLogix 133

## Ethernet port

CompactLogix 132

## EtherNet/IP

address 126

dynamic address 129

static address 127

DHCP 129

EtherNet/IP external reference 142

## EMC

68

## explicit messaging

data types 213

DINT data 214

REAL data 215

string data 216

## F

fault codes 155

faults category 98

feedback connections 74

feedback power supply 53

fuse selection 17

fuse specifications

Kinetix 300 18

## G

general category 85

generic TTL incremental 48

ground multiple subpanels 63

system to subpanel 62

grounded power configuration 57

## H

HF bonding 22

high frequency energy y 24

homing category y 111

## I

I/O connections 74

I/O connector wiring 76

I/O specifications analog output 44

analog reference 43

back-up power 47

buffered encoder outputs 46

digital inputs 37

digital outputs 42

Ethernet 47

master gearing 45

pinouts 34

step and direction 45

ID tag descriptions 199

index base addressing 212

index configuration assembly instance 109

index select 99

indexing 142 , 148

indexing category 99

input and output assembly y 191

## input assembly

instance 194

tags 192

| input power wiring                                                        | MicroLogix diagrams  186                                              | MicroLogix diagrams  186                                              |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------|
| 3-phase Delta  57                                                         | mode                                                                  | mode                                                                  |
| 3-phase WYE  57                                                           | analog velocity  186                                                  | analog velocity  186                                                  |
| determine input power  56                                                 | current  186                                                          | current  186                                                          |
| grounded power configuration  57                                          | master gearing  45                                                    | master gearing  45                                                    |
| single-phase  58                                                          | step and direction  186                                               | step and direction  186                                               |
| voltage doubler  58                                                       | monitor category  97                                                  | monitor category  97                                                  |
| single-phase amplifiers on 3-phase power                                  | MotionView software                                                   | MotionView software                                                   |
| 59 ,  60 input/output category  91                                        | analog I/O category  92                                               | analog I/O category  92                                               |
| install drive accessories                                                 | communication category  89                                            | communication category  89                                            |
| I/O terminal block  76                                                    | configuration  81 digital I/O category                                | configuration  81 digital I/O category                                |
| low-profile connector kits  77                                            | drive organizer  82                                                   | drive organizer  82                                                   |
| shunt resistor  78                                                        | dynamics category  95                                                 | dynamics category  95                                                 |
| install your drive                                                        | Ethernet category  89                                                 | Ethernet category  89                                                 |
| bonding subpanels  24                                                     | faults category  98                                                   | faults category  98                                                   |
| circuit breakers  17                                                      | general category  85                                                  | general category  85                                                  |
| fuse selection  17                                                        | homing category  111                                                  | homing category  111                                                  |
| HF bonding  22                                                            | absolute homing  113                                                  | absolute homing  113                                                  |
| system mounting requirements  16                                          | home offset  114                                                      | home offset  114                                                      |
| transformer  17                                                           | home to marker                                                        | home to marker                                                        |
|                                                                           | 114                                                                   | 114                                                                   |
| interconnect diagrams                                                     | homing firmware algorithm  115 homing method 23  117                  | homing firmware algorithm  115 homing method 23  117                  |
| 120/240V single-phase input power  176 120V single-phase input power  175 | homing method 25  118                                                 | homing method 25  118                                                 |
| 2097 master gearing example  187                                          | homing method 27  119                                                 | homing method 27  119                                                 |
| 2097 with Kinetix LDC and Kinetix LDL linear                              | homing method 29  120                                                 | homing method 29  120                                                 |
| motor  181                                                                | homing method 33                                                      | homing method 33                                                      |
| 2097 with Kinetix MPAR actuator  184                                      | homing method 34  121                                                 | homing method 34  121                                                 |
| 2097 with Kinetix MPAS actuator  183                                      | homing method 35  121                                                 | homing method 35  121                                                 |
| 2097 with Kinetix MPL/MPM/MPF/MPS motor  178                              | homing methods  112 homing methods 7…14                               | homing methods  112 homing methods 7…14                               |
| 2097 with Kinetix TLAR actuator  185                                      | homing switch  114                                                    | homing switch  114                                                    |
| 2097 with Kinetix TLY motor  180                                          | immediate homing  113 indexing category  99                           | immediate homing  113 indexing category  99                           |
| 2097 with Kinetx MPAI actuator  184                                       | abort index  107                                                      | abort index  107                                                      |
| 2097 with MicroLogix  186 240/480V three-phase input power  177           | absolute  101                                                         | absolute  101                                                         |
|                                                                           | action parameter  106 blended  102                                    | action parameter  106 blended  102                                    |
| notes  174                                                                |                                                                       |                                                                       |
| shunt resistor  177                                                       | current  105                                                          | current  105                                                          |
|                                                                           | explicit messaging                                                    | explicit messaging                                                    |
| K                                                                         | 108 incremental  101 index configuration assembly instance            | 108 incremental  101 index configuration assembly instance            |
| keypad input                                                              | 109                                                                   | 109                                                                   |
|                                                                           | registration distance  reset index  107                               | registration distance  reset index  107                               |
| circuit breaker/fuse  18                                                  | rotary absolute                                                       | rotary absolute                                                       |
| KinetixLDAT  183                                                          | 102 rotary incremental  103 rotary negative  104 rotary positive  104 | 102 rotary incremental  103 rotary negative  104 rotary positive  104 |
| L                                                                         | rotary shortest path  103 start index  107                            | rotary shortest path  103 start index  107                            |
| limits category  93                                                       | 91 93                                                                 | 91 93                                                                 |
| linear motor database  84                                                 | input/output category  limits category                                | input/output category  limits category                                |
| linear motors                                                             | linear motor database  84 monitor category  97                        | linear motor database  84 monitor category  97                        |
| interconnect diagram Kinetix LDC and Kinetix LDL  181                     | motor category  82 motor database  83                                 | motor category  82 motor database  83                                 |
| low profile connector kits                                                |                                                                       |                                                                       |
|                                                                           | position limits category  94 tools category  96                       | position limits category  94 tools category  96                       |
| wiring  77 low voltage directive                                          | velocity limits category  93 82                                       | velocity limits category  93 82                                       |
| 166                                                                       | motor category  motor database  83                                    | motor category  motor database  83                                    |
| M                                                                         | motor feedback                                                        | motor feedback                                                        |
| 45 ,  142 ,  144 ,  148 ,  187                                            | pinouts  35                                                           | pinouts  35                                                           |
| 143                                                                       |                                                                       |                                                                       |
| examples                                                                  |                                                                       |                                                                       |
| master gearing                                                            |                                                                       |                                                                       |
| specifications                                                            |                                                                       |                                                                       |
| Kinetix 300                                                               |                                                                       |                                                                       |
| 124                                                                       |                                                                       |                                                                       |

specifications

| general  48 thermostat  49                      | publications, related  10                             | publications, related  10                             | publications, related  10                             | publications, related  10                             |
|-------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| wiring  74                                      |                                                       |                                                       |                                                       |                                                       |
| motor power                                     |                                                       |                                                       |                                                       |                                                       |
| pinouts  36                                     | reglations  166                                       | reglations  166                                       | reglations  166                                       | reglations  166                                       |
| wiring  69                                      | related publications  10                              | related publications  10                              | related publications  10                              | related publications  10                              |
| motors                                          |                                                       |                                                       |                                                       |                                                       |
| brake currents  188                             | requirements 21                                       | requirements 21                                       | requirements 21                                       | requirements 21                                       |
| feedback pinouts  75                            | clearance                                             | clearance                                             | clearance                                             | clearance                                             |
| ground termination  68                          | RJ45                                                  | RJ45                                                  | RJ45                                                  | RJ45                                                  |
| interconnect diagram                            | Ethernet connector  79                                | Ethernet connector  79                                | Ethernet connector  79                                | Ethernet connector  79                                |
| Kinetix MPL/MPM/MPF/MPS                         | route power and signal wiring                         | route power and signal wiring                         | route power and signal wiring                         | route power and signal wiring                         |
| Kinetix TLY  180                                | RSLogix 5000 software  11 ,  131                      | RSLogix 5000 software  11 ,  131                      | RSLogix 5000 software  11 ,  131                      | RSLogix 5000 software  11 ,  131                      |
|                                                 | power wiring                                          | power wiring                                          | power wiring                                          | power wiring                                          |
| 3-phase and brake  71                           |                                                       |                                                       |                                                       |                                                       |
| 3-phase only  70 Kinetix TL  69                 | S                                                     | S                                                     | S                                                     | S                                                     |
| shield clamp wiring  73                         | safe torque off                                       | safe torque off                                       | safe torque off                                       | safe torque off                                       |
| mount                                           | 164                                                   | 164                                                   | 164                                                   | 164                                                   |
|                                                 | troubleshooting                                       | troubleshooting                                       | troubleshooting                                       | troubleshooting                                       |
| Kinetix 300 drive  30                           | safe torque-off                                       | safe torque-off                                       | safe torque-off                                       | safe torque-off                                       |
| N                                               | bypass  connector location  165 operation  163 ,  168 | bypass  connector location  165 operation  163 ,  168 | bypass  connector location  165 operation  163 ,  168 | bypass  connector location  165 operation  163 ,  168 |
|                                                 | PFD and PFH data  164                                 | PFD and PFH data  164                                 | PFD and PFH data  164                                 | PFD and PFH data  164                                 |
| noise  25                                       | PFD and PFH definition  164 pinouts  33               | PFD and PFH definition  164 pinouts  33               | PFD and PFH definition  164 pinouts  33               | PFD and PFH definition  164 pinouts  33               |
|                                                 | proof tests  163 170                                  | proof tests  163 170                                  | proof tests  163 170                                  | proof tests  163 170                                  |
| O                                               | specifications                                        | specifications                                        | specifications                                        | specifications                                        |
| output assembly                                 | wiring diagram                                        | wiring diagram                                        | wiring diagram                                        | wiring diagram                                        |
| examples  197                                   | wiring requirements  167                              | wiring requirements  167                              | wiring requirements  167                              | wiring requirements  167                              |
| incremental examples  198                       | safety products catalog  169                          | safety products catalog  169                          | safety products catalog  169                          | safety products catalog  169                          |
| instance  196                                   | select drive mode  142                                | select drive mode  142                                | select drive mode  142                                | select drive mode  142                                |
| tags  195                                       | servo loop diagram  96                                | servo loop diagram  96                                | servo loop diagram  96                                | servo loop diagram  96                                |
| velocity examples  198                          | shield clamp  73                                      | shield clamp  73                                      | shield clamp  73                                      | shield clamp  73                                      |
| overtravels                                     | 28                                                    | 28                                                    | 28                                                    | 28                                                    |
| dedicated inputs  220                           | shunt resistor  ,  29                                 | shunt resistor  ,  29                                 | shunt resistor  ,  29                                 | shunt resistor  ,  29                                 |
| fault recovery  222 modes of operation  219     | interconnect diagram  177 wiring requirements  78     | interconnect diagram  177 wiring requirements  78     | interconnect diagram  177 wiring requirements  78     | interconnect diagram  177 wiring requirements  78     |
| operation  221                                  | shunt resistor and DC bus 36                          | shunt resistor and DC bus 36                          | shunt resistor and DC bus 36                          | shunt resistor and DC bus 36                          |
|                                                 | pinouts  shunt/DC bus connector                       | pinouts  shunt/DC bus connector                       | pinouts  shunt/DC bus connector                       | pinouts  shunt/DC bus connector                       |
| P                                               |                                                       |                                                       |                                                       |                                                       |
|                                                 | SICK-Stegmann  48                                     | SICK-Stegmann  48                                     | SICK-Stegmann  48                                     | SICK-Stegmann  48                                     |
| panel                                           | software                                              | software                                              | software                                              | software                                              |
| requirements  16                                | Logix Designer application  11 ,  MotionView  82      | Logix Designer application  11 ,  MotionView  82      | Logix Designer application  11 ,  MotionView  82      | Logix Designer application  11 ,  MotionView  82      |
| PFD and PFH data  164                           | RSLogix 5000  11                                      | RSLogix 5000  11                                      | RSLogix 5000  11                                      | RSLogix 5000  11                                      |
| PFD and PFH definition  164                     | ,  131                                                | ,  131                                                | ,  131                                                | ,  131                                                |
|                                                 | specifications                                        | specifications                                        | specifications                                        | specifications                                        |
| pinouts                                         | analog output  44                                     | analog output  44                                     | analog output  44                                     | analog output  44                                     |
| AC input power (IPD)  36 back-up power (BP)  36 |                                                       |                                                       |                                                       |                                                       |
| 35                                              | analog reference inputs  43 back-up power  47         | analog reference inputs  43 back-up power  47         | analog reference inputs  43 back-up power  47         | analog reference inputs  43 back-up power  47         |
| Ethernet (Port 1)  I/O (IOD)  34                | buffered encoder outputs  digital inputs  37          | buffered encoder outputs  digital inputs  37          | buffered encoder outputs  digital inputs  37          | buffered encoder outputs  digital inputs  37          |
| motor feedback (MF)                             | digital outputs  42                                   | digital outputs  42                                   | digital outputs  42                                   | digital outputs  42                                   |
| 35 motor feedback connector  75 36              | Ethernet  47                                          | Ethernet  47                                          | Ethernet  47                                          | Ethernet  47                                          |
| motor power (MP)  33                            | feedback                                              | feedback                                              | feedback                                              | feedback                                              |
| safe torque-off (STO)                           |                                                       |                                                       |                                                       |                                                       |
| shunt resistor and DC bus (BC)  36              | power supply  53 Kinetix 300                          | power supply  53 Kinetix 300                          | power supply  53 Kinetix 300                          | power supply  53 Kinetix 300                          |
| PL  162                                         | circuit breaker/fuse  18                              | circuit breaker/fuse  18                              | circuit breaker/fuse  18                              | circuit breaker/fuse  18                              |
| position limits category  94                    | master gearing  45                                    | master gearing  45                                    | master gearing  45                                    | master gearing  45                                    |
| power block diagram  189                        | motor feedback  48                                    | motor feedback  48                                    | motor feedback  48                                    | motor feedback  48                                    |
|                                                 | generic TTL  51                                       | generic TTL  51                                       | generic TTL  51                                       | generic TTL  51                                       |
| power supply, feedback  53                      |                                                       |                                                       |                                                       |                                                       |
| 137                                             |                                                       |                                                       |                                                       |                                                       |
| power up                                        | SICK-Stegmann  50                                     | SICK-Stegmann  50                                     | SICK-Stegmann  50                                     | SICK-Stegmann  50                                     |
| 163                                             |                                                       |                                                       |                                                       |                                                       |
| proof tests                                     |                                                       |                                                       |                                                       |                                                       |
| power dissipation specifications  20            |                                                       |                                                       |                                                       |                                                       |

Tamagawa 52

motor thermostat interface 49

power dissipation 20

safe torque-off f 170

step and direction 45

status indicators 125

step and direction 45 , 142 , 148 , 186

Studio 5000 Logix Designer 11 , 131

system block diagrams

power block diagram 189

voltage-doubler block diagram 190

system mounting requirements 16

system overview 11

diagram 12

## T

Tamagawa 48

test the axis

138

tools category 96

training 9

transformer

sizing 17

troubleshooting 154

clear faults 158

error code E39 164

error codes 155

safe torque off f 164

tune the axis

139

servo loop diagram 96

## U

UK elecrical equipment (safety) regulations

166

UK EMC

166

## V

velocity limits category 93

velocity mode 186

voltage doubler block diagram 190 operation 58

power diagram 175

## W

## who should use this manual 9 wiring

build your own cables 56 diagram, safe torque-off f 169

drive

BP connector 66

IPD connector 67

MP connector 68

STO connector 66

Ethernet connections 79

grounded power configuration 57

grounding drive 62 guidelines 65 I/O connector 76 input power determine type 56 low profile connectors 77 master gearing 187 motor cable shield clamp 73 motor feedback 74 motor power 69 , 70 , 71 167

requirements 55 ,

drive 64

shunt resistor 78

route power and signal wiring 56

shunt resistor 78

## Notes:

## Rockwell Automation Support

Use these resources to access support information.

| Technical Support Center                         | Find help with how-to videos, FAQs, chat, user forums, Knowledgebase, and product notification updates.   | rok.auto/support      |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------|
| Local Technical Support Phone Numbers            | Locate the telephone number for your country.                                                             | rok.auto/phonesupport |
| Technical Documentation Center                   | Quickly access and download technical specifications, installation instructions, and user manuals.        | rok.auto/techdocs     |
| Literature Library                               | Find installation instructions, manuals, brochures, and technical data publications.                      | rok.auto/literature   |
| Product Compatibility and Download Center (PCDC) | Download firmware, associated files (such as AOP, EDS, and DTM), and access product release notes.        | rok.auto/pcdc         |

## Documentation Feedback

Your comments help us serve your documentation needs better. If you have any suggestions on how to improve our content, complete the form at rok.auto/docfeedback .

## Waste Electrical and Electronic Equipment (WEEE)

<!-- image -->

At the end of life, this equipment should be collected separately from any unsorted municipal waste.

Rockwell Automation maintains current product environmental compliance information on its website at rok.auto/pec .

Allen-Bradley, CompactLogix, ControlFLASH, ControlLogix, expanding human possibility, Kinetix, Logix PAC, Micro850, MicroLogix, RSLogix 500, RSLogix 5000, SoftLogix, Rockwell Automation, Stratix, Studio 5000, and Studio 5000 Logix Designer are trademarks of Rockwell Automation, Inc.

EtherNet/IP is a trademark of ODVA, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş. Kar Plaza İş Merkezi E Blok Kat:6 34752, İçerenköy, İstanbul, Tel: +90 (216) 5698400 EEE Yönetmeliğine Uygundur

Connectwithus.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

rockwellautomation.com expandinghumanpossibility

AMERICAS:RockwellAutomation.1201SouthSec0ndStreet,Milwaukee,W153204-2496USA,Tel:(1)414.382.2000,Fax:(1)414.382.4444 EUR0PE/MIDDLEEAST/AFRICA:RockwellAutomationNV,PegasusPark,DeKleetlaan12a,1831Diegem,Belgium,Tel:(32)26630600.Fax:(32)26630640 ASIAPAClFIC:RockwellAutamation,Level 14,CoreF,Cyberport3,100Cyberport Road,HongKong,Tel:(852)28874788,Fax:(852)25081846 UNITED KINGD0M:RockwellAutomationLtd.Pitfield,KilnFarmMiltonKeynes,MK113DR,UnitedKingdom.Tel:(44)（1908)838-800.Fax:(44)（1908)261-917