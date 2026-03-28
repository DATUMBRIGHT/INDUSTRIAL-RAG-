## Guard I/O EtherNet/IP Safety Modules

Catalog Numbers 1732ES-IB16, 1732ES-IB8XOB8, 1732ES-IB8XOBV4, 1732ES-IB12XOB4, 1732ES-IB12XOBV2, 1791ES-IB16, 1791ES-IB8XOBV4

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Important User Information

Read this document and the documents listed in the additional resources section about installation, configuration, and operation of this equipment before you install, configure, operate, or maintain this product. Users are required to familiarize themselves with installation and wiring instructions in addition to requirements of all applicable codes, laws, and standards.

Activities including installation, adjustments, putting into service, use, assembly, disassembly, and maintenance are required to be carried out by suitably trained personnel in accordance with applicable code of practice.

If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss.

<!-- image -->

IMPORTANT

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence.

Identifies information that is critical for successful application and understanding of the product.

Labels may also be on or inside the equipment to provide specific precautions.

<!-- image -->

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

<!-- image -->

<!-- image -->

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective Equipment (PPE).

## Table of Contents

| Preface                   | About the Specifications and Dimensions in This Manual . . . . . . . . . 9                      |                                            |
|---------------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------|
|                           | Terminology . . . . . . . . .  . . . . . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . . . . . 9  |
|                           | Additional Resources . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . 10       |
|                           | Chapter 1                                                                                       |                                            |
| Safety Function Operation | Safe State . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . . .                 | . . . . . . . . . . . . . . . . . . . 11   |
|                           | Self-diagnostic Functions  . . . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . . . 12     |
|                           | Configuration Lock . . . .  . . . . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . . . . 12   |
|                           | I/O Status Data . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . . . . . . 12       |
|                           | Safety Inputs. . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                   | . . . . . . . . . . . . . . . . . . 13     |
|                           | Using a Test Output with a Safety Input. . . . . . . . . . . . . . . . . . . . . 13             |                                            |
|                           | Set Dual-channel Mode and Discrepancy Time . . . . . . . . . . . . . . 17                       |                                            |
|                           | Dual-channels, Equivalent. . . .  . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . 17             |
|                           | Dual-channels, Complementary .  . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . 19               |
|                           | Safety Input Fault Recovery .  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . 20           |
|                           | Input Delays . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                         | . . . . . . . . . . . . . . . . . 20       |
|                           | Muting Lamp Operation. . . . . . .  . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . 21           |
|                           | Safety Outputs . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . . . . . . . 23     |
|                           | Safety Output with Test Pulse  . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . 23             |
|                           | Dual-channel. . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . . 24         |
|                           | Single-channel. . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                        | . . . . . . . . . . . . . . . . 25         |
|                           | Safety Output Fault Recovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25     |                                            |
|                           | Controlling Devices . . . . . . . . .  . . . . . . . . . . . . . . . . . .                      | . . . . . . . . . . . . . . . . 26         |
|                           | Chapter 2                                                                                       |                                            |
| About the Modules         | Before You Begin. . . . .  . . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . . 27 |
|                           | Firmware Information and Downloads. . . . . . . . . . . . . . . . . . . . . . . . . . 28        |                                            |
|                           | Functional Safety Certificates .  . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . . 28         |
|                           | Understand Suitability for Use . .  . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . 28           |
|                           | 1791ES-IB16 and                                                                                 |                                            |
|                           | 1791ES-IB8XOBV4 Modules North American Hazardous Location                                       |                                            |
|                           | Approval . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                 | . . . . . . . . . . . . . . . . . . 29     |
|                           | Follow Precautions for Use. . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 30         |
|                           | I/O Module Overview . . . . . . . .  . . . . . . . . . . . . . . . . .                          | . . . . . . . . . . . . . . . . 31         |
|                           | Selecting a Power Supply.  . . . . . . . . . . . . . . . . . . . .                              | . . . . . . . . . . . . . . . . . . 33     |
|                           | Programming Requirements . . . .  . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 34           |
|                           | CIP Safety in                                                                                   |                                            |
|                           | EtherNet/IP Safety Architectures.   . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . 34           |
|                           | Device Level Ring (DLR) . . . .  . . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . . 35             |
|                           | Identify Major Parts of the Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37 |                                            |
|                           | Chapter 3                                                                                       |                                            |
| Install the Module        | Environment and Enclosure. . . .  . . . . . . . . . . . . . . . . .                             | . . . . . . . . . . . . . . . 39           |

|                           | For 1732ES Modules . . . . . . .  . . . . . . . . . . . . . . . .                                            | . . . . . . . . . . . . . . . 40     |
|---------------------------|--------------------------------------------------------------------------------------------------------------|--------------------------------------|
|                           | Prevent Electrostatic Discharge. .  . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . 41     |
|                           | Environmental Considerations for Use. . . . . . . . . . . . . . . . . . . . . . . . . . 42                   |                                      |
|                           | Follow Wiring Precautions. . . .  . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . . 42   |
|                           | Follow DC Power Supply Precautions . . . . . . . . . . . . . . . . . . . . . . . . . . 45                    |                                      |
|                           | Mount the Module . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 45   |
|                           | Module Spacing . . . . . . . . . .  . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . 46   |
|                           | Mount the 1791ES Modules on a DIN Rail. . . . . . . . . . . . . . . . . . 48                                 |                                      |
|                           | Mount the 1732ES Modules on a Wall or Panel. . . . . . . . . . . . . . 49                                    |                                      |
|                           | Grounding the 1732ES Modules.  . . . . . . . . . . . . . .                                                   | . . . . . . . . . . . . . 51         |
|                           | Make Connections for 1791ES Modules . . . . . . . . . . . . . . . . . . . . . . . . 52                       |                                      |
|                           | Power Connections. . . . . . . . .  . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . 52     |
|                           | EtherNet/IP Connections.  . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . 53   |
|                           | I/O Connections . . . . . . . . . .  . . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . 53     |
|                           | Make Connections for 1732ES Modules . . . . . . . . . . . . . . . . . . . . . . . . 55                       |                                      |
|                           | Power Connections. . . . . . . . .  . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . 55     |
|                           | Power Pass Through . . . . . . .  . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . 55     |
|                           | EtherNet/IP Connections.  . . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . . . 59   |
|                           | I/O Connections . . . . . . . . . .  . . . . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . . . 60     |
|                           | Label the IP Address and Device Connections . . . . . . . . . . . . . . . 62                                 |                                      |
|                           | Chapter 4                                                                                                    |                                      |
| Wiring Examples           | Wiring Examples for Safety Categories . . . . . . . . . . . . . . . . . . . . . . . . . . 64                 |                                      |
|                           | Wiring by Application . . .  . . . . . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . 67 |                                      |
|                           | Chapter 5                                                                                                    |                                      |
| Configure the I/O Modules | Set the IP Address . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                  | . . . . . . . . . . . . . . . . . 75 |
|                           | Add Modules to the I/O Configuration Tree . . . . . . . . . . . . . . . . . . . . 77                         |                                      |
|                           | Configure the Module Properties .   . . . . . . . . . . . . . . .                                            | . . . . . . . . . . . . . . . 79     |
|                           | Set the IP Address in the Programming Software . . . . . . . . . . . . . 80                                  |                                      |
|                           | Change the Module Definition  . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . 80       |
|                           | Configure the Safety Connections   . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . 86     |
|                           | Configuration Ownership – Reset Ownership . . . . . . . . . . . . . . . 87                                   |                                      |
|                           | Configuration Signature . . . .  . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . 88     |
|                           | Configure the Module Inputs . .  . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . 88     |
|                           | Configure the Test Outputs. . .  . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . 90   |
|                           | Configure the Module Outputs .  . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . 91     |
|                           | Save and Download the Module Configuration . . . . . . . . . . . . . . . . . . 92                            |                                      |
|                           | Chapter 6                                                                                                    |                                      |
| Replace Guard I/O Modules | Manually Set the Safety Network Number . . . . . . . . . . . . . . . . . . . . . . 93                        |                                      |
|                           | Reset the Module to Out-of-box Configuration. . . . . . . . . . . . . . . . . . 94                           |                                      |
|                           | Replace a Module in a GuardLogix System . . . . . . . . . . . . . . . . . . . . . . 94                       |                                      |
|                           | Configure Only When No Safety Signature Exists. . . . . . . . . . . . 95 . . . . . . . . . . . . . . . . .   | . . . . . . . . . . . . . . . . 95   |

Configure Always . . . . . . . .

Chapter 7

| Interpret the Module Status   | Module Status Indicator Depictions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97   |                                           |
|-------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------|
| Indicators                    | Module Status Indicator Descriptions. . . . . . . . . . . . . . . . . . . . . . . . . . . 98    |                                           |
|                               | Appendix A                                                                                      |                                           |
| Get Diagnostic Status from    | Get Status Messages from 1791ES-IB8XOBV4 Modules . . . . . . . . 102                            |                                           |
| Modules by Using Explicit     | Get Status Messages from 1791ES-IB16 Modules . . . . . . . . . . . . . . . 107                  |                                           |
| Messaging                     | Get Status Messages from 1732ES Modules . . . . . . . . . . . . . . . . . . . . 112             |                                           |
|                               | 1732ES-IB12XOB4 Modules. . .  . . . . . . . . . . . . . .                                       | . . . . . . . . . . . . . 112             |
|                               | 1732ES-IB12XOBV2 Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117            |                                           |
|                               | 1732ES-IB16 Modules . . .  . . . . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . . . . 122       |
|                               | 1732ES-IBXOB8 Modules . . . . .  . . . . . . . . . . . . . .                                    | . . . . . . . . . . . . . 127             |
|                               | 1732ES-IB8XOBV4 Modules  . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . 132           |
|                               | I/O Data Supported by Each Module . . . . . . . . . . . . . . . . . . . . . . . . . . 136       |                                           |
|                               | I/O Assembly and Reference Data .  . . . . . . . . . . . . . . .                                | . . . . . . . . . . . . . 140             |
|                               | 1791ES Modules . . . . . .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 140     |
|                               | 1732ES Modules . . . . . .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 143     |
|                               | Explicit Messages. . . . .  . . . . . . . . . . . . . . . . . . . . .                           | . . . . . . . . . . . . . . . . . . . 149 |
|                               | Appendix B                                                                                      |                                           |
| Safety Data                   | Calculated Values . . . .  . . . . . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . . . . 151 |
|                               | Appendix C                                                                                      |                                           |
| Configuration Reference       | Parameter Groups . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . 159       |
| Information                   |                                                                                                 |                                           |
| Specifications                | Technical Specifications  . . . . . . . . . . . . . . . . . . . .                               | . . . . . . . . . . . . . . . . . . 161   |
|                               | 1791ES Modules . . . . . .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 161     |
|                               | 1732ES Modules . . . . . .  . . . . . . . . . . . . . . . . . .                                 | . . . . . . . . . . . . . . . . . 163     |
|                               | Environmental Specifications . . . . . . . .  . . . . . . . . . . . . .                         | . . . . . . . . . . . . 166               |
|                               | Certifications . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                     | . . . . . . . . . . . . . . . . . . 168   |
|                               | Europe . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                       | . . . . . . . . . . . . . . . . . 168     |
|                               | North America . . . . . . . . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 169       |
|                               | Japan . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . . . . . . 169     |
|                               | EC Directives . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                    | . . . . . . . . . . . . . . . . . 169     |
|                               | EMC Directive . . . . . . . . . .  . . . . . . . . . . . . . . . . .                            | . . . . . . . . . . . . . . . . 169       |
|                               | Compliance with EC Directives . . . . . . . . . . . . . . . . . . . . . . . . . . . 169         |                                           |

## Notes:

## Summary of Changes

This manual contains new and updated information as indicated in this table.

| Topic Page                                                                |
|---------------------------------------------------------------------------|
| Updated Attention to include the text `chromate-passivated’. 48           |
| Updated text, provides information for configuring the safety outputs. 91 |

## Notes:

## About the Specifications and Dimensions in This Manual

## Terminology

Product specifications and accessories can change at any time based on improvements and other reasons. Consult with your Rockwell Automation representative to confirm actual specifications of purchased product. Dimensions and weights are nominal and are not for use for manufacturing purposes, even when tolerances are shown.

See this table for the meaning of common terms.

| Term Definition                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1732ES modules Also known as ArmorBlock® Guard I/O™ EtherNet/IP Safety Modules.                                                                                                                                                                                                                                      |
| 1791ES modules Also known as CompactBlock™ Guard I/O EtherNet/IP Safety Modules.                                                                                                                                                                                                                                     |
| Connection Logical communication channel for communication between nodes. Connections are maintained and controlled between masters and slaves.                                                                                                                                                                      |
| DLR Acronym for Device Level Ring, a type of network topology.                                                                                                                                                                                                                                                       |
| EDS Acronym for Electronic Data Sheet, a template that RSNetWorx™ software uses to display the configuration parameters, I/O data profile, and connection-type support for a given I/O module. These are simple text files used by RSNetWorx software for you to identify products and commission them on a network. |
| L- Output +24V DC common.                                                                                                                                                                                                                                                                                            |
| M Sinking output common channel, output switches to the common voltage.                                                                                                                                                                                                                                              |
| MTBF Acronym for mean time between failure, the average time between failure occurrences.                                                                                                                                                                                                                            |
| NAT Acronym for network address translation, a service that lets modules reuse IP addresses throughout a network.                                                                                                                                                                                                    |
| ODVA Acronym for Open DeviceNet Vendor Association, a nonprofit association of vendors established for the promotion of CIP networks.                                                                                                                                                                                |
| P Sourcing output channel, output switches to the plus voltage.                                                                                                                                                                                                                                                      |
| PFD Acronym for probability of failure on demand, the average probability of a system to fail to perform its design function on demand.                                                                                                                                                                              |
| PFH Acronym for probability of failure per hour, the probability of a system to have a dangerous failure occur per hour.                                                                                                                                                                                             |
| Proof test Periodic test performed to detect failures in a safety-related system so that, if necessary, the system can be restored to an as-new condition or as close as practical to this condition.                                                                                                                |
| S+ Output +24V DC.                                                                                                                                                                                                                                                                                                   |
| SNN Acronym for safety network number, which uniquely identifies a network across all networks in the safety system. You are responsible for assigning a unique number for each safety network or safety sub-net within a system.                                                                                    |
| Standard Devices or portions of devices that do not participate in the safety function.                                                                                                                                                                                                                              |

## Additional Resources

These documents contain additional information concerning related products from Rockwell Automation.

|                                                                                                                          | Resource Description                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Allen-Bradley® Stratix® 5700 Network Address Translation (NAT) White Paper, publication ENET-WP032                       | Provides information about NAT.                                                                                                                                               |
| ArmorBlock Guard I/O EtherNet/IP Safety Modules Product Information, publication 1732ES-PC001                            | Provides instructions to install ArmorBlock Guard I/O EtherNet/IP Safety modules.                                                                                             |
| CompactBlock Guard I/O EtherNet/IP Safety Modules Installation Instructions, publication 1791ES-IN001                    | Provides specifications and information related to the 1791ES Guard I/O modules.                                                                                              |
| Compact GuardLogix® 5370 Controllers User Manual, publication 1769-UM022                                                 | Provides information on how to install, configure, program, and use Compact GuardLogix 5370 controllers.                                                                      |
| EtherNet/IP Embedded Switch Technology Application Guide, publication ENET-AP005                                         | Describes how to install, configure, and maintain linear and Device Level Ring (DLR) networks using Rockwell Automation® EtherNet/IP devices with embedded switch technology. |
| Ethernet Design Considerations Reference Manual, publication ENET-RM002                                                  | Describes the required media components and how to plan for and install these required components.                                                                            |
| GuardLogix 5570 and Compact GuardLogix 5370 Controller Systems Safety Reference Manual, publication 1756-RM099           | Provides information on safety application requirements for GuardLogix 5570 controllers in Studio 5000 Logix Designer® projects.                                              |
| GuardLogix 5570 Controllers User Manual, publication 1756-UM022                                                          | Provides information on how to install, configure, program, and use GuardLogix 5570 controllers in Studio 5000 Logix Designer projects.                                       |
| GuardLogix Controller Systems Safety Reference Manual, publication 1756-RM093                                            | Provides information on safety application requirements for GuardLogix 5560 and 5570 controllers in Studio 5000 Logix Designer projects.                                      |
| GuardLogix Controllers User Manual, publication 1756-UM020                                                               | Provides information on how to install, configure, program, and use GuardLogix 5560 and 5570 controllers in Studio 5000 Logix Designer projects.                              |
| GuardLogix Safety Application Instructions Safety Reference Manual, publication 1756-RM095                               | Provides reference information describing the GuardLogix Safety Application Instruction Set.                                                                                  |
| ODVA Media Planning and Installation Manual, publication 00148-BR00, available from the EtherNet/IP™ Library at ODVA.org | Describes the required media components and how to plan for and install these required components.                                                                            |
| Switched Mode Power Supply Specifications Technical Data, publication 1606-TD002                                         | Provides specifications and more information for the switched mode power supplies.                                                                                            |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                                              | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                           |
| Product Certifications website, http://www.rockwellautomation.com/global/certification/overview.page                     | Provides declarations of conformity, certificates, and other certification details.                                                                                           |

You can view or download publications at http://www.rockwellautomation.com/global/literature-library/overview.page .

To order paper copies of technical documentation, contact your local Allen-Bradley distributor or Rockwell Automation sales representative.

## Safe State

## Safety Function Operation

| Topic Page                   |
|------------------------------|
| Safe State 11                |
| Self-diagnostic Functions 12 |
| Configuration Lock 12        |
| I/O Status Data 12           |
| Safety Inputs 13             |
| Muting Lamp Operation 21     |
| Safety Outputs 23            |
| Controlling Devices 26       |

Read this chapter for information related to the safety functions of the modules. Also included is a brief overview on international standards and directives that you must be familiar with.

<!-- image -->

## ATTENTION: Safety State of the Module

- Safety state of the inputs and outputs is defined as the off state.
- Safety state of the module and its data is defined as the off state.
- Use the Guard I/O™ module only in applications where the off state is the safety state.

The following status is the safety state of the Guard I/O modules:

- Safety outputs: off
- Safety input data to network: off

## Figure 1 - Safety Status

<!-- image -->

## Self-diagnostic Functions

## Configuration Lock

## I/O Status Data

The module is designed for use in applications where the safety state is the off state.

Self-diagnostics are performed when the power is turned on and periodically during operation. If a fatal internal module error occurs, the red module status (MS) indicator illuminates, and the safety outputs and input data and status to the network turn off.

After configuration data has been downloaded and verified, the configuration data within the module can be protected.

For GuardLogix® systems, the status indicator is not used. For information about safety signatures, see the appropriate GuardLogix Safety Reference Manual, which is listed in the Additional Resources on page 10 .

The module provides status data for monitoring the I/O circuits and I/O data. The status data includes the following data, which the controllers can read. 1 = ON/Normal, and 0 = OFF/Fault/Alarm.

- Individual point input status
- Combined input status
- Individual point output status
- Combined output status
- Individual test output status
- Individual output readback (actual ON/OFF state of the outputs)

Status data indicate whether each safety input, safety output, or test output is normal (normal status: ON, faulted status: OFF). For fatal errors, communication connections can be broken, so the status data cannot be read.

Combined status is provided by an AND of the status of all safety inputs or all safety outputs. When all inputs or outputs are normal, the respective combined status is ON. When one or more of them has an error, the respective combined status is OFF. This status is known as the combined safety input status or combined safety output status.

## Safety Inputs

Read this section for information about safety inputs and their associated test outputs. A safety input can be used with test outputs. Safety inputs are used to monitor safety input devices.

## Using a Test Output with a Safety Input

A test output can be used in combination with a safety input for short circuit detection. Configure the test output as a pulse test source and associate it to a specific safety input.

<!-- image -->

<!-- image -->

ATTENTION: You can configure Test Outputs to be used as standard outputs. You can connect actuators to Test Output points that are expecting a Standard configuration.

Test Output points configured as Pulse Test or Power Supply become active whenever you apply input power to the module. These configured functions are independent of the I/O connections to the module.

ATTENTION: If a module with Test Outputs configured as Pulse Test or Power Supply is incorrectly installed in an application where actuators are connected to these Test Output points, the actuators are activated when input power is applied.

To prevent this possibility, follow these procedures.

- When installing or replacing a module, be sure that the module is correctly configured for the application or in the out-of-box condition before applying input power.
- Reset modules to their out-of-box condition when removing them from an application.
- Be sure that all modules in replacement stock are in their out-of-box condition.

The test output can also be used as a power supply to source 24V DC for an external input circuit.

Figure 2 - Example Use of a 1791ES-IB16 Module

<!-- image -->

Table 1 - Typical Pulse Width and Period

| Pulse Width Period   |
|----------------------|
| 500 μs 150 ms        |

Figure 3 - Test Pulse in a Cycle

<!-- image -->

<!-- image -->

ATTENTION: Do not use test outputs as safety outputs. Test outputs do not function as safety outputs.

When the external input contact is closed, a test pulse is output from the test output terminal to diagnose the field wiring and input circuitry. By using this function, short circuits between input signal lines and the power supply (positive side), and short circuits between input signal lines can be detected.

Figure 4 - Short Circuit Between Input Signal Lines

<!-- image -->

If an error is detected, safety input data and safety input status turns off.

Figure 5 - Single Channel Normal Operation and Fault Detection (not to scale)

<!-- image -->

## Set Dual-channel Mode and Discrepancy Time

To support redundant channel safety devices, the consistency between signals on two channels can be evaluated. Either equivalent or complementary can be selected. This function monitors the time during which there is a discrepancy between the two channels.

If the length of the discrepancy exceeds the configured discrepancy time, the safety input data and the individual-safety input status turn off for both channels. The configured discrepancy time is 0…65,530 ms in increments of 10 ms.

## IMPORTANT

The dual-channel function is used with two consecutive inputs that are paired together, this process starts at an even input number, such as inputs 0 and 1; 2 and 3; and so on.

## IMPORTANT

Do not set the discrepancy time longer than necessary. The purpose of the discrepancy time is to allow for normal differences between contact switching when demands are placed on safety inputs. For this testing to operate correctly, only one demand on the safety input is expected during the discrepancy time. If the discrepancy time is set too high, and multiple demands occur during this time, then both safety input channels will fault.

Table 2 shows the relation between input terminal states and controller input data and status.

Table 2 - Terminal Input Status and Controller I/O Data

| Dual-channel Mode Input Terminal Controller Input Data and Status Dual- channel   | Dual-channel Resultant Status    |
|-----------------------------------------------------------------------------------|----------------------------------|
| Dual-channels, Equivalent OFF OFF OFF OFF ON ON OFF Normal                        | Dual-channel Resultant Status    |
| Dual-channels, Equivalent OFF OFF OFF OFF ON ON OFF Normal                        | OFF ON OFF OFF OFF OFF OFF Fault |
| Dual-channels, Equivalent OFF OFF OFF OFF ON ON OFF Normal                        | ON OFF OFF OFF OFF OFF OFF Fault |
| Dual-channels, Equivalent OFF OFF OFF OFF ON ON OFF Normal                        | ON ON ON ON ON ON ON Normal      |
| Dual-channels, Complementary OFF OFF OFF ON OFF OFF OFF Fault                     |                                  |
| Dual-channels, Complementary OFF OFF OFF ON OFF OFF OFF Fault                     | OFF ON OFF ON ON ON OFF Normal   |
| Dual-channels, Complementary OFF OFF OFF ON OFF OFF OFF Fault                     | ON OFF ON OFF ON ON ON Normal    |
| Dual-channels, Complementary OFF OFF OFF ON OFF OFF OFF Fault                     | ON ON OFF ON OFF OFF OFF Fault   |

## Dual-channels, Equivalent

In Equivalent mode, both inputs of a pair must typically be in the same (equivalent) state. When a transition occurs in one channel of the pair, before the transition of the second channel of the pair, a discrepancy occurs. If the second channel transitions to the appropriate state before the discrepancy time elapses, the inputs are considered equivalent. If the second transition does not

occur before the discrepancy time elapses, the channels fault. In the fault state, the input and status for both channels are set low (off ). When configured as an equivalent dual pair, the data bits for both channels are sent to the controller as equivalent, both high or both low.

Figure 6 - Equivalent, Normal Operation, and Fault Detection (not to scale)

<!-- image -->

## Dual-channels, Complementary

In Complementary mode, the inputs of a pair are typically in the opposite (complementary) state. When a transition occurs in one channel of the pair before the transition of the second channel of the pair, a discrepancy occurs. If the second channel transitions to the appropriate state before the discrepancy time elapses, the inputs are considered complementary.

If the second transition does not occur before the discrepancy time elapses, the channels fault. The fault state of complementary inputs is the even-numbered input turned off and the odd-numbered input turned on. If faulted, both channel status bits are set low. When configured as a complementary dual-channel pair, the data bits for both channels are sent to the controller in complementary, or opposite states.

Figure 7 - Complementary, Normal Operation and Fault Detection (not to scale)

<!-- image -->

## Safety Input Fault Recovery

If an error is detected, the safety input data remains in the off state. Follow this procedure to activate the safety input data.

1. Remove the cause of the error.
2. Place the safety input (or safety inputs) into the safety state.

The safety input status turns on (fault cleared) after the input-error latch time has elapsed. The I/O indicator (red) turns off. The input data can now be controlled.

## Input Delays

On-delay – An input signal is treated as logic 0 during the on-delay time (0…126 ms, in increments of 6 ms) after the rising edge of the input contact. The input only turns on if the input contact remains on after the on-delay time has elapsed. This delay helps prevent rapid changes of the input data due to contact bounce.

Figure 8 - On-delay

<!-- image -->

Off-delay – An input signal is treated as logic 1 during the off-delay time (0…126 ms, in increments of 6 ms) after the falling edge of the input contact. The input only turns off if the input contact remains off after the off delay time has elapsed. This delay helps prevent rapid changes of the input data due to contact bounce.

Figure 9 - Off-delay

<!-- image -->

## Muting Lamp Operation

The 1732ES modules support this muting lamp feature. The feature was added to 1791ES modules in firmware revision 1.009. The operation of the muting status bits for the test outputs has changed. Your PLC processor program controls certain test outputs to illuminate a muting lamp:

- T3 and T7 for 1791ES-IB8XOBV4, 1732ES-IB8XOBV4, 1732ES-IB8XOB8
- T3, T7, and T11 for 1732ES-IB12XOB4 and 1732ES-IB12XOBV2
- T3, T7, T11, and T15 for 1791ES-IB16 and 1732ES-IB16

Muting lamp status is monitored with a test that runs periodically during every test interval to detect a burned-out lamp. The test runs repeatedly when the test output is commanded on. Figure 10 explains how muting lamp operation, status, and fault detection are monitored.

TIP The lamp test interval is 3 seconds. Two consecutive failed lamp tests are required to declare a burned-out lamp condition. The lamp test does not run immediately after the test output is energized. It starts at the next 3-second interval. To allow time for two consecutive test intervals, program a minimum Test Output On Time of 6 seconds.

Figure 10 - Muting Lamp Timing Diagram

<!-- image -->

Table 3 shows the expected behavior of the muting status bits. Keep these points in mind as well:

- When power is applied to the module, and a test output capable of operating as a muting output remains commanded off, the muting status defaults to on.

This bit operation is designed to help prevent erroneous muting instruction faults from the GuardLogix controller. This bit status is not the true indication of a burned-out lamp.

## IMPORTANT

Before checking the state of the corresponding muting status, make sure that the test output is commanded on. Once the test output is commanded on, a maximum time of 6 seconds is required for the module to detect a burned-out lamp.

- If a muting lamp circuit is open when power is applied to the module, the condition is detected when the test output is commanded on.
- When a lamp burns out and is replaced, the fault (muting status bit) returns to the normal condition, independent of the state of the test output.

Table 3 - Muting Status Bit Operation

| Test Output Commanded State   | Lamp Condition Muting Status Bit   | Description                                                                                                                          |
|-------------------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
|                               |                                    | ON Bad (open circuit) 0 Repair lamp.                                                                                                 |
|                               |                                    | ON Good 1 Normal condition. Lamp is operating properly.                                                                              |
|                               |                                    | OFF Bad (open circuit) 0 If lamp remains off after a test output capable of operating as a muting output is cycled, repair the lamp. |
|                               |                                    | OFF Good 1 Normal condition.                                                                                                         |

## Safety Outputs

Read this section for information about safety outputs.

<!-- image -->

ATTENTION: Serious injury can occur due to the breakdown of safety outputs. Do not connect loads beyond the rated value to the safety outputs.

## Safety Output with Test Pulse

When the safety output is on, the safety output can be test pulsed, as shown in Table 4 and Figure 11 .

Table 4 - Safety Output Test Pulse

| Pulse Width Period   |
|----------------------|
| 700 μs 600 ms        |

By using this function, the following can be detected:

- Short circuits between sourcing output signal lines and the power supply (positive side)
- Short circuits between sinking output signal lines and the power supply (negative side)
- Short circuits between output signal lines of the same polarity (from sourcing output to sourcing output or from sinking output to sinking output)

If an error is detected, the safety output data and individual-safety output status turns off.

Figure 11 - Test Pulse in a Cycle

<!-- image -->

## IMPORTANT

To prevent the test pulse from causing the connected device to malfunction, pay careful attention to the input response time of the device.

## Dual-channel

When the data of both channels is in the on state, and neither channel has a fault, the outputs are turned on. The status is normal. If a fault is detected on one channel, the safety output data and individual safety output status turn off for both channels.

Figure 12 - Dual-channel (not to scale)

<!-- image -->

## Single-channel

When the data of the channel is in the on state, and the channel does not have a fault, the output is turned on. The status is normal. If a fault is detected on the channel, the safety output data and individual safety output status turn off for the channel.

| Fault Detection   |                           | ON OFF   |                |
|-------------------|---------------------------|----------|----------------|
|                   | OUT0                      |          |                |
| Remote I/O        | Safety Output Status 0, 1 | ON       | Error Detected |
| Data              |                           | OFF      |                |

<!-- image -->

## Safety Output Fault Recovery

If a fault is detected, the safety outputs are switched off and remain in the off state.

Follow this procedure to reactivate the safety output data for modules with bipolar safety outputs (1791ES, 1732ES-IB12XOBV2, and 1732ES-IB12XOBV4 modules).

1. Remove the cause of the error.
2. Place the safety output (or safety outputs) into the safety state.

The safety output status turns on (fault cleared) when the output-error latch time has elapsed. The I/O indicator (red) turns off. The output data can now be controlled.

## Controlling Devices

Table 5 - Controlling Device Requirements

|                                                  |                                                                                                                                                                                 | Device Requirement Allen-Bradley® Bulletin Safety Components                        |
|--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|                                                  | Emergency stop switches Use approved devices with direct opening mechanisms that comply with IEC/EN 60947-5-1.                                                                  | Bulletin 800F, 800T                                                                 |
| Door interlocking switches, limit switches       | Use approved devices with direct opening mechanisms that comply with IEC/EN 60947-5-1 and capable of switching microloads of 24V DC 5 mA.                                       | Bulletin 440K, 440G, 440H for interlock switch Bulletin 440P, 802T for limit switch |
|                                                  | Safety sensors Use approved devices that comply with the relevant product standards, regulations, and rules in the country where used.                                          | Any Guardmaster® product                                                            |
| Relays with forcibly guided contacts, contactors | Use approved devices with forcibly guided contacts that comply with EN 50205. For feedback purposes, use devices with contacts capable of switching micro loads of 24V DC 5 mA. | Bulletin 700S, 100S                                                                 |
|                                                  | Other devices Evaluate whether devices used are appropriate to satisfy the requirements of safety category levels.                                                              | —                                                                                   |

Safety output faults are considered critical enough to require a module power cycle to clear (a sourcing safety output channel that is shorted to output power supply positive). This condition applies to modules with sourcing-only safety outputs (only 1732ES-IB8XOB8 and 1732ES-IB12XOB4 modules).

One of these faults on any safety output channel results in all sourcing-only safety outputs being placed in the safe state (off ). This condition applies to modules with sourcing-only safety outputs (only 1732ES-IB8XOB8 and 1732ES-IB12XOB4 modules).

Follow this procedure to reactivate the safety outputs after one of these faults.

1. Remove the cause of the error.
2. Power cycle the module.

The output data can now be controlled.

See Table 5 for information about controlling devices.

<!-- image -->

ATTENTION: Use appropriate devices as indicated in the Controlling Device Requirements table. Serious injury can occur due to loss of safety functions.

## Before You Begin

## About the Modules

| Topic Page                                                                            |
|---------------------------------------------------------------------------------------|
| Before You Begin 27                                                                   |
| Firmware Information and Downloads 28                                                 |
| Functional Safety Certificates 28                                                     |
| Understand Suitability for Use 28                                                     |
| Follow Precautions for Use 30                                                         |
| I/O Module Overview 31                                                                |
| 1791ES-IB16 and 1791ES-IB8XOBV4 Modules North American Hazardous Location Approval 29 |
| Selecting a Power Supply 33                                                           |
| Programming Requirements 34                                                           |
| CIP Safety in EtherNet/IP Safety Architectures 34                                     |
| Identify Major Parts of the Module 37                                                 |

Read this chapter for important overview information and precautions for use for the Guard I/O™ modules that implement the EtherNet/IP safety protocol. This chapter also includes an overview on how these I/O modules are used within a safety system.

In this manual defines safety administrator as a person who is qualified, authorized, and responsible to secure safety in the design, installation, operation, maintenance, and disposal of the machine. Follow these guidelines when using a module.

- Read and understand this manual before installing and operating the module.
- Keep this manual in a safe and accessible place where personnel can refer to it when necessary.
- Use the module properly according to the installation environment, performance, and functions of the machine.
- Verify that a safety administrator conducts a risk assessment on the machine and determines module suitability before installation.

<!-- image -->

## Firmware Information and Downloads

## Functional Safety Certificates

## Understand Suitability for Use

Verify that the Guard I/O firmware revision is correct before you commission the safety system. Firmware information and downloads for safety modules are available at this link:

http://www.rockwellautomation.com/rockwellautomation/support/ pcdc.page .

Safety certificates for Functional Safety modules are available at this link: http://www.rockwellautomation.com/global/certification/overview.page

Rockwell Automation is not responsible for conformity with any standards, codes, or regulations that apply to the combination of products in your application or use of the product.

Take all necessary steps to determine the suitability of the product for the systems, machine, and equipment with which it is used.

Know and observe all prohibitions of use applicable to this product.

Never use the products for an application that involves serious risk to life or property without making sure of the following:

- The system as a whole is designed to address the risks.
- The Rockwell Automation product is properly rated and installed for the intended use within the overall equipment or system.

Use the module only in an environment that is within the general specifications of the module.

## 1791ES-IB16 and 1791ES-IB8XOBV4 Modules North American Hazardous Location Approval

The following information applies when operating this equipment in hazardous locations:

Products marked "CL I, DIV 2, GP A, B, C, D" are suitable for use in Class I Division 2 Groups A, B, C, D, Hazardous Locations and nonhazardous locations only. Each product is supplied with markings on the rating nameplate indicating the hazardous location temperature code. When combining products within a system, the most adverse temperature code (lowest "T" number) may be used to help determine the overall temperature code of the system. Combinations of equipment in your system are subject to investigation by the local authority having jurisdiction at the time of installation.

<!-- image -->

## WARNING: EXPLOSION HAZARD

- Do not disconnect equipment unless power has been removed or the area is known to be nonhazardous.
- Do not disconnect connections to this equipment unless power has been removed or the area is known to be nonhazardous. Secure any external connections that mate to this equipment by using screws, sliding latches, threaded connectors, or other means provided with this product.
- Substitution of components may impair suitability for Class I, Division 2.
- If this product contains batteries, they must be changed only in an area known to be nonhazardous.

Informations sur l'utilisation de cet équipement en environnements dangereux: Les produits marqués "CL I, DIV 2, GP A, B, C, D" ne conviennent qu'à une utilisation en environnements de Classe I Division 2 Groupes A, B, C, D dangereux et non dangereux. Chaque produit est livré avec des marquages sur sa plaque d'identification qui indiquent le code de température pour les environnements dangereux. Lorsque plusieurs produits sont combinés dans un système, le code de température le plus défavorable (code de température le plus faible) peut être utilisé pour déterminer le code de température global du système. Les combinaisons d'équipements dans le système sont sujettes à inspection par les autorités locales qualifiées au moment de l'installation.

<!-- image -->

## WARNING: RISQUE D'EXPLOSION

- Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher l'équipement.
- Couper le courant ou s'assurer que l'environnement est classé non dangereux avant de débrancher les connecteurs. Fixer tous les connecteurs externes reliés à cet équipement à l'aide de vis, loquets coulissants, connecteurs filetés ou autres moyens fournis avec ce produit.
- La substitution de composants peut rendre cet équipement inadapté à une utilisation en environnement de Classe I, Division 2.
- S'assurer que l'environnement est classé non dangereux avant de changer les piles.

## Follow Precautions for Use

Follow the precautions for use listed here and throughout this manual.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

ATTENTION: Follow Safety Standards for Installation and Testing

- Use only appropriate components or devices complying with relevant safety standards corresponding to the required safety category and safety integrity level:
- Conformity to requirements of the safety category and safety integrity level must be determined for the entire system.
- We recommend you consult a certification body regarding assessment of conformity to the required safety integrity level or safety category.
- You must confirm compliance with the applicable standards for the entire system.
- Perform testing to confirm that all device configuration data and operation is correct before starting system operation.
- After installation of the module, a safety administrator must confirm the installation and conduct trial operation and maintenance procedures.

ATTENTION: Personnel responsible for the application of safety-related programmable electronic systems (PES) shall be aware of the safety requirements in the application of the system and shall be trained in using the system.

ATTENTION: Do not disassemble, repair, or modify the module. Any changes to the module can result in the loss of safety functions.

In case of malfunction or damage, no attempts at repair should be made. The module should be returned to the manufacturer for repair. Do not dismantle the module.

ATTENTION: Do not use EtherNet/IP standard I/O data or explicit message data as safety data.

ATTENTION: Installing or Replacing Modules

- When installing or replacing modules, clear any previous configuration before connecting the module to the network or connecting input or output power to the module.
- When replacing a device, configure the replacement device suitably and confirm that it operates correctly.

## I/O Module Overview

The Guard I/O modules implement the CIP Safety™ protocol extensions over EtherNet/IP networks and provide various features for a safety system.

Use the modules to construct a safety-control network system that meets the following requirements, up to and including:

- Safety Integrity Level Claim Limit 3 (SIL CL 3), as defined in IEC 61508
- Category 4 (CAT. 4), Performance Level e (PLe), as defined in ISO 13849-1

Remote I/O communication for safety I/O data is performed through safety connections that support CIP Safety over an EtherNet/IP network, and data processing is performed in the safety controller.

A safety controller monitors the status and fault diagnostics of the I/O modules through a safety connection by using a new or existing EtherNet/IP network.

The following is a list of features common to Guard I/O modules:

- CIP Safety and EtherNet/IP protocol conformance
- Safety inputs
- – Safety devices, such as emergency stop push buttons, gate switches, and safety light curtains, can be connected.
- – Dual-channel mode evaluates consistency between two input signals (channels), which allows use of the module for Safety Category 3 and 4.
- – Single-channel evaluates one input signal (channel). This evaluation allows use of the module Safe Inputs for safety Category 2 and in applications rated up to and including Performance Level d / SIL CL2.
- – The time of a logical discrepancy between two channels can be monitored by using a discrepancy time setting.
- – An external wiring short circuit check is possible when inputs are wired in combination with test outputs.
- – Independently adjustable on and off delay is available per channel.
- Test outputs
- – Separate test outputs are provided for short circuit detection of a safety input (or inputs).
- – Power (24V) can be supplied to devices, such as safety sensors.
- – Test outputs can be configured as standard outputs.
- – All Guard I/O modules have numerous test outputs, of which some can be used for broken wire detection of a muting lamp.
- Safety outputs
- – Dual-channel mode evaluates consistency between two output signals (channels).
- – Safety outputs can be pulse tested to detect field wiring shorts to 24V DC and 0V DC.
- I/O status data – The module includes status data for monitoring I/O circuits and I/O data.
- Removable I/O connectors (only 1791ES modules) – I/O connectors support mechanical keying.
- Network address translation (NAT) support – Available in Logix Designer version 24 or later, NAT is a service that translates one IP address to another IP address via a NAT-configured switch. The switch translates the source and destination addresses within data packets as traffic passes between subnets. This service is useful if you must reuse IP addresses throughout a network. For example, with NAT, you can segment devices that share one IP address on a private subnet into multiple identical private subnets while maintaining unique identities on the public subnet.

See Table 6 for a description of the Guard I/O modules.

## Table 6 - Guard I/O Module Descriptions

| Catalog Number Description Enclosure Type Rating                                                     | Safety Inputs Test Outputs (1)  Safety Outputs (solid-state)                                            |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| 1791ES-IB16 CompactBlock™ safety input module Meets IP20 16 16 —                                     |                                                                                                         |
| 1791ES-IB16 CompactBlock™ safety input module Meets IP20 16 16 —                                     | 1791ES-IB8XOBV4 CompactBlock safety I/O module with solid-state outputs 8 8 8 bipolar outputs (4 pairs) |
| 1732ES-IB12XOB4 ArmorBlock® safety I/O module with solid-state outputs Meets IP65/IP67 (when marked) | 12 12 4 sourcing outputs                                                                                |
| 1732ES-IB12XOB4 ArmorBlock® safety I/O module with solid-state outputs Meets IP65/IP67 (when marked) | (when marked) 1732ES-IB12XOBV2 ArmorBlock safety I/O module with solid-state outputs 12 12 4 bipolar outputs (2 pairs)                                                                                                         |
| 1732ES-IB16 ArmorBlock safety input module Meets IP65/IP67 (when marked)                             | 16 16 —                                                                                                 |
| 1732ES-IB8XOB8 ArmorBlock safety I/O module with solid-state outputs Meets IP65/IP67 (when marked)   | 8 8 8 sourcing outputs                                                                                  |
| 1732ES-IB8XOBV4 ArmorBlock safety I/O module with solid-state outputs Meets IP65/IP67 (when marked)  | 8 8 8 bipolar outputs (4 pairs)                                                                         |

## Selecting a Power Supply

For CE LVD compliance, verify that the external power supply that provides power to the modules is safety extra low voltage (SELV) rated. Some Rockwell Automation® Bulletin 1606 power supplies are SELV-compliant. See Switched Mode Power Supply Specifications Technical Data, publication 1606-TD002 , and the installation instructions for the modules.

<!-- image -->

<!-- image -->

## ATTENTION: Prevent Electric Shock

To prevent electric shock, use a DC power supply that meets the following requirements:

- A DC power supply with double or reinforced insulation; for example, according to IED/EN 60950, or EN 50178, or a transformer according to IEC/EN 61558.
- A DC power supply satisfies requirement for class 2 circuits or limited voltage/current circuit stated in UL 508.
- An external power supply that is safety extra-low voltage (SELV) rated.
- Do not apply DC voltages exceeding the rated voltages to the module.
- Apply properly specified voltages to the module inputs. Applying inappropriate voltages causes the module to fail to perform its specified function, which leads to loss of safety functions or damage to the module.

## ATTENTION: Do Not Exceed Specified Voltage

## Programming Requirements Use the minimum software versions listed here.

|                   | Cat. No. Studio 5000 Logix Designer® Version (1)   | RSLogix 5000® Software Version  (1) (EtherNet/IP Network)   |
|-------------------|----------------------------------------------------|-------------------------------------------------------------|
| 1791ES-IB16 21 16 |                                                    |                                                             |
| 1791ES-IB8XOBV4   |                                                    |                                                             |
| 1732ES-IB12XOB4   |                                                    |                                                             |
| 1732ES-IB12XOBV2  |                                                    |                                                             |
| 1732ES-IB16 18    |                                                    |                                                             |
| 1732ES-IB8XOB8    |                                                    |                                                             |
| 1732ES-IB8XOBV4   |                                                    |                                                             |

(1) This version or later.

Safety controllers control the safety outputs. Safety or standard controllers can control the standard outputs. Use Guard I/O modules in EtherNet/IP safety architectures as shown in Figure 14. The Guard I/O family is a set of I/O modules that when connected to an EtherNet/IP safety network are suitable for applications up to and including:

- SIL CL 3 as defined in IEC 61508
- CAT. 4, PLe, as defined in ISO 13849-1

Figure 14 - Safety Interlocking and Control Via CIP Safety (linear and star topology)

<!-- image -->

## CIP Safety in EtherNet/IP Safety Architectures

## Device Level Ring (DLR)

A DLR network is a single-fault-tolerant ring network that is intended for the interconnection of automation devices without the need for more switches.

The ring topology offers these advantages:

- Media redundancy
- Fast-network fault detection and reconfiguration
- Resiliency of a single-fault-tolerant network
- Easy implementation without more hardware requirements

## IMPORTANT

This section summarizes a DLR network. To plan, configure, and monitor DLR networks, see EtherNet/IP Embedded Switch Technology Application Guide, publication ENET-AP005 .

One DLR network can support as many as 50 nodes. A DLR network supports copper connections (maximum of 100 m), fiber-optic connections (maximum of 2 km), or a mix of copper and fiber.

Figure 15 - Safety Interlocking and Control Via CIP Safety (DLR topology) Only 1732ES Modules

<!-- image -->

IMPORTANT

Only one DLR ring is supported per active Stratix® 5700 switch.

## A DLR network includes the following nodes.

| Node Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Supervisor node A DLR network requires at least one node to be configured as ring supervisor. IMPORTANT: By default, the supervisor function is disabled on supervisor-capable devices, so they are ready to participate in a linear/star network or as a ring node on a DLR network. In a DLR network, you must configure at least one of the supervisor-capable devices as the ring supervisor before physically connecting the ring. If you do not, the DLR network does not work. The ring supervisor provides these main functions: • Manages traffic on the DLR network • Collects diagnostic information for the network We recommend that you do the following: • Configure at least one back-up supervisor. • Configure the desired active ring supervisor with a numerically higher precedence value as compared to the back-up supervisors. • Track the supervisor-precedence values for all supervisor-enabled nodes in the DLR network. |
| Ring node A ring node is any node that operates on the network to process data that is transmitted over the network. A ring node  can also pass on the data to the next node on the network. When a fault occurs on the DLR network, the ring nodes reconfigure themselves and relearn the network topology. Additionally, ring nodes can report fault locations to the active ring supervisor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Identify Major Parts of the Module

See Figure 16 and Figure 17 for module identification. See Chapter 3 for pinout information.

Figure 16 - 1791ES Module Connections and Indicators

<!-- image -->

Figure 17 - 1732ES Module Connection and Indicators

<!-- image -->

## Notes:

## Environment and Enclosure

## Install the Module

| Topic Page                              |
|-----------------------------------------|
| Environment and Enclosure 39            |
| Prevent Electrostatic Discharge 41      |
| Environmental Considerations for Use 42 |
| Follow Wiring Precautions 42            |
| Follow DC Power Supply Precautions 45   |
| Mount the Module 45                     |
| Make Connections for 1791ES Modules 52  |
| Make Connections for 1732ES Modules 55  |

Read and understand this section before you begin to install the module.

## For 1791ES Modules

<!-- image -->

ATTENTION: This equipment is intended for use in a Pollution Degree 2 industrial environment, in overvoltage Category II applications (as defined in IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment is not intended for use in residential environments and may not provide adequate protection to radio communication services in such environments.

This equipment is supplied as open-type equipment for indoor use. It must be mounted within an enclosure that is suitably designed for those specific environmental conditions that will be present and appropriately designed to prevent personal injury resulting from accessibility to live parts. The enclosure must have suitable flame-retardant properties to prevent or minimize the spread of flame, complying with a flame spread rating of 5VA, or be approved for the application if non-metallic. The interior of the enclosure must be accessible only by the use of a tool. Subsequent sections of this publication may contain additional information regarding specific enclosure type ratings that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for more installation requirements.
- NEMA Standard 250 and EN/IEC 60529, as applicable, for explanations of the degrees of protection provided by enclosures.

<!-- image -->

<!-- image -->

ATTENTION: 1791ES modules are certified for use only within the surrounding air temperature range of -20…+60 °C (-4…+140 °F). The 1791ES modules must not be used outside of this range.

<!-- image -->

WARNING: Do not replace components or disconnect equipment unless power has been switched off or the area is known to be free of ignitable concentrations.

## For 1732ES Modules

<!-- image -->

This equipment is intended for use in overvoltage Category II applications (as defined in IEC 60664-1), at altitudes up to 2000 m (6562 ft) without derating.

This equipment is not intended for use in residential environments and may not provide adequate protection to radio communication services in such environments.

This equipment is supplied as enclosed equipment. It should not require additional system enclosure when used in locations consistent with the enclosure type ratings stated in the Specifications section of this publication. Subsequent sections of this publication may contain more information regarding specific enclosure type ratings, beyond what this product provides, that are required to comply with certain product safety certifications.

In addition to this publication, see the following:

- Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1, for more installation requirements.
- NEMA Standard 250 and EN/IEC 60529, as applicable, for explanations of the degrees of protection provided by enclosures.

ATTENTION: All 1732ES modules EXCEPT the 1732ES-IB16 module are certified for use only within the surrounding air temperature range of -20…+55 °C (-4…+131 °F). All 1732ES modules EXCEPT the 1732ES-IB16 modules must not be used outside of this range. The 1732ES-IB16 module is certified for use only within the surrounding air temperature range of -20…+60 °C (-4…+140 °F). The 1732ES-IB16 module must not be used outside of this range.

<!-- image -->

## Prevent Electrostatic Discharge

<!-- image -->

Install the Module

Chapter 3

ATTENTION: This equipment is sensitive to electrostatic discharge, which can cause internal damage and affect normal operation. Follow these guidelines when you handle this equipment:

- Touch a grounded object to discharge potential static.
- Wear an approved grounding wriststrap.
- Do not touch connectors or pins on component boards.
- Do not touch circuit components inside the equipment.
- Use a static-safe workstation, if available.
- Use only a soft dry anti-static cloth to wipe down equipment. Do not use any cleaning agents.
- Store the equipment in appropriate static-safe packaging when not in use.

## Environmental Considerations for Use

## Follow Wiring Precautions

Do not use the module in locations that are subject to these conditions:

- Direct sunlight
- Temperatures or humidity beyond the ranges noted in Specifications on page 161
- Condensation as the result of severe changes in temperature
- Corrosive or flammable gases
- Dust, especially iron dust (only 1791ES modules)
- Salts
- Water (only 1791ES modules)
- Oil or chemicals
- Shock or vibration beyond the range noted in Specifications on page 161

Do not clean the modules with these materials:

- Acetone
- Benzene
- Thinner

<!-- image -->

WARNING: Connecting and Disconnecting Wiring and Cables

- When you connect or disconnect the removable terminal block (RTB) or power cables with field-side power applied, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.
- If you connect or disconnect wiring or cables while the field-side power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.
- If you connect or disconnect the communication cables with power applied to this module or any device on the network, an electrical arc can occur. This could cause an explosion in hazardous location installations.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## ATTENTION: Wiring Guidelines

- Disconnect the module from the power supply before wiring or connecting cables. Devices connected to the module can operate unexpectedly if wiring is performed while power is supplied.
- Wire correctly after confirming the signal names of all terminals.
- Wire the Guard I/O™ modules properly so that 24V DC line does not touch the safety outputs accidentally or unintentionally.
- Do not route communication, input, or output wiring with conduit containing high voltage. Refer to Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1 .
- Wire conductors correctly and verify operation of the module before placing the system into operation. Incorrect wiring can lead to loss of safety function.

ATTENTION: Be Aware of Safety Requirements

Personnel responsible for the application of safety-related programmable electronic systems (PES) shall be aware of the safety requirements in the application of the system and shall be trained in using the system.

ATTENTION: Electrical Safety Considerations

To comply with the CE Low Voltage Directive (LVD), all connections to this equipment must be powered from a source compliant with the following:

- Safety Extra Low Voltage (SELV) Supply.
- Protected Extra Low Voltage (PELV) Supply.

If the devices (sensors) connected to the input connections require Class 2 power to operate, the auxiliary power connections of this equipment must be powered by a Class 2 source.

ATTENTION: Maintain IP Rating for 1732ES Modules

Make sure all connectors and caps on 1732ES modules are securely tightened to properly seal the connections against leaks and maintain IP enclosure type requirements.

Applicable only to 1732ES modules.

<!-- image -->

<!-- image -->

ATTENTION: You can configure Test Outputs to be used as standard outputs. You can connect actuators to Test Output points that are expecting a Standard configuration.

Test Output points configured as Pulse Test or Power Supply become active whenever you apply input power to the module. These configured functions are independent of the I/O connections to the module.

ATTENTION: If a module with Test Outputs configured as Pulse Test or Power Supply is incorrectly installed in an application where actuators are connected to these Test Output points, the actuators are activated when input power is applied.

To prevent this possibility, follow these procedures.

- When installing a module, be sure that the module is correctly configured for the application or in the out-of-box condition before applying input power.
- When replacing a module, be sure that the module is correctly configured for the application or in the out-of-box condition before applying input power.
- Reset modules to their out-of-box condition when removing them from an application.
- Be sure that all modules in replacement stock are in their out-of-box condition.

## Follow DC Power Supply Precautions

## Mount the Module

<!-- image -->

Install the Module

Chapter 3

ATTENTION: To prevent electric shock, use a DC power supply that meets these requirements:

- A DC power supply with double or reinforced insulation, for example, according to IED/EN 60950 or EN 50178 or a transformer according to IEC/EN 61558.
- A DC supply satisfies requirement for class 2 circuits or limited voltage/ current circuit stated in UL 508.
- Use an external power supply that is safety extra-low voltage (SELV) rated.
- Follow these precautions for safe use.
- Wire conductors correctly and verify operation of the module before placing the system into operation. Incorrect wiring can lead to loss of safety function.
- Do not apply DC voltages exceeding the rated voltages to the module.
- Apply properly specified voltages to the module inputs. Applying inappropriate voltages causes the module to fail to perform its specified function, which leads to loss of safety functions or damage to the module.
- Never use test outputs as safety outputs. Test outputs are not safety outputs.
- Note that after installation of the module, a safety administrator must confirm the installation and conduct trial operation and maintenance.
- Do not disassemble, repair, or modify the module. This can result in loss of safety functions.
- Use only appropriate components or devices complying with relevant safety standards corresponding to the required safety category and safety integrity level.
- Conformity to requirements of the safety category and safety integrity level must be determined for the entire system.
- We recommend you consult a certification body regarding assessment of conformity to the required safety integrity level or safety category.
- Note that you must confirm compliance with the applicable standards for the entire system.
- Disconnect the module from the power supply before wiring. Devices connected to the module can operate unexpectedly if wiring is performed while power is supplied.

Follow these guidelines to mount the module:

- Modules can be mounted horizontally or vertically.
- Do not mount the module near any heat source that can increase the operating temperature of the module.
- 1732ES modules meet IP65/IP67 (when marked).
- Mount catalog number 1791ES-IB16 and 1791ES-IB8XOBV4 modules in an enclosure rated IP54 (IEC60529) or higher.

## Module Spacing

Leave minimum spacing to the wiring duct or other objects for adequate ventilation and room for wiring.

Figure 18 - Required Spacing for 1791ES-IB16 and 1791ES-IB8XOBV4 Modules

<!-- image -->

Use horizontal or vertical mounting.

Figure 19 - Required Spacing for 1732ES Modules

<!-- image -->

Wiring Duct or Other Object

## Mount the 1791ES Modules on a DIN Rail

Use a DIN rail that is 35 mm (1.38 in.) wide to install the module in the control panel. Secure the 35 mm (1.4 in.) DIN rail properly with fasteners every 200 mm (7.87 in.). Use an end plate on each end of the module to secure it to the DIN rail.

Follow these steps to mount the module on a DIN rail.

1. To lock them in the open position, pry open the two gray latches.
2. Hook the module over the top of the DIN rail.
3. Rotate the module down until it makes full contact with the DIN rail.
4. To secure the module to the rail, snap the latches back into place.
5. Verify that the module is securely attached to the DIN rail.

<!-- image -->

<!-- image -->

Grounding

<!-- image -->

ATTENTION: This product is grounded through the DIN-rail-to-chassis ground. Use zinc plated chromate-passivated steel DIN rail to assure proper grounding. The use of other DIN rail materials (for example, aluminum and plastic) that can corrode, oxidize, or are poor conductors, can result in improper or intermittent grounding. Secure the DIN rail to the mounting surface approximately every 200 mm (7.87 in.) and use end plates to secure the product to the DIN rail.

## Mount the 1732ES Modules on a Wall or Panel

To mount the module on a wall or panel, use the screw holes provided in the module.

<!-- image -->

ATTENTION: To meet safety and EMC requirement this module must be mounted on a flat conductive and fireproof surface.

Follow these steps to mount the module.

1. To lay out the drill locations, use the mounting holes in the module as a guide.
2. Mark the center of drill location with a pencil or marker.
3. Use a center punch to mark the drill locations.
4. Use a 4.5 mm (0.177 in.) drill to make the pilot holes.
5. Mount the module with two #8 (M4) screws.

<!-- image -->

Figure 20 - 1732ES Module Physical Dimensions

<!-- image -->

<!-- image -->

(10.17 in)

<!-- image -->

## Mount the Module in High Vibration Areas

If you mount the module in an area that is subject to shock or vibration, use a flat washer and a lock washer to mount the module.

<!-- image -->

Torque the mounting screws to 0.68 N·m (6 lb·in.).

## Grounding the 1732ES Modules

This figure shows the grounding features for the 1732ES modules.

<!-- image -->

## Functional Earth Ground for Ethernet

The mounting screw at the top of the module is for the complex Ethernet shield grounding features. The rectangular 'shorting' bar is held in place by a conductive screw/washer combination that connects electrically to the metal shields of the Ethernet connectors internal to the module.

To ground the Ethernet shields at the module, leave the factory-installed 'shorting' bar with the conductive screw/washer combination in place. You

## Make Connections for 1791ES Modules

must also mount the module to an earth-grounded, conductive surface with conductive mounting hardware.

If you do not want to ground the Ethernet shields at the module, remove the 'shorting' bar and conductive screw/washer combination and mount the module to wall or panel.

TIP If the Ethernet shields are not grounded at the module, the mounting screw at the Ethernet end of the module is not required to make a connection with earth ground.

## Functional Earth Ground for EMC

The mounting screw at the bottom of the module is required to be a conductive screw for EMC compliance. Mount the module to an earthgrounded, conductive surface by using conductive mounting hardware to make the required connection with earth ground.

Follow these guidelines when wiring the module:

- For stranded wire, install an insulation-covered ferrule (DIN 46228-4 standard compatible-type) at the ends before you connect wires.
- Torque screws for the power connector to 0.56…0.79 N·m (5…7 lb·in).
- Torque screws for the I/O connectors to 0.5…0.56 N·m (4.5…5 lb·in).

See the Ethernet Design Considerations Reference Manual, publication ENET-RM002, for information about Ethernet cable.

## Power Connections

See Table 7 for a description of the pins in the power connector.

Table 7 - Power Connector Pin Descriptions

| Pin No. Signal             |
|----------------------------|
| 1 Input +24V DC power      |
| 2 Input power common       |
| 3 Output +24V DC power (1) |
| 4 Output power common (1)  |

<!-- image -->

## EtherNet/IP Connections

See Table 8 for a description of the pins in the EtherNet/IP connector.

Table 8 - EtherNet/IP Connector Pin Descriptions

<!-- image -->

| Pin No. Signal        |
|-----------------------|
| 8 No connection       |
| 7 No connection       |
| 6 Receive data minus  |
| 5 No connection       |
| 4 No connection       |
| 3 Receive data plus   |
| 2 Transmit data minus |
| 1 Transmit data plus  |

## I/O Connections

For wiring diagrams, see Wiring Examples on page 63 .

## IMPORTANT

Because the I/O connector has a structure that helps prevent incorrect wiring, make connections at the specified locations that correspond to the terminal numbers.

See Figure 21 for a description of the pins in the I/O connector.

Figure 21 - I/O Connector Pin Descriptions

<!-- image -->

Table 9 - Terminal Positions for I/O Field Power

| Terminal No. Signal Terminal No. Signal   |                                      |
|-------------------------------------------|--------------------------------------|
|                                           | 1 Input +24V DC 3 Output +24V DC (1) |
|                                           | 2 Input -24V DC 4 Output -24V DC (1) |

(1) Applies only to catalog number 1791ES-IB8XOBV4 module.

Table 10 - Terminal Positions for Terminal Numbers 1…18

| Terminal No. Signal Terminal No. Signal    |                                         |
|--------------------------------------------|-----------------------------------------|
| 1 Functional earth 10 Safety input 4       |                                         |
| 2 Safety input 0 11 Safety input 5         |                                         |
| 3 Safety input 1 12 Test output 4          |                                         |
| 4 Test output 0 13 Test output 5           |                                         |
|                                            | 5 Test output 1 14 Safety input 6       |
| 6 Safety input 2 15 Safety input 7         |                                         |
| 7 Safety input 3 16 Test output 6          |                                         |
|                                            | 8 Test output 2 17 Test output 7/muting |
| 9 Test output 3/muting 18 Functional earth |                                         |

Table 11 - Terminal Positions for Numbers 19…34

| Terminal No. Signal                                          | Terminal No. Signal                          |
|--------------------------------------------------------------|----------------------------------------------|
| Cat. No. 1791ES-IB8XOBV4 Module Cat. No. 1791ES-IB16 Module  |                                              |
| 19 Safety output 0 (1) /switch +24V DC                       | Safety input 8                               |
| 20 Safety output 1 (1)/ switch 24V DC common Safety input 9  |                                              |
| 21 L-/24V DC common Test output 8                            |                                              |
|                                                              | 22 S+/24V DC Test output 9                   |
| 23 Safety output 2 (2) /switch +24V DC                       | Safety input 10                              |
| 24 Safety output 3 (2)                                       | /switch 24V DC common Safety input 11/muting |
| 25 L-/24V DC common Test output 10                           |                                              |
|                                                              | 26 S+/24V DC Test output 11                  |
| 27 Safety output 4 (3) /switch +24V DC                       | Safety input 12                              |
| 28 Safety output 5 (3) /switch 24V DC common Safety input 13 |                                              |
| 29 L-/24V DC common Test output 12                           |                                              |
|                                                              | 30 S+/24V DC Test output 13                  |
| 31 Safety output 6 (4) /switch+24V DC                        | Safety input 14                              |
| 32 Safety output 7 (4) /switch 24V DC common Safety input 15 |                                              |
| 33 L-/24V DC common Test output 14                           |                                              |
|                                                              | 34 S+/24V DC Test output 15/muting           |

## Make Connections for 1732ES Modules

See the Ethernet Design Considerations Reference Manual, publication ENET-RM002, for information about Ethernet cable.

## Power Connections

This section describes the power connectors and recommended cables.

| Pin No. Signal             |
|----------------------------|
| 1 Output +24V DC power (1) |
| 2 Input +24V DC power      |
| 3 Input power, common      |
| 4 Output power, common (1) |

<!-- image -->

Table 13 - Recommended Power Cables

| Description Cat. No.                                                     |
|--------------------------------------------------------------------------|
| Mini right angle female to flying leads cord set 889N-R4AFC-6F (1)       |
| Mini straight female to flying leads cord set 889N-F4AFC-6F (1)          |
| Mini right angle male to flying leads cord set 889N-E4AFC-6F (1)         |
| Mini straight male to flying leads cord set 889N-M4AFC-6F (1)            |
| Mini right angle male to right angle female patch cord 889N-R4AFNE-2 (2) |
| Mini straight male to straight female patch cord 889N-F4AFNM-2 (2)       |

See http://www.ab.com/en/epub/catalogs/6005557/6005561/10508712/ 10513424/10513435/Introduction.html for more information.

## Power Pass Through

The power that the module requires is supplied via a 4-pin mini-style connector system. The module receives its required power through the male connector on the left. A female connector on the right is also provided so that power can be daisy chained from module to module.

IMPORTANT

Use power pass through (daisy chaining of power) only for 'de-energize to trip' (safety state = OFF) applications.

Most 1732ES modules require two 24V DC (nominal) supplies. These supplies are called the 'input +24V DC power' and the 'output +24V DC power'. The input +24V DC power provides power for the module control and Ethernet portions of the module, the safety input/test output circuits, and the test output loads. The output +24V DC power provides power for the safety output circuits and the safety output loads. Since the 1732ES-IB16 module has no safety outputs, it requires only one 24V DC (nominal) power supply to provide 'input +24V DC power'.

Internally, the input +24V DC power and output +24V DC power are isolated from each other.

## IMPORTANT

The maximum current that any pin on the power connectors can carry is 10 A.

The input +24V DC power current that is required for a module in the daisy chain can be estimated as described here.

I IP ~ I IPM + I TO + I IPDC

Where:

I IP is the input +24V DC power current through the male power connector of the module.

I IPM is the input +24V DC power current required by the module itself (with no test output load current).

I TO is the total test output load current for test outputs N (0…11).

I IPDC is the total input +24V DC power current through the female power connector of the module (input +24V DC power current for the modules that follow in the daisy chain).

I IPM can be approximated by dividing the number of watts for each type of 1732ES module by +24V DC as listed here:

- 1732ES-IB12XOB4, 1732ES-IB12XOBV2 = 4.2 W
- 1732ES-IB8XOB8, 1732ES-IB8XOBV4 = 3.96 W
- 1732ES-IB16 = 4.56 W

The table input +24V DC power calculation shows an example input +24V DC power current calculation for a system of four 1732ES-IB12XOB4 modules. The input +24V DC power voltage is 24V DC in this example. Module 1 is the first module in the daisy chain. Fill out the table by starting with the last module in the daisy chain, in this example Module 4. Once IIP is calculated for module 4, it transfers as the I IPDC value for Module 3. This process continues for all modules in the daisy chain.

As shown in the cell with value set in bold, the maximum input +24V DC power current through the male power connectors in the daisy chain is 6.5 A. This value is less than 10 A, so this system is adequate. The IIP value for a module in this system or any daisy chained system cannot exceed 10 A. If the value exceeds 10 A, the system fails to meet the maximum current requirement for the module. The maximum current requirement is the maximum current that any pin on the power connectors can carry, which is 10 A.

Table 14 - Input +24V DC Power Calculation

|        |         | Value Module 1 Module 2 Module 3 Module 4   |
|--------|---------|---------------------------------------------|
| I IPDC |         | 4.875 A 3.250 A 1.625 A 0.000 A             |
| I IPM  |         | 0.175 A 0.175 A 0.175 A 0.175 A             |
| I TO0  |         | 0.005 A 0.005 A 0.005 A 0.700 A             |
| I TO1  |         | 0.005 A 0.005 A 0.005 A 0.700 A             |
| I TO2  |         | 0.005 A 0.005 A 0.700 A 0.005 A             |
| I TO3  |         | 0.005 A 0.005 A 0.700 A 0.005 A             |
| I TO4  |         | 0.005 A 0.700 A 0.005 A 0.005 A             |
| I TO5  |         | 0.005 A 0.700 A 0.005 A 0.005 A             |
| I TO6  |         | 0.700 A 0.005 A 0.005 A 0.005 A             |
| I TO7  |         | 0.700 A 0.005 A 0.005 A 0.005 A             |
| I TO8  |         | 0.005 A 0.005 A 0.005 A 0.005 A             |
| I TO9  |         | 0.005 A 0.005 A 0.005 A 0.005 A             |
| I TO10 |         | 0.005 A 0.005 A 0.005 A 0.005 A             |
| I TO11 |         | 0.005 A 0.005 A 0.005 A 0.005 A             |
| I IP   | 6.500 A | 4.875 A 3.250 A 1.625 A                     |

The output +24V DC power current that is required for a module in the daisy chain can be estimated as described here.

I OP ~ I OPM + I SO + I SNSO + I OPDC

Where:

I OP is the output +24V DC power current through the male power connector of the module.

I OPM is the output +24V DC power current required by the module itself (with no safety output load current).

I SO is the total safety output load current for safety outputs N. Modules with bipolar safety outputs enter values only in the even numbered ISO table locations. Modules with sourcing-only safety outputs enter values in all ISO table locations.

I SNSO is the total sensor output load current for the Output +24V DC power output pins (pin 1 in the output I/O connectors).

I OPDC is the total output +24V DC power current through the female power connector of the module (output +24V DC power current for the modules that follow in the daisy chain).

I OPM can be approximated by dividing the number of watts for each type of 1732ES module by +24V DC as listed here:

- 1732ES-IB12XOBV2 - 1.56W
- 1732ES-IB12XOB4 - 1.08W
- 1732ES-IB8XOB8 - 1.56W
- 1732ES-IB8XOBV4 - 2.64 W

The table output +24V DC power calculation shows an example output +24V DC power current calculation for a system of four modules. The output +24V DC power voltage is 24V DC in this example. Module 1 is the first module in the daisy chain. Modules 1 and 3 are 1732ES-IB12XOBV2 modules and have bipolar safety outputs. Modules 2 and 4 are 1732ES-IB12XOB4 modules and have sourcing safety outputs. Fill out the table by starting with the last module in the daisy chain, in this example Module 4. Once IOP is calculated for module 4, it transfers as the I OPDC value for Module 3. This process continues for all modules in the daisy chain.

As can be seen in the cell with value set in bold, the maximum output +24V DC power current through the male power connectors in the daisy chain is 9.02 A. This value is less than 10 A, so this system is adequate. The IOP value for a module in this system or any daisy chained system cannot exceed 10 A. If the value exceeds 10 A, the system fails to meet the maximum current requirement for the module. The maximum current requirement is the maximum current that any pin on the power connectors can carry, which is 10 A.

Table 15 - Output +24V DC Power Calculation

|        | Value Module 1 Module 2 Module 3 Module 4   |                                 |
|--------|---------------------------------------------|---------------------------------|
| I opdc |                                             | 6.755 A 4.600 A 2.245 A 0.000 A |
| I opm  |                                             | 0.065 A 0.045 A 0.065 A 0.045 A |
| I so0  |                                             | 1.000 A 0.500 A 1.000 A 0.500 A |
| I so1  |                                             | – 0.500 A – 0.500 A             |
| I so2  |                                             | 1.000 A 0.500 A 1.000 A 0.500 A |
| I so3  |                                             | – 0.500 A – 0.500 A             |
| I so4  |                                             | ––––                            |
| I so5  |                                             | ––––                            |
| I so6  |                                             | ––––                            |
| I so7  |                                             | ––––                            |
| I SNSO |                                             | 0.200 A 0.200 A 0.200 A 0.200 A |
| I op   | 9.020 A                                     | 6.755 A 4.600 A 2.245 A         |

<!-- image -->

ATTENTION: To comply with the CE Low Voltage Directive (LVD), this equipment and all connected I/O must be powered from a source compliant with Safety Extra Low Voltage (SELV) or Protected Extra Low Voltage (PELV).

## EtherNet/IP Connections

This section describes the EtherNet/IP connector and sample cables.

<!-- image -->

Table 16 - EtherNet/IP Connector Pin Description

| Pin No. Signal   |
|------------------|
| 1 Tx+            |
| 2 Rx+            |
| 3 Tx                  |
| 4 Rx                  |
| 5 Shell/Shield   |

Table 17 - Sample EtherNet/IP Cables

| Description Cat. No.                                                    |
|-------------------------------------------------------------------------|
| M12 D-Coded straight to RJ45 patchcord 1585D-M4UBJM-2 (1)               |
| M12 D-Coded straight to flying leads cordset 1585D-M4UB-2 (1)           |
| M12 D-Coded straight to M12 straight patchcord 1585D-M4UBDM-2 (1)       |
| M12 D-Coded right angle to M12 right angle patchcord 1585D-E4UBDE-2 (1) |

See http://www.ab.com/en/epub/catalogs/6005557/6005561/10514505/ 10515166/Introduction.html for additional information.

Table 19 - Terminal Positions

| Terminal 1732ES-IB12XOBV2 1732ES-IB12XOB4 1732ES-IB16 1732ES-IB8XOBV4 1732ES-IB8XOB8   |
|----------------------------------------------------------------------------------------|
| A-1 Test out 1 Test out 1 Test out 1 Test out 1 Test out 1                             |
| A-2 Safety input 1 Safety input 1 Safety input 1 Safety input 1 Safety input 1         |
| A-3 Input common Input common Input common Input common Input common                   |
| A-4 Safety input 0 Safety input 0 Safety input 0 Safety input 0 Safety input 0         |
| A-5 Test out 0 Test out 0 Test out 0 Test out 0 Test out 0                             |
| B-1 Test out 3 Test out 3 Test out 3 Test out 3 Test out 3                             |
| B-2 Safety input 3 Safety input 3 Safety input 3 Safety input 3 Safety input 3         |
| B-3 Input common Input common Input common Input common Input common                   |
| B-4 Safety input 2 Safety input 2 Safety input 2 Safety input 2 Safety input 2         |
| B-5 Test out 2 Test out 2 Test out 2 Test out 2 Test out 2                             |
| C-1 Test out 5 Test out 5 Test out 5 Test out 5 Test out 5                             |
| C-2 Safety input 5 Safety input 5 Safety input 5 Safety input 5 Safety input 5         |
| C-3 Input common Input common Input common Input common Input common                   |
| C-4 Safety input 4 Safety input 4 Safety input 4 Safety input 4 Safety input 4         |

## I/O Connections

This section describes the I/O connectors and recommended cables.

Table 18 - I/O Connector Pin Description

| Pin No. Input Signal I/O Connector Bipolar Output Signal                                                                                                                                                                   | Sourcing Output Signal   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| 1 Test out n+1 Output +24V DC power 2 Input n+1 Output n+1 (N) (sinking) 3 Input common Output power common 4 Input n Output n (P) (sourcing) 5 Test out n Output power common Case No connect No connect No connect 1 2 5 | Output +24V DC power     |
| 1 Test out n+1 Output +24V DC power 2 Input n+1 Output n+1 (N) (sinking) 3 Input common Output power common 4 Input n Output n (P) (sourcing) 5 Test out n Output power common Case No connect No connect No connect 1 2 5 | Output n+1               |
| 1 Test out n+1 Output +24V DC power 2 Input n+1 Output n+1 (N) (sinking) 3 Input common Output power common 4 Input n Output n (P) (sourcing) 5 Test out n Output power common Case No connect No connect No connect 1 2 5 | Output power common      |
| 1 Test out n+1 Output +24V DC power 2 Input n+1 Output n+1 (N) (sinking) 3 Input common Output power common 4 Input n Output n (P) (sourcing) 5 Test out n Output power common Case No connect No connect No connect 1 2 5 | Output n                 |
| 1 Test out n+1 Output +24V DC power 2 Input n+1 Output n+1 (N) (sinking) 3 Input common Output power common 4 Input n Output n (P) (sourcing) 5 Test out n Output power common Case No connect No connect No connect 1 2 5 | Output power common      |
| 1 Test out n+1 Output +24V DC power 2 Input n+1 Output n+1 (N) (sinking) 3 Input common Output power common 4 Input n Output n (P) (sourcing) 5 Test out n Output power common Case No connect No connect No connect 1 2 5 |                          |

Figure 22 - I/O Connector Positions

<!-- image -->

## Table 19 - Terminal Positions (Continued)

| Terminal 1732ES-IB12XOBV2 1732ES-IB12XOB4 1732ES-IB16 1732ES-IB8XOBV4 1732ES-IB8XOB8                |                                                                                                |
|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| C-5 Test out 4 Test out 4 Test out 4 Test out 4 Test out 4                                          |                                                                                                |
| D-1 Test out 7 Test out 7 Test out 7 Test out 7 Test out 7                                          |                                                                                                |
| D-2 Safety input 7 Safety input 7 Safety input 7 Safety input 7 Safety input 7                      |                                                                                                |
| D-3 Input common Input common Input common Input common Input common                                |                                                                                                |
| D-4 Safety input 6 Safety input 6 Safety input 6 Safety input 6 Safety input 6                      |                                                                                                |
| D-5 Test out 6 Test out 6 Test out 6 Test out 6 Test out 6                                          |                                                                                                |
|                                                                                                     | E-1 Test out 9 Test out 9 Test out 9 Output +24V DC power Output +24V DC power                 |
| E-2 Safety input 9 Safety input 9 Safety input 9 Safety output 1                                    | (1)  (N) (sinking) Safety output 1 (3)  (sourcing)                                             |
|                                                                                                     | E-3 Input common Input common Input common Output power common Output power common             |
| E-4 Safety input 8 Safety input 8 Safety input 8 Safety output 0                                    | (1)  (P) (sourcing) Safety output 0 (3)  (sourcing)                                            |
|                                                                                                     | E-5 Test out 8 Test out 8 Test out 8 Output power common Output power common                   |
|                                                                                                     | F-1 Test out 11 Test out 11 Test out 11 Output +24V DC power Output +24V DC power              |
| F-2 Safety input 11 Safety input 11 Safety input 11 Safety output 3                                 | (2)  (N) (sinking) Safety output 3 (4)  (sourcing)                                             |
|                                                                                                     | F-3 Input common Input common Input common Output power common Output power common             |
| F-4 Safety input 10 Safety input 10 Safety input 10 Safety output 2                                 | (2)  (P) (sourcing) Safety output 2 (4)  (sourcing)                                            |
|                                                                                                     | F-5 Test out 10 Test out 10 Test out 10 Output power common Output power common                |
| G-1 Output +24V DC power Output +24V DC power Test out 13 Output +24V DC power Output +24V DC power |                                                                                                |
| G-2 Safety output 1 (1)  (N) (sinking) Safety output 1 (3)                                          | (sourcing) Safety input 13 Safety output 5 (5)  (N) (sinking) Safety output 5 (7)  (sourcing)  |
| G-3 Output power common Output power common Input common Output power common Output power common    |                                                                                                |
| G-4 Safety output 0 (1)  (P) (sourcing) Safety output 0 (3)                                         | (sourcing) Safety input 12 Safety output 4 (5)  (P) (sourcing) Safety output 4 (7)  (sourcing) |
| G-5 Output power common Output power common Test out 12 Output power common Output power common     |                                                                                                |
| H-1 Output +24V DC power Output +24V DC power Test out 15 Output +24V DC power Output +24V DC power |                                                                                                |
| H-2 Safety output 3 (2)  (N) (sinking) Safety output 3 (4)                                          | (sourcing) Safety input 15 Safety output 7 (6)  (N) (sinking) Safety output 7 (8)  (sourcing)  |
| H-3 Output power common Output power common Input common Output power common Output power common    |                                                                                                |
| H-4 Safety output 2 (2)  (P) (sourcing) Safety output 2 (4)                                         | (sourcing) Safety input 14 Safety output 6 (6)  (P) (sourcing) Safety output 6 (8)  (sourcing) |
| H-5 Output power common Output power common Test out 14 Output power common Output power common     |                                                                                                |

Table 20 - Recommended I/O Connector Cables

| Description Cat. No.                                                |
|---------------------------------------------------------------------|
| M12 right-angle male to flying leads cordset 889D-E5AC-2 (1)        |
| M12 straight-male to flying leads cordset 889D-M5AC-2 (1)           |
| M12 right-angle male to straight female patchcord 889D-F5ACDE-2 (2) |
| M12 straight male to straight female patchcord 889D-F5ACDM-2 (2)    |

- (1) Replace -2 (2 m [6.6 ft]) with -5 (5 m [16.4 ft]) or -10 (10 m [32.8 ft]) for additional standard cable lengths.

(2) Replace -2 (2m [6.6 ft]) with -OM3 (0.3 m [1.0 f t]), -1 (1 m [3.3 ft]), -5 (5 m [16.4 ft]), or -10 (10 m [32.8 ft]) for additional standard cable lengths.

See http://www.ab.com/en/epub/catalogs/6005557/6005561/6125318/ 8613745/8613769/8613771/Introduction.html for additional information.

## Label the IP Address and Device Connections

The 1732ES module ships with 12 white labels that you can use to identify the IP address of the module, and the input and output connections. There are six areas on the module to place the labels, with six additional labels that can be used if the IP address or device connections change.

Use a pen or indelible marker with a fine tip to write on the labels. You can also use a printing device to print the data onto the label. Contact a Brady representative at http://www.bradyid.com and ask about printer compatibility for part number PTLEP-171-593.

<!-- image -->

IMPORTANT: Be sure that the surface of the module is clean and dry before you apply the labels to the module.

## Wiring Examples

| Topic Page                               |
|------------------------------------------|
| Wiring Examples for Safety Categories 64 |
| Wiring by Application 67                 |

For more examples, see the Safety Functions available at http://marketing.rockwellautomation.com/safety/en/safety\_functions .

You can also go to Literature Library at http://www.rockwellautomation.com/global/literature-library/overview.page and enter SAFETY-AT in the search field.

These publications provide guidance for a specific safety function based on the following:

- Functional requirements
- Equipment selection
- Performance level requirements
- Setup and wiring
- Configuration
- Verification and validation plans
- Calculation of performance level

<!-- image -->

## Wiring Examples for Safety Categories

Read this chapter for information about wiring and safety categories. See Table 21 for more information on input device connection methods and their safety categories.

Table 21 - Input Device Connection Methods and Safety Categories

<!-- image -->

Table 21 - Input Device Connection Methods and Safety Categories (Continued)

<!-- image -->

| Connected Device Test Pulse        | from Test Output   |                                                                                          | Connection Schematic Diagram Safety                                                                                                        | Category   | Maximum Performance Level   |
|------------------------------------|--------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------|-----------------------------|
| Emergency stop switch Door monitor |                    | Yes Connect the switches between I0 and T0, and I1 and T1                                | 1 4 5 2 3 I0  I1  T0  T1 1791ES Modules 1732ES Modules 1 - Test Output 1 2 - Input 1 3 - Input Common 4 - Input 0 5 - Test Output 0        | 4 E        |                             |
| Emergency stop switch Door monitor |                    | No Connect the switches between T0 and I0 and I1. T0 is configured for 24V power supply. | I0  I1  T0  T1 1791ES Modules                                                                                                              | 3 D        |                             |
|                                    |                    | Connect the switches between 24V DC and I0 and I1.                                       | I0  I1  T0  T1 24V DC 1 4 5 2 3 1791ES Modules 1732ES Modules 1 - Test Output 1 2 - Input 1 3 - Input Common 4 - Input 0 5 - Test Output 0 |            | D                           |

Table 21 - Input Device Connection Methods and Safety Categories (Continued)

<!-- image -->

## Wiring by Application

Read this section for examples of wiring by application. See catalog number details for appropriate module.

Figure 23 - Emergency Stop Switch Dual-channel Inputs with Manual Reset

<!-- image -->

| Controller Configuration Parameter Name Configuration Setting                 |
|-------------------------------------------------------------------------------|
| Safety Input 0 Safety Input 0 Channel Mode Test Pulse from Test Output        |
| Safety Input 0 Test Source Test Output 0                                      |
| Dual-channel Safety Input 0/1 Mode Dual-channel Equivalent                    |
| Dual-channel Safety Input 0/1 Discrepancy Time 100 ms (application dependent) |
| Safety Input 1 Safety Input 1 Channel Mode Test Pulse from Test Output        |
| Safety Input 1 Test Source Test Output 1                                      |
| Safety Input 2 Safety Input 2 Channel Mode Used as standard input             |
| Safety Input 2 Test Source Not Used                                           |
| Dual-channel Safety Input 2/3 Mode Single Channel                             |
| Test Output 0 Test Output 0 Mode Pulse Test Output                            |
| Test Output 1 Test Output 1 Mode Pulse Test Output                            |
| Test Output 2 Test Output 2 Mode Power Supply Output                          |

This example shows wiring and controller configuration when using the Guard I/O module. If used in combination with the programs in a safety controller, this wiring is Safety Category 4 in accordance with ISO 13849-1:2008 wiring requirements.

Figure 24 - Two-hand Monitor

<!-- image -->

| Controller Configuration Parameter Name Configuration Setting                 |
|-------------------------------------------------------------------------------|
| Safety Input 0 Safety Input 0 Channel Mode Test Pulse from Test Output        |
| Safety Input 0 Test Source Test Output 0                                      |
| Dual Channel Safety Input 0/1 Mode Dual Channel Complementary                 |
| Dual Channel Safety Input 0/1 Discrepancy Time 100 ms (application dependent) |
| Safety Input 1 Safety Input 1 Channel Mode Test Pulse from Test Output        |
| Safety Input 1 Test Source Test Output 1                                      |
| Safety Input 2 Safety Input 2 Channel Mode Test Pulse from Test Output        |
| Safety Input 2 Test Source Test Output 0                                      |
| Dual Channel Safety Input 2/3 Mode Dual Channel Complementary                 |
| Dual Channel Safety Input 2/3 Discrepancy Time 100 ms (application dependent) |
| Safety Input 3 Safety Input 3 Channel Mode Test Pulse from Test Output        |
| Safety Input 3 Test Source Test Output 1                                      |
| Test Output 0 Test Output 0 Mode Pulse Test Output                            |
| Test Output 1 Test Output 1 Mode Pulse Test Output                            |

This example shows wiring and controller configuration when using the Guard I/O™ module. If used in combination with the programs of a safety controller, the wiring is Category 4 in accordance with ISO 13849-1:2008 wiring requirements.

## Figure 25 - Mode Select Switch

1791ES Modules

PS1: User 24V DC Power Supply S1…S5: Switches

<!-- image -->

<!-- image -->

| Controller Configuration Parameter Name Configuration Setting   |
|-----------------------------------------------------------------|
| Safety Input 0 Safety Input 0 Channel Mode Safety Input         |
| Safety Input 0 Test Source None                                 |
| Dual Channel Safety Input 0/1 Mode Single Channel               |
| Safety Input 1 Safety Input 1 Channel Mode Safety Input         |
| Safety Input 1 Test Source None                                 |
| Safety Input 2 Safety Input 2 Channel Mode Safety Input         |
| Safety Input 2 Test Source None                                 |
| Dual Channel Safety Input 2/3 Mode Single Channel               |
| Safety Input 3 Safety Input 3 Channel Mode Safety Input         |
| Safety Input 3 Test Source None                                 |
| Safety Input 4 Safety Input 4 Channel Mode Safety Input         |
| Safety Input 4 Test Source None                                 |
| Dual Channel Safety Input 4/5 Mode Single Channel               |
| Test Output 0 Test Output 0 Mode Power Supply                   |

## Figure 26 - Muting Lamp Output

| Controller Configuration Parameter Name Configuration Setting   |                                                     |
|-----------------------------------------------------------------|-----------------------------------------------------|
|                                                                 | Test Output 3 Test Output 3 Mode Muting Lamp Output |

<!-- image -->

Figure 27 - Limit Switch Dual-channel Inputs and a Manual Reset

<!-- image -->

| Controller Configuration Parameter Name Configuration Setting                  |
|--------------------------------------------------------------------------------|
| Safety Input 0 Safety Input 0 Channel Mode Test Pulse from Test Output         |
| Safety Input 0 Test Source Test Output 0                                       |
| Dual-channel Safety Input 0/1 Mode Dual-channel Equivalent                     |
| Dual-channel Safety Input 0/1 Discrepancy Time 1000 ms (application dependent) |
| Safety Input 1 Safety Input 1 Channel Mode Test Pulse from Test Output         |
| Safety Input 1 Test Source Test Output 1                                       |
| Safety Input 2 Safety Input 2 Channel Mode Used as Standard Input              |
| Safety Input 2 Test Source Not Used                                            |
| Dual-channel Safety Input 2/3 Mode Single Channel                              |
| Test Output 0 Test Output 0 Mode Pulse Test Output                             |
| Test Output 1 Test Output 1 Mode Pulse Test Output                             |
| Test Output 2 Test Output 2 Mode Power Supply Output                           |

This example shows wiring and controller configuration when using the Guard I/O module with limit switch dual-channel inputs and a manual reset. If used in combination with the programs of a safety controller, the wiring is Category 4 in accordance with ISO 13849-1:2008 wiring requirements.

PS1: User 24V DC Power Supply

- L1: Lamp
- S1: Switch

## Figure 28 - Guard I/O Module with Limit Switch Dual-channel Inputs and a Manual Reset

<!-- image -->

| Controller Configuration Parameter Name Configuration Setting   |
|-----------------------------------------------------------------|
| Safety Input 1 Safety Input 1 Channel Mode Standard Input       |
| Safety Input 1 Test Source None                                 |
| Dual-channel Safety Input 0/1 Mode Single Channel               |
| Test Output 0 Test Output 0 Mode Standard Output                |
| Test Output 1 Test Output 1 Mode Power Supply                   |

## IMPORTANT

For the bipolar safety outputs to work as intended, you must connect the devices that are being controlled as shown in this figure. Connection of devices directly to 24V DC, 0V DC, or ground is strictly prohibited.

Figure 29 - Dual-load Bipolar Outputs (1732ES-IB12XOBV2 or 1732ES-IB8XOBV4)

<!-- image -->

| Controller Configuration Parameter Name Configuration Setting          |
|------------------------------------------------------------------------|
| Safety Input 0 Safety Input 0 Channel Mode Test Pulse from Test Output |
| Safety Input 0 Test Source Test Output 0                               |
| Dual-channel Safety Input 0/1 Mode Single Channel                      |
| Test Output 0 Test Output 0 Mode Pulse Test Output                     |
| Safety Output 0 Safety Output 0 Channel Mode Safety Pulse Test         |
| Safety Output 1 Safety Output 1 Channel Mode Safety Pulse Test         |

This example shows wiring and configuration when using the Guard I/O module with solid-state outputs in Dual-channel mode.

All safety outputs of this Guard I/O module are permanently configured for use as Dual-channel mode only. When used in combination with the programs of the safety controller, this circuit configuration is Safety Category 4 in accordance with ISO 13849-1:2008 wiring requirements and is rated up to Performance Level e.

Figure 30 - Dual-load Sourcing Outputs – 1732ES-IB12XOB4 and 1732ES-IB8XOB8 Modules

<!-- image -->

| Controller Configuration Parameter Name Configuration Setting          |
|------------------------------------------------------------------------|
| Safety Input 0 Safety Input 0 Channel Mode Test Pulse from Test Output |
| Safety Input 0 Test Source Test Output 0                               |
| Dual-channel Safety Input 0/1 Mode Single Channel                      |
| Test Output 0 Test Output 0 Mode Pulse Test Output                     |
| Safety Output 0/1 Safety Output 0/1 Operation Type Dual                |
| Safety Output 0 Safety Output 0 Channel Mode Safety Pulse Test         |
| Safety Output 1 Safety Output 1 Channel Mode Safety Pulse Test         |

The example shows wiring and configuration when using the 1732ES-IB12XOB4 Guard I/O module with solid-state outputs in Dualchannel mode.

When used in combination with the programs of the safety controller, this circuit configuration is Safety Category 4 in accordance with ISO 13849-1:2008 wiring requirements and is rated up to Performance Level e.

## Set the IP Address

## Configure the I/O Modules

| Topic Page                                    |
|-----------------------------------------------|
| Add Modules to the I/O Configuration Tree 77  |
| Configure the Module Properties 79            |
| Configure the Safety Connections 86           |
| Configure the Module Inputs 88                |
| Configure the Test Outputs 90                 |
| Configure the Module Outputs 91               |
| Save and Download the Module Configuration 92 |

Use the Studio 5000 Logix Designer® application to configure the modules.

At the bottom of a dialog box, choose Help for information about how to complete entries in the dialog box. At the bottom of a warning dialog box, choose Help to get information about that specific error.

If the network uses 192.168.1.x, use the rotary switches on the module to set the last octet of network IP address. Valid numbers range from 001…254.

Figure 31 - Example Network Address

<!-- image -->

<!-- image -->

WARNING: When you change switch settings while power is on, an electrical arc can occur. This could cause an explosion in hazardous location installations. Be sure that power is removed or the area is nonhazardous before proceeding.

<!-- image -->

<!-- image -->

ATTENTION: Set a suitable network IP addresses before connecting the module to a network.

## IMPORTANT

1732ES modules have plastic dust caps that cover the network IP switches. Remove the dust caps to adjust the IP address switches.

The dust caps must be installed to maintain the ingress protection (IPxx) rating marked on the 1732ES modules.

Torque the dust caps to 0.3 ± 0.03 N·m (2.5 ± 0.3 lb·in).

If DHCP is not enabled, the module uses the IP address (along with other TCP configurable parameters) stored in nonvolatile memory.

## IMPORTANT Your module comes preconfigured with a gateway address of 192.168.1.1.

At power-up, the module reads the rotary switches to determine if they are set to a valid number for the last octet of the IP address. If the settings are a valid number, these conditions result:

- IP address = 192.168.1.xxx (where xxx represents the switch settings)
- Subnet mask = 255.255.255.0
- Gateway address = 192.168.1.1
- The module does not have an assigned host name, nor does it use any Domain Name System.

## IMPORTANT

The gateway address automatically changes to 0.0.0.0 if the address switches are set to match the gateway address.

If the network does not use 192.168.1.x, after you install and power up the module, you can use the following tools to set the network IP address:

- Bootstrap Protocol/Dynamic Host Configuration Protocol (BOOTP/DHCP) server
- RSLinx® Classic software
- Studio 5000 Logix Designer application

Apply two labels to the module to identify the IP address of the module.

For more information on how to configure the module with these tools, see the EtherNet/IP Communication Modules in 5000 Series Systems User Manual, publication ENET-UM004 .

## Add Modules to the I/O Configuration Tree

To add a module to the I/O configuration tree in your programming software project, follow these guidelines.

1. From the I/O Configuration tree, right-click the Ethernet bridge, as shown in the figure, and choose New Module.
2. Uncheck the Module Type Category Filters box.
3. Scroll down through the list and check Safety.

<!-- image -->

The Select Module dialog box displays a list of safety modules and controllers.

<!-- image -->

4. Select the required safety module from the list.

This example uses the 1732ESIB12XOB4 module.

<!-- image -->

5. To add the module to your configuration, click Create.

## Configure the Module Properties

Follow these steps to configure the general properties of the module.

1. From the I/O configuration tree, double-click the module, such as the 1791ES-IB8XOBV4 module, to see the Module Properties dialog box.
2. Type a unique name for the module.
3. If desired, type a description.

<!-- image -->

Note the safety network number (SNN). In most cases, you can use the default that is provided by the programming software. For a detailed explanation of the safety network number (SNN), see the GuardLogix® Controller Systems Safety Reference Manual that is listed in the Additional Resources on page 10 .

## Set the IP Address in the Programming Software

If you are not using network address translation (NAT), type the IP address of the module in the IP Address field. See the Allen-Bradley® Stratix® 5700 Network Address Translation (NAT) White Paper, publication ENET-WP032, for more information on NAT.

If you are using NAT, follow these steps:

1. In the IP Address field, type the IP address of the controller.
2. To open the Advanced Ethernet Settings dialog box, click Advanced.
3. Check the checkbox to indicate that this module and the controller communicate through NAT devices.
4. Type the actual module address.

<!-- image -->

If you configured the IP address with the rotary switches, this address is the address that you set on the module.

5. Click OK.

## IMPORTANT

When NAT is used in a safety application with a GuardLogix controller, the module does not accept a safety connection unless the actual module address is provided.

## Change the Module Definition

Click Change to open the Module Definition dialog box, where you can select values to configure what data and status tags to generate implicitly for the safety module.

See these sections for settings explanations:

- Input Data Options on page 81
- Input Status Options on page 82
- Output Data Options on page 84

- Values and States of Tags on page 85

<!-- image -->

## Input Data Options

Choose from these options:

- Safety - Creates these tags for the target module:
- – RunMode: Module mode
- – ConnectionFaulted: Communication status
- – Safety Data: Safety inputs from module
- Safety-Readback - This selection is not available for input-only safety modules. Safety-Readback creates both safety and readback tags. Readback indicates the presence of 24V on the output terminal.

<!-- image -->

<!-- image -->

## Input Status Options

Choose from these options.

## IMPORTANT

Status data is not SIL 3 data. Do not use status data to control a SIL 3 safety output.

- None - No status tags, only data for the inputs
- Point Status-Muting - A muting status tag for test output with muting output capability with point status for each input and output point

| IB&xOBV4_ES:1                   | AB:1791ES_IB8X...   | Safety   |
|---------------------------------|---------------------|----------|
| HB8xOBV4_ES:1.RunMode           | BOOL                | Safety   |
| IB&xOBV4_ES:1.ConnectionFaulted | BOOL                | Safety   |
| IB&xOBV4_ES:1.Pt00Data          | BOOL                | Safety   |
| HB8xOBV4_ES:1.Pt01Data          | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt02Data          | BOOL                | Safety   |
| HB8xOBV4_ES:1.Pt03Data          | BOOL                | Safety   |
| HB8xOBV4_ES:1.Pt04Data          | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt05Data          | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt06Data          | BOOL                | Safety   |
| HB8xOBV4_ES:1.Pt07Data          | BOOL                | Safety   |
| HB&xOBV4_ES:1.Pt00lnputStatus   | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt01lnputStatus   | BOOL                | Safety   |
| IB&xOBV4_ES:1.Pt02lnputStatus   | BOOL                | Safety   |
| HB8xOBV4_ES:1.Pt03lnputStatus   | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt04lnputStatus   | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt05lnputStatus   | BOOL                | Safety   |
| HB8xOBV4_ES:1.Pt06lnputStatus   | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt07lnputStatus   | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt000utputStatus  | BOOL                | Safety   |
| HB8xOBV4_ES:1.Pt010utputStatus  | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt020utput Status | BOOL                | Safety   |
| IB&xOBV4_ES:1.Pt030utputStatus  | BOOL                | Safety   |
| IB&xOBV4_ES:1.Pt040utputStatus  | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt050utputStatus  | BOOL                | Safety   |
| IB8xOBV4_ES:1.Pt060utput Status | BOOL                | Safety   |
| IB&xOBV4_ES:1.Pt070utputStatus  | BOOL                | Safety   |
| IB8xOBV4_ES:1.Muting03Status    | BOOL                | Safety   |
| IB8xOBV4_ES:1.Muting07Status    | BOOL                | Safety   |
| HB8xOBV4_ES:1.OutputPowerStatus | BOOL                | Safety   |
| IB8xOBV4_ES:1.lnputPowerStatus  | BOOL                | Safety   |

- Combined Status-Muting
- – One BOOL tag represents an AND of the status bits for all input points. For example, if any input channel has a fault, this bit goes LO.(1)
- – One BOOL tag represents an AND of the status bits for all output points. (1)
- – A muting status tag for test output T3/T7 (for 1791ES-IB8XOBV4, 1732ES-IB8XOB8 and 1732ES-IB8XOBV4 modules) T3/T7/T11/T15 (for 1791ES-IB16 and 1732ES-IB16 modules), and T3/T7/T11 (for 1732ES-IB12XOB4 and 1732ES-IB12XOBV2 modules).

<!-- image -->

## Output Data Options

Choose from these options.

## IMPORTANT The standard outputs on the module must not be used for safety purposes.

- None - Results in an input only connection to the module. Inputs and status are read, but no outputs are written.
- Safety - Creates the safety tags shown here and enables the safety outputs for use in the safety task.
- Test - Creates these tags and enables the test outputs on the module. These outputs are standard outputs and must not be used for safety purposes.
- Combined - Creates these tags and enables all module outputs - safety and test.

<!-- image -->

| IB8xOBV4_ES:0          | AB:1791ES_IB8X..   | Safety   |
|------------------------|--------------------|----------|
| HB8xOBV4_ES:O.Pt00Data | BOOL               | Safety   |
| IB8xOBV4_ES:O.Pt01Data | BOOL               | Safety   |
| IB8xOBV4_ES:O.Pt02Data | BOOL               | Safety   |
| IB8x0BV4_ES:O.Pt03Data | BOOL               | Safety   |
| IB8xOBV4_ES:O.Pt04Data | BOOL               | Safety   |
| IB8x0BV4ES:O.Pt05Data  | BOOL               | Safety   |
| 1B8x0BV4_ES:O.Pt06Data | BOOL               | Safety   |
| B8xOBV4_ES:0.Pt07Data  | BOOL               | Safety   |

<!-- image -->

| IB8xOBV4_ES:O            | AB:1791ES_IB8X.. Safety   |        |
|--------------------------|---------------------------|--------|
| IB8xOBV4_ES:O.Test00Data | BOOL                      | Safety |
| IB8xOBV4ES:O.Test01Data  | BOOL                      | Safety |
| IB8xOBV4_ES:O.Test02Data | BOOL                      | Safety |
| IB8xOBV4_ES:O.Test03Data | BOOL                      | Safety |
| IB8xOBV4ES:O.Test04Data  | BOOL                      | Safety |
| IB8xOBV4_ES:O.Test05Data | BOOL                      | Safety |
| IB8xOBV4_ES:O.Test06Data | BOOL                      | Safety |
| IB8xOBV4_ES:O.Test07Data | BOOL                      | Safety |

<!-- image -->

| -IB8xOBV4_ES:0           | AB:1791ES_IB8X...   | Safety   |
|--------------------------|---------------------|----------|
| HB8xOBV4_ES:O.Pt00Data   | BOOL                | Safety   |
| HB8xOBV4_ES:O.Pt01Data   | BOOL                | Safety   |
| HB8xOBV4_ES:O.Pt02Data   | BOOL                | Safety   |
| IB8xOBV4_ES:O.Pt03Data   | BOOL                | Safety   |
| 1B8x0BV4_ES:0.Pt04Data   | BOOL                | Safety   |
| IB&xOBV4_ES:O.Pt05Data   | BOOL                | Safety   |
| IB&xOBV4_ES:O.Pt06Data   | BOOL                | Safety   |
| 1B8x0BV4_ES:0.Pt07Data   | BOOL                | Safety   |
| 1B&xOBV4_ES:O.Test00Data | BOOL                | Safety   |
| HB&xOBV4_ES:O.Test01Data | BOOL                | Safety   |
| 1B8x0BV4_ES:O.Test02Data | BOOL                | Safety   |
| 1B8xOBV4_ES:O.Test03Data | BOOL                | Safety   |
| IB&xOBV4_ES:O.Test04Data | BOOL                | Safety   |
| HB&xOBV4_ES:O.Test05Data | BOOL                | Safety   |
| 1B8xOBV4_ES:O.Test06Data | BOOL                | Safety   |
| IB8xOBV4_ES:O.Test07Data | BOOL                | Safety   |

Table 22 - Values and States of Tags

| Data Description                       |                                                                                                                                                 |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Input data Run Mode STANDARD           | Indicates whether a device actively updates consumed data that is in one of these states. • Run mode: 1 • Idle State: 0                         |
| Connection Faulted STANDARD            | Indicates the validity of the safety connection between the safety producer and the safety consumer. • Valid: 0 • Faulted: 1                    |
| Safety Input Data SAFETY               | Indicates the ON/OFF status of each input circuit. • ON: 1 • OFF: 0                                                                             |
| Combined Safety Input Status SAFETY    | An AND of the status of all input circuits. • All circuits are normal: 1 • An error was detected in one or more input circuits: 0               |
| Individual Safety Input Status SAFETY  | Indicates the status of each input circuit. • Normal: 1 • Fault (Alarm): 0                                                                      |
| Combined Safety Output Status SAFETY   | An AND of the status of all safety output circuits. • All circuits are normal: 1 • An error has been detected in one or more output circuits: 0 |
| Individual Safety Output Status SAFETY | Indicates the status of each safety output circuit. • Normal: 1 • Fault (Alarm): 0                                                              |
| Muting Lamp Status SAFETY              | Indicates the status when a test output is configured as a muting lamp output. • Normal: 1 • Fault (Alarm): 0                                   |
| Safety Output Monitor STANDARD         | Monitors the outputs of the safety output circuits. • ON: 1 • OFF: 0                                                                            |
| Individual Test Output Status STANDARD | Indicates the status of each of the test output circuits. • Normal: 1 • Fault (Alarm): 0                                                        |
| Input Power Error Bit STANDARD         | Indicates if the field power supplied is within specification. • Power error: 1 • Power OK: 0                                                   |
| Output Power Error Bit STANDARD        | Indicates if the field power supplied is within specification. • Power error: 1 • Power OK: 0                                                   |
| Output data Safety Output Data SAFETY  | Controls the safety output. • ON: 1 • OFF: 0                                                                                                    |
| Standard Output Data STANDARD          | Controls the test output when test output mode is set to a standard output. • ON: 1 • OFF: 0                                                    |

## IMPORTANT

Safety denotes information the controller can use in safety-related functions. Standard denotes additional information that must not be relied on for safety functions.

## Values and States of Tags

This table shows the values and states of the tags.

## Configure the Safety Connections

Follow these steps to complete entries when you choose the Safety tab.

1. From the Module Properties dialog box, choose the Safety tab to see the Safety dialog box.
2. Click Advanced to configure Requested Packet Interval (RPI) and Configure Connection Reaction Time Limit (CRTL).

<!-- image -->

<!-- image -->

We suggest that you keep the Timeout Multiplier and Network Delay Multiplier at their default values of 2 and 200.

See the GuardLogix Controllers User Manual, which is listed in the Additional Resources on page 10, for more information about the CRTL.

Make sure that input RPI is set to match the need. The smallest input RPI allowed is 6 ms. Small RPIs consume network bandwidth and can cause nuisance trips because other devices cannot get access to the network.

As an example, a safety input module with only E-stop switches connected to it generally can work well with settings of 50…100 ms. An input module with a light curtain guarding a hazard can need the fastest response that is possible.

Appropriate RPI selection results in a system with maximum (best) performance.

## IMPORTANT

Analyze each safety channel to determine what is appropriate. The default timeout multiplier of 2 and network delay multiplier of 200 creates the following:

- An input connection reaction time limit of four times the RPI.
- An output connection reaction limit of three times the RPI.

A safety administrator must approve changes to these parameters.

Every connection has a connection status tag.

<!-- image -->

If the RPI and CRTL for the network are set appropriately, then this status tag must always remain LO. Monitor all connection status bits to verify that they are not going HI intermittently due to timeouts.

## Configuration Ownership – Reset Ownership

The connection between the owner and the Guard I/O™ module is based on the following items:

- Guard I/O EtherNet/IP address
- Guard I/O safety network number
- GuardLogix slot number
- GuardLogix safety network number
- Path from GuardLogix controller to Guard I/O module
- Configuration signature

If any of these items change, the connection between the GuardLogix controller and the Guard I/O module is lost, and the yellow yield in the project tree appears. Reset ownership to re-establish the connection by using this procedure.

1. Open the safety I/O module properties.

## Configure the Module Inputs

Table 23 - Typical Safety Input Parameters

| Parameter Name Value Description   |                                  |                                                                                                                                                                                                                                                                                                          |
|------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                    |                                  | Input Point Operation Type Single Channel Inputs are treated as single channel.                                                                                                                                                                                                                          |
|                                    |                                  | Dual-channel Equivalent Inputs are treated as a dual-channel pair. The channels must match (be equal) within the discrepancy time or a fault is generated.                                                                                                                                               |
|                                    |                                  | Dual-channel Complementary Inputs are treated as a dual-channel pair. The channels must disagree (be opposite) within the discrepancy time or a fault is generated.                                                                                                                                      |
|                                    |                                  | Input Point Mode Not Used The input is disabled. It remains logic 0 if 24V is applied to the input terminal.                                                                                                                                                                                             |
|                                    |                                  | Safety Test Pulse Pulse testing is performed on this input circuit. A test source on the module must be used as the 24V source for  this circuit. The test source is configured by using the test source pull-down. The pulse test detects shorts to 24V, and channel-to-channel shorts to other inputs. |
|                                    |                                  | Safety A safety input is connected but there is no requirement for the 1791ES module to perform a pulse test on this circuit. An example is a safety device that performs its own pulse tests on the input wires, such as a light curtain.                                                               |
|                                    |                                  | Standard A standard device, such as a reset switch, is connected. This point cannot be used in dual channel operation.                                                                                                                                                                                   |
|                                    |                                  | Safety Input Test Source None If pulse testing is being performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit.                             |
|                                    | Test Output 0                    | Safety Input Test Source None If pulse testing is being performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit.                             |
|                                    | Test Output 1                    | Safety Input Test Source None If pulse testing is being performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit.                             |
|                                    | Test Output 2                    | Safety Input Test Source None If pulse testing is being performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit.                             |
|                                    | Test Output 3                    | Safety Input Test Source None If pulse testing is being performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit.                             |
|                                    | Test Output 4…15 (1)             | Safety Input Test Source None If pulse testing is being performed on an input point, then the test source that is sourcing the 24V for the input circuit must be selected. If the incorrect test source is entered, the result is pulse test failures on that input circuit.                             |
| Input Delay Time Off -> On         | 0…126 ms (in increments of 6 ms) | Filter time is for OFF to ON transition. Input must be high after input delay has elapsed before it is set logic 1.                                                                                                                                                                                      |
| Input Delay Time On -> Off         | 0…126 ms (in increments of 6 ms) | Filter time is ON to OFF transition. Input must be low after input delay has elapsed before it is set logic 0.                                                                                                                                                                                           |

2. Choose the Safety tab.
3. From the dialog box, choose Reset ownership.

## Configuration Signature

The programming software creates the configuration signature and the safety module verifies it. The configuration signature provides SIL 3 integrity of the configuration of a Guard I/O module.

- When a GuardLogix controller first connects to an unconfigured Guard I/O module, the complete configuration is downloaded to the I/O module.
- Any time the GuardLogix controller attempts to connect to a Guard I/O module, if the configuration signatures are the same, then the configuration does not need to be downloaded, because they already match.
- Any time the GuardLogix controller attempts to connect to a Guard I/O module and the signatures do not match, the module checks the IP address and safety network number. If these values are all correct, the controller attempts to configure the module.

Table 23 shows the typical safety input parameters available on the Input Configuration tab. See Chapter 1 for related information.

Table 23 - Typical Safety Input Parameters (Continued)

|                                                                    | Parameter Name Value Description                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Safety Input Error Latch Time 0…65,530 ms (in increments of 10 ms) | Default is 1000 ms. The purpose for latching input errors is to make sure that intermittent faults that can only exist for a few milliseconds are latched long enough for the controller to read. The amount of time to latch the error must be based on the RPI, the safety task watchdog, and other application-specific variables. |

Follow these steps to configure the module inputs.

1. Click the Input Configuration tab.
2. For Point Operation Type, choose one of these values and a value for Discrepancy Time if set to Equivalent or Complementary:
- Single
4. Inputs are treated as single channels. In many cases, dual-channel safety inputs are configured as two individual single channels. This configuration does not affect pulse testing because it is handled on an individual channel basis.
- Equivalent
6. (1)
7. Inputs are treated as a dual-channel pair. The channels must match within the discrepancy time or an error is generated.
8. (1)
- Complementary Inputs are treated as a dual-channel pair. They must be in opposite states within the discrepancy time or an error is generated.
3. For Point Mode, choose one of these values for each point and refer to the Safety Input Parameters table for additional information:
- Not Used - Safety input channel is disabled
- Safety Pulse Test - Safety input is configured for pulse test operation
- Safety - The safety input is used with a safety field device
- (1) If you configure discrepancy time on safety I/O modules, it masks input inconsistent faults from the GuardLogix safety instructions. GuardLogix can read status to obtain this fault information.

<!-- image -->

## Configure the Test Outputs

## Table 24 - Configuring Test Outputs

| Parameter Name Value Description Default                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Test Output Mode Not Used The test output is disabled. Not Used                                                                                                                                                                                                      |
| Standard The output point is enabled for use by the GuardLogix controller.                                                                                                                                                                                           |
| Pulse Test The test output is being used as a pulse test source.                                                                                                                                                                                                     |
| Power Supply A constant 24V is placed on the output terminal. It can be used to provide power to a field device.                                                                                                                                                     |
| Muting Lamp Output  (1)  An indicator lamp is connected to the output. When this lamp is energized, a burned-out bulb, broken wire, or short to GND error condition can be detected. Typically, the lamp is an indicator that is used in light curtain applications. |

Follow these steps to configure the test outputs.

1. Click the Test Outputs tab.
- Standard - Safety input has a standard field device that is wired to it
4. Complete entries, and note the following:
- For each safety input on the module, you can define if the input is pulse tested. If the inputs are pulse tested, select which test source to use.
- Off -&gt; On and On -&gt; Off delay times can be configured per channel with each channel tuned to match the characteristics of the field device for maximum performance.
- Input Error Latch Time is the time that the module holds an error to make sure that the controller can detect it. This setting provides you more reliable diagnostics and enhances the chances that a nuisance error is detected.
5. Click OK at the bottom of the dialog box or a tab at the top of the dialog box.

<!-- image -->

## Table 24 provides information for configuring the test outputs.

.

2. From the Port Mode pull-down menus, select the desired configuration option for each point.

## Configure the Module Outputs

Table 25 provides information for configuring the safety outputs.

Table 25 - Guidelines for Configuring Safety Outputs

| Parameter Name Value Description Default                                                                                                                                                                                                                                                                                                                                    |              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Point Operation Type Dual The 1791ES modules, the 1732ES-IB12XOBV2 module, and the 1732ES-IB8XOBV4 module treat the outputs as a pair. It always sets them HI to LO as a matched pair. Safety logic must set both of these outputs ON or OFF simultaneously or the module declares a channel fault.                                                                         | Dual-channel |
| Single The 1732ES-IB12XOB4 module can be configured with the outputs treated as single channels. Both channels of an output pair are set to either Single or Dual.                                                                                                                                                                                                          | Dual-channel |
| Point Mode Not Used The output is disabled. Not Used                                                                                                                                                                                                                                                                                                                        |              |
| Safety The output point is enabled, and it does not perform a pulse test on the output.                                                                                                                                                                                                                                                                                     |              |
| Safety Pulse Test The output point is enabled and performs a pulse test on the output. When the output is energized, the output pulses LO briefly. The pulse test detects if 24V remains on the output terminal during this LO pulse due to a short to 24V. The pulse test also detects if the output is shorted to another output terminal.                                |              |
| Output Error Latch Time 0…65,530 ms (in increments of 10 ms) The purpose for latching output errors is to make sure that intermittent faults that can only exist for a few milliseconds are latched long enough for the controller to read. The amount of time to latch the errors is based on the RPI, the safety task watchdog, and other application-specific variables. | 1000 ms      |

Follow these steps to configure the module outputs.

1. For Point Operation, select single or dual.
2. For Point Mode, select Not Used, Safety, or Safety Pulse Test. See the Safety Output Parameters table for additional information.
3. Select a value for Output Error Latch Time. Output Error Latch Time is the time that the module holds an error to make sure that the controller can detect it. This setting provides you more reliable diagnostics and enhances the changes that a nuisance error is detected.
4. Click Apply from the bottom of the dialog box.

<!-- image -->

## Save and Download the Module Configuration

We recommend that after a module is configured you save your work.

If after downloading the program the MS and NS indicators on the Guard I/O module are not both solid green, this state can be due to loss of ownership. The ownership is based on the following items:

- Guard I/O EtherNet/IP address
- Guard I/O safety network number
- GuardLogix slot number
- GuardLogix safety network number
- Path from GuardLogix controller to Guard I/O module
- Configuration signature

If any of these items change, the connection between the GuardLogix controller and the Guard I/O module is lost, and the yellow yield in the project tree appears. Reset ownership to re-establish the connection by using this procedure.

1. Open the safety I/O module properties.
2. Choose the Safety tab.
3. From the dialog box, choose Reset ownership.

## Manually Set the Safety Network Number

## Replace Guard I/O Modules

| Topic Page                                      |
|-------------------------------------------------|
| Manually Set the Safety Network Number 93       |
| Reset the Module to Out-of-box Configuration 94 |
| Replace a Module in a GuardLogix System 94      |

GuardLogix® controllers retain I/O module configuration onboard and are able to download the configuration to the replacement module. Replacing a safety I/O module that sits on a CIP Safety network is more complicated than replacing standard devices because of the safety network number (SNN). The module number and SNN constitute the DeviceID of the safety module. Safety devices require this more complex identifier to make sure that duplicate module numbers do not compromise communication between the correct safety devices.

The following statement applies if a safety signature exists. The POINT Guard I/O™ module must have a proper SNN/node number identification that matches the module within the safety controller project before it can receive its configuration. To keep integrity, the SNN setting of the module is required to be a manual action. This manual action is to use the 'set' function on an out-of-box POINT Guard I/O module.

<!-- image -->

Figure 32 - Setting the SNN with a GuardLogix Controller

<!-- image -->

## Reset the Module to Out-ofbox Configuration

## Replace a Module in a GuardLogix System

If a Guard I/O module was used previously, clear the existing configuration before installing it on a safety network.

When the programming software is online, the Safety tab of the Module Properties dialog box displays the current configuration ownership. When the opened project owns the configuration, Local is displayed. When a second device owns the configuration, Remote is displayed, along with the safety network number (SNN), and node address or slot number of the configuration owner. Communication error is displayed if the module read fails.

If the connection is Local, you must inhibit the module connection before you reset ownership. To inhibit the module:

1. Right-click the module and choose Properties.
2. Click the Connection tab.
3. Check the inhibit module checkbox.
4. Click Apply and then OK.

Follow these steps to reset the module to its out-of-box configuration when online.

1. Right-click the module and choose Properties.
2. Click the Safety tab.
3. Click Reset Ownership.

<!-- image -->

The replacement of safety devices requires that the replacement device is configured properly and that the operation of the replacement device is userverified.

<!-- image -->

ATTENTION: During replacement or functional testing of a device, the safety of the system must not rely on any portion of the affected device.

Two options for I/O device replacement are available on the Safety tab of the Controller Properties dialog box in the programming software:

- Configure Only When No Safety Signature Exists
- Configure Always

Figure 33 - Safety I/O Replacement Options

<!-- image -->

## Configure Only When No Safety Signature Exists

This setting instructs the GuardLogix controller to configure a safety device only when the safety task does not have a safety task signature. The replacement device must also be in an out-of-box condition, meaning that a safety network number does not exist in the safety device.

If the safety task has a safety task signature, the GuardLogix controller only automatically configures the replacement CIP Safety I/O device if the following is true:

- The device already has the correct safety network number.
- The device electronic keying is correct.
- The node or IP address is correct.

For detailed information, see the appropriate GuardLogix Safety Reference Manual, which is listed in the Additional Resources on page 10 .

## Configure Always

The GuardLogix controller always attempts to configure a replacement CIP Safety I/O device if the device is in an out-of-box condition. This occurrence means that a safety network number does not exist in the replacement safety device and the node number and I/O device keying matches the configuration of the controller.

<!-- image -->

<!-- image -->

ATTENTION: Enable the Configure Always feature only if the entire routable CIP Safety control system is not being relied on to maintain SIL 3 behavior during the replacement and functional testing of a device.

If other parts of the CIP Safety control system are being relied upon to maintain SIL 3, make sure that the controller's Configure Always feature is disabled.

It is your responsibility to implement a process to make sure proper safety functionality is maintained during device replacement.

ATTENTION: Do not place any devices in the out-of-box condition on any CIP Safety network when the Configure Always feature is enabled, except while following the device replacement procedure in the appropriate GuardLogix Safety Reference Manual, which is listed in the Additional Resources on page 10 .

## Module Status Indicator Depictions

<!-- image -->

## Interpret the Module Status Indicators

See Figure 23 and Table 26 … Table 33 for information on the 1791ES module indicators.

Figure 23 - 1791ES Module Status Indicators

<!-- image -->

See Figure 34 and Table 26 … Table 33 for information on the 1732ES module status indicators.

Figure 34 - 1732ES Module Status Indicators

<!-- image -->

## Module Status Indicator Descriptions

## Table 26 - 24V DC Input Power Indicator

|                                                                                         | State Status Description Recommended Action                                                                                         |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Off No power No power is applied. No input power or severe input power overvoltage. (1) | Apply power to this section. Apply power that is within specifications to this section. (2)                                         |
| Solid green Normal operation The applied voltage is within specifications. None.        |                                                                                                                                     |
|                                                                                         | Solid yellow Input power out of specification The input power is out of specification. Check your connectors, wiring, and voltages. |

Table 27 - 24V DC Output Power Indicator

|                                                                                           | State Status Description Recommended Action                                                                                           |
|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Off No power No power is applied. No output power or severe output power overvoltage. (1) | Apply power to this section. Apply power that is within specifications to this section. (2)                                           |
| Solid green Normal operation The applied voltage is within specifications. None.          |                                                                                                                                       |
|                                                                                           | Solid yellow Output power out of specification The output power is out of specification. Check your connectors, wiring, and voltages. |

## Table 28 - Module Status Indicator

|                                                                                                                                  | State Status Description Recommended Action                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Off No power No power is applied to the power connector. No power is applied to the input power connector or severe (1) input power overvoltage. (1)                                                                                                                                  | Apply power to this connector. Apply input power that is within specification to the (2) ppy p module.(2)                                                                                                                                               |
| Solid green Normal operation The module is operating normally. None.                                                             |                                                                                                                                               |
|                                                                                                                                  | Solid red Unrecoverable fault The module detected an unrecoverable fault. Cycle power to the module. If problem persists, replace the module. |
| Flashing red and green Module is unconfigured Module needs commissioning due to missing, incomplete, or incorrect configuration. | Reconfigure the module. For additional information, inspect Network Status indicator.                                                         |
|                                                                                                                                  | Device in self-test The module is performing its power-cycle diagnostic tests. Wait for the module to complete its power-cycle diagnostics.   |
| Flashing green Idle Idle, waiting for connection from scanner. Establish connection.                                             |                                                                                                                                               |
|                                                                                                                                  | Flashing red Recoverable fault The module has detected a recoverable fault. Cycle power to the module or reset the module.                    |
| User-initiated firmware update in User-initiated firmware update is in progress. Wait for firmware update to complete.           |                                                                                                                                               |

## Table 29 - Network Status Indicator

|                                                                       |                                                                                                                                                                  | State Status Description Recommended Action                                                                                      |
|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
|                                                                       |                                                                                                                                                                  | Off Module not online The module does not have an IP address. Verify that your network is working properly.                      |
| Flashing green Module online with no connections in established state | The module has acquired an IP address, but no connections are established.                                                                                       | Verify your network and module configuration.                                                                                    |
| Solid green Module online with connections in established state       | The module is operating normally. None.                                                                                                                          |                                                                                                                                  |
| Flashing red One or more I/O connections in timed out state                                                                       | The module detected a recoverable network fault.                                                                                                                 | Verify your network and module configuration.                                                                                    |
|                                                                       | User-initiated firmware update User-initiated firmware update is in progress. Wait for firmware update to complete.                                              |                                                                                                                                  |
|                                                                       | Solid red Critical link failure The module detected an error that prevents it from communicating on the network, such as duplicate IP address has been detected. | Cycle power to the module. Check network IP addressing.                                                                          |
| Flashing red                                                          |                                                                                                                                                                  | Self-test The module is performing its power-cycle diagnostic test. Wait for the module to complete its power-cycle diagnostics. |
| and green Waiting for TUNID (1)                                       | The module has received the proposed UNID and is waiting (2) for the TUNID.(2)                                                                                                                                                                  | None.(3)                                                                                                                         |

## Table 30 - Network Activity Indicators (link 1 and link2)

| State Status Recommended Action                    |
|----------------------------------------------------|
| Off No link is established. Establish link.        |
| Flashing Green Transmit or receive activity. None. |
| Steady Green Link is established None.             |

## Table 31 - Test Output Status Indicator (only 1791ES Modules)

|                                                                                       | State Status Description Recommended Action                                                                                                                                                                                                  |
|---------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off Test output off The test output is off or the channel is configured for not used. | Turn on the test output or reconfigure the channel, if desired.                                                                                                                                                                              |
| Solid yellow Output on Output is on. None.                                            |                                                                                                                                                                                                                                              |
|                                                                                       | Solid red Fault detected A fault in the external wiring or input circuit detected. Check field wiring. If no problem found, replace module. For outputs that are configured for muting, this could indicate undercurrent or burned-out lamp. |

Table 32 - Safety Input Status Indicator

| State Status Description Recommended Action                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off Safety input off The safety input is off or the channel is configured for not used. Turn on the safety input or reconfigure the channel, if desired.                                                                             |
| Solid yellow Safety input on The safety input is on. None.                                                                                                                                                                           |
| Solid red Fault detected A fault in the external wiring or input circuit detected. Check configuration, field wiring, and devices. If no problem found, replace module.                                                              |
| Flashing red Partner fault detected  A fault in the partner input circuit of a dual-input configuration detected. Check the field wiring and verify your configuration for the partner circuit. If no problem found, replace module. |

\

Table 33 - Safety Output Status Indicator (only 1732ES and 1791ES-IB8XOBV4 Modules)

| State Status Description Recommended Action                                                                                                                                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Off Safety output off The safety output is off or the channel is configured for not used. Turn on the safety output or reconfigure the channel, if desired.                                                         |
| Solid yellow Safety output on The safety output is on. None.                                                                                                                                                        |
| Solid red Fault detected A fault in the output circuit was detected. Check the circuit wiring and end device. If no problem found, replace module.                                                                  |
| Both tags in a dual channel circuit do not have the same value. Make sure that logic is driving tag values to the same state (off or on).                                                                           |
| Flashing red Partner fault detected A fault in the partner output circuit of a dual output configuration was detected. Check the circuit wiring and end device of the partner. If no problem found, replace module. |

<!-- image -->

## Get Diagnostic Status from Modules by Using Explicit Messaging

| Topic Page                                           |
|------------------------------------------------------|
| Get Status Messages from 1791ES-IB8XOBV4 Modules 102 |
| Get Status Messages from 1791ES-IB16 Modules 107     |
| Get Status Messages from 1732ES Modules 112          |
| I/O Data Supported by Each Module 136                |
| I/O Assembly and Reference Data 140                  |
| Explicit Messages 149                                |

This appendix provides information about how to use CIP Generic Message instructions (sometimes called Explicit Messaging) to get diagnostic status information from the modules.

You can implicitly obtain individual point status of the Guard I/O™ module from the Module Definition dialog box by choosing Pt. Status from the Input Status pull-down menu.

<!-- image -->

## Get Status Messages from 1791ES-IB8XOBV4 Modules

Another choice is to obtain overall status implicitly from the Module Definition dialog box by choosing Combined Status from the Input Status pull-down menu.

<!-- image -->

If the Combined Status changes, use Explicit Messaging to obtain the point level status.

Follow these steps to get status messages from 1791ES-IB8XOBV4 modules.

1. In the Module Definition dialog box, from the Input Status pull-down menu, choose Combined Status.

<!-- image -->

This selection creates a two-byte input assembly, as shown for the 1791ES-IB8XOBV4 module.

<!-- image -->

2. Use the CombinedInputStatus and CombinedOutputStatus bits to detect if one or more of the I/O points on the module have a fault.
- If any input or output status bit goes to a value of 0 (0=error, 1=no error), use the CombinedInputStatus and CombinedOutputStatus bits to condition your MSG rungs as follows.
- The second rung can be used to read the status on mode transition and once a fault is detected, continue reading until the fault is corrected.
- Place these rungs in the standard task.

<!-- image -->

Figure 35 … Figure 39 show the MSG instruction parameters to read Instance 852 from the 1791ES-IB8XOBV4 module.

Figure 35 - Instance 852 Configuration Tab

<!-- image -->

Instance 852 (354 hex) is 5 bytes in length, so the destination tag MSGdata must be at least 5 bytes in length to hold this data. The size is DINT[2] or 8 bytes (see Table 34).

Table 34 - Layout of Instance 852 (354 hex) – 1791ES-IB8XOBV4 Module

| Instance Hex (decimal)   | Connection Type               | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                                                                      |                         |                         |                         |                         |                         |                                        |                         |
|--------------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|----------------------------------------|-------------------------|
|                          | 354 (852) Safety and standard | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                         |                         |                         |                         |                         |                                        |                         |
|                          | 354 (852) Safety and standard | 1 Safety Input 7 Status                                                                                                   | Safety Input 6 Status   | Safety Input 5 Status   | Safety Input 4 Status   | Safety Input 3 Status   | Safety Input 2 Status   | Safety Input 1 Status                  | Safety Input 0 Status   |
|                          | 354 (852) Safety and standard | 2 Safety Output 7 Status                                                                                                  | Safety Output 6 Status  | Safety Output 5 Status  | Safety Output 4 Status  | Safety Output 3 Status  | Safety Output 2 Status  | Safety Output 1 Status                 | Safety Output 0 Status  |
|                          | 354 (852) Safety and standard | 3 Safety Output 7 Monitor                                                                                                 | Safety Output 6 Monitor | Safety Output 5 Monitor | Safety Output 4 Monitor | Safety Output 3 Monitor | Safety Output 2 Monitor | Safety Output 1 Monitor                | Safety Output 0 Monitor |
|                          | 354 (852) Safety and standard |                                                                                                                           |                         | 4 Reserved Reserved Input Power (1)  p Error (1)                         | Output Power (1)  p Error (1)                         |                         |                         | Reserved Reserved Muting Lamp 7 Status | Muting Lamp 3 Status    |

- (1) This data is only diagnostic data. This data does not have safety integrity.
3. Click the Communication tab.

This dialog box requires the path to the module.

4. Click Browse to select the module that the MSG reads.

Figure 36 - Instance 852 Communication Tab

<!-- image -->

5. From the top of the Message Configuration dialog box, choose Tag.

Figure 37 - Instance 852 Tag Tab

<!-- image -->

When the explicit message reads the data from the 1791ES-IB8XOBV4 module, the data appears in the MSGdata tags as shown in Figure 38 .

Figure 38 - Instance 852 MSGdata Tags

<!-- image -->

The first 32 bits of the instance are in MSGdata[0].0…31, and the final 8 bits are in MSGdata[1].0…7. These 40 bits must be mapped according to Instance 852. An easy method to do this mapping is to create a user-defined tag (UDT) for Instance 852. Once complete, it appears as shown in Figure 39 .

Figure 39 - Instance 852 UDT

<!-- image -->

## Get Status Messages from 1791ES-IB16 Modules

Follow these steps to get status messages from 1791ES-IB16 modules.

1. In the Module Definition dialog box, from the Input Status pull-down menu, choose Combined Status.

<!-- image -->

This selection creates a three-byte input assembly, as shown, for the 1791ES-IB16 module.

<!-- image -->

2. Use the CombinedInputStatus bit to detect if one or more of the I/O points on the module have a fault.
- If any input status bits go to a value of 0 (0 = bad; 1 = good), use an explicit message to determine which individual data points have faulted.

- You can use the second rung to read the status on mode transition and once a fault is detected, continue reading until the fault is corrected.
- Place these rungs in the standard task.

<!-- image -->

Figure 40 … Figure 44 show the MSG instruction parameters for to read Instance 869 from the 1791ES-IB16 module. See Appendix C of this manual for a layout of possible instances.

Figure 40 - Instance 869 Configuration Tab Configuration

<!-- image -->

Instance 869 (365 hex) is 7 bytes in length, so the destination tag IB16MSGdata must be at least 7 bytes in length to hold this data. The size is DINT[2] or 8 bytes (see Table 35).

Table 35 - Layout of Instance 869 (365 hex) – 1791ES-IB16 Module

| Instance Hex (decimal)   | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                        |                                                                   |                                                                                                                                          |                        |                                                               |                       |                       |
|--------------------------|------------------------------------------------------------------------|------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------|---------------------------------------------------------------|-----------------------|-----------------------|
|                          |                                                                        |                        |                                                                   | 365 (869) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                        |                                                               |                       | Safety Input 0        |
|                          |                                                                        |                        | 1 Safety Input 15 Safety Input 14 Safety Input 13 Safety Input 12 |                                                                                                                                          |                        | Safety Input 11 Safety Input 10 Safety Input 9 Safety Input 8 |                       |                       |
|                          | 2 Safety Input 7 Status                                                | Safety Input 6 Status  | Safety Input 5 Status                                             | Safety Input 4 Status                                                                                                                    | Safety Input 3 Status  | Safety Input 2 Status                                         | Safety Input 1 Status | Safety Input 0 Status |
|                          | 3 Safety Input 15 Status                                               | Safety Input 14 Status | Safety Input 13 Status                                            | Safety Input 12 Status                                                                                                                   | Safety Input 11 Status | Safety Input 10 Status                                        | Safety Input 9 Status | Safety Input 8 Status |
|                          | 4 Test Output 7 Status                                                 | Test Output 6 Status   | Test Output 5 Status                                              | Test Output 4 Status                                                                                                                     | Test Output 3 Status   | Test Output 2 Status                                          | Test Output 1 Status  | Test Output 0 Status  |
|                          | 5 Test Output 15 Status                                                | Test Output 14 Status  | Test Output 13 Status                                             | Test Output 12 Status                                                                                                                    | Test Output 11 Status  | Test Output 10 Status                                         | Test Output 9 Status  | Test Output 8 Status  |
|                          |                                                                        |                        | 6 Reserved Reserved Input Power (1)  p Error (1)                                                                   | Output Power (1)  p Error (1)                                                                                                                                          | Muting Lamp 15 Status  | Muting Lamp 11 Status                                         | Muting Lamp 7 Status  | Muting Lamp 3 Status  |

3. From the top of the Message Configuration dialog box, choose the Communication tab.

This dialog box requires the path to the module.

4. Click Browse to go to the module that the MSG reads.

Figure 41 - Instance 869 Communication Tab

<!-- image -->

<!-- image -->

5. From the top of the Message Configuration dialog box, click Tag.

Figure 42 - Instance 869 Tag Tab

<!-- image -->

When the explicit message reads the data from the 1791ES-IB16 module, the data appears in the MSGdata tags as shown in Figure 43 .

Figure 43 - Instance 869 MSGdata Tags

<!-- image -->

The first 32 bits of the instance are in IB16MSGdata[0].0…31, and the final 24 bits are in IB16MSGdata[1].0…23. Map these 56 bits according to Instance 869. An easy method to do this mapping is to create a userdefined tag (UDT) for Instance 869. Once complete, it appears as shown in Figure 44 .

Figure 44 - Instance 869 UDT

<!-- image -->

## Get Status Messages from 1732ES Modules

Follow these steps to get status messages from 1732ES modules.

TIP The process is identical for all 1732ES modules.

## 1732ES-IB12XOB4 Modules

1. In the Module Definition dialog box, from the Input Status pull-down menu, choose Combined Status.

<!-- image -->

This selection creates a three-byte input assembly, as shown, for the 1732ES-IB12XOB4 modules.

<!-- image -->

2. Use the CombinedInputStatus and CombinedOutputStatus bits to detect if one or more of the I/O points on the module have a fault.

- If any input or output status bits go to a value of 0 (0 = bad; 1 = good), use the CombinedInputStatus and CombinedOutputStatus bits to condition your MSG rungs as follows.

Only use of the CombinedInputStatus bit is shown. Create similar rungs by using the CombinedOutputStatus bit instead of the CombinedInputStatus bit.

- The second rung can be used to read the status on mode transition and once a fault is detected, continue reading until the fault is corrected.
- Place these rungs in the standard task.

<!-- image -->

Figure 45 … Figure 49 show the MSG instruction parameters to read Instance 860 from the 1732ES-IB12XOB4 module. See Appendix C of this manual for a layout of possible instances.

Figure 45 - Instance 860 Configuration Tab

<!-- image -->

Instance 860 (35C hex) is 5 bytes in length, so the destination tag IB12XOB4MSGdata must be at least 5 bytes in length to hold this data. The size is DINT[2] or 8 bytes (see Table 36).

Table 36 - Layout of Instance 860 (35C hex) – 1732ES-IB12XOB4 Modules

| Instance Hex (decimal)   |                           |                                                                                                                                          |                         |                         |                        |                                | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                               |
|--------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------------------|------------------------|--------------------------------|------------------------------------------------------------------------|-------------------------------|
|                          |                           | 35C (860) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                         |                         |                        |                                |                                                                        | Safety Input 0                |
|                          | 1 Safety Input 3 Status   | Safety Input 2 Status                                                                                                                    | Safety Input 1 Status   | Safety Input 0 Status   | Safety Input 11        | Safety Input 10                |                                                                        | Safety Input 9 Safety Input 8 |
|                          | 2 Safety Input 11 Status  | Safety Input 10 Status                                                                                                                   | Safety Input 9 Status   | Safety Input 8 Status   | Safety Input 7 Status  | Safety Input 6 Status          | Safety Input 5 Status                                                  | Safety Input 4 Status         |
|                          | 3 Safety Output 3 Monitor | Safety Output 2 Monitor                                                                                                                  | Safety Output 1 Monitor | Safety Output 0 Monitor | Safety Output 3 Status | Safety Output 2 Status         | Safety Output 1 Status                                                 | Safety Output 0 Status        |
|                          |                           |                                                                                                                                          | 4 Reserved Reserved Input Power (1)  p Error (1)                         | Output Power (1)  p Error (1)                         |                        | Reserved Muting Lamp 11 Status | Muting Lamp 7 Status                                                   | Muting Lamp 3 Status          |

- (1) This data is only diagnostic data. This data does not have safety integrity.
3. From the top of the Message Configuration dialog box, choose the Communication tab.

This dialog box requires the path to the module.

4. Click Browse to go to the module that the MSG reads.

Figure 46 - Instance 860 Communication Tab

<!-- image -->

<!-- image -->

5. From the top of the Message Configuration dialog box, click Tag.

Figure 47 - Instance 860 Tag Tab

<!-- image -->

When the explicit message reads the data from the 1732ES-IB12XOB4 modules, the data appears in the MSGdata tags as shown in Figure 48 .

Figure 48 - Instance 860 MSGdata Tags

<!-- image -->

The first 32 bits of the instance are in IB12XOB4MSGdata[0].0…31, and the final 8 bits are in IB12XOB4MSGdata[1].0…7. Map these 40 bits according to Instance 860. An easy method to do this mapping is to create a user-defined tag (UDT) for Instance 860. Once complete, it appears as shown in Figure 49 .

Figure 49 - Instance 860 UDT

<!-- image -->

## 1732ES-IB12XOBV2 Modules

1. In the Module Definition dialog box, from the Input Status pull-down menu, choose Combined Status.

<!-- image -->

This selection creates a three-byte input assembly, as shown, for the 1732ES-IB12XOBV2 modules.

<!-- image -->

2. Use the CombinedInputStatus and CombinedOutputStatus bits to detect if one or more of the I/O points on the module have a fault.
- If any input or output status bits go to a value of 0 (0 = bad; 1 = good), use the CombinedInputStatus and CombinedOutputStatus bits to condition your MSG rungs as follows.

Only use of the CombinedInputStatus bit is shown. Create similar rungs by using the CombinedOutputStatus bit instead of the CombinedInputStatus bit.

- The second rung can be used to read the status on mode transition and once a fault is detected, continue reading until the fault is corrected.
- Place these rungs in the standard task.

<!-- image -->

Figure 50 … Figure 54 show the MSG instruction parameters to read Instance 860 from the 1732ES-IB12XOBV2 module. See Appendix C of this manual for a layout of possible instances.

Figure 50 - Instance 860 Configuration Tab

<!-- image -->

Instance 860 (35C hex) is 5 bytes in length, so the destination tag IB12XOBV2MSGdata must be at least 5 bytes in length to hold this data. The size is DINT[2] or 8 bytes (see Table 37).

Table 37 - Layout of Instance 860 (35C hex) – 1732ES-IB12XOBV2 Modules

| Instance Hex   | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                                                                     |                           |                         |                         |                         |                        |                                                               |                        |                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-------------------------|-------------------------|-------------------------|------------------------|---------------------------------------------------------------|------------------------|------------------------|
| (decimal)      |                                                                                                                                          |                           |                         |                         |                         |                        |                                                               |                        |                        |
|                | 35C (860) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                           |                         |                         |                         |                        |                                                               |                        | Safety Input 0         |
|                | 35C (860) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 | 1 Safety Input 3 Status   | Safety Input 2 Status   | Safety Input 1 Status   | Safety Input 0 Status   |                        | Safety Input 11 Safety Input 10 Safety Input 9 Safety Input 8 |                        |                        |
|                | 35C (860) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 | 2 Safety Input 11 Status  | Safety Input 10 Status  | Safety Input 9 Status   | Safety Input 8 Status   | Safety Input 7 Status  | Safety Input 6 Status                                         | Safety Input 5 Status  | Safety Input 4 Status  |
|                | 35C (860) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 | 3 Safety Output 3 Monitor | Safety Output 2 Monitor | Safety Output 1 Monitor | Safety Output 0 Monitor | Safety Output 3 Status | Safety Output 2 Status                                        | Safety Output 1 Status | Safety Output 0 Status |
|                | 35C (860) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                           |                         | 4 Reserved Reserved Input Power (1)  p Error(1)                         | Output Power (1)  p Error(1)                         |                        | Reserved Muting Lamp 11 Muting Lamp 7 Muting Lamp 3           |                        |                        |

3. From the top of the Message Configuration dialog box, choose the Communication tab.

This dialog box requires the path to the module.

4. Click Browse to go to the module that the MSG reads.

Figure 51 - Instance 860 Communication Tab

<!-- image -->

<!-- image -->

5. From the top of the Message Configuration dialog box, click Tag.

Figure 52 - Instance 860 Tag Tab

<!-- image -->

When the explicit message reads the data from the 1732ESIB12XOBV2 modules, the data appears in the MSGdata tags as shown in Figure 53 .

Figure 53 - Instance 860 MSGdata Tags

<!-- image -->

The first 32 bits of the instance are in IB12XOBV2MSGdata[0].0…31, and the final 8 bits are in IB12XOBV2MSGdata[1].0…7. Map these 40 bits according to Instance 860. An easy method to do this mapping is to create a user-defined tag (UDT) for Instance 860. Once complete, it appears as shown in Figure 54 .

Figure 54 - Instance 860 UDT

<!-- image -->

## 1732ES-IB16 Modules

1. In the Module Definition dialog box, from the Input Status pull-down menu, choose Combined Status.

<!-- image -->

This selection creates a three-byte input assembly, as shown here.

<!-- image -->

2. Use the CombinedInputStatus and CombinedOutputStatus bits to detect if one or more of the I/O points on the module have a fault.
- If any input or output status bits go to a value of 0 (0 = bad; 1 = good), use the CombinedInputStatus and CombinedOutputStatus bits to condition your MSG rungs as follows.
3. Only use of the CombinedInputStatus bit is shown. Create similar rungs by using the CombinedOutputStatus bit instead of the CombinedInputStatus bit.

- The second rung can be used to read the status on mode transition and once a fault is detected, continue reading until the fault is corrected.
- Place these rungs in the standard task.

<!-- image -->

Figure 55 … Figure 60 show the MSG instruction parameters to read Instance 821 from the 1732ES-IB16 module. See Appendix C of this manual for a layout of possible instances.

Figure 55 - Instance 821 Configuration Tab

<!-- image -->

Instance 821 (335 hex) is 5 bytes in length, so the destination tag IB16MSGdata must be at least 5 bytes in length to hold this data. The size is DINT[2] or 8 bytes (see Table 38).

Table 38 - Layout of Instance 821 (335 hex) – 1732ES-IB16 Modules

| Instance Hex (decimal)   | Connection Type Byte Bit 7                                                                                                               |                          | Figure 56 - Bit 6      |                        |                        |                                |                        | Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                               |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------------------|------------------------|------------------------|--------------------------------|------------------------|---------------------------------------|-------------------------------|
|                          | 335 (821) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                          |                        |                        |                        |                                |                        |                                       | Safety Input 0                |
|                          |                                                                                                                                          | 1 Safety Input 15        | Safety Input 14        | Safety Input 13        | Safety Input 12        | Safety Input 11                | Safety Input 10        |                                       | Safety Input 9 Safety Input 8 |
|                          |                                                                                                                                          | 2 Safety Input 7 Status  | Safety Input 6 Status  | Safety Input 5 Status  | Safety Input 4 Status  | Safety Input 3 Status          | Safety Input 2 Status  | Safety Input 1 Status                 | Safety Input 0 Status         |
|                          |                                                                                                                                          | 3 Safety Input 15 Status | Safety Input 14 Status | Safety Input 13 Status | Safety Input 12 Status | Safety Input 11 Status         | Safety Input 10 Status | Safety Input 9 Status                 | Safety Input 8 Status         |
|                          |                                                                                                                                          |                          |                        | 4 Reserved Reserved Input Power (1)  p Error (1)                        |                        | Reserved Muting Lamp 15 Status | Muting Lamp 11 Status  | Muting Lamp 7 Status                  | Muting Lamp 3 Status          |

- (1) This data is only diagnostic data. This data does not have safety integrity.
3. From the top of the Message Configuration dialog box, choose the Communication tab.

This dialog box requires the path to the module.

4. Click Browse to go to the module that the MSG reads.

Figure 57 - Instance 821 Communication Tab

<!-- image -->

<!-- image -->

5. From the top of the Message Configuration dialog box, click Tag.

Figure 58 - Instance 821 Tag Tab

<!-- image -->

When the explicit message reads the data from the 1732ES-IB16 module, the data appears in the MSGdata tags as shown in Figure 59 .

Figure 59 - Instance 821 MSGdata Tags

<!-- image -->

The first 32 bits of the instance are in IB16MSGdata[0].0…31, and the final 8 bits are in IB16MSGdata[1].0…7. Map these 40 bits according to Instance 821. An easy method to do this mapping is to create a userdefined tag (UDT) for Instance 821. Once complete, it appears as shown in Figure 60 .

Figure 60 - Instance 821 UDT

<!-- image -->

## 1732ES-IBXOB8 Modules

1. In the Module Definition dialog box, from the Input Status pull-down menu, choose Combined Status.

<!-- image -->

This selection creates a three-byte input assembly, as shown here.

<!-- image -->

2. Use the CombinedInputStatus and CombinedOutputStatus bits to detect if one or more of the I/O points on the module have a fault.
- If any input or output status bits go to a value of 0 (0 = bad; 1 = good), use the CombinedInputStatus and CombinedOutputStatus bits to condition your MSG rungs as follows.
3. Only use of the CombinedInputStatus bit is shown. Create similar rungs by using the CombinedOutputStatus bit instead of the CombinedInputStatus bit.
- The second rung can be used to read the status on mode transition and once a fault is detected, continue reading until the fault is corrected.

- Place these rungs in the standard task.

<!-- image -->

Figure 61 … Figure 65 show the MSG instruction parameters to read Instance 852 from the 1732ES-IB8XOB8 module. See Appendix C of this manual for a layout of possible instances.

Figure 61 - Instance 852 Configuration Tab

<!-- image -->

Instance 852 (354 hex) is 5 bytes in length, so the destination tag IB8XOB8MSGdata must be at least 5 bytes in length to hold this data. The size is DINT[2] or 8 bytes (see Table 39).

Table 39 - Layout of Instance 852 (354 hex) – 1732ES-IB8XOB8 Modules

| Instance Hex (decimal)   |                           |                                                                                                                                          |                         |                         |                         | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                                        |                         |
|--------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------------------|-------------------------|------------------------------------------------------------------------|----------------------------------------|-------------------------|
|                          |                           | 354 (852) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                         |                         |                         |                                                                        |                                        | Safety Input 0          |
|                          | 1 Safety Input 7 Status   | Safety Input 6 Status                                                                                                                    | Safety Input 5 Status   | Safety Input 4 Status   | Safety Input 3 Status   | Safety Input 2 Status                                                  | Safety Input 1 Status                  | Safety Input 0 Status   |
|                          | 2 Safety Output 7 Status  | Safety Output 6 Status                                                                                                                   | Safety Output 5 Status  | Safety Output 4 Status  | Safety Output 3 Status  | Safety Output 2 Status                                                 | Safety Output 1 Status                 | Safety Output 0 Status  |
|                          | 3 Safety Output 7 Monitor | Safety Output 6 Monitor                                                                                                                  | Safety Output 5 Monitor | Safety Output 4 Monitor | Safety Output 3 Monitor | Safety Output 2 Monitor                                                | Safety Output 1 Monitor                | Safety Output 0 Monitor |
|                          |                           |                                                                                                                                          | 4 Reserved Reserved Input Power (1)  p Error (1)                         | Output Power (1)  p Error (1)                         |                         |                                                                        | Reserved Reserved Muting Lamp 7 Status | Muting Lamp 3 Status    |

3. From the top of the Message Configuration dialog box, choose the Communication tab.

This dialog box requires the path to the module.

4. Click Browse to go to the module that the MSG reads.

Figure 62 - Instance 852 Communication Tab

<!-- image -->

<!-- image -->

5. From the top of the Message Configuration dialog box, click Tag to see this dialog box.

Figure 63 - Instance 852 Tag Tab

<!-- image -->

When the explicit message reads the data from the 1732ES-IB8XOB8 module, the data appears in the MSGdata tags as shown in Figure 64 .

Figure 64 - Instance 852 MSGdata Tags

<!-- image -->

The first 32 bits of the instance are in IB8XOB8MSGdata[0].0…31, and the final 8 bits are in IB8XOB8MSGdata[1].0…7. Map these 40 bits according to Instance 852. An easy method to do this mapping is to create a user-defined tag (UDT) for Instance 852. Once complete, it appears as shown in Figure 65 .

Figure 65 - Instance 852 UDT

<!-- image -->

## 1732ES-IB8XOBV4 Modules

1. In the Module Definition dialog box, from the Input Status pull-down menu, choose Combined Status.

<!-- image -->

This selection creates a three-byte input assembly, as shown here.

<!-- image -->

2. Use the CombinedInputStatus and CombinedOutputStatus bits to detect if one or more of the I/O points on the module have a fault.
- If any input or output status bits go to a value of 0 (0 = bad; 1 = good), use the CombinedInputStatus and CombinedOutputStatus bits to condition your MSG rungs as follows.
3. Only use of the CombinedInputStatus bit is shown. Create similar rungs by using the CombinedOutputStatus bit instead of the CombinedInputStatus bit.
- The second rung can be used to read the status on mode transition and once a fault is detected, continue reading until the fault is corrected.

- Place these rungs in the standard task.

<!-- image -->

Figure 66 … Figure 70 show the MSG instruction parameters to read Instance 852 from the 1732ES-IB8XOBV4 module. See Appendix C of this manual for a layout of possible instances.

Figure 66 - Instance 852 Configuration Tab

<!-- image -->

From the top of the Message Configuration dialog box, choose the Communication tab. This dialog box requires the path to the module. Click Browse to go to the module that the MSG reads.

Figure 67 - Instance 852 Communication Tab

<!-- image -->

<!-- image -->

Instance 852 (354 hex) is 5 bytes in length, so the destination tag IB8XOBV4MSGdata must be at least 5 bytes in length to hold this data. The size is DINT[2] or 8 bytes (see Table 40).

Table 40 - Layout of Instance 852 (354 hex) – 1732ES-IB8XOBV4 Modules

| Instance Hex (decimal)   |                           |                                                                                                                                          |                         |                         |                         |                         | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                         |
|--------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------------------|-------------------------|-------------------------|------------------------------------------------------------------------|-------------------------|
|                          |                           | 354 (852) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                         |                         |                         |                         |                                                                        | Safety Input 0          |
|                          | 1 Safety Input 7 Status   | Safety Input 6 Status                                                                                                                    | Safety Input 5 Status   | Safety Input 4 Status   | Safety Input 3 Status   | Safety Input 2 Status   | Safety Input 1 Status                                                  | Safety Input 0 Status   |
|                          | 2 Safety Output 7 Status  | Safety Output 6 Status                                                                                                                   | Safety Output 5 Status  | Safety Output 4 Status  | Safety Output 3 Status  | Safety Output 2 Status  | Safety Output 1 Status                                                 | Safety Output 0 Status  |
|                          | 3 Safety Output 7 Monitor | Safety Output 6 Monitor                                                                                                                  | Safety Output 5 Monitor | Safety Output 4 Monitor | Safety Output 3 Monitor | Safety Output 2 Monitor | Safety Output 1 Monitor                                                | Safety Output 0 Monitor |
|                          |                           |                                                                                                                                          | 4 Reserved Reserved Input Power (1)  p Error (1)                         | Output Power (1)  p Error (1)                         |                         |                         | Reserved Reserved Muting Lamp 7 Status                                 | Muting Lamp 3 Status    |

From the top of the Message Configuration dialog box, click Tag to see this dialog box.

Figure 68 - Instance 852 Tag Tab

<!-- image -->

When the explicit message reads the data from the 1732ES-IB8XOBV4 module, the data appears in the MSGdata tags as shown in Figure 69 .

Figure 69 - Instance 852 MSGdata Tags

<!-- image -->

The first 32 bits of the instance are in IB8XOBV4MSGdata[0].0…31, and the final 8 bits are in IB8XOBV4MSGdata[1].0…7. Map these 40 bits according to Instance 852. An easy method to do this mapping is to create a user-defined tag (UDT) for Instance 852. Once complete, it appears as shown in Figure 70 .

Figure 70 - Instance 852 UDT

<!-- image -->

## I/O Data Supported by Each Module

Table 41 shows a summary of default I/O data by module.

Table 41 - Default I/O Data

|                                     | Module Cat. No. Safety Connection Assembly Instance (hex)   |
|-------------------------------------|-------------------------------------------------------------|
| 1791ES-IB16 Safety 225 and 23       |                                                             |
| 1791ES-IB8XOBV4 Safety 204 and 234  |                                                             |
| 1732ES-IB12XOBV2 Safety 20C and 233 |                                                             |
| 1732ES-IB12XOB4 Safety 20C and 233  |                                                             |

Table 41 - Default I/O Data

|                                   | Module Cat. No. Safety Connection Assembly Instance (hex)   |
|-----------------------------------|-------------------------------------------------------------|
| 1732ES-IB16 Safety 205 and 23     |                                                             |
| 1732ES-IB8XOB8 Safety 204 and 22  |                                                             |
| 1732ES-IB8XOBV4 Safety 204 and 22 |                                                             |

The tables show the I/O data supported by each module. See I/O Assembly and Reference Data on page 140 for data arrangements.

For I/O data, safety connections for up to four items, including one output, can be allocated for the master unit. Also, standard connections for up to two items can be allocated for the master unit.

Table 42 - 1791ES-IB8XOBV4 Modules

|                                             | Input Data Input Status Assembly Instance   |
|---------------------------------------------|---------------------------------------------|
| Safety None 204                             | (1)                                         |
| Safety None 204                             | Point Status - Muting 334                   |
| Safety None 204                             | Combined Status - Muting 324                |
| Safety - Readback Point Status - Muting 354 |                                             |
| Safety - Readback Point Status - Muting 354 | Point Status - Muting - Test Output 374     |
| Output Data Assembly Instance               | Output Data Assembly Instance               |
| Safety – 234                                | (1)                                         |
| Test 22                                     |                                             |
| Combined 2C4                                |                                             |
| None C7                                     |                                             |

(1) The default Assembly Instance.

Table 43 - 1791ES-IB16 Modules

|                               | Input Data Input Status Assembly Instance   |
|-------------------------------|---------------------------------------------|
| Safety None 205               |                                             |
|                               | Point Status - Muting 335                   |
|                               | Point Status - Muting - Test Output 365     |
|                               | Combined Status - Muting 315                |
|                               | Point Status 225(1)                         |
| Output Data Assembly Instance | Output Data Assembly Instance               |
| Test – 23(1)                  |                                             |
| None C7                       |                                             |

(1) The default Assembly Instance.

Table 44 - 1732ES-IB12XOBV2

|                                             | Input Data Input Status Assembly Instance   |
|---------------------------------------------|---------------------------------------------|
| Safety None 20C                             | (1)                                         |
| Safety None 20C                             | Point Status - Muting 34C                   |
| Safety None 20C                             | Combined Status - Muting 32C                |
| Safety - Readback Point Status - Muting 35C |                                             |
| Safety - Readback Point Status - Muting 35C | Point Status - Muting - Test Output 37C     |
| Output Data Assembly Instance               | Output Data Assembly Instance               |
| Safety – 233                                | (1)                                         |
| Test 25                                     |                                             |
| Combined 3C4                                |                                             |
| None C7                                     |                                             |

(1) The default Assembly Instance.

Table 45 - 1732ES-IB12XOBV4

|                                             | Input Data Input Status Assembly Instance   |
|---------------------------------------------|---------------------------------------------|
| Safety None 20C                             | (1)                                         |
| Safety None 20C                             | Point Status - Muting 34C                   |
| Safety None 20C                             | Combined Status - Muting 32C                |
| Safety - Readback Point Status - Muting 35C |                                             |
| Safety - Readback Point Status - Muting 35C | Point Status - Muting - Test Output 37C     |
| Output Data Assembly Instance               | Output Data Assembly Instance               |
| Safety – 233                                | (1)                                         |
| Test 25                                     |                                             |
| Combined 3C4                                |                                             |
| None C7                                     |                                             |

(1) The default Assembly Instance.

Table 46 - 1732ES-IB16 Modules

|                               | Input Data Input Status Assembly Instance   |
|-------------------------------|---------------------------------------------|
| Safety None 205               |                                             |
|                               | Point Status - Muting 335                   |
|                               | Point Status - Muting - Test Output 365     |
|                               | Combined Status - Muting 315                |
|                               | Point Status 225(1)                         |
| Output Data Assembly Instance | Output Data Assembly Instance               |
| Test – 23(1)                  |                                             |
| None C7                       |                                             |

(1) The default Assembly Instance.

Table 47 - 1732ES-IB8XOBV4 Modules

|                                             | Input Data Input Status Assembly Instance   |
|---------------------------------------------|---------------------------------------------|
| Safety None 204                             | (1)                                         |
| Safety None 204                             | Point Status - Muting 344                   |
| Safety None 204                             | Combined Status - Muting 324                |
| Safety - Readback Point Status - Muting 354 |                                             |
| Safety - Readback Point Status - Muting 354 | Point Status - Muting - Test Output 374     |
| Output Data Assembly Instance               | Output Data Assembly Instance               |
| Safety – 234                                | (1)                                         |
| Test 22                                     |                                             |
| Combined 2C4                                |                                             |
| None C7                                     |                                             |

Table 48 - 1732ES-IB8XOB8 Modules

|                                             | Input Data Input Status Assembly Instance   |
|---------------------------------------------|---------------------------------------------|
| Safety None 204                             | (1)                                         |
| Safety None 204                             | Point Status - Muting 344                   |
| Safety None 204                             | Combined Status - Muting 324                |
| Safety - Readback Point Status - Muting 354 |                                             |
| Safety - Readback Point Status - Muting 354 | Point Status - Muting - Test Output 374     |
| Output Data Assembly Instance               | Output Data Assembly Instance               |
| Safety – 234                                | (1)                                         |
| Test 22                                     |                                             |
| Combined 2C4                                |                                             |
| None C7                                     |                                             |

(1) The default Assembly Instance.

## I/O Assembly and Reference Data

This section provides information for I/O assembly and reference data.

## 1791ES Modules

The bits in the tag definitions of the programming software are different than the bits shown in the following section. Table 49 defines the name associations for clarification with the programming software.

Table 49 - Bit Definitions and Programming Software Tag Names

| Bit Definitions Programming Software Tag Name   |
|-------------------------------------------------|
| Safety Input 0 Pt00Data                         |
| Safety Input 15 Pt15Data                        |
| Safety Input 0 Status Pt00InputStatus           |
| Safety Input 15 Status Pt15InputStatus          |
| Safety In Status InputStatus                    |
| Muting Lamp Status MutingStatus                 |
| Safety Output 0 Pt00Data                        |
| Safety Output 7 Pt07Data                        |
| Standard Output 0 Test00Data                    |
| Standard Output 15 Test15Data                   |
| Safety Output 0 Status Pt00OutputStatus         |
| Safety Output 7 Status Pt07OutputStatus         |
| Safety Out Status OutputStatus                  |
| Safety Output 0 Monitor Pt00Readback            |
| Safety Output 7 Monitor Pt07Readback            |
| Test Output 0 Status Pt00TestOutputStatus       |
| Test Output 15 Status Pt15TestOutputStatus      |

See Table 50 … Table 53 for reference data concerning input and output data.

Table 50 - Input Data – 1791ES-IB8XOBV4 Modules

| Instance Hex Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                                                                                                                           |                            |                       |                       |                                             |                       |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------|-----------------------|-----------------------|---------------------------------------------|-----------------------|
| 204 (516) Safety and standard                                                       | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                            |                       |                       |                                             |                       |
| 224 (548) Safety and standard                                                       | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                            |                       |                       |                                             |                       |
| 224 (548) Safety and standard                                                       | 1 Safety Input 7 Status Safety Input 3 Status                                                                             | Safety Input 6 Status      | Safety Input 5 Status | Safety Input 4 Status | Safety Input 2 Status Safety Input 1 Status | Safety Input 0 Status |
| 301 (769) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power (1)                                                                                     |                                                                                                                           |                            |                       |                       | p Error (1)                                             | Input Power Error     |
| 324 (804) Safety and standard                                                       | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                            |                       |                       |                                             |                       |
| 324 (804) Safety and standard                                                       | 1 Combined Safety In Status                                                                                               | Combined Safety Out Status | Input Power (1)  p Error (1)                       | Output Power (1)  p Error (1)                       | Reserved Reserved Muting Lamp 7 Status      | Muting Lamp 3 Status  |

Table 50 - Input Data – 1791ES-IB8XOBV4 Modules (Continued)

| Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                         |                           |                         |                                                                                                                           |                         |                                                                                                                           |                         |                                                                                                                           |                         |
|----------------------------------------------------------------------------------------------|---------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------|---------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 334 (820) Safety and standard                                                                |                           |                         | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                         |                                                                                                                           |                         |                                                                                                                           |                         |
| 334 (820) Safety and standard                                                                | 1 Safety Input 7 Status   | Safety Input 6 Status   | Safety Input 5 Status                                                                                                     | Safety Input 4 Status   | Safety Input 3 Status                                                                                                     | Safety Input 2 Status   | Safety Input 1 Status                                                                                                     | Safety Input 0 Status   |
| 334 (820) Safety and standard                                                                |                           |                         | 2 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                           | Output Power (1)  p Error (1)                         |                                                                                                                           |                         | Reserved Reserved Muting Lamp 7 Status                                                                                    | Muting Lamp 3 Status    |
| 344 (836) Safety and standard                                                                |                           |                         |                                                                                                                           |                         |                                                                                                                           |                         | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                         |
| 344 (836) Safety and standard                                                                | 1 Safety Input 7 Status   | Safety Input 6 Status   | Safety Input 5 Status                                                                                                     | Safety Input 4 Status   | Safety Input 3 Status                                                                                                     | Safety Input 2 Status   | Safety Input 1 Status                                                                                                     | Safety Input 0 Status   |
| 344 (836) Safety and standard                                                                | 2 Safety Output 7 Status  | Safety Output 6 Status  | Safety Output 5 Status                                                                                                    | Safety Output 4 Status  | Safety Output 3 Status                                                                                                    | Safety Output 2 Status  | Safety Output 1 Status                                                                                                    | Safety Output 0 Status  |
| 344 (836) Safety and standard                                                                |                           |                         | 3 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                           | Output Power (1)  p Error (1)                         |                                                                                                                           |                         | Reserved Reserved Muting Lamp 7 Status                                                                                    | Muting Lamp 3 Status    |
| 354 (852) Safety and standard                                                                |                           |                         |                                                                                                                           |                         | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                         |                                                                                                                           |                         |
| 354 (852) Safety and standard                                                                | 1 Safety Input 7 Status   | Safety Input 6 Status   | Safety Input 5 Status                                                                                                     | Safety Input 4 Status   | Safety Input 3 Status                                                                                                     | Safety Input 2 Status   | Safety Input 1 Status                                                                                                     | Safety Input 0 Status   |
| 354 (852) Safety and standard                                                                | 2 Safety Output 7 Status  | Safety Output 6 Status  | Safety Output 5 Status                                                                                                    | Safety Output 4 Status  | Safety Output 3 Status                                                                                                    | Safety Output 2 Status  | Safety Output 1 Status                                                                                                    | Safety Output 0 Status  |
| 354 (852) Safety and standard                                                                | 3 Safety Output 7 Monitor | Safety Output 6 Monitor | Safety Output 5 Monitor                                                                                                   | Safety Output 4 Monitor | Safety Output 3 Monitor                                                                                                   | Safety Output 2 Monitor | Safety Output 1 Monitor                                                                                                   | Safety Output 0 Monitor |
| 354 (852) Safety and standard                                                                |                           |                         | 4 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                           | Output Power (1)  p Error (1)                         |                                                                                                                           |                         | Reserved Reserved Muting Lamp 7 Status                                                                                    | Muting Lamp 3 Status    |
| 364 (868) Safety and standard                                                                | 0 Safety Input 7 Status   | Safety Input 6 Status   | Safety Input 5 Status                                                                                                     | Safety Input 4 Status   | Safety Input 3 Status                                                                                                     | Safety Input 2 Status   | Safety Input 1 Status                                                                                                     | Safety Input 0 Status   |
| 364 (868) Safety and standard                                                                | 1 Safety Output 7 Status  | Safety Output 6 Status  | Safety Output 5 Status                                                                                                    | Safety Output 4 Status  | Safety Output 3 Status                                                                                                    | Safety Output 2 Status  | Safety Output 1 Status                                                                                                    | Safety Output 0 Status  |
| 364 (868) Safety and standard                                                                | 2 Test Output 7 Status    | Test Output 6 Status    | Test Output 5 Status                                                                                                      | Test Output 4 Status    | Test Output 3 Status                                                                                                      | Test Output 2 Status    | Test Output 1 Status                                                                                                      | Test Output 0 Status    |
| 364 (868) Safety and standard                                                                |                           |                         | 3 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                           | Output Power (1)  p Error (1)                         |                                                                                                                           |                         | Reserved Reserved Muting Lamp 7 Status                                                                                    | Muting Lamp 3 Status    |
| 374 (884) Safety and standard                                                                |                           |                         |                                                                                                                           |                         |                                                                                                                           |                         | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                         |
| 374 (884) Safety and standard                                                                | 1 Safety Input 7 Status   | Safety Input 6 Status   | Safety Input 5 Status                                                                                                     | Safety Input 4 Status   | Safety Input 3 Status                                                                                                     | Safety Input 2 Status   | Safety Input 1 Status                                                                                                     | Safety Input 0 Status   |
| 374 (884) Safety and standard                                                                | 2 Safety Output 7 Status  | Safety Output 6 Status  | Safety Output 5 Status                                                                                                    | Safety Output 4 Status  | Safety Output 3 Status                                                                                                    | Safety Output 2 Status  | Safety Output 1 Status                                                                                                    | Safety Output 0 Status  |
| 374 (884) Safety and standard                                                                | 3 Safety Output 7 Monitor | Safety Output 6 Monitor | Safety Output 5 Monitor                                                                                                   | Safety Output 4 Monitor | Safety Output 3 Monitor                                                                                                   | Safety Output 2 Monitor | Safety Output 1 Monitor                                                                                                   | Safety Output 0 Monitor |
| 374 (884) Safety and standard                                                                | 4 Test Output 7 Status    | Test Output 6 Status    | Test Output 5 Status                                                                                                      | Test Output 4 Status    | Test Output 3 Status                                                                                                      | Test Output 2 Status    | Test Output 1 Status                                                                                                      | Test Output 0 Status    |
| 374 (884) Safety and standard                                                                |                           |                         | 5 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                           | Output Power (1)  p Error (1)                         |                                                                                                                           |                         | Reserved Reserved Muting Lamp 7 Status                                                                                    | Muting Lamp 3 Status    |
| 394 (916) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power |                           |                         |                                                                                                                           |                         |                                                                                                                           |                         | Error                                                                                                                     | Input Power Error       |
| 394 (916) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power | 1 Test Output 7 Status    | Test Output 6 Status    | Test Output 5 Status                                                                                                      | Test Output 4 Status    | Test Output 3 Status                                                                                                      | Test Output 2 Status    | Test Output 1 Status                                                                                                      | Test Output 0 Status    |
| 3A4 (932) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power |                           |                         |                                                                                                                           |                         |                                                                                                                           |                         | Error                                                                                                                     | Input Power Error       |
| 3A4 (932) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power | 1 Safety Output 7 Monitor | Safety Output 6 Monitor | Safety Output 5 Monitor                                                                                                   | Safety Output 4 Monitor | Safety Output 3 Monitor                                                                                                   | Safety Output 2 Monitor | Safety Output 1 Monitor                                                                                                   | Safety Output 0 Monitor |
| 3A4 (932) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power | 2 Test Output 7 Status    | Test Output 6 Status    | Test Output 5 Status                                                                                                      | Test Output 4 Status    | Test Output 3 Status                                                                                                      | Test Output 2 Status    | Test Output 1 Status                                                                                                      | Test Output 0 Status    |

Table 51 - Input Data – 1791ES-IB16 Modules

| Instance Hex (decimal) Connection Type                                                               |                                                                                                                           |                                                                                                                           | Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                                                                      |                        |                                |                        |                       |                               |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|------------------------|--------------------------------|------------------------|-----------------------|-------------------------------|
| 205 (517) Safety and standard                                                                        |                                                                                                                           |                                                                                                                           | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                        |                                |                        |                       |                               |
| 205 (517) Safety and standard                                                                        | 1 Safety Input 15                                                                                                         | Safety Input 14                                                                                                           | Safety Input 13                                                                                                           | Safety Input 12        | Safety Input 11                | Safety Input 10        |                       | Safety Input 9 Safety Input 8 |
| 225 (549) Safety and standard                                                                        |                                                                                                                           |                                                                                                                           | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                        |                                |                        |                       |                               |
| 225 (549) Safety and standard                                                                        | 1 Safety Input 15                                                                                                         | Safety Input 14                                                                                                           | Safety Input 13                                                                                                           | Safety Input 12        | Safety Input 11                | Safety Input 10        |                       | Safety Input 9 Safety Input 8 |
| 225 (549) Safety and standard                                                                        | 2 Safety Input 7 Status                                                                                                   | Safety Input 6 Status                                                                                                     | Safety Input 5 Status                                                                                                     | Safety Input 4 Status  | Safety Input 3 Status          | Safety Input 2 Status  | Safety Input 1 Status | Safety Input 0 Status         |
| 225 (549) Safety and standard                                                                        | 3 Safety Input 15 Status                                                                                                  | Safety Input 14 Status                                                                                                    | Safety Input 13 Status                                                                                                    | Safety Input 12 Status | Safety Input 11 Status         | Safety Input 10 Status | Safety Input 9 Status | Safety Input 8 Status         |
| 300 (768) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Reserved Input Power |                                                                                                                           |                                                                                                                           |                                                                                                                           |                        |                                |                        |                       | Error                         |
| 315 (789) Safety and standard                                                                        | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                                                                                                                           |                                                                                                                           |                        |                                |                        |                       |                               |
| 315 (789) Safety and standard                                                                        | 1 Safety Input 15 Status                                                                                                  | Safety Input 14 Status                                                                                                    | Safety Input 13 Status                                                                                                    | Safety Input 12 Status | Safety Input 11 Status         | Safety Input 10 Status | Safety Input 9 Status | Safety Input 8 Status         |
| 315 (789) Safety and standard                                                                        | 2 Combined Safety In Status                                                                                               |                                                                                                                           | Reserved Input Power (1)  p Error (1)                                                                                                                           |                        | Reserved Muting Lamp 15 Status | Muting Lamp 11 Status  | Muting Lamp 7 Status  | Muting Lamp 3 Status          |
| 335 (821) Safety and standard                                                                        |                                                                                                                           | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                                                                                                                           |                        |                                |                        |                       |                               |
| 335 (821) Safety and standard                                                                        | 1 Safety Input 15                                                                                                         | Safety Input 14                                                                                                           | Safety Input 13                                                                                                           | Safety Input 12        | Safety Input 11                | Safety Input 10        |                       | Safety Input 9 Safety Input 8 |
| 335 (821) Safety and standard                                                                        | 2 Safety Input 7 Status                                                                                                   | Safety Input 6 Status                                                                                                     | Safety Input 5 Status                                                                                                     | Safety Input 4 Status  | Safety Input 3 Status          | Safety Input 2 Status  | Safety Input 1 Status | Safety Input 0 Status         |
| 335 (821) Safety and standard                                                                        | 3 Safety Input 15 Status                                                                                                  | Safety Input 14 Status                                                                                                    | Safety Input 13 Status                                                                                                    | Safety Input 12 Status | Safety Input 11 Status         | Safety Input 10 Status | Safety Input 9 Status | Safety Input 8 Status         |
| 335 (821) Safety and standard                                                                        |                                                                                                                           |                                                                                                                           | 4 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                           |                        | Reserved Muting Lamp 15 Status | Muting Lamp 11 Status  | Muting Lamp 7 Status  | Muting Lamp 3 Status          |
| 365 (869) Safety and standard                                                                        |                                                                                                                           |                                                                                                                           | 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                        |                                |                        |                       |                               |
| 365 (869) Safety and standard                                                                        | 1 Safety Input 15                                                                                                         | Safety Input 14                                                                                                           | Safety Input 13                                                                                                           | Safety Input 12        | Safety Input 11                | Safety Input 10        |                       | Safety Input 9 Safety Input 8 |
| 365 (869) Safety and standard                                                                        | 2 Safety Input 7 Status                                                                                                   | Safety Input 6 Status                                                                                                     | Safety Input 5 Status                                                                                                     | Safety Input 4 Status  | Safety Input 3 Status          | Safety Input 2 Status  | Safety Input 1 Status | Safety Input 0 Status         |
| 365 (869) Safety and standard                                                                        | 3 Safety Input 15 Status                                                                                                  | Safety Input 14 Status                                                                                                    | Safety Input 13 Status                                                                                                    | Safety Input 12 Status | Safety Input 11 Status         | Safety Input 10 Status | Safety Input 9 Status | Safety Input 8 Status         |
| 365 (869) Safety and standard                                                                        | 4 Test Output 7 Status                                                                                                    | Test Output 6 Status                                                                                                      | Test Output 5 Status                                                                                                      | Test Output 4 Status   | Test Output 3 Status           | Test Output 2 Status   | Test Output 1 Status  | Test Output 0 Status          |
| 365 (869) Safety and standard                                                                        | 5 Test Output 15 Status                                                                                                   | Test Output 14 Status                                                                                                     | Test Output 13 Status                                                                                                     | Test Output 12 Status  | Test Output 11 Status          | Test Output 10 Status  | Test Output 9 Status  | Test Output 8 Status          |
| 365 (869) Safety and standard                                                                        |                                                                                                                           |                                                                                                                           | 6 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                           | Output Power (1)  p Error (1)                        | Muting Lamp 15 Status          | Muting Lamp 11 Status  | Muting Lamp 7 Status  | Muting Lamp 3 Status          |
| 385 (901) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Reserved Input Power |                                                                                                                           |                                                                                                                           |                                                                                                                           |                        |                                |                        |                       | Error                         |
| 385 (901) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Reserved Input Power | 1 Test Output 7 Status                                                                                                    | Test Output 6 Status                                                                                                      | Test Output 5 Status                                                                                                      | Test Output 4 Status   | Test Output 3 Status           | Test Output 2 Status   | Test Output 1 Status  | Test Output 0 Status          |
| 385 (901) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Reserved Input Power | 2 Test Output 15 Status                                                                                                   | Test Output 14 Status                                                                                                     | Test Output 13 Status                                                                                                     | Test Output 12 Status  | Test Output 11 Status          | Test Output 10 Status  | Test Output 9 Status  | Test Output 8 Status          |

Table 52 - Output Data – 1791ES-IB8XOVB4 Modules

| Instance Hex (decimal)   | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                     |                   |                   |                   |                   |                   |                   |                   |
|--------------------------|------------------------------------------------------------------------|---------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
|                          | 22 (34) Safety and standard 0 Standard                                 | Output 7 (1)        | Standard Output 6 | Standard Output 5 | Standard Output 4 | Standard Output 3 | Standard Output 2 | Standard Output 1 | Standard Output 0 |
|                          | 234 (564) Only safety 0 Safety                                         | Output 7            | Safety Output 6   | Safety Output 5   | Safety Output 4   | Safety Output 3   | Safety Output 2   | Safety Output 1   | Safety Output 0   |
|                          | 2C4 (708) Only safety 0 Safety                                         | Output 7            | Safety Output 6   | Safety Output 5   | Safety Output 4   | Safety Output 3   | Safety Output 2   | Safety Output 1   | Safety Output 0   |
|                          |                                                                        | 1 Standard Output 7 | Standard Output 6 | Standard Output 5 | Standard Output 4 | Standard Output 3 | Standard Output 2 | Standard Output 1 | Standard Output 0 |

Table 53 - Output Data – 1791ES-IB16 Modules

| Instance Hex (decimal)   | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                      |                    |                    |                    |                    |                    |                   |                   |
|--------------------------|------------------------------------------------------------------------|----------------------|--------------------|--------------------|--------------------|--------------------|--------------------|-------------------|-------------------|
|                          | 23 (35) Safety and standard 0 Standard                                 | Output 7             | Standard Output 6  | Standard Output 5  | Standard Output 4  | Standard Output 3  | Standard Output 2  | Standard Output 1 | Standard Output 0 |
|                          |                                                                        | 1 Standard Output 15 | Standard Output 14 | Standard Output 13 | Standard Output 12 | Standard Output 11 | Standard Output 10 | Standard Output 9 | Standard Output 8 |

## 1732ES Modules

The bits in the tag definitions of the programming software are different than those bits that are shown in the following section. Table 54 the name associations for clarification with the programming software.

Table 54 - Bit Definitions and Programming Software Tag Names

|                            | Bit Definitions Programming Software Tag Name            |
|----------------------------|----------------------------------------------------------|
| Safety Input 0…11          | ModuleName:I.Pt00Data - Pt11Data                         |
| Safety Input 0…11 Status   | ModuleName:I.Pt00InputStatus - Pt11InputStatus           |
| Combined Safety In Status  | ModuleName:I.InputStatus                                 |
| Muting Lamp Status         | ModuleName:I.MutingStatusXX where XX = 03, 07, 11        |
| Safety Output 0…3          | ModuleName:O.Pt00Data - Pt03Data                         |
| Safety Output 0…3 Status   | ModuleName:I.Pt00OutputStatus - Pt03OutputStatus         |
| Combined Safety Out Status | ModuleName:I.OutputStatus                                |
| Safety Output 0…3 Monitor  | ModuleName:I.Pt00Readback - Pt03Readback                 |
| Test Output 0…11 Data      | ModuleName:O.Test00Data - Test11Data                     |
| Test Output 0…11 Status    | ModuleName:I.Pt00TestOutputStatus - Pt11TestOutputStatus |
| Input Power Status         | ModuleName:I.InputPowerStatus                            |
| Output Power Status        | ModuleName:I.OutputPowerStatus                           |

Table 55 - Input Data 1732ES-IB16 Modules

| Instance Hex (decimal)   |                                                                                                                                          |                        | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                                                                     |                        |                                                                                                                                          |                        |                       |                                                                                                            |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------|-----------------------|------------------------------------------------------------------------------------------------------------|
|                          |                                                                                                                                          |                        | 205 (517) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                        |                                                                                                                                          |                        |                       | Safety Input 0                                                                                             |
|                          | 1 Safety Input 15                                                                                                                        | Safety Input 14        | Safety Input 13                                                                                                                          | Safety Input 12        | Safety Input 11                                                                                                                          | Safety Input 10        |                       | Safety Input 9 Safety Input 8                                                                              |
|                          | 225 (549) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                        |                                                                                                                                          |                        |                                                                                                                                          |                        |                       | Safety Input 0                                                                                             |
|                          | 1 Safety Input 15                                                                                                                        | Safety Input 14        | Safety Input 13                                                                                                                          | Safety Input 12        | Safety Input 11                                                                                                                          | Safety Input 10        |                       | Safety Input 9 Safety Input 8                                                                              |
|                          | 2 Safety Input 7 Status                                                                                                                  | Safety Input 6 Status  | Safety Input 5 Status                                                                                                                    | Safety Input 4 Status  | Safety Input 3 Status                                                                                                                    | Safety Input 2 Status  | Safety Input 1 Status | Safety Input 0 Status                                                                                      |
|                          | 3 Safety Input 15 Status                                                                                                                 | Safety Input 14 Status | Safety Input 13 Status                                                                                                                   | Safety Input 12 Status | Safety Input 11 Status                                                                                                                   | Safety Input 10 Status | Safety Input 9 Status | Safety Input 8 Status                                                                                      |
|                          |                                                                                                                                          |                        |                                                                                                                                          |                        |                                                                                                                                          |                        |                       | 300 (768) Standard only 0 Reserved Reserved Reserved Reserved Reserved Reserved Reserved Input Power Error |
|                          |                                                                                                                                          |                        |                                                                                                                                          |                        | 315 (789) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                        |                       | Safety Input 0                                                                                             |
|                          | 1 Safety Input 15                                                                                                                        | Safety Input 14        | Safety Input 13                                                                                                                          | Safety Input 12        | Safety Input 11                                                                                                                          | Safety Input 10        |                       | Safety Input 9 Safety Input 8                                                                              |
|                          | 2 Combined Safety In Status                                                                                                              |                        | Reserved Input Power (1)  p Error (1)                                                                                                                                          |                        | Reserved Muting Lamp 15 Status                                                                                                           | Muting Lamp 11 Status  | Muting Lamp 7 Status  | Muting Lamp 3 Status                                                                                       |
|                          | 335 (821) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                        |                                                                                                                                          |                        |                                                                                                                                          |                        |                       | Safety Input 0                                                                                             |
|                          | 1 Safety Input 15                                                                                                                        | Safety Input 14        | Safety Input 13                                                                                                                          | Safety Input 12        | Safety Input 11                                                                                                                          | Safety Input 10        |                       | Safety Input 9 Safety Input 8                                                                              |
|                          | 2 Safety Input 7 Status                                                                                                                  | Safety Input 6 Status  | Safety Input 5 Status                                                                                                                    | Safety Input 4 Status  | Safety Input 3 Status                                                                                                                    | Safety Input 2 Status  | Safety Input 1 Status | Safety Input 0 Status                                                                                      |
|                          | 3 Safety Input 15 Status                                                                                                                 | Safety Input 14 Status | Safety Input 13 Status                                                                                                                   | Safety Input 12 Status | Safety Input 11 Status                                                                                                                   | Safety Input 10 Status | Safety Input 9 Status | Safety Input 8 Status                                                                                      |
|                          |                                                                                                                                          |                        | 4 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                                          |                        | Reserved Muting Lamp 15 Status                                                                                                           | Muting Lamp 11 Status  | Muting Lamp 7 Status  | Muting Lamp 3 Status                                                                                       |
|                          | 365 (869) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                        |                                                                                                                                          |                        |                                                                                                                                          |                        |                       | Safety Input 0                                                                                             |
|                          | 1 Safety Input 15                                                                                                                        | Safety Input 14        | Safety Input 13                                                                                                                          | Safety Input 12        | Safety Input 11                                                                                                                          | Safety Input 10        |                       | Safety Input 9 Safety Input 8                                                                              |
|                          | 2 Safety Input 7 Status                                                                                                                  | Safety Input 6 Status  | Safety Input 5 Status                                                                                                                    | Safety Input 4 Status  | Safety Input 3 Status                                                                                                                    | Safety Input 2 Status  | Safety Input 1 Status | Safety Input 0 Status                                                                                      |
|                          | 3 Safety Input 15 Status                                                                                                                 | Safety Input 14 Status | Safety Input 13 Status                                                                                                                   | Safety Input 12 Status | Safety Input 11 Status                                                                                                                   | Safety Input 10 Status | Safety Input 9 Status | Safety Input 8 Status                                                                                      |
|                          | 4 Test Output 7 Status                                                                                                                   | Test Output 6 Status   | Test Output 5 Status                                                                                                                     | Test Output 4 Status   | Test Output 3 Status                                                                                                                     | Test Output 2 Status   | Test Output 1 Status  | Test Output 0 Status                                                                                       |
|                          | 5 Test Output 15 Status                                                                                                                  | Test Output 14 Status  | Test Output 13 Status                                                                                                                    | Test Output 12 Status  | Test Output 11 Status                                                                                                                    | Test Output 10 Status  | Test Output 9 Status  | Test Output 8 Status                                                                                       |
|                          |                                                                                                                                          |                        | 6 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                                          |                        | Reserved Muting Lamp 15 Status                                                                                                           | Muting Lamp 11 Status  | Muting Lamp 7 Status  | Muting Lamp 3 Status                                                                                       |
|                          |                                                                                                                                          |                        |                                                                                                                                          |                        |                                                                                                                                          |                        |                       | 385 (901) Standard only 0 Reserved Reserved Reserved Reserved Reserved Reserved Reserved Input Power Error |
|                          | 1 Test Output 7 Status                                                                                                                   | Test Output 6 Status   | Test Output 5 Status                                                                                                                     | Test Output 4 Status   | Test Output 3 Status                                                                                                                     | Test Output 2 Status   | Test Output 1 Status  | Test Output 0 Status                                                                                       |
|                          | 2 Test Output 15 Status                                                                                                                  | Test Output 14 Status  | Test Output 13 Status                                                                                                                    | Test Output 12 Status  | Test Output 11 Status                                                                                                                    | Test Output 10 Status  | Test Output 9 Status  | Test Output 8 Status                                                                                       |

See Table 55 … Table 60 for reference data related to input and output data.

Table 56 - Input Data 1732ES-IB8XOBV4 and 1732ES-IB8XOB8 Modules

| Instance Hex (decimal)   |                                                                                                                                          |                            | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                                                                     |                         |                         |                                                                                                                                          |                                                                                                    |                         |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------|
|                          | 204 (516) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                            |                                                                                                                                          |                         |                         |                                                                                                                                          |                                                                                                    | Safety Input 0          |
|                          | 224 (548) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                            |                                                                                                                                          |                         |                         |                                                                                                                                          |                                                                                                    | Safety Input 0          |
|                          | 1 Safety Input 7 Status                                                                                                                  | Safety Input 6 Status      | Safety Input 5 Status                                                                                                                    | Safety Input 4 Status   | Safety Input 3 Status   | Safety Input 2 Status                                                                                                                    | Safety Input 1 Status                                                                              | Safety Input 0 Status   |
|                          |                                                                                                                                          |                            |                                                                                                                                          |                         |                         |                                                                                                                                          | 301 (769) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power Error | Input Power Error       |
|                          |                                                                                                                                          |                            |                                                                                                                                          |                         |                         | 324 (804) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                                                                                                    | Safety Input 0          |
|                          | 1 Combined Safety In Status                                                                                                              | Combined Safety Out Status | Input Power (1)  p Error (1)                                                                                                                                          | Output Power (1)  p Error (1)                         |                         |                                                                                                                                          | Reserved Reserved Muting Lamp 7 Status                                                             | Muting Lamp 3 Status    |
|                          | 334 (820) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                            |                                                                                                                                          |                         |                         |                                                                                                                                          |                                                                                                    | Safety Input 0          |
|                          | 1 Safety Input7 Status                                                                                                                   | Safety Input 6 Status      | Safety Input 5 Status                                                                                                                    | Safety Input 4 Status   | Safety Input 3 Status   | Safety Input 2 Status                                                                                                                    | Safety Input 1 Status                                                                              | Safety Input 0 Status   |
|                          |                                                                                                                                          |                            | 2 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                                          | Output Power (1)  p Error (1)                         |                         |                                                                                                                                          | Reserved Reserved Muting Lamp 7 Status                                                             | Muting Lamp 3 Status    |
|                          |                                                                                                                                          |                            | 344 (836) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                         |                         |                                                                                                                                          |                                                                                                    | Safety Input 0          |
|                          | 1 Safety Input 7 Status                                                                                                                  | Safety Input 6 Status      | Safety Input 5 Status                                                                                                                    | Safety Input 4 Status   | Safety Input 3 Status   | Safety Input 2 Status                                                                                                                    | Safety Input 1 Status                                                                              | Safety Input 0 Status   |
|                          | 2 Safety Output 7 Status                                                                                                                 | Safety Output 6 Status     | Safety Output 5 Status                                                                                                                   | Safety Output 4 Status  | Safety Output 3 Status  | Safety Output 2 Status                                                                                                                   | Safety Output 1 Status                                                                             | Safety Output 0 Status  |
|                          |                                                                                                                                          |                            | 3 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                                          | Output Power (1)  p Error (1)                         |                         |                                                                                                                                          | Reserved Reserved Muting Lamp 7 Status                                                             | Muting Lamp 3 Status    |
|                          | 354 (852) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                            |                                                                                                                                          |                         |                         |                                                                                                                                          |                                                                                                    | Safety Input 0          |
|                          | 1 Safety Input 7 Status                                                                                                                  | Safety Input 6 Status      | Safety Input 5 Status                                                                                                                    | Safety Input 4 Status   | Safety Input 3 Status   | Safety Input 2 Status                                                                                                                    | Safety Input 1 Status                                                                              | Safety Input 0 Status   |
|                          | 2 Safety Output 7 Status                                                                                                                 | Safety Output 6 Status     | Safety Output 5 Status                                                                                                                   | Safety Output 4 Status  | Safety Output 3 Status  | Safety Output 2 Status                                                                                                                   | Safety Output 1 Status                                                                             | Safety Output 0 Status  |
|                          | 3 Safety Output 7 Monitor                                                                                                                | Safety Output 6 Monitor    | Safety Output 5 Monitor                                                                                                                  | Safety Output 4 Monitor | Safety Output 3 Monitor | Safety Output 2 Monitor                                                                                                                  | Safety Output 1 Monitor                                                                            | Safety Output 0 Monitor |
|                          |                                                                                                                                          |                            | 4 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                                          | Output Power (1)  p Error (1)                         |                         |                                                                                                                                          | Reserved Reserved Muting Lamp 7 Status                                                             | Muting Lamp 3 Status    |
|                          |                                                                                                                                          |                            |                                                                                                                                          |                         |                         | 364 (868) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                                                                                                    | Safety Input 0          |
|                          | 1 Safety Input 7 Status                                                                                                                  | Safety Input 6 Status      | Safety Input 5 Status                                                                                                                    | Safety Input 4 Status   | Safety Input 3 Status   | Safety Input 2 Status                                                                                                                    | Safety Input 1 Status                                                                              | Safety Input 0 Status   |
|                          | 2 Test Output 7 Status                                                                                                                   | Test Output 6 Status       | Test Output 5 Status                                                                                                                     | Test Output 4 Status    | Test Output 3 Status    | Test Output 2 Status                                                                                                                     | Test Output 1 Status                                                                               | Test Output O Status    |
|                          |                                                                                                                                          |                            | 3 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                                          | Output Power (1)  p Error (1)                         |                         |                                                                                                                                          | Reserved Reserved Muting Lamp 7 Status                                                             | Muting Lamp 3 Status    |
|                          | 374 (884) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                            |                                                                                                                                          |                         |                         |                                                                                                                                          |                                                                                                    | Safety Input 0          |
|                          | 1 Safety Input 7 Status                                                                                                                  | Safety Input 6 Status      | Safety Input 5 Status                                                                                                                    | Safety Input 4 Status   | Safety Input 3 Status   | Safety Input 2 Status                                                                                                                    | Safety Input 1 Status                                                                              | Safety Input 0 Status   |
|                          | 2 Safety Output 7 Status                                                                                                                 | Safety Output 6 Status     | Safety Output 5 Status                                                                                                                   | Safety Output 4 Status  | Safety Output 3 Status  | Safety Output 2 Status                                                                                                                   | Safety Output 1 Status                                                                             | Safety Output 0 Status  |
|                          | 3 Safety Output 7 Monitor                                                                                                                | Safety Output 6 Monitor    | Safety Output 5 Monitor                                                                                                                  | Safety Output 4 Monitor | Safety Output 3 Monitor | Safety Output 2 Monitor                                                                                                                  | Safety Output 1 Monitor                                                                            | Safety Output 0 Monitor |
|                          | 4 Test Output 7 Status                                                                                                                   | Test Output 6 Status       | Test Output 5 Status                                                                                                                     | Test Output 4 Status    | Test Output 3 Status    | Test Output 2 Status                                                                                                                     | Test Output 1 Status                                                                               | Test Output 0 Status    |
|                          |                                                                                                                                          | 6 Reserved Reserved Input Power (1)                            | p Error (1)                                                                                                                                          | Output Power (1)  p Error (1)                         |                         |                                                                                                                                          | Reserved Reserved Muting Lamp 7 Status                                                             | Muting Lamp 3 Status    |

Table 56 - Input Data 1732ES-IB8XOBV4 and 1732ES-IB8XOB8 Modules (Continued)

| Instance Hex (decimal)   | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                         |                           |                         |                         |                         |                         |                         |                         |                         |
|--------------------------|----------------------------------------------------------------------------------------------|---------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
|                          | 394 (916) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power |                           |                         |                         |                         |                         |                         | Error                   | Input Power Error       |
|                          | 394 (916) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power | 1 Test Output 7 Status    | Test Output 6 Status    | Test Output 5 Status    | Test Output 4 Status    | Test Output 3 Status    | Test Output 2 Status    | Test Output 1 Status    | Test Output 0 Status    |
|                          | 3A4 (932) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power |                           |                         |                         |                         |                         |                         | Error                   | Input Power Error       |
|                          | 3A4 (932) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power | 1 Safety Output 7 Monitor | Safety Output 6 Monitor | Safety Output 5 Monitor | Safety Output 4 Monitor | Safety Output 3 Monitor | Safety Output 2 Monitor | Safety Output 1 Monitor | Safety Output 0 Monitor |
|                          | 3A4 (932) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power | 2 Test Output 7 Status    | Test Output 6 Status    | Test Output 5 Status    | Test Output 4 Status    | Test Output 3 Status    | Test Output 2 Status    | Test Output 1 Status    | Test Output 0 Status    |

Table 57 - Input Data – 1732ES-IB12XOBV2 and 1732ES-IB12XOB4 Modules

| Instance Hex (decimal)   |                                                                                                                                                 |                            |                                                                                                                                                 |                       |                                                              |                                                                                                                                          | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                               |                               |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
|                          |                                                                                                                                                 |                            | 20C (524) Only safety 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                       |                                                              |                                                                                                                                          |                                                                                                    |                               |
|                          |                                                                                                                                                 |                            |                                                                                                                                                 |                       | 1 Reserved Reserved Reserved Reserved Safety Input 11        | Safety Input 10                                                                                                                          |                                                                                                    | Safety Input 9 Safety Input 8 |
|                          | 22C (556) Only safety 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 Safety Input 0 |                            |                                                                                                                                                 |                       |                                                              |                                                                                                                                          |                                                                                                    |                               |
|                          | 1 Safety Input 3 Status                                                                                                                         | Safety Input 2 Status      | Safety Input 1 Status                                                                                                                           | Safety Input 0 Status | Safety Input 11                                              | Safety Input 10                                                                                                                          |                                                                                                    | Safety Input 9 Safety Input 8 |
|                          | 2 Safety Input 11 Status                                                                                                                        | Safety Input 10 Status     | Safety Input 9 Status                                                                                                                           | Safety Input 8 Status | Safety Input 7 Status                                        | Safety Input 6 Status                                                                                                                    | Safety Input 5 Status                                                                              | Safety Input 4 Status         |
|                          |                                                                                                                                                 |                            |                                                                                                                                                 |                       |                                                              |                                                                                                                                          | 301 (769) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power Error | Input Power Error             |
|                          |                                                                                                                                                 |                            |                                                                                                                                                 |                       |                                                              | 32C (812) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                                                                                                    | Safety Input 0                |
|                          |                                                                                                                                                 |                            |                                                                                                                                                 |                       | 1 Reserved Reserved Reserved Reserved Safety Input 11        | Safety Input 10                                                                                                                          |                                                                                                    | Safety Input 9 Safety Input 8 |
|                          | 2 Combined Safety In Status                                                                                                                     | Combined Safety Out Status | Input Power (1)  p Error (1)                                                                                                                                                 | Output Power (1)  p Error (1)                       |                                                              | Reserved Muting Lamp 11 Status                                                                                                           | Muting Lamp 7 Status                                                                               | Muting Lamp 3 Status          |
|                          | 33C (828) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1        |                            |                                                                                                                                                 |                       |                                                              |                                                                                                                                          |                                                                                                    | Safety Input 0                |
|                          | 1 Safety Input 3 Status                                                                                                                         | Safety Input 2 Status      | Safety Input 1 Status                                                                                                                           | Safety Input 0 Status | Safety Input 11                                              | Safety Input 10                                                                                                                          |                                                                                                    | Safety Input 9 Safety Input 8 |
|                          | 2 Safety Input 11 Status                                                                                                                        | Safety Input 10 Status     | Safety Input 9 Status                                                                                                                           | Safety Input 8 Status | Safety Input 7 Status                                        | Safety Input 6 Status                                                                                                                    | Safety Input 5 Status                                                                              | Safety Input 4 Status         |
|                          |                                                                                                                                                 |                            | 3 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                                                 | Output Power (1)  p Error (1)                       |                                                              | Reserved Muting Lamp 11 Status                                                                                                           | Muting Lamp 7 Status                                                                               | Muting Lamp 3 Status          |
|                          |                                                                                                                                                 |                            | 34C (844) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1        |                       |                                                              |                                                                                                                                          |                                                                                                    | Safety Input 0                |
|                          | 1 Safety Input 3 Status                                                                                                                         | Safety Input 2 Status      | Safety Input 1 Status                                                                                                                           | Safety Input 0 Status | Safety Input 11                                              | Safety Input 10                                                                                                                          |                                                                                                    | Safety Input 9 Safety Input 8 |
|                          | 2 Safety Input 11 Status                                                                                                                        | Safety Input 10 Status     | Safety Input 9 Status                                                                                                                           | Safety Input 8 Status | Safety Input 7 Status                                        | Safety Input 6 Status                                                                                                                    | Safety Input 5 Status                                                                              | Safety Input 4 Status         |
|                          |                                                                                                                                                 |                            |                                                                                                                                                 |                       | 3 Reserved Reserved Reserved Reserved Safety Output 3 Status | Safety Output 2 Status                                                                                                                   | Safety Output 1 Status                                                                             | Safety Output 0 Status        |
|                          |                                                                                                                                                 |                            | 4 Reserved Reserved Input Power (1)  p Error (1)                                                                                                                                                 | Output Power (1)  p Error (1)                       |                                                              | Reserved Muting Lamp 11 Status                                                                                                           | Muting Lamp 7 Status                                                                               | Muting Lamp 3 Status          |

Table 57 - Input Data – 1732ES-IB12XOBV2 and 1732ES-IB12XOB4 Modules (Continued)

| Instance Hex (decimal)   |                                                                                                                                          |                         |                         | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0                                                                     |                                                             |                                |                                                                                                    |                               |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------|
|                          |                                                                                                                                          |                         |                         | 35C (860) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                                                             |                                |                                                                                                    | Safety Input 0                |
|                          | 1 Safety Input 3 Status                                                                                                                  | Safety Input 2 Status   | Safety Input 1 Status   | Safety Input 0 Status                                                                                                                    | Safety Input 11                                             | Safety Input 10                |                                                                                                    | Safety Input 9 Safety Input 8 |
|                          | 2 Safety Input 11 Status                                                                                                                 | Safety Input 10 Status  | Safety Input 9 Status   | Safety Input 8 Status                                                                                                                    | Safety Input 7 Status                                       | Safety Input 6 Status          | Safety Input 5 Status                                                                              | Safety Input 4 Status         |
|                          | 3 Safety Output 3 Monitor                                                                                                                | Safety Output 2 Monitor | Safety Output 1 Monitor | Safety Output 0 Monitor                                                                                                                  | Safety Output 3 Status                                      | Safety Output 2 Status         | Safety Output 1 Status                                                                             | Safety Output 0 Status        |
|                          |                                                                                                                                          |                         | 4 Reserved Reserved Input Power (1)  p Error (1)                         | Output Power (1)  p Error (1)                                                                                                                                          |                                                             | Reserved Muting Lamp 11 Status | Muting Lamp 7 Status                                                                               | Muting Lamp 3 Status          |
|                          |                                                                                                                                          |                         |                         | 36C (876) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                                                             |                                |                                                                                                    | Safety Input 0                |
|                          | 1 Safety Input 3 Status                                                                                                                  | Safety Input 2 Status   | Safety Input 1 Status   | Safety Input 0 Status                                                                                                                    | Safety Input 11                                             | Safety Input 10                |                                                                                                    | Safety Input 9 Safety Input 8 |
|                          | 2 Safety Input 11 Status                                                                                                                 | Safety Input 10 Status  | Safety Input 9 Status   | Safety Input 8 Status                                                                                                                    | Safety Input 7 Status                                       | Safety Input 6 Status          | Safety Input 5 Status                                                                              | Safety Input 4 Status         |
|                          | 3 Test Output 7 Status                                                                                                                   | Test Output 6 Status    | Test Output 5 Status    | Test Output 4 Status                                                                                                                     | Test Output 3 Status                                        | Test Output 2 Status           | Test Output 1 Status                                                                               | Test Output O Status          |
|                          |                                                                                                                                          |                         |                         |                                                                                                                                          | 4 Reserved Reserved Reserved Reserved Test Output 11 Status | Test Output 10 Status          | Test Output 9 Status                                                                               | Test Output 8 Status          |
|                          |                                                                                                                                          |                         | 5 Reserved Reserved Input Power (1)  p Error (1)                         | Output Power (1)  p Error (1)                                                                                                                                          |                                                             | Reserved Muting Lamp 11 Status | Muting Lamp 7 Status                                                                               | Muting Lamp 3 Status          |
|                          | 37C (892) Safety and standard 0 Safety Input 7 Safety Input 6 Safety Input 5 Safety Input 4 Safety Input 3 Safety Input 2 Safety Input 1 |                         |                         |                                                                                                                                          |                                                             |                                |                                                                                                    | Safety Input 0                |
|                          | 1 Safety Input 3 Status                                                                                                                  | Safety Input 2 Status   | Safety Input 1 Status   | Safety Input 0 Status                                                                                                                    | Safety Input 11                                             | Safety Input 10                |                                                                                                    | Safety Input 9 Safety Input 8 |
|                          | 2 Safety Input 11 Status                                                                                                                 | Safety Input 10 Status  | Safety Input 9 Status   | Safety Input 8 Status                                                                                                                    | Safety Input 7 Status                                       | Safety Input 6 Status          | Safety Input 5 Status                                                                              | Safety Input 4 Status         |
|                          | 3 Safety Output 3 Monitor                                                                                                                | Safety Output 2 Monitor | Safety Output 1 Monitor | Safety Output 0 Monitor                                                                                                                  | Safety Output 3 Status                                      | Safety Output 2 Status         | Safety Output 1 Status                                                                             | Safety Output 0 Status        |
|                          | 4 Test Output 7 Status                                                                                                                   | Test Output 6 Status    | Test Output 5 Status    | Test Output 4 Status                                                                                                                     | Test Output 3 Status                                        | Test Output 2 Status           | Test Output 1 Status                                                                               | Test Output 0 Status          |
|                          |                                                                                                                                          |                         |                         |                                                                                                                                          | 5 Reserved Reserved Reserved Reserved Test Output 11 Status | Test Output 10 Status          | Test Output 9 Status                                                                               | Test Output 8 Status          |
|                          |                                                                                                                                          |                         | 6 Reserved Reserved Input Power (1)  p Error (1)                         | Output Power (1)  p Error (1)                                                                                                                                          |                                                             | Reserved Muting Lamp 11 Status | Muting Lamp 7 Status                                                                               | Muting Lamp 3 Status          |
|                          |                                                                                                                                          |                         |                         |                                                                                                                                          |                                                             |                                | 39C (924) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power Error | Input Power Error             |
|                          | 1 Test Output 7 Status                                                                                                                   | Test Output 6 Status    | Test Output 5 Status    | Test Output 4 Status                                                                                                                     | Test Output 3 Status                                        | Test Output 2 Status           | Test Output 1 Status                                                                               | Test Output 0 Status          |
|                          |                                                                                                                                          |                         |                         |                                                                                                                                          | 2 Reserved Reserved Reserved Reserved Test Output 11 Status | Test Output 10 Status          | Test Output 9 Status                                                                               | Test Output 8 Status          |
|                          |                                                                                                                                          |                         |                         |                                                                                                                                          |                                                             |                                | 3AC (940) Only standard 0 Reserved Reserved Reserved Reserved Reserved Reserved Output Power Error | Input Power Error             |
|                          | 1 Test Output 3 Status                                                                                                                   | Test Output 2 Status    | Test Output 1 Status    | Test Output 0 Status                                                                                                                     | Safety Output 3 Monitor                                     | Safety Output 2 Monitor        | Safety Output 1 Monitor                                                                            | Safety Output 0 Monitor       |
|                          | 2 Test Output 11 Status                                                                                                                  | Test Output 10 Status   | Test Output 9 Status    | Test Output 8 Status                                                                                                                     | Test Output 7 Status                                        | Test Output 6 Status           | Test Output 5 Status                                                                               | Test Output 4 Status          |

Table 58 - Output Data 1732ES-IB16 Modules

| Instance Hex (decimal)   | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                      |                    |                    |                    |                    |                    |                   |                   |
|--------------------------|------------------------------------------------------------------------|----------------------|--------------------|--------------------|--------------------|--------------------|--------------------|-------------------|-------------------|
|                          | 23 (35) Safety and standard 0 Standard                                 | Output 7             | Standard Output 6  | Standard Output 5  | Standard Output 4  | Standard Output 3  | Standard Output 2  | Standard Output 1 | Standard Output 0 |
|                          |                                                                        | 1 Standard Output 15 | Standard Output 14 | Standard Output 13 | Standard Output 12 | Standard Output 11 | Standard Output 10 | Standard Output 9 | Standard Output 8 |

Table 59 - Output Data 1732ES-IB8XOBV4 and 1732ES-IB8XOB8 Modules

| Instance Hex (decimal)   | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                     |                   |                   |                   |                   |                   |                   |                   |
|--------------------------|------------------------------------------------------------------------|---------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
|                          | 22 (34) Safety and standard 0 Standard                                 | Output 7            | Standard Output 6 | Standard Output 5 | Standard Output 4 | Standard Output 3 | Standard Output 2 | Standard Output 1 | Standard Output 0 |
|                          | 234 (564) Only safety 0 Safety                                         | Output 7            | Safety Output 6   | Safety Output 5   | Safety Output 4   | Safety Output 3   | Safety Output 2   | Safety Output 1   | Safety Output 0   |
|                          | 2C4 (708) Safety and standard 0 Safety                                 | Output 7            | Safety Output 6   | Safety Output 5   | Safety Output 4   | Safety Output 3   | Safety Output 2   | Safety Output 1   | Safety Output 0   |
|                          |                                                                        | 1 Standard Output 7 | Standard Output 6 | Standard Output 5 | Standard Output 4 | Standard Output 3 | Standard Output 2 | Standard Output 1 | Standard Output 0 |

Table 60 - Output Data 1732ES-IB12XOBV2 and 1732ES-IB12XOB4 Modules

| Instance Hex (decimal)   | Connection Type Byte Bit 7 Bit 6 Bit 5 Bit 4 Bit 3 Bit 2 Bit 1 Bit 0   |                                                |                    |                   |                   |                   |                    |                   |                   |
|--------------------------|------------------------------------------------------------------------|------------------------------------------------|--------------------|-------------------|-------------------|-------------------|--------------------|-------------------|-------------------|
|                          | 25 (37) Only standard 0 Standard                                       | Output 7                                       | Standard Output 6  | Standard Output 5 | Standard Output 4 | Standard Output 3 | Standard Output 2  | Standard Output 1 | Standard Output 0 |
|                          |                                                                        | 1 Reserved Reserved Reserved Reserved Standard |                    |                   |                   | Output 11         | Standard Output 10 | Standard Output 9 | Standard Output 8 |
|                          | 233 (563) Only safety 0 Reserved Reserved Reserved Reserved Safety     |                                                |                    |                   |                   | Output 3          | Safety Output 2    | Safety Output 1   | Safety Output 0   |
|                          | 3C4 (964) Safety and standard 0 Standard                               | Output 3                                       | Standard Output 2  | Standard Output 1 | Standard Output 0 | Safety Output 3   | Safety Output 2    | Safety Output 1   | Safety Output 0   |
|                          |                                                                        | 1 Standard Output 11                           | Standard Output 10 | Standard Output 9 | Standard Output 8 | Standard Output 7 | Standard Output 6  | Standard Output 5 | Standard Output 4 |

## Explicit Messages

Explicit Messaging can also be used to read individual channel status for safety inputs, safety outputs, test outputs, and power status. You can also configure communication error settings for test outputs.

Table 61 - Reading the Cause of the Safety Input Error

| Explicit Message                                     |                      |                                                                                      | Service Function Command (hex) Response (hex)   | Service Function Command (hex) Response (hex)   | Service Function Command (hex) Response (hex)   | Service Function Command (hex) Response (hex)   | Service Function Command (hex) Response (hex)                                                                                                                                 |
|------------------------------------------------------|----------------------|--------------------------------------------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                      |                      |                                                                                      | Service Code                                    | Class ID                                        | Instance ID                                     | Attribute ID Data Size                          |                                                                                                                                                                               |
| Safety input cause of error (fault) information read | Get attribute Single | Reads the cause for the status bit (1…n), specified by the Instance ID, turning OFF. |                                                 |                                                 |                                                 |                                                 | 0E 3D 01…n 6E - 0: No error 01: Configuration invalid 02: External test signal error 03: Internal input error 04: Discrepancy error 05: Error in the other dual channel input |

Table 62 - Reading the Cause of the Safety Output Error

| Explicit Message                                 |                      |                                                                                      | Service Function Command (hex) Response (hex)   | Service Function Command (hex) Response (hex)   | Service Function Command (hex) Response (hex)   | Service Function Command (hex) Response (hex)   | Service Function Command (hex) Response (hex)                                                                                                                                                                                               |
|--------------------------------------------------|----------------------|--------------------------------------------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                  |                      |                                                                                      | Service Code                                    | Class ID                                        | Instance ID                                     | Attribute ID Data Size                          |                                                                                                                                                                                                                                             |
| Safety output cause of error (fault) information | Get attribute single | Reads the cause for the status bit (1…n), specified by the Instance ID, turning OFF. |                                                 |                                                 |                                                 |                                                 | 0E 3B 01…n 6E - 0: No error 01: Configuration invalid 02: Over current detected 03: Short circuit detected 04: Output ON error 05: Error in the other dual channel output 08: Output data error 09: Short circuit detected at safety output |

## Table 63 - Monitoring the Test Output Point

|                                                |                      |                                                                                      | Explicit Message Service Function Command (hex) Response (hex)   | Explicit Message Service Function Command (hex) Response (hex)   | Explicit Message Service Function Command (hex) Response (hex)   | Explicit Message Service Function Command (hex) Response (hex)                                                                             | Explicit Message Service Function Command (hex) Response (hex)   |
|------------------------------------------------|----------------------|--------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
|                                                |                      |                                                                                      | Service Code                                                     | Class ID                                                         | Instance ID Attribute ID Data Size                               |                                                                                                                                            |                                                                  |
| Test output cause of error (fault) information | Get attribute single | Reads the cause for the status bit (1…n), specified by the Instance ID, turning OFF. |                                                                  |                                                                  |                                                                  | 0E 09 01…n 76 - 0 = No error 01: Configuration invalid 02: Overload detected 05: Output ON error 06: Undercurrent detected for muting lamp |                                                                  |

Table 64 - Setting Hold/Clear for Communications Errors (test output)

|                                                                    |                      |                                                                                                                                                                                                                         | Explicit Message Service Function Command (hex) Response (hex)   | Explicit Message Service Function Command (hex) Response (hex)   | Explicit Message Service Function Command (hex) Response (hex)   | Explicit Message Service Function Command (hex) Response (hex)   | Explicit Message Service Function Command (hex) Response (hex)   |
|--------------------------------------------------------------------|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
|                                                                    |                      |                                                                                                                                                                                                                         | Service Code                                                     | Class ID                                                         | Instance ID Attribute ID Data                                    | Size                                                             |                                                                  |
| Setting for output state (hold or clear) after communication error | Get attribute single | Reads whether hold or clear is set as the output state after a communication error for a test output specified by the instance ID. The setting can be read for a specified number of points.                            |                                                                  |                                                                  | OE 09 01…08 05 – 1 byte                                          |                                                                  | 00: Clear 01: Hold                                               |
| Setting for output state (hold or clear) after communication error | Set attribute single | Sets whether hold or clear as the output status after a communication error for an output specified by the instance ID. Sets whether a test output must hold its state or clear (turn off) after a communication error. |                                                                  |                                                                  | 10 09 01…08 05 1 byte                                            | 00: Clear 01: Hold                                               |                                                                  |

## Calculated Values

## Safety Data

This appendix lists calculated values for probability of failure on demand (PFD), probability of failure per hour (PFH), and mean time to failure (MTTF). PFD and PFH calculations comply with IEC 61508, edition 2, 2010.

Calculated values of probability of failure on demand and probability of failure per hour appear in Table 65. These values must be calculated for the devices within the system to comply with the SIL level required for application.

You are responsible for following the requirements of ISO 13849-1:2008 to assess performance levels in your safety system.

Functionally test every I/O module by individually toggling each input point and verify that the controller detects it within the proof test interval.

Additionally, individually toggle each output point with the controller and verify that the output point changes state.

For more information, see the appropriate GuardLogix® Safety Reference Manual, which is listed in the Additional Resources on page 10 .

<!-- image -->

Figure 24 - PFD vs. Proof Test Interval 1791ES-IB8XOBV4 Single Channel Inputs

<!-- image -->

Figure 25 - PFD vs. Proof Test Interval 1791ES-IB8XOBV4 Dual Channel Inputs

<!-- image -->

Figure 26 - PFD vs. Proof Test Interval 1791ES-IB8XOBV4 Dual Channel Outputs

<!-- image -->

Figure 27 - PFD vs. Proof Test Interval 1791ES-IB16 Single Channel Inputs

<!-- image -->

Figure 28 - PFD vs. Proof Test Interval 1791ES-IB16 Dual Channel Inputs

<!-- image -->

Figure 29 - PFD vs. Proof Test Interval 1732ES-IB12XOBV2, 1732ES-IB12XOB4, 1732ESIB8XOBV4, 1732ES-IB8XOB8, 1732ES-IB16 - Single Channel Inputs

<!-- image -->

Figure 30 - PFD vs. Proof Test Interval 1732ES-IB12XOBV2, 1732ES-IB12XOB4, 1732ESIB8XOBV4, 1732ES-IB8XOB8, 1732ES-IB16 - Dual Channel Inputs

<!-- image -->

Figure 31 - PFD vs. Proof Test Interval 1732ES-IB12XOBV2, 1732ES-IB8XOBV4 - Dual Channel Outputs

<!-- image -->

Figure 32 - PFD vs. Proof Test Interval 1732ES-IB12XOB4, 1732ES-IB8XOB8 - Single Channel Outputs (1)

<!-- image -->

Figure 33 - PFD vs. Proof Test Interval 1732ES-IB12XOB4, 1732ES-IB8XOB8 - Dual Channel Output

<!-- image -->

Table 65 - Calculated Values for Probability of Failure on Demand (PFD), Probability of Failure per Hour (PFH), and Mean Time To Failure (MTTF)

| Cat. No. Proof Test Interval          | PFD PFH                  | (1/hour)                 | Spurious Trip Rate (3) (STR) (3)                                          | MTTF MTTFSpurious (4) (years) p (years)   |
|---------------------------------------|--------------------------|--------------------------|------------------------------------------|---|
| 1791ES-IB8XOBV4 Single Channel Inputs | PFD PFH                  | (1/hour)                 | 1 8760 2.81E-05 6.41E-09 5.612E-06 20.33 | MTTF MTTFSpurious (4) (years) p (years)   |
| 1791ES-IB8XOBV4 Single Channel Inputs | 2 17520 5.61E-05         |                          |                                          |   |
| 1791ES-IB8XOBV4 Single Channel Inputs | 5 43800 1.40E-04         |                          |                                          |   |
| 1791ES-IB8XOBV4 Single Channel Inputs | 10 87600 2.81E-04        |                          |                                          |   |
| 1791ES-IB8XOBV4 Single Channel Inputs | 20 175200 5.61E-04       |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Inputs   | 1 8760 1.12E-06 2.63E-10 |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Inputs   | 2 17520 2.25E-06         |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Inputs   | 5 43800 5.64E-06         |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Inputs   | 10 87600 1.13E-05        |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Inputs   | 20 175200 2.27E-05       |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Outputs  | 1 8760 1.38E-06 3.38E-10 |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Outputs  | 2 17520 2.76E-06         |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Outputs  | 5 43800 6.95E-06         |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Outputs  | 10 87600 1.41E-05        |                          |                                          |   |
| 1791ES-IB8XOBV4 Dual Channel Outputs  | 20 175200 2.89E-05       |                          |                                          |   |
| 1791ES-IB16 Single Channel Inputs     |                          |                          | 1 8760 2.80E-05 6.40E-09 3.309E-06 34.48 |   |
| 1791ES-IB16 Single Channel Inputs     | 2 17520 5.60E-05         |                          |                                          |   |
| 1791ES-IB16 Single Channel Inputs     | 5 43800 1.40E-04         |                          |                                          |   |
| 1791ES-IB16 Single Channel Inputs     | 10 87600 2.80E-04        |                          |                                          |   |
| 1791ES-IB16 Single Channel Inputs     | 20 175200 5.60E-04       |                          |                                          |   |
| 1791ES-IB16 Dual Channel Inputs       |                          | 1 8760 1.10E-06 2.60E-10 |                                          |   |
| 1791ES-IB16 Dual Channel Inputs       | 2 17520 2.20E-06         |                          |                                          |   |
| 1791ES-IB16 Dual Channel Inputs       | 5 43800 5.50E-06         |                          |                                          |   |
| 1791ES-IB16 Dual Channel Inputs       | 10 87600 1.10E-05        |                          |                                          |   |
| 1791ES-IB16 Dual Channel Inputs       | 20 175200 2.20E-05       |                          |                                          |   |
| 1732ES-IB12XOBV2                      |                          |                          | 1 8760 2.32E-06 5.38E-10 6.791E-06 16.81 |   |
| 1732ES-IB12XOBV2                      | 2 17520 4.63E-06         |                          |                                          |   |
| 1732ES-IB12XOBV2                      | 5 43800 1.16E-05         |                          |                                          |   |
| 1732ES-IB12XOBV2                      | 10 87600 2.33E-05        |                          |                                          |   |
| 1732ES-IB12XOBV2                      | 20 175200 4.69E-05       |                          |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Inputs  |                          | 1 8760 5.51E-07 1.35E-10 |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Inputs  | 2 17520 1.11E-06         |                          |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Inputs  | 5 43800 2.78E-06         |                          |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Inputs  | 10 87600 5.64E-06        |                          |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Inputs  | 20 175200 1.16E-05       |                          |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Outputs | 1 8760 5.68E-07 1.43E-10 |                          |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Outputs | 2 17520 1.14E-06         |                          |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Outputs | 5 43800 2.87E-06         |                          |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Outputs | 10 87600 5.81E-06        |                          |                                          |   |
| 1732ES-IB12XOBV2 Dual Channel Outputs | 20 175200 1.19E-05       |                          |                                          |   |

| Cat. No. Proof Test Interval              | PFD PFH                                  | (1/hour)                 | Spurious Trip Rate (3) (STR) (3)                                          | MTTF MTTFSpurious (4) (years) p (years)   |
|-------------------------------------------|------------------------------------------|--------------------------|------------------------------------------|---|
| Cat. No. Proof Test Interval              | PFD PFH                                  | (1/hour)                 | Spurious Trip Rate (3) (STR) (3)                                          | MTTF MTTFSpurious (4) (years) p (years)   |
| 1732ES-IB12XOB4 Single Channel Inputs     | 2 17520 4.63E-06                         |                          | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Single Channel Inputs     | 5 43800 1.16E-05                         |                          | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Single Channel Inputs     | 10 87600 2.33E-05                        |                          | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Single Channel Inputs     | 20 175200 4.69E-05                       |                          | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Inputs       | 1 8760 5.51E-07 1.35E-10                 |                          | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Inputs       | 2 17520 1.11E-06                         |                          | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Inputs       | 5 43800 2.78E-06                         |                          | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Inputs       | 10 87600 5.64E-06                        |                          | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Inputs       | 20 175200 1.16E-05                       |                          | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4(1) Single Channel Outputs |                                          | 1 8760 2.95E-05 6.75E-09 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4(1) Single Channel Outputs | 2 17520 5.91E-05                         | 1 8760 2.95E-05 6.75E-09 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4(1) Single Channel Outputs | 5 43800 1.48E-04                         | 1 8760 2.95E-05 6.75E-09 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4(1) Single Channel Outputs | 10 87600 2.95E-04                        | 1 8760 2.95E-05 6.75E-09 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4(1) Single Channel Outputs | 20 175200 5.91E-04                       | 1 8760 2.95E-05 6.75E-09 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Outputs      |                                          | 1 8760 5.62E-07 1.38E-10 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Outputs      | 2 17520 1.13E-06                         | 1 8760 5.62E-07 1.38E-10 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Outputs      | 5 43800 2.84E-06                         | 1 8760 5.62E-07 1.38E-10 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Outputs      | 10 87600 5.75E-06                        | 1 8760 5.62E-07 1.38E-10 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB12XOB4 Dual Channel Outputs      | 20 175200 1.18E-05                       | 1 8760 5.62E-07 1.38E-10 | 1 8760 2.32E-06 5.38E-10 6.670E-06 17.12 |   |
| 1732ES-IB8XOBV4 Single Channel Inputs     | 1 8760 2.32E-06 5.38E-10 6.896E-06 16.55 |                          |                                          |   |
| 1732ES-IB8XOBV4 Single Channel Inputs     | 2 17520 4.63E-06                         |                          |                                          |   |
| 1732ES-IB8XOBV4 Single Channel Inputs     | 5 43800 1.16E-05                         |                          |                                          |   |
| 1732ES-IB8XOBV4 Single Channel Inputs     | 10 87600 2.33E-05                        |                          |                                          |   |
| 1732ES-IB8XOBV4 Single Channel Inputs     | 20 175200 4.69E-05                       |                          |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Inputs       |                                          | 1 8760 5.51E-07 1.35E-10 |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Inputs       | 2 17520 1.11E-06                         | 1 8760 5.51E-07 1.35E-10 |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Inputs       | 5 43800 2.78E-06                         | 1 8760 5.51E-07 1.35E-10 |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Inputs       | 10 87600 5.64E-06                        | 1 8760 5.51E-07 1.35E-10 |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Inputs       | 20 175200 1.16E-05                       | 1 8760 5.51E-07 1.35E-10 |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Outputs      | 1 8760 5.68E-07 1.43E-10                 |                          |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Outputs      | 2 17520 1.14E-06                         |                          |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Outputs      | 5 43800 2.87E-06                         |                          |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Outputs      | 10 87600 5.81E-06                        |                          |                                          |   |
| 1732ES-IB8XOBV4 Dual Channel Outputs      | 20 175200 1.19E-05                       |                          |                                          |   |

| Cat. No. Proof Test Interval (Mission Time (2) )   | PFD PFH                                  | (1/hour)   | Spurious Trip Rate (3) (3)       | MTTF MTTFSpurious (4) (years) p (years)   |
|----------------------------------------------------|------------------------------------------|------------|-------|---|
|                                                    |                                          |            | (STR) |   |
| 1732ES-IB8XOB8 Single Channel Inputs               | 1 8760 2.32E-06 5.38E-10 6.813E-06 16.75 |            |       |   |
| 1732ES-IB8XOB8 Single Channel Inputs               | 2 17520 4.63E-06                         |            |       |   |
| 1732ES-IB8XOB8 Single Channel Inputs               | 5 43800 1.16E-05                         |            |       |   |
| 1732ES-IB8XOB8 Single Channel Inputs               | 10 87600 2.33E-05                        |            |       |   |
| 1732ES-IB8XOB8 Single Channel Inputs               | 20 175200 4.69E-05                       |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Inputs                 | 1 8760 5.51E-07 1.35E-10                 |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Inputs                 | 2 17520 1.11E-06                         |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Inputs                 | 5 43800 2.78E-06                         |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Inputs                 | 10 87600 5.64E-06                        |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Inputs                 | 20 175200 1.16E-05                       |            |       |   |
| 1732ES-IB8XOB8(1) Single Channel Outputs           | 1 8760 2.95E-05 6.75E-09                 |            |       |   |
| 1732ES-IB8XOB8(1) Single Channel Outputs           | 2 17520 5.91E-05                         |            |       |   |
| 1732ES-IB8XOB8(1) Single Channel Outputs           | 5 43800 1.48E-04                         |            |       |   |
| 1732ES-IB8XOB8(1) Single Channel Outputs           | 10 87600 2.95E-04                        |            |       |   |
| 1732ES-IB8XOB8(1) Single Channel Outputs           | 20 175200 5.91E-04                       |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Outputs                | 1 8760 5.62E-07 1.38E-10                 |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Outputs                | 2 17520 1.13E-06                         |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Outputs                | 5 43800 2.84E-06                         |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Outputs                | 10 87600 5.75E-06                        |            |       |   |
| 1732ES-IB8XOB8 Dual Channel Outputs                | 20 175200 1.18E-05                       |            |       |   |
| 1732ES-IB16 Single Channel Inputs                  | 1 8760 2.32E-06 5.38E-10 6.526E-06 17.49 |            |       |   |
| 1732ES-IB16 Single Channel Inputs                  | 2 17520 4.63E-06                         |            |       |   |
| 1732ES-IB16 Single Channel Inputs                  | 5 43800 1.16E-05                         |            |       |   |
| 1732ES-IB16 Single Channel Inputs                  | 10 87600 2.33E-05                        |            |       |   |
| 1732ES-IB16 Single Channel Inputs                  | 20 175200 4.69E-05                       |            |       |   |
| 1732ES-IB16 Dual Channel Inputs                    | 1 8760 5.51E-07 1.35E-10                 |            |       |   |
| 1732ES-IB16 Dual Channel Inputs                    | 2 17520 1.11E-06                         |            |       |   |
| 1732ES-IB16 Dual Channel Inputs                    | 5 43800 2.78E-06                         |            |       |   |
| 1732ES-IB16 Dual Channel Inputs                    | 10 87600 5.64E-06                        |            |       |   |
| 1732ES-IB16 Dual Channel Inputs                    | 20 175200 1.16E-05                       |            |       |   |

(3) Calculated based on ISA TR-84 method.

(4) Mean Time to Failure (Spurious).

Table 66 - Failure Rate Data (failures per hour) (1)

| Cat. No. I/O Configuration λS  λDD                                     | λDU   |
|------------------------------------------------------------------------|-------|
| 1791ES-OB8XOBV4 Single Channel Inputs 7.8343E-07 7.5766E-07 5.5089E-09 |       |
| Dual Channel Inputs 1.1786E-06 1.1552E-06 2.6384E-10                   |       |
| Dual Channel Outputs 1.7205E-06 1.7009E-06 3.0765E-10                  |       |
| 1791ES-IB16 Single Channel Inputs 7.8024E-07 7.5356E-07 5.5087E-09     |       |
| Dual Channel Inputs 1.1760E-06 1.1519E-06 2.5974E-10                   |       |

Table 66 - Failure Rate Data (failures per hour) (1)

| Cat. No. I/O Configuration λS  λDU                                      | λDD           |
|-------------------------------------------------------------------------|---------------|
| 1732ES-IB12XOBV2 Single Channel Inputs 2.7190E-07 2.7190E-07 5.8410E-10 |               |
| Dual Channel Inputs 3.0730E-07 3.0730E-07 2.0350E-10                    |               |
| Dual Channel Outputs 3.7360E-07 3.7360E-07 2.0820E-10                   |               |
| 1732ES-IB12XOB4 Single Channel Inputs 2.7190E-07 2.7190E-07 5.8410E-10  |               |
| Dual Channel Inputs 3.0730E-07 3.0730E-07 2.0350E-10                    |               |
| Single Channel Outputs (2)  2.8910E-07(2)  6.4630E-09(2)                | 2.8910E-07(2) |
| Dual Channel Outputs 3.5140E-07 3.5140E-07 2.0660E-10                   |               |
| 1732ES-IB8XOBV4 Single Channel Inputs 2.7190E-07 2.7190E-07 5.8410E-10  |               |
| Dual Channel Inputs 3.0730E-07 3.0730E-07 2.0350E-10                    |               |
| Dual Channel Outputs 3.7360E-07 3.7360E-07 2.0820E-10                   |               |
| 1732ES-IB8XOB8 Single Channel Inputs 2.7190E-07 2.7190E-07 5.8410E-10   |               |
| Dual Channel Inputs 3.0730E-07 3.0730E-07 2.0350E-10                    |               |
| Single Channel Outputs (2)  2.8910E-07(2)  6.4630E-09(2)                | 2.8910E-07(2) |
| Dual Channel Outputs 3.5140E-07 3.5140E-07 2.0660E-10                   |               |
| 1732ES-IB16 Single Channel Inputs 2.7190E-07 2.7190E-07 5.8410E-10      |               |
| Dual Channel Inputs 3.0730E-07 3.0730E-07 2.0350E-10                    |               |

## Parameter Groups

## Table 67 - General Parameters

|                                                                     | Parameter Name Value Description Default                              |
|---------------------------------------------------------------------|-----------------------------------------------------------------------|
| Safety Output Error Latch Time 0…65,530 ms (in increments of 10 ms) | Safety output errors are latched for this time. 1000 ms               |
| Safety Input Error Latch Time 0…65,530 ms (in increments of 10 ms)  | Safety input or test output errors are latched for this time. 1000 ms |

## Table 68 - Safety Input Parameters

| Parameter Name Value Description                                 |                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Input Point Operation Type Single Channel Use as single channel. |                                                                                                                                                                                                                                                                |
| Input Point Operation Type Single Channel Use as single channel. | Dual-channel Equivalent Use as dual-channel. Normal when both channels are ON or OFF.                                                                                                                                                                          |
| Input Point Operation Type Single Channel Use as single channel. | Dual-channel Complementary Use as dual-channel. Normal when one channel is ON and the other channel is OFF.                                                                                                                                                    |
|                                                                  | Input Point Mode Not Used External input device is not connected.                                                                                                                                                                                              |
|                                                                  | Safety Test Pulse Use with a contact output device and in combination with a test output. By using this setting, short circuits between input signal lines and the power supply (positive side) and short circuits between input signal lines can be detected. |
|                                                                  | Safety A solid-state output safety sensor is connected.                                                                                                                                                                                                        |
|                                                                  | Standard A standard device, such as a reset switch, is connected.                                                                                                                                                                                              |
|                                                                  | Safety Input Test Source Not Used The test output that is used with the input. n is dependent on the module catalog number.                                                                                                                                    |
| Input Delay Time Off -> On 0…126 ms (in increments of 6 ms)      | Filter time for OFF to ON transition                                                                                                                                                                                                                           |
| Input Delay Time On -> Off 0…126 ms (in increments of 6 ms)      | Filter time for ON to OFF transition                                                                                                                                                                                                                           |

## IMPORTANT

When configuring a test output for Pulse Test mode, verify that the corresponding safety input is configured for safety pulse test.

<!-- image -->

## Configuration Reference Information

The modules have these parameter groups: general parameters, safety input, test output, safety output.

See Table 67…Table 70 for the settings in each parameter group. All parameters are set by using the Studio 5000 Logix Designer® application.

## Table 69 - Test Output Parameters

|                                                                                                                                                                                                             | Parameter Name Value Description Default                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                                                                                             | Test Output Mode Not Used An external device is not connected. Not Used                                                                          |
|                                                                                                                                                                                                             | Standard The output is connected to a standard device.                                                                                           |
|                                                                                                                                                                                                             | Pulse Test A contact output device is connected. Use in combination with a safety input.                                                         |
|                                                                                                                                                                                                             | Power Supply The power supply of a Safety Sensor is connected. The voltage supplied to I/O power (V, G) is output from the test output terminal. |
| Muting Lamp Output 1791ES-IB8XOBV4, 1732ES-IB8XOBV4, 1732ES-IB8XOB8 modules = T3 and T7 1791ES-IB16, 1732ES-IB16 modules = T3, T7, T11, and T15 1732ES-IB12XOBV2, 1732ES-IB12XOB4 modules = T3, T7, and T11 | An indicator is connected and turned ON to detect broken lines in an external indicator.                                                         |

## Table 70 - Safety Output Parameters

| Parameter Name Value Description Default                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Output Point Mode Not Used An external output device is not connected. Not Used                                                                                                           |
| Safety When the output is ON, the test pulse is not output (remains ON).                                                                                                                  |
| Safety Pulse Test By using this function, short circuits between output signal lines and the power supply (positive side) and short circuits between output signal lines can be detected. |
| Output Point Operation Type Single Channel (1)  Use as single channel. Dual-channel                                                                                                       |
| Dual-channel Use as dual-channel. When both channels are normal, outputs can be turned ON.                                                                                                |

## Technical Specifications

## Specifications

| Topic Page                       |
|----------------------------------|
| Technical Specifications 161     |
| Environmental Specifications 166 |
| Certifications 168               |
| Europe 168                       |
| EC Directives 169                |

This section provides technical specifications for the modules.

## 1791ES Modules

For 1791ES modules, see Table 71 and Table 72 .

| Attribute Value                                                                                            |               |
|------------------------------------------------------------------------------------------------------------|---------------|
| Safety input                                                                                               |               |
| Inputs type Current sinking                                                                                |               |
| Voltage, on-state input, min 11V DC                                                                        |               |
| Current, on-state input, min 3.3 mA                                                                        |               |
| Voltage, off-state input, max 5V DC                                                                        |               |
| Current, off-state, max 1.3 mA                                                                             |               |
| IEC 61131-2 (input type) Type 3                                                                            |               |
| Pulse test output                                                                                          |               |
| Output type Current sourcing                                                                               |               |
| Pulse test output current 0.7 A per output                                                                 |               |
| Residual voltage, max 1.2V                                                                                 |               |
| Output leakage current, max 0.1 mA                                                                         |               |
| Short circuit protection Yes                                                                               |               |
| Current, max 25 mA – current, max (to avoid fault when used as a muted lamp output)                        |               |
| Current, min 5 mA – current, min (at which fault indication is generated when used as a muted lamp output) |               |
| Safety output                                                                                              | Safety output |

Table 71 - 1791ES-IB16 and 1791ES-IB8XOBV4 Modules – Technical Specifications

<!-- image -->

Table 71 - 1791ES-IB16 and 1791ES-IB8XOBV4 Modules – Technical Specifications (Continued)

| Attribute Value                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Output types Current sourcing/current sinking – bipolar pair                                                                                                                                                                                                                                                                                                               |
| Output current rating 2 A max per point 8 A total module at 40 °C (104 °F) (see temperature versus current derating) 6 A total module at 60 °C (140 °F)                                                                                                                                                                                                                    |
| Voltage and current ratings IN PWR (No Load): 19.2-28.8 Vdc, 190 mA @ 24 Vdc typ. No load Inputs: 11-30Vdc, 3.5mA Test Outputs: 19.2-28.8Vdc, 700mA Sum of P and M Currents: 8 A at 40 °C (104 °F), 6 A at 60 °C (140 °F) P & M Outputs: 19.2-28.8Vdc, 2A; 2.5A Inrush. Max. Current (Input plus Output): 8A@40C, 6A@60C. Operating Temperature: -20 °C to +60 °C (140 °F) |
| On-state voltage drop +/- 0.6V                                                                                                                                                                                                                                                                                                                                             |
| Leakage current +/- 1.0 mA (1)                                                                                                                                                                                                                                                                                                                                             |
| Internal resistance from P to M terminal 3.25 kΩ                                                                                                                                                                                                                                                                                                                           |
| Short circuit detection Yes (short high and low and cross-circuit fault detection)                                                                                                                                                                                                                                                                                         |
| Short circuit protection Electronic                                                                                                                                                                                                                                                                                                                                        |
| Aggregate current of module 8 A at 40 °C (104 °F), 6 A at 60 °C (140 °F) (see product temperature versus current derating)                                                                                                                                                                                                                                                 |
| Pilot duty rating 2.5 A inrush for 1791ES-IB8XOBV4 module                                                                                                                                                                                                                                                                                                                  |
| Number of outputs 4, dual-channel                                                                                                                                                                                                                                                                                                                                          |

## Table 72 - 1791ES-IB16 and 1791ES-IB8XOBV4 Modules – General

| Attribute Value                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| North American temp code 1791ES-IB8XOBV4: T4A 1791ES-IB16: T5                                                                                                                                                                                                                                |
| Enclosure type rating Meets IP20                                                                                                                                                                                                                                                             |
| Communication current consumption 250 mA at 24V DC                                                                                                                                                                                                                                           |
| Operating voltage range 19.2…28.8V DC (24V DC, -20…20%)                                                                                                                                                                                                                                      |
| Isolation voltage 1791ES-IB16 - 50V (continuous), basic insulation - type tested at 800V DC for 60 s between input channels and network 1791ES-IB8XOBV4 - 50V (continuous), basic insulation - type tested at 800V DC for 60 s between input and output channels and between I/O and network |

Table 72 - 1791ES-IB16 and 1791ES-IB8XOBV4 Modules – General (Continued)

<!-- image -->

| Attribute Value                             |                                                                                                                                                                            |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Product temperature versus current derating | 8 A 7 A 6 A -20 °C (-4 °F) Product Temperature Versus Current Derating (combined current from both input and output supplies) 40 °C 50 °C 60 °C (104 °F) (122 °F) (140 °F) |
| Wiring category (1)                         | 2 - on signal ports, 2 - on power ports, 2 -on communication ports                                                                                                         |
|                                             | Wire size Power and I/O wiring: 0.34…1.5 mm2 (22…16 AWG) solid or stranded copper wire rated at 75 °C (167 °F) or greater, 1.2 mm (3/64 in.) insulation max                |
|                                             | Weight, approx 600 g (1.32 lb)                                                                                                                                             |
|                                             | Dimensions (HxWxD), approx. 80 x 196 x 77 mm (3.2 x 7.7 x 3 in.) with terminal block                                                                                       |
|                                             | 77 x 196 x 62 mm (3 x 7.7 x 2.5 in.) without terminal block                                                                                                                |

## 1732ES Modules

For 1732ES modules, see Table 73 and Table 74 .

Table 73 - 1732ES-IB16, 1732ES-IB8XOB8, 1732ES-IB8XOBV4, 1732ES-IB12XOB4, and 1732ES-IB12XOBV2 Modules – Technical Specifications

| Attribute Value                                                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs type Current sinking                                                                                                                                                                                                                                                   |
| Voltage, on-state input 11…30V DC                                                                                                                                                                                                                                             |
| Current, on-state input 3.5 mA                                                                                                                                                                                                                                                |
| Voltage, off-state input, max 5V DC                                                                                                                                                                                                                                           |
| Current, off-state, max 1 mA                                                                                                                                                                                                                                                  |
| IEC 61131-2 (input type) Type 3                                                                                                                                                                                                                                               |
| Output type Current sourcing                                                                                                                                                                                                                                                  |
| Pulse test output current (each) (all 1732ES modules except 1732ES-IB16) 0.7 A max per point at 40 °C (104 °F) 0.3 A max per point at 55 °C (131 °F) See Product temperature versus pulse test output current derating (All 1732ES modules except 1732ES-IB16) on  page 165 . |
| Pulse test output current (1732ES-IB16 only) 0.7 A max per point 8.4 A max per module                                                                                                                                                                                         |
| Residual voltage, max 1.2V                                                                                                                                                                                                                                                    |

Table 73 - 1732ES-IB16, 1732ES-IB8XOB8, 1732ES-IB8XOBV4, 1732ES-IB12XOB4, and 1732ES-IB12XOBV2 Modules – Technical Specifications

| Attribute Value                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Output leakage current, max 0.1 mA                                                                                                                                                                                                              |
| Short circuit protection Yes                                                                                                                                                                                                                    |
| Current, max 25 mA – current, max (to avoid fault when used as a muted lamp output)                                                                                                                                                             |
| Current, min 5 mA – current, min (at which fault indication is generated when used as a muted lamp output)                                                                                                                                      |
| Output types 1732ES-IB12XOBV2, 1732ES-IB8XOBV4: Current sourcing/current sinking bipolar pair 1732ES-IB12XOB4, 1732ES-IB8XOB8: Current sourcing                                                                                                 |
| Output current rating (each) 1732ES-IB12XOBV2, 1732ES-IB8XOBV4: 2 A max per point, bipolar outputs 1732ES-IB12XOB4, 1732ES-IB8XOB8: 1 A max per point, sourcing outputs                                                                         |
| On-state voltage drop, max 1.15V                                                                                                                                                                                                                |
| Leakage current 1732ES-IB12XOB4, 1732ES-IB8XOB8: +/-0.1 mA 1732ES-IB12XOBV2, 1732ES-IB8XOBV4: +/-1.0 mA (1)                                                                                                                                     |
| Internal resistance from sourcing to sinking terminal 1732ES-IB12XOBV2, 1732ES-IB8XOBV4: 3.25 kΩ 1732ES-IB12XOB4, 1732ES-IB8XOB8: N/A                                                                                                           |
| Short circuit detection Yes (short high and low and cross-circuit fault detection)                                                                                                                                                              |
| Short circuit protection Electronic                                                                                                                                                                                                             |
| Pilot duty rating DC13, 2.5 A inrush                                                                                                                                                                                                            |
| Number of outputs Safety outputs 1732ES-IB12XOB4 module, 4 sourcing outputs 1732ES-IB12XOBV2 module, 4 bipolar outputs, (2 pairs) 1732ES-IB8XOB8 module, 8 sourcing outputs 1732ES-IB8XOBV4 module, 8 bipolar outputs (4 pairs)                 |
| Output power current rating (pins 1, 3, and 5 of each output signal I/O connector) 2 A max per point at 40 °C (104 °F) 1 A max per point at 55 °C (131 °F) See Product temperature versus output power current derating (per pin) on page 165 . |

Table 74 - 1732ES-IB16, 1732ES-IB8XOB8, 1732ES-IB8XOBV4, 1732ES-IB12XOB4, and 1732ES-IB12XOBV2 Modules – General

| Attribute Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enclosure type rating Meets IP65/IP67 (when marked)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Product current consumption (not including Test output or Safety output load current) 1732ES-IB12XOBV2: • In power (no load): 19.2…28.8V DC, 175 mA at 24V DC • Out power (no load): 19.2…28.8V DC, 65 mA at 24V DC 1732ES-IB12XOB4: • In power (no load): 19.2…28.8V DC, 175 mA at 24V DC • Out power (no load): 19.2…28.8V DC, 45 mA at 24V DC 1732ES-IB8XOB8: • In power (no load): 19.2…28.8V DC, 165 mA at 24V DC • Out power (no load): 19.2…28.8V DC, 65 mA at 24V DC 1732ES-IB8XOBV4: • In power (no load): 19.2…28.8V DC, 165 mA at 24V DC • Out power (no load): 19.2…28.8V DC, 110 mA at 24V DC 1732ES-IB16: In power (no load): 19.2…28.8V DC, 190 mA at 24V DC |
| Operating voltage range 19.2…28.8V DC (24V DC, -20…20%)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Module power connector rating 10 A max per pin                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

Table 74 - 1732ES-IB16, 1732ES-IB8XOB8, 1732ES-IB8XOBV4, 1732ES-IB12XOB4, and 1732ES-IB12XOBV2 Modules – General (Continued)

<!-- image -->

| Attribute Value                                                                                       |                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                       | Isolation voltage 50V (continuous), Basic Type, Input Power and I/O to Ethernet, Input Power and I/O to Output Power and IO, and Output Power and IO to Ethernet Tested at 707V DC for 60s |
| Product temperature versus pulse test output current derating (All 1732ES modules except 1732ES-IB16) | 0.7 A 0.3 A Product Temperature Versus Pulse Test Output Current Derating -20 °C (-4 °F) 40 °C (104 °F) 55 °C (131 °F)                                                                     |
| Product temperature versus output power current derating (per pin)                                    | 2.0 A 1.0 A Product Temperature Versus Output Power Current Derating (per pin) -20 °C (-4 °F) 40 °C (104 °F) 55 °C (131 °F)                                                                |
| Wiring category (1)                                                                                   | 2 - on signal ports 2 - on power ports 2 - on communication ports                                                                                                                          |
|                                                                                                       | Weight, approx 786 g (1.73 lb)                                                                                                                                                             |
|                                                                                                       | Dimensions (HxWxD), approx 70 x 259 x 69 mm (2.8 x 10.2 x 2.7 in.) without cables                                                                                                          |

## Environmental Specifications This section provides environmental specifications for the modules.

- For 1791ES modules, see Table 75 on page 166 .
- For 1732ES modules, see Table 76 on page 167 .

Table 75 - 1791ES-IB16 and 1791ES-IB8XOBV4 Modules – Environmental Specifications

| Attribute Value                                                                                                                                                                                             |                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Nb, Operating Thermal Shock)                                              | -20…+60 °C (-4…+140 °F)                                                                                                                                                                               |
| Temperature, nonoperating IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock) | -40…+85 °C (-40…+185 °F)                                                                                                                                                                              |
| Relative humidity IEC 60068-2-30 (Test Db, Unpackaged Nonoperating Damp Heat)                                                                                                                               | 5…95% noncondensing                                                                                                                                                                                   |
| Vibration IEC 60068-2-6 (Test Fc, Operating)                                                                                                                                                                | 5 g at 10…500 Hz                                                                                                                                                                                      |
| Shock, operating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                                 | 30 g                                                                                                                                                                                                  |
| Shock, nonoperating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                              | 50 g                                                                                                                                                                                                  |
|                                                                                                                                                                                                             | Emissions IEC 61000-6-4                                                                                                                                                                               |
| ESD immunity IEC 61000-4-2                                                                                                                                                                                  | 8 kV contact discharges 10 kV air discharges                                                                                                                                                          |
| Radiated RF immunity IEC 61000-4-3                                                                                                                                                                          | 10V/m with 1 kHz sine-wave 80% AM from 80…2000 MHz 10V/m with 200 Hz 50% Pulse 100% AM at 900 MHz 10V/m with 200 Hz 50% Pulse 100% AM at 1890 MHz 3V/m with 1 kHz sine-wave 80% AM from 2000…2700 MHz |
| Conducted RF immunity IEC 61000-4-6                                                                                                                                                                         | 10V rms with 1 kHz sine-wave 80% AM from 150 kHz…80 MHz                                                                                                                                               |
| EFT/B immunity IEC 61000-4-4                                                                                                                                                                                | ±4 kV at 5 kHz on power ports ±3 kV at 5 kHz on signal ports ±2 kV at 5 kHz on communication ports                                                                                                    |
| Surge transient immunity IEC 61000-4-5                                                                                                                                                                      | ±1 kV line-line (DM) and ±2 kV line-earth (CM) on power ports ±1 kV line-line (DM) and ±2 kV line-earth (CM) on signal ports ±2 kV line-earth (CM) on communication ports                             |
| Reaction time                                                                                                                                                                                               |                                                                                                                                                                                                       |
|                                                                                                                                                                                                             | Input reaction time, max 16.2 ms + set values of ON/OFF delays                                                                                                                                        |
|                                                                                                                                                                                                             | Output reaction time, max 6.2 ms + (20 ms) relay response time                                                                                                                                        |

Signal sequence

<!-- image -->

While safety outputs are in an on state, the signal sequence shown in the figure is output continuously for fault diagnosis. Confirm response time of device connected to safety outputs so the device does not malfunction due to off pulse.

Table 76 - 1732ES-IB16, 1732ES-IB8XOB8, 1732ES-IB8XOBV4, 1732ES-IB12XOB4, and 1732ES-IB12XOBV2 Modules – Environmental Specifications

| Attribute Value                                                                                                                                                                                             |                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Nb, Operating Thermal Shock)                                              | -20…+55 °C (-4…+131 °F) (All 1732ES modules except 1732ES-IB16 modules)                                                                                                                               |
| Temperature, operating IEC 60068-2-1 (Test Ad, Operating Cold), IEC 60068-2-2 (Test Bd, Operating Dry Heat), IEC 60068-2-14 (Test Nb, Operating Thermal Shock)                                              | -20…+60 °C (-4…+140 °F) (Only 1732ES-IB16 modules)                                                                                                                                                    |
| Temperature, nonoperating IEC 60068-2-1 (Test Ab, Unpackaged Nonoperating Cold), IEC 60068-2-2 (Test Bb, Unpackaged Nonoperating Dry Heat), IEC 60068-2-14 (Test Na, Unpackaged Nonoperating Thermal Shock) | -40…+85 °C (-40…+185 °F)                                                                                                                                                                              |
| Relative humidity IEC 60068-2-30 (Test Db, Unpackaged Nonoperating Damp Heat)                                                                                                                               | 5…95% noncondensing                                                                                                                                                                                   |
| Vibration IEC 60068-2-6 (Test Fc, Operating)                                                                                                                                                                | 5 g at 10…500 Hz                                                                                                                                                                                      |
| Shock, operating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                                 | 30 g                                                                                                                                                                                                  |
| Shock, nonoperating IEC 60068-2-27 (Test Ea, Unpackaged Shock)                                                                                                                                              | 50 g                                                                                                                                                                                                  |
|                                                                                                                                                                                                             | Emissions IEC 61000-6-4                                                                                                                                                                               |
| ESD immunity IEC 61000-4-2                                                                                                                                                                                  | 4 kV contact discharges 10 kV air discharges                                                                                                                                                          |
| Radiated RF immunity IEC 61000-4-3                                                                                                                                                                          | 10V/m with 1 kHz sine-wave 80% AM from 80…2000 MHz 10V/m with 200 Hz 50% Pulse 100% AM at 900 MHz 10V/m with 200 Hz 50% Pulse 100% AM at 1890 MHz 3V/m with 1 kHz sine-wave 80% AM from 2000…2700 MHz |
| Conducted RF immunity IEC 61000-4-6                                                                                                                                                                         | 10V rms with 1 kHz sine-wave 80% AM from 150 kHz…80 MHz                                                                                                                                               |
| EFT/B immunity IEC 61000-4-4                                                                                                                                                                                | ±2 kV at 5 kHz on power ports ±1 kV at 5 kHz on signal ports ±1 kV at 5 kHz on communication ports                                                                                                    |
| Surge transient immunity IEC 61000-4-5                                                                                                                                                                      | ±2 kV line-earth (CM) on power ports ±2 kV line-earth (CM) on signal ports ±2 kV line-earth (CM) on communication ports                                                                               |
| Reaction time                                                                                                                                                                                               |                                                                                                                                                                                                       |
|                                                                                                                                                                                                             | Input reaction time, max 16.2 ms + set values of ON/OFF delays                                                                                                                                        |
|                                                                                                                                                                                                             | Output reaction time, max 6.2 ms + (20 ms) relay response time                                                                                                                                        |

Signal sequence

<!-- image -->

While safety outputs are in an on state, the signal sequence shown in the figure is output continuously for fault diagnosis. Confirm response time of device connected to safety outputs so the device does not malfunction due to off pulse.

## Certifications

This section provides certification information for the 1791ES and 1732ES modules.

Table 77 - 1791ES and 1732ES Modules – Certifications

| Certification(1)  1732ES-IB16, 1732ES-IB8XOB8, 1732ES-IB8XOBV4, 1732ES-IB12XOBV2, 1732ES-IB12XOB4, 1791ES-IB16, 1791ES-IB8XOBV4                                                                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CE European Union 2004/108/EC EMC Directive, compliant with these norms: EN 61326-1; Meas./Control/Lab, Industrial Requirements EN 61000-6-2; Industrial Immunity EN 61000-6-4; Industrial Emissions EN 61010-2-201; Control Equipment Safety Requirements EN 61131-2; Programmable Controllers (Clause 8, Zone A & B) |
| EtherNet/IP ODVA conformance tested to CIP Safety on EtherNet/IP specifications                                                                                                                                                                                                                                        |
| KC Korean Registration of Broadcasting and Communications Equipment, compliant with Article 58-2 of Radio Waves Act, Clause 3                                                                                                                                                                                          |
| RCM, C-Tick Australian Radiocommunications Act, compliant with: EN 61000-6-4; Industrial Emissions                                                                                                                                                                                                                     |
| TUV Capable of Cat. 4/PL e according to EN ISO 13849-1 and SIL 3 according to (2) p EN 62061/IEC 61508(2)                                                                                                                                                                                                                                                                                                                        |
| c-UL-us UL Listed Industrial Control Equipment, certified for US and Canada. See UL File E65584. UL Listed for Class I, Division 2 Group A,B,C,D Hazardous Locations, certified for U.S. and Canada. See UL File E194810. (1791ES only)                                                                                |
| C-Tick Australian Radiocommunications Act                                                                                                                                                                                                                                                                              |

Guard I/O™ EtherNet/IP Safety Modules, publication 1791ES-UM001 .

## Europe

The type approval of TÜV-Rheinland addresses compliance to applicable requirements of the following directives and standards:

- EU legislation
- – Low-voltage Directive 73/23/EEC
- – EMC Directive 89/336/EEC
- European standards
- – EN 61508 (SIL1-3)
- – EN 61131-2
- – EN 60204-1
- – IEC 61000-6-2
- – IEC 61000-6-4
- – ISO 13849-1:2008

## EC Directives

## North America

In North America, the TÜV-Rheinland type approval includes Guard I/O compliance to the relevant standards and related information including the following:

- U.S. standards - ANSI RIA15.06, ANSI B11.19, NFPA 79
- The modules are UL-certified functionally safe and carry the NRGF label, when product is marked (only 1791ES modules).

## Japan

In Japan, type test requirements are provided in Article 44 of the Industrial Safety and Health Law. These requirements apply to complete systems and cannot be applied to a module by itself. Accordingly, to use the module in Japan as a safety device for press machine or shearing tool pursuant to Article 42 of the above-mentioned law, it is necessary to apply for testing of the entire system (only 1791ES modules).

These products conform to the EMC Directive and Low-voltage Directive. For additional information, see the relevant installation instructions.

## EMC Directive

Rockwell Automation devices that comply with EC directives also conform to the related EMC standards so that they can more easily be built into other devices or the overall machine. The actual products have been checked for conformity to EMC standards. Whether they conform to the standards in the system used by the customer, however, must be confirmed by the customer.

EMC-related performance of Rockwell Automation devices that comply with EC directives vary depending on the configuration, wiring, and other conditions of the equipment or control panel in which the Rockwell Automation devices are installed. The customer must, therefore, perform the final check to confirm that devices and the overall machine conform to EMC standards.

## Compliance with EC Directives

EtherNet/IP products that comply with EC directives must be installed as follows:

- All Type IP20 EtherNet/IP units must be installed within control panels.

- Use reinforced insulation or double insulation for the DC power supplies used for the communication power supply, internal- circuit power supply, and the I/O power supplies.
- EtherNet/IP products that comply with EC directives also conform to the Common Emission Standard (EN 50081-2). Radiated emission characteristics (10-m regulations) can vary depending on the configuration of the control panel used, other devices connected to the control panel, wiring, and other conditions. You must confirm that the overall machine or equipment complies with EC directives.

## Symbols

+24V DC power current input 56

output 57

## Numerics

1732ES-IB12XOB4 33

1732ES-IB12XOBV2 33

1732ES-IB16 33

1732ES-IB8XOB8 33

1732ES-IB8XOBV4 33

1791ES-IB16 33

1791ES-IB8XOBV4 33

A

architectures, safety 34

B

before you begin 27

C

CAT. 4, PLe 31 , 34

CE LVD compliance 33

CIP generic message instructions 101

CIP Safety 93

common terms 9

compliance with EC directive 169

configuration reference information 159

conformity codes 28

regulations 28

standards 28

controlling devices 26

CRTL 86

D

DC power supply according to

EN 50178 33

IED/EN 60950 33

UL 508 33

Device Level Ring 9

diagnostic status information 101

diagnostics 12

dialog

Safety 86

DIN rail 48

directives 168

discrepancy time 17

DLR

See Device Level Ring

door interlocking switches 26

dual-load bipolar outputs 73 , 74

E

electric shock prevention 45

Electronic Data Sheet 9

EMC Directives 169

emergency stop switch 26 , 67

EN 50081-2 170

EtherNet/IP cables recommended 59

EtherNet/IP safety network k 34

explicit messages 149

Explicit Messaging 101 , 102

explosion hazards 42

external power supply y 33

F

fatal errors 12

fault recovery 20 , 25

features

Guard I/O modules 32

firmware revision information

Guard I/O modules 28

forcibly-guided contacts 26

G

get point status information 101

glossary 9

Guard I/O modules features 32

firmware revision information 28

Guardmaster product 26

H

help button 75

I

I/O

configuration tree 77

connectors 32

module overview 31

status data 32

I/O assembly and reference data 140

I/O connector cables, recommended 62

I/O data 136

IEC 61508 31 , 34 , 151

IP rating for 1732ES modules 43

ISO 13849-1 31 , 34

2008 151

| J                                                             | probability of failure on demand  9                                            |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| Japan  169                                                    | probability of failure per hour  9 programming requirements  34                |
| L                                                             | R                                                                              |
| limit switches  26                                            | redundant channel safety devices  17 replacement stock  44 reset ownership  87 |
| M maximum current  56                                         | RPI  86                                                                        |
| mean time between failure  9 ,  151                           | RSLogix 5000 software                                                          |
| model types  32                                               | version  34                                                                    |
| module                                                        |                                                                                |
| 42                                                            | S                                                                              |
| cleaning  configuration  75 definition  80                    | safety administrator  category  30                                             |
| MTBF See mean time between failure. MTTF  151 muting lamp  21 | 30 integrity level  30 safety architectures                                    |
| mounting guidelines  45                                       |                                                                                |
|                                                               | 34 safety functions                                                            |
| output wiring  70                                             | safety input  13 ,  32 safety output  23 ,                                     |
|                                                               | 32 understanding operation                                                     |
| N                                                             | 11 safety network number  9 ,  79 ,  93 safety precautions  168                |
| NAT  80                                                       | safety state  11                                                               |
| See network address translation network (IP) address          | self-diagnostics  12 SIL CL 3  31 34                                           |
| setting  52                                                   | ,  SNN  79                                                                     |
| network address switches  75 network address translation      |                                                                                |
| 9 ,  32 ,  80                                                 | See safety network number. software versions  34                               |
| node address setting  52                                      | standards  168                                                                 |
| North America  169                                            | status bits                                                                    |
|                                                               | muting  21 ,                                                                   |
| O                                                             | 22 status data  12                                                             |
| ODVA  9 off-delay function                                    | status messages 1732ES modules  112 1791ES-IB16 modules                        |
| 20 on-delay function  20                                      | 107 1791ES-IB8XOBV4 modules                                                    |
| online help  75                                               | 102 12                                                                         |
| out-of-box condition                                          | status, combined                                                               |
| 44                                                            | Studio 5000 Logix Designer application                                         |
| outputs                                                       | version  34                                                                    |
| safety  32                                                    | Studio 5000 Logix Designer software version  34                                |
| test  32                                                      |                                                                                |
| P                                                             | T                                                                              |
| parameter groups  159                                         | tag values and states input data  85 85                                        |
| PFD  151 See probability of failure on demand. PFH  151       | output data  9                                                                 |
|                                                               | terminology  test outputs  21 ,  32                                            |
| See probability of failure per hour                           |                                                                                |
| point status information  101                                 | topology                                                                       |
| power pass through  55                                        | DLR  35                                                                        |
| precautions for use  30                                       | linear                                                                         |
| probability of failure                                        | star  34                                                                       |
|                                                               | 34                                                                             |
| on demand  151                                                |                                                                                |
| 151                                                           | transformer, according to IEC/EN 61558  33                                     |
| per hour                                                      |                                                                                |

## W

## wiring by application

dual-load bipolar outputs 73

dual-load sourcing outputs – only 1732ES-

IB12XOB4 module 74

emergency stop switch dual-channel inputs with manual reset 67

Guard I/O module with limit switch dualchannel inputs and a manual reset 72

limit switch dual-channel inputs and a manual reset 71

mode select switch 69

muting lamp output 70

two-hand monitor 68

## wiring examples 63

door monitor 65

emergency stop switch light curtain 66

65

reset switch 64

single-channel safety device 64

wiring guidelines 43 , 52

## wiring requirements

ISO 13849-1:2008 67 , 68 , 71 , 73 , 74

## Notes:

.

## Rockwell Automation Support

Use the following resources to access support information.

| Technical Support Center                         | Knowledgebase Articles, How-to Videos, FAQs, Chat, User Forums, and Product Notification Updates.                     | https://rockwellautomation.custhelp.com/                                  |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| Local Technical Support Phone Numbers            | Locate the phone number for your country.                                                                             | http://www.rockwellautomation.com/global/support/get-support-now.page     |
| Direct Dial Codes                                | Find the Direct Dial Code for your product. Use the code to route your call directly to a technical support engineer. | http://www.rockwellautomation.com/global/support/direct-dial.page         |
| Literature Library                               | Installation Instructions, Manuals, Brochures, and Technical Data.                                                    | http://www.rockwellautomation.com/global/literature-library/overview.page |
| Product Compatibility and Download Center (PCDC) | Get help determining how products interact, check features and capabilities, and find associated firmware.            | http://www.rockwellautomation.com/global/support/pcdc.page                |

## Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete the How Are We Doing? form at http://literature.rockwellautomation.com/idc/groups/literature/documents/du/ra-du002\_-en-e.pdf. f.

Rockwell Automation maintains current product environmental information on its website at http://www.rockwellautomation.com/rockwellautomation/about-us/sustainability-ethics/product-environmental-compliance.page .

Allen-Bradley, ArmorBlock, CompactBlock, Guard I/O, GuardLogix, GuardMaster, POINT Guard I/O, Rockwell Automation, Rockwell Software, RSLinx, RSLogix, RSLogix 5000, RSNetWorx, RSView, Stratix, and Studio 5000 Logix Designer, are trademarks of Rockwell Automation, Inc.

CIP Safety, ControlNet, DeviceNet and EtherNet/IP are trademarks of ODVA, Inc. Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş., Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400