## ControlNet to EtherNet/IP Migration

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

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

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

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential MonthArc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective Equipment (PPE).

## Table of Contents

|                               | Preface . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . .                                            | . . . . . . . . . . . . . . . . . . . . . . . . . . 5      |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
|                               | Integrated Architecture Tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5           |                                                            |
|                               | Migration Services. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 |                                                            |
|                               | Additional Resources . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                     | . . . . . . . . . . . . . . . . 5                          |
|                               | Chapter 1                                                                                                       |                                                            |
| Overview                      | Network Overviews . . . . .  . . . . . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . . . . 7                      |
|                               | ControlNet Network Overview .                                                                                   | . . . . . . . . . . . . . . .  . . . . . . . . . . . . . 7 |
|                               | EtherNet/IP Network Overview.                                                                                   | . . . . . . . . . . . . . . .  . . . . . . . . . . . . . 7 |
|                               | Network Infrastructure Comparisons. . . . . . . . . . . . . . . . . . . . . . . . . . . . 8                     |                                                            |
|                               | Linear Topology. . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                         | . . . . . . . . . . . . . . . . 8                          |
|                               | Star Topology . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . 9                          |
|                               | Ring Topology . . . . . . . . . . .  . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . . 10                         |
|                               | Redundant Media Topology. . .  . . . . . . . . . . . . . . .                                                    | . . . . . . . . . . . . . . 11                             |
|                               | Infrastructure Components . .  . . . . . . . . . . . . . . . .                                                  | . . . . . . . . . . . . . . 13                             |
|                               | Network Comparison . . . . . . . .  . . . . . . . . . . . . . . . . .                                           | . . . . . . . . . . . . . . . . 14                         |
|                               | Network Performance . . . . . .  . . . . . . . . . . . . . . . .                                                | . . . . . . . . . . . . . . . 14                           |
|                               | Network Configuration. . . . .  . . . . . . . . . . . . . . . .                                                 | . . . . . . . . . . . . . . . 14                           |
|                               | Chapter 2                                                                                                       |                                                            |
| Products                      | Product Replacements . . .  . . . . . . . . . . . . . . . . . . . .                                             | . . . . . . . . . . . . . . . . . . 15                     |
|                               | Controllers . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                        | . . . . . . . . . . . . . . . . . 16                       |
|                               | I/O Module Interfaces . . . . . .  . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . 18                           |
|                               | Drives . . . . . . . . . . . . . . . .  . . . . . . . . . . . . . . . . . . .                                   | . . . . . . . . . . . . . . . . . 19                       |
|                               | Operator Interfaces . . . . . . . .  . . . . . . . . . . . . . . . . .                                          | . . . . . . . . . . . . . . . 20                           |
|                               | Linking Devices . . . . .  . . . . . . . . . . . . . . . . . . . .                                              | . . . . . . . . . . . . . . . . . . 20                     |
|                               | Computer Interfaces. . . . . . . . . . . . . . .                                                                | . . . . . . . . . . . . .  . . . . . . . . . . . 20        |
|                               | Chapter 3                                                                                                       |                                                            |
| Migrate ControlNet Network to | Application Considerations .  . . . . . . . . . . . . . . . . . .                                               | . . . . . . . . . . . . . . . . . 21                       |
| EtherNet/IP Network           | Migration Process . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . . 22                       |
|                               | Migration Example . . . . . . . . . .  . . . . . . . . . . . . . . . . . .                                      | . . . . . . . . . . . . . . . . 23                         |

## Notes:

## Integrated Architecture Tools

## Migration Services

## Additional Resources

The Integrated Architecture® tools can help you plan and configure a system, as well as migrate system architectures. For more information, go to: http://www.rockwellautomation.com/rockwellautomation/products-technologi es/integrated-architecture/tools/overview.page?

Throughout the product lifecycle, as products mature, Rockwell Automation is there as your partner to help you get the most out of your current equipment, to help you determine your next steps, and to help you lay out a plan for the transition to newer technology.

Whether you choose to migrate all at once or use our unique, phased approach to help minimize the costs, risks, and complexities involved with managing legacy products and systems, Rockwell Automation has the tools and the experience to guide you through the transition.

For more information, see Migration Solutions Brochure, publication MIGRAT-BR002 .

These documents contain additional information concerning related products from Rockwell Automation.

| Resource                                                                                              | Description                                                                                                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ControlNet Coax Media Planning and Installation Guide, publication CNET-IN002                         | Describes the required components of a ControlNet® coax media system.                                                                                                                                                                     |
| ControlNet Fiber Media Planning and Installation Guide, publication CNET-IN001                        | Describes the components and topologies for creating a ControlNet fiber media system.                                                                                                                                                     |
| ControlNet Media System Components List, publication AG-PA002                                         | Lists category numbers and specifications for the components that comprise the ControlNet media system.                                                                                                                                   |
| ControlNet Accessory Specifications, publication 1786-TD008                                           | Provides technical specifications for ControlNet accessories.                                                                                                                                                                             |
| EtherNet/IP Network Devices, publication ENET-UM006                                                   | Describes how to configure and use EtherNet/IP™ devices to communicate on the EtherNet/IP network.                                                                                                                                        |
| Converged Plantwide Ethernet (CPwE) Design and Implementation Guide publication ENET-TD001            | A collaborative development effort from Cisco Systems and Rockwell Automation. It is built on, and adds to, design guidelines from the Cisco® Ethernet-to-the-Factory (EttF) solution and the Rockwell Automation Integrated Architecture |
| Industrial Automation Wiring and Grounding Guidelines, publication 1770-4.1                           | Provides general guidelines for installing a Rockwell Automation industrial system.                                                                                                                                                       |
| Product Certifications website, http://www.rockwellautomation.com/global/certification /overview.page | Provides declarations of conformity, certificates, and other certification details.                                                                                                                                                       |

You can view or download publications at http://www.rockwellautomation.com/global/literature-library/overview.page .

To order paper copies of technical documentation, contact your local Allen-Bradley distributor or Rockwell Automation sales representative.

## Notes:

## Network Overviews

## Overview

This document provides information to migrate from an existing ControlNet® network to an EtherNet/IP™ network.

Unlike information networks, industrial control networks place a greater burden on the designers of system components. An industrial control network requires fast and guaranteed throughput to control machines and manufacturing processes effectively. Additionally, some industrial environments require a greater level of performance due to the elevated levels of noise and contaminants common to those installations.

## ControlNet Network Overview

The ControlNet network provides high-speed transmission of time-critical I/O and interlocking data and messaging data. This data transfer capability enhances I/O performance and peer-to-peer communication in any system or application.

The ControlNet network remains unaffected as devices are connected or disconnected from it. This data transfer capability delivers a dependable, synchronized, and coordinated real-time performance.

## EtherNet/IP Network Overview

EtherNet/IP networks offer a comprehensive suite of messages and services for many automation applications. This open network standard uses standard Ethernet communication products to support real-time I/O messaging, information exchange, and general messaging.

EtherNet/IP networks support CIP Safety™ applications. Such support makes the simultaneous transmission of safety and standard control data and diagnostics information over a common network possible. EtherNet/IP networks also support CIP Motion™ and CIP Security™. These features are not supported in ControlNet.

## Network Infrastructure Comparisons

## Linear Topology

In a linear topology, all nodes of the network are connected to a common transmission medium, typically referred to as the bus or trunk. The bus or trunk has exactly two endpoints. All data that is transmitted in between nodes is transmitted over this common transmission medium.

This bus/trunk is terminated at both ends and the signal is halted when it reaches the end.

Figure 1 - ControlNet

<!-- image -->

Figure 2 - EtherNet/IP

<!-- image -->

The EtherNet/IP linear topology requires embedded EtherNet/IP in the device, a communication module, or separate ETAP.

## Star Topology

In star topology, every device is connected to a central node called hub or switch. The network does not necessarily have to resemble a star to be classified as a star network, but all devices on the network must be connected to one central device. The ControlNet star topology requires the use of a repeater

Figure 3 - ControlNet

<!-- image -->

The EtherNet/IP star topology requires the use of a switch.

For available Stratix® switches see publication 1783-TD001, Stratix Ethernet Device Specifications.

## Ring Topology

In this topology, all devices are connected to cable that forms a closed loop. Transmissions from each device travel around the loop and are blocked when it reaches the original sending repeater.

A ring topology provides additional resiliency by being able to survive a single break in the cable.

<!-- image -->

A ring topology is only supported using the 1786-RPFRL and 1786-RPFRXL ControlNet Repeater modules.

See Knowledgebase ID 32215, ControlNet Ring Topology, Allowable Configuration Using Repeaters, for examples of allowable configurations.

Figure 6 - EtherNet/IP DLR

<!-- image -->

See EtherNet/IP Device Level Ring, Publication ENET-AT007, for more information.

## Redundant Media Topology

Redundant media provides maximum resiliency by providing duplicate paths for the transmission of data. When using redundant cabling, each ControlNet node always simultaneously transmits/receives on both channel A and channel B. Each individual node decides, independent of other nodes, which single channel it uses incoming data from. This decision is based on which channel historically has provided the best data over time.

Figure 7 - ControlNet

<!-- image -->

Figure 8 - EtherNet/IP Parallel Redundancy Protocol (PRP)

<!-- image -->

This architecture requires devices that support Parallel Redundancy Protocol as end nodes.

EtherNet/IP redundancy is more flexible than ControlNet media redundancy because the redundant PRP networks do not have to be the same topology. For example, one network can be a star and one network can be a ring. With EtherNet/IP PRP, it is possible to have devices on only one of the two networks. It is also possible to get non-PRP devices onto both LANs by using a RedBox.

See EtherNet/IP Parallel Redundancy Protocol, publication ENET-AT006, for more information.

## Infrastructure Components

| ControlNet Component                                                                                                                                                                                                                                                                | EtherNet/IP Component                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RG-6 quad-shield coaxial cable • 1786-RG6F/A high flex • 1786-RG6 standard Fiber-optic 200 micron cable • 1786-FS10 10 m (32.8 ft) • 1786-FS20 20 m (65.6 ft) • 1786-FS60 60 m (196.8 ft) • 1786-FS100 100 m (328.1 ft) • 1786-FS200 200 m (656.2 ft) • 1786-FS300 300 m (948.2 ft) | Commercially available media: • Fiber-optic using SFPs and same fiber as ControlNet • Copper STP (shielded twisted pair) • Copper UTP (unshielded twisted pair) Existing fiber cables can be used but may require new connectors and new SFPs. See 1783-TD001 for options |
| Repeater • 1786 RPA repeater adapter • 1786-RPCD coax repeater • 1786-RPFS short-distance fiber repeater • 1786-RPFM medium-distance fiber repeater • 1786-RPFRL long-distance fiber repeater • 1786-RPFRXL extra-long-distance fiber repeater                                      | Stratix Switch 1783 series switches See 1783-TD001 for options                                                                                                                                                                                                            |
| Coaxial Tap • 1786-TPR Right-angle T-tap • 1786-TPS Straight T-tap • 1786-TPYR Right-angle Y-tap • 1786-TPYS Straight Y-tap • 1786-TCT2BD1 IP67 tap                                                                                                                                 | —                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                     | — • 1783-ETAP twisted-pair tap • 1783-ETAP1F fiber tap • 1783-ETAP2F dual-port fiber tap                                                                                                                                                                                  |

For a list of all ControlNet media components, see ControlNet Media System Components List, publication AG-PA002 .

## Network Comparison

## Network Performance

EtherNet/IP has higher bandwidth than ControlNet. ControlNet is a 5 Mbps network, whereas EtherNet/IP is typically a 100 Mbps or 1 Gbps network. This bandwidth translates to 20 to 200 times the data rate. Because ControlNet is a bus, traffic is seen at all points on the network at all times. The use of switches in Ethernet allows traffic to be confined only to the devices that need to receive that traffic.

ControlNet has a capacity of 99 nodes per network with the use of repeaters. Without repeaters, the maximum number of nodes on one ControlNet network is 48. The number of nodes supported on an EtherNet/IP network is only limited by the number of IP addresses available in the network.

## Network Configuration

|                               | ControlNet                                                                                                               | EtherNet/IP                                                                                |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Software                      | RSNetWorx™ for ControlNet (required)                                                                                     | FactoryTalk® Network Manager™ (optional) Integrated Architecture® Builder (IAB) (optional) |
| Items Requiring Configuration | ControlNet Network Keeper ControlNet Network Update Time Scheduled Maximum Node Address Unscheduled Maximum Node Address | EtherNet/IP DLR Supervisor                                                                 |
| Communication                 | Scheduled I/O Unscheduled Messaging                                                                                      | UDP I/O TCP Messaging                                                                      |

## Product Replacements

## Products

This chapter contains information about the ControlNet® devices and the corresponding EtherNet/IP™ devices that replace them during a migration.

There are discontinued products that were supported on ControlNet network that do not have direct replacements on EtherNet/IP network. These devices are not mentioned in this document.

## IMPORTANT

There are other considerations when replacing hardware. Consult the appropriate technical documentation before replacing any hardware.

## IMPORTANT

The lifecycle status of the following products is subject to change. See the Product Lifecycle Status website for the most up-to-date information.

All of the replacements listed in this manual are engineered replacements. An engineered replacement is defined as follows:

A product or family that can be used to migrate an earlier product or family and requires engineering changes to existing applications.

An engineered replacement means that there is a form, fit, or function change of the application that is not backward compatible and that does not emulate the earlier product. It requires considerable changes to the application.

The migration solution requires engineering effort that requires additional software/hardware tools and products or architectural modifications. Rockwell Automation® services and/or third-party services are available to support Engineered replacements.

<!-- image -->

## Controllers

Replace the existing controller with either a controller with an embedded EtherNet/IP port (new controller), or the existing controller can be used with an EtherNet/IP network device (new scanner or adapter.)

CompactLogix and Compact GuardLogix Controllers

These ControlNet solutions are discontinued, replace with an EtherNet/IP solution.

| ControlNet Option                                                                                           | EtherNet/IP Option                                                                                                                                                  | Replacement Type      |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 1769 CompactLogix™ L4 and Compact GuardLogix® L4: • 1768-CNB • 1768-CNBR 1769-L32C, 1769-L35CR CompactLogix | 1769 CompactLogix or Compact GuardLogix 5370 controller with embedded EtherNet/IP 5069 CompactLogix or Compact GuardLogix 5380 controller with embedded EtherNet/IP | Engineered Engineered |

For more information see the following publications:

- CompactLogix Controllers Selection Guide, publication 1769-SG001
- Replacement Guidelines: Logix 5000™ Controllers Reference Manual, publication 1756-RM100
- EtherNet/IP Network Devices User Manual, publication ENET-UM006

## ControlLogix and GuardLogix Controllers

You do not have to replace the ControlLogix and GuardLogix controllers, however the ControlNet communication module must be replaced, as described in the following table.

| ControlNet Option                                                               | EtherNet/IP Option                                                                                                        | Replacement Type   |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------|
| 1756 ControlLogix and GuardLogix: • 1756-CNB • 1756-CNBR • 1756-CN2 • 1756-CN2R | 1756 ControlLogix and GuardLogix: • 1756-EN2F • 1756-EN2T • 1756-EN2TP • 1756-EN2TR • 1756-EN3TR • 1756-EN4TR • 1756-ENBT | Engineered         |

For more information see the following publications:

- ControlLogix Controllers Selection Guide, publication 1756-SG001
- Replacement Guidelines: Logix 5000 Controllers Reference Manual, publication 1756-RM100
- EtherNet/IP Network Devices User Manual, publication ENET-UM006

## FlexLogix Controllers

These ControlNet solutions are discontinued, replace with an EtherNet/IP solution.

| ControlNet Option                            | EtherNet/IP Option                                                                                                                                                  | Replacement Type   |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| FlexLogix™ L33 or L34: • 1788-CNC • 1788-CNF | 1769 CompactLogix or Compact GuardLogix 5370 controller with embedded EtherNet/IP 5069 CompactLogix or Compact GuardLogix 5380 controller with embedded EtherNet/IP | Engineered         |

## SLC Controllers

These ControlNet solutions are discontinued, replace with an EtherNet/IP solution.

| ControlNet Option                   | EtherNet/IP Option                                                                                                                                                  | Replacement Type   |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| 1747 SLC™: • 1747-SCNR • 1747-KFC15 | 1769 CompactLogix or Compact GuardLogix 5370 controller with embedded EtherNet/IP 5069 CompactLogix or Compact GuardLogix 5380 controller with embedded EtherNet/IP | Engineered         |

For more information see the following publications:

- CompactLogix System Selection Guide, publication 1769-SG001
- Replacement Guidelines: SLC Quick Migration Guide 1746-RM003
- EtherNet/IP Network Devices User Manual, publication ENET-UM006

## PLC-5 Controllers

These ControlNet solutions are discontinued, replace with an EtherNet/IP solution.

| ControlNet Option                                                             | EtherNet/IP Option                                                     | Replacement Type   |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------|--------------------|
| 1785 PLC-5®/20C 1785 PLC-5/40C 1785 PLC-5/80C 1785 PLC-5/46C protected memory | 1756 ControlLogix controller with an EtherNet/IP communication module. | Engineered         |

## I/O Module Interfaces

Replace the existing I/O module interfaces with I/O module interfaces with embedded EtherNet/IP ports.

## Distributed I/O

|                                       | ControlNet Option EtherNet/IP Option                                        | Replacement Type                                                                                              |
|---------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| POINT I/O™: • 1734-ACNR               | POINT I/O: • 1734-AENT • 1734-AENTR                                         | Engineered                                                                                                    |
| ArmorPOINT® I/O: • 1738-ACNR          | ArmorPoint I/O: • 1738-AENTR • 1738-AENT                                    | Engineered                                                                                                    |
| FLEX™ I/O: • 1794-ACN15 • 1794-ACNR15 | FLEX I/O: • 1794-AENT • 1794-AENTR                                          | Engineered                                                                                                    |
| FLEX™ I/O: • 1794-ACN15 • 1794-ACNR15 | 5094 FLEX 5000™ I/O (requires 5580 or 5380 controller and new I/O modules.) | Engineered                                                                                                    |
| SLC I/O: • 1747-ACN15 • 1747-ACNR15   | SLC I/O: • 1747-AENTR                                                       | Engineered                                                                                                    |
| SLC I/O: • 1747-ACN15 • 1747-ACNR15   | Compact 5000 I/O (requires 5069 CompactLogix 5380 controller)               | Engineered                                                                                                    |
| FLEX Ex™ I/O: • 1797-ACNR15           | FLEX: • 1794-AENTR and 1797-CEC and 1797-BIC (Class 1 Div 2 area)           | Engineered Additional considerations are required for hazardous locations. 1719 solutions are also available. |

For more information see the following publications:

- POINT I/O Modules Selection Guide, publication 1734-SG001
- ArmorPoint I/O Modules Selection Guide, publication 1738-SG001
- FLEX and FLEX Ex I/O Modules Selection Guide, publication 1794-SG002
- CompactLogix System Selection Guide, publication 1769-SG001

## Chassis-based I/O

| ControlNet Option                                                    | EtherNet/IP Option                                                                                                                                                                                            | Replacement Type   |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| 1756 ControlLogix I/O: • 1756-CNB • 1756-CNBR • 1756-CN2 • 1756-CN2R | 1756 ControlLogix I/O: • 1756-EN2F • 1756-EN2T • 1756-EN2TP • 1756-EN2TR • 1756-EN3TR • 1756-EN4TR • 1756-ENBT                                                                                                | Engineered         |
| 1771 I/O: • 1771-ACN • 1771-ACN15 • 1771-ACNR • 1771-ACNR15          | No direct 1771 I/O support It is recommended to move to a new I/O platform. For help migrating from 1771 I/O to 1756 I/O, see Digital/Analog Programmable Controller Wiring Systems, publication 1492-TD008 . | Engineered         |

For more information see the following publications:

- ControlLogix Controllers Selection Guide, publication 1756-SG001

## Drives

Replace the existing drive with either a drive with embedded EtherNet/IP ports (new drive), or an EtherNet/IP adapter for the drive (keep the existing drive but have a new adapter.)

## PowerFlex 4-Class Drives

|                                                                                   | ControlNet Option EtherNet/IP Option Replacement Type   |            |
|-----------------------------------------------------------------------------------|---------------------------------------------------------|------------|
| 22B PowerFlex® 40 AC drives with built-in ControlNet                              | PowerFlex Drive with embedded EtherNet/IP port          | Engineered |
| 22C PowerFlex 400 AC drive with built-in ControlNet PowerFlex Drive with embedded | EtherNet/IP port                                        | Engineered |
|                                                                                   | 22-COMM-C 22-COMM-E Engineered                          |            |

For more information see the following publications:

- PowerFlex Standard Drives Low Voltage Selection Guide, publication PFLEX-SG002

## PowerFlex 7-Class Drives

|                                    | ControlNet Option EtherNet/IP Option Replacement Type                  |
|------------------------------------|------------------------------------------------------------------------|
| 20-COMM-C (coax) 20-COMM-Q (fiber) | 20-COMM-E Engineered                                                   |
|                                    | 20-750-CNETC PowerFlex Drive with embedded EtherNet/IP port Engineered |

For more information see the following publications:

- PowerFlex Standard Drives Low Voltage Selection Guide, publication PFLEX-SG002

## PowerFlex DC Drives

| ControlNet Option   | EtherNet/IP Option Replacement Type   |            |
|---------------------|---------------------------------------|------------|
|                     | 20-COMM-C 20-COMM-E                   | Functional |

For more information see the following publications:

- PowerFlex Standard Drives Low Voltage Selection Guide, publication PFLEX-SG002

## Operator Interfaces

Replace the existing PanelView™ terminal with a PanelView terminal with an embedded EtherNet/IP port.

|                                                 | ControlNet Option EtherNet/IP Option                         | Replacement Type   |
|-------------------------------------------------|--------------------------------------------------------------|--------------------|
| 2711P PanelView Plus 6 terminals: • 2711P-RN15S | PanelView terminal with embedded EtherNet/IP port Engineered |                    |

For more information see the following publications:

- Visualization Solutions Selection Guide, publication VIEW-SG001

## Linking Devices

|             | ControlNet Option EtherNet/IP Option Replacement Type   |            |
|-------------|---------------------------------------------------------|------------|
| 1788-CN2DN  | 1788-EN2DNR                                             | Engineered |
| 1788-CN2FFR | 1788-EN2FFR                                             |            |
| 1788-CN2PAR | 1788-EN2PAR                                             |            |

For more information see the following publications:

- 1788 Linking Device Specifications, publication 1788-TD001

## Computer Interfaces

|               | ControlNet Option EtherNet/IP Option Replacement Type   |
|---------------|---------------------------------------------------------|
| 1784-PCIC(s)  | PC Ethernet port Engineered                             |
| 1784- PKTC(s) |                                                         |
| 1784-KTC(s)   |                                                         |

## Application Considerations

<!-- image -->

## Migrate ControlNet Network to EtherNet/IP Network

Not all nodes migrate from a ControlNet® solution to an EtherNet/IP™ solution. A migration solution requires engineering effort with additional software/hardware tools, products, and architectural modifications. Rockwell Automation® services are available to support engineered replacements.

You do not need to migrate all nodes at the same time. You can schedule migration phases. For example, during one phase of the migration, add an EtherNet/IP module to a controller chassis (see Figure 9.)

Figure 9 - EtherNet/IP Module Addition

Controller ControlNet EtheNet/IP

1734-ACN 1794-ACN PanelView™ 1336 Drive

## Migration Process

Then migrate a subset of ControlNet devices to the EtherNet/IP devices (see Figure 10.) At a later time, migrate the remaining devices.

Figure 10 - I/O Modules Moved to EtherNet/IP

<!-- image -->

The following steps are an overview of the migration process.

- Install new infrastructure - such as cables and switches. (no system interruptions)
- Acquire EtherNet/IP hardware (no system interruptions)
- Convert the I/O configuration tree (see Migration Example on page 23)
- Align tags to the new devices (rename)
- Add new logic, if needed, for new device platforms
- Verify any MSG paths (logic)
- Verify any produced/consumed tags (configuration)

Software changes can be made offline in advance if desired.

When you add an EtherNet/IP device to a project, use the same properties, including the name, as the ControlNet device. After you add the device, edit the name and the tags change accordingly. For example, if an original device name includes 'CNET', use the same name for the EtherNet/IP device, then later edit the name and other properties accordingly. This provides for a straightforward migration where the logic does not need to change; only the tags need to change.

## Migration Example

This example is an overview of the migration process. Highly engineered solutions require additional work due to difference in devices.

1. Open the original controller project.

<!-- image -->

2. Edit the project name in the controller properties and save as a new project, making no other changes. Keep both the original project and the new project open.
3. In the new project, delete all ControlNet devices. Start with individual I/O devices first, followed by any adapters or bridge modules. Deleting devices makes some rungs invalid due to deletion of I/O tags. Step 5 resolves the invalid rungs.

<!-- image -->

<!-- image -->

4. In the new project, add comparable EtherNet/IP devices. Do not add individual I/O modules at this time.
- Be sure that the new names and properties match the original ControlNet names and properties.
- Be sure that new chassis sizes match the original chassis sizes.
- Set other properties such as IP address as desired.

<!-- image -->

5. Drag and drop or copy and paste the individual I/O modules from the original project into the new project. This resolves the tag issues caused in Step 3.

<!-- image -->

6. Optionally, you can now re-name anything in the I/O tree as desired.

<!-- image -->

## Notes:

.

## Rockwell Automation Support

Use the following resources to access support information.

| Technical Support Center                         | Knowledgebase Articles, How-to Videos, FAQs, Chat, User Forums, and Product Notification Updates.                     | https://rockwellautomation.custhelp.com/                                   |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Local Technical Support Phone Numbers            | Locate the phone number for your country.                                                                             | http://www.rockwellautomation.com/global/support/get-support now.page                                                                            |
| Direct Dial Codes                                | Find the Direct Dial Code for your product. Use the code to route your call directly to a technical support engineer. | http://www.rockwellautomation.com/global/support/direct-dial.page          |
| Literature Library                               | Installation Instructions, Manuals, Brochures, and Technical Data.                                                    | http://www.rockwellautomation.com/global/literature-library/ overview.page |
| Product Compatibility and Download Center (PCDC) | Get help determining how products interact, check features and capabilities, and find associated firmware.            | http://www.rockwellautomation.com/global/support/pcdc.page                 |

## Documentation Feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete the How Are We Doing? form at http://literature.rockwellautomation.com/idc/groups/literature/ documents/du/ra-du002\_-en-e.pdf. f.

Rockwell Automation maintains current product environmental information on its website at http://www.rockwellautomation.com/rockwellautomation/about-us/sustainability-ethics/product-environmental-compliance.page . Allen-Bradley, ArmorPoint, CompactLogix, FactoryTalk Network Manager, FLEX, FLEX 5000, FLEX Ex, FLEXLogix, GuardLogix, Integrated Architecture Builder, Logix 5000, PanelView, PLC-5, POINT I/O ,PowerFlex, Rockwell Automation, Rockwell Software, RSNetWorx, SLC, and STRATIX are trademarks of Rockwell Automation, Inc..

CIP Safety, CIP Motion, CIP Security, ControlNet and EtherNet/IP are trademarks of ODVA Inc.

Cisco is a trademark of Cisco Systems, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

Rockwell Otomasyon Ticaret A.Ş., Kar Plaza İş Merkezi E Blok Kat:6 34752 İçerenköy, İstanbul, Tel: +90 (216) 5698400