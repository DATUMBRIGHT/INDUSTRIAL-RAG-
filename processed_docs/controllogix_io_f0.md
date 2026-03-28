## Studio 5000 License Portal

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Important user information

Read this document and the documents listed in the additional resources section about installation, configuration, and operation of this equipment before you install, configure, operate, or maintain this product. Users are required to familiarize themselves with installation and wiring instructions in addition to requirements of all applicable codes, laws, and standards.

Activities including installation, adjustments, putting into service, use, assembly, disassembly, and maintenance are required to be carried out by suitably trained personnel in accordance with applicable code of practice. If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

If this equipment is used in a manner not specified by the manufacturer, the protection provided by the equipment may be impaired.

In no event will Rockwell Automation, Inc. be responsible or liable for indirect or consequential damages resulting from the use or application of this equipment.

The examples and diagrams in this manual are included solely for illustrative purposes. Because of the many variables and requirements associated with any particular installation, Rockwell Automation, Inc. cannot assume responsibility or liability for actual use based on the examples and diagrams.

No patent liability is assumed by Rockwell Automation, Inc. with respect to use of information, circuits, equipment, or software described in this manual.

Reproduction of the contents of this manual, in whole or in part, without written permission of Rockwell Automation, Inc., is prohibited.

Throughout this manual, when necessary, we use notes to make you aware of safety considerations.

<!-- image -->

WARNING: Identifies information about practices or circumstances that can cause an explosion in a hazardous environment, which may lead to personal injury or death, property damage, or economic loss.

<!-- image -->

Important:

ATTENTION: Identifies information about practices or circumstances that can lead to personal injury or death, property damage, or economic loss. Attentions help you identify a hazard, avoid a hazard, and recognize the consequence

Identifies information that is critical for successful application and understanding of the product.

Labels may also be on or inside the equipment to provide specific precautions.

<!-- image -->

SHOCK HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that dangerous voltage may be present.

<!-- image -->

<!-- image -->

BURN HAZARD: Labels may be on or inside the equipment, for example, a drive or motor, to alert people that surfaces may reach dangerous temperatures.

ARC FLASH HAZARD: Labels may be on or inside the equipment, for example, a motor control center, to alert people to potential Arc Flash. Arc Flash will cause severe injury or death. Wear proper Personal Protective Equipment (PPE). Follow ALL Regulatory requirements for safe work practices and for Personal Protective Equipment (PPE).

## Summary of changes

This manual includes new and updated information. Use these reference tables to locate changed information.

Grammatical and editorial style changes are not included in this summary.

## Global changes

None in this release.

## New or enhanced features

None in this release.

## Table of contents

| Preface                    | Studio 5000 environment ....................................................................................................   9  9                      |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create and manage licenses | Additional resources   .  .............................................................................................................   9  9           |
|                            | Legal notices   .  ........................................................................................................................  10          |
|                            | Chapter 1 Introduction   .  ........................................................................................................................  13 |
| and accounts               | Create licenses   .  .....................................................................................................................  13           |
|                            | Create license types   .  ....................................................................................................  13                       |
|                            | Create recipient types   .  ................................................................................................  14                         |
|                            | Create an order  ...........................................................................................................  16                         |
|                            | Create a copy of an order  r .  ..........................................................................................  17                           |
|                            | Cancel an order  r .  ...........................................................................................................  19                    |
|                            | Filter the orders list   .  ....................................................................................................   2  20                 |
|                            | Download the orders list as a CSV file   .  ...................................................................   2  21                                  |
|                            | Manage license containers   .  ................................................................................................   2  21                  |
|                            | Revoke and reinstate license containers   .  .................................................................   2  21                                   |
|                            | Manage administrator accounts   .  ......................................................................................   2  22                        |
|                            | Change an administrator password  d  ........................................................................   2  23                                    |
|                            | Log out of the License Portal  l .  ...................................................................................   2  24                          |
|                            | Chapter 2                                                                                                                                                |
| Retrieve and view licenses | Retrieve a license for a locally connected license container  r  .......................................   2  25                                         |
|                            | Retrieve a license for a license container not connected locally  y .  ................................   2                                              |
|                            | Retrieve a license using an email link  k .  ..............................................................................   2  26                      |
|                            | 27                                                                                                                                                       |
|                            | Create a license request file   .  .......................................................................................   2  29                       |

## Studio 5000 environment

## Additional resources

The Studio 5000 Automation Engineering &amp; Design Environment® combines engineering and design elements into a common environment. The first element is the Studio 5000 Logix Designer® application. The Logix Designer application is the rebranding of RSLogix 5000® software and will continue to be the product to program Logix 5000™ controllers for discrete, process, batch, motion, safety, and drive -based solutions.

<!-- image -->

The Studio 5000® environment is the foundation for the future of Rockwell Automation® engineering design tools and capabilities. The Studio 5000 environment is the one place for design engineers to develop all elements of their control system.

These documents contain additional information concerning related Rockwell Automation products.

| Resource                                                                      | Description                                                                         |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Industrial Automation Wiring and Grounding Guidelines , publication 1770-4.1  | Provides general guidelines for installing a Rockwell Automation industrial system. |
| Product Certifications webpage, available at http://ab.rockwellautomation.com | Provides declarations of conformity, certificates, and other certification details. |

You can view or download publications at http://www.rockwellautomation.com/literature . To order paper copies of technical documentation, contact your local Rockwell Automation distributor or sales representative.

## Legal notices

## Copyright notice

Copyright © 2019 Rockwell Automation Technologies, Inc. All Rights Reserved. Printed in USA.

This document and any accompanying Rockwell Software products are copyrighted by Rockwell Automation Technologies, Inc. Any reproduction and/or distribution without prior written consent from Rockwell Automation Technologies, Inc. is strictly prohibited. Please refer to the license agreement for details.

## End User License Agreement (EULA)

You can view the Rockwell Automation End -User License Agreement ("EULA") by opening the License.rtf file located in your product's install folder on your hard drive.

## Open Source Licenses

The software included in this product contains copyrighted software that is licensed under one or more open source licenses. Copies of those licenses are included with the software. Corresponding Source code for open source packages included in this product are located at their respective web site(s).

Alternately, obtain complete Corresponding Source code by contacting Rockwell Automation via the Contact form on the Rockwell Automation website: http://www.rockwellautomation.com/global/about-us/contact/contact.page Please include "Open Source" as part of the request text.

## Trademark Notices

Allen -Bradley, ControlBus, ControlFLASH, Compact GuardLogix, Compact I/O, ControlLogix, CompactLogix, DCM, DH+, Data Highway Plus, DriveLogix, DPI, DriveTools, Explorer, FactoryTalk, FactoryTalk Administration Console, FactoryTalk Alarms and Events, FactoryTalk Batch, FactoryTalk Directory, FactoryTalk Security, FactoryTalk Services Platform, FactoryTalk View, FactoryTalk View SE, FLEX Ex, FlexLogix, FLEX I/O, Guard I/O, High Performance Drive, Integrated Architecture, Kinetix, Logix5000, Logix 5000, Logix5550, MicroLogix, DeviceNet, EtherNet/IP, PLC-2, PLC-3, PLC-5, PanelBuilder, PowerFlex, PhaseManager, POINT I/O, PowerFlex, Rockwell Automation, RSBizWare, Rockwell Software, RSEmulate, Historian, RSFieldbus, RSLinx, RSLogix, RSNetWorx for DeviceNet, RSNetWorx for EtherNet/IP, RSMACC, RSView, RSView32, Rockwell Software Studio 5000 Automation Engineering &amp; Design Environment, Studio 5000 View Designer, SCANport, SLC, SoftLogix, SMC Flex, Studio 5000, Ultra 100, Ultra 200, VersaView, WINtelligent, XM, SequenceManager are trademarks of Rockwell Automation, Inc.

Any Rockwell Automation logo, software or hardware product not mentioned herein is also a trademark, registered or otherwise, of Rockwell Automation, Inc.

## Other Trademarks

CmFAS Assistant, CmDongle, CodeMeter, CodeMeter Control Center, and WIBU are trademarks of WIBU -SYSTEMS AG in the United States and/or other countries. Microsoft is a registered trademark of Microsoft Corporation in t he United States and/or other countries. ControlNet is a trademark of ControlNet International. DeviceNet is a trademark of the Open DeviceNet Vendors Association (ODVA). Ethernet/IP is a trademark of ControlNet International under license by ODVA.

All other trademarks are the property of their respective holders and are hereby acknowledged.

## Warranty

This product is warranted in accordance with the product license. The product's performance may be affected by system configuration, the application being performed, operator control, maintenance, and other related factors. Rockwell Automation is not responsible for these intervening factors. The instructions in this document do not cover all the details or variations in the equipment, procedure, or process described, nor do they provide directions for meeting every possible contingency during installation, operation, or maintenance. This product's implementation may vary among users.

This document is current as of the time of release of the product; however, the accompanying software may have changed since the release. Rockwell Automation, Inc. reserves the right to change any information contained in this document or the software at any time without prior notice. It is your responsibility to obtain the most curr ent information available from Rockwell when installing or using this product.

## Environmental compliance

Rockwell Automation maintains current product environmental information on its website at http://www.rockwellautomation.com/rockwellautomation/about-us/sustainabili ty -ethics/product-environmental-compliance.page

## Contact Rockwell Automation

Customer Support Telephone — 1.440.646.3434

Online Support — http://www.rockwellautomation.com/support/

## Introduction

## Create licenses

## Create license types

## Create and manage licenses and accounts

This chapter describes how to:

- Create and manage licenses
- Manage license containers
- Manage administrator accounts

When creating licenses in the License Portal, complete three main steps:

- Create license types: Use license types to group the Logix Designer p project components that are protected by licenses. For example, you could create license types based on functionality, geography, product, or customer.
- Create recipient types: Use recipient types to assign license permissions to user profiles.
- Create an order: Create an order to deliver a license ticket to the end user. End users enter the ticket number when they retrieve a license.

## See also

Create recipient types on p page 14

Create an order on p page 16

Create a copy of an order on p page 17

Cancel an order on p page 19

Use license types to categorize the licenses that protect Logix Designer project components. Create license types based on criteria such as functionality, geography, p product, or customer. For example, for Customer XYZ, create a license type named Customer\_XYZ and use those licenses to protect components only in Customer XYZ's Logix Designer projects. See the Logix Designer online help for instructions on applying license protection.

## Create recipient types

Create and edit license types on the License Types p page, which provides a list of existing license types.

## To create a license type:

1. On the License Portal Home p page, select License Types .
2. On the License Types p page, select Create License Types .
3. In the Name box, type a name for the license type and click Create. Each license type requires a unique name that:
- Contains a maximum of 40 characters.
- Does not contain spaces.
- Contains only letters, numbers, or underscores.
- Does not begin with a number.
- Does not contain more than one underscore in a row.

<!-- image -->

The new license type appears in the list of existing license types. The portal assigns each license type a license type number, which consists of the firm code and a product code, separated by a colon .

Use recipient types to assign permissions to user profiles. Create and edit recipient types on the Recipient Types p page, which provides a list of existing recipient types and their associated permissions.

## To create a recipient type:

1. On the License Portal Home p page, select Recipient Types .

2. On the Recipient Types p page, select Create Recipient Types .
3. In the Name box, type a name for the recipient type. Each recipient type requires a unique name that:
- Contains a maximum of 40 characters.
- Does not contain spaces.
- Contains only letters, numbers, or underscores.
- Does not begin with a number.
- Does not contain more than one underscore in a row.
4. In the Permissions area, select the permissions to assign to the license for the recipient type. W When selecting a permission, any additional permissions that are required are selected automatically.
- Use. Allows the recipient to open, import, upload, or download a project containing content protected with the corresponding license type. This is the minimum permission available for a license.
- View. Allows the recipient to view routine logic for the component, or local tags for an Add-On Instruction. View also enables printing, searching, and cross reference. Editors and properties dialog boxes for the component are limited to read-only mode.
- Edit. Allows the recipient to edit a routine or Add-On Instruction. When you select Edit , V View w is selected automatically.
- Copy contents. Allows the recipient to copy the logic and tags contained in the protected routine or Add-On Instruction. Note that this permission applies only to the contents of the component; the component itself can be copied with or without the license. When you select Copy contents , V View w and Edit are selected automatically.

<!-- image -->

## Create an order

- Protect. Allows the recipient to apply or remove license protection from components protected by this license type. When you select Protect , V View w and Edit are selected automatically.
- Export in clear text. Allows the recipient to export the routine or Add -On Instruction in a non -encrypted format. When you select Export in clear text , V View w is selected automatically.

## 5. Click Create .

## See also

## Create license types on p page 13

Creating an order, also known as a transaction, generates a license ticket, ticket number, and retrieval URL. The ticket number and retrieval URL are used when a recipient needs to retrieve a license. Once the ticket number is used to retrieve a license, the ticket is marked as used and cannot be entered again to retrieve a license.

Use the Orders p page to create new orders and see the list of existing orders and their status.

## To create an order:

1. On the License Portal Home p page, click Orders .
2. On the Orders p page, click Create New Order .
3. (Optional) In the Name box, type the name of the license recipient. Names can contain up to 40 characters.
4. (Optional) In the Company y box, type the name of the recipient's company. Company names can contain up to 40 characters.
5. (Optional) To delete all existing licenses from the recipient's license container when this license is retrieved, select Remove all previous container contents .

<!-- image -->

## Create a copy of an order

6. Click Add license .
7. Select a license type.
8. Select the permissions to assign to the license, or select a recipient type to assign the permissions contained in that type.
9. (Optional) Select Allow user over network k to enable the license for network use.

Important:

This setting is required if users intend to share the license privileges on a network.

10. (Optional) Select License expires on to set an expiration date for the license. Select a date and time for the expiration.
11. Click Add .
12. Click Finish Order r and review the license configuration.
13. Click Create Order .
14. Under Retrieval Details, note the Retrieval URL and the Ticket number for the order. The recipient needs this information to retrieve the license. Select Email Recipient to send this information to the recipient in an email.

## See also

Cancel an order on p page 19

Filter the Orders list on p page 20

Download the Orders list as a CSV file on p page 21

Make copies of existing orders to save time.

## To create a copy of an order:

1. On the License Portal Home p page, select Orders .
2. In the list of orders, select the Order ID of the order to copy.

3. On the Order details p page, select Copy .
4. In the Name box, type the name of the license recipient. The recipient name can contain up to 40 characters.
5. (Optional) In the Company y box, type the name of the recipient's company. The company name can contain up to 40 characters.
6. (Optional) To delete all existing licenses from the recipient's license container when this license is retrieved, select Remove all previous container contents .
7. (Optional) Select Add License to add additional licenses to this order.
8. (Optional) Select the pencil icon in the Edit column to change other license settings, such as the License Type, Recipient Type, permissions, or license expiration date.
9. (Optional) Select the Delete icon to delete a license from the order.
10. Select Finish Order r and review the license configuration.
11. Select Create Order .
12. Under Retrieval Details, note the Retrieval URL and the Ticket number for the order. The recipient needs this information to retrieve the license. Select Email Recipient to send this information to the recipient in an email.

<!-- image -->

## See also

Create an order on p page 16

Filter the Orders list on p page 20

## Cancel an order

Cancel orders that are no longer needed. Orders that have been retrieved cannot be canceled.

## To cancel an order:

1. On the License Portal Home p page, click Orders .
2. In the list of orders, click the Order ID of the order you want to cancel.
3. On the Order details p page, click Cancel .
4. Click Yes to confirm the cancelation. On the Orders p page, Canceled appears in the Retrieved column for the canceled order.

<!-- image -->

## See also

Create an order on p page 16

## Filter the orders list

Filter the orders list to find orders based on criteria such as recipient, company, or date of retrieval.

## To filter the orders list:

1. On the Orders p page, select Filter Orders .
2. Select the filter criteria to apply to the list:
- To filter by keyword, in the Keyword menu, choose the field to search for the keyword, either Order ID , Recipient , Company , Container ID , License Type, or Recipient Type, and then type the keyword in the space provided.
- To filter on order dates, enter date ranges in the Creation Date and Retrieval Date boxes.
- To filter on order status, select or clear the check boxes for Retrieved , Not Retrieved , No Receipt, or Canceled .
3. Select Apply Filters .
4. To remove the filters, select Clear All .

<!-- image -->

## See also

Create an order on p

```
page 16
```

Cancel an order on p page 19

Create a copy of an order on p page 17

## Download the orders list as a CSV file

## Manage license containers

## Revoke and reinstate license containers

Download the orders list as a CSV file for use with spreadsheet applications.

## To download the orders list as a CSV file:

1. On the Orders p page, select Export to CSV .
2. Save the file and open it in a spreadsheet application.

<!-- image -->

## See also

Create an order on p page 16

Create a copy of an order on p page 17

Filter the orders list on p page 20

Licenses are retrieved onto license containers. A license container can be either a USB (CmStick) or an SD card (CmCard). If a license container is lost or broken, disqualify it from use by revoking it. A revoked license container cannot be used to retrieve a license. A license container can also be reinstated to return it to active status.

A revoked license container cannot be used to retrieve a license. The most common reason to revoke a license container is when it is lost or broken.

Revoked license containers can be reinstated to return them to use .

## To revoke a license container:

1. On the License Portal Home p page, select Revoked Containers .

## Manage administrator accounts

## 2. Click Revoke a Container .

<!-- image -->

3. In the Revoke Container r dialog box, in the Enter container serial number r box, type the serial number of the license container to revoke .

Select View Details to see additional information about the license container to make sure you selected the correct one.

4. (Optional) In the Comments box, type notes or additional information.
5. Select Revoke .

## To reinstate a license container:

1. On the License Portal Home p page, select Revoked Containers .
2. In the list of license containers, select the pencil icon in the Reinstate column for the license container to reinstate.
3. In the Reinstate Container r dialog box, select Yes .

Use the Admin Accounts p page to create, edit, and delete administrator accounts. All users of the License Portal are administrators.

## To manage administrator accounts:

1. On the License Portal Home p page, select Accounts .

<!-- image -->

## Change an administrator password

2. To create an administrator account, select Create Admin Account and enter the administrator's username and email address.
3. Select Create. A password is automatically generated for the new account and is sent to the new user's email address.
4. To edit the email address for an account, click the pencil icon in the Edit column. Enter the new email address.
5. To delete an account, click the trash can icon in the Delete column.

## See also

Log out of the License Portal on p page 24

Manage license containers on p page 21

Create licenses on p page 13

Follow these steps to change an administrator password.

## To change a password:

1. Point to the user name at the top of the page and select Change Password .
2. In the Current Password box, type the current password.
3. In the New Password box, type the new password. The password must contain at least eight characters.
4. In the Confirm New Password box, type the new password again.
5. Click Save .

<!-- image -->

## See also

Manage administrator accounts on p page 22

Log out of the License Portal on p page 24

## Log out of the License Portal

To log out of the License Portal, point to the user name at the top of the page and select Logout .

<!-- image -->

See also

Manage administrator accounts on p page 22

## Introduction

## Retrieve a license for a locally connected license container

## Retrieve and view licenses

This chapter describes how to:

- Retrieve licenses
- Use the License Viewer Client

Use the License Portal to retrieve a license for a license container connected to a USB port on the computer.

## To retrieve a license for a locally connected license container:

1. Open the License Portal.
2. Enter the ticket number in the Ticket number r box.
3. Click Find Ticket .
4. Click Retrieve Licenses .
5. On the Choose License Container r menu, select the license container where the license should be downloaded. Plug the license container can be plugged into any USB port on the computer.

<!-- image -->

## Retrieve a license using an email link

<!-- image -->

Click the Refresh icon to discover license containers recently plugged into the computer.

<!-- image -->

- Tip: Some licenses are configured to remove all other licenses from the license container when they are downloaded. Contact the license administrator if the existing licenses on the license container should not be deleted.
6. Click Retrieve Licenses .
7. When the license transfer is complete, click OK .

Users who are not administrators can use the License Portal to retrieve a license by clicking the link in an email notification.

## To retrieve a license using an email link:

1. Click the link in the email to open the License Portal.
2. Click Retrieve Licenses .
3. On the Choose License Container r menu, select the license container that will contain the license. The license container can be plugged into any USB port on the computer.

<!-- image -->

<!-- image -->

Click the Refresh icon to discover license containers recently plugged into the computer.

## Retrieve a license for a license container not connected locally

- Tip: Some licenses are configured to remove all other licenses from the license container when they are downloaded. Contact your license administrator if the existing licenses on the license container should not be deleted.
4. Click Retrieve Licenses .
5. When the license transfer is complete, click OK .

Use the License Portal to retrieve a license for a license container that is not connected to the computer. A license request file is required to retrieve a license for a license container that is not connected locally. After transferring the license file to the remote computer, generate a receipt that can be uploaded to the license portal to verify that the license was delivered to the remote license container .

## To retrieve a license for a license container not connected locally:

1. On the remote computer, use the CodeMeter™ application to create a license request file.
2. Copy the license request file to the local computer.
3. Open the License Portal.
4. Enter the ticket number in the Ticket number r box.
5. Select Find Ticket .
6. Select Retrieve Licenses .

## 7. Select Remote Retrieval .

<!-- image -->

8. Select Browse to find the license request file on the computer.
9. Select Upload Request and Continue Now .
10. Select Download License Update File Now .
11. When the license transfer is complete, click OK K and save the license file on the computer. License file names use WibuCmRAU as the extension; for example, license.WibuCmRAU.
12. Copy the license file onto the remote computer. Double-click the file on the remote co mputer to add it to the license container connected to that computer.
13. On the remote computer, open the CodeMeter Control Center™ application.
14. Select the license container plugged into the remote computer and click License Update .
15. In the CMFAS Assistant™ , click Create receipt .
16. Save the receipt file and transfer it to the local computer. The receipt file also uses WibuCmRAU as the extension; for example, receipt.WibuCmRAU.

## Create a license request file

17. In the license portal on the local computer, click Upload Receipt .

## See also

Retrieve a license for a locally connected license container on p page 25

To retrieve a license for a license container connected to a remote computer that does not have Internet access, create a license request file. Use the CodeMeter Control Center r application on the remote computer to create a license request file, and then transfer the license request file from the remote computer to the local computer.

## To create a license request file:

1. Log on to the remote computer. The remote computer must have a license conta iner plugged into a USB port.
2. Open the CodeMeter Control Center r application on the remote computer. To open the application, click the CodeMeter icon in the system tray, or navigate to the C:\Program Files (x86)\CodeMeter\Runtime\bin folder and run the CodeMeter.exe file.
3. Select the license container plugged into the remote computer and click License Update .
4. In the CMFAS Assistant, click Create license request .
5. Choose either Extend existing license or A Add license of a new producer:
- If the license container already contains a license with the desired Firm Code, choose Extend existing license .
- If the license container does not contain a license with the desired Firm Code, choose Add license of a new producer .
6. Click Next, and either select the desired Vendor (Firm Code) to extend an existing license, or type the desired Firm Code to add a new license vendor.
7. Type a file name for the license request file.
8. Click Commit to save the license request file.
9. Transfer the license request file to the local computer, which has an Internet connection.
10. Follow the steps for retrieving a license for a license container not connected locally.

## Rockwell Automation support

Use the following resources to access support information.

| Technical Support Center                         | Knowledgebase Articles, How - to Videos, FAQs, Chat, User Forums, and Product Notification Updates                    | https://rockwellautomation.custhelp.com                                    |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Local Technical Support Phone Numbers            | Locate the phone number for your country.                                                                             | http://www.rockwellautomation.com/global/support/get-support-now. page     |
| Direct Dial Codes                                | Find the Direct Dial Code for your product. Use the code to route your call directly to a technical support engineer. | http://www.rockwellautomation.com/global/support/direct-dial.page          |
| Literature Library                               | Installation Instructions, Manuals, Brochures, and Technical Data.                                                    | http://www.rockwellautomation.com/global/literature-library/overvie w.page |
| Product Compatibility and Download Center (PCDC) | Get help determining how products interact, check features and capabilities, and find associated firmware.            | http://www.rockwellautomation.com/global/support/pcdc.page                 |

## Documentation feedback

Your comments will help us serve your documentation needs better. If you have any suggestions on how to improve this document, complete the How Are We Doing? form at http://literature.rockwellautomation.com/idc/groups/literature/documents/du/ra-du002\_-en-e.pdf. f.

Rockwell Automation maintains current product environmental information on its website at http://www.rockwellautomation.com/rockwellautomation/about-us/sustainability-ethics/product-environmental-compliance.page .

Allen -Bradley, Rockwell Automation, and Rockwell Software are trademarks of Rockwell Automation, Inc.

Trademarks not belonging to Rockwell Automation are property of their respective companies.

## www.rockwellautomation.com

## Power,ControlandInformationSolutionsHeadquarters

Americas:RockwellAutomation,1201SouthSecondStreet,Milwaukee,WI53204-2496USA,Tel:（1)414.382.2000,Fax:（1)414.382.4444 Europe/MiddleEast/Africa:Rockwell AutomationNV,Pegasus Park,DeKleetlaan 12a,1831Diegem,Belgium,Tel:(32)2663 0600,Fax:(32)2663 0640 Asia Pacific:Rockwell Automation,Level14,Core F,Cyberport 3,100 Cyberport Road,Hong Kong,Tel:(852)28874788,Fax:(852)25081846